# PutV1HistoricalEmployeesHomeAddress

Residential address on file for tax withholding and compliance mail.


## Fields

| Field                                                   | Type                                                    | Required                                                | Description                                             | Example                                                 |
| ------------------------------------------------------- | ------------------------------------------------------- | ------------------------------------------------------- | ------------------------------------------------------- | ------------------------------------------------------- |
| `street_1`                                              | *str*                                                   | :heavy_check_mark:                                      | Street address line 1.                                  | 55 Mission St                                           |
| `street_2`                                              | *OptionalNullable[str]*                                 | :heavy_minus_sign:                                      | Apartment, suite, unit, or building (optional).         | Floor 3                                                 |
| `city`                                                  | *str*                                                   | :heavy_check_mark:                                      | City.                                                   | San Francisco                                           |
| `state`                                                 | *str*                                                   | :heavy_check_mark:                                      | Two-letter U.S. state or territory postal abbreviation. | CA                                                      |
| `zip_code`                                              | *str*                                                   | :heavy_check_mark:                                      | ZIP or ZIP+4.                                           | 94105                                                   |