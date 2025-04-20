# I9AuthorizationDocument

An employee's I-9 verification document


## Fields

| Field                                     | Type                                      | Required                                  | Description                               |
| ----------------------------------------- | ----------------------------------------- | ----------------------------------------- | ----------------------------------------- |
| `uuid`                                    | *str*                                     | :heavy_check_mark:                        | The UUID of the I-9 verification document |
| `document_type`                           | *str*                                     | :heavy_check_mark:                        | The document's document type              |
| `document_title`                          | *str*                                     | :heavy_check_mark:                        | The document's document title             |
| `expiration_date`                         | *Optional[str]*                           | :heavy_minus_sign:                        | The document's expiration date            |
| `issuing_authority`                       | *str*                                     | :heavy_check_mark:                        | The document's issuing authority          |