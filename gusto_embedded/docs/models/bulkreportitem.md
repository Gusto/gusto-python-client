# BulkReportItem

A single report inside a bulk batch. Required fields depend on `report_type`: `custom_report` requires `columns` and `file_type`; `general_ledger` requires `payroll_uuid` and `aggregation`.


## Supported Types

### `models.BulkReportCustomReportItem`

```python
value: models.BulkReportCustomReportItem = /* values here */
```

### `models.BulkReportGeneralLedgerItem`

```python
value: models.BulkReportGeneralLedgerItem = /* values here */
```

