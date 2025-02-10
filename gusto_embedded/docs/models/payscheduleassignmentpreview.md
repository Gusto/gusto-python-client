# PayScheduleAssignmentPreview

The representation of a pay schedule assignment preview.


## Fields

| Field                                                                                                      | Type                                                                                                       | Required                                                                                                   | Description                                                                                                |
| ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| `type`                                                                                                     | [OptionalNullable[models.PayScheduleAssignmentPreviewType]](../models/payscheduleassignmentpreviewtype.md) | :heavy_minus_sign:                                                                                         | The pay schedule assignment type.                                                                          |
| `employee_changes`                                                                                         | List[[models.PayScheduleAssignmentEmployeeChange](../models/payscheduleassignmentemployeechange.md)]       | :heavy_minus_sign:                                                                                         | A list of pay schedule changes including pay period and transition pay period.                             |