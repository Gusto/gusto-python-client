# Report

Example response


## Fields

| Field                                                                                 | Type                                                                                  | Required                                                                              | Description                                                                           |
| ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| `request_uuid`                                                                        | *Optional[str]*                                                                       | :heavy_minus_sign:                                                                    | A unique identifier of the report request                                             |
| `status`                                                                              | *Optional[str]*                                                                       | :heavy_minus_sign:                                                                    | Current status of the report, possible values are 'succeeded', 'pending', or 'failed' |
| `report_urls`                                                                         | List[*str*]                                                                           | :heavy_minus_sign:                                                                    | The array of urls to access the report                                                |