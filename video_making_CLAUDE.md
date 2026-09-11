# Capillary stalling pipeline — how to reproduce it

Everything from a HaemoLynx-generated network to a video of vessels stalling
over time. Written after doing it once the hard way, so the dead ends are
recorded alongside the steps that work.

Machine: `bn466399`, Ubuntu 24, Intel Arc graphics, ParaView 6.1.1.
**That GPU's OpenGL is unreliable and is the source of most of the pain below.**

---

## 0. Environment

napari and the Python tools live in a venv, deliberately separate from the
system Python and from the napari desktop app (which bundles its own Python
that nothing else can see):

```bash
~/napari-venv/bin/python      # use this, not `python3`
```

Created with:

```bash
python3 -m venv ~/napari-venv
~/napari-venv/bin/pip install "napari[all]" pyvista networkx tifffile scipy
```

There is no need to `source activate` anything; call the full path.

### ilastik

Downloaded from ilastik.org and unpacked to `~/ilastik-1.4.2-Linux`. The
launcher inside has a shebang pointing at the build machine's Python, so it
cannot be run directly. A wrapper is needed:

```bash
cat > ~/ilastik-1.4.2-Linux/run_ilastik.sh << 'EOF'
#!/bin/bash
export FONTCONFIG_FILE=/etc/fonts/fonts.conf
exec /home/sliu205/ilastik-1.4.2-Linux/bin/python \
     /home/sliu205/ilastik-1.4.2-Linux/bin/ilastik "$@"
EOF
chmod +x ~/ilastik-1.4.2-Linux/run_ilastik.sh
```

ilastik also ships an incomplete libglvnd, which prevents it from getting an
OpenGL context. Move the bundled copies aside so the system ones are used:

```bash
cd ~/ilastik-1.4.2-Linux/lib
mkdir -p _glvnd_backup
mv libGL.so* libGLX.so* libGLdispatch.so* libEGL.so* _glvnd_backup/
```

The same defect affects the napari **installer** build, which is why napari is
installed with pip instead.

---

## 1. HaemoLynx: image → network

Run the plugin from the repo directory so relative paths resolve there:

```bash
cd ~/Documents/git_projects/Haemolynx/HaemoLynx
~/napari-venv/bin/napari
```

Settings that matter, learned the hard way:

| setting | value | why |
| --- | --- | --- |
| `ilastik_output_suffix` | `.tiff` | ilastik writes two f's; `.tif` makes HaemoLynx look for a file that is never created |
| `ilastik_executable` | the wrapper above | not `bin/ilastik`, which has the broken shebang |
| `centreline_smoothing_method` | `taubin` | `chaikin` subdivides, multiplying points by 2^iterations, and then crashes in the blending fallback because the arrays no longer match |
| `cluster_collapse_distance` | 2–3 | at 8 it fuses many real bifurcations into single hubs of degree 26–34 |

Outputs land in `outputs/`, including `..._segmented_graph.pkl` and
`HaemoLynx_image.tif`.

---

## 2. Curate the network

```bash
cd ~/Documents/git_projects/Haemolynx/HaemoLynx/outputs
~/napari-venv/bin/python \
  ~/Documents/git_projects/Haemolynx/HaemoLynx/Network_creation_scripts/curate_network_v13.py \
  vessel-Zstack2_Male_SM_9W_16072024_segmented_graph.pkl \
  --image HaemoLynx_image.tif
```

Order of operations inside the tool:

1. **Collapse hairpins** — split-and-rejoin loops from holes in the mask
2. **Remove or split over-connected nodes**
3. **Drop short vessels / terminal stubs**
4. **Crop** to a sub-volume if the network is too large
5. **Keep largest component**
6. **Highlight terminals**, then **mark inlets**
7. **Export** — writes `.pkl`, `.vtp`, `_vessel_array.csv`, `_recipe.json`

The `.vtp` carries `vessel_id` and `boundary` cell arrays. Keep it: everything
downstream needs it for geometry.

---

## 3. Build the vessel array

```bash
cd ~/Documents/git_projects/Haemolynx/HaemoLynx/outputs/Post_processed
~/napari-venv/bin/python \
  ~/Documents/git_projects/Haemolynx/HaemoLynx/Network_creation_scripts/build_vessel_array.py \
  vessel-..._Manual_pruned.vtp \
  --image ../HaemoLynx_image.tif
```

Order inside the tool — this order matters:

1. **Sweep degree-2 joins** first. It changes vessel lengths, which changes
   which vessels qualify for a pericyte. Doing pericyte edits before the sweep
   means judging the wrong lengths.
