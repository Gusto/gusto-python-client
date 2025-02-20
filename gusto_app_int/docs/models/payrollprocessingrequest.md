# PayrollProcessingRequest


## Fields

| Field                                                                                          | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `status`                                                                                       | [Optional[models.PayrollProcessingRequestStatus]](../models/payrollprocessingrequeststatus.md) | :heavy_minus_sign:                                                                             | The status of the payroll processing request                                                   |
| `errors`                                                                                       | List[[models.EntityErrorObject](../models/entityerrorobject.md)]                               | :heavy_minus_sign:                                                                             | Errors that occurred during async payroll processing                                           |