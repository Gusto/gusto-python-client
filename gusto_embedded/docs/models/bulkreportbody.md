# BulkReportBody

Each `batch` item is a `custom_report` or a `general_ledger` report.


## Fields

| Field                                                                                                        | Type                                                                                                         | Required                                                                                                     | Description                                                                                                  |
| ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ |
| `batch`                                                                                                      | List[[models.BulkReportItem](../models/bulkreportitem.md)]                                                   | :heavy_check_mark:                                                                                           | One report per item. Up to 25 items per batch, across any combination of companies the partner is mapped to. |