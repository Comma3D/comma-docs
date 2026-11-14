---
title: uIfcApplySharedParams
weight: 4
aliases:
  - /help/uifcapplysharedparams/
---

| Menu | Command |
| --- | --- |
| `commaMenu` → **IFC** | `uIfcApplySharedParams` |

Copies `IFC.SharedParam.*[Type]` document keys onto the selection (skips keys that already exist on the object). The type token is in the key; the value is user data.

#### Steps

1. Select objects to apply shared parameters`.


## Key shape

```text
Right: Dimensions.QTO.Area[Area] = 12.5
Right: Pset_WallCommon.IsExternal[YesNo] = False
Wrong: Spec.Flag = True[IfcBoolean]
```

| Token in `[…]` | IFC nominal value |
| --- | --- |
| `Text` / `IfcLabel` | `IfcLabel` |
| `IfcText` | `IfcText` |
| `IfcIdentifier` | `IfcIdentifier` |
| `YesNo` / `IfcBoolean` | `IfcBoolean` |
| `Integer` / `IfcInteger` | `IfcInteger` |
| `Number` / `IfcReal` | `IfcReal` |
| `Length` / `Area` / `Volume` | length / area / volume measures |
| `IfcDate` / `IfcDateTime` / `IfcTime` / `IfcDuration` | time types |
