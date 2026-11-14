# TimeSheetsBatchCreateBodyStatus

Status of the time sheet. When `batch_action` is `create`, one of `approved` or `pending`. When `batch_action` is `update`, one of `approved`, `pending` or `rejected`.

## Example Usage

```python
from gusto_app_integration.models import TimeSheetsBatchCreateBodyStatus

value = TimeSheetsBatchCreateBodyStatus.APPROVED
```


## Values

| Name       | Value      |
| ---------- | ---------- |
| `APPROVED` | approved   |
| `PENDING`  | pending    |
| `REJECTED` | rejected   |