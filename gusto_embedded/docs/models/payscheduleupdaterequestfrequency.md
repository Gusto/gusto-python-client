# PayScheduleUpdateRequestFrequency

The frequency that employees on this pay schedule are paid with Gusto. Only weekly, bi-weekly, twice per month, and monthly are supported on create and update.

- `Every week`: Weekly pay.
- `Every other week`: Biweekly pay.
- `Twice per month`: Two pay dates per month. Provide first_pay_period_pay_day and second_pay_period_pay_day for a regular schedule, and add first_pay_period_end_day and second_pay_period_end_day for a flexible schedule. Legacy day_1/day_2 are still accepted separately. Use 31 for the last day of the month.
- `Monthly`: One pay date per month; require day_1 (1-31).


## Example Usage

```python
from gusto_embedded.models import PayScheduleUpdateRequestFrequency

value = PayScheduleUpdateRequestFrequency.EVERY_WEEK
```


## Values

| Name               | Value              |
| ------------------ | ------------------ |
| `EVERY_WEEK`       | Every week         |
| `EVERY_OTHER_WEEK` | Every other week   |
| `TWICE_PER_MONTH`  | Twice per month    |
| `MONTHLY`          | Monthly            |