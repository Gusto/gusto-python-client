# TaxFilingStatus

The current status of the tax filing

## Example Usage

```python
from gusto_embedded_v_2026_06_15.models import TaxFilingStatus

value = TaxFilingStatus.NOT_STARTED

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name           | Value          |
| -------------- | -------------- |
| `NOT_STARTED`  | not_started    |
| `IN_PROGRESS`  | in_progress    |
| `BLOCKED`      | blocked        |
| `ACCEPTED`     | accepted       |
| `NOT_REQUIRED` | not_required   |
| `FAILED`       | failed         |
| `UNKNOWN`      | unknown        |