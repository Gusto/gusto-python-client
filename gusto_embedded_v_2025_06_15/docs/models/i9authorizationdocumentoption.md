# I9AuthorizationDocumentOption

An employee's I-9 verification document option based on the authorization status


## Fields

| Field                                                                             | Type                                                                              | Required                                                                          | Description                                                                       |
| --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- |
| `section`                                                                         | [models.Section](../models/section.md)                                            | :heavy_check_mark:                                                                | The document option's section in the list of acceptable documents on the Form I-9 |
| `description`                                                                     | *str*                                                                             | :heavy_check_mark:                                                                | The document option's description                                                 |
| `document_type`                                                                   | *str*                                                                             | :heavy_check_mark:                                                                | The document option's document type                                               |
| `document_title`                                                                  | List[*str*]                                                                       | :heavy_check_mark:                                                                | The document option's document titles                                             |
| `common_choice`                                                                   | *bool*                                                                            | :heavy_check_mark:                                                                | Whether the document is a common choice for I-9 verification                      |