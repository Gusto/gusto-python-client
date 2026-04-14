# PayrollCheck

Example response


## Fields

| Field                                                                              | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `payroll_uuid`                                                                     | *Optional[str]*                                                                    | :heavy_minus_sign:                                                                 | A unique identifier of the payroll.                                                |
| `printing_format`                                                                  | *Optional[str]*                                                                    | :heavy_minus_sign:                                                                 | The format the checks will be printed.                                             |
| `starting_check_number`                                                            | *Optional[str]*                                                                    | :heavy_minus_sign:                                                                 | The starting check number for the checks being printed.                            |
| `request_uuid`                                                                     | *Optional[str]*                                                                    | :heavy_minus_sign:                                                                 | A unique identifier of the Generated Document request                              |
| `status`                                                                           | *Optional[str]*                                                                    | :heavy_minus_sign:                                                                 | Current status of the Generated Document                                           |
| `employee_check_number_mapping`                                                    | List[[models.EmployeeCheckNumberMapping](../models/employeechecknumbermapping.md)] | :heavy_minus_sign:                                                                 | An array of mapping employee uuids to their check numbers                          |