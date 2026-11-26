---
title: Changelog
weight: 8
---

All notable changes to the Comma_GH_ScriptOrganizer package, newest first.

## 26.1.6 — 2026-10-27

- Republished: 26.1.5 was built without the 26.1.4 changes (Color Only option,
  recolor selected groups). This release contains both.

## 26.1.5 — 2026-10-26

- Added "Ctrl+Alt Copy Without Wires" (Comma menu toggle, on by default): when
  drag-copying with Alt, holding Ctrl as the mouse is released makes the copies
  come out without the input wires from the original sources. Wires between the
  copied objects themselves are kept.
- Fixed Ctrl+Alt copy handlers staying attached to a closed document or being
  hooked to the canvas more than once.

## 26.1.4 — 2026-10-12

- New "Color Only (no text)" option in the Color Group dialog: the canvas color
  buttons create groups with no name, carrying only the color. Unnamed groups
  whose color matches a preset are no longer reset to the default color by
  auto mode.
- When a group is selected, the canvas color buttons now recolor that group
  (one undo step for all selected groups) instead of creating a new group
  around it.

## 26.1.3 — 2026-10-07

- Color Group is now undoable (Ctrl+Z) in both manual and automatic mode:
  recoloring/renaming a group, Run Once, Reset Default (all/selected), and
  the canvas color swatch buttons (which create a new group) all properly
  record undo. Multiple groups changed in a single action share one combined
  undo record, so one Ctrl+Z reverts the whole action instead of only the
  last group touched.
- Scribble (Label Groups, and the font Size +/- buttons) is now undoable for
  the same reason: creating, removing, and re-adding scribbles, and updating
  group membership, previously left nothing on the undo stack.
- Restored the Default/Faint/Hidden wire-display button icons, which were
  missing from the previous release.

## 26.1.2 — 2026-09-14

- Opacity dropdown now behaves like Grasshopper's native Zoom Factor control:
  it accepts a typed custom percentage (clamped to 20%–100%) in addition to
  the 100% / 70% / 50% presets, normalizes the text to "NNN%" on commit, and
  reverts on Escape.
- Fixed the Opacity dropdown showing two overlapping/flickering tooltips on
  hover.

## 26.1.1 — 2026-08-19

- Added an Opacity dropdown (100% / 70% / 50%) to the canvas toolbar for
  adjusting the Grasshopper editor window's transparency.

## 26.1.0 — 2026-08-02

- Bounded the Scribble tool's font size to the range [5, 100].
- Removed the Auto Reference feature (creating Param > Geometry components from
  the Rhino selection) and its "Layer Info" setting.
- Fixed the canvas toolbar's color and wire-display button groups swapping
  places when one of the two was rebuilt after the other.
- Auto Reference now creates a Grasshopper document if none is open yet
  (folded in from the unpublished 1.2.0 line).
- Settings dialog now applies feature toggles (Auto, Remove Prefix, Debug,
  etc.) before applying color changes, so color updates see the correct flags.
- Fix Params and Fix Wire now refresh the canvas immediately after running.
- Versioning scheme moved to 26.1.0 going forward.

## 1.1.1

- Maintenance release.

## 1.1.0 — 2026-03-31

- Renamed the plugin/assembly from Comma.GH.ColorGroups to
  Comma.GH.ScriptOrganizer.
- Added the Scribble tool: label selected groups from their name, and
  increase/decrease scribble font size.
- Simplified Internalize Selected Inputs.
- Improved Auto Reference and Fix Wire behavior.

## 1.0.0 — 2026-03-30

- General availability release.

## 0.1.0 — 2026-03-30

- Initial release: automatic group coloring by name prefix, canvas/panel
  color settings, and fainted cross-group wires.
