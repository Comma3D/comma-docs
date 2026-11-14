---
title: uArea
weight: 11
aliases:
  - /help/uarea/
---

| Menu | Command |
| --- | --- |
| `commaMenu` → **Drafting** | `uArea` |

Adds up the area of surfaces, polysurfaces, meshes, closed curves and hatches. The result is shown in square meters by default.

#### Steps

1. Run `uArea`.
2. At `Select Objects for Area` pick breps, meshes, closed curves or hatches. Set `BakeResult` and `UnitDisplay` first if needed.
3. Press Enter. The total area is printed with its unit (for example m2) and copied to the clipboard.
4. With `BakeResult` Yes a text dot `S: ...` is added on the layer `CheckArea`.

#### Options

| Option | Values | What it does |
| --- | --- | --- |
| BakeResult | No, Yes (default No) | Adds a text dot with the area. |
| UnitDisplay | Document, Meters (default Meters) | Unit of the result. |
