# AmountType

The amount type of the deduction for the pay period. Only present for unprocessed payrolls.

## Example Usage

```python
from gusto_embedded_v_2026_06_15.models import AmountType

value = AmountType.FIXED

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name      | Value     |
| --------- | --------- |
| `FIXED`   | fixed     |
| `PERCENT` | percent   |