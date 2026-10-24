# PayrollBatchResultsResultsCategory

Machine-readable reason the cancellation failed.
- `not_cancellable`: the payroll is past the point where it can be cancelled
- `internal_error`: an unexpected error occurred; the request can be retried


## Example Usage

```python
from gusto_embedded_v_2026_06_15.models import PayrollBatchResultsResultsCategory

value = PayrollBatchResultsResultsCategory.NOT_CANCELLABLE

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name              | Value             |
| ----------------- | ----------------- |
| `NOT_CANCELLABLE` | not_cancellable   |
| `INTERNAL_ERROR`  | internal_error    |