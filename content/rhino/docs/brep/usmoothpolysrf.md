---
title: uSmoothPolySrf
weight: 4
aliases:
  - /help/usmoothpolysrf/
---

| Menu | Command |
| --- | --- |
| `commaMenu` → **Brep** | `uSmoothPolySrf` |

Turns many surface or brep segments into one smooth lofted result along a direction curve. It works like uCombineNurbs but is tuned for closed profiles, so it closes the loft and sorts sections by boundary by default.

#### Steps

1. Run `uSmoothPolySrf`. The prompt reads `Select Breps or surfaces`.
2. Set the options on the same prompt (same list as uCombineNurbs; values are remembered).
3. Select the objects and press Enter.
4. At `Select direction curve` pick a curve that runs along the structure.
5. If `GuidePoints` is Yes, pick at least two points at `Guide point (Enter when done)`.
6. Edges parallel to the direction are collected, joined, aligned, sorted and rebuilt to degree 3 sections, then lofted.
7. The new surfaces are added with the chosen `BakeMode`, grouped as `LoftedGroup` when `GroupResult` is Yes, and the originals are deleted when `DeleteOriginal` is Yes.

#### Options

| Option | Values | What it does |
| --- | --- | --- |
| DirectionMode | Line, Curve (default Curve) | How edges are matched to the direction curve. |
| BakeMode | ByLayer, ByObject (default ByLayer) | Where color, material and print settings come from. |
| AngleTolerance | 0 to 90 degrees, default 15 | Maximum angle between an edge and the direction. |
| SampleCount | 1 to 50, default 3 | Sample points per edge in Curve mode. |
| SplitZone | No, Yes (default No) | Splits sections into overlap zones. |
| SegmentLength | 1 to 100000, default 500 | Target control-point spacing of rebuilt sections. |
| JoinTolerance | 0 to 500, default 1.0 | Distance used when joining edges. |
| ClosedLoft | No, Yes (default Yes) | Closes the loft from last section to first. |
| SortByBoundary | No, Yes (default Yes) | Sorts sections by boundary position. |
| GuidePoints | No, Yes (default No) | Asks for guide points that define the order. |
| PairSimilar | No, Yes (default No) | Pairs similar sections before lofting. |
| DeleteOriginal | No, Yes (default No) | Deletes the source objects after success. |
| GroupResult | No, Yes (default Yes) | Groups results as LoftedGroup. |
| CapResult | No, Yes (default No) | Caps planar holes of the results. |
| ShowIsocurves | No, Yes (default No) | Shows or hides isocurves on the result. |

Differences from uCombineNurbs: ClosedLoft and SortByBoundary default to Yes, and the result group is named LoftedGroup.
