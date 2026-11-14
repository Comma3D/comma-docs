---
title: u3dSlope
weight: 14
aliases:
  - /help/u3dslope/
---

| Menu | Command |
| --- | --- |
| `commaMenu` → **Drafting** | `u3dSlope` |

Measures the 3D slope between two points as vertical rise over horizontal distance. The result can be a percentage or a ratio.

#### Steps

1. Run `u3dSlope`.
2. Optional: set `BakeResult`, `Display` (Percent or Ratio) and `Scale`.
3. Pick `Pick Point 1 (Top/Bottom)`.
4. Pick `Pick Point 2`.
5. The slope (vertical divided by horizontal) is printed and copied to the clipboard. Percent output is signed, for example +2.50%.
6. With `BakeResult` Yes a line and a text dot are added on the layer `CheckSlope3D`.

#### Options

| Option | Values | What it does |
| --- | --- | --- |
| BakeResult | No, Yes (default No) | Adds a line and a text dot. |
| Display | Percent, Ratio (default Percent) | Shows the slope as a percent or a ratio. |
| Scale | 0 to 1000, default 0 | Ratio scale. With a value of 0.1 or more the ratio is shown as rise:run scaled; otherwise as 1:N. |

Points with no horizontal distance report Vertical. Level points report 0% or 0:1.
