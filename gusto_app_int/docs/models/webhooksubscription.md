# WebhookSubscription

The representation of webhook subscription.


## Fields

| Field                                                                                | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `uuid`                                                                               | *str*                                                                                | :heavy_check_mark:                                                                   | The UUID of the webhook subscription.                                                |
| `url`                                                                                | *Optional[str]*                                                                      | :heavy_minus_sign:                                                                   | The webhook subscriber URL. Updates will be POSTed to this URL.                      |
| `status`                                                                             | [Optional[models.WebhookSubscriptionStatus]](../models/webhooksubscriptionstatus.md) | :heavy_minus_sign:                                                                   | The status of the webhook subscription.                                              |
| `subscription_types`                                                                 | List[[models.SubscriptionTypes](../models/subscriptiontypes.md)]                     | :heavy_minus_sign:                                                                   | Receive updates for these types.                                                     |