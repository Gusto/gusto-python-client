# PeopleBatchStatus

The current status of the batch processing.

## Example Usage

```python
from gusto_embedded_v_2026_06_15.models import PeopleBatchStatus

value = PeopleBatchStatus.PENDING

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name              | Value             |
| ----------------- | ----------------- |
| `PENDING`         | pending           |
| `PROCESSING`      | processing        |
| `COMPLETED`       | completed         |
| `FAILED`          | failed            |
| `PARTIAL_SUCCESS` | partial_success   |