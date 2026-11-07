# TimeSheetsBatchItemResultStatus

Status of the item.
- `pending`: The item is not processed yet.
- `success`: The time sheet was created or updated.
- `failed`: The time sheet was not created or updated. See `errors`.


## Example Usage

```python
from gusto_app_integration_v_2026_06_15.models import TimeSheetsBatchItemResultStatus

value = TimeSheetsBatchItemResultStatus.PENDING

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name      | Value     |
| --------- | --------- |
| `PENDING` | pending   |
| `SUCCESS` | success   |
| `FAILED`  | failed    |