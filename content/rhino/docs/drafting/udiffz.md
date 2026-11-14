---
title: uDiffZ
weight: 8
aliases:
  - /help/udiffz/
---

| Menu | Command |
| --- | --- |
| `commaMenu` → **Drafting** | `uDiffZ` |

Measures the signed height difference between two points along a world axis (Z by default). The result is printed and copied to the clipboard.

#### Steps

1. Run `uDiffZ`.
2. At `First Point` pick the first point. `UnitDisplay` is available on this prompt.
3. At `Second Point` pick the second point. On this prompt you can set `BakeResult`, `UnitDisplay` and click the axis option to cycle `AxisX`, `AxisY`, `AxisZ` (default Z).
4. The signed difference (second minus first) along the chosen axis is printed and copied.
5. With `BakeResult` Yes a line and a text dot are added on the layer `CheckDiffZ`.

#### Options

| Option | Values | What it does |
| --- | --- | --- |
| BakeResult | No, Yes (default No) | Adds a line and a text dot to the model. |
| UnitDisplay | Document, Meters (default Document) | Unit of the result. |
| Axis | AxisX, AxisY, AxisZ (default Z) | World axis of the difference. |
