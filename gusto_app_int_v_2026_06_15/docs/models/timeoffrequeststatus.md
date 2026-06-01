# TimeOffRequestStatus

The status of the time off request.

## Example Usage

```python
from gusto_app_integration_v_2026_06_15.models import TimeOffRequestStatus

value = TimeOffRequestStatus.PENDING

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name       | Value      |
| ---------- | ---------- |
| `PENDING`  | pending    |
| `APPROVED` | approved   |
| `DECLINED` | declined   |
| `CONSUMED` | consumed   |