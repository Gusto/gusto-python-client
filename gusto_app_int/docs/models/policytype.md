# PolicyType

Type of the time off policy. Only "vacation" and "sick" can be created through the API, but other types may be present if the company was previously a Gusto.com customer.

## Example Usage

```python
from gusto_app_integration.models import PolicyType

value = PolicyType.VACATION
```


## Values

| Name                       | Value                      |
| -------------------------- | -------------------------- |
| `VACATION`                 | vacation                   |
| `SICK`                     | sick                       |
| `BEREAVEMENT`              | bereavement                |
| `CUSTOM`                   | custom                     |
| `FLOATING_HOLIDAY`         | floating_holiday           |
| `JURY_DUTY`                | jury_duty                  |
| `LEARNING_AND_DEVELOPMENT` | learning_and_development   |
| `PARENTAL_LEAVE`           | parental_leave             |
| `PERSONAL_DAY`             | personal_day               |
| `VOLUNTEER`                | volunteer                  |
| `WEATHER`                  | weather                    |