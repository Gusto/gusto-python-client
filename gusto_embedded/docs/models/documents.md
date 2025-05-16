# Documents


## Fields

| Field                                                | Type                                                 | Required                                             | Description                                          |
| ---------------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------- |
| `document_type`                                      | *str*                                                | :heavy_check_mark:                                   | The document type                                    |
| `document_title`                                     | *str*                                                | :heavy_check_mark:                                   | The document title associated with the document type |
| `document_number`                                    | *Optional[str]*                                      | :heavy_minus_sign:                                   | The document's document number                       |
| `expiration_date`                                    | *Optional[str]*                                      | :heavy_minus_sign:                                   | The document's expiration date                       |
| `issuing_authority`                                  | *str*                                                | :heavy_check_mark:                                   | The document's issuing authority                     |