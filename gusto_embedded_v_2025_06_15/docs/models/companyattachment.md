# CompanyAttachment

The company attachment


## Fields

| Field                                                     | Type                                                      | Required                                                  | Description                                               |
| --------------------------------------------------------- | --------------------------------------------------------- | --------------------------------------------------------- | --------------------------------------------------------- |
| `uuid`                                                    | *Optional[str]*                                           | :heavy_minus_sign:                                        | UUID of the company attachment                            |
| `name`                                                    | *Optional[str]*                                           | :heavy_minus_sign:                                        | name of the file uploaded                                 |
| `category`                                                | [Optional[models.Category]](../models/category.md)        | :heavy_minus_sign:                                        | The category of the company attachment                    |
| `upload_time`                                             | *Optional[str]*                                           | :heavy_minus_sign:                                        | The ISO 8601 timestamp of when an attachment was uploaded |