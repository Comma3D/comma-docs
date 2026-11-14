---
title: uFlipCrv
weight: 2
aliases:
  - /help/uflipcrv/
---

| Menu | Command |
| --- | --- |
| `commaMenu` → **Curve** | `uFlipCrv` |

Makes the direction of many curves agree with a vector or a guide curve. Only curves that point against the chosen direction are reversed.

#### Steps

1. Run `uFlipCrv`. The prompt reads `Select curves to flip`. Select the curves and press Enter.
2. At `Pick flip vector start point` either click a start point, or choose an option: `X`, `Y`, `Z` (world axis direction) or `Crv` (guide curve).
3. After a start point, pick `Pick flip vector end point`. A rubber-band line shows the vector. The `X`, `Y`, `Z` and `Crv` options remain available.
4. With `Crv`, select the guide curve at `Select guide curve`. Each curve is compared with the guide tangent at the point of the guide closest to the start of that curve.
5. A curve is reversed when its start tangent points against the chosen direction. The command line reports `Flipped N of M curve(s).`
6. A vector that is too short stops with `Flip vector is too short.`

#### Options

| Option | Values | What it does |
| --- | --- | --- |
| X | Immediate | Uses the world X axis as the flip direction. |
| Y | Immediate | Uses the world Y axis as the flip direction. |
| Z | Immediate | Uses the world Z axis as the flip direction. |
| Crv | Select guide curve | Uses the tangent of a guide curve near each curve as the direction. |
