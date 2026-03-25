# PaySchedulePreviewPayPeriod

A single pay period in a pay schedule preview, with check date, period boundaries, and payroll deadline.


## Fields

| Field                                                                               | Type                                                                                | Required                                                                            | Description                                                                         |
| ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- |
| `check_date`                                                                        | [datetime](https://docs.python.org/3/library/datetime.html#datetime-objects)        | :heavy_check_mark:                                                                  | The date employees will be paid (check date).                                       |
| `start_date`                                                                        | [datetime](https://docs.python.org/3/library/datetime.html#datetime-objects)        | :heavy_check_mark:                                                                  | The first day of the pay period.                                                    |
| `run_payroll_by`                                                                    | [datetime](https://docs.python.org/3/library/datetime.html#datetime-objects)        | :heavy_check_mark:                                                                  | The deadline by which payroll must be run for this period to be paid on check_date. |
| `end_date`                                                                          | [datetime](https://docs.python.org/3/library/datetime.html#datetime-objects)        | :heavy_check_mark:                                                                  | The last day of the pay period.                                                     |