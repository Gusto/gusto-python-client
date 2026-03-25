# PayrollWithholdingPayPeriodType

The payment schedule tax rate the payroll is based on. Only included for off-cycle payrolls.

## Example Usage

```python
from gusto_app_integration.models import PayrollWithholdingPayPeriodType

value = PayrollWithholdingPayPeriodType.EVERY_WEEK
```


## Values

| Name               | Value              |
| ------------------ | ------------------ |
| `EVERY_WEEK`       | Every week         |
| `EVERY_OTHER_WEEK` | Every other week   |
| `TWICE_PER_MONTH`  | Twice per month    |
| `MONTHLY`          | Monthly            |
| `QUARTERLY`        | Quarterly          |
| `SEMIANNUALLY`     | Semiannually       |
| `ANNUALLY`         | Annually           |