---
title: Color Group
weight: 1
---

Color Group colors Grasshopper groups for you. A group is colored from the **prefix** of its name: the text before the first underscore, including the underscore. A group named `r_inputs` has the prefix `r_`.

## Automatic mode

With **Auto** on, a group is recolored when you **rename** it, and when groups are added to the canvas or pasted (all of them in one undo step). Color-only changes do not trigger it, so a color you set by hand stays.

A group is left untouched when:

- its name has no underscore, for example `inputs`;
- its prefix is not in the prefix table.

A group with **no name at all** gets the default group color, unless it already has a prefix color.

{{% callout type="info" %}}
**Your colors stay.** Automatic mode only reacts when a group is renamed or added. A color you set by hand is never snapped back by it, and only **Reset Default** does that.
{{% /callout %}}

## Default prefix colors

| Prefix | Color (R, G, B) |
| --- | --- |
| `i_` | green (125, 217, 98) |
| `s_` | orange (224, 145, 81) |
| `g_` | off-white (245, 243, 237) |
| `c_` | beige (235, 227, 206) |
| `o_` | light blue (160, 218, 242) |
| `r_` | red (242, 63, 63) |
| `y_` | yellow (247, 244, 64) |
| `u_` | purple (208, 115, 230) |
| `od_` | gray (97, 97, 97) |

The prefixes have no built-in meaning: use them however your team names things. Change, add or remove prefixes in [Settings](../settings/). A prefix you type without a trailing underscore gets one added.

## Canvas color buttons

The canvas toolbar has one color swatch per prefix. Select some objects and click a swatch to put them in a new group of that color. If a **group is selected**, the swatch recolors that group (and every selected group) instead of creating a new one, in one undo step.

By default the new group is named from the prefix. Two options in [Settings](../settings/) change this:

- **Remove Prefix**: the leading segment is stripped from the name (`r_references` becomes `references`).
- **Color Only (no text)**: the new group has no name and carries only the color. Unnamed groups that have a prefix color are not reset to the default color by automatic mode.

## Commands

| Command in **Comma → Color Group** | What it does |
| --- | --- |
| **Run One** | Recolors all groups in the active document now. |
| **Reset Default** | Resets the selected groups, or all groups when nothing is selected, to the default group color. |

Every color change can be undone with **Ctrl+Z**, and one action that changes several groups is a single undo step.
