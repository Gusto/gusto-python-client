# BulkReportStatus

Overall batch status. `pending`/`processing` while in progress; once finished, `success` (all reports succeeded), `partial_success` (some succeeded, some failed), or `failed` (none succeeded).

## Example Usage

```python
from gusto_embedded_v_2026_06_15.models import BulkReportStatus

value = BulkReportStatus.PENDING

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name              | Value             |
| ----------------- | ----------------- |
| `PENDING`         | pending           |
| `PROCESSING`      | processing        |
| `SUCCESS`         | success           |
| `PARTIAL_SUCCESS` | partial_success   |
| `FAILED`          | failed            |