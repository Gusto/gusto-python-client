# ExternalPayrollStatus

The status of the external payroll. The status will be `unprocessed` when the external payroll is created and transition to `processed` once tax liabilities are entered and finalized.  Once in the `processed` status all actions that can edit an external payroll will be disabled.

## Example Usage

```python
from gusto_embedded_v_2026_06_15.models import ExternalPayrollStatus

value = ExternalPayrollStatus.UNPROCESSED

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name          | Value         |
| ------------- | ------------- |
| `UNPROCESSED` | unprocessed   |
| `PROCESSED`   | processed     |