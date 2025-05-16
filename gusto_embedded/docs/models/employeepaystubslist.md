# EmployeePayStubsList

The representation of an employee pay stub information.


## Fields

| Field                                                             | Type                                                              | Required                                                          | Description                                                       |
| ----------------------------------------------------------------- | ----------------------------------------------------------------- | ----------------------------------------------------------------- | ----------------------------------------------------------------- |
| `uuid`                                                            | *str*                                                             | :heavy_check_mark:                                                | The UUID of the employee pay stub.                                |
| `check_date`                                                      | *Optional[str]*                                                   | :heavy_minus_sign:                                                | The check date of the pay stub.                                   |
| `gross_pay`                                                       | *Optional[str]*                                                   | :heavy_minus_sign:                                                | The gross pay amount for the pay stub.                            |
| `net_pay`                                                         | *Optional[str]*                                                   | :heavy_minus_sign:                                                | The net pay amount for the pay stub.                              |
| `payroll_uuid`                                                    | *Optional[str]*                                                   | :heavy_minus_sign:                                                | A unique identifier of the payroll to which the pay stub belongs. |
| `check_amount`                                                    | *Optional[str]*                                                   | :heavy_minus_sign:                                                | The check amount for the pay stub.                                |