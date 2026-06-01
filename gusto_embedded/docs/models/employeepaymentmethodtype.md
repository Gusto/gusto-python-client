# EmployeePaymentMethodType

The payment method type. If type is Check, then `split_by` and `splits` do not need to be populated. If type is Direct Deposit, `split_by` and `splits` are required.

## Example Usage

```python
from gusto_embedded.models import EmployeePaymentMethodType

value = EmployeePaymentMethodType.DIRECT_DEPOSIT
```


## Values

| Name             | Value            |
| ---------------- | ---------------- |
| `DIRECT_DEPOSIT` | Direct Deposit   |
| `CHECK`          | Check            |