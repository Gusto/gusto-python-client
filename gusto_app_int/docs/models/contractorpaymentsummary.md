# ContractorPaymentSummary

The representation of the summary of contractor payments for a given company in a given time period.


## Fields

| Field                                                                                     | Type                                                                                      | Required                                                                                  | Description                                                                               |
| ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- |
| `total`                                                                                   | [Optional[models.Total]](../models/total.md)                                              | :heavy_minus_sign:                                                                        | The wage and reimbursement totals for all contractor payments within a given time period. |
| `contractor_payments`                                                                     | List[[models.ContractorPaymentsModel](../models/contractorpaymentsmodel.md)]              | :heavy_minus_sign:                                                                        | The individual contractor payments, within a given time period, grouped by contractor.    |