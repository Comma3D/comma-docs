#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate Hugo markdown pages for CommaRh public commands.

Usage:  python _gen_commands.py

Writes one page per command to content/rhino/docs/<section>/<slug>.md
(relative to this script). Existing command pages are overwritten; section
_index.md files and other pages are not touched.

Page layout: front matter (title, weight, aliases) -> Menu|Command table ->
summary -> #### Steps -> #### Options (omitted when there are none) ->
notes -> extra markdown. No Limits / Free / Trial sections are written.
"""
import io
import os
import re
import sys

ROOT = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(ROOT, "content", "rhino", "docs")
ARROW = "\u2192"

SECTIONS = {
    "doc": "Doc", "curve": "Curve", "surface": "Surface", "brep": "Brep",
    "mesh": "Mesh", "drafting": "Drafting", "cad": "CAD", "ifc": "IFC",
    "more": "More",
}
NOT_ON_MENU = {"uquicktoolsconfig", "commamenu", "uexportbox", "uvisibilityadd"}
EXPECTED_COUNT = 48

# Command data: title, slug, section, group, onMenu, summary, steps,
# options [{name, values, does}], notes, extra.
COMMANDS = [{'title': 'uLayer',
  'slug': 'ulayer',
  'section': 'doc',
  'group': 'Doc',
  'onMenu': True,
  'summary': 'Opens the Comma Layer dock panel, or closes it when it is already open. The panel shows one '
             'button per layer you define in Setup, so you can move objects onto a layer, restyle them, or '
             'make a layer current with one click. Extra layer tools are in the Advance flyout of the panel.',
  'steps': ['Run `uLayer`. The Comma Layer panel docks next to the viewports. Run `uLayer` again to close '
            'it.',
            'Open `Setup` (button in the panel header, also listed in the `Advance` flyout). The `Comma '
            'Layer Setup` dialog has one row per layer with the columns Show, Map, Nickname, Layer Name, '
            'Color, Linetype and Print Width.',
            'In Setup, add rows with `+` or pull the layers that already exist in the document with `Get`. '
            'Fill in Nickname, Layer Name (use `::` for sublayers), Color, Linetype and Print Width, and '
            'tick `Show` for every row that should become a panel button.',
            'Use `Bake` in Setup to create or update the layers in the Rhino document, then `OK` to save the '
            'button set. Row order is changed with the up and down arrows; `All` / `None` tick or clear the '
            'Show column.',
            'Optional: save the whole button set as a preset with `Save`, switch with `Load`, remove with '
            '`Del`. Layer sets can also be moved between machines with `Import` / `Export` (JSON) or applied '
            'from a template file.',
            'Optional: in the panel, type a prefix in the Main layer box (for example `Main::`, `Main_` or '
            '`Main-`). A prefix ending in `::` (or no separator) nests the button layers under it as '
            'sublayers; `_` or `-` joins prefix and layer name into one flat layer name.',
            'Select objects in the model, then click a layer button. If nothing is selected, the command '
            'asks `Select objects for [layer]` and applies the click to the objects you pick.',
            'Choose the click type to decide what changes: left click moves the objects to the layer; '
            'Shift+left click only sets the object color from the button swatch; Ctrl+left click moves the '
            'objects and resets color, linetype and print width to By Layer.',
            'Right-click a button to make that layer the current layer. A filled dot on the button marks the '
            'current layer.',
            'Open `Advance` for related tools: `uMergeLayer`, `uReNameLayer`, `uBlockToLayer`, '
            '`uFindMainLayer`, `uApplyColorMap` (assign objects to layers by color) and `Setup`.'],
  'options': [{'name': 'Main layer prefix',
               'values': 'Text such as Main:: or Main_ or Main-',
               'does': 'Text box at the top of the panel. Prepended to every button layer name. Ending in '
                       '`::` creates nested sublayers; `_` or `-` creates a flat merged name.'},
              {'name': 'Left click',
               'values': 'Button',
               'does': 'Moves the selected objects to the button layer (creating or updating the layer '
                       'first). Without a selection it prompts for objects.'},
              {'name': 'Shift + left click',
               'values': 'Button',
               'does': 'Sets only the object color from the button swatch (color from object). Layer is '
                       'unchanged.'},
              {'name': 'Ctrl + left click',
               'values': 'Button',
               'does': 'Moves objects to the layer and sets color, linetype and print width to By Layer.'},
              {'name': 'Right click',
               'values': 'Button',
               'does': 'Sets the button layer as the current layer.'},
              {'name': 'Setup',
               'values': 'Button',
               'does': 'Opens Comma Layer Setup: Show, Map, Nickname, Layer Name, Color, Linetype, Print '
                       'Width, plus presets, Get, Bake, Search, templates and JSON import/export.'},
              {'name': 'Advance',
               'values': 'Flyout',
               'does': 'Lists uMergeLayer, uReNameLayer, uBlockToLayer, uFindMainLayer, uApplyColorMap and '
                       'Setup.'}],
  'notes': 'The button layers, colors and presets are stored per user, so the same panel layout is available '
           'in every document.',
  'extra': ''},
 {'title': 'uObject',
  'slug': 'uobject',
  'section': 'doc',
  'group': 'Doc',
  'onMenu': True,
  'summary': 'Opens the Comma Object dock panel to inspect the current selection and select similar objects. '
             'The panel lists the properties of the selected objects, and you tick the properties that '
             'matches must share before pressing Select Similar. Shortcuts to Heaviest, Visibility and '
             'FindBlock are built in.',
  'steps': ['Run `uObject`. The Comma Object panel opens with the status text `Select one or more objects to '
            'begin.`',
            'Select one or more objects in the model. The panel groups them by object type and fills a grid '
            'with the columns Select, Property, Description and Value.',
            'Use the `Property` and `Description` links in the `Visible:` row to show or hide those columns.',
            'Tick `Select` on every property that matching objects must share. Layer, Name and Color are '
            'common to all types; each type adds its own rows (see the options table).',
            'Use the per-type `All` and `None` links to tick or clear every row of one type. Use the `Area` '
            'and `Volume` links to switch those measures on, and the mm / m unit combo to read them in mm2 '
            'and mm3 or m2 and m3.',
            'Optional: click `Tolerance` to set how close a number must be to count as a match (Length, '
            'Area, Volume, Other numeric %, display unit, Max seed objects).',
            'Click `Select Similar`. Objects that match every ticked property are selected and the command '
            'line reports `[uObject - Select Similar] N object(s).`',
            'Optional: click `Heaviest` (runs `uSelHeaviest`), `Visibility` (runs `uVisibility`) or '
            '`FindBlock` (runs `uFindCreateBlock`) without leaving the panel.'],
  'options': [{'name': 'Heaviest',
               'values': 'Button',
               'does': 'Runs uSelHeaviest: selects the heaviest objects in the model by memory estimate.'},
              {'name': 'Visibility',
               'values': 'Button',
               'does': 'Runs uVisibility and opens the Comma Visibility hide/show panel.'},
              {'name': 'FindBlock',
               'values': 'Button',
               'does': 'Runs uFindCreateBlock: finds rigidly copied assemblies and converts them to blocks.'},
              {'name': 'Tolerance',
               'values': 'Button',
               'does': 'Opens the Configuration dialog: Length (default 1), Area (default 100), Volume '
                       '(default 1000), Other numeric % (default 1.0), display unit (millimeters by default, '
                       'meters optional) and Max seed objects (1 to 500, default 20).'},
              {'name': 'Property / Description',
               'values': 'Links',
               'does': 'Toggle the Property and Description columns of the grid.'},
              {'name': 'Select (checkbox)',
               'values': 'Per row',
               'does': 'Marks a property as a matching rule for Select Similar.'},
              {'name': 'All / None',
               'values': 'Per object type',
               'does': 'Ticks or clears every property row in that type group.'},
              {'name': 'Area / Volume',
               'values': 'Per type links with mm or m unit combo',
               'does': 'Computes area (mm2 or m2) or volume (mm3 or m3) on demand for the type group.'},
              {'name': 'Common rows',
               'values': 'Layer, Name, Color',
               'does': 'Properties shared by all object types.'},
              {'name': 'Curve rows',
               'values': 'Curve subtype, Length, Closed, Planar, Radius, Major radius, Minor radius, Arc '
                         'angle, Segment count, Degree, Control point count',
               'does': 'Geometry rows offered for curves.'},
              {'name': 'Brep and surface rows',
               'values': 'Solid, Area, Volume, Face count, Edge count, Vertex count',
               'does': 'Geometry rows offered for polysurfaces and surfaces.'},
              {'name': 'Block rows',
               'values': 'Block definition, Mirrored, Uniform scale, Scale factor, Scale X, Scale Y, Scale Z',
               'does': 'Rows offered for block instances.'},
              {'name': 'Text, hatch and point rows',
               'values': 'Text height, Font, Hatch pattern, Pattern scale, Point count',
               'does': 'Rows offered for annotation text, hatches and point objects.'},
              {'name': 'Select Similar',
               'values': 'Button',
               'does': 'Selects all matching objects in the model.'}],
  'notes': 'When more objects are selected than Max seed objects, only the first N are inspected to build '
           'the property list.',
  'extra': ''},
 {'title': 'uMove',
  'slug': 'umove',
  'section': 'doc',
  'group': 'Doc',
  'onMenu': True,
  'summary': 'Opens the U Move form to shift objects between local model coordinates and real-world (survey) '
             'coordinates using a saved offset and rotation. Real applies the offset, Local reverses it. '
             'Named offsets can be saved per project and reused.',
  'steps': ['Select the objects to transform. If nothing is selected when you click `Real` or `Local`, the '
            'command asks `Select objects to transform`.',
            'Run `uMove`. The U Move form opens and stays open while you work.',
            'Type a project name in the project combo box, or pick a saved one to load its values.',
            'Enter `X` and `Y` (required) and optionally `Z` and `R`. `Z` and `R` default to 0. `R` is a '
            'rotation in degrees.',
            'Click `Save` to store the current values under the project name, or `Delete` to remove the '
            'selected saved project.',
            'Click `Real` to go from local to real coordinates: objects are rotated by `R` about 0,0,0 and '
            'then moved by (X, Y, Z).',
            'Click `Local` to go back: objects are moved by (-X, -Y, -Z) and then rotated by -R about 0,0,0.',
            'Read the report label and the command line message `uMove: Transformed N object(s).` A message '
            'box confirms the operation; a model base point warning is added when Rhino has a model base '
            'point set.',
            'Close the form with `Cancel`.'],
  'options': [{'name': 'Project',
               'values': 'Saved name or new name',
               'does': 'Combo box that loads or names a saved offset.'},
              {'name': 'X', 'values': 'Number (required)', 'does': 'Move offset along X in model units.'},
              {'name': 'Y', 'values': 'Number (required)', 'does': 'Move offset along Y in model units.'},
              {'name': 'Z', 'values': 'Number (default 0)', 'does': 'Move offset along Z in model units.'},
              {'name': 'R',
               'values': 'Degrees (default 0)',
               'does': 'Rotation about 0,0,0 around the world Z axis.'},
              {'name': 'Save',
               'values': 'Button',
               'does': 'Stores the project values in the Comma settings file (UMoveConfig.json).'},
              {'name': 'Delete', 'values': 'Button', 'does': 'Removes the selected saved project.'},
              {'name': 'Real', 'values': 'Button', 'does': 'Rotate by R, then move by (X, Y, Z).'},
              {'name': 'Local', 'values': 'Button', 'does': 'Move by (-X, -Y, -Z), then rotate by -R.'},
              {'name': 'Cancel',
               'values': 'Button',
               'does': 'Closes the form without transforming anything.'}],
  'notes': 'Real followed by Local with the same values returns objects to their original position.',
  'extra': ''},
 {'title': 'uAttribute',
  'slug': 'uattribute',
  'section': 'doc',
  'group': 'Doc',
  'onMenu': True,
  'summary': 'Opens the Comma Attribute Manager, a modeless table of object Layer, Name, Color and user-text '
             'keys. You can edit values in bulk, group and color objects by a key, calculate area and '
             'volume, and import or export the table as CSV or JSON.',
  'steps': ['Run `uAttribute`. The Comma Attribute Manager opens as a modeless window.',
            'Choose the scope in the dropdown: `Selected`, `Visible` (default) or `All`.',
            'Click `Sync` to read Layer, Name, Color and the user-text keys of those objects into the grid. '
            'Clicking a row selects that object in the model.',
            'Click `Attribute` to open the Filter Keys dialog and choose which user-text keys become '
            'columns. Tick keys, add or remove keys with `+` and `-`, reorder with the arrows, use `All` / '
            '`None`, save presets, then `Apply`.',
            'Edit cells in the grid. Nothing is written to the objects until you click `Set`.',
            'Click `Set` to apply the edits to the objects. If you close the window with unsaved edits, a '
            'prompt offers `Set`, `Ignore`, `Export` or `Cancel`.',
            'Optional: pick a key in the group-by dropdown to color-code the model and the rows by value. '
            'Use `Group` to collapse or expand rows with the same value and `Clear Color` to restore the '
            'original colors.',
            'Optional: type in the search box (`Search name, key, value...`) to filter rows.',
            'Optional: click `Cal Volume` or `Cal Area` to calculate measures for the rows, using the unit '
            'combo (`mm` or `m`, default `m`).',
            'Optional: `Import` a CSV or JSON file to update rows matched by Id, or `Export` the grid to CSV '
            'keyed by Id. Click `Close` when finished.'],
  'options': [{'name': 'Scope',
               'values': 'Selected, Visible, All (default Visible)',
               'does': 'Chooses which objects `Sync` reads.'},
              {'name': 'Sync',
               'values': 'Button',
               'does': 'Reads Layer, Name, Color and user-text keys into the grid. The status line reads: '
                       'Sync once - row click selects in the model.'},
              {'name': 'Set', 'values': 'Button', 'does': 'Writes grid edits back to the objects.'},
              {'name': 'Attribute',
               'values': 'Button',
               'does': 'Opens Filter Keys: key checklist, preset Save / Load / Delete, + / - / up / down, '
                       'All / None, Apply / Cancel.'},
              {'name': 'Group by',
               'values': 'Dropdown of keys',
               'does': 'Color-codes model objects and grid rows by the chosen key value.'},
              {'name': 'Clear Color',
               'values': 'Button',
               'does': 'Removes the group colors from model and grid.'},
              {'name': 'Group',
               'values': 'Toggle button',
               'does': 'Collapses or expands rows that share a value.'},
              {'name': 'Cal Volume', 'values': 'Button', 'does': 'Calculates volume for the rows.'},
              {'name': 'Cal Area', 'values': 'Button', 'does': 'Calculates area for the rows.'},
              {'name': 'Unit',
               'values': 'mm, m (default m)',
               'does': 'Unit used by Cal Volume and Cal Area.'},
              {'name': 'Import',
               'values': 'CSV or JSON file',
               'does': 'Matches rows by Id and updates attributes.'},
              {'name': 'Export', 'values': 'CSV file', 'does': 'Saves the grid with the Id column.'},
              {'name': 'Search', 'values': 'Text', 'does': 'Filters rows by name, key or value.'},
              {'name': 'Close',
               'values': 'Button',
               'does': 'Closes the manager (asks about unsaved edits).'}],
  'notes': 'The grid reflects the model at the time of the last Sync. Run Sync again after changing the '
           'model in Rhino.',
  'extra': ''},
 {'title': 'uSort',
  'slug': 'usort',
  'section': 'doc',
  'group': 'Doc',
  'onMenu': True,
  'summary': 'Opens the Comma Sort floating toolbar that sorts the selected objects by axis, radial position '
             'or guide curve and remembers that order. The saved order can then be injected into another '
             "command's object prompt, or baked into groups, lofts, curves and polylines.",
  'steps': ['Select at least two objects in the model, then run `uSort`. The Comma Sort toolbar appears; its '
            'label reads `Select -> sort` until you sort.',
            'Click `X`, `Y` or `Z`. A single click adds that axis to the sort stack and sorts the selection; '
            'double-click sorts by that axis only and replaces the stack.',
            'Or click `Rad` for a radial sort: pick the origin at `Radial sort origin (Enter for centroid)`.',
            'Or click `Crv` to sort along a guide curve: pick it at `Select guide curve for sort order`.',
            'Click `Rev` to reverse the saved order. Click `Clear` to discard it.',
            'Use the saved order: click `Select` to select the objects in the sorted order. When another '
            'command is waiting for objects (for example `Loft`), `Select` injects the objects into that '
            'prompt in the saved order.',
            'Optional: type a group pattern such as `2` or `2,3` (repeats) and click `Group` to bake Rhino '
            'groups named CommaSort_1, CommaSort_2 and so on.',
            'Optional: click `Loft` to loft each complete group of sorted curves, `Nurbs` to create a '
            'control-point curve per group of sorted points, or `Poly` to create a polyline per group.'],
  'options': [{'name': 'Select',
               'values': 'Button',
               'does': 'Selects the saved order, or injects it into an active object prompt.'},
              {'name': 'Clear', 'values': 'Button', 'does': 'Clears the saved sort order.'},
              {'name': 'X / Y / Z',
               'values': 'Buttons',
               'does': 'Single click adds the axis to the sort stack; double-click sorts by that axis '
                       'alone.'},
              {'name': 'Rad',
               'values': 'Button',
               'does': 'Radial sort around a picked origin (Enter uses the centroid).'},
              {'name': 'Crv', 'values': 'Button', 'does': 'Sorts by position along a guide curve.'},
              {'name': 'Rev', 'values': 'Button', 'does': 'Reverses the saved order.'},
              {'name': 'Group pattern',
               'values': 'Text such as 2 or 2,3',
               'does': 'Number of objects per group; a list repeats.'},
              {'name': 'Group',
               'values': 'Button',
               'does': 'Bakes Rhino groups from the sorted list using the pattern.'},
              {'name': 'Loft', 'values': 'Button', 'does': 'Lofts each complete group of sorted curves.'},
              {'name': 'Nurbs',
               'values': 'Button',
               'does': 'Builds a control-point curve per group of sorted points.'},
              {'name': 'Poly', 'values': 'Button', 'does': 'Builds a polyline per group.'}],
  'notes': 'uSortOrder is a hidden alias. The nested sub-command uSortApply is run for you by the Select '
           'button.',
  'extra': ''},
 {'title': 'uTolerance',
  'slug': 'utolerance',
  'section': 'doc',
  'group': 'Doc',
  'onMenu': True,
  'summary': 'Opens the Comma Tolerance toolbar that temporarily overrides the document absolute tolerance '
             'while Rhino commands run. The file itself keeps its original tolerance, so saved models are '
             'not changed.',
  'steps': ['Run `uTolerance`. The Comma Tolerance toolbar opens already enabled, showing the current '
            'document tolerance and its unit.',
            'Type a new tolerance in the box. The value must be a finite number greater than zero, otherwise '
            'the command line says `uTolerance: enter a finite number greater than zero.`',
            'Press Enter or leave the box to apply it. The command line confirms the active override '
            '(`ACTIVE ...`).',
            'Run your Rhino commands (Boolean, join, loft, offset and so on). The override is active only '
            'while a command runs; between commands and during Save the file tolerance is restored.',
            'Click `Disable` to turn the override off (the box becomes read-only and the file tolerance is '
            'used). Click `Enable` to turn it back on.',
            'Close the toolbar, or disable it, to reset to the file tolerance. Changing the active document '
            'also resets it.'],
  'options': [{'name': 'Tolerance',
               'values': 'Number greater than 0',
               'does': 'Absolute tolerance used while commands run. Read-only while disabled.'},
              {'name': 'Unit label', 'values': 'Document unit', 'does': 'Shows the unit of the document.'},
              {'name': 'Enable / Disable',
               'values': 'Toggle button',
               'does': 'Turns the temporary override on or off.'}],
  'notes': 'The command line prints reset to file tolerance when the override ends.',
  'extra': ''},
 {'title': 'uQuickTools',
  'slug': 'uquicktools',
  'section': 'doc',
  'group': 'Doc',
  'onMenu': True,
  'summary': 'Shows a pop-up menu at the cursor with your favorite commands and macros. Click an item to run '
             'it. The list is edited with uQuickToolsConfig.',
  'steps': ['Run `uQuickTools` (it works best when assigned to a hotkey or alias). A menu appears at the '
            'cursor with the prompt `Select item from quick tools (move to highlight, click to run, ESC to '
            'cancel)`.',
            'Move the cursor to highlight an item. `CommaMenu` is always first and `Setup` (opens '
            '`uQuickToolsConfig`) is always last; your own items are in between.',
            'Click an item to run it, or press Esc to cancel.',
            'A Command item runs as `! _<command>` after the menu closes.',
            'A Macro item runs its script. In `Once` mode the script runs one time with the current '
            'selection. In `PerObject` mode each selected object is selected alone, the script runs, and the '
            'original selection is restored afterwards.'],
  'options': [{'name': 'CommaMenu',
               'values': 'Default item',
               'does': 'Opens the Comma command menu (commaMenu).'},
              {'name': 'Setup',
               'values': 'Default item',
               'does': 'Opens uQuickToolsConfig to edit the list.'},
              {'name': 'Command item',
               'values': 'Any Rhino or Comma command',
               'does': 'Runs the command as ! _<command>.'},
              {'name': 'Macro item - Once',
               'values': 'Run mode',
               'does': 'Runs the script once with the current selection.'},
              {'name': 'Macro item - PerObject',
               'values': 'Run mode',
               'does': 'Runs the script for every selected object, one at a time (needs a selection).'}],
  'notes': 'PerObject macros need a selection; otherwise the command line says `uMacro: PerObject mode needs '
           'a selection.` After a run it reports how many objects the script ran on.',
  'extra': ''},
 {'title': 'uQuickToolsConfig',
  'slug': 'uquicktoolsconfig',
  'section': 'doc',
  'group': 'Doc',
  'onMenu': False,
  'summary': 'Opens the Quick Tools Setup dialog where you build the uQuickTools menu from commands and '
             'macros. Items can be reordered, imported and exported as XML.',
  'steps': ['Run `uQuickToolsConfig`, or choose `Setup` in the uQuickTools menu. The modal `Quick Tools '
            'Setup` dialog opens with the grid Label, Type, Command / Script, Mode, Tooltip.',
            'Click `+ Cmd` to add a command. Enter a Label, the Command (for example `uLayer`) and an '
            'optional Tooltip. Label and Command are required.',
            'Click `+ Macro` to add a macro. In the Edit Macro dialog set Name, Tooltip, Mode (`Once` or '
            '`PerObject`) and paste the Script. Do not start the script with `!`.',
            'Select a row and click `Edit` to change it, `-` to remove it, and the up and down arrows to '
            'reorder.',
            'Optional: `Export` writes the setup to a Comma Quick Tools XML file, and `Import` loads one. '
            'Import asks `Replace current items with imported file?`: Yes replaces, No merges (appends), '
            'Cancel aborts.',
            'Optional: use the folder button to open the folder that holds the configuration file.',
            'Click `Reset` to clear all custom items (after a confirmation), then `Save` to keep the changes '
            'or `Cancel` to discard them. Save reports `Quick tools configuration saved (commands + '
            'macros).`'],
  'options': [{'name': '+ Cmd', 'values': 'Button', 'does': 'Adds a command item (Label, Command, Tooltip).'},
              {'name': '+ Macro',
               'values': 'Button',
               'does': 'Adds a macro item (Name, Tooltip, Mode, Script).'},
              {'name': 'Edit', 'values': 'Button', 'does': 'Edits the selected item.'},
              {'name': '-', 'values': 'Button', 'does': 'Removes the selected item.'},
              {'name': 'Up / Down',
               'values': 'Buttons',
               'does': 'Moves the selected item in the menu order.'},
              {'name': 'Reset', 'values': 'Button', 'does': 'Clears custom items after confirmation.'},
              {'name': 'Import / Export',
               'values': 'XML Comma Quick Tools',
               'does': 'Loads or saves the setup; Import can replace or merge.'},
              {'name': 'Folder', 'values': 'Button', 'does': 'Opens the configuration folder.'},
              {'name': 'Mode',
               'values': 'Once, PerObject',
               'does': 'Macro run mode: once with the selection, or once per selected object.'},
              {'name': 'Save / Cancel', 'values': 'Buttons', 'does': 'Keeps or discards the changes.'}],
  'notes': 'The CommaMenu and Setup items are reserved and cannot be added, removed or imported.',
  'extra': ''},
 {'title': 'uScopeBox',
  'slug': 'uscopebox',
  'section': 'doc',
  'group': 'Doc',
  'onMenu': True,
  'summary': 'Creates six clipping planes around a box so the active viewport shows only what is inside it. '
             'The box is drawn with three points or taken from an existing closed box object.',
  'steps': ['Run `uScopeBox` in the viewport you want to clip.',
            'Choose `Mode`: `Draw3PtBox` (default) or `SelectBox`. Optionally set `Size` (clipping plane '
            'size, default 500) and `DeleteExisting` (shown only when ScopeBox objects already exist).',
            'In `Draw3PtBox` mode pick `Corner 1`, then `End of edge`, then `Width`, then `Height`.',
            'In `SelectBox` mode pick an existing closed box at `Select Box` (a polysurface or extrusion).',
            'Six clipping planes are added to the active viewport, each flipped to face the center of the '
            'box. They are grouped as `ScopeBox` and carry the user text ScopeBox=ScopeBox at each face '
            'center.',
            'Run `uScopeBox` again with `DeleteExisting` set to Yes to replace the previous scope box.'],
  'options': [{'name': 'Mode',
               'values': 'SelectBox, Draw3PtBox (default Draw3PtBox)',
               'does': 'Selects an existing box or draws a new one by three points and a height.'},
              {'name': 'Size', 'values': 'Number (default 500)', 'does': 'Clipping plane size.'},
              {'name': 'DeleteExisting',
               'values': 'No, Yes',
               'does': 'Deletes the previous ScopeBox clipping planes. Only shown when ScopeBox objects '
                       'exist.'}],
  'notes': '',
  'extra': ''},
 {'title': 'uScaleCrvAtt',
  'slug': 'uscalecrvatt',
  'section': 'curve',
  'group': 'Curve',
  'onMenu': True,
  'summary': 'Scales curves about their midpoint or extends their ends, replacing each curve in place so '
             'layer and attributes are kept. Switch between the two behaviours with the Mode option.',
  'steps': ['Run `uScaleCrvAtt`. The prompt reads `Select curves to scale` (or `Select curves to extend` '
            'when Mode is Extend).',
            'Optional: set `Mode` to `Scale` or `Extend`. In Extend mode also set `Side` to `Both`, `Start` '
            'or `End`.',
            'Select the curves and press Enter.',
            'Enter `Scale Factor` (default 2, zero or more) in Scale mode, or `Extension length` (default '
            '1000, zero or more) in Extend mode.',
            'Scale mode scales each curve about its midpoint (the point at 50 percent of its length).',
            'Extend mode extends each open curve smoothly at the chosen side(s). Closed curves cannot be '
            'extended; if nothing could be extended the command line says `Unable to extend selected '
            'curve(s).`'],
  'options': [{'name': 'Mode',
               'values': 'Scale, Extend (default Scale)',
               'does': 'Chooses between scaling and extending.'},
              {'name': 'Side',
               'values': 'Both, Start, End (default Both)',
               'does': 'Which end to extend. Only shown in Extend mode.'},
              {'name': 'Scale Factor',
               'values': 'Number, default 2',
               'does': 'Scale mode multiplier about the midpoint.'},
              {'name': 'Extension length',
               'values': 'Number, default 1000',
               'does': 'Extend mode length added at each chosen end.'}],
  'notes': 'Mode and Side are remembered between runs.',
  'extra': ''},
 {'title': 'uFlipCrv',
  'slug': 'uflipcrv',
  'section': 'curve',
  'group': 'Curve',
  'onMenu': True,
  'summary': 'Makes the direction of many curves agree with a vector or a guide curve. Only curves that '
             'point against the chosen direction are reversed.',
  'steps': ['Run `uFlipCrv`. The prompt reads `Select curves to flip`. Select the curves and press Enter.',
            'At `Pick flip vector start point` either click a start point, or choose an option: `X`, `Y`, '
            '`Z` (world axis direction) or `Crv` (guide curve).',
            'After a start point, pick `Pick flip vector end point`. A rubber-band line shows the vector. '
            'The `X`, `Y`, `Z` and `Crv` options remain available.',
            'With `Crv`, select the guide curve at `Select guide curve`. Each curve is compared with the '
            'guide tangent at the point of the guide closest to the start of that curve.',
            'A curve is reversed when its start tangent points against the chosen direction. The command '
            'line reports `Flipped N of M curve(s).`',
            'A vector that is too short stops with `Flip vector is too short.`'],
  'options': [{'name': 'X', 'values': 'Immediate', 'does': 'Uses the world X axis as the flip direction.'},
              {'name': 'Y', 'values': 'Immediate', 'does': 'Uses the world Y axis as the flip direction.'},
              {'name': 'Z', 'values': 'Immediate', 'does': 'Uses the world Z axis as the flip direction.'},
              {'name': 'Crv',
               'values': 'Select guide curve',
               'does': 'Uses the tangent of a guide curve near each curve as the direction.'}],
  'notes': '',
  'extra': ''},
 {'title': 'uPolyToNurbsCurve',
  'slug': 'upolytonurbscurve',
  'section': 'curve',
  'group': 'Curve',
  'onMenu': True,
  'summary': 'Converts polylines into smooth cubic NURBS curves that pass through the polyline vertices. '
             'Vertices that are closer together than the tolerance are dropped first.',
  'steps': ['Run `uPolyToNurbsCurve`. The prompt reads `Select polyline curves`.',
            'Optional: set `Tolerance` (default 0.01, remembered between runs).',
            'Select the polylines and press Enter.',
            'For each polyline, vertices closer than the tolerance to the previously kept vertex are '
            'removed, and an interpolated degree 3 curve is built through the remaining vertices.',
            'The new curve is added on the current layer and the original polyline is deleted. Curves that '
            'are not polylines are skipped.'],
  'options': [{'name': 'Tolerance',
               'values': 'Number, default 0.01',
               'does': 'Minimum distance between kept vertices.'}],
  'notes': '',
  'extra': ''},
 {'title': 'uTryGetCircle',
  'slug': 'utrygetcircle',
  'section': 'curve',
  'group': 'Curve',
  'onMenu': True,
  'summary': 'Replaces curves that are really circles or arcs (for example from CAD or meshes) with true '
             'circle and arc curves. It reports how far each fit deviates from the original.',
  'steps': ['Run `uTryGetCircle`. The prompt reads `Select curves to fit as circles or arcs`.',
            'Select the curves and press Enter.',
            'Each curve is sampled at 48 points. The command tries native circle and arc recognition and a '
            'sampled fit, then keeps the better result.',
            'Closed curves become circles. Open curves become arcs that keep their end points. Each result '
            'replaces the original curve.',
            'Read the report `Fitted X circles and Y arcs. Failed: Z. Max deviation ...` with the document '
            'tolerance for comparison.'],
  'options': [],
  'notes': 'The document tolerance is only reported. A fit that exceeds it is still kept and counted as '
           '`Over-tolerance: N (kept best fit)`, so check that number. uTryGetArc is a legacy alias.',
  'extra': ''},
 {'title': 'uFlipSrf',
  'slug': 'uflipsrf',
  'section': 'surface',
  'group': 'Surface',
  'onMenu': True,
  'summary': 'Makes the normals of many surfaces and polysurfaces point the same way as a vector or a guide '
             'curve. Only objects that point against the direction are flipped.',
  'steps': ['Run `uFlipSrf`. The prompt reads `Select surfaces to flip`. Select surfaces or polysurfaces and '
            'press Enter.',
            'At `Pick flip vector start point` either click a start point or choose `X`, `Y`, `Z` (world '
            'axis) or `Crv` (guide curve).',
            'After a start point, pick `Pick flip vector end point`; the vector is drawn as a rubber-band '
            'line.',
            'With `Crv`, select the guide curve at `Select guide curve`. Each surface is compared with the '
            'guide tangent at the point closest to the surface centroid.',
            'A surface is flipped when its reference normal (taken at the point nearest its centroid) points '
            'against the direction. The command line reports `Flipped N of M surface(s).`'],
  'options': [{'name': 'X', 'values': 'Immediate', 'does': 'Uses the world X axis as the target direction.'},
              {'name': 'Y', 'values': 'Immediate', 'does': 'Uses the world Y axis as the target direction.'},
              {'name': 'Z', 'values': 'Immediate', 'does': 'Uses the world Z axis as the target direction.'},
              {'name': 'Crv',
               'values': 'Select guide curve',
               'does': 'Uses a guide curve tangent as the target direction.'}],
  'notes': 'A vector shorter than the tolerance stops with `Flip vector is too short.`',
  'extra': ''},
 {'title': 'uScaleBrep',
  'slug': 'uscalebrep',
  'section': 'brep',
  'group': 'Brep',
  'onMenu': True,
  'summary': 'Scales polysurfaces, surfaces and meshes about their own centroid, so each object shrinks or '
             'grows in place. Several objects are scaled in one go, each about its own center.',
  'steps': ['Run `uScaleBrep`. The prompt reads `Select Brep/Mesh/Surface to scale`.',
            'Select the objects and press Enter.',
            'Enter the `Scale Factor` (default 0.9).',
            'Each object is scaled uniformly about its own centroid. For a brep the area centroid is used '
            '(bounding box center as fallback); for a mesh the volume centroid, then the area centroid, then '
            'the bounding box center.'],
  'options': [{'name': 'Scale Factor',
               'values': 'Number, default 0.9',
               'does': 'Uniform scale applied about each object centroid.'}],
  'notes': '',
  'extra': ''},
 {'title': 'uCombineNurbs',
  'slug': 'ucombinenurbs',
  'section': 'brep',
  'group': 'Brep',
  'onMenu': True,
  'summary': 'Builds one continuous lofted surface set from many separate surfaces or breps that follow the '
             'same direction, such as a deck, tunnel or pipe cut into segments. It collects the edges that '
             'run along a direction curve, joins and rebuilds them into smooth sections, then lofts through '
             'them.',
  'steps': ['Run `uCombineNurbs`. The prompt reads `Select Breps or surfaces to combine`.',
            'Set the options on the same prompt (see the table): direction mode, angle tolerance, sample '
            'count, split zone, segment length, join tolerance, loft and result options. Option values are '
            'remembered between runs.',
            'Select the breps or surfaces and press Enter.',
            'At `Select direction curve` pick a curve that runs along the long direction of the structure.',
            'If `GuidePoints` is Yes, pick points at `Guide point (Enter when done)` (at least two) to '
            'define the order of the sections.',
            'The command collects edges parallel to the direction. In `Line` mode an edge must be within the '
            'angle tolerance of the direction. In `Curve` mode, sample points on each edge are compared with '
            'the direction curve tangent. Fewer than two edges stops with `Not enough edges parallel to '
            'direction (need >= 2).`',
            'Edges are joined, converted to smooth section curves and aligned in the same direction. With '
            '`SplitZone` Yes the sections are cut into zones where they overlap.',
            'Sections are sorted along the direction curve (or by boundary, or by the guide points), rebuilt '
            'to degree 3 with at least 4 control points and about one point per `SegmentLength`, and lofted '
            'with a straight (ruled) loft.',
            'Results are added using `BakeMode`, optionally capped, optionally grouped as `CombinedGroup`, '
            'and the originals are deleted when `DeleteOriginal` is Yes. The command line reports `Combined '
            'into N surface(s).`'],
  'options': [{'name': 'DirectionMode',
               'values': 'Line, Curve (default Curve)',
               'does': 'How edges are matched to the direction curve: Line uses one overall direction, Curve '
                       'compares the tangent at sample points.'},
              {'name': 'BakeMode',
               'values': 'ByLayer, ByObject (default ByLayer)',
               'does': 'ByLayer takes color, material, linetype and print settings from the layer. ByObject '
                       'copies the source object overrides.'},
              {'name': 'AngleTolerance',
               'values': '0 to 90 degrees, default 15',
               'does': 'Maximum angle between an edge and the direction for the edge to be used.'},
              {'name': 'SampleCount',
               'values': '1 to 50, default 3',
               'does': 'Sample points per edge in Curve mode.'},
              {'name': 'SplitZone',
               'values': 'No, Yes (default No)',
               'does': 'Splits sections into overlap zones before lofting.'},
              {'name': 'SegmentLength',
               'values': '1 to 100000, default 500',
               'does': 'Target spacing for control points when sections are rebuilt.'},
              {'name': 'JoinTolerance',
               'values': '0 to 500, default 1.0',
               'does': 'Distance used when joining edges into section curves.'},
              {'name': 'ClosedLoft',
               'values': 'No, Yes (default No)',
               'does': 'Closes the loft from the last section back to the first.'},
              {'name': 'SortByBoundary',
               'values': 'No, Yes (default No)',
               'does': 'Sorts sections by boundary position instead of along the direction curve.'},
              {'name': 'GuidePoints',
               'values': 'No, Yes (default No, not remembered)',
               'does': 'Asks for guide points that define section order.'},
              {'name': 'PairSimilar',
               'values': 'No, Yes (default No)',
               'does': 'Pairs sections of similar shape, lofts inside each pair and bridges between '
                       'neighbouring pairs.'},
              {'name': 'DeleteOriginal',
               'values': 'No, Yes (default No)',
               'does': 'Deletes the source objects after the result is created.'},
              {'name': 'GroupResult',
               'values': 'No, Yes (default Yes)',
               'does': 'Groups the new surfaces as CombinedGroup.'},
              {'name': 'CapResult',
               'values': 'No, Yes (default No)',
               'does': 'Caps planar holes of each result.'},
              {'name': 'ShowIsocurves',
               'values': 'No, Yes (default No)',
               'does': 'Shows isocurves on the result (wire density 1) or hides them.'}],
  'notes': 'uSmoothPolySrf uses the same workflow with different defaults.',
  'extra': ''},
 {'title': 'uLoftPro',
  'slug': 'uloftpro',
  'section': 'brep',
  'group': 'Brep',
  'onMenu': True,
  'summary': 'Distributes profiles, blocks, meshes, points, text or breps along rail curves and lofts or '
             'sweeps curve profiles through them. You pick rails, pick what to distribute, set a reference '
             'point and preview the result before it is baked.',
  'steps': ['Run `uLoftPro`. At `Select Alignment curves (Rails)` pick one or more rails. Optionally set '
            '`Mode` (`PerPlane` or `PerHorPln`, default PerHorPln) and `DivideDist` (default 500, from 0.1 '
            'to 1000000).',
            'At `Select Objects to Distribute` pick curves, blocks, meshes, points, annotation text or '
            'breps.',
            'At `Pick Reference Point (Origin)` pick the point on the objects that will sit on the rail.',
            'A preview appears with direction arrows on the rails. The prompt reads `Previewing... Enter to '
            'Bake.`',
            'While previewing you can change the options: `Method` (Loft or Sweep, only shown when curves '
            'were selected), `Cap`, `Flip_Rails` (`Select Rail to Flip (Press Enter when done)`), '
            '`Reselect_Objects` and `Pick_New_Origin`.',
            'Press Enter to bake, or Esc to cancel.',
            'Rails are divided by length (end points included) every `DivideDist`. A frame is built at each '
            'division: with `PerHorPln` the frame stays upright (Y is world Z), with `PerPlane` the frame '
            'follows the 3D tangent of the rail.',
            'Blocks, meshes, breps, points and text are copied to every frame. Curves are lofted between '
            'frames (`Loft`) or swept along the rail (`Sweep`). With `Cap` Yes planar holes are capped.',
            'The results of each rail are grouped as `Align_N_Result`.'],
  'options': [{'name': 'Mode',
               'values': 'PerPlane, PerHorPln (default PerHorPln)',
               'does': 'PerPlane tilts frames with the rail tangent; PerHorPln keeps frames vertical (Y is '
                       'world Z).'},
              {'name': 'DivideDist',
               'values': '0.1 to 1000000, default 500',
               'does': 'Distance between frames along each rail.'},
              {'name': 'Method',
               'values': 'Loft, Sweep',
               'does': 'How curve profiles are turned into surfaces. Shown only when curves were selected.'},
              {'name': 'Cap',
               'values': 'No, Yes (default No)',
               'does': 'Caps planar holes of the lofted or swept results.'},
              {'name': 'Flip_Rails',
               'values': 'Select rails, Enter when done',
               'does': 'Reverses the direction of the picked rails.'},
              {'name': 'Reselect_Objects',
               'values': 'Select objects',
               'does': 'Replaces the set of objects to distribute.'},
              {'name': 'Pick_New_Origin',
               'values': 'Point',
               'does': 'Changes the reference point (the current one is shown in the prompt).'}],
  'notes': 'Flip rails if the preview arrows point the wrong way, because the direction decides the '
           'orientation of every frame.',
  'extra': ''},
 {'title': 'uSmoothPolySrf',
  'slug': 'usmoothpolysrf',
  'section': 'brep',
  'group': 'Brep',
  'onMenu': True,
  'summary': 'Turns many surface or brep segments into one smooth lofted result along a direction curve. It '
             'works like uCombineNurbs but is tuned for closed profiles, so it closes the loft and sorts '
             'sections by boundary by default.',
  'steps': ['Run `uSmoothPolySrf`. The prompt reads `Select Breps or surfaces`.',
            'Set the options on the same prompt (same list as uCombineNurbs; values are remembered).',
            'Select the objects and press Enter.',
            'At `Select direction curve` pick a curve that runs along the structure.',
            'If `GuidePoints` is Yes, pick at least two points at `Guide point (Enter when done)`.',
            'Edges parallel to the direction are collected, joined, aligned, sorted and rebuilt to degree 3 '
            'sections, then lofted.',
            'The new surfaces are added with the chosen `BakeMode`, grouped as `LoftedGroup` when '
            '`GroupResult` is Yes, and the originals are deleted when `DeleteOriginal` is Yes.'],
  'options': [{'name': 'DirectionMode',
               'values': 'Line, Curve (default Curve)',
               'does': 'How edges are matched to the direction curve.'},
              {'name': 'BakeMode',
               'values': 'ByLayer, ByObject (default ByLayer)',
               'does': 'Where color, material and print settings come from.'},
              {'name': 'AngleTolerance',
               'values': '0 to 90 degrees, default 15',
               'does': 'Maximum angle between an edge and the direction.'},
              {'name': 'SampleCount',
               'values': '1 to 50, default 3',
               'does': 'Sample points per edge in Curve mode.'},
              {'name': 'SplitZone',
               'values': 'No, Yes (default No)',
               'does': 'Splits sections into overlap zones.'},
              {'name': 'SegmentLength',
               'values': '1 to 100000, default 500',
               'does': 'Target control-point spacing of rebuilt sections.'},
              {'name': 'JoinTolerance',
               'values': '0 to 500, default 1.0',
               'does': 'Distance used when joining edges.'},
              {'name': 'ClosedLoft',
               'values': 'No, Yes (default Yes)',
               'does': 'Closes the loft from last section to first.'},
              {'name': 'SortByBoundary',
               'values': 'No, Yes (default Yes)',
               'does': 'Sorts sections by boundary position.'},
              {'name': 'GuidePoints',
               'values': 'No, Yes (default No)',
               'does': 'Asks for guide points that define the order.'},
              {'name': 'PairSimilar',
               'values': 'No, Yes (default No)',
               'does': 'Pairs similar sections before lofting.'},
              {'name': 'DeleteOriginal',
               'values': 'No, Yes (default No)',
               'does': 'Deletes the source objects after success.'},
              {'name': 'GroupResult',
               'values': 'No, Yes (default Yes)',
               'does': 'Groups results as LoftedGroup.'},
              {'name': 'CapResult',
               'values': 'No, Yes (default No)',
               'does': 'Caps planar holes of the results.'},
              {'name': 'ShowIsocurves',
               'values': 'No, Yes (default No)',
               'does': 'Shows or hides isocurves on the result.'}],
  'notes': 'Differences from uCombineNurbs: ClosedLoft and SortByBoundary default to Yes, and the result '
           'group is named LoftedGroup.',
  'extra': ''},
 {'title': 'uFaceFromDirection',
  'slug': 'ufacefromdirection',
  'section': 'brep',
  'group': 'Brep',
  'onMenu': True,
  'summary': 'Extracts the faces of a brep whose normals point in a chosen direction, for example all '
             'upward-facing faces. A tolerance angle controls how strictly the normal must match.',
  'steps': ['Run `uFaceFromDirection`. The prompt reads `Select brep to extract faces`. Select a brep or '
            'surface.',
            'Optional: set `Reverse` (No or Yes) and `BothDirections` (No or Yes) on the prompts. Both are '
            'remembered.',
            'At `First point of direction vector (Enter for Z-axis)` click a start point, or press Enter to '
            'use the world Z axis.',
            'If you picked a point, click the `Second point of direction vector`.',
            'Enter the `Angle tolerance in degrees` (0 to 90, default 0). A face is kept when its normal, '
            'measured at the middle of its surface domain, is within that angle of the direction.',
            'The matching faces are extracted as new breps and selected. The command line reports `Extracted '
            'N faces from M total faces`.'],
  'options': [{'name': 'Reverse', 'values': 'No, Yes', 'does': 'Uses the opposite of the picked direction.'},
              {'name': 'BothDirections',
               'values': 'No, Yes',
               'does': 'Accepts faces that point with or against the direction.'},
              {'name': 'Angle tolerance',
               'values': '0 to 90 degrees, default 0',
               'does': 'Allowed angle between face normal and direction.'}],
  'notes': '',
  'extra': ''},
 {'title': 'uMeshPatch',
  'slug': 'umeshpatch',
  'section': 'mesh',
  'group': 'Mesh',
  'onMenu': True,
  'summary': 'Fills closed boundary curves with a relaxed quad-dominant mesh patch. Edge length, grading '
             'toward the boundary and relaxation are controlled with options.',
  'steps': ['Run `uMeshPatch`. The prompt reads `Select closed boundary curve(s) to patch`.',
            'Set the options on the prompt: `BoundaryEdgeLength`, `Grading`, `RelaxIterations`, '
            '`SlideBoundary`, `RelaxMode`, `MatchAttributes`, `DeleteInput`.',
            'Select one or more boundary curves that join into a closed loop and press Enter.',
            'The command builds the mesh and prints the vertex and face counts. If the curves do not form '
            'one closed loop it reports `Could not build mesh (check curves are joinable to one closed '
            'loop).`'],
  'options': [{'name': 'BoundaryEdgeLength',
               'values': 'Number, default 1.0',
               'does': 'Target mesh edge length along the boundary.'},
              {'name': 'Grading',
               'values': '1 to 1000, default 2.0',
               'does': 'Edge growth toward the middle. 1 means uniform.'},
              {'name': 'RelaxIterations',
               'values': '1 to 5000, default 200',
               'does': 'Number of smoothing passes.'},
              {'name': 'SlideBoundary',
               'values': 'Fixed, Slide (default Slide)',
               'does': 'Whether boundary vertices may slide along the boundary during relaxation.'},
              {'name': 'RelaxMode',
               'values': 'Laplacian, Tensile (default Tensile)',
               'does': 'Smoothing method.'},
              {'name': 'MatchAttributes',
               'values': 'No, Yes (default Yes)',
               'does': 'Gives the mesh the layer and attributes of the first boundary curve.'},
              {'name': 'DeleteInput',
               'values': 'No, Yes (default No)',
               'does': 'Deletes the boundary curves after the patch is created.'}],
  'notes': '',
  'extra': ''},
 {'title': 'uMeshToNurbs',
  'slug': 'umeshtonurbs',
  'section': 'mesh',
  'group': 'Mesh',
  'onMenu': True,
  'summary': 'Converts meshes, typically imported IFC meshes, into NURBS breps. Presets trade speed against '
             'fit, and an Advanced set of options exposes the detailed conversion controls. Pieces that '
             'cannot be converted safely stay as meshes and are reported.',
  'steps': ['Run `uMeshToNurbs`. The prompt reads `Select IFC meshes (Enter = all meshes)`. Select meshes, '
            'or press Enter to take every mesh in the model, including hidden and locked ones.',
            'Choose `Quality`: `Fast`, `Balanced` (default) or `Tight`. Choose `Output`: `Replace` (default) '
            'or `Copy`.',
            'Optional: set `Advanced` to Yes to reveal `Mode`, `Method`, `HealOpen`, `Tolerance`, '
            '`TimeLimit`, `MaxFaces`, `CheckObjects` and `Report`. Advanced resets to No at every run.',
            'Press Enter to start. A progress meter runs; press Esc to cancel.',
            'Each mesh is classified: OK, OK_FACETED, PARTIAL (the converted pieces become NURBS, pieces '
            'that need checking stay as meshes and are selected) or CHECK (the mesh is kept).',
            'Read the summary and the suggestions for meshes that were not converted. If `Report` is Yes a '
            'CSV file is written.'],
  'options': [{'name': 'Quality',
               'values': 'Fast, Balanced, Tight (default Balanced)',
               'does': 'Fast makes faceted breps only. Balanced uses the smart pipeline. Tight prefers '
                       'analytic surfaces with stricter circle and merge settings.'},
              {'name': 'Output',
               'values': 'Replace, Copy (default Replace)',
               'does': 'Replace deletes the source meshes; Copy keeps them.'},
              {'name': 'Advanced',
               'values': 'No, Yes (default No)',
               'does': 'Shows the advanced options below. Reset to No on each run.'},
              {'name': 'Mode',
               'values': 'Auto, Primitives, Pipe, Extrude, Freeform',
               'does': 'Which shape recognition strategy is used.'},
              {'name': 'Method', 'values': 'Smart, Faceted, Analytic', 'does': 'Conversion method.'},
              {'name': 'HealOpen',
               'values': 'No, Yes (default Yes)',
               'does': 'Tries to close small gaps in open meshes before conversion.'},
              {'name': 'Tolerance',
               'values': '0 to 100, default 0',
               'does': 'Fit tolerance. 0 detects the resolution of the IFC data automatically.'},
              {'name': 'TimeLimit',
               'values': '1 to 600 seconds, default 5',
               'does': 'Time allowed for each object.'},
              {'name': 'MaxFaces',
               'values': '0 to 1000000, default 0',
               'does': 'Only meshes with at most this many faces are converted. 0 turns the filter off.'},
              {'name': 'CheckObjects',
               'values': 'KeepMesh, ToBrep',
               'does': 'What to do with pieces that need checking: keep them as meshes, or convert them to '
                       'faceted breps.'},
              {'name': 'Report',
               'values': 'No, Yes',
               'does': 'Writes a CSV named <name>_NURBS_<yyyyMMdd_HHmm>_report.csv next to the document, or '
                       'on the Desktop if the document is not saved.'}],
  'notes': 'Use Copy first on large files so the original meshes stay available for comparison.',
  'extra': ''},
 {'title': 'uMeshOutline',
  'slug': 'umeshoutline',
  'section': 'mesh',
  'group': 'Mesh',
  'onMenu': True,
  'summary': 'Creates the outer outline curves of surfaces, polysurfaces and meshes as seen from a plane. '
             'Outlines are placed on layers named Outline::<source layer> and can be merged by layer, by '
             'object or all together.',
  'steps': ['Run `uMeshOutline`. The prompt reads `Select objects to outline` (surfaces, polysurfaces, '
            'meshes).',
            'Set `Plane` (`CPlane`, `World` or `View`; default CPlane) and `Merge` (`All`, `ByLayer` or '
            '`PerObject`; default ByLayer).',
            'Select the objects and press Enter.',
            'The shapes are projected onto the plane, merged according to `Merge` and the outer contour is '
            'kept.',
            'Outline curves are created on the layer `Outline::<source layer path>` (`Outline::Merged` for '
            'All). PerObject outlines go under the source layer path. The color is copied from the source '
            'layer.',
            'The command line reports `Done: N outline curve(s) created.`'],
  'options': [{'name': 'Plane',
               'values': 'CPlane, World, View (default CPlane)',
               'does': 'Projection plane for the outline.'},
              {'name': 'Merge',
               'values': 'All, ByLayer, PerObject (default ByLayer)',
               'does': 'All makes one outline set, ByLayer one per source layer, PerObject one per object.'}],
  'notes': 'Only the outer contour is created; holes are not outlined.',
  'extra': ''},
 {'title': 'uFindCreateBlock',
  'slug': 'ufindcreateblock',
  'section': 'drafting',
  'group': 'Drafting',
  'onMenu': True,
  'summary': 'Finds identical copies of an assembly (moved or rotated, not scaled or mirrored) and replaces '
             'all of them with one block definition. You pick one example and the command locates every '
             'repeat in the visible model.',
  'steps': ['Run `uFindCreateBlock`. At `Select one repeated assembly to find and convert to blocks` select '
            'one example (any object types, several objects allowed).',
            'At `Block base point (uses active CPlane)` pick the base point of the new block.',
            'Enter the `Matching tolerance` (default is the larger of the document tolerance and 1 mm).',
            'Enter the `New block name` (default CommaBlock_N). The name must not already exist.',
            'The command scans visible objects for rigid copies. If fewer than two occurrences are found it '
            'says `No repeat found...`.',
            'The matching occurrences are highlighted. Answer `Convert highlighted occurrences to one block` '
            'with No or Yes.',
            'On Yes the block is created and each occurrence is replaced by a block instance.'],
  'options': [{'name': 'Matching tolerance',
               'values': 'Number',
               'does': 'How closely a copy must match the example.'},
              {'name': 'New block name',
               'values': 'Text, default CommaBlock_N',
               'does': 'Name of the block definition.'},
              {'name': 'Convert',
               'values': 'No, Yes',
               'does': 'Confirms replacement of the highlighted occurrences.'}],
  'notes': 'Text, annotations, lights, grips, details and clipping planes cannot be part of the assembly.',
  'extra': ''},
 {'title': 'uSection',
  'slug': 'usection',
  'section': 'drafting',
  'group': 'Drafting',
  'onMenu': True,
  'summary': 'Cuts sections through solids, surfaces, meshes, blocks and curves with a line or a plane and '
             'places the section curves where you click. It repeats until you press Esc, so you can create '
             'many sections from the same selection.',
  'steps': ['Run `uSection`. At `Select objects to section` pick breps, surfaces, meshes, blocks or curves '
            'and press Enter.',
            'Set `Mode` to `LineCut` (default) or `PlaneCut`, and set the other options (see the table).',
            'In `LineCut` mode pick `Start of section line (Esc to exit)` and `End of section line`. The '
            'cutter is a tall plane along the CPlane Z direction.',
            'In `PlaneCut` mode pick `Select plane source (Esc to exit)` (a surface, brep, mesh or face), '
            'then `Pick origin point for section plane`, then the two corners of the cut range (`First point '
            'of cut range (on plane)` and `Second point of cut range`).',
            'At `Pick placement point (Enter = place at cut, no orient)` click where the section should be '
            'placed. Placement is constrained to the world XY plane and the section curves are oriented onto '
            'it. Press Enter to leave them at the cut.',
            'The command line reports `Section complete (N result(s)). Pick new section line or Esc to '
            'exit.` Repeat with a new line or press Esc to finish.'],
  'options': [{'name': 'Mode',
               'values': 'LineCut, PlaneCut (default LineCut)',
               'does': 'Section by a line or by a plane.'},
              {'name': 'SelectResults',
               'values': 'Off, On (default On)',
               'does': 'Selects the new section curves.'},
              {'name': 'BakeCutter',
               'values': 'No, Yes (default No)',
               'does': 'Keeps the cutter: a curve named Reference_Line in LineCut, a brep named '
                       'Section_Cutter in PlaneCut.'},
              {'name': 'OutputLayer',
               'values': 'InputLayer, CurrentLayer (default InputLayer)',
               'does': 'Layer of the section curves.'},
              {'name': 'GroupOutput',
               'values': 'No, Yes (default No)',
               'does': 'Groups the results as Section_Result.'},
              {'name': 'Project',
               'values': 'No, Yes (default No)',
               'does': 'Projects the picked points onto the plane chosen in Plane before cutting.'},
              {'name': 'Plane', 'values': 'CPlane, World (default CPlane)', 'does': 'Plane used by Project.'},
              {'name': 'ExtentY',
               'values': '0 to 1000000, default 1000',
               'does': 'PlaneCut only: height of the cutting plane.'}],
  'notes': '',
  'extra': ''},
 {'title': 'uAnnotation',
  'slug': 'uannotation',
  'section': 'drafting',
  'group': 'Drafting',
  'onMenu': True,
  'summary': 'Opens the Comma Annotation toolbar to manage annotation scale for dimensions, text, leaders '
             'and hatches. You choose a drawing scale and paper text height, and annotations follow the '
             'scale automatically.',
  'steps': ['Run `uAnnotation`. The Comma Annotation toolbar opens.',
            'Choose a dimension style in the style dropdown.',
            'Choose the current scale (1:N) in the scale dropdown. Click `Scales` to open Edit Drawing '
            'Scales and add, edit, move, delete or reset scales.',
            'Set the paper text height in millimeters (0.001 to 10000) with the stepper.',
            'Draw dimensions, text, leaders or hatches. New annotations take the current scale and paper '
            'height.',
            'Use `Show` to switch between all scales and the current scale only.',
            'Use `Match` to copy properties: select the targets, then select the source.',
            'Use `Sync` to apply the current scale and height to the selected annotations.',
            'Use the `Auto` link to pause or resume automatic scale application and filtering while '
            'drawing.'],
  'options': [{'name': 'Dimension style',
               'values': 'Dropdown',
               'does': 'Dimension style used for new dimensions.'},
              {'name': 'Scale', 'values': 'Dropdown of 1:N', 'does': 'Current annotation scale.'},
              {'name': 'Scales',
               'values': 'Button',
               'does': 'Opens Edit Drawing Scales with Add, Edit, Move Up, Move Down, Delete, Reset, OK, '
                       'Cancel and Help. Drawing units are 1:N.'},
              {'name': 'Paper text height',
               'values': 'Millimeters, 0.001 to 10000',
               'does': 'Text height on paper.'},
              {'name': 'Show', 'values': 'Toggle', 'does': 'All scales or current scale only.'},
              {'name': 'Match',
               'values': 'Button',
               'does': 'Runs uAnnoMatchProperties: select targets, then the source.'},
              {'name': 'Sync',
               'values': 'Button',
               'does': 'Applies current scale and height to the selection.'},
              {'name': 'Auto',
               'values': 'Link toggle',
               'does': 'Auto-applies scale and filtering while drawing; click to pause.'}],
  'notes': 'Standard scales are 1:1, 1:10, 1:20, 1:50, 1:100, 1:200 and 1:500. The default scale is 1:100 '
           'and the default paper height is 2.5 mm.',
  'extra': ''},
 {'title': 'uMergeHatch',
  'slug': 'umergehatch',
  'section': 'drafting',
  'group': 'Drafting',
  'onMenu': True,
  'summary': 'Merges touching or overlapping hatches into one hatch by taking the union of their boundaries. '
             'The first selected hatch supplies the pattern, rotation and scale.',
  'steps': ['Run `uMergeHatch`. The prompt reads `Select hatches to merge`.',
            'Select at least two hatches and press Enter.',
            'The command builds a planar region for each hatch boundary, unions them, joins the outer edges '
            'and creates new hatches.',
            'The new hatches use the pattern, rotation and scale of the first hatch. The original hatches '
            'are deleted on success.'],
  'options': [],
  'notes': '',
  'extra': ''},
 {'title': 'uDist',
  'slug': 'udist',
  'section': 'drafting',
  'group': 'Drafting',
  'onMenu': True,
  'summary': 'Measures the distance between two points with a live preview. The result is printed on the '
             'command line and copied to the clipboard.',
  'steps': ['Run `uDist`.',
            'Optional: set `BakeResult` (No or Yes) and `UnitDisplay` (Document or Meters).',
            'Pick the `Start point`.',
            'Pick the `End point`. The distance updates live while you move the mouse.',
            'The result is printed and copied to the clipboard. With `BakeResult` Yes a line and a text dot '
            'are added on the layer `CheckDist` and grouped.'],
  'options': [{'name': 'BakeResult',
               'values': 'No, Yes (default No)',
               'does': 'Adds a line and a text dot to the model.'},
              {'name': 'UnitDisplay',
               'values': 'Document, Meters (default Document)',
               'does': 'Unit of the printed result.'}],
  'notes': '',
  'extra': ''},
 {'title': 'uLength',
  'slug': 'ulength',
  'section': 'drafting',
  'group': 'Drafting',
  'onMenu': True,
  'summary': 'Adds up the length of the selected curves. The total is printed and copied to the clipboard.',
  'steps': ['Run `uLength`.',
            'At `Select Curves` pick one or more curves. Set `BakeResult` and `UnitDisplay` first if needed.',
            'Press Enter. The total length is printed on the command line and copied to the clipboard.',
            'With `BakeResult` Yes a text dot `L: ...` is added at the average midpoint of the curves on the '
            'layer `CheckLength`.'],
  'options': [{'name': 'BakeResult',
               'values': 'No, Yes (default No)',
               'does': 'Adds a text dot with the total length.'},
              {'name': 'UnitDisplay',
               'values': 'Document, Meters (default Document)',
               'does': 'Unit of the result.'}],
  'notes': '',
  'extra': ''},
 {'title': 'uLevel',
  'slug': 'ulevel',
  'section': 'drafting',
  'group': 'Drafting',
  'onMenu': True,
  'summary': 'Reads the level (height) of a picked point along an axis, measured from the world origin or '
             'the construction plane. Use it to check elevations quickly.',
  'steps': ['Run `uLevel`.',
            'Optional: set `BakeResult`, `UnitDisplay`, `Reference` (CPlane or World) and click the axis '
            'option to cycle between `AxisX`, `AxisY` and `AxisZ` (default Z).',
            'At `Pick point` click the point to measure.',
            'The level is the distance from the reference plane origin along the chosen axis. It is printed '
            'and copied to the clipboard.',
            'With `BakeResult` Yes a line to the projected point and a text dot are added on the layer '
            '`CheckLevel`.'],
  'options': [{'name': 'BakeResult',
               'values': 'No, Yes (default No)',
               'does': 'Adds a line and a text dot to the model.'},
              {'name': 'UnitDisplay',
               'values': 'Document, Meters (default Document)',
               'does': 'Unit of the result.'},
              {'name': 'Reference',
               'values': 'CPlane, World (default World)',
               'does': 'Origin and axes used for the level.'},
              {'name': 'Axis',
               'values': 'AxisX, AxisY, AxisZ (default Z)',
               'does': 'Axis along which the level is measured. Click to cycle.'}],
  'notes': '',
  'extra': ''},
 {'title': 'uDiffZ',
  'slug': 'udiffz',
  'section': 'drafting',
  'group': 'Drafting',
  'onMenu': True,
  'summary': 'Measures the signed height difference between two points along a world axis (Z by default). '
             'The result is printed and copied to the clipboard.',
  'steps': ['Run `uDiffZ`.',
            'At `First Point` pick the first point. `UnitDisplay` is available on this prompt.',
            'At `Second Point` pick the second point. On this prompt you can set `BakeResult`, `UnitDisplay` '
            'and click the axis option to cycle `AxisX`, `AxisY`, `AxisZ` (default Z).',
            'The signed difference (second minus first) along the chosen axis is printed and copied.',
            'With `BakeResult` Yes a line and a text dot are added on the layer `CheckDiffZ`.'],
  'options': [{'name': 'BakeResult',
               'values': 'No, Yes (default No)',
               'does': 'Adds a line and a text dot to the model.'},
              {'name': 'UnitDisplay',
               'values': 'Document, Meters (default Document)',
               'does': 'Unit of the result.'},
              {'name': 'Axis',
               'values': 'AxisX, AxisY, AxisZ (default Z)',
               'does': 'World axis of the difference.'}],
  'notes': '',
  'extra': ''},
 {'title': 'uAngle',
  'slug': 'uangle',
  'section': 'drafting',
  'group': 'Drafting',
  'onMenu': True,
  'summary': 'Measures the angle at a vertex between two picked points. The angle is reported in degrees '
             'with two decimals.',
  'steps': ['Run `uAngle`.',
            'Optional: set `BakeResult`.',
            'Pick the `Vertex`.',
            'Pick `Point 1`.',
            'Pick `Point 2`.',
            'The angle in degrees is printed and copied to the clipboard. With `BakeResult` Yes the angle is '
            'added to the model on the layer `CheckAngle`.'],
  'options': [{'name': 'BakeResult',
               'values': 'No, Yes (default No)',
               'does': 'Adds the measurement to the model.'}],
  'notes': '',
  'extra': ''},
 {'title': 'uGap',
  'slug': 'ugap',
  'section': 'drafting',
  'group': 'Drafting',
  'onMenu': True,
  'summary': 'Measures the gap between two objects: the minimum and maximum distance, and the local gap at '
             'any point you click on the source. Useful for checking clearances between surfaces, curves and '
             'breps.',
  'steps': ['Run `uGap`.',
            'At `Select Source (Surface, Curve, Brep, or face/edge - Ctrl+Shift for face/edge)` pick the '
            'source.',
            'At `Select Target (...)` pick the target.',
            'The command line shows `Computing gap...` and then the prompt `Pick point on Source to measure '
            'gap (Enter = bake Min/Max)`.',
            'Click a point on the source to read the local gap at that point. You can click as many points '
            'as you like.',
            'Press Enter to finish. With `BakeResult` Yes the minimum gap line (cyan) and the maximum gap '
            'line (orange) are added with text dots, grouped, on the layer `CheckGap`.'],
  'options': [{'name': 'BakeResult',
               'values': 'No, Yes (default No)',
               'does': 'Adds the Min and Max gap lines to the model when you press Enter.'},
              {'name': 'UnitDisplay',
               'values': 'Document, Meters (default Document)',
               'does': 'Unit of the printed values.'}],
  'notes': '',
  'extra': ''},
 {'title': 'uArea',
  'slug': 'uarea',
  'section': 'drafting',
  'group': 'Drafting',
  'onMenu': True,
  'summary': 'Adds up the area of surfaces, polysurfaces, meshes, closed curves and hatches. The result is '
             'shown in square meters by default.',
  'steps': ['Run `uArea`.',
            'At `Select Objects for Area` pick breps, meshes, closed curves or hatches. Set `BakeResult` and '
            '`UnitDisplay` first if needed.',
            'Press Enter. The total area is printed with its unit (for example m2) and copied to the '
            'clipboard.',
            'With `BakeResult` Yes a text dot `S: ...` is added on the layer `CheckArea`.'],
  'options': [{'name': 'BakeResult',
               'values': 'No, Yes (default No)',
               'does': 'Adds a text dot with the area.'},
              {'name': 'UnitDisplay',
               'values': 'Document, Meters (default Meters)',
               'does': 'Unit of the result.'}],
  'notes': '',
  'extra': ''},
 {'title': 'uVolume',
  'slug': 'uvolume',
  'section': 'drafting',
  'group': 'Drafting',
  'onMenu': True,
  'summary': 'Adds up the volume of closed polysurfaces and meshes. The result is shown in cubic meters by '
             'default.',
  'steps': ['Run `uVolume`.',
            'At `Select Closed Brep/Mesh` pick the solids. Set `BakeResult` and `UnitDisplay` first if '
            'needed.',
            'Press Enter. The total volume is printed with its unit and copied to the clipboard.',
            'With `BakeResult` Yes a text dot `V: ...` is added on the layer `CheckVolume`.'],
  'options': [{'name': 'BakeResult',
               'values': 'No, Yes (default No)',
               'does': 'Adds a text dot with the volume.'},
              {'name': 'UnitDisplay',
               'values': 'Document, Meters (default Meters)',
               'does': 'Unit of the result.'}],
  'notes': '',
  'extra': ''},
 {'title': 'uSlope',
  'slug': 'uslope',
  'section': 'drafting',
  'group': 'Drafting',
  'onMenu': True,
  'summary': 'Measures the slope between two points in a plane (run along X, rise along Y of the chosen '
             'plane), or draws a line at a given slope percent. The slope can be shown as a percentage or as '
             'a ratio.',
  'steps': ['Run `uSlope`.',
            'Optional: set `BakeResult`, `Display` (Percent or Ratio), `Scale`, `Plane` (CPlane or World), '
            '`Draw` and `Slope`.',
            'Pick `Pick Point 1 (Top/Bottom)`.',
            'In measure mode pick Point 2. The slope between the points is printed and copied to the '
            'clipboard. Horizontal run is taken along X and rise along Y of the plane.',
            'With `Draw` Yes the command instead asks `Pick run direction/length (line will be drawn at '
            'slope)` and draws a line from Point 1 at the `Slope` percent.',
            '`BakeResult` or `Draw` adds a line and a text dot on the layer `CheckSlope`.'],
  'options': [{'name': 'BakeResult', 'values': 'No, Yes (default No)', 'does': 'Adds a line and a text dot.'},
              {'name': 'Display',
               'values': 'Percent, Ratio (default Percent)',
               'does': 'Shows the slope as a signed percent or as a ratio.'},
              {'name': 'Scale',
               'values': '0 to 1000, default 0',
               'does': 'Ratio scale. For example 4 gives 4:6 for a 1:1.5 slope. 0 turns it off and shows '
                       '1:N.'},
              {'name': 'Plane',
               'values': 'CPlane, World (default World)',
               'does': 'Plane used to split the points into run and rise.'},
              {'name': 'Draw',
               'values': 'No, Yes (default No)',
               'does': 'Draws a line at the given slope instead of measuring.'},
              {'name': 'Slope',
               'values': '-1000 to 1000, default 2',
               'does': 'Slope percent used when Draw is Yes (for example 2 for 2 percent).'}],
  'notes': 'A vertical pair of points reports Vertical, and a flat pair reports 0% or 0:1.',
  'extra': ''},
 {'title': 'u3dSlope',
  'slug': 'u3dslope',
  'section': 'drafting',
  'group': 'Drafting',
  'onMenu': True,
  'summary': 'Measures the 3D slope between two points as vertical rise over horizontal distance. The result '
             'can be a percentage or a ratio.',
  'steps': ['Run `u3dSlope`.',
            'Optional: set `BakeResult`, `Display` (Percent or Ratio) and `Scale`.',
            'Pick `Pick Point 1 (Top/Bottom)`.',
            'Pick `Pick Point 2`.',
            'The slope (vertical divided by horizontal) is printed and copied to the clipboard. Percent '
            'output is signed, for example +2.50%.',
            'With `BakeResult` Yes a line and a text dot are added on the layer `CheckSlope3D`.'],
  'options': [{'name': 'BakeResult', 'values': 'No, Yes (default No)', 'does': 'Adds a line and a text dot.'},
              {'name': 'Display',
               'values': 'Percent, Ratio (default Percent)',
               'does': 'Shows the slope as a percent or a ratio.'},
              {'name': 'Scale',
               'values': '0 to 1000, default 0',
               'does': 'Ratio scale. With a value of 0.1 or more the ratio is shown as rise:run scaled; '
                       'otherwise as 1:N.'}],
  'notes': 'Points with no horizontal distance report Vertical. Level points report 0% or 0:1.',
  'extra': ''},
 {'title': 'uDwg',
  'slug': 'udwg',
  'section': 'cad',
  'group': 'CAD',
  'onMenu': True,
  'summary': 'Sends selected Rhino geometry straight into the running AutoCAD drawing, with layers, colors '
             'and block instances mapped. Use it to hand off curves, points, text, hatches and blocks to CAD '
             'without exporting a file.',
  'steps': ['Start AutoCAD and open the target drawing.',
            'Run `uDwg`. The prompt reads `Select objects to transfer (Esc to cancel)`. Pick curves, points, '
            'text dots, annotations, hatches or block instances (preselected objects are accepted).',
            'Set the options on the prompt: `LayerExport`, `KeepStyle`, `ConvertCurve`, `InsertBlock`.',
            'Press Enter. A progress meter runs; press Esc to cancel.',
            'Hatches, dimensions and leaders go through a temporary DWG batch INSERT, with a COM fallback.',
            'The command line ends with `Done. Sent: N, Failed: M`.'],
  'options': [{'name': 'LayerExport',
               'values': 'ChildOnly, Full (default ChildOnly)',
               'does': 'Uses only the child layer name, or the full layer path.'},
              {'name': 'KeepStyle',
               'values': 'ByLayer, ByObject (default ByLayer)',
               'does': 'ByLayer takes color and linetype from the layer; ByObject keeps the object '
                       'overrides.'},
              {'name': 'ConvertCurve',
               'values': 'No, Yes (default Yes)',
               'does': 'Yes turns freeform curves into polylines using the document tolerance. No joins '
                       'lines and arcs and leaves freeform curves as splines.'},
              {'name': 'InsertBlock',
               'values': '0 to 100000, default 100',
               'does': 'When a batch has more objects than this number, the INSERT stays one block. 0 always '
                       'uses one block.'}],
  'notes': 'If AutoCAD is not running the command says `AutoCAD is not running.` If AutoCAD is busy it asks '
           'you to press Esc in AutoCAD and run `uDwg` again.',
  'extra': ''},
 {'title': 'uDwgImport',
  'slug': 'udwgimport',
  'section': 'cad',
  'group': 'CAD',
  'onMenu': True,
  'summary': 'Imports one or many DWG and DXF files into the current Rhino document with a chosen source '
             'unit. New layers are grouped under a parent layer named after each file.',
  'steps': ['Run `uDwgImport`. The modal dialog `uDwgImport - Import CAD (Esc to cancel)` opens.',
            'Enter the path in the text box: one file, several files separated by `;`, or a folder. A folder '
            'imports every `*.dwg` and `*.dxf` directly inside it (not subfolders).',
            'Or use the file button to browse for files (multi-select) or the folder button to browse for a '
            'folder.',
            'Choose the source unit in the dropdown.',
            'Optional: click `Options` to open Document Properties, Units.',
            'Click `Import`. Each file is imported with `_-Import` using the chosen units, and its new '
            'top-level layers are moved under a layer named after the file.',
            'The command line reports `Import Complete. N file(s) imported.`'],
  'options': [{'name': 'Path', 'values': 'File, files separated by ;, or folder', 'does': 'What to import.'},
              {'name': 'Browse files', 'values': 'Button', 'does': 'Multi-select file picker.'},
              {'name': 'Browse folder',
               'values': 'Button',
               'does': 'Folder picker; imports *.dwg and *.dxf in that folder.'},
              {'name': 'Unit',
               'values': 'From DWG, Microns, Millimeters, Centimeters, Meters, Kilometers, Inches, Feet, '
                         'Miles (default From DWG)',
               'does': 'Unit of the source file, used for scaling. It is not the document unit.'},
              {'name': 'Options', 'values': 'Button', 'does': 'Opens Document Properties, Units.'},
              {'name': 'Import / Cancel',
               'values': 'Buttons',
               'does': 'Runs the import or closes the dialog.'}],
  'notes': '',
  'extra': ''},
 {'title': 'uDwgExport',
  'slug': 'udwgexport',
  'section': 'cad',
  'group': 'CAD',
  'onMenu': True,
  'summary': 'Batch exports selected objects into several DWG, 3DM or DXF files, one file per object or per '
             'layer group. You control the folder layout and file names from the layer path, with a live '
             'list of the files that will be created.',
  'steps': ['Run `uDwgExport`. At `Select objects to batch export` pick any objects (preselected objects are '
            'accepted).',
            'The modal dialog `uDwgExport - Batch export (DWG/3DM/DXF)` opens. Choose the `Export folder` '
            '(default Desktop).',
            'Choose the `Format` (.dwg, .3dm or .dxf) and the `File name prefix` (default Export).',
            'Choose the `Export mode`: `Layer` (default, one file per layer group) or `Object` (one file per '
            'selected object).',
            'Set `Level N` (0 to 9). Level 0 is the root of the layer table, the same as path level 1.',
            'Tick the parts of the file name: `Level (N)` (on), `Path below N`, `Layer name (leaf)` and '
            '`Suffix` (number or date, on).',
            'Set the layer name written inside each file: `Path from level N down` (off) and `Layer name '
            'only (leaf)` (on).',
            'Optional: set the folder layout `Create subfolders from ancestors above level N` (on) with '
            '`Ancestor levels` 1 to 9 (default 1).',
            'Optional: tick `Include Ref_box in every file (Layer mode)`, `Use date suffix instead of '
            'number` (suffix _yyyyMMdd), set `Start number` (default 1001) and the `Replace in file name` '
            'From and To (default `::` to `_`).',
            'Check the `Files to be created` list, then click `Export`.',
            'The command line reports `Successfully exported N files to: ...`.'],
  'options': [{'name': 'Export folder',
               'values': 'Folder path (default Desktop)',
               'does': 'Destination folder; use Browse to choose.'},
              {'name': 'Format', 'values': '.dwg, .3dm, .dxf', 'does': 'File type of the exported files.'},
              {'name': 'File name prefix',
               'values': 'Text, default Export',
               'does': 'Start of every file name.'},
              {'name': 'Export mode',
               'values': 'Object, Layer (default Layer)',
               'does': 'One file per object, or one file per layer group.'},
              {'name': 'Level N',
               'values': '0 to 9',
               'does': 'Layer level used for grouping and naming. 0 is the root in the layer table.'},
              {'name': 'Level (N)',
               'values': 'On, off (default on)',
               'does': 'Adds the layer name at level N to the file name.'},
              {'name': 'Path below N',
               'values': 'On, off (default off)',
               'does': 'Adds the segments under level N to the file name.'},
              {'name': 'Layer name (leaf)',
               'values': 'On, off (default off)',
               'does': 'Adds the last layer segment to the file name.'},
              {'name': 'Suffix',
               'values': 'On, off (default on)',
               'does': 'Adds a number or a date. Required in Object mode so each file name is unique.'},
              {'name': 'Path from level N down',
               'values': 'On, off (default off)',
               'does': 'Writes the layer path from level N down to each object inside the file.'},
              {'name': 'Layer name only (leaf)',
               'values': 'On, off (default on)',
               'does': 'Writes only the last layer segment inside the file.'},
              {'name': 'Create subfolders from ancestors above level N',
               'values': 'On, off (default on)',
               'does': 'Builds subfolders from the layer segments above level N.'},
              {'name': 'Ancestor levels',
               'values': '1 to 9, default 1',
               'does': 'How many ancestor levels become subfolders.'},
              {'name': 'Include Ref_box in every file',
               'values': 'On, off',
               'does': 'Layer mode: adds the Ref_box object to each file.'},
              {'name': 'Use date suffix instead of number',
               'values': 'On, off',
               'does': 'Uses _yyyyMMdd instead of a number.'},
              {'name': 'Start number',
               'values': '1 to 99999, default 1001',
               'does': 'First number for numeric suffixes.'},
              {'name': 'Replace in file name',
               'values': 'From, To (default :: and _)',
               'does': 'Text replacement applied to the file name.'}],
  'notes': 'Validation messages: `File name: tick at least one of Level (N), Path below N, or Layer name.`, '
           '`Object mode requires a suffix so each file stays unique.`, and an error for duplicate output '
           'paths. Objects whose layer depth is below N are skipped and counted in `Skipped N object(s) with '
           'layer depth below level N.`',
  'extra': ''},
 {'title': 'uRegen',
  'slug': 'uregen',
  'section': 'cad',
  'group': 'CAD',
  'onMenu': True,
  'summary': 'Regenerates all viewports of the drawing that is open in AutoCAD, straight from Rhino. Use it '
             'after sending geometry with uDwg so the drawing refreshes.',
  'steps': ['Make sure AutoCAD is running with a drawing open.',
            'Run `uRegen`.',
            'The command regenerates all viewports in AutoCAD and prints `AutoCAD Regenerated successfully.`',
            'If AutoCAD is not running or is busy the command prints `Error: AutoCAD is not running or '
            'busy.`'],
  'options': [],
  'notes': '',
  'extra': ''},
 {'title': 'uIfcImport',
  'slug': 'uifcimport',
  'section': 'ifc',
  'group': 'IFC',
  'onMenu': True,
  'summary': 'Imports one or many IFC files into Rhino as meshes or Breps, with layers built from the IFC '
             'spatial structure. You choose the engine, what to import, how layers and metadata are written, '
             'and an optional coordinate offset.',
  'steps': ['Run `uIfcImport`. The modal dialog `uIfcImport - Import IFC` opens.',
            'Enter the path in the box (`File path(s) or folder...`): one file, several files separated by '
            '`;`, or a folder. Or use the file and folder buttons to browse.',
            'Choose the `Engine`: `Rhino Built-in`, `IfcOpenShell (Hierarchy)` (default) or `xBIM (Direct '
            'Memory)`.',
            'Tick what to import and how to handle the file, then set `Sharp edge angle` and the `Offset '
            '(m)` X, Y and Z.',
            'Click `Import`. The layer root is the file name (prefixed by the relative folder segments when '
            'a folder was chosen). Layers follow Project, Site, Storey and, optionally, the IFC type.',
            'The command line reports `Files: ok/total`.'],
  'options': [{'name': 'Engine',
               'values': 'Rhino Built-in, IfcOpenShell (Hierarchy), xBIM (Direct Memory) (default '
                         'IfcOpenShell)',
               'does': 'Import engine.'},
              {'name': 'Import Abstract/Spatial Elements (IfcSpace, IfcOpening...)',
               'values': 'On, off (default off)',
               'does': 'Also imports spaces and openings.'},
              {'name': 'When selecting a folder: include IFC files in all subfolders',
               'values': 'On, off (default off)',
               'does': 'Searches subfolders when a folder is chosen.'},
              {'name': 'If layer root exists',
               'values': 'Replace existing (delete old objects), Skip file',
               'does': 'What to do when the file layer root is already in the document.'},
              {'name': 'Export detailed error/skip report to Desktop (.log)',
               'values': 'On, off (default off)',
               'does': 'Writes a log file.'},
              {'name': 'IfcOpenShell: use native Brep when available (extrusions)',
               'values': 'On, off (default off)',
               'does': 'Creates Breps for extrusions instead of meshes. Only for IfcOpenShell.'},
              {'name': 'Organize layers by IFC type',
               'values': 'On, off (default off)',
               'does': 'Off: Project, Site, Storey (and Name) layers with IfcType stored on the object. On: '
                       'adds the IfcType segment to the layer path.'},
              {'name': 'Write IFC metadata to Document User Text',
               'values': 'On, off (default off)',
               'does': 'Stores project data in Document User Text. With several files the keys are '
                       'overwritten and the last file wins.'},
              {'name': 'Write object UserText keys with [Type]',
               'values': 'On, off (default off)',
               'does': 'On writes keys like Pset.Name[Volume] = value so they can be re-exported.'},
              {'name': 'Sharp edge angle',
               'values': '0 to 180 degrees, default 80',
               'does': '0 makes every edge sharp, 180 makes all smooth.'},
              {'name': 'Offset (m) X / Y / Z',
               'values': 'Numbers, default 0',
               'does': 'Subtracted from real-world coordinates so the model sits near the origin.'}],
  'notes': 'Check the layer tree after import. It is the same structure that uIfcExport reads back.',
  'extra': ''},
 {'title': 'uIfcExport',
  'slug': 'uifcexport',
  'section': 'ifc',
  'group': 'IFC',
  'onMenu': True,
  'summary': 'Exports the selected objects to an IFC file. The IFC type comes from object user text or the '
             'layer path, and the spatial structure (project, site, building, storey) comes from the layer '
             'path and the Document User Text.',
  'steps': ['Run `uIfcSetupTemplateFile` once to prepare layers and document keys, and run '
            '`uIfcApplySharedParams` if you want property sets.',
            'Run `uIfcExport`. At `Select objects to export to IFC` pick the objects (preselected objects '
            'are accepted).',
            'The modal dialog `uIfcExport - Export IFC` opens. Choose the `Save to` file with Browse.',
            'Choose the `Engine`: `Python (ifcopenshell)` (default) or `Xbim C# native`, and the `Schema`: '
            '`IFC2x3`, `IFC4` (default) or `IFC4.3`.',
            'Choose the `Meshing`: `Render Mesh (recommended)` or `Detail Mesh (slower)`. For Detail Mesh '
            'also set `Max angle (deg)` and `Max edge-to-surface`.',
            'Tick the checkboxes you need (IFC4X3 Bridge mode, Optimize IFC4 mesh, Export detailed report).',
            'Check the shared-origin label, then click `Export`.',
            'The command line prints the exported, failed and skipped counts.'],
  'options': [{'name': 'Save to',
               'values': 'IFC file path',
               'does': 'Output file. Without a path the dialog shows `Please select a save location.`'},
              {'name': 'Engine',
               'values': 'Python (ifcopenshell), Xbim C# native (default Python)',
               'does': 'Export engine.'},
              {'name': 'Schema',
               'values': 'IFC2x3, IFC4, IFC4.3 (default IFC4)',
               'does': 'IFC schema. The default can come from the Document User Text key IFC.Schema.'},
              {'name': 'Meshing',
               'values': 'Render Mesh (recommended), Detail Mesh (slower)',
               'does': 'Mesh quality used to write geometry.'},
              {'name': 'Max angle (deg)',
               'values': '5 to 35, default 20',
               'does': 'Detail Mesh only: maximum angle between faces.'},
              {'name': 'Max edge-to-surface',
               'values': 'Number, default 1.0 document units',
               'does': 'Detail Mesh only: maximum distance between mesh edges and the surface.'},
              {'name': 'IFC4X3 Bridge mode',
               'values': 'On, off',
               'does': 'Only visible with IFC4.3. Also driven by IFC.UseBridge.'},
              {'name': 'Optimize IFC4 mesh (IfcTriangulatedFaceSet)',
               'values': 'On, off (default on)',
               'does': 'Writes compact triangulated face sets. Ignored for IFC2x3.'},
              {'name': 'Export detailed report to Desktop (.log)',
               'values': 'On, off',
               'does': 'Writes a log file.'},
              {'name': 'Shared origin label',
               'values': 'Information',
               'does': 'Shows the shared origin from IFC.Offset X, Y and Z, or a warning to run '
                       'uIfcSetupTemplateFile.'}],
  'notes': 'IFC type is read from the object user text `IfcType` (or `IFC.Type`), then from a type token in '
           'the layer path, otherwise IfcBuildingElementProxy is used. The layer path is read as segment 0 '
           'Project, 1 Site, 2 Building, 3 Storey, and the rest is group and name. After export, missing '
           'Document User Text keys (site placement, project, site and building names, storey elevations, '
           'map conversion) are written for you. Existing keys are never overwritten.',
  'extra': '## Document User Text\n'
           '\n'
           'Run [`uIfcSetupTemplateFile`](../uifcsetuptemplatefile/) before a serious export. Check or edit '
           'these keys in **Document Properties -> User Text**.\n'
           '\n'
           '| Key | Default | Meaning |\n'
           '| --- | --- | --- |\n'
           '| `IFC.SitePlacement` | `Local` | `Local`: the site is placed at Z = 0, the engineering '
           'elevation stays on the object, and each storey placement Z equals its storey Elevation. '
           '`Anchor`, `Mean` or `Legacy` anchor the site at the mean XYZ of the objects (older behavior). |\n'
           '| `IFC.Storey.{Building}.{Storey}.Elevation` or `IFC.Storey.{Storey}.Elevation` | Lowest Z of '
           'the storey objects when not set | Storey elevation. The name must match the storey segment of '
           'the layer path. |\n'
           '| `IFC.MapConversion.Eastings`, `Northings`, `OrthogonalHeight` | `0` | Map conversion origin. '
           'With `Local` placement and a value of 0 (unset), export writes the mean XY and the mean Z (or '
           '`IFC.Offset.Z`). |\n'
           '| `IFC.Offset.X`, `IFC.Offset.Y`, `IFC.Offset.Z` | `0` | Geometry offset, independent of the map '
           'conversion. |\n'
           '| `IFC.Schema` | `IFC4` | Default schema (`IFC4`, `IFC2X3` or `IFC4X3`). |\n'
           '| `IFC.UseBridge` | `False` | With `IFC4X3`, `True` writes IfcBridge and IfcBridgePart. |'},
 {'title': 'uIfcSetupTemplateFile',
  'slug': 'uifcsetuptemplatefile',
  'section': 'ifc',
  'group': 'IFC',
  'onMenu': True,
  'summary': 'Prepares a document for IFC export: it creates a sample layer tree, writes the IFC Document '
             'User Text keys with placeholder values, and adds a few sample objects and a type catalog. Edit '
             'the placeholders, then use the layer pattern for your own model.',
  'steps': ['Open the Rhino document you want to prepare (a new empty file works best).',
            'Run `uIfcSetupTemplateFile`. The command has no prompts.',
            'It creates sample layers such as '
            '`MyProject::MainSite::Building01::GroundFloor::Case0_ExteriorWall`, `...::GroundFloor::Abutment '
            'LH1::Case1_AbutmentWall`, `...::GroundFloor::Pylon P01::Case2_PylonBody` and '
            '`...::GroundFloor::Case3_GenericElement`, plus a TypeCatalog layer.',
            'It sets the Document User Text keys (schema, bridge flag, project, site and building names, '
            'author and contacts, storey elevation, offsets, site placement, map conversion and sample '
            'material keys).',
            'It migrates and sets the `IFC.SharedParam.*[Type]` keys and creates sample objects with IfcType '
            'values (IfcWall twice, IfcColumn, IfcBuildingElementProxy) and a TypeCatalog_Sample object with '
            'one key per supported type.',
            'Open **Document Properties -> User Text** and replace the placeholders with your project '
            'values.',
            'The command ends with the hint `Run uIfcApplySharedParams on selection, then uIfcExport.`'],
  'options': [],
  'notes': 'Keys written include IFC.Schema=IFC4, IFC.UseBridge=False, '
           'IFC.Storey.Building01.GroundFloor.Elevation=0.0, IFC.Offset.X, Y and Z = 0, '
           'IFC.SitePlacement=Local and the IFC.MapConversion keys (CRSName EPSG:4326, Eastings, Northings '
           'and OrthogonalHeight 0, XAxisAbscissa 1.0, XAxisOrdinate 0.0, Scale 1.0).',
  'extra': ''},
 {'title': 'uIfcApplySharedParams',
  'slug': 'uifcapplysharedparams',
  'section': 'ifc',
  'group': 'IFC',
  'onMenu': True,
  'summary': 'Copies the shared parameter definitions stored in the Document User Text onto the selected '
             'objects as object user text. After that, uIfcExport writes them as IFC properties. Keys that '
             'an object already has are not overwritten.',
  'steps': ['Define shared parameters in **Document Properties -> User Text** as '
            '`IFC.SharedParam.<ObjectKey>[Type]`, or let `uIfcSetupTemplateFile` create the samples.',
            'Run `uIfcApplySharedParams`. The command migrates document keys to the `Key[Type]` form and '
            'reads all `IFC.SharedParam.*` keys. If none exist it shows help.',
            'At `Select objects to apply shared parameters` pick the objects (preselected objects are '
            'accepted).',
            'Each key is copied to each object. A key is skipped when the object already has it, or has the '
            'same key without a bracket and with a value. An empty default is written as a single space.',
            'The command line reports `Applied N shared parameter(s) to M object(s).`',
            'Edit the values per object in Rhino Properties -> Attribute User Text, then run `uIfcExport`.'],
  'options': [],
  'notes': 'Document keys use `IFC.SharedParam.<ObjectKey>[Type]`. Object user text uses '
           '`<ObjectKey>[Type]`. On export the bracket is removed for the property name and the property is '
           'written as an IfcPropertySingleValue with that nominal type.',
  'extra': '## Key shape\n'
           '\n'
           'The type goes in square brackets at the end of the key name, never in the value.\n'
           '\n'
           '| Right | Wrong |\n'
           '| --- | --- |\n'
           '| `Dimensions.QTO.Area[Area] = 12.5` | `Spec.Flag = True[IfcBoolean]` |\n'
           '| `Pset_WallCommon.IsExternal[YesNo] = False` | |\n'
           '| `Spec.Code[IfcIdentifier] = W-01` | |\n'
           '\n'
           '## Type tokens\n'
           '\n'
           '| Token | IFC type |\n'
           '| --- | --- |\n'
           '| `Text`, `IfcLabel` | IfcLabel |\n'
           '| `IfcText` | IfcText |\n'
           '| `IfcIdentifier` | IfcIdentifier |\n'
           '| `YesNo`, `IfcBoolean` | IfcBoolean |\n'
           '| `IfcLogical` | IfcLogical |\n'
           '| `Integer`, `IfcInteger` | IfcInteger |\n'
           '| `Number`, `IfcReal` | IfcReal |\n'
           '| `Length`, `IfcLengthMeasure` | IfcLengthMeasure |\n'
           '| `Area`, `IfcAreaMeasure` | IfcAreaMeasure |\n'
           '| `Volume`, `IfcVolumeMeasure` | IfcVolumeMeasure |\n'
           '| `IfcDate`, `IfcDateTime`, `IfcTime`, `IfcDuration`, `IfcTimeStamp` | Date and time types |\n'
           '| `IfcURIReference` | IfcURIReference |\n'
           '| `IfcDescriptiveMeasure` | IfcDescriptiveMeasure |'},
 {'title': 'uIfcInstall',
  'slug': 'uifcinstall',
  'section': 'ifc',
  'group': 'IFC',
  'onMenu': True,
  'summary': 'Installs the Python packages that the IFC commands need into the Python that Rhino uses. A '
             'dialog shows which packages are present and installs the missing ones with one click.',
  'steps': ['Run `uIfcInstall`. The modal dialog `Install IFC Dependencies` opens.',
            'Read the status list: `ifcopenshell`, `numpy` and `orjson` (optional, makes JSON handling 5 to '
            '10 times faster) with their versions and a check or cross.',
            "Click `Install`. The command installs the packages into Rhino's Python with pip. The output "
            'text area shows the pip output.',
            'Wait until the status list updates. If installing `orjson` fails the import still works without '
            'it.',
            'Click `Close`.'],
  'options': [{'name': 'Install',
               'values': 'Button',
               'does': 'Installs the missing packages. Enabled only while ifcopenshell or numpy is missing.'},
              {'name': 'Close', 'values': 'Button', 'does': 'Closes the dialog.'}],
  'notes': 'ifcopenshell and numpy are required; orjson is optional.',
  'extra': ''},
 {'title': 'commaMenu',
  'slug': 'commamenu',
  'section': 'more',
  'group': 'More',
  'onMenu': False,
  'summary': 'Shows a pop-up text menu at the pointer with every Comma command grouped by category. Use it '
             'when the Comma menu bar is not visible or from a hotkey.',
  'steps': ['Run `commaMenu`. A text menu opens near the pointer.',
            'The first item is `License Manager` (runs `commaRegister`). Below it are the submenus Doc, '
            'Curve, Surface, Brep, Mesh, Drafting, CAD and IFC.',
            'Open a submenu and click a command. The command runs as `! _<command>`.',
            'At the end, `About` shows the `About CommaRh...` dialog and `User Manual`, which opens the '
            'manual in the web browser.'],
  'options': [],
  'notes': 'commaMenu is also the first item of the uQuickTools menu.',
  'extra': ''},
 {'title': 'uExportBox',
  'slug': 'uexportbox',
  'section': 'more',
  'group': 'More',
  'onMenu': False,
  'summary': 'Exports the part of the model that lies inside a closed box to a new 3DM file. Meshes are '
             'clipped to the box in parallel, so large IFC models export quickly.',
  'steps': ['Run `uExportBox`. At `Select clipping box (closed polysurface)` pick a polysurface or extrusion '
            'that is a closed box. Otherwise the command says `Selected object is not a closed box-like '
            'Brep.`',
            'Choose a `Preset`: `Speed` (default), `Quality` or `Custom`. Changing `IncludeHidden` or '
            '`Boolean` switches the preset to Custom.',
            'Optional: set `IncludeHidden` (No or Yes) and `Boolean` (Off or On).',
            'Press Enter. The Save dialog `Export Box Region` opens; choose a `.3dm` file (default '
            '`uExportBox.3dm`).',
            'The meshes are clipped to the box and written to the file. The command line reports `uExportBox '
            'done - N meshes written to ...`.'],
  'options': [{'name': 'Preset',
               'values': 'Speed, Quality, Custom (default Speed)',
               'does': 'Speed: IncludeHidden No and Boolean Off. Quality: IncludeHidden Yes and Boolean On. '
                       'Custom: your own mix.'},
              {'name': 'IncludeHidden', 'values': 'No, Yes', 'does': 'Also exports hidden objects.'},
              {'name': 'Boolean',
               'values': 'Off, On',
               'does': 'On makes watertight clipped results with a Boolean operation; Off only cuts the '
                       'meshes, which is faster.'}],
  'notes': '',
  'extra': ''},
 {'title': 'uVisibilityAdd',
  'slug': 'uvisibilityadd',
  'section': 'more',
  'group': 'More',
  'onMenu': False,
  'summary': 'Adds more objects to the Comma Visibility panel that was opened with uVisibility. It is '
             'normally run from the Add button of that panel.',
  'steps': ['Run `uVisibility` first to open the Comma Visibility panel.',
            'Click `Add` in the panel, or run `uVisibilityAdd`. The prompt reads `Select more objects to '
            'add.`',
            'Select more objects and press Enter (or Esc) to finish.',
            'The added objects appear in the panel grid, where you can use `Hide`, `Iso`, `Show`, `Remove`, '
            '`Select` and `Clear`.'],
  'options': [],
  'notes': 'If the panel is not open the command says `Comma Visibility panel is not open. Run uVisibility '
           'first.` The panel has a search box (`Search layer, type...`), sync and group toggles, and the '
           'columns Object and Vis.',
  'extra': ''}]



_CODE_SPAN = re.compile(r"(`[^`]*`)")


def esc(text):
    """Escape < and > outside inline code spans so Hugo does not treat them as HTML."""
    parts = _CODE_SPAN.split(text)
    for i in range(0, len(parts), 2):
        parts[i] = parts[i].replace("<", "&lt;").replace(">", "&gt;")
    return "".join(parts)


def cell(text):
    """Make text safe for a markdown table cell."""
    return esc(str(text)).replace("|", "\\|").replace("\r", " ").replace("\n", " ").strip()


def yaml_str(text):
    return text if re.fullmatch(r"[A-Za-z0-9_.-]+", text) else '"' + text.replace('"', '\\"') + '"'


def render(cmd, weight):
    title = cmd["title"]
    on_menu = bool(cmd["onMenu"])
    if on_menu:
        menu = "`commaMenu` " + ARROW + " **" + cmd["group"] + "**"
    else:
        menu = "Not on `commaMenu`. Type the command name."

    out = []
    out.append("---")
    out.append("title: " + yaml_str(title))
    out.append("weight: " + str(weight))
    out.append("aliases:")
    out.append("  - /help/" + title.lower() + "/")
    out.append("---")
    out.append("")
    out.append("| Menu | Command |")
    out.append("| --- | --- |")
    out.append("| " + menu + " | `" + title + "` |")
    out.append("")
    out.append(esc(cmd["summary"].strip()))
    out.append("")

    steps = cmd.get("steps") or []
    if steps:
        out.append("#### Steps")
        out.append("")
        for i, s in enumerate(steps, 1):
            out.append(str(i) + ". " + esc(s.strip()))
        out.append("")

    options = cmd.get("options") or []
    if options:
        out.append("#### Options")
        out.append("")
        out.append("| Option | Values | What it does |")
        out.append("| --- | --- | --- |")
        for o in options:
            out.append("| " + cell(o["name"]) + " | " + cell(o["values"]) + " | " + cell(o["does"]) + " |")
        out.append("")

    notes = (cmd.get("notes") or "").strip()
    if notes:
        out.append(esc(notes))
        out.append("")

    extra = (cmd.get("extra") or "").strip()
    if extra:
        out.append(extra)
        out.append("")

    return "\n".join(out).rstrip() + "\n"


def main():
    written = 0
    errors = []
    weights = {}
    seen = set()

    if len(COMMANDS) != EXPECTED_COUNT:
        errors.append("expected %d commands, found %d" % (EXPECTED_COUNT, len(COMMANDS)))

    for cmd in COMMANDS:
        title = cmd.get("title", "?")
        try:
            section = cmd["section"]
            slug = cmd["slug"]
            if section not in SECTIONS:
                raise ValueError("unknown section " + repr(section))
            if cmd["group"] != SECTIONS[section]:
                raise ValueError("group %r does not match section %r" % (cmd["group"], section))
            if slug != title.lower():
                raise ValueError("slug %r is not lowercase title" % slug)
            if slug in seen:
                raise ValueError("duplicate slug")
            seen.add(slug)
            if bool(cmd["onMenu"]) != (slug not in NOT_ON_MENU):
                raise ValueError("onMenu flag does not match the agreed list")
            if re.search(r"(?im)^#+\s*(limits?|free|trial)\b", render(cmd, 0)):
                raise ValueError("forbidden Limits/Free/Trial heading")

            weights[section] = weights.get(section, 0) + 1
            text = render(cmd, weights[section])

            folder = os.path.join(OUT, section)
            os.makedirs(folder, exist_ok=True)
            path = os.path.join(folder, slug + ".md")
            with io.open(path, "w", encoding="utf-8", newline="\n") as fh:
                fh.write(text)
            written += 1
        except Exception as exc:  # report and continue
            errors.append("%s: %s" % (title, exc))

    print("Files written: %d (of %d commands)" % (written, len(COMMANDS)))
    if errors:
        print("Errors (%d):" % len(errors))
        for e in errors:
            print("  - " + e)
    else:
        print("Errors: none")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
