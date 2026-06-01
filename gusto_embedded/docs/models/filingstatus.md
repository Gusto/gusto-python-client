# FilingStatus

Determines which tax return form an individual will use. One of: Single, Married, Head of Household, Exempt from withholding.

## Example Usage

```python
from gusto_embedded.models import FilingStatus

value = FilingStatus.SINGLE
```


## Values

| Name                      | Value                     |
| ------------------------- | ------------------------- |
| `SINGLE`                  | Single                    |
| `MARRIED`                 | Married                   |
| `HEAD_OF_HOUSEHOLD`       | Head of Household         |
| `EXEMPT_FROM_WITHHOLDING` | Exempt from withholding   |