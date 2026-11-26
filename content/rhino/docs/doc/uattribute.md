---
title: uAttribute
weight: 4
aliases:
  - /help/uattribute/
---

| Menu | Command |
| --- | --- |
| `commaMenu` → **Doc** | `uAttribute` |

Opens the Comma Attribute Manager, a modeless table of object Layer, Name, Color and user-text keys. You edit values in bulk, fill them from a project picklist, group and color objects by a key, and exchange the table with the IFC editor (Model.html) as JSON matched by Id.

#### Steps

1. Run `uAttribute`. The Comma Attribute Manager opens.
2. Choose the scope (`Selected`, `Visible` or `All`) and, with `Object ▾`, which object kinds are read. Click `Sync`.
3. Click `Columns` to choose which user-text keys are shown.
4. Optional: click `Picklist` and load a picklist (Comma template `.xlsx`, Classification Manager workbook or `.json`). Tick one or more filter values (for example LOD or phase) in the menu next to it: the menu stays open while you tick, the table updates when it closes.
5. Edit cells. Nothing is written until you click `Set`. Columns with a tinted header and `▾` pick from a list: double-click the cell, type to search, press Enter. The value goes to every selected row when the clicked row is part of the selection.
6. Double-click an **Id** cell to open the **Properties** panel for that object (see below). Double-click a plain cell to zoom to the object.
7. Click `Set` to write the edits to the objects.

#### Picklist

A picklist lists the classes of a project (for example wall, beam, track) with their parameters and allowed values. When a picklist is loaded:

- The class of an object is found from its **layer name**. The first four layer segments (Project, Site, Building, Storey) are skipped when the path is longer than four segments.
- The other layer segments fill dropdown values when they match a value of the list exactly.
- `IfcType` is filled from the class.
- Fixed values of the class are written as they are.

Values are matched as written in the picklist. Nothing is translated. Use the search in the picklist or in Model.html to find a value in another language.

#### Properties panel (double-click Id)

| Part | What it does |
| --- | --- |
| Class | Dropdown of the picklist classes. Type to search. |
| Parameters | The parameters of the class, with dropdowns for listed values. |
| Apply | Writes the panel values to the object(s) of the panel only. |

When you pick another class, a prompt asks what to do with the layer:

| Choice | Result |
| --- | --- |
| Rename layer | Renames the object's layer to the class name. Every object on that layer follows. If a layer with that name exists next to it, the objects are merged into it. |
| New layer | Moves only the selected object(s) to a layer of the class name next to their own layer. |
| Cancel | Nothing changes. |

#### Toolbar

| Option | What it does |
| --- | --- |
| Scope | Selected, Visible, All (default Visible). |
| Sync / Set | Read the objects into the table / write the edits back. |
| Columns | Choose, order and save presets of the shown keys. |
| Group by, Collapse, Clear Color | Color model and rows by a key value, collapse rows, restore colors. |
| Picklist, filter ▾, ? | Load or save a picklist, filter its parameters (tick several values), open the picklist guide. |
| Object ▾ | Object kinds read by Sync. |
| Options ▾ | Cal Volume, Cal Area, units (m or mm), Import…, Export…. |
| Select all, None, Show, Hide, Isolate, Restore | Act on the objects of the rows shown. |
| Search | `ST*`, `Trade=STR`, `Layer=Walls::*`, `-Slab`, `STR|ARC`. |

#### Import and export

- `Export…` writes CSV or JSON keyed by Id.
- `Import…` reads CSV or JSON and updates objects matched by Id. Compressed IFC GlobalIds (22 characters) are accepted too.
- A JSON file downloaded from Model.html (`Attributes`) applies the class change: the `Rhino.Layer` value moves the object to that layer under the same Project::Site::Building::Storey. A key removed in Model.html is cleared on the object.

The table reflects the model at the last Sync. Run Sync again after changing the model in Rhino.
