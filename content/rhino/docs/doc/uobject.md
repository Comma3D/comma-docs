---
title: uObject
weight: 2
aliases:
  - /help/uobject/
---

| Menu | Command |
| --- | --- |
| `commaMenu` → **Doc** | `uObject` |

Opens the Comma Object dock panel to inspect the current selection and select similar objects. The panel lists the properties of the selected objects, and you tick the properties that matches must share before pressing Select Similar. Shortcuts to Heaviest, Visibility and FindBlock are built in.

#### Steps

1. Run `uObject`. The Comma Object panel opens with the status text `Select one or more objects to begin.`
2. Select one or more objects in the model. The panel groups them by object type and fills a grid with the columns Select, Property, Description and Value.
3. Use the `Property` and `Description` links in the `Visible:` row to show or hide those columns.
4. Tick `Select` on every property that matching objects must share. Layer, Name and Color are common to all types; each type adds its own rows (see the options table).
5. Use the per-type `All` and `None` links to tick or clear every row of one type. Use the `Area` and `Volume` links to switch those measures on, and the mm / m unit combo to read them in mm2 and mm3 or m2 and m3.
6. Optional: click `Tolerance` to set how close a number must be to count as a match (Length, Area, Volume, Other numeric %, display unit, Max seed objects).
7. Click `Select Similar`. Objects that match every ticked property are selected and the command line reports `[uObject - Select Similar] N object(s).`
8. Optional: click `Heaviest` (runs `uSelHeaviest`), `Visibility` (runs `uVisibility`) or `FindBlock` (runs `uFindCreateBlock`) without leaving the panel.

#### Options

| Option | Values | What it does |
| --- | --- | --- |
| Heaviest | Button | Runs uSelHeaviest: selects the heaviest objects in the model by memory estimate. |
| Visibility | Button | Runs uVisibility and opens the Comma Visibility hide/show panel. |
| FindBlock | Button | Runs uFindCreateBlock: finds rigidly copied assemblies and converts them to blocks. |
| Tolerance | Button | Opens the Configuration dialog: Length (default 1), Area (default 100), Volume (default 1000), Other numeric % (default 1.0), display unit (millimeters by default, meters optional) and Max seed objects (1 to 500, default 20). |
| Property / Description | Links | Toggle the Property and Description columns of the grid. |
| Select (checkbox) | Per row | Marks a property as a matching rule for Select Similar. |
| All / None | Per object type | Ticks or clears every property row in that type group. |
| Area / Volume | Per type links with mm or m unit combo | Computes area (mm2 or m2) or volume (mm3 or m3) on demand for the type group. |
| Common rows | Layer, Name, Color | Properties shared by all object types. |
| Curve rows | Curve subtype, Length, Closed, Planar, Radius, Major radius, Minor radius, Arc angle, Segment count, Degree, Control point count | Geometry rows offered for curves. |
| Brep and surface rows | Solid, Area, Volume, Face count, Edge count, Vertex count | Geometry rows offered for polysurfaces and surfaces. |
| Block rows | Block definition, Mirrored, Uniform scale, Scale factor, Scale X, Scale Y, Scale Z | Rows offered for block instances. |
| Text, hatch and point rows | Text height, Font, Hatch pattern, Pattern scale, Point count | Rows offered for annotation text, hatches and point objects. |
| Select Similar | Button | Selects all matching objects in the model. |

When more objects are selected than Max seed objects, only the first N are inspected to build the property list.
