---
title: uTryGetCircle
weight: 4
aliases:
  - /help/utrygetcircle/
---

| Menu | Command |
| --- | --- |
| `commaMenu` → **Curve** | `uTryGetCircle` |

Replaces curves that are really circles or arcs (for example from CAD or meshes) with true circle and arc curves. It reports how far each fit deviates from the original.

#### Steps

1. Run `uTryGetCircle`. The prompt reads `Select curves to fit as circles or arcs`.
2. Select the curves and press Enter.
3. Each curve is sampled at 48 points. The command tries native circle and arc recognition and a sampled fit, then keeps the better result.
4. Closed curves become circles. Open curves become arcs that keep their end points. Each result replaces the original curve.
5. Read the report `Fitted X circles and Y arcs. Failed: Z. Max deviation ...` with the document tolerance for comparison.

The document tolerance is only reported. A fit that exceeds it is still kept and counted as `Over-tolerance: N (kept best fit)`, so check that number. uTryGetArc is a legacy alias.
