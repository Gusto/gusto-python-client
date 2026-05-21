# IntegrationType

The kind of integration set up for the company. Required when `aggregation` is 'integration'. Must be null if `aggregation` is not 'integration'.

## Example Usage

```python
from gusto_embedded.models import IntegrationType

value = IntegrationType.XERO
```


## Values

| Name   | Value  |
| ------ | ------ |
| `XERO` | xero   |
| `QBO`  | qbo    |