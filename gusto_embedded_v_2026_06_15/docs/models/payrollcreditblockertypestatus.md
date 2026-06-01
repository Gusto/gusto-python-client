# PayrollCreditBlockerTypeStatus

The status of the credit blocker

## Example Usage

```python
from gusto_embedded_v_2026_06_15.models import PayrollCreditBlockerTypeStatus

value = PayrollCreditBlockerTypeStatus.UNRESOLVED

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name             | Value            |
| ---------------- | ---------------- |
| `UNRESOLVED`     | unresolved       |
| `PENDING_REVIEW` | pending_review   |
| `RESOLVED`       | resolved         |
| `FAILED`         | failed           |