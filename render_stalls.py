#!/usr/bin/env pvpython
"""
Render the stall animation to PNG frames without the ParaView window.

    pvpython render_stalls.py <stall.pvd> <vessel_array.csv> <output_dir>

The interactive renderer on this machine keeps losing its OpenGL context --
the magenta view and the vtkOpenGLState warnings -- and every extra actor
makes it likelier. Offscreen rendering from pvpython avoids that path
completely: it builds the scene, writes the frames, and exits.

Everything the GUI scripts do is done here: the grey context network, the
measured vessels, the focus sets with dashed leaders and labels, the legend,
the clock.

Afterwards:
    ffmpeg -framerate 30 -i f.%04d.png -c:v libx264 -pix_fmt yuv420p -crf 20 stalls.mp4
"""

import csv
import math
import os
import sys

from paraview.simple import *

# ------------------------------------------------------------------ settings
FOCUS_SETS = [
    ("VV_junc7 pair", ["PV12", "PV13"]),
    ("parallel paths", ["PV30", "PV34"]),
    ("VV_junc4 pair", ["PV07", "PV08"]),
]
ANGLES = [200, 20, 90]        # on screen: 0 right, 90 up
RING = 0.35           # labels sit this far outside the focus vessels. Above
                      # about 0.5 they fall outside the camera's view and
                      # simply do not appear, which is what happened before.
DASHES = 3                    # kept low: fewer actors, less to go wrong
DASH_DUTY = 0.6
ARROWHEAD = 0.035

SHOW_FOCUS = True             # False = colour every measured vessel instead

TUBE_FOCUS = 4.0
TUBE_MODEL = 3.0
TUBE_REST = 1.0
REST_OPACITY = 0.35
OTHER_MODEL_OPACITY = 0.55
LEADER_WIDTH = 4.0

COLOUR_UNMEASURED = [0.10, 0.35, 0.85]
COLOUR_FLOWING = [0.10, 0.70, 0.25]
COLOUR_STALLED = [0.85, 0.10, 0.10]
COLOUR_REST = [0.62, 0.62, 0.66]
BACKGROUND = [1.0, 1.0, 1.0]
BLACK = [0.0, 0.0, 0.0]

# Camera, captured from an interactive session so the offscreen render uses
# the orientation you chose rather than whatever ResetCamera picks.
# Set USE_CAMERA = False to let it frame the network automatically.
USE_CAMERA = True
CAM_POSITION = (1155.6842183735796, 888.6433665608276, -2161.082415209181)
CAM_FOCAL = (511.4116037397849, 520.3427906921027, 52.96677835397444)
# negated: the captured camera had world +y pointing down, so the network
# rendered upside down. Flipping ViewUp turns it the right way up.
CAM_UP = (-0.12222174007860107, 0.9841945225564489, 0.12815220646575895)
CAM_SCALE = 320.0     # smaller = more zoomed in. 412.8 was the captured value

SIZE = [1920, 1080]
TEXT_SIZE = 26
CLOCK_SIZE = 30
BAR_TITLE = 24
BAR_LABEL = 22
# ---------------------------------------------------------------------------


def setp(o, n, v):
    try:
        setattr(o, n, v)
        return True
    except Exception:
        return False


def set_first(o, n, values):
    for v in values:
        try:
            setattr(o, n, v)
            return v
        except Exception:
            continue
    return None


def geometry_for(elements, array_csv):
    ids = set()
    for r in csv.DictReader(open(array_csv)):
        if r.get("name") in elements:
            ids |= set(str(r.get("source_ids") or "").split())
            g = (r.get("graph_vessel_id") or "").strip()
            if g:
                ids.add(g)
    return ids


def tubes_of(src, radius):
    surf = ExtractSurface(Input=src)
    tb = Tube(Input=surf)
    setp(tb, "Scalars", ["CELLS", "stall"])
    setp(tb, "Radius", radius)
    setp(tb, "NumberofSides", 8)
    return tb


def threshold_on(src, array, lo, hi):
    t = Threshold(Input=src)
    setp(t, "Scalars", ["CELLS", array])
    if not setp(t, "LowerThreshold", lo):
        setp(t, "ThresholdRange", [lo, hi])
    setp(t, "UpperThreshold", hi)
    setp(t, "ThresholdMethod", "Between")
    return t


