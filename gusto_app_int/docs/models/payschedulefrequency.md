# PayScheduleFrequency

Pay frequency for this schedule. READ-ONLY.

- `Every week`: Employees are paid weekly.
- `Every other week`: Employees are paid bi-weekly (every two weeks).
- `Twice per month`: Employees are paid on two fixed days each month (e.g. 1st and 15th); use day_1 and day_2.
- `Monthly`: Employees are paid once per month; use day_1 for the pay day.
- `Quarterly`: Employees are paid every three months.
- `Annually`: Employees are paid once per year.


## Example Usage

```python
from gusto_app_integration.models import PayScheduleFrequency

value = PayScheduleFrequency.EVERY_WEEK
```


## Values

| Name               | Value              |
| ------------------ | ------------------ |
| `EVERY_WEEK`       | Every week         |
| `EVERY_OTHER_WEEK` | Every other week   |
| `TWICE_PER_MONTH`  | Twice per month    |
| `MONTHLY`          | Monthly            |
| `QUARTERLY`        | Quarterly          |
| `ANNUALLY`         | Annually           |