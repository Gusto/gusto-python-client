# PayrollBatchResultsResultsStatus

The outcome of cancelling this payroll. A cancel is atomic — there is no per-payroll `partial_success`.
- `success`: the payroll was cancelled, or required no action (already cancelled / never run)
- `failed`: the payroll could not be cancelled; see `errors`


## Example Usage

```python
from gusto_embedded_v_2026_06_15.models import PayrollBatchResultsResultsStatus

value = PayrollBatchResultsResultsStatus.SUCCESS

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name      | Value     |
| --------- | --------- |
| `SUCCESS` | success   |
| `FAILED`  | failed    |