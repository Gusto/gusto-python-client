# PaymentEventType

The type of payment event associated with the ACH transaction

## Example Usage

```python
from gusto_embedded_v_2026_06_15.models import PaymentEventType

value = PaymentEventType.PAYROLL

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name                 | Value                |
| -------------------- | -------------------- |
| `PAYROLL`            | Payroll              |
| `CONTRACTOR_PAYMENT` | ContractorPayment    |