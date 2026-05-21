# DateFilterBy

Specifies which date field to use when filtering payrolls with start_date and end_date. This field applies only to regular processed payrolls and defaults to pay period if not provided.

## Example Usage

```python
from gusto_app_integration_v_2025_11_15.models import DateFilterBy

value = DateFilterBy.CHECK_DATE
```


## Values

| Name         | Value        |
| ------------ | ------------ |
| `CHECK_DATE` | check_date   |