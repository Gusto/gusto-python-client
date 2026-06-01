# PayrollDigestResultsTotals

Pay totals. `null` when the payroll has not been calculated, or when the calculation is stale (the partner edited hours/earnings after the last calculation).


## Fields

| Field                                                                          | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `total_debit_amount`                                                           | *Optional[str]*                                                                | :heavy_minus_sign:                                                             | Total amount debited from the company bank account (string-formatted decimal). |
| `net_pay`                                                                      | *Optional[str]*                                                                | :heavy_minus_sign:                                                             | Total net pay across all employees on this payroll (string-formatted decimal). |
| `total_employer_cost`                                                          | *Optional[str]*                                                                | :heavy_minus_sign:                                                             | Total employer cost including taxes and benefits (string-formatted decimal).   |