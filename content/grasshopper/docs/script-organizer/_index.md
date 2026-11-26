---
title: Script Organizer
weight: 30
---

Comma Script Organizer keeps a Grasshopper canvas readable while you work. It adds a **Comma** menu to Grasshopper's menu bar and a row of buttons to the canvas toolbar, and it works on the active Grasshopper document.

{{< cards >}}

  {{< card link="color-groups" icon="color-swatch" title="Color Group" subtitle="Color groups from the prefix of their name, or with the canvas color buttons" >}}

  {{< card link="fix-params" icon="eye" title="Fix Params" subtitle="Show parameter names instead of icons on every new parameter" >}}

  {{< card link="fix-wires" icon="switch-horizontal" title="Fix Wire" subtitle="Fade the wires that cross from one group to another" >}}

  {{< card link="scribble" icon="pencil" title="Scribble" subtitle="Label groups with scribbles and resize them" >}}

  {{< card link="input-tools" icon="trash" title="Input tools" subtitle="Clear or internalise the inputs of selected components" >}}

  {{< card link="copy-without-wires" icon="duplicate" title="Ctrl+Alt copy without wires" subtitle="Drag-copy components without their input wires" >}}

  {{< card link="settings" icon="cog" title="Settings and shortcuts" subtitle="Automatic modes, prefix colors, canvas opacity and keyboard shortcuts" >}}

  {{< card link="changelog" icon="clock" title="Changelog" subtitle="What changed in each version" >}}

{{< /cards >}}

## Automatic and manual modes

Three features have an **Auto** mode that is **on by default**: Color Group, Fix Params and Fix Wire. In automatic mode they react to what you do on the canvas. Each also has a **Run Once** command in the **Comma** menu that works on the whole document at the time you choose, whether the automatic mode is on or not, and a **Reset Default** command that undoes the effect on the selected objects (or on everything when nothing is selected).

Settings are stored in Grasshopper's own settings, so they are kept between sessions.
