---
title: Installing
weight: 1
---

Comma for Grasshopper is two separate plugins. Install the one you need, or both.

## Comma Components

1. Download the zip that matches your Rhino from the **Releases** page:

   | Rhino | File |
   | --- | --- |
   | Rhino 7 (Windows) | `Comma.GH.Components-v<version>-net48.zip` |
   | Rhino 8 (Windows) | `Comma.GH.Components-v<version>-net7.0-windows.zip` |
   | Rhino 8 (Mac) | `Comma.GH.Components-v<version>-net7.0.zip` |

2. On Windows, right-click the zip, choose **Properties**, tick **Unblock** and click **OK**.

   {{% callout type="warning" %}}
   Do not skip the unblock step. Windows blocks downloaded `.gha` files and Grasshopper will not load them.
   {{% /callout %}}

3. Extract the zip into a folder inside Grasshopper's Components folder (in Grasshopper: **File → Special Folders → Components Folder**).
4. Restart Rhino.

The zip holds `Comma.GH.Components.gha` and `Comma.Core.dll`. Keep them together in the same folder.

## Comma Script Organizer

Comma Script Organizer is a Rhino 8 package named `Comma_GH_ScriptOrganizer`, built for Grasshopper on Windows. Install it from Rhino's Package Manager (type `PackageManager` in the Rhino command line and search for `Comma_GH_ScriptOrganizer`), then restart Rhino.

## Comma Container

Comma Container adds the snippet button and search box. It is a separate plugin, `Comma.GH.Container.gha`, and it is **not** part of the Script Organizer package. It works together with Script Organizer (it places its toolbar items before Script Organizer's), so install both. Put the `.gha` in a folder inside Grasshopper's Components folder (**File → Special Folders → Components Folder**), unblock it on Windows as described above, and restart Rhino.

## Check that it loaded

Open Grasshopper. You should see:

- a **Comma** tab in the component ribbon (Comma Components);
- a **Comma** menu in Grasshopper's menu bar and a row of color, wire and **Opacity** controls at the end of the canvas toolbar (Comma Script Organizer);
- a **Comma button** and a **Search** box on the canvas toolbar, before the Script Organizer controls (Comma Container).

If a plugin does not show up, check the Rhino command line for load errors and make sure the zip was unblocked and extracted completely.
