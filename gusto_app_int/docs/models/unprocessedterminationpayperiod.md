# UnprocessedTerminationPayPeriod

The representation of an unprocessed termination pay period.


## Fields

| Field                                                                    | Type                                                                     | Required                                                                 | Description                                                              |
| ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ |
| `start_date`                                                             | *Optional[str]*                                                          | :heavy_minus_sign:                                                       | The start date of the pay period.                                        |
| `end_date`                                                               | *Optional[str]*                                                          | :heavy_minus_sign:                                                       | The end date of the pay period.                                          |
| `check_date`                                                             | *Optional[str]*                                                          | :heavy_minus_sign:                                                       | The check date of the pay period.                                        |
| `debit_date`                                                             | *Optional[str]*                                                          | :heavy_minus_sign:                                                       | The debit date of the pay period.                                        |
| `employee_name`                                                          | *Optional[str]*                                                          | :heavy_minus_sign:                                                       | The full name of the employee.                                           |
| `employee_uuid`                                                          | *Optional[str]*                                                          | :heavy_minus_sign:                                                       | A unique identifier of the employee.                                     |
| `pay_schedule_uuid`                                                      | *Optional[str]*                                                          | :heavy_minus_sign:                                                       | A unique identifier of the pay schedule to which the pay period belongs. |