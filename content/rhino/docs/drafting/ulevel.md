---
title: uLevel
weight: 7
aliases:
  - /help/ulevel/
---

| Menu | Command |
| --- | --- |
| `commaMenu` → **Drafting** | `uLevel` |

Reads the level (height) of a picked point along an axis, measured from the world origin or the construction plane. Use it to check elevations quickly.

#### Steps

1. Run `uLevel`.
2. Optional: set `BakeResult`, `UnitDisplay`, `Reference` (CPlane or World) and click the axis option to cycle between `AxisX`, `AxisY` and `AxisZ` (default Z).
3. At `Pick point` click the point to measure.
4. The level is the distance from the reference plane origin along the chosen axis. It is printed and copied to the clipboard.
5. With `BakeResult` Yes a line to the projected point and a text dot are added on the layer `CheckLevel`.

#### Options

| Option | Values | What it does |
| --- | --- | --- |
| BakeResult | No, Yes (default No) | Adds a line and a text dot to the model. |
| UnitDisplay | Document, Meters (default Document) | Unit of the result. |
| Reference | CPlane, World (default World) | Origin and axes used for the level. |
| Axis | AxisX, AxisY, AxisZ (default Z) | Axis along which the level is measured. Click to cycle. |
