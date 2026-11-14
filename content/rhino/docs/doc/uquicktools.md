---
title: uQuickTools
weight: 7
aliases:
  - /help/uquicktools/
---

| Menu | Command |
| --- | --- |
| `commaMenu` → **Doc** | `uQuickTools` |

Shows a pop-up menu at the cursor with your favorite commands and macros. Click an item to run it. The list is edited with uQuickToolsConfig.

#### Steps

1. Run `uQuickTools` (it works best when assigned to a hotkey or alias). A menu appears at the cursor with the prompt `Select item from quick tools (move to highlight, click to run, ESC to cancel)`.
2. Move the cursor to highlight an item. `CommaMenu` is always first and `Setup` (opens `uQuickToolsConfig`) is always last; your own items are in between.
3. Click an item to run it, or press Esc to cancel.
4. A Command item runs as `! _<command>` after the menu closes.
5. A Macro item runs its script. In `Once` mode the script runs one time with the current selection. In `PerObject` mode each selected object is selected alone, the script runs, and the original selection is restored afterwards.

#### Options

| Option | Values | What it does |
| --- | --- | --- |
| CommaMenu | Default item | Opens the Comma command menu (commaMenu). |
| Setup | Default item | Opens uQuickToolsConfig to edit the list. |
| Command item | Any Rhino or Comma command | Runs the command as ! _&lt;command&gt;. |
| Macro item - Once | Run mode | Runs the script once with the current selection. |
| Macro item - PerObject | Run mode | Runs the script for every selected object, one at a time (needs a selection). |

PerObject macros need a selection; otherwise the command line says `uMacro: PerObject mode needs a selection.` After a run it reports how many objects the script ran on.
