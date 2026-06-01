# AmountType

The amount type of the deduction for the pay period. Only present for unprocessed payrolls.

## Example Usage

```python
from gusto_embedded.models import AmountType

value = AmountType.FIXED
```


## Values

| Name      | Value     |
| --------- | --------- |
| `FIXED`   | fixed     |
| `PERCENT` | percent   |