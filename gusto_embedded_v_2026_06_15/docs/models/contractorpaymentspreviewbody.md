# ContractorPaymentsPreviewBody

Request body for previewing contractor payments. The expected debit date for the payments is calculated from the provided check date and the company's ACH speed.


## Fields

| Field                                                                                                                        | Type                                                                                                                         | Required                                                                                                                     | Description                                                                                                                  |
| ---------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| `contractor_payments`                                                                                                        | List[[models.ContractorPaymentsPreviewBodyContractorPayments](../models/contractorpaymentspreviewbodycontractorpayments.md)] | :heavy_check_mark:                                                                                                           | A list of contractor payments to preview.                                                                                    |