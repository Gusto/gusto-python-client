# CompensationsRequestBodyPaymentUnit

The unit accompanying the compensation rate. If the employee is an owner, rate should be 'Paycheck'.

## Example Usage

```python
from gusto_app_integration_v_2025_11_15.models import CompensationsRequestBodyPaymentUnit

value = CompensationsRequestBodyPaymentUnit.HOUR
```


## Values

| Name       | Value      |
| ---------- | ---------- |
| `HOUR`     | Hour       |
| `WEEK`     | Week       |
| `MONTH`    | Month      |
| `YEAR`     | Year       |
| `PAYCHECK` | Paycheck   |