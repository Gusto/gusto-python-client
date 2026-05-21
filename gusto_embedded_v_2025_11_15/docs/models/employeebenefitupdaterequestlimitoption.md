# EmployeeBenefitUpdateRequestLimitOption

Some benefits require additional information to determine
their limit.

`Family` or `Individual`: Applicable to HSA benefit.

`Joint Filing or Single` or `Married and Filing Separately`: Applicable to Dependent Care FSA benefit.

## Example Usage

```python
from gusto_embedded_v_2025_11_15.models import EmployeeBenefitUpdateRequestLimitOption

value = EmployeeBenefitUpdateRequestLimitOption.FAMILY
```


## Values

| Name                            | Value                           |
| ------------------------------- | ------------------------------- |
| `FAMILY`                        | Family                          |
| `INDIVIDUAL`                    | Individual                      |
| `JOINT_FILING_OR_SINGLE`        | Joint Filing or Single          |
| `MARRIED_AND_FILING_SEPARATELY` | Married and Filing Separately   |