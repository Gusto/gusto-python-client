# PrimarySignatory

The primary signatory of the company.


## Fields

| Field                                                                  | Type                                                                   | Required                                                               | Description                                                            |
| ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| `uuid`                                                                 | *Optional[str]*                                                        | :heavy_minus_sign:                                                     | The UUID of the company's primary signatory.                           |
| `first_name`                                                           | *Optional[str]*                                                        | :heavy_minus_sign:                                                     | The company's primary signatory's first name.                          |
| `middle_initial`                                                       | *OptionalNullable[str]*                                                | :heavy_minus_sign:                                                     | The company's primary signatory's middle initial.                      |
| `last_name`                                                            | *Optional[str]*                                                        | :heavy_minus_sign:                                                     | The company's primary signatory's last name.                           |
| `phone`                                                                | *Optional[str]*                                                        | :heavy_minus_sign:                                                     | The company's primary signatory's phone number.                        |
| `email`                                                                | *Optional[str]*                                                        | :heavy_minus_sign:                                                     | The company's primary signatory's email address.                       |
| `home_address`                                                         | [Optional[models.CompanyHomeAddress]](../models/companyhomeaddress.md) | :heavy_minus_sign:                                                     | The company's primary signatory's home address.                        |