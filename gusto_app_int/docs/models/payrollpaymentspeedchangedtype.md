# PayrollPaymentSpeedChangedType

Only applicable when a payroll is moved to four day processing instead of fast ach.


## Fields

| Field                                            | Type                                             | Required                                         | Description                                      |
| ------------------------------------------------ | ------------------------------------------------ | ------------------------------------------------ | ------------------------------------------------ |
| `original_check_date`                            | *Optional[str]*                                  | :heavy_minus_sign:                               | Original check date when fast ach applies.       |
| `current_check_date`                             | *Optional[str]*                                  | :heavy_minus_sign:                               | Current check date.                              |
| `original_debit_date`                            | *Optional[str]*                                  | :heavy_minus_sign:                               | Original debit date when fast ach applies.       |
| `current_debit_date`                             | *Optional[str]*                                  | :heavy_minus_sign:                               | Current debit date.                              |
| `reason`                                         | *Optional[str]*                                  | :heavy_minus_sign:                               | The reason why the payroll is moved to four day. |