---
title: uFlipSrf
weight: 1
aliases:
  - /help/uflipsrf/
---

| Menu | Command |
| --- | --- |
| `commaMenu` → **Surface** | `uFlipSrf` |

Makes the normals of many surfaces and polysurfaces point the same way as a vector or a guide curve. Only objects that point against the direction are flipped.

#### Steps

1. Run `uFlipSrf`. The prompt reads `Select surfaces to flip`. Select surfaces or polysurfaces and press Enter.
2. At `Pick flip vector start point` either click a start point or choose `X`, `Y`, `Z` (world axis) or `Crv` (guide curve).
3. After a start point, pick `Pick flip vector end point`; the vector is drawn as a rubber-band line.
4. With `Crv`, select the guide curve at `Select guide curve`. Each surface is compared with the guide tangent at the point closest to the surface centroid.
5. A surface is flipped when its reference normal (taken at the point nearest its centroid) points against the direction. The command line reports `Flipped N of M surface(s).`

#### Options

| Option | Values | What it does |
| --- | --- | --- |
| X | Immediate | Uses the world X axis as the target direction. |
| Y | Immediate | Uses the world Y axis as the target direction. |
| Z | Immediate | Uses the world Z axis as the target direction. |
| Crv | Select guide curve | Uses a guide curve tangent as the target direction. |

A vector shorter than the tolerance stops with `Flip vector is too short.`
