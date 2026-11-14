---
title: uVolume
weight: 12
aliases:
  - /help/uvolume/
---

| Menu | Command |
| --- | --- |
| `commaMenu` → **Drafting** | `uVolume` |

Adds up the volume of closed polysurfaces and meshes. The result is shown in cubic meters by default.

#### Steps

1. Run `uVolume`.
2. At `Select Closed Brep/Mesh` pick the solids. Set `BakeResult` and `UnitDisplay` first if needed.
3. Press Enter. The total volume is printed with its unit and copied to the clipboard.
4. With `BakeResult` Yes a text dot `V: ...` is added on the layer `CheckVolume`.

#### Options

| Option | Values | What it does |
| --- | --- | --- |
| BakeResult | No, Yes (default No) | Adds a text dot with the volume. |
| UnitDisplay | Document, Meters (default Meters) | Unit of the result. |
