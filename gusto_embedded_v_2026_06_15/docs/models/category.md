# Category

The category of the company attachment.
- `gep_notice`: A tax notice attachment
- `compliance`: A compliance attachment
- `other`: Any other attachment type


## Example Usage

```python
from gusto_embedded_v_2026_06_15.models import Category

value = Category.GEP_NOTICE

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name         | Value        |
| ------------ | ------------ |
| `GEP_NOTICE` | gep_notice   |
| `COMPLIANCE` | compliance   |
| `OTHER`      | other        |