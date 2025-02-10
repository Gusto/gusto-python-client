# PostV1CompaniesCompanyIDLocationsRequestBody

Create a company location.


## Fields

| Field                                                      | Type                                                       | Required                                                   | Description                                                |
| ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- |
| `phone_number`                                             | *str*                                                      | :heavy_check_mark:                                         | N/A                                                        |
| `street_1`                                                 | *str*                                                      | :heavy_check_mark:                                         | N/A                                                        |
| `city`                                                     | *str*                                                      | :heavy_check_mark:                                         | N/A                                                        |
| `state`                                                    | *str*                                                      | :heavy_check_mark:                                         | N/A                                                        |
| `zip`                                                      | *str*                                                      | :heavy_check_mark:                                         | N/A                                                        |
| `street_2`                                                 | *OptionalNullable[str]*                                    | :heavy_minus_sign:                                         | N/A                                                        |
| `mailing_address`                                          | *Optional[bool]*                                           | :heavy_minus_sign:                                         | Specify if this location is the company's mailing address. |
| `filing_address`                                           | *Optional[bool]*                                           | :heavy_minus_sign:                                         | Specify if this location is the company's filing address.  |