---
title: uCombineNurbs
weight: 2
aliases:
  - /help/ucombinenurbs/
---

| Menu | Command |
| --- | --- |
| `commaMenu` → **Brep** | `uCombineNurbs` |

Extracts and direction-matches Brep or surface edges, rebuilds them, and loft-combines them. Preview first, then bake.

#### Steps

1. Select Breps or surfaces to combine
2. Select direction curve
3. Guide point (Enter when done)`.


#### Options

| Option | What it does |
| --- | --- |
| DirectionMode | Line or Curve. |
| BakeMode | ByLayer or ByObject. |
| AngleTolerance / SampleCount / SegmentLength / JoinTolerance | Rebuild and join controls. |
| SplitZone / ClosedLoft / SortByBoundary / GuidePoints / PairSimilar | Matching and loft behaviour. |
| DeleteOriginal / GroupResult / CapResult / ShowIsocurves | Yes/No result toggles. |
