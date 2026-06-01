# WebhookSubscriptionStatus

The status of the webhook subscription.

## Example Usage

```python
from gusto_app_integration_v_2026_06_15.models import WebhookSubscriptionStatus

value = WebhookSubscriptionStatus.PENDING

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name          | Value         |
| ------------- | ------------- |
| `PENDING`     | pending       |
| `VERIFIED`    | verified      |
| `REMOVED`     | removed       |
| `UNREACHABLE` | unreachable   |