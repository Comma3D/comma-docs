---
title: uSlope
weight: 13
aliases:
  - /help/uslope/
---

| Menu | Command |
| --- | --- |
| `commaMenu` → **Drafting** | `uSlope` |

Measures the slope between two points in a plane (run along X, rise along Y of the chosen plane), or draws a line at a given slope percent. The slope can be shown as a percentage or as a ratio.

#### Steps

1. Run `uSlope`.
2. Optional: set `BakeResult`, `Display` (Percent or Ratio), `Scale`, `Plane` (CPlane or World), `Draw` and `Slope`.
3. Pick `Pick Point 1 (Top/Bottom)`.
4. In measure mode pick Point 2. The slope between the points is printed and copied to the clipboard. Horizontal run is taken along X and rise along Y of the plane.
5. With `Draw` Yes the command instead asks `Pick run direction/length (line will be drawn at slope)` and draws a line from Point 1 at the `Slope` percent.
6. `BakeResult` or `Draw` adds a line and a text dot on the layer `CheckSlope`.

#### Options

| Option | Values | What it does |
| --- | --- | --- |
| BakeResult | No, Yes (default No) | Adds a line and a text dot. |
| Display | Percent, Ratio (default Percent) | Shows the slope as a signed percent or as a ratio. |
| Scale | 0 to 1000, default 0 | Ratio scale. For example 4 gives 4:6 for a 1:1.5 slope. 0 turns it off and shows 1:N. |
| Plane | CPlane, World (default World) | Plane used to split the points into run and rise. |
| Draw | No, Yes (default No) | Draws a line at the given slope instead of measuring. |
| Slope | -1000 to 1000, default 2 | Slope percent used when Draw is Yes (for example 2 for 2 percent). |

A vertical pair of points reports Vertical, and a flat pair reports 0% or 0:1.
