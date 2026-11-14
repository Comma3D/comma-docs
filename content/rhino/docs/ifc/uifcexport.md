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
6. Tick the checkboxes you need (IFC4X3 Bridge mode, Optimize IFC4 mesh, Export detailed report).
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
| Shared origin label | Information | Shows the shared origin from IFC.Offset X, Y and Z, or a warning to run uIfcSetupTemplateFile. |

IFC type is read from the object user text `IfcType` (or `IFC.Type`), then from a type token in the layer path, otherwise IfcBuildingElementProxy is used. The layer path is read as segment 0 Project, 1 Site, 2 Building, 3 Storey, and the rest is group and name. After export, missing Document User Text keys (site placement, project, site and building names, storey elevations, map conversion) are written for you. Existing keys are never overwritten.

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
