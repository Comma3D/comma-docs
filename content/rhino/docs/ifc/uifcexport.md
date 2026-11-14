---
title: uIfcExport
weight: 2
aliases:
  - /help/uifcexport/
---

| Menu | Command |
| --- | --- |
| `commaMenu` → **IFC** | `uIfcExport` |

Exports the selection to IFC through Python ifcopenshell or Xbim after an options dialog. Default SitePlacement is Local (OpenBIM). Missing SitePlacement / MapConversion values are seeded into Document User Text when needed.

#### Steps

1. Select objects to export to IFC`.


#### Options

| Option | What it does |
| --- | --- |
| Save path / Engine | Python or Xbim. |
| Schema | IFC2x3 / IFC4 / IFC4.3. |
| Meshing | Render Mesh or Detail Mesh (+ max angle / edge). |
| IFC4X3 Bridge / Optimize IFC4 mesh / detailed .log | Schema extras. |

## Document User Text

Run [`uIfcSetupTemplateFile`](../uifcsetuptemplatefile/) before a serious export. Check keys in **Document Properties → User Text**.

| Key | Default | Meaning |
| --- | --- | --- |
| `IFC.SitePlacement` | `Local` | Site Z = 0. `Anchor` / `Mean` / `Legacy` use older site anchoring. |
| `IFC.Storey.{Building}.{Storey}.Elevation` | min Z if unset | Storey elevation; name must match layer path segment 4. |
| `IFC.MapConversion.*` | seeded when Local and empty/0 | Georeference. |
| `IFC.Offset.X/Y/Z` | `0` | Geometry offset, independent of MapConversion. |
| `IFC.Schema` | `IFC4` | `IFC4` / `IFC2X3` / `IFC4X3`. |
| `IFC.UseBridge` | off | `True` with IFC4X3 uses IfcBridge / IfcBridgePart. |

Property types live in the key. See [`uIfcApplySharedParams`](../uifcapplysharedparams/).
