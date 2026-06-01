# TimeOffActivity

Representation of a Time Off Activity


## Fields

| Field                                                               | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `policy_uuid`                                                       | *OptionalNullable[str]*                                             | :heavy_minus_sign:                                                  | unique identifier of a time off policy                              |
| `time_off_type`                                                     | [Optional[models.TimeOffType]](../models/timeofftype.md)            | :heavy_minus_sign:                                                  | Type of the time off activity                                       |
| `policy_name`                                                       | *OptionalNullable[str]*                                             | :heavy_minus_sign:                                                  | The name of the time off policy for this activity                   |
| `event_type`                                                        | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | The type of the time off event/activity                             |
| `event_description`                                                 | *OptionalNullable[str]*                                             | :heavy_minus_sign:                                                  | A description for the time off event/activity                       |
| `effective_time`                                                    | *OptionalNullable[str]*                                             | :heavy_minus_sign:                                                  | The datetime of the time off activity                               |
| `balance`                                                           | *OptionalNullable[str]*                                             | :heavy_minus_sign:                                                  | The time off balance at the time of the activity                    |
| `balance_change`                                                    | *OptionalNullable[str]*                                             | :heavy_minus_sign:                                                  | The amount the time off balance changed as a result of the activity |