# CreateFlowRequestEntityType

The type of target entity applicable to the flow. This field is optional for company flows.

## Example Usage

```python
from gusto_embedded.models import CreateFlowRequestEntityType

value = CreateFlowRequestEntityType.COMPANY
```


## Values

| Name         | Value        |
| ------------ | ------------ |
| `COMPANY`    | Company      |
| `EMPLOYEE`   | Employee     |
| `CONTRACTOR` | Contractor   |
| `PAYROLL`    | Payroll      |