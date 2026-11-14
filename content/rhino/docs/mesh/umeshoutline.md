---
title: uMeshOutline
weight: 3
aliases:
  - /help/umeshoutline/
---

| Menu | Command |
| --- | --- |
| `commaMenu` → **Mesh** | `uMeshOutline` |

Creates the outer outline curves of surfaces, polysurfaces and meshes as seen from a plane. Outlines are placed on layers named Outline::&lt;source layer&gt; and can be merged by layer, by object or all together.

#### Steps

1. Run `uMeshOutline`. The prompt reads `Select objects to outline` (surfaces, polysurfaces, meshes).
2. Set `Plane` (`CPlane`, `World` or `View`; default CPlane) and `Merge` (`All`, `ByLayer` or `PerObject`; default ByLayer).
3. Select the objects and press Enter.
4. The shapes are projected onto the plane, merged according to `Merge` and the outer contour is kept.
5. Outline curves are created on the layer `Outline::<source layer path>` (`Outline::Merged` for All). PerObject outlines go under the source layer path. The color is copied from the source layer.
6. The command line reports `Done: N outline curve(s) created.`

#### Options

| Option | Values | What it does |
| --- | --- | --- |
| Plane | CPlane, World, View (default CPlane) | Projection plane for the outline. |
| Merge | All, ByLayer, PerObject (default ByLayer) | All makes one outline set, ByLayer one per source layer, PerObject one per object. |

Only the outer contour is created; holes are not outlined.
