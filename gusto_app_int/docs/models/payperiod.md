# PayPeriod

The representation of a pay period.


## Fields

| Field                                                                    | Type                                                                     | Required                                                                 | Description                                                              |
| ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ |
| `start_date`                                                             | *Optional[str]*                                                          | :heavy_minus_sign:                                                       | The start date, inclusive, of the pay period.                            |
| `end_date`                                                               | *Optional[str]*                                                          | :heavy_minus_sign:                                                       | The end date, inclusive, of the pay period.                              |
| `pay_schedule_uuid`                                                      | *Optional[str]*                                                          | :heavy_minus_sign:                                                       | A unique identifier of the pay schedule to which the pay period belongs. |
| `payroll`                                                                | [Optional[models.PayPeriodPayroll]](../models/payperiodpayroll.md)       | :heavy_minus_sign:                                                       | Information about the payroll for the pay period.                        |