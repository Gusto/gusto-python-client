# TimeOffActivity

Representation of a Time Off Activity


## Fields

| Field                                                               | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `policy_uuid`                                                       | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | unique identifier of a time off policy                              |
| `time_off_type`                                                     | [Optional[models.TimeOffType]](../models/timeofftype.md)            | :heavy_minus_sign:                                                  | Type of the time off activity                                       |
| `policy_name`                                                       | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | The name of the time off policy for this activity                   |
| `event_type`                                                        | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | The type of the time off event/activity                             |
| `event_description`                                                 | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | A description for the time off event/activity                       |
| `effective_time`                                                    | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | The datetime of the time off activity                               |
| `balance`                                                           | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | The time off balance at the time of the activity                    |
| `balance_change`                                                    | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | The amount the time off balance changed as a result of the activity |