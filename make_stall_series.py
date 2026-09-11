#!/usr/bin/env python3
"""
Turn simulation stall data into a ParaView time series.

    python make_stall_series.py network.vtp vessel_array.csv stall_data.csv

Writes a folder of numbered .vtp frames plus a .pvd that ties them to real
times. Open the .pvd in ParaView and the play button animates the run.

The stall columns are named after array elements (PV04, PV07, ...). Each is
looked up in the vessel array to find the geometry it belongs to, so the whole
vessel carrying that pericyte is coloured.

The `stall` array written on every frame has four states, so the picture
distinguishes "not modelled" from "modelled but not measured":

   -1  not in the vessel array at all          (draw grey)
    0  in the array, but no stall data for it  (draw blue)
    1  flowing at this instant                 (draw green)
    2  stalled at this instant                 (draw red)

Also written: `stall_any` (1 if this vessel ever stalls), `in_model`,
`focus` (0, or the number of the --focus set a vessel belongs to),
`vessel_id` and `name`.

Options:
    --frames N     how many frames to write (default 300)
    --out DIR      output folder (default <network>_stall_series)
    --every N      take every Nth timestep instead of resampling to --frames
"""

import argparse
import csv
from pathlib import Path

import numpy as np


def read_stalls(path):
    """Time column plus one column per element, from the solver output."""
    rows = list(csv.reader(open(path)))
    header = rows[0]
    names = [h.split("|")[0].strip() for h in header[1:]]
    data = np.array([[float(x) for x in r] for r in rows[1:] if r], dtype=float)
    return data[:, 0], names, data[:, 1:]


def read_array(path):
    """element name -> every original vessel it covers, plus the rows.

    A merged vessel has a `graph_vessel_id` that exists only after the sweep --
    the source .vtp still holds the pieces it was made from, which are listed in
    `source_ids`. Matching on the id alone therefore misses every merged vessel,
    which is most of the long ones. Both are used here.
    """
    rows = list(csv.DictReader(open(path)))
    to_geom, by_name = {}, {}
    for r in rows:
        by_name[r["name"]] = r
        ids = set(str(r.get("source_ids") or "").split())
        gid = (r.get("graph_vessel_id") or "").strip()
        if gid:
            ids.add(gid)
        if ids:
            to_geom[r["name"]] = ids
    return to_geom, by_name


