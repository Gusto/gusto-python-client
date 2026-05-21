# CompanyBenefitWithEmployeeBenefitsSource

The source of the company benefit. This can be "internal", "external", or "partnered". Company benefits created via the API default to "external". Certain partners can create company benefits with a source of "partnered".

## Example Usage

```python
from gusto_embedded_v_2025_11_15.models import CompanyBenefitWithEmployeeBenefitsSource

value = CompanyBenefitWithEmployeeBenefitsSource.INTERNAL

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name        | Value       |
| ----------- | ----------- |
| `INTERNAL`  | internal    |
| `EXTERNAL`  | external    |
| `PARTNERED` | partnered   |