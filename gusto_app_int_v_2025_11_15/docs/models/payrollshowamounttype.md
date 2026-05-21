# PayrollShowAmountType

The amount type of the deduction for the pay period. Only present for unprocessed payrolls.

## Example Usage

```python
from gusto_app_integration_v_2025_11_15.models import PayrollShowAmountType

value = PayrollShowAmountType.FIXED

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name      | Value     |
| --------- | --------- |
| `FIXED`   | fixed     |
| `PERCENT` | percent   |