---
title: uIfcApplySharedParams
weight: 4
aliases:
  - /help/uifcapplysharedparams/
---

| Menu | Command |
| --- | --- |
| `commaMenu` → **IFC** | `uIfcApplySharedParams` |

Copies the shared parameter definitions stored in the Document User Text onto the selected objects as object user text. After that, uIfcExport writes them as IFC properties. Keys that an object already has are not overwritten.

#### Steps

1. Define shared parameters in **Document Properties -&gt; User Text** as `IFC.SharedParam.<ObjectKey>[Type]`, or let `uIfcSetupTemplateFile` create the samples.
2. Run `uIfcApplySharedParams`. The command migrates document keys to the `Key[Type]` form and reads all `IFC.SharedParam.*` keys. If none exist it shows help.
3. At `Select objects to apply shared parameters` pick the objects (preselected objects are accepted).
4. Each key is copied to each object. A key is skipped when the object already has it, or has the same key without a bracket and with a value. An empty default is written as a single space.
5. The command line reports `Applied N shared parameter(s) to M object(s).`
6. Edit the values per object in Rhino Properties -&gt; Attribute User Text, then run `uIfcExport`.

Document keys use `IFC.SharedParam.<ObjectKey>[Type]`. Object user text uses `<ObjectKey>[Type]`. On export the bracket is removed for the property name and the property is written as an IfcPropertySingleValue with that nominal type.

## Key shape

The type goes in square brackets at the end of the key name, never in the value.

| Right | Wrong |
| --- | --- |
| `Dimensions.QTO.Area[Area] = 12.5` | `Spec.Flag = True[IfcBoolean]` |
| `Pset_WallCommon.IsExternal[YesNo] = False` | |
| `Spec.Code[IfcIdentifier] = W-01` | |

## Type tokens

| Token | IFC type |
| --- | --- |
| `Text`, `IfcLabel` | IfcLabel |
| `IfcText` | IfcText |
| `IfcIdentifier` | IfcIdentifier |
| `YesNo`, `IfcBoolean` | IfcBoolean |
| `IfcLogical` | IfcLogical |
| `Integer`, `IfcInteger` | IfcInteger |
| `Number`, `IfcReal` | IfcReal |
| `Length`, `IfcLengthMeasure` | IfcLengthMeasure |
| `Area`, `IfcAreaMeasure` | IfcAreaMeasure |
| `Volume`, `IfcVolumeMeasure` | IfcVolumeMeasure |
| `IfcDate`, `IfcDateTime`, `IfcTime`, `IfcDuration`, `IfcTimeStamp` | Date and time types |
| `IfcURIReference` | IfcURIReference |
| `IfcDescriptiveMeasure` | IfcDescriptiveMeasure |
