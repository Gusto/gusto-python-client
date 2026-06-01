# Source

The source of the company benefit. This can be "internal", "external", or "partnered". Company benefits created via the API default to "external". Certain partners can create company benefits with a source of "partnered".

## Example Usage

```python
from gusto_embedded_v_2026_06_15.models import Source

value = Source.INTERNAL

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name        | Value       |
| ----------- | ----------- |
| `INTERNAL`  | internal    |
| `EXTERNAL`  | external    |
| `PARTNERED` | partnered   |