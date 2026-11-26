---
title: Saving and inserting snippets
weight: 1
---

## Save the selected components

1. Select the components you want to keep on the canvas.
2. Click the **Comma button** on the canvas toolbar (the main part, not the arrow). The **Add new group** dialog opens.
3. Fill in the three fields. All are required:

   | Field | What to enter |
   | --- | --- |
   | **Tab name** | The tab to file the snippet under. Type a new name, or start typing to pick an existing tab from the suggestions. |
   | **Group name** | The snippet's name. The arrow lists the names that already exist. |
   | **Description** | What the snippet does. It shows in the tooltip when you hover over the snippet. |

4. Click **Done**. The snippet is saved at once and appears in the menu and in the search results.

If nothing is selected, the dialog says *No selected component*.

### Names

Tab and snippet names can **not** contain `\`, `/` or `.` (the dot separates the parts of the file name, see [Managing the library](../managing-the-library/)). Snippet names are unique across **all** tabs. If the name already exists you are asked whether to overwrite it; if you say yes, the old snippet is replaced and ends up in the tab you chose.

## Insert a snippet

You can pick a snippet in two ways:

- **From the menu:** click the **arrow** of the Comma button, point at a tab, and click a snippet. Hover over a snippet to see its tab and description.
- **From the search box:** click **Search** and type part of a snippet's name or of a tab's name (not case sensitive). Up to 50 matches are listed; click one.

{{% callout type="info" %}}
**Search also matches tab names.** Typing a tab name lists every snippet in that tab.
{{% /callout %}}

Then **click on the canvas** where you want it. The snippet is pasted with its middle at the cursor. If no definition is open, a new one is created. The paste is one undo step, so **Ctrl+Z** removes it.

The pasted objects get new identities, so you can insert the same snippet as many times as you like.
