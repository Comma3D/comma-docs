---
title: uCombineNurbs
weight: 2
aliases:
  - /help/ucombinenurbs/
---

Where to find it: `commaMenu` → **Brep** → `uCombineNurbs`.

Extracts and direction-matches Brep or surface edges, rebuilds them, and loft-combines them. Preview first, then bake.

## Options

| Option | What it does |
| --- | --- |
| DirectionMode | Line or Curve. |
| BakeMode | ByLayer or ByObject. |
| AngleTolerance / SampleCount / SegmentLength / JoinTolerance | Rebuild and join controls. |
| SplitZone / ClosedLoft / SortByBoundary / GuidePoints / PairSimilar | Matching and loft behaviour. |
| DeleteOriginal / GroupResult / CapResult / ShowIsocurves | Yes/No result toggles. |

## Prompts

`Select Breps or surfaces to combine`; `Select direction curve`; `Guide point (Enter when done)`.

## Limits

Free/Trial: preview only; baking is disabled.
