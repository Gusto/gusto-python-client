# PayrollUnprocessedEmployeeCompensationsTypePaymentMethod

The employee's compensation payment method. Is *only* `Historical` when retrieving external payrolls initially run outside of Gusto, then put into Gusto.

## Example Usage

```python
from gusto_embedded_v_2025_11_15.models import PayrollUnprocessedEmployeeCompensationsTypePaymentMethod

value = PayrollUnprocessedEmployeeCompensationsTypePaymentMethod.DIRECT_DEPOSIT

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name             | Value            |
| ---------------- | ---------------- |
| `DIRECT_DEPOSIT` | Direct Deposit   |
| `CHECK`          | Check            |
| `HISTORICAL`     | Historical       |