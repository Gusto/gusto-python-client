# TimeSheetsBatchStatus

Status of the batch. READ-ONLY.

## State Transitions
```
pending ──► processing ──┬──► success
                         ├──► partial_success
                         └──► failed
```

- `pending`: The batch is accepted and waits to be processed.
- `processing`: The time sheets in the batch are being processed.
- `success`: All time sheets were processed successfully.
- `partial_success`: Some time sheets were processed successfully and some failed. See `results`.
- `failed`: All time sheets failed. See `results`.


## Example Usage

```python
from gusto_app_integration_v_2026_06_15.models import TimeSheetsBatchStatus

value = TimeSheetsBatchStatus.PENDING

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name              | Value             |
| ----------------- | ----------------- |
| `PENDING`         | pending           |
| `PROCESSING`      | processing        |
| `SUCCESS`         | success           |
| `FAILED`          | failed            |
| `PARTIAL_SUCCESS` | partial_success   |