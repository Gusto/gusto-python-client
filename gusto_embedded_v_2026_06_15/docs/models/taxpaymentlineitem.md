# TaxPaymentLineItem

A single payroll tax liability rolled up into a tax payment


## Fields

| Field                                                     | Type                                                      | Required                                                  | Description                                               |
| --------------------------------------------------------- | --------------------------------------------------------- | --------------------------------------------------------- | --------------------------------------------------------- |
| `payroll_uuid`                                            | *str*                                                     | :heavy_check_mark:                                        | Unique identifier of the payroll this liability came from |
| `unique_tax_id`                                           | *str*                                                     | :heavy_check_mark:                                        | Unique identifier of the tax type this liability is for   |
| `amount`                                                  | *str*                                                     | :heavy_check_mark:                                        | The amount of this liability included in the tax payment  |