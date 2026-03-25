# RecoveryCaseStatus

Status of the recovery case

## Example Usage

```python
from gusto_embedded.models import RecoveryCaseStatus

value = RecoveryCaseStatus.OPEN
```


## Values

| Name                | Value               |
| ------------------- | ------------------- |
| `OPEN`              | open                |
| `REDEBIT_INITIATED` | redebit_initiated   |
| `WIRE_INITIATED`    | wire_initiated      |
| `RECOVERED`         | recovered           |
| `LOST`              | lost                |