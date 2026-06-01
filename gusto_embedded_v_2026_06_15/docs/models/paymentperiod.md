# PaymentPeriod

How often the agency collects the withholding amount. e.g. $500 monthly -> `Monthly`.

## Example Usage

```python
from gusto_embedded_v_2026_06_15.models import PaymentPeriod

value = PaymentPeriod.EVERY_WEEK

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name               | Value              |
| ------------------ | ------------------ |
| `EVERY_WEEK`       | Every week         |
| `EVERY_OTHER_WEEK` | Every other week   |
| `TWICE_PER_MONTH`  | Twice per month    |
| `MONTHLY`          | Monthly            |