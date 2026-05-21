# Frequency

The frequency that employees on this pay schedule are paid with Gusto. Only weekly, bi-weekly, twice per month, and monthly are supported on create and update.

- `Every week`: Weekly pay.
- `Every other week`: Biweekly pay.
- `Twice per month`: Two pay dates per month; require day_1 and day_2 (use 31 for last day of month).
- `Monthly`: One pay date per month; require day_1 (1-31).


## Example Usage

```python
from gusto_embedded_v_2025_11_15.models import Frequency

value = Frequency.EVERY_WEEK
```


## Values

| Name               | Value              |
| ------------------ | ------------------ |
| `EVERY_WEEK`       | Every week         |
| `EVERY_OTHER_WEEK` | Every other week   |
| `TWICE_PER_MONTH`  | Twice per month    |
| `MONTHLY`          | Monthly            |