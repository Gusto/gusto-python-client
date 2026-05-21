# ExternalPayrollCreateRequest

The request body for creating an external payroll.


## Fields

| Field                                                                        | Type                                                                         | Required                                                                     | Description                                                                  | Example                                                                      |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `check_date`                                                                 | [datetime](https://docs.python.org/3/library/datetime.html#datetime-objects) | :heavy_check_mark:                                                           | The check date of the external payroll.                                      | 2022-06-03                                                                   |
| `payment_period_start_date`                                                  | [datetime](https://docs.python.org/3/library/datetime.html#datetime-objects) | :heavy_check_mark:                                                           | The start date of the external payroll payment period.                       | 2022-05-15                                                                   |
| `payment_period_end_date`                                                    | [datetime](https://docs.python.org/3/library/datetime.html#datetime-objects) | :heavy_check_mark:                                                           | The end date of the external payroll payment period.                         | 2022-05-30                                                                   |