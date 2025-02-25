# GetV1TokenInfoResponseBody

Example response


## Fields

| Field                                                        | Type                                                         | Required                                                     | Description                                                  |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| `scope`                                                      | *str*                                                        | :heavy_check_mark:                                           | Space delimited string of accessible scopes.                 |
| `resource`                                                   | [Nullable[models.Resource]](../models/resource.md)           | :heavy_check_mark:                                           | Information about the token resource.                        |
| `resource_owner`                                             | [Nullable[models.ResourceOwner]](../models/resourceowner.md) | :heavy_check_mark:                                           | Information about the token owner                            |