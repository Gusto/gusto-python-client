# BulkReportStatus

Overall batch status. `pending`/`processing` while in progress; once finished, `success` (all reports succeeded), `partial_success` (some succeeded, some failed), or `failed` (none succeeded).

## Example Usage

```python
from gusto_embedded.models import BulkReportStatus

value = BulkReportStatus.PENDING
```


## Values

| Name              | Value             |
| ----------------- | ----------------- |
| `PENDING`         | pending           |
| `PROCESSING`      | processing        |
| `SUCCESS`         | success           |
| `PARTIAL_SUCCESS` | partial_success   |
| `FAILED`          | failed            |