# DocumentSignedRecipientType

The type of recipient associated with the document (will be `Contractor` for Contractor Documents)

## Example Usage

```python
from gusto_embedded_v_2026_06_15.models import DocumentSignedRecipientType

value = DocumentSignedRecipientType.COMPANY

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name         | Value        |
| ------------ | ------------ |
| `COMPANY`    | Company      |
| `EMPLOYEE`   | Employee     |
| `CONTRACTOR` | Contractor   |