---
title: uQuickToolsConfig
weight: 8
aliases:
  - /help/uquicktoolsconfig/
---

| Menu | Command |
| --- | --- |
| Not on `commaMenu`. Type the command name. | `uQuickToolsConfig` |

Opens the Quick Tools Setup dialog where you build the uQuickTools menu from commands and macros. Items can be reordered, imported and exported as XML.

#### Steps

1. Run `uQuickToolsConfig`, or choose `Setup` in the uQuickTools menu. The modal `Quick Tools Setup` dialog opens with the grid Label, Type, Command / Script, Mode, Tooltip.
2. Click `+ Cmd` to add a command. Enter a Label, the Command (for example `uLayer`) and an optional Tooltip. Label and Command are required.
3. Click `+ Macro` to add a macro. In the Edit Macro dialog set Name, Tooltip, Mode (`Once` or `PerObject`) and paste the Script. Do not start the script with `!`.
4. Select a row and click `Edit` to change it, `-` to remove it, and the up and down arrows to reorder.
5. Optional: `Export` writes the setup to a Comma Quick Tools XML file, and `Import` loads one. Import asks `Replace current items with imported file?`: Yes replaces, No merges (appends), Cancel aborts.
6. Optional: use the folder button to open the folder that holds the configuration file.
7. Click `Reset` to clear all custom items (after a confirmation), then `Save` to keep the changes or `Cancel` to discard them. Save reports `Quick tools configuration saved (commands + macros).`

#### Options

| Option | Values | What it does |
| --- | --- | --- |
| + Cmd | Button | Adds a command item (Label, Command, Tooltip). |
| + Macro | Button | Adds a macro item (Name, Tooltip, Mode, Script). |
| Edit | Button | Edits the selected item. |
| - | Button | Removes the selected item. |
| Up / Down | Buttons | Moves the selected item in the menu order. |
| Reset | Button | Clears custom items after confirmation. |
| Import / Export | XML Comma Quick Tools | Loads or saves the setup; Import can replace or merge. |
| Folder | Button | Opens the configuration folder. |
| Mode | Once, PerObject | Macro run mode: once with the selection, or once per selected object. |
| Save / Cancel | Buttons | Keeps or discards the changes. |

The CommaMenu and Setup items are reserved and cannot be added, removed or imported.
