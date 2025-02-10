# PayrollReversal

Example response


## Fields

| Field                                                    | Type                                                     | Required                                                 | Description                                              |
| -------------------------------------------------------- | -------------------------------------------------------- | -------------------------------------------------------- | -------------------------------------------------------- |
| `reversed_payroll_uuid`                                  | *Optional[str]*                                          | :heavy_minus_sign:                                       | The UUID for the payroll run being reversed.             |
| `reversal_payroll_uuid`                                  | *Optional[str]*                                          | :heavy_minus_sign:                                       | The UUID of the payroll where the reversal was applied.  |
| `reason`                                                 | *Optional[str]*                                          | :heavy_minus_sign:                                       | A reason provided by the admin who created the reversal. |
| `approved_at`                                            | *OptionalNullable[str]*                                  | :heavy_minus_sign:                                       | Timestamp of when the reversal was approved.             |
| `category`                                               | *Optional[str]*                                          | :heavy_minus_sign:                                       | Category chosen by the admin who requested the reversal. |
| `reversed_employee_uuids`                                | List[*str*]                                              | :heavy_minus_sign:                                       | Array of affected employee UUIDs.                        |