# ContractorPaymentSummaryByDatesContractorPayments


## Fields

| Field                                                                   | Type                                                                    | Required                                                                | Description                                                             |
| ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- |
| `contractor_uuid`                                                       | *Optional[str]*                                                         | :heavy_minus_sign:                                                      | The UUID of the contractor.                                             |
| `check_date`                                                            | *Optional[str]*                                                         | :heavy_minus_sign:                                                      | The payment check date.                                                 |
| `reimbursement_total`                                                   | *Optional[str]*                                                         | :heavy_minus_sign:                                                      | The total reimbursements for the contractor within a given time period. |
| `wage_total`                                                            | *Optional[str]*                                                         | :heavy_minus_sign:                                                      | The total wages for the contractor within a given time period.          |
| `payments`                                                              | List[[models.ContractorPayment](../models/contractorpayment.md)]        | :heavy_minus_sign:                                                      | The contractor’s payments within a given time period.<br/>              |