# PaymentUnit

The unit accompanying the compensation rate. If the employee is an owner, rate should be 'Paycheck'.

## Example Usage

```python
from gusto_embedded.models import PaymentUnit

value = PaymentUnit.HOUR
```


## Values

| Name       | Value      |
| ---------- | ---------- |
| `HOUR`     | Hour       |
| `WEEK`     | Week       |
| `MONTH`    | Month      |
| `YEAR`     | Year       |
| `PAYCHECK` | Paycheck   |