---
title: uGap
weight: 10
aliases:
  - /help/ugap/
---

| Menu | Command |
| --- | --- |
| `commaMenu` → **Drafting** | `uGap` |

Measures the gap between two objects: the minimum and maximum distance, and the local gap at any point you click on the source. Useful for checking clearances between surfaces, curves and breps.

#### Steps

1. Run `uGap`.
2. At `Select Source (Surface, Curve, Brep, or face/edge - Ctrl+Shift for face/edge)` pick the source.
3. At `Select Target (...)` pick the target.
4. The command line shows `Computing gap...` and then the prompt `Pick point on Source to measure gap (Enter = bake Min/Max)`.
5. Click a point on the source to read the local gap at that point. You can click as many points as you like.
6. Press Enter to finish. With `BakeResult` Yes the minimum gap line (cyan) and the maximum gap line (orange) are added with text dots, grouped, on the layer `CheckGap`.

#### Options

| Option | Values | What it does |
| --- | --- | --- |
| BakeResult | No, Yes (default No) | Adds the Min and Max gap lines to the model when you press Enter. |
| UnitDisplay | Document, Meters (default Document) | Unit of the printed values. |
