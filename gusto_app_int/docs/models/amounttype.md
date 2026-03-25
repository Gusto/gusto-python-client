# AmountType

The amount type of the deduction for the pay period. Only present for calculated or processed payrolls.

## Example Usage

```python
from gusto_app_integration.models import AmountType

value = AmountType.FIXED
```


## Values

| Name      | Value     |
| --------- | --------- |
| `FIXED`   | fixed     |
| `PERCENT` | percent   |