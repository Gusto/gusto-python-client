# RefreshAccessTokenRequestBody


## Fields

| Field                                                        | Type                                                         | Required                                                     | Description                                                  |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| `client_id`                                                  | *str*                                                        | :heavy_check_mark:                                           | Your client id                                               |
| `client_secret`                                              | *str*                                                        | :heavy_check_mark:                                           | Your client secret                                           |
| `redirect_uri`                                               | *Optional[str]*                                              | :heavy_minus_sign:                                           | The redirect URI you set up via the Developer Portal         |
| `refresh_token`                                              | *str*                                                        | :heavy_check_mark:                                           | The `refresh_token` being exchanged for an access token code |
| `grant_type`                                                 | *str*                                                        | :heavy_check_mark:                                           | this should be the literal string 'refresh_token'            |