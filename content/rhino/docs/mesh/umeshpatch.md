---
title: uMeshPatch
weight: 1
aliases:
  - /help/umeshpatch/
---

| Menu | Command |
| --- | --- |
| `commaMenu` → **Mesh** | `uMeshPatch` |

Fills closed boundary curves with a relaxed quad-dominant mesh patch. Edge length, grading toward the boundary and relaxation are controlled with options.

#### Steps

1. Run `uMeshPatch`. The prompt reads `Select closed boundary curve(s) to patch`.
2. Set the options on the prompt: `BoundaryEdgeLength`, `Grading`, `RelaxIterations`, `SlideBoundary`, `RelaxMode`, `MatchAttributes`, `DeleteInput`.
3. Select one or more boundary curves that join into a closed loop and press Enter.
4. The command builds the mesh and prints the vertex and face counts. If the curves do not form one closed loop it reports `Could not build mesh (check curves are joinable to one closed loop).`

#### Options

| Option | Values | What it does |
| --- | --- | --- |
| BoundaryEdgeLength | Number, default 1.0 | Target mesh edge length along the boundary. |
| Grading | 1 to 1000, default 2.0 | Edge growth toward the middle. 1 means uniform. |
| RelaxIterations | 1 to 5000, default 200 | Number of smoothing passes. |
| SlideBoundary | Fixed, Slide (default Slide) | Whether boundary vertices may slide along the boundary during relaxation. |
| RelaxMode | Laplacian, Tensile (default Tensile) | Smoothing method. |
| MatchAttributes | No, Yes (default Yes) | Gives the mesh the layer and attributes of the first boundary curve. |
| DeleteInput | No, Yes (default No) | Deletes the boundary curves after the patch is created. |
