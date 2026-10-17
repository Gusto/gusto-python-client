# Status

The batch's processing state.
- `pending`: accepted, not yet started
- `processing`: reports are being generated
- `completed`: all reports finished
- `failed`: the batch failed before completing


## Example Usage

```python
from gusto_embedded_v_2026_06_15.models import Status

value = Status.PENDING

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name         | Value        |
| ------------ | ------------ |
| `PENDING`    | pending      |
| `PROCESSING` | processing   |
| `COMPLETED`  | completed    |
| `FAILED`     | failed       |