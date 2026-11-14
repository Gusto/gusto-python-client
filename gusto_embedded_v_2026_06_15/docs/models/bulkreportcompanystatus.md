# BulkReportCompanyStatus

This company's overall status across its `reports`:
- `success`: every report succeeded
- `partial_success`: some succeeded, some failed
- `failed`: every report failed
- `pending`: at least one report is still being generated


## Example Usage

```python
from gusto_embedded_v_2026_06_15.models import BulkReportCompanyStatus

value = BulkReportCompanyStatus.PENDING

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name              | Value             |
| ----------------- | ----------------- |
| `PENDING`         | pending           |
| `SUCCESS`         | success           |
| `PARTIAL_SUCCESS` | partial_success   |
| `FAILED`          | failed            |