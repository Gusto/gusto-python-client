# TimeSheetsBatchCreateBodyEntityType

Type of entity associated with the time sheet. Required when `batch_action` is `create`. Ignored when `batch_action` is `update`.

## Example Usage

```python
from gusto_app_integration.models import TimeSheetsBatchCreateBodyEntityType

value = TimeSheetsBatchCreateBodyEntityType.EMPLOYEE
```


## Values

| Name         | Value        |
| ------------ | ------------ |
| `EMPLOYEE`   | Employee     |
| `CONTRACTOR` | Contractor   |