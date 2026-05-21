# PayrollPartnerDisbursements

Partner disbursements for a payroll


## Fields

| Field                                                                                                          | Type                                                                                                           | Required                                                                                                       | Description                                                                                                    |
| -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| `payroll_uuid`                                                                                                 | *Optional[str]*                                                                                                | :heavy_minus_sign:                                                                                             | The UUID of the payroll                                                                                        |
| `disbursements`                                                                                                | List[[models.PayrollPartnerDisbursementsDisbursements](../models/payrollpartnerdisbursementsdisbursements.md)] | :heavy_minus_sign:                                                                                             | List of disbursements for the payroll                                                                          |