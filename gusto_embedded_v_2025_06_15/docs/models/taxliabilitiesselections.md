# TaxLiabilitiesSelections

Example response


## Fields

| Field                                                                | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `tax_id`                                                             | *Optional[int]*                                                      | :heavy_minus_sign:                                                   | The ID of the tax.                                                   |
| `tax_name`                                                           | *Optional[str]*                                                      | :heavy_minus_sign:                                                   | The name of the tax.                                                 |
| `last_unpaid_external_payroll_uuid`                                  | *OptionalNullable[str]*                                              | :heavy_minus_sign:                                                   | The UUID of last unpaid external payroll.                            |
| `possible_liabilities`                                               | List[[models.PossibleLiabilities](../models/possibleliabilities.md)] | :heavy_minus_sign:                                                   | Possible tax liabilities selections.                                 |