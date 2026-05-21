# ContractorPaymentGroupPartnerDisbursements

Partner disbursements for a contractor payment group


## Fields

| Field                                                    | Type                                                     | Required                                                 | Description                                              |
| -------------------------------------------------------- | -------------------------------------------------------- | -------------------------------------------------------- | -------------------------------------------------------- |
| `contractor_payment_group_uuid`                          | *Optional[str]*                                          | :heavy_minus_sign:                                       | The UUID of the contractor payment group                 |
| `disbursements`                                          | List[[models.Disbursements](../models/disbursements.md)] | :heavy_minus_sign:                                       | List of disbursements for the contractor payment group   |