# WebhooksHealthCheckStatus

The representation of a webhooks health check response


## Fields

| Field                                                                                            | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `status`                                                                                         | [Optional[models.WebhooksHealthCheckStatusStatus]](../models/webhookshealthcheckstatusstatus.md) | :heavy_minus_sign:                                                                               | Latest health status of the webhooks system                                                      |
| `last_checked_at`                                                                                | [date](https://docs.python.org/3/library/datetime.html#date-objects)                             | :heavy_minus_sign:                                                                               | ISO8601 timestamp of the last successful health check with millisecond precision                 |