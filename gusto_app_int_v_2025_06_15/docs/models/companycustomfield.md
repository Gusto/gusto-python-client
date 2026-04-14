# CompanyCustomField

A custom field on a company


## Fields

| Field                                                          | Type                                                           | Required                                                       | Description                                                    |
| -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- |
| `uuid`                                                         | *str*                                                          | :heavy_check_mark:                                             | UUID of the company custom field                               |
| `name`                                                         | *str*                                                          | :heavy_check_mark:                                             | Name of the company custom field                               |
| `type`                                                         | [models.CustomFieldType](../models/customfieldtype.md)         | :heavy_check_mark:                                             | Input type for the custom field.                               |
| `description`                                                  | *Optional[str]*                                                | :heavy_minus_sign:                                             | Description of the company custom field                        |
| `selection_options`                                            | List[*str*]                                                    | :heavy_minus_sign:                                             | An array of options for fields of type radio. Otherwise, null. |