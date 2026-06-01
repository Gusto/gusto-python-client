# FilingForm

The form used by the company for federal tax filing. One of:
- 941 (Quarterly federal tax return form)
- 944 (Annual federal tax return form)

## Example Usage

```python
from gusto_embedded_v_2026_06_15.models import FilingForm

value = FilingForm.NINE_HUNDRED_AND_FORTY_ONE

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name                          | Value                         |
| ----------------------------- | ----------------------------- |
| `NINE_HUNDRED_AND_FORTY_ONE`  | 941                           |
| `NINE_HUNDRED_AND_FORTY_FOUR` | 944                           |