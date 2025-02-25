# ContractorPaymentsModel


## Fields

| Field                                                                   | Type                                                                    | Required                                                                | Description                                                             |
| ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- |
| `contractor_uuid`                                                       | *Optional[float]*                                                       | :heavy_minus_sign:                                                      | The UUID of the contractor.                                             |
| `reimbursement_total`                                                   | *Optional[str]*                                                         | :heavy_minus_sign:                                                      | The total reimbursements for the contractor within a given time period. |
| `wage_total`                                                            | *Optional[str]*                                                         | :heavy_minus_sign:                                                      | The total wages for the contractor within a given time period.          |
| `payments`                                                              | List[[models.ContractorPayment](../models/contractorpayment.md)]        | :heavy_minus_sign:                                                      | The contractor’s payments within a given time period.<br/>              |