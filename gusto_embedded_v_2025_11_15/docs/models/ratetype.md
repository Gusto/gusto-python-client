# RateType

[for `workers_compensation_rate`] The type of rate being collected. Either:
  - `percent`: A percentage formatted as a decimal, e.g. `0.01` for 1%
  - `currency_per_hour`: A dollar amount per hour, e.g. `3.24` for $3.24/hr


## Example Usage

```python
from gusto_embedded_v_2025_11_15.models import RateType

value = RateType.PERCENT

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name                | Value               |
| ------------------- | ------------------- |
| `PERCENT`           | percent             |
| `CURRENCY_PER_HOUR` | currency_per_hour   |