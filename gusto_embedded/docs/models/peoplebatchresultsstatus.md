# PeopleBatchResultsStatus

The current status of the batch processing.

## Example Usage

```python
from gusto_embedded.models import PeopleBatchResultsStatus

value = PeopleBatchResultsStatus.PENDING
```


## Values

| Name              | Value             |
| ----------------- | ----------------- |
| `PENDING`         | pending           |
| `PROCESSING`      | processing        |
| `COMPLETED`       | completed         |
| `FAILED`          | failed            |
| `PARTIAL_SUCCESS` | partial_success   |