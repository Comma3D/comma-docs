---
title: uScaleCrvAtt
weight: 1
aliases:
  - /help/uscalecrvatt/
---

| Menu | Command |
| --- | --- |
| `commaMenu` → **Curve** | `uScaleCrvAtt` |

Scales curves about their midpoint or extends their ends, replacing each curve in place so layer and attributes are kept. Switch between the two behaviours with the Mode option.

#### Steps

1. Run `uScaleCrvAtt`. The prompt reads `Select curves to scale` (or `Select curves to extend` when Mode is Extend).
2. Optional: set `Mode` to `Scale` or `Extend`. In Extend mode also set `Side` to `Both`, `Start` or `End`.
3. Select the curves and press Enter.
4. Enter `Scale Factor` (default 2, zero or more) in Scale mode, or `Extension length` (default 1000, zero or more) in Extend mode.
5. Scale mode scales each curve about its midpoint (the point at 50 percent of its length).
6. Extend mode extends each open curve smoothly at the chosen side(s). Closed curves cannot be extended; if nothing could be extended the command line says `Unable to extend selected curve(s).`

#### Options

| Option | Values | What it does |
| --- | --- | --- |
| Mode | Scale, Extend (default Scale) | Chooses between scaling and extending. |
| Side | Both, Start, End (default Both) | Which end to extend. Only shown in Extend mode. |
| Scale Factor | Number, default 2 | Scale mode multiplier about the midpoint. |
| Extension length | Number, default 1000 | Extend mode length added at each chosen end. |

Mode and Side are remembered between runs.
