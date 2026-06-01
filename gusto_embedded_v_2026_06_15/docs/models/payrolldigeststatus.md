# PayrollDigestStatus

The lifecycle status of the batch request itself. Terminal values are `completed` (processing finished — inspect `results` and `exclusions` for per-company outcomes) and `failed` (request failed; can be retried). This is distinct from the per-company `status` returned inside `results[]` and `exclusions[]`.

## Example Usage

```python
from gusto_embedded_v_2026_06_15.models import PayrollDigestStatus

value = PayrollDigestStatus.PENDING

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name         | Value        |
| ------------ | ------------ |
| `PENDING`    | pending      |
| `PROCESSING` | processing   |
| `COMPLETED`  | completed    |
| `FAILED`     | failed       |