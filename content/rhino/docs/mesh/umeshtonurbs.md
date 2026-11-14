---
title: uMeshToNurbs
weight: 2
aliases:
  - /help/umeshtonurbs/
---

| Menu | Command |
| --- | --- |
| `commaMenu` → **Mesh** | `uMeshToNurbs` |

Converts meshes, typically imported IFC meshes, into NURBS breps. Presets trade speed against fit, and an Advanced set of options exposes the detailed conversion controls. Pieces that cannot be converted safely stay as meshes and are reported.

#### Steps

1. Run `uMeshToNurbs`. The prompt reads `Select IFC meshes (Enter = all meshes)`. Select meshes, or press Enter to take every mesh in the model, including hidden and locked ones.
2. Choose `Quality`: `Fast`, `Balanced` (default) or `Tight`. Choose `Output`: `Replace` (default) or `Copy`.
3. Optional: set `Advanced` to Yes to reveal `Mode`, `Method`, `HealOpen`, `Tolerance`, `TimeLimit`, `MaxFaces`, `CheckObjects` and `Report`. Advanced resets to No at every run.
4. Press Enter to start. A progress meter runs; press Esc to cancel.
5. Each mesh is classified: OK, OK_FACETED, PARTIAL (the converted pieces become NURBS, pieces that need checking stay as meshes and are selected) or CHECK (the mesh is kept).
6. Read the summary and the suggestions for meshes that were not converted. If `Report` is Yes a CSV file is written.

#### Options

| Option | Values | What it does |
| --- | --- | --- |
| Quality | Fast, Balanced, Tight (default Balanced) | Fast makes faceted breps only. Balanced uses the smart pipeline. Tight prefers analytic surfaces with stricter circle and merge settings. |
| Output | Replace, Copy (default Replace) | Replace deletes the source meshes; Copy keeps them. |
| Advanced | No, Yes (default No) | Shows the advanced options below. Reset to No on each run. |
| Mode | Auto, Primitives, Pipe, Extrude, Freeform | Which shape recognition strategy is used. |
| Method | Smart, Faceted, Analytic | Conversion method. |
| HealOpen | No, Yes (default Yes) | Tries to close small gaps in open meshes before conversion. |
| Tolerance | 0 to 100, default 0 | Fit tolerance. 0 detects the resolution of the IFC data automatically. |
| TimeLimit | 1 to 600 seconds, default 5 | Time allowed for each object. |
| MaxFaces | 0 to 1000000, default 0 | Only meshes with at most this many faces are converted. 0 turns the filter off. |
| CheckObjects | KeepMesh, ToBrep | What to do with pieces that need checking: keep them as meshes, or convert them to faceted breps. |
| Report | No, Yes | Writes a CSV named &lt;name&gt;_NURBS_&lt;yyyyMMdd_HHmm&gt;_report.csv next to the document, or on the Desktop if the document is not saved. |

Use Copy first on large files so the original meshes stay available for comparison.
