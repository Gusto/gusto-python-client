# ExternalPayrollTaxSuggestions

The representation of an external payroll with minimal information.


## Fields

| Field                                                      | Type                                                       | Required                                                   | Description                                                |
| ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- |
| `employee_uuid`                                            | *Optional[str]*                                            | :heavy_minus_sign:                                         | The UUID of the employee.                                  |
| `tax_suggestions`                                          | List[[models.TaxSuggestions](../models/taxsuggestions.md)] | :heavy_minus_sign:                                         | Possible tax liabilities selections.                       |