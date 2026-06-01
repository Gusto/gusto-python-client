# CompensationsUpdateRequestBodyPaymentUnit

The unit accompanying the compensation rate. If the employee is an owner, rate should be 'Paycheck'.

## Example Usage

```python
from gusto_embedded_v_2026_06_15.models import CompensationsUpdateRequestBodyPaymentUnit

value = CompensationsUpdateRequestBodyPaymentUnit.HOUR
```


## Values

| Name       | Value      |
| ---------- | ---------- |
| `HOUR`     | Hour       |
| `WEEK`     | Week       |
| `MONTH`    | Month      |
| `YEAR`     | Year       |
| `PAYCHECK` | Paycheck   |