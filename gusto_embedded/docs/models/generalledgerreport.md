# GeneralLedgerReport

Successful response for general ledger report generation


## Fields

| Field                                                             | Type                                                              | Required                                                          | Description                                                       |
| ----------------------------------------------------------------- | ----------------------------------------------------------------- | ----------------------------------------------------------------- | ----------------------------------------------------------------- |
| `payroll_uuid`                                                    | *Optional[str]*                                                   | :heavy_minus_sign:                                                | The UUID of the payroll record for which the report was generated |
| `aggregation`                                                     | [Optional[models.Aggregation]](../models/aggregation.md)          | :heavy_minus_sign:                                                | The breakdown level used for the report                           |
| `request_uuid`                                                    | *Optional[str]*                                                   | :heavy_minus_sign:                                                | UUID to use for polling the report status                         |