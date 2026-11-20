---
title: uIfcImport
weight: 1
aliases:
  - /help/uifcimport/
---

| Menu | Command |
| --- | --- |
| `commaMenu` → **IFC** | `uIfcImport` |

Imports one or many IFC files into Rhino as meshes or Breps, with layers built from the IFC spatial structure. You choose the engine, what to import, how layers and metadata are written, and an optional coordinate offset.

#### Steps

1. Run `uIfcImport`. The modal dialog `uIfcImport - Import IFC` opens.
2. Enter the path in the box (`File path(s) or folder...`): one file, several files separated by `;`, or a folder. Or use the file and folder buttons to browse.
3. Choose the `Engine`: `Rhino Built-in`, `IfcOpenShell (Hierarchy)` (default) or `xBIM (Direct Memory)`.
4. Tick what to import and how to handle the file, then set `Sharp edge angle` and the `Offset (m)` X, Y and Z.
5. Click `Import`. Layers are `<file name>::Site::Building::Storey::<object name>`. Objects with the same name share a layer (a trailing `:<id>` is dropped). A file exported by Comma keeps its own layers (`Rhino.Layer`). With `Organize layers by IFC type` the IFC type sits above the name. Sublayers you add under the name export unchanged; do not add layers above the storey.
6. The command line reports `Files: ok/total`.

#### Options

| Option | Values | What it does |
| --- | --- | --- |
| Engine | Rhino Built-in, IfcOpenShell (Hierarchy), xBIM (Direct Memory) (default IfcOpenShell) | Import engine. |
| Import Abstract/Spatial Elements (IfcSpace, IfcOpening...) | On, off (default off) | Also imports spaces and openings. |
| When selecting a folder: include IFC files in all subfolders | On, off (default off) | Searches subfolders when a folder is chosen. |
| If layer root exists | Replace existing (delete old objects), Skip file | What to do when the file layer root is already in the document. |
| Export detailed error/skip report to Desktop (.log) | On, off (default off) | Writes a log file. |
| IfcOpenShell: use native Brep when available (extrusions) | On, off (default off) | Creates Breps for extrusions instead of meshes. Only for IfcOpenShell. |
| Organize layers by IFC type | On, off (default off) | Off: Site, Building, Storey, object name. On: Site, Building, Storey, IFC type, object name. IfcType is stored on the object either way. |
| Write IFC metadata to Document User Text | On, off (default off) | Stores project data in Document User Text. With several files the keys are overwritten and the last file wins. |
| Write object UserText keys with [Type] | On, off (default off) | On writes keys like Pset.Name[Volume] = value so they can be re-exported. |
| Sharp edge angle | 0 to 180 degrees, default 80 | 0 makes every edge sharp, 180 makes all smooth. |
| Offset (m) X / Y / Z | Numbers, default 0 | Subtracted from real-world coordinates so the model sits near the origin. |

#### What is kept on each object

| Data | User text |
| --- | --- |
| Property sets and quantity sets (`Qto_*`) | `Pset.Name` keys. Lengths, areas, volumes, angles and masses are converted to SI (m, m², m³, rad, kg). |
| Entity attributes | `IfcType`, `IfcPredefinedType`, `IfcObjectType`, `IfcDescription`, `GlobalId` |
| Type object | `IfcTypeClass`, `IfcTypeName` |
| Presentation layer | `IfcPresentationLayer` |
| Nested buildings | Building names joined with ` › ` (for example `Val › Oost`) |

Files from Revit, Tekla and Allplan keep this data when you export them again with [`uIfcExport`](../uifcexport/). Check the layer tree after import. It is the same structure that uIfcExport reads back.
