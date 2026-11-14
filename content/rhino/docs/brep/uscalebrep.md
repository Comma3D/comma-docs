---
title: uScaleBrep
weight: 1
aliases:
  - /help/uscalebrep/
---

| Menu | Command |
| --- | --- |
| `commaMenu` → **Brep** | `uScaleBrep` |

Scales polysurfaces, surfaces and meshes about their own centroid, so each object shrinks or grows in place. Several objects are scaled in one go, each about its own center.

#### Steps

1. Run `uScaleBrep`. The prompt reads `Select Brep/Mesh/Surface to scale`.
2. Select the objects and press Enter.
3. Enter the `Scale Factor` (default 0.9).
4. Each object is scaled uniformly about its own centroid. For a brep the area centroid is used (bounding box center as fallback); for a mesh the volume centroid, then the area centroid, then the bounding box center.

#### Options

| Option | Values | What it does |
| --- | --- | --- |
| Scale Factor | Number, default 0.9 | Uniform scale applied about each object centroid. |
