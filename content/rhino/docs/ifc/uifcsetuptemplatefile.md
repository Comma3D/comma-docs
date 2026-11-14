---
title: uIfcSetupTemplateFile
weight: 3
aliases:
  - /help/uifcsetuptemplatefile/
---

| Menu | Command |
| --- | --- |
| `commaMenu` → **IFC** | `uIfcSetupTemplateFile` |

Prepares a document for IFC export: it creates a sample layer tree, writes the IFC Document User Text keys with placeholder values, and adds a few sample objects and a type catalog. Edit the placeholders, then use the layer pattern for your own model.

#### Steps

1. Open the Rhino document you want to prepare (a new empty file works best).
2. Run `uIfcSetupTemplateFile`. The command has no prompts.
3. It creates sample layers such as `MyProject::MainSite::Building01::GroundFloor::Case0_ExteriorWall`, `...::GroundFloor::Abutment LH1::Case1_AbutmentWall`, `...::GroundFloor::Pylon P01::Case2_PylonBody` and `...::GroundFloor::Case3_GenericElement`, plus a TypeCatalog layer.
4. It sets the Document User Text keys (schema, bridge flag, project, site and building names, author and contacts, storey elevation, offsets, site placement, map conversion and sample material keys).
5. It migrates and sets the `IFC.SharedParam.*[Type]` keys and creates sample objects with IfcType values (IfcWall twice, IfcColumn, IfcBuildingElementProxy) and a TypeCatalog_Sample object with one key per supported type.
6. Open **Document Properties -&gt; User Text** and replace the placeholders with your project values.
7. The command ends with the hint `Run uIfcApplySharedParams on selection, then uIfcExport.`

Keys written include IFC.Schema=IFC4, IFC.UseBridge=False, IFC.Storey.Building01.GroundFloor.Elevation=0.0, IFC.Offset.X, Y and Z = 0, IFC.SitePlacement=Local and the IFC.MapConversion keys (CRSName EPSG:4326, Eastings, Northings and OrthogonalHeight 0, XAxisAbscissa 1.0, XAxisOrdinate 0.0, Scale 1.0).
