# PayScheduleFrequencyCreateUpdate

Pay frequency when creating or updating a schedule. Only weekly, bi-weekly, twice per month, and monthly are supported via the API.

- `Every week`: Weekly pay.
- `Every other week`: Biweekly pay.
- `Twice per month`: Two pay dates per month; require day_1 and day_2 (use 31 for last day of month).
- `Monthly`: One pay date per month; require day_1 (1-31).


## Example Usage

```python
from gusto_embedded.models import PayScheduleFrequencyCreateUpdate

value = PayScheduleFrequencyCreateUpdate.EVERY_WEEK
```


## Values

| Name               | Value              |
| ------------------ | ------------------ |
| `EVERY_WEEK`       | Every week         |
| `EVERY_OTHER_WEEK` | Every other week   |
| `TWICE_PER_MONTH`  | Twice per month    |
| `MONTHLY`          | Monthly            |