def downstream_geoms(start, by_name, to_geom, depth):
    """Geometry of the vessels lying `depth` vessels past `start`.

    A pericyte and the vessel it sits on are the same tube, so walking to the
    next distinct geometry means stepping over junction rows and over the
    element that shares the starting geometry.
    """
    if depth <= 0:
        return set()
    found, seen = set(), {start}
    frontier = [start]
    origin = to_geom.get(start, set())
    reached = 0
    hops = 0
    while frontier and hops < depth + 4:
        hops += 1
        nxt = []
        for nm in frontier:
            r = by_name.get(nm)
            if not r:
                continue
            for o in str(r.get("out_vessels", "")).split():
                if o in seen:
                    continue
                seen.add(o)
                g = to_geom.get(o, set())
                if g and g != origin:
                    found |= g
                    reached += 1
                    if reached >= depth:
                        return found
                nxt.append(o)          # junctions carry no geometry: step over
        frontier = nxt
    return found


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("network", help="the curated .vtp")
    ap.add_argument("array", help="the vessel array .csv")
    ap.add_argument("stalls", help="the solver output .csv")
    ap.add_argument("--frames", type=int, default=300)
    ap.add_argument("--every", type=int, default=None)
    ap.add_argument("--out", default=None)
    ap.add_argument("--only-array", action="store_true",
                    help="keep only the vessels present in the array, instead "
                         "of showing the whole network with the rest greyed")
    ap.add_argument("--focus", action="append", default=[],
                    help='a focus set as "label:PV12,PV13". Repeatable. Writes '
                         'a numeric `focus` array (0 none, 1 first set, ...) so '
                         'ParaView can isolate a set by thresholding, which is '
                         'more reliable than querying the string vessel_id.')
    ap.add_argument("--downstream", type=int, default=1,
                    help="how many vessels past each measured one to colour "
                         "with the same state (default 1, 0 for none)")
    args = ap.parse_args()

    import pyvista as pv

    net = Path(args.network)
    mesh = pv.read(net)
    if "vessel_id" not in mesh.cell_data:
        raise SystemExit("that .vtp has no vessel_id array")
    geom_ids = [str(x) for x in mesh.cell_data["vessel_id"]]
    print(f"network: {mesh.n_cells} vessels")

    to_geom, by_name = read_array(args.array)
    t, names, stall = read_stalls(args.stalls)
    print(f"stalls:  {len(t)} timesteps, {len(names)} tracked elements")

    # element -> which cells of the mesh take its state
    cells_for = {}
    unmatched = []
    extra = 0
    for i, nm in enumerate(names):
        gid = to_geom.get(nm)
        if not gid:
            unmatched.append(nm)
            continue
        wanted = set(gid) | downstream_geoms(nm, by_name, to_geom, args.downstream)
        idx = [j for j, g in enumerate(geom_ids) if g in wanted]
        if not idx:
            unmatched.append(nm)
            continue
        cells_for[i] = idx
        extra += len(wanted) - 1
    if args.downstream:
        print(f"colouring {args.downstream} vessel(s) downstream of each "
              f"measured one: {extra} extra vessel(s) picked up")
    print(f"matched {len(cells_for)} of {len(names)} to geometry")
    if unmatched:
        print(f"  no geometry for: {', '.join(unmatched[:8])}"
              + (" ..." if len(unmatched) > 8 else ""))
        print("  (check the array and the .vtp came from the same session)")

    # The array is usually a subset of the network it came from. Showing the
    # whole thing puts the simulated part in context; restricting to the array
    # gives a cleaner shot of just what was modelled.
    in_array = set()
    for r in csv.DictReader(open(args.array)):
        in_array |= set(str(r.get("source_ids") or "").split())
        gid = (r.get("graph_vessel_id") or "").strip()
        if gid:
            in_array.add(gid)
    keep_mask = np.array([g in in_array for g in geom_ids], dtype=bool)
    print(f"vessels also in the array: {int(keep_mask.sum())} of {mesh.n_cells}")
    if keep_mask.sum() == 0:
        print("  NONE MATCHED -- the array and this .vtp are from different runs")
    elif keep_mask.sum() < 0.5 * len(in_array):
        print(f"  only {int(keep_mask.sum())} of {len(in_array)} ids in the array "
              "were found; check these files belong together")

    if args.only_array:
        if not keep_mask.any():
            raise SystemExit("no vessel in the array matches this network — "
                             "are they from the same session?")
        mesh = mesh.extract_cells(np.flatnonzero(keep_mask)).extract_surface()
        geom_ids = [str(x) for x in mesh.cell_data["vessel_id"]]
        cells_for = {}
        for i, nm in enumerate(names):
            gid = to_geom.get(nm)
            if gid:
                idx = [j for j, g in enumerate(geom_ids) if g in gid]
                if idx:
                    cells_for[i] = idx
        print(f"restricted to the array: {mesh.n_cells} vessels")

    # which frames to write
    if args.every:
        picks = list(range(0, len(t), args.every))
    else:
        picks = np.unique(np.linspace(0, len(t) - 1, args.frames).astype(int)).tolist()
    print(f"writing {len(picks)} frames")

    out = Path(args.out) if args.out else net.with_name(net.stem + "_stall_series")
    out.mkdir(parents=True, exist_ok=True)

    # focus sets, resolved to geometry and written as a plain integer array:
    # a numeric threshold works on every ParaView build, whereas a query
    # against the string vessel_id does not
    focus = np.zeros(mesh.n_cells, dtype=np.int8)
    focus_labels = []
    for n_set, spec in enumerate(args.focus, start=1):
        label, _, members = spec.partition(":")
        wanted_names = {m.strip() for m in members.split(",") if m.strip()}
        ids = set()
        for nm in wanted_names:
            ids |= to_geom.get(nm, set())
            ids |= downstream_geoms(nm, by_name, to_geom, args.downstream)
        hit = [j for j, g in enumerate(geom_ids) if g in ids]
        focus[hit] = n_set
        focus_labels.append((n_set, label.strip() or f"set {n_set}",
                             sorted(wanted_names), len(hit)))
        print(f"focus {n_set} '{label.strip()}': {len(wanted_names)} element(s) "
              f"-> {len(ids)} vessel id(s), {len(hit)} cells")

    # vessels that never stall stay dim, so the eye follows the ones that do
    ever = np.zeros(mesh.n_cells, dtype=np.int8)
    in_model = np.array([1 if g in in_array else 0 for g in geom_ids], dtype=np.int8)
    for i, idx in cells_for.items():
        if stall[:, i].max() > 0:
            ever[idx] = 1

    element_name = np.array([""] * mesh.n_cells, dtype=object)
    for i, idx in cells_for.items():
        for j in idx:
            element_name[j] = names[i]

    for f, step in enumerate(picks):
        frame = mesh.copy()
        # -1 not in the array, 0 in the array but unmeasured, 1 flowing,
        # 2 stalled. Keeping "unmeasured" distinct from "flowing" matters:
        # otherwise the picture claims knowledge it does not have.
        s = np.where(in_model > 0, 0, -1).astype(np.int8)
        for i, idx in cells_for.items():
            s[idx] = 2 if stall[step, i] > 0 else 1
        frame.cell_data["stall"] = s
        frame.cell_data["stall_any"] = ever
        frame.cell_data["in_model"] = in_model
        frame.cell_data["focus"] = focus
        frame.cell_data["name"] = np.array([str(x) for x in element_name])
        frame.save(out / f"stall_{f:04d}.vtp")

    # a .pvd so ParaView knows the real times, not just frame numbers
    with open(out / "stall.pvd", "w") as fh:
        fh.write('<?xml version="1.0"?>\n')
        fh.write('<VTKFile type="Collection" version="0.1" '
                 'byte_order="LittleEndian">\n  <Collection>\n')
        for f, step in enumerate(picks):
            fh.write(f'    <DataSet timestep="{t[step]}" group="" part="0" '
                     f'file="stall_{f:04d}.vtp"/>\n')
        fh.write("  </Collection>\n</VTKFile>\n")

    frac = float((stall > 0).mean())
    print(f"\nwrote {out}/stall.pvd")
    print(f"  {len(picks)} frames, t = {t[picks[0]]:g} to {t[picks[-1]]:g}")
    measured = len({j for idx in cells_for.values() for j in idx})
    print(f"  {int(in_model.sum())} of {mesh.n_cells} vessels are in the array")
    print(f"  {measured} of those carry stall data")
    print(f"  {int(ever.sum())} stall at some point")
    for n_set, label, members, cells in focus_labels:
        print(f"  focus {n_set}: {label} ({', '.join(members)}) -> {cells} cells")
    print(f"  mean stalled fraction over the run: {frac:.2f}")
    print("""
In ParaView:
  1. Open stall.pvd
  2. Colour by `stall` as four categories:
     -1 grey (not modelled), 0 blue (modelled, not measured),
      1 green (flowing), 2 red (stalled)
  3. Easier: run paraview_stall_setup.py, which does all of this
  4. Filters -> Tube for thickness, radius about 1-2
     To show only the simulated part, Threshold on `in_model` = 1,
     or run with --only-array to leave the rest out of the files
  5. Press play; File -> Save Animation for the video
""")


if __name__ == "__main__":
    main()
