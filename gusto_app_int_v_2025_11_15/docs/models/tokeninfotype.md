# TokenInfoType

The type of resource owner:
- `CompanyAdmin`: A company administrator
- `Employee`: An employee
- `Contractor`: A contractor


## Example Usage

```python
from gusto_app_integration_v_2025_11_15.models import TokenInfoType

value = TokenInfoType.COMPANY_ADMIN

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name            | Value           |
| --------------- | --------------- |
| `COMPANY_ADMIN` | CompanyAdmin    |
| `EMPLOYEE`      | Employee        |
| `CONTRACTOR`    | Contractor      |