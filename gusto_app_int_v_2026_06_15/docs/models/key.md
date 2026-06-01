# Key

A required attribute when creating a garnishment for this state agency. The current values are listed as an enum; though unlikely, values could be added if state agency requirements change in the future.

## Example Usage

```python
from gusto_app_integration_v_2026_06_15.models import Key

value = Key.CASE_NUMBER

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name                | Value               |
| ------------------- | ------------------- |
| `CASE_NUMBER`       | case_number         |
| `ORDER_NUMBER`      | order_number        |
| `REMITTANCE_NUMBER` | remittance_number   |