2. **Find nodes joining >3**, then split or delete until none remain. Build
   refuses while any exist.
3. **Compute density** — sets the pericyte plan.
4. **Mark inlets** if not already read from the file.
5. **Build vessel array**.
6. Check the **unreachable branches** panel. Anything listed is outside the
   flow; delete it or mark it as a second inlet.
7. Check the **bad junctions** panel. A VV junction takes at most two inputs
   and two outputs and must have at least one of each.
8. **Export CSV** — also writes `_steps.json` recording every action.

Run the regression suite after any change to the script:

```bash
~/napari-venv/bin/python test_build_vessel_array.py <network>.vtp
```

64 checks. It has caught real bugs, including a loader fault that inflated
total network length by 8%.

### Things that bite

* A merged vessel's `graph_vessel_id` exists only after the sweep. The original
  pieces are in `source_ids`, and those are what the `.vtp` contains. **Always
  match on both.**
* Manual pericyte edits are recorded against vessel ids, so a later sweep
  renames them. The tool remaps them; if you write your own analysis, remember.

---

## 4. Simulation

The vessel array goes to circulatory autogen, which produces
`..._Data.csv`: a time column plus one `stall` column per pericyte element
(`PV04`, `PV07`, ...). Values are 0 or 1.

The example run: 5001 timesteps, 0 to 5000 s, 23 tracked pericytes.

---

## 5. Frames for ParaView

```bash
BASE=~/0D_hemodynamics_paper/0D_hemodynamics_paper/Haemolynx_simplified_zstack_make2
SERIES=~/Documents/git_projects/Haemolynx/HaemoLynx/outputs/Post_processed/vessel-..._Manual_pruned_stall_series

~/napari-venv/bin/python $BASE/make_stall_series.py \
  ~/Documents/git_projects/Haemolynx/HaemoLynx/outputs/Post_processed/vessel-..._Manual_pruned.vtp \
  $BASE/resources/Haemolynx_partial_network_vessel_array.csv \
  $BASE/generated_models/Haemolynx_partial_network/Haemolynx_partial_network_Data.csv \
  --frames 600 --downstream 1 \
  --focus "VV_junc7 pair:PV12,PV13" \
  --focus "parallel paths:PV30,PV34" \
  --focus "VV_junc4 pair:PV07,PV08"
```

Writes `stall.pvd` plus 600 numbered `.vtp` frames.

`--frames 600` at 30 fps gives a 20-second clip. More frames capture more
transitions: the run has 180, of which 600 frames keeps about 106.

Cell arrays written per frame:

| array | meaning |
| --- | --- |
| `stall` | −1 not in the array, 0 in the array but unmeasured, 1 flowing, 2 stalled |
| `in_model` | 1 if the vessel is part of the simulated array |
| `focus` | 0, or the number of the `--focus` set it belongs to |
| `vessel_id` | stable identifier |

The `focus` array is numeric on purpose: ParaView can threshold an integer on
any build, whereas querying the string `vessel_id` is unreliable across
versions.

### Finding sets worth showing

Sets were chosen by correlating the stall series. Sibling branches that
alternate cleanly:

| set | alternate | correlation |
| --- | --- | --- |
| PV12 / PV13 at VV_junc7 | 79% | −0.63 |
| PV30 / PV34, parallel paths | 86% | −0.74 |
| PV07 / PV08 at VV_junc4 | 62% | −0.33 |

---

## 6. ParaView

**Open `stall.pvd`, never the numbered `.vtp` files.** The `.pvd` carries the
real times; opening the series directly gives frame indices, so the clock ends
at 599 instead of 5000.

### The sequence

1. File → Open → `stall.pvd` → Apply
2. View → Python Shell → **Run Script** → `paraview_stall_setup.py`
   *(Run Script, never paste: the shell executes line by line and a blank line
   inside a function ends the block early)*
3. In the shell, one line:

```python
GetAnimationScene().PlayMode = 'Snap To TimeSteps'
```

4. Click `time` in the Pipeline Browser. Properties → **Format**:

```
Time: {time:.0f} s
```

Press Apply. ParaView 6.x uses `{time}`; the old `%.0f` style prints literally.

5. **Rotate to the view you want.** Labels are laid out from the camera, so
   this must come before step 6.
6. Run Script → `paraview_labels.py`
7. In the shell, one line at a time:

