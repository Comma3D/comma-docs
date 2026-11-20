# CommaRh updates

Short notes for Package Manager users.

## [26.2.0] - 2026-11-19

- Attribute Manager: project picklists fill class, values and IfcType from the layer name. Double-click Id to change the class and move the layer.
- IFC import and export keep units, quantities, types and layers from Revit, Tekla and Allplan files.
- IFC export works with any layer names; the layer is kept as the property Rhino.Layer.
- uIfcExportHtml writes Model.html next to an IFC file: an offline viewer and attribute editor.
- IFC export can group objects by the layers below the storey (IfcGroup, off by default).
- Attribute Manager: picklist filter takes several values; large tables edit much faster.
- Visibility panel filters by key and value; Ctrl / Shift multi-select, Alt+click isolates.
- IFC import puts objects of one name on one layer under the storey; Comma files keep their layers.
- IFC export shows the Site / Building / Storey tree your layers give before you export.
- commaMenu: launcher with search and a short description per command.
- Sort toolbar Loft has Type and Closed. Try Get Circle fits faceted circles to the true radius.
- Cleaner dialogs: buttons fit their text, one action row on the right.
- Runs on Rhino 8 and Rhino 9.

## [26.1.9] - 2026-11-14

- Attribute Manager and Visibility panels: faster Sync, Id-based CSV/JSON, group colors.
- DWG send: hatches stay in place (no Y-mirror); Import Unit default is From DWG.
- Merge layers by level moves objects up the tree; Face from direction has X/Y/Z/Pick preview + Flip.
- Help and About open the online docs website.

## [26.1.8] - 2026-11-11

- Mesh to NURBS handles tubes, fasteners, and multi-piece models better.
- Faster and more stable on large meshes.

## [26.1.7] - 2026-11-06

- Mesh to NURBS improved for beams, columns, and pipes.

## [26.1.6] - 2026-11-05

- DWG / AutoCAD export keeps curves joined more reliably.
- Better handling of large batches and freeform curves.

## [26.1.5] - 2026-11-04

- Cleaner curve export to AutoCAD.
- Simpler quality choice for mesh to NURBS; partial results keep the good pieces.

## [26.1.4] - 2026-11-03

- Fixes for current Rhino 8 / Windows setups.
- Mesh tools easier to find in the menu.
- Clearer IFC export defaults for site and storeys.

## [26.1.3] - 2026-11-03

- Package update (follow-up load fix in 26.1.4).

## [26.1.2] - 2026-10-18

- DWG and annotation stability improvements.
- IFC import layers follow the building structure by default.
- Menu and panels polished.

## [26.1.1] - 2026-10-16

- DWG stability in the Package Manager build.
- Packaging fixes for IFC tools.

## [26.1.0] - 2026-09-01

- Tools grouped by type: Doc, Curve, Surface, Brep, Mesh, Drafting, CAD, IFC.
- New object, tolerance, sort, and block-finding workflows.
- About and licence entry updated for this layout.

## [26.0.3] - 2026-08-26

- Clearer layer naming when using a main layer.

## [26.0.2] - 2026-08-04

- Optional main layer for nested layer buttons.

## [26.0.1] - 2026-07-19

- Mesh conversion and outline improvements.
- Licence and registration polish.

## [26.0.0] - 2026-07-07

- Signed licence keys.
- Typed IFC shared parameters.
