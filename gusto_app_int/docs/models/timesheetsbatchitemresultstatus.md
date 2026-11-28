# TimeSheetsBatchItemResultStatus

Status of the item.
- `pending`: The item is not processed yet.
- `success`: The time sheet was created or updated.
- `failed`: The time sheet was not created or updated. See `errors`.


## Example Usage

```python
from gusto_app_integration.models import TimeSheetsBatchItemResultStatus

value = TimeSheetsBatchItemResultStatus.PENDING
```


## Values

| Name      | Value     |
| --------- | --------- |
| `PENDING` | pending   |
| `SUCCESS` | success   |
| `FAILED`  | failed    |