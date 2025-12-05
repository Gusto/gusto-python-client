# Admin

The representation of an admin user in Gusto.


## Fields

| Field                                      | Type                                       | Required                                   | Description                                |
| ------------------------------------------ | ------------------------------------------ | ------------------------------------------ | ------------------------------------------ |
| `uuid`                                     | *str*                                      | :heavy_check_mark:                         | The unique id of the admin.                |
| `email`                                    | *Optional[str]*                            | :heavy_minus_sign:                         | The email of the admin for Gusto's system. |
| `first_name`                               | *Optional[str]*                            | :heavy_minus_sign:                         | The first name of the admin.               |
| `last_name`                                | *Optional[str]*                            | :heavy_minus_sign:                         | The last name of the admin.                |