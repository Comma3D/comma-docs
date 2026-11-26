---
title: Managing the library
weight: 2
---

## Rename and remove

| Where | How | What it does |
| --- | --- | --- |
| A snippet in the menu or in the search results | Right-click, then **Rename** | Type the new name and press **Enter** (**Esc** cancels). The name follows the same rules as when saving: no `\`, `/` or `.`, and unique within the tab. |
| A snippet | Right-click, then **Remove** | Deletes the snippet from the library straight away. There is no confirmation and no undo. |
| A tab in the menu | Right-click, then **Rename Tab** | Renames the tab and moves all its snippets with it. The name must not exist already. |
| A tab | Right-click, then **Remove Tab** | Deletes the tab and every snippet in it. |

{{% callout type="warning" %}}
**Remove** and **Remove Tab** delete the files from the library at once. There is no confirmation and no undo, so back up first if you are not sure.
{{% /callout %}}

## Open the library folder

The last item of the dropdown, **Open library**, opens the library folder in Windows Explorer.

## Where the files are

The library is a `Comma` folder inside Grasshopper's settings folder. Every snippet is one XML file, named after its tab and its name:

```text
Comma.<Tab name>.<Snippet name>.xml
```

For example `Comma.Curves.Divide and label.xml`. The file holds the components, the description and the picture.

## Share and back up snippets

- **Back up:** copy the `Comma.*.xml` files from the library folder.
- **Share or restore:** right-click the **Comma button** and choose one or more `.xml` snippet files. They are copied into the library, and a file with the same name is replaced.
- You can also drop the files into the library folder yourself. They show up the next time you open the menu or click the search box.

Because the tab is part of the file name, renaming a file by hand changes the tab or the snippet name.
