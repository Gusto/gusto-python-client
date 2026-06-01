# SetupStatus

The current status of the state tax setup.
- `not_started`: No requirements have been filled
- `in_progress`: Some requirements have been filled, or default rates are applied
- `complete`: All requirements have been filled without default rates


## Example Usage

```python
from gusto_embedded_v_2026_06_15.models import SetupStatus

value = SetupStatus.NOT_STARTED

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name          | Value         |
| ------------- | ------------- |
| `NOT_STARTED` | not_started   |
| `IN_PROGRESS` | in_progress   |
| `COMPLETE`    | complete      |