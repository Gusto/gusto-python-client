# PaySchedulePreview

Preview of pay schedule dates for the next 18 months. Use this to show partners expected pay dates, pay period boundaries, and payroll deadlines before they create or change a pay schedule. See [Preview pay schedule dates](https://docs.gusto.com/embedded-payroll/reference/get-v1-companies-company_id-pay_schedules-preview) for usage.

- **pay_periods**: One entry per pay period in the range; each includes check_date, start_date, end_date, and run_payroll_by.
- **holidays**: Observed bank holidays (ISO date strings) that may affect payroll timing.



## Fields

| Field                                                                                                                          | Type                                                                                                                           | Required                                                                                                                       | Description                                                                                                                    |
| ------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------ |
| `pay_periods`                                                                                                                  | List[[models.PaySchedulePreviewPayPeriod](../models/payschedulepreviewpayperiod.md)]                                           | :heavy_minus_sign:                                                                                                             | A list of pay periods for the previewed pay schedule (default range is 18 months from today, or up to end_date when provided). |
| `holidays`                                                                                                                     | List[[datetime](https://docs.python.org/3/library/datetime.html#datetime-objects)]                                             | :heavy_minus_sign:                                                                                                             | A list of dates for bank closures (ISO date strings); may affect payroll processing.                                           |