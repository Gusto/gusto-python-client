# TaxRequirementMetadataOptions


## Fields

| Field                                                                          | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `label`                                                                        | *str*                                                                          | :heavy_check_mark:                                                             | A customer facing label for the answer                                         |
| `value`                                                                        | [models.TaxRequirementMetadataValue](../models/taxrequirementmetadatavalue.md) | :heavy_check_mark:                                                             | The actual value to be submitted                                               |
| `short_label`                                                                  | *Optional[str]*                                                                | :heavy_minus_sign:                                                             | A less verbose label that may sometimes be available                           |