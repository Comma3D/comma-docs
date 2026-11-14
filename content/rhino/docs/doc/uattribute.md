---
title: uAttribute
weight: 4
aliases:
  - /help/uattribute/
---

| Menu | Command |
| --- | --- |
| `commaMenu` → **Doc** | `uAttribute` |

Opens the Comma Attribute Manager, a modeless table of object Layer, Name, Color and user-text keys. You can edit values in bulk, group and color objects by a key, calculate area and volume, and import or export the table as CSV or JSON.

#### Steps

1. Run `uAttribute`. The Comma Attribute Manager opens as a modeless window.
2. Choose the scope in the dropdown: `Selected`, `Visible` (default) or `All`.
3. Click `Sync` to read Layer, Name, Color and the user-text keys of those objects into the grid. Clicking a row selects that object in the model.
4. Click `Attribute` to open the Filter Keys dialog and choose which user-text keys become columns. Tick keys, add or remove keys with `+` and `-`, reorder with the arrows, use `All` / `None`, save presets, then `Apply`.
5. Edit cells in the grid. Nothing is written to the objects until you click `Set`.
6. Click `Set` to apply the edits to the objects. If you close the window with unsaved edits, a prompt offers `Set`, `Ignore`, `Export` or `Cancel`.
7. Optional: pick a key in the group-by dropdown to color-code the model and the rows by value. Use `Group` to collapse or expand rows with the same value and `Clear Color` to restore the original colors.
8. Optional: type in the search box (`Search name, key, value...`) to filter rows.
9. Optional: click `Cal Volume` or `Cal Area` to calculate measures for the rows, using the unit combo (`mm` or `m`, default `m`).
10. Optional: `Import` a CSV or JSON file to update rows matched by Id, or `Export` the grid to CSV keyed by Id. Click `Close` when finished.

#### Options

| Option | Values | What it does |
| --- | --- | --- |
| Scope | Selected, Visible, All (default Visible) | Chooses which objects `Sync` reads. |
| Sync | Button | Reads Layer, Name, Color and user-text keys into the grid. The status line reads: Sync once - row click selects in the model. |
| Set | Button | Writes grid edits back to the objects. |
| Attribute | Button | Opens Filter Keys: key checklist, preset Save / Load / Delete, + / - / up / down, All / None, Apply / Cancel. |
| Group by | Dropdown of keys | Color-codes model objects and grid rows by the chosen key value. |
| Clear Color | Button | Removes the group colors from model and grid. |
| Group | Toggle button | Collapses or expands rows that share a value. |
| Cal Volume | Button | Calculates volume for the rows. |
| Cal Area | Button | Calculates area for the rows. |
| Unit | mm, m (default m) | Unit used by Cal Volume and Cal Area. |
| Import | CSV or JSON file | Matches rows by Id and updates attributes. |
| Export | CSV file | Saves the grid with the Id column. |
| Search | Text | Filters rows by name, key or value. |
| Close | Button | Closes the manager (asks about unsaved edits). |

The grid reflects the model at the time of the last Sync. Run Sync again after changing the model in Rhino.
