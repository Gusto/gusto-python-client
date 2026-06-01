# PayrollDigestResultsStatus

The lifecycle status of the batch request itself. Terminal values are `completed` (processing finished — inspect `results` and `exclusions` for per-company outcomes) and `failed` (request failed; can be retried). This is distinct from the per-company `status` returned inside `results[]` and `exclusions[]`.

## Example Usage

```python
from gusto_embedded.models import PayrollDigestResultsStatus

value = PayrollDigestResultsStatus.PENDING
```


## Values

| Name         | Value        |
| ------------ | ------------ |
| `PENDING`    | pending      |
| `PROCESSING` | processing   |
| `COMPLETED`  | completed    |
| `FAILED`     | failed       |