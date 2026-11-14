---
title: uCombineNurbs
weight: 2
aliases:
  - /help/ucombinenurbs/
---

| Menu | Command |
| --- | --- |
| `commaMenu` → **Brep** | `uCombineNurbs` |

Builds one continuous lofted surface set from many separate surfaces or breps that follow the same direction, such as a deck, tunnel or pipe cut into segments. It collects the edges that run along a direction curve, joins and rebuilds them into smooth sections, then lofts through them.

#### Steps

1. Run `uCombineNurbs`. The prompt reads `Select Breps or surfaces to combine`.
2. Set the options on the same prompt (see the table): direction mode, angle tolerance, sample count, split zone, segment length, join tolerance, loft and result options. Option values are remembered between runs.
3. Select the breps or surfaces and press Enter.
4. At `Select direction curve` pick a curve that runs along the long direction of the structure.
5. If `GuidePoints` is Yes, pick points at `Guide point (Enter when done)` (at least two) to define the order of the sections.
6. The command collects edges parallel to the direction. In `Line` mode an edge must be within the angle tolerance of the direction. In `Curve` mode, sample points on each edge are compared with the direction curve tangent. Fewer than two edges stops with `Not enough edges parallel to direction (need >= 2).`
7. Edges are joined, converted to smooth section curves and aligned in the same direction. With `SplitZone` Yes the sections are cut into zones where they overlap.
8. Sections are sorted along the direction curve (or by boundary, or by the guide points), rebuilt to degree 3 with at least 4 control points and about one point per `SegmentLength`, and lofted with a straight (ruled) loft.
9. Results are added using `BakeMode`, optionally capped, optionally grouped as `CombinedGroup`, and the originals are deleted when `DeleteOriginal` is Yes. The command line reports `Combined into N surface(s).`

#### Options

| Option | Values | What it does |
| --- | --- | --- |
| DirectionMode | Line, Curve (default Curve) | How edges are matched to the direction curve: Line uses one overall direction, Curve compares the tangent at sample points. |
| BakeMode | ByLayer, ByObject (default ByLayer) | ByLayer takes color, material, linetype and print settings from the layer. ByObject copies the source object overrides. |
| AngleTolerance | 0 to 90 degrees, default 15 | Maximum angle between an edge and the direction for the edge to be used. |
| SampleCount | 1 to 50, default 3 | Sample points per edge in Curve mode. |
| SplitZone | No, Yes (default No) | Splits sections into overlap zones before lofting. |
| SegmentLength | 1 to 100000, default 500 | Target spacing for control points when sections are rebuilt. |
| JoinTolerance | 0 to 500, default 1.0 | Distance used when joining edges into section curves. |
| ClosedLoft | No, Yes (default No) | Closes the loft from the last section back to the first. |
| SortByBoundary | No, Yes (default No) | Sorts sections by boundary position instead of along the direction curve. |
| GuidePoints | No, Yes (default No, not remembered) | Asks for guide points that define section order. |
| PairSimilar | No, Yes (default No) | Pairs sections of similar shape, lofts inside each pair and bridges between neighbouring pairs. |
| DeleteOriginal | No, Yes (default No) | Deletes the source objects after the result is created. |
| GroupResult | No, Yes (default Yes) | Groups the new surfaces as CombinedGroup. |
| CapResult | No, Yes (default No) | Caps planar holes of each result. |
| ShowIsocurves | No, Yes (default No) | Shows isocurves on the result (wire density 1) or hides them. |

uSmoothPolySrf uses the same workflow with different defaults.
