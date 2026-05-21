# PaymentStatus

The status of the ACH transaction

## Example Usage

```python
from gusto_embedded_v_2025_11_15.models import PaymentStatus

value = PaymentStatus.UNSUBMITTED

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name          | Value         |
| ------------- | ------------- |
| `UNSUBMITTED` | unsubmitted   |
| `SUBMITTED`   | submitted     |
| `SUCCESSFUL`  | successful    |
| `FAILED`      | failed        |