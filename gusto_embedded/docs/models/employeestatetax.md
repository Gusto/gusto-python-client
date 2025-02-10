# EmployeeStateTax

Example response


## Fields

| Field                                                                          | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `employee_uuid`                                                                | *str*                                                                          | :heavy_check_mark:                                                             | The employee's uuid                                                            |
| `state`                                                                        | *str*                                                                          | :heavy_check_mark:                                                             | Two letter US state abbreviation                                               |
| `questions`                                                                    | List[[models.EmployeeStateTaxQuestion](../models/employeestatetaxquestion.md)] | :heavy_check_mark:                                                             | N/A                                                                            |
| `file_new_hire_report`                                                         | *OptionalNullable[bool]*                                                       | :heavy_minus_sign:                                                             | N/A                                                                            |
| `is_work_state`                                                                | *Optional[bool]*                                                               | :heavy_minus_sign:                                                             | N/A                                                                            |