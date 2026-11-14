---
title: uLoftPro
weight: 3
aliases:
  - /help/uloftpro/
---

| Menu | Command |
| --- | --- |
| `commaMenu` → **Brep** | `uLoftPro` |

Distributes profiles, blocks, meshes, points, text or breps along rail curves and lofts or sweeps curve profiles through them. You pick rails, pick what to distribute, set a reference point and preview the result before it is baked.

#### Steps

1. Run `uLoftPro`. At `Select Alignment curves (Rails)` pick one or more rails. Optionally set `Mode` (`PerPlane` or `PerHorPln`, default PerHorPln) and `DivideDist` (default 500, from 0.1 to 1000000).
2. At `Select Objects to Distribute` pick curves, blocks, meshes, points, annotation text or breps.
3. At `Pick Reference Point (Origin)` pick the point on the objects that will sit on the rail.
4. A preview appears with direction arrows on the rails. The prompt reads `Previewing... Enter to Bake.`
5. While previewing you can change the options: `Method` (Loft or Sweep, only shown when curves were selected), `Cap`, `Flip_Rails` (`Select Rail to Flip (Press Enter when done)`), `Reselect_Objects` and `Pick_New_Origin`.
6. Press Enter to bake, or Esc to cancel.
7. Rails are divided by length (end points included) every `DivideDist`. A frame is built at each division: with `PerHorPln` the frame stays upright (Y is world Z), with `PerPlane` the frame follows the 3D tangent of the rail.
8. Blocks, meshes, breps, points and text are copied to every frame. Curves are lofted between frames (`Loft`) or swept along the rail (`Sweep`). With `Cap` Yes planar holes are capped.
9. The results of each rail are grouped as `Align_N_Result`.

#### Options

| Option | Values | What it does |
| --- | --- | --- |
| Mode | PerPlane, PerHorPln (default PerHorPln) | PerPlane tilts frames with the rail tangent; PerHorPln keeps frames vertical (Y is world Z). |
| DivideDist | 0.1 to 1000000, default 500 | Distance between frames along each rail. |
| Method | Loft, Sweep | How curve profiles are turned into surfaces. Shown only when curves were selected. |
| Cap | No, Yes (default No) | Caps planar holes of the lofted or swept results. |
| Flip_Rails | Select rails, Enter when done | Reverses the direction of the picked rails. |
| Reselect_Objects | Select objects | Replaces the set of objects to distribute. |
| Pick_New_Origin | Point | Changes the reference point (the current one is shown in the prompt). |

Flip rails if the preview arrows point the wrong way, because the direction decides the orientation of every frame.
