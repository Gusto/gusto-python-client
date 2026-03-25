# PayrollCalculateAccruingTimeOffHoursRequest

Request body for calculating accruing time off hours


## Fields

| Field                                           | Type                                            | Required                                        | Description                                     |
| ----------------------------------------------- | ----------------------------------------------- | ----------------------------------------------- | ----------------------------------------------- |
| `regular_hours_worked`                          | *OptionalNullable[str]*                         | :heavy_minus_sign:                              | Regular hours worked in this pay period         |
| `overtime_hours_worked`                         | *OptionalNullable[str]*                         | :heavy_minus_sign:                              | Overtime hours worked in this pay period        |
| `double_overtime_hours_worked`                  | *OptionalNullable[str]*                         | :heavy_minus_sign:                              | Double overtime hours worked in this pay period |
| `pto_hours_used`                                | *OptionalNullable[str]*                         | :heavy_minus_sign:                              | Paid time off hours used in this pay period     |
| `sick_hours_used`                               | *OptionalNullable[str]*                         | :heavy_minus_sign:                              | Sick hours used in this pay period              |