```python
v = GetActiveView(); pxm = servermanager.ProxyManager()
```
```python
[setattr(p, 'Visibility', 0) for p in pxm.GetProxiesInGroup('scalar_bars').values()]
```
```python
b = GetScalarBar(GetColorTransferFunction('stall'), v); b.Visibility = 1
```
```python
b.TitleFontSize = 34; b.LabelFontSize = 30; b.TitleBold = 1; b.LabelBold = 1
```
```python
b.ScalarBarThickness = 30; b.ScalarBarLength = 0.30
```
```python
b.WindowLocation = 'Lower Right Corner'
```
```python
GetLayout().SetSize(1920, 1080); Render()
```

8. Press **stop** (not pause) — Save Animation refuses during playback.
9. File → Save Animation → **PNG** → `/home/sliu205/stall_frames/f.png`
   → Image Resolution **1920 × 1080**

### Which layers to show

| view | eye ON | eye OFF |
| --- | --- | --- |
| focus sets | `context`, `focus: ALL SETS`, `rest of model (all sets)`, `time`, `dash:`/`label:` | `all measured vessels` |
| all measured | `context`, `all measured vessels`, `time` | `focus: ALL SETS`, `rest of model (all sets)` |

Never both `all measured vessels` and `focus: ALL SETS`: they draw the same
vessels in the same place.

---

## 7. Encode

```bash
cd ~/stall_frames
ffmpeg -framerate 30 -i f.%04d.png -c:v libx264 -pix_fmt yuv420p -crf 20 stalls.mp4
```

`-pix_fmt yuv420p` is what makes it play in PowerPoint instead of showing a
black box. Insert via Insert → Video → This Device, then Playback → Start
Automatically, Loop until Stopped.

---

## The OpenGL problem

The view turning **magenta** with `vtkOpenGLState` warnings is the render view
losing its context. It is not a scripting error. It gets likelier as the actor
count rises. Two things reliably cause it here:

* **Billboard 3D text.** Never use `TextPropMode = "Billboard 3D Text"`.
  Labels must be `2D Text Widget`.
* **Interactive text widgets.** `Interactivity = 1` on a Text source needs its
  own context and crashes. Labels are therefore not draggable; move one by
  selecting it in the Pipeline Browser and editing **Text Position** (two
  fractions of the window) in Properties.

Also keep the actor count down. `paraview_labels.py` uses `DASHES = 4` and no
arrowhead cones for this reason. If magenta returns, `DASHES = 1` is the next
step down, then `SHOW_LABELS = False`.

Software rendering is a fallback:

```bash
LIBGL_ALWAYS_SOFTWARE=1 ~/Desktop/ParaView-6.1.1-MPI-Linux-Python3.12-x86_64/bin/paraview
```

There is also an offscreen renderer, `render_stalls.py`, run through
`pvpython --force-offscreen-rendering`. It cannot crash this way, but the
camera has to be typed in rather than chosen by rotating, which makes it
painful to frame. Use it only if the interactive route will not survive.

---

## Mistakes to avoid

**Aspect ratio.** If the render view is wider than the export resolution, the
save crops and the fonts look oversized. Always `GetLayout().SetSize(1920, 1080)`
before judging how anything looks.

**ParaView's AVI writer** ignored the frame rate and produced 600 frames at
1 fps — a ten-minute video. Save PNG and encode with ffmpeg.

**Odd resolutions** get silently rounded (1560×683 → 1560×680). Use even
numbers.

**The scalar bar in the top right** comes back whenever the colour map
bookkeeping is re-triggered, such as by editing the time filter. Hiding it via
the representations is not enough; the proxy-manager loop in step 7 is. Do that
step last.

**Label angles** are measured on screen, 0 = right and 90 = up, and are
computed in the camera's plane. Computing them in world XY puts them in the
wrong corners, because the camera does not look down the world z axis.

---

## Files

| file | what it does |
| --- | --- |
| `curate_network_v13.py` | interactive network curation in napari |
| `build_vessel_array.py` | vessel array generation, pericytes, boundaries |
| `test_build_vessel_array.py` | 64 regression checks — run after any change |
| `make_stall_series.py` | simulation output → ParaView time series |
| `paraview_stall_setup.py` | builds the layers, colours, legend |
| `paraview_labels.py` | leaders and labels, legend cleanup |
| `render_stalls.py` | offscreen fallback via pvpython |
| `vessel_array_viewer.html` | standalone browser viewer for a vessel array |

The scripts belong in
`~/Documents/git_projects/Haemolynx/HaemoLynx/Network_creation_scripts/` and
should be committed — two copies of a script being actively edited is how the
`VV_junc14` naming confusion happened.
