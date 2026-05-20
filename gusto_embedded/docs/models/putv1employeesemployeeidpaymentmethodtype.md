# PutV1EmployeesEmployeeIDPaymentMethodType

The payment method type. If type is Check, split_by and splits do not need to be populated. If type is Direct Deposit, split_by and splits are required.

## Example Usage

```python
from gusto_embedded.models import PutV1EmployeesEmployeeIDPaymentMethodType

value = PutV1EmployeesEmployeeIDPaymentMethodType.CHECK
```


## Values

| Name             | Value            |
| ---------------- | ---------------- |
| `CHECK`          | Check            |
| `DIRECT_DEPOSIT` | Direct Deposit   |