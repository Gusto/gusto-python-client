# RecoveryCaseStatus

Status of the recovery case

## Example Usage

```python
from gusto_embedded_v_2025_11_15.models import RecoveryCaseStatus

value = RecoveryCaseStatus.OPEN

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name                | Value               |
| ------------------- | ------------------- |
| `OPEN`              | open                |
| `REDEBIT_INITIATED` | redebit_initiated   |
| `WIRE_INITIATED`    | wire_initiated      |
| `RECOVERED`         | recovered           |
| `LOST`              | lost                |