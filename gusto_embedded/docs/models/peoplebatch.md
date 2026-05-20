# PeopleBatch

A batch for bulk people creation.


## Fields

| Field                                                      | Type                                                       | Required                                                   | Description                                                |
| ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- |
| `uuid`                                                     | *str*                                                      | :heavy_check_mark:                                         | The unique identifier of the people batch.                 |
| `idempotency_key`                                          | *str*                                                      | :heavy_check_mark:                                         | The idempotency key provided when creating the batch.      |
| `status`                                                   | [models.PeopleBatchStatus](../models/peoplebatchstatus.md) | :heavy_check_mark:                                         | The current status of the batch processing.                |
| `batch_action`                                             | *str*                                                      | :heavy_check_mark:                                         | The action being performed on the batch.                   |