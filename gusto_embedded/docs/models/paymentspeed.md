# PaymentSpeed

Payment speed. READ-ONLY.
- `1-day`: Next-day ACH (only for partners that opt in).
- `2-day`: Two-day ACH.
- `4-day`: Standard ACH.


## Example Usage

```python
from gusto_embedded.models import PaymentSpeed

value = PaymentSpeed.ONE_MINUS_DAY
```


## Values

| Name             | Value            |
| ---------------- | ---------------- |
| `ONE_MINUS_DAY`  | 1-day            |
| `TWO_MINUS_DAY`  | 2-day            |
| `FOUR_MINUS_DAY` | 4-day            |