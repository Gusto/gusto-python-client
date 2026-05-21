# PaymentStatus

The status of the ACH transaction

## Example Usage

```python
from gusto_embedded.models import PaymentStatus

value = PaymentStatus.UNSUBMITTED
```


## Values

| Name          | Value         |
| ------------- | ------------- |
| `UNSUBMITTED` | unsubmitted   |
| `SUBMITTED`   | submitted     |
| `SUCCESSFUL`  | successful    |
| `FAILED`      | failed        |