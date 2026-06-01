# EmploymentStatus

The employee's employment status. Supplying an invalid option will set the employment_status to *not_set*.

## Example Usage

```python
from gusto_app_integration_v_2026_06_15.models import EmploymentStatus

value = EmploymentStatus.PART_TIME

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name                 | Value                |
| -------------------- | -------------------- |
| `PART_TIME`          | part_time            |
| `FULL_TIME`          | full_time            |
| `PART_TIME_ELIGIBLE` | part_time_eligible   |
| `VARIABLE`           | variable             |
| `SEASONAL`           | seasonal             |
| `NOT_SET`            | not_set              |