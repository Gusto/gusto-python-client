# PayrollTypes

Comma-separated list of payroll types to include (regular, transition). Defaults to regular only.

## Example Usage

```python
from gusto_embedded.models import PayrollTypes

value = PayrollTypes.REGULAR
```


## Values

| Name                 | Value                |
| -------------------- | -------------------- |
| `REGULAR`            | regular              |
| `TRANSITION`         | transition           |
| `REGULAR_TRANSITION` | regular,transition   |