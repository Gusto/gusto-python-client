# DocumentSignedRecipientType

The type of recipient associated with the document (will be `Contractor` for Contractor Documents)

## Example Usage

```python
from gusto_embedded.models import DocumentSignedRecipientType

value = DocumentSignedRecipientType.COMPANY
```


## Values

| Name         | Value        |
| ------------ | ------------ |
| `COMPANY`    | Company      |
| `EMPLOYEE`   | Employee     |
| `CONTRACTOR` | Contractor   |