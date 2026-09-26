# BulkReportItemResult

A single report's outcome.


## Fields

| Field                                                                                | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `report_type`                                                                        | [models.BulkReportItemResultReportType](../models/bulkreportitemresultreporttype.md) | :heavy_check_mark:                                                                   | Which report this entry refers to.                                                   |
| `file_type`                                                                          | *str*                                                                                | :heavy_check_mark:                                                                   | The report's output file type.                                                       |
| `status`                                                                             | [models.BulkReportItemResultStatus](../models/bulkreportitemresultstatus.md)         | :heavy_check_mark:                                                                   | The terminal state for this individual report.                                       |
| `error`                                                                              | *Nullable[str]*                                                                      | :heavy_check_mark:                                                                   | A user-facing error message when status is `failed`. Null on success.                |