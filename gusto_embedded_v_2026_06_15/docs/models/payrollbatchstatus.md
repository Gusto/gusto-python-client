# PayrollBatchStatus

The lifecycle status of the batch request itself. Terminal values are `completed` (processing finished — inspect `results` and `exclusions` for per-payroll outcomes) and `failed` (the batch crashed at the system level; can be retried). This is distinct from the per-payroll `status` returned inside `results[]`. A `completed` batch does not imply every payroll was cancelled.

## Example Usage

```python
from gusto_embedded_v_2026_06_15.models import PayrollBatchStatus

value = PayrollBatchStatus.PENDING

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name         | Value        |
| ------------ | ------------ |
| `PENDING`    | pending      |
| `PROCESSING` | processing   |
| `COMPLETED`  | completed    |
| `FAILED`     | failed       |