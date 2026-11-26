---
title: "Check Param"
weight: 40
---

**Ribbon** · Comma Rvt → Parameter → Check Param

Check whether required parameters exist and contain values on supported Revit elements.

1. Choose the scope and a **Settings File** under **Configuration**. Use **Edit Settings** to adjust which parameter names are required.
2. Click **Run Check**. Review the results by parameter and status. **Error** means the parameter is absent, **Missing** means its value is empty, **Warning** means it contains a recognized placeholder, and **Pass** means it has a value.
3. Double-click a result or use **Select Element** to locate it in Revit.

The checker can use a populated type parameter when the instance value is empty. You can exchange values with Excel and use **Apply Changes** to write edits back to the model.
