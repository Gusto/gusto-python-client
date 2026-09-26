# PayrollBatchResultsCategory

Machine-readable category for why the payroll was excluded.
- `not_found`: the payroll does not exist, or is not associated with a company the partner is mapped to
- `duplicate_operation`: the same payroll UUID appeared more than once in the request; only the first occurrence is processed


## Example Usage

```python
from gusto_embedded.models import PayrollBatchResultsCategory

value = PayrollBatchResultsCategory.NOT_FOUND
```


## Values

| Name                  | Value                 |
| --------------------- | --------------------- |
| `NOT_FOUND`           | not_found             |
| `DUPLICATE_OPERATION` | duplicate_operation   |