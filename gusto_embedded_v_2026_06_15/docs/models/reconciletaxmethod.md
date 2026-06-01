# ReconcileTaxMethod

How Gusto will handle taxes already collected.

## Example Usage

```python
from gusto_embedded_v_2026_06_15.models import ReconcileTaxMethod

value = ReconcileTaxMethod.PAY_TAXES

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name           | Value          |
| -------------- | -------------- |
| `PAY_TAXES`    | pay_taxes      |
| `REFUND_TAXES` | refund_taxes   |