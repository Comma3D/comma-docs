---
title: uPolyToNurbsCurve
weight: 3
aliases:
  - /help/upolytonurbscurve/
---

| Menu | Command |
| --- | --- |
| `commaMenu` → **Curve** | `uPolyToNurbsCurve` |

Converts polylines into smooth cubic NURBS curves that pass through the polyline vertices. Vertices that are closer together than the tolerance are dropped first.

#### Steps

1. Run `uPolyToNurbsCurve`. The prompt reads `Select polyline curves`.
2. Optional: set `Tolerance` (default 0.01, remembered between runs).
3. Select the polylines and press Enter.
4. For each polyline, vertices closer than the tolerance to the previously kept vertex are removed, and an interpolated degree 3 curve is built through the remaining vertices.
5. The new curve is added on the current layer and the original polyline is deleted. Curves that are not polylines are skipped.

#### Options

| Option | Values | What it does |
| --- | --- | --- |
| Tolerance | Number, default 0.01 | Minimum distance between kept vertices. |
