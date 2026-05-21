# PayrollProcessingRequestStatus

The status of the payroll processing request

## Example Usage

```python
from gusto_app_integration_v_2025_11_15.models import PayrollProcessingRequestStatus

value = PayrollProcessingRequestStatus.CALCULATING

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name                | Value               |
| ------------------- | ------------------- |
| `CALCULATING`       | calculating         |
| `CALCULATE_SUCCESS` | calculate_success   |
| `SUBMITTING`        | submitting          |
| `SUBMIT_SUCCESS`    | submit_success      |
| `PROCESSING_FAILED` | processing_failed   |