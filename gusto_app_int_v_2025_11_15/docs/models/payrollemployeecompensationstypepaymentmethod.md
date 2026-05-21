# PayrollEmployeeCompensationsTypePaymentMethod

The employee's compensation payment method. Is *only* `Historical` when retrieving external payrolls initially run outside of Gusto, then put into Gusto.

## Example Usage

```python
from gusto_app_integration_v_2025_11_15.models import PayrollEmployeeCompensationsTypePaymentMethod

value = PayrollEmployeeCompensationsTypePaymentMethod.DIRECT_DEPOSIT

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name             | Value            |
| ---------------- | ---------------- |
| `DIRECT_DEPOSIT` | Direct Deposit   |
| `CHECK`          | Check            |
| `HISTORICAL`     | Historical       |