def main():
    if len(sys.argv) < 4:
        print(__doc__)
        sys.exit(1)
    pvd, array_csv, outdir = sys.argv[1], sys.argv[2], sys.argv[3]
    os.makedirs(outdir, exist_ok=True)

    reader = OpenDataFile(pvd)
    view = CreateRenderView()
    view.ViewSize = SIZE
    setp(view, "UseColorPaletteForBackground", 0)
    setp(view, "BackgroundColorMode", "Single Color")
    setp(view, "Background", BACKGROUND)
    setp(view, "OrientationAxesVisibility", 0)
    setp(view, "CameraParallelProjection", 1)

    times = list(reader.TimestepValues)
    print(f"{len(times)} timesteps, {times[0]:g} to {times[-1]:g}")

    # the surrounding network
    rest = tubes_of(threshold_on(reader, "in_model", 0, 0), TUBE_REST)
    rd = Show(rest, view)
    ColorBy(rd, None)
    setp(rd, "AmbientColor", COLOUR_REST)
    setp(rd, "DiffuseColor", COLOUR_REST)
    setp(rd, "Opacity", REST_OPACITY)

    model_src = threshold_on(reader, "in_model", 1, 1)

    if SHOW_FOCUS:
        chosen = tubes_of(threshold_on(model_src, "focus", 1, 99), TUBE_FOCUS)
        cd = Show(chosen, view)
        ColorBy(cd, ("CELLS", "stall"))
        others = tubes_of(threshold_on(model_src, "focus", 0, 0), TUBE_MODEL)
        od = Show(others, view)
        ColorBy(od, None)
        setp(od, "AmbientColor", COLOUR_UNMEASURED)
        setp(od, "DiffuseColor", COLOUR_UNMEASURED)
        setp(od, "Opacity", OTHER_MODEL_OPACITY)
        main_disp, main_src = cd, chosen
    else:
        allm = tubes_of(model_src, TUBE_MODEL)
        ad = Show(allm, view)
        ColorBy(ad, ("CELLS", "stall"))
        main_disp, main_src = ad, allm

    # colours: four states, fixed range
    lut = GetColorTransferFunction("stall")
    setp(lut, "InterpretValuesAsCategories", 1)
    setp(lut, "AnnotationsInitialized", 1)
    setp(lut, "Annotations", ["0", "in model, no data",
                              "1", "flowing", "2", "stalled"])
    setp(lut, "IndexedColors",
         COLOUR_UNMEASURED + COLOUR_FLOWING + COLOUR_STALLED)
    setp(lut, "IndexedOpacities", [1.0, 1.0, 1.0])
    try:
        lut.RescaleTransferFunction(0.0, 2.0)
    except Exception:
        pass

    if USE_CAMERA:
        cam = GetActiveCamera()
        cam.SetPosition(*CAM_POSITION)
        cam.SetFocalPoint(*CAM_FOCAL)
        cam.SetViewUp(*CAM_UP)
        cam.SetParallelScale(CAM_SCALE)
    else:
        ResetCamera(view)
    Render(view)

    bar = GetScalarBar(lut, view)
    setp(bar, "Title", "blood flow")
    setp(bar, "ComponentTitle", "")
    setp(bar, "TitleFontSize", BAR_TITLE)
    setp(bar, "LabelFontSize", BAR_LABEL)
    setp(bar, "TitleColor", BLACK)
    setp(bar, "LabelColor", BLACK)
    setp(bar, "TitleBold", 1)
    setp(bar, "LabelBold", 1)
    setp(bar, "ScalarBarThickness", 22)
    setp(bar, "ScalarBarLength", 0.28)
    set_first(bar, "WindowLocation", ["Any Location", "AnyLocation"])
    setp(bar, "Position", [0.88, 0.08])
    main_disp.SetScalarBarVisibility(view, True)

    # the clock
    clock = AnnotateTimeFilter(Input=reader)
    if not setp(clock, "Format", "Time: {time:.0f} s"):
        setp(clock, "Format", "Time: %.0f s")
    cd2 = Show(clock, view)
    setp(cd2, "FontSize", CLOCK_SIZE)
    setp(cd2, "Color", BLACK)
    setp(cd2, "Bold", 1)
    setp(cd2, "WindowLocation", "Upper Left Corner")

    # labels, placed in the camera's own plane so the angles mean what they look
    if SHOW_FOCUS:
        b = main_src.GetDataInformation().GetBounds()
        centre = [(b[0] + b[1]) / 2, (b[2] + b[3]) / 2, (b[4] + b[5]) / 2]
        half = max(b[1] - b[0], b[3] - b[2]) / 2.0
        span = max(b[1] - b[0], b[3] - b[2])

        cam = GetActiveCamera()
        p, f, vu = cam.GetPosition(), cam.GetFocalPoint(), cam.GetViewUp()
        # (this is the camera set above, so the label angles are screen angles)
        fwd = [f[k] - p[k] for k in range(3)]
        n = math.sqrt(sum(c * c for c in fwd)) or 1.0
        fwd = [c / n for c in fwd]
        rt = [fwd[1] * vu[2] - fwd[2] * vu[1],
              fwd[2] * vu[0] - fwd[0] * vu[2],
              fwd[0] * vu[1] - fwd[1] * vu[0]]
        n = math.sqrt(sum(c * c for c in rt)) or 1.0
        rt = [c / n for c in rt]
        upv = [rt[1] * fwd[2] - rt[2] * fwd[1],
               rt[2] * fwd[0] - rt[0] * fwd[2],
               rt[0] * fwd[1] - rt[1] * fwd[0]]
        n = math.sqrt(sum(c * c for c in upv)) or 1.0
        upv = [c / n for c in upv]

        for i, (label, elements) in enumerate(FOCUS_SETS):
            ids = geometry_for(set(elements), array_csv)
            if not ids:
                print(f"  '{label}': no geometry, skipped")
                continue
            q = " | ".join('(vessel_id == "%s")' % v for v in sorted(ids))
            sel = None
            for kw in ({"ElementType": "Cell"}, {"ElementType": "CELL"},
                       {"FieldType": "CELL"}, {}):
                try:
                    sel = SelectionQuerySource(QueryString=q, **kw)
                    break
                except Exception:
                    continue
            if sel is None:
                continue
            part = ExtractSelection(Input=model_src, Selection=sel)
            try:
                part.UpdatePipeline()
                pb = part.GetDataInformation().GetBounds()
                if pb[1] < pb[0]:
                    continue
            except Exception:
                continue
            tip = [(pb[0] + pb[1]) / 2, (pb[2] + pb[3]) / 2, (pb[4] + pb[5]) / 2]

            ang = math.radians(ANGLES[i % len(ANGLES)])
            r = half * (1.0 + RING)
            anchor = [centre[k] + (rt[k] * math.cos(ang)
                                   + upv[k] * math.sin(ang)) * r
                      for k in range(3)]

            for d in range(DASHES):
                a0 = d / float(DASHES)
                a1 = a0 + DASH_DUTY / DASHES
                p1 = [anchor[k] + (tip[k] - anchor[k]) * a0 for k in range(3)]
                p2 = [anchor[k] + (tip[k] - anchor[k]) * a1 for k in range(3)]
                seg = Line(Point1=p1, Point2=p2)
                sd = Show(seg, view)
                ColorBy(sd, None)
                setp(sd, "LineWidth", LEADER_WIDTH)
                setp(sd, "AmbientColor", BLACK)
                setp(sd, "DiffuseColor", BLACK)

            hx, hy = tip[0] - anchor[0], tip[1] - anchor[1]
            hn = math.hypot(hx, hy) or 1.0
            head = Cone(Radius=span * ARROWHEAD * 0.5, Height=span * ARROWHEAD,
                        Direction=[hx / hn, hy / hn, 0.0],
                        Center=[tip[0] - hx / hn * span * ARROWHEAD * 0.5,
                                tip[1] - hy / hn * span * ARROWHEAD * 0.5,
                                tip[2]], Resolution=12)
            hd = Show(head, view)
            ColorBy(hd, None)
            setp(hd, "AmbientColor", BLACK)
            setp(hd, "DiffuseColor", BLACK)

            txt = Text()
            setp(txt, "Text", " / ".join(elements))
            td = Show(txt, view)
            set_first(td, "TextPropMode",
                      ["Billboard 3D Text", "3D Text Widget", "2D Text Widget"])
            setp(td, "BillboardPosition", anchor)
            setp(td, "FontSize", TEXT_SIZE)
            setp(td, "Bold", 1)
            setp(td, "Color", BLACK)
            setp(td, "Justification", "Center")
            print(f"  labelled '{label}' at angle {ANGLES[i % len(ANGLES)]}")

    if not USE_CAMERA:
        ResetCamera(view)
    Render(view)

    print(f"writing {len(times)} frames to {outdir} ...")
    for i, t in enumerate(times):
        view.ViewTime = t
        SaveScreenshot(os.path.join(outdir, f"f.{i:04d}.png"), view,
                       ImageResolution=SIZE)
        if i % 50 == 0:
            print(f"  {i}/{len(times)}")
    print("done\n")
    fps = max(1, int(round(len(times) / 20.0)))
    print("now encode:")
    print(f'  cd "{outdir}"')
    print(f"  ffmpeg -framerate {fps} -i f.%04d.png "
          f"-c:v libx264 -pix_fmt yuv420p -crf 20 stalls.mp4")
    print(f"  ({len(times)} frames at {fps} fps = {len(times)/fps:.0f} s)")


if __name__ == "__main__":
    main()
