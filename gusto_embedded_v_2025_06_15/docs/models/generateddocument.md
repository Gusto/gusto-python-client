# GeneratedDocument

Example response


## Fields

| Field                                                                            | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `request_uuid`                                                                   | *Optional[str]*                                                                  | :heavy_minus_sign:                                                               | A unique identifier of the Generated Document request                            |
| `status`                                                                         | [Optional[models.GeneratedDocumentStatus]](../models/generateddocumentstatus.md) | :heavy_minus_sign:                                                               | Current status of the Generated Document                                         |
| `document_urls`                                                                  | List[*str*]                                                                      | :heavy_minus_sign:                                                               | The array of urls to access the documents.                                       |