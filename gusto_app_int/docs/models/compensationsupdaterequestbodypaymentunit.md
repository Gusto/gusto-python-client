# CompensationsUpdateRequestBodyPaymentUnit

The unit accompanying the compensation rate. If the employee is an owner, rate should be 'Paycheck'.

## Example Usage

```python
from gusto_app_integration.models import CompensationsUpdateRequestBodyPaymentUnit

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