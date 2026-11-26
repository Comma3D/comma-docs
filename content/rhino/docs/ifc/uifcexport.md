---
title: uIfcExport
weight: 2
aliases:
  - /help/uifcexport/
---

| Menu | Command |
| --- | --- |
| `commaMenu` → **IFC** | `uIfcExport` |

Exports the selected objects to an IFC file. The IFC type comes from object user text or the layer path, and the spatial structure (project, site, building, storey) comes from the layer path and the Document User Text.

#### Steps

1. Run `uIfcSetupTemplateFile` once to prepare layers and document keys, and run `uIfcApplySharedParams` if you want property sets.
2. Run `uIfcExport`. At `Select objects to export to IFC` pick the objects (preselected objects are accepted).
3. The modal dialog `uIfcExport - Export IFC` opens. Choose the `Save to` file with Browse.
4. Choose the `Engine`: `Python (ifcopenshell)` (default) or `Xbim C# native`, and the `Schema`: `IFC2x3`, `IFC4` (default) or `IFC4.3`.
5. Choose the `Meshing`: `Render Mesh (recommended)` or `Detail Mesh (slower)`. For Detail Mesh also set `Max angle (deg)` and `Max edge-to-surface`.
6. Tick the checkboxes you need (IFC4X3 Bridge mode, Optimize IFC4 mesh, Layer groups, Also save Model.html, Export detailed report).
7. Check the shared-origin label, then click `Export`.
8. The command line prints the exported, failed and skipped counts.

#### Options

| Option | Values | What it does |
| --- | --- | --- |
| Save to | IFC file path | Output file. Without a path the dialog shows `Please select a save location.` |
| Engine | Python (ifcopenshell), Xbim C# native (default Python) | Export engine. |
| Schema | IFC2x3, IFC4, IFC4.3 (default IFC4) | IFC schema. The default can come from the Document User Text key IFC.Schema. |
| Meshing | Render Mesh (recommended), Detail Mesh (slower) | Mesh quality used to write geometry. |
| Max angle (deg) | 5 to 35, default 20 | Detail Mesh only: maximum angle between faces. |
| Max edge-to-surface | Number, default 1.0 document units | Detail Mesh only: maximum distance between mesh edges and the surface. |
| IFC4X3 Bridge mode | On, off | Only visible with IFC4.3. Also driven by IFC.UseBridge. |
| Optimize IFC4 mesh (IfcTriangulatedFaceSet) | On, off (default on) | Writes compact triangulated face sets. Ignored for IFC2x3. |
| Export detailed report to Desktop (.log) | On, off | Writes a log file. |
| Layer groups below the storey (IfcGroup) | On, off (default off) | Each layer level under Project::Site::Building::Storey becomes a group, so a viewer can show the layer tree. Objects stay in their storey. |
| Also save Model.html (viewer + attribute editor) | On, off (default off) | Writes Model.html next to the IFC: an offline viewer and attribute editor. For an IFC from another program use uIfcExportHtml. |
| Structure line | Information | The tree the layers give: sites, buildings, storeys, an example path, and how many objects go to Default. Check it before Export when layers are not set up with uIfcSetupTemplateFile. |
| Shared origin label | Information | Shows the shared origin from IFC.Offset X, Y and Z, or a warning to run uIfcSetupTemplateFile. |

IFC type is read from the object user text `IfcType` (or `IFC.Type`), then from a type token in the layer path, otherwise IfcBuildingElementProxy is used. Every IFC4 element class is written as itself (beams, railings, piles, fasteners).

#### Layers

| Layer path | Spatial structure | `Rhino.Layer` property |
| --- | --- | --- |
| 4 segments or more: `Project::Site::Building::Storey::…` | From the first four segments | The rest of the path |
| Fewer than 4 segments (`Walls`, `A::B`) | One Default site, building and storey | The whole layer path |

So a model with any layer names exports. The layer is never lost: it is written as the property `Rhino.Layer`.

#### What is written

- Property keys with a type (`Key[Length]`, `Key[Area]`…) keep their IFC type. `Qto_*` sets are written as quantities (IfcElementQuantity).
- `IfcPredefinedType`, `IfcObjectType`, `IfcDescription`, type objects and presentation layers from [`uIfcImport`](../uifcimport/) are written back.
- Identical meshes (bolts, repeated plates) share one geometry, which keeps files small.
- IFC2x3 files carry the owner history and composition type that the schema requires.
- `IFC4.3` always uses the Python engine.
- `Also save Model.html` writes a viewer and attribute editor next to the IFC. It opens offline in a browser. Its `Attributes` download goes back into Rhino with uAttribute `Import…`. After export, missing Document User Text keys (site placement, project, site and building names, storey elevations, map conversion) are written for you. Existing keys are never overwritten.

## Document User Text

Run [`uIfcSetupTemplateFile`](../uifcsetuptemplatefile/) before a serious export. Check or edit these keys in **Document Properties -> User Text**.

| Key | Default | Meaning |
| --- | --- | --- |
| `IFC.SitePlacement` | `Local` | `Local`: the site is placed at Z = 0, the engineering elevation stays on the object, and each storey placement Z equals its storey Elevation. `Anchor`, `Mean` or `Legacy` anchor the site at the mean XYZ of the objects (older behavior). |
| `IFC.Storey.{Building}.{Storey}.Elevation` or `IFC.Storey.{Storey}.Elevation` | Lowest Z of the storey objects when not set | Storey elevation. The name must match the storey segment of the layer path. |
| `IFC.MapConversion.Eastings`, `Northings`, `OrthogonalHeight` | `0` | Map conversion origin. With `Local` placement and a value of 0 (unset), export writes the mean XY and the mean Z (or `IFC.Offset.Z`). |
| `IFC.Offset.X`, `IFC.Offset.Y`, `IFC.Offset.Z` | `0` | Geometry offset, independent of the map conversion. |
| `IFC.Schema` | `IFC4` | Default schema (`IFC4`, `IFC2X3` or `IFC4X3`). |
| `IFC.UseBridge` | `False` | With `IFC4X3`, `True` writes IfcBridge and IfcBridgePart. |
