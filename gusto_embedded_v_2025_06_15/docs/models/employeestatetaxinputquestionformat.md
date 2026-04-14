# EmployeeStateTaxInputQuestionFormat


## Fields

| Field                                                                 | Type                                                                  | Required                                                              | Description                                                           |
| --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- |
| `type`                                                                | *str*                                                                 | :heavy_check_mark:                                                    | Describes the type of question - Text, Number, Select, Currency, Date |
| `options`                                                             | List[[models.Options](../models/options.md)]                          | :heavy_minus_sign:                                                    | For "Select" type questions, the allowed values and display labels.   |