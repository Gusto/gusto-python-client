# PayrollCancellations

## Overview

### Available Operations

* [post_v1_payroll_batches](#post_v1_payroll_batches) - Create a payroll cancellation batch
* [get_v1_payroll_batches_payroll_batch_uuid](#get_v1_payroll_batches_payroll_batch_uuid) - Get a payroll cancellation batch

## post_v1_payroll_batches

Cancels up to 100 payrolls across one or more companies the partner is mapped to, asynchronously.

The batch is processed asynchronously. Use the returned batch UUID to poll `GET /v1/payroll_batches/{payroll_batch_uuid}` for status and per-payroll results.

Each item carries the payroll `uuid` and the `company_uuid` that owns it. A payroll whose company is not mapped to the partner — or that doesn't exist — is recorded as a `not_found` exclusion rather than a hard error, so every requested UUID lands in either `results` or `exclusions`.

Idempotency is scoped per `(partner, idempotency_key)`. A duplicate POST with the same `idempotency_key` returns a 409 Conflict referencing the existing batch UUID — no duplicate processing occurs.

📘 System Access Authentication

This endpoint uses the [Bearer Auth scheme with the system-level access token in the HTTP Authorization header](https://docs.gusto.com/embedded-payroll/docs/system-access)

scope: `payroll_batches:write`

### Example Usage

<!-- UsageSnippet language="python" operationID="post-v1-payroll_batches" method="post" path="/v1/payroll_batches" -->
```python
import gusto_embedded
from gusto_embedded import Gusto
import os


with Gusto() as gusto:

    res = gusto.payroll_cancellations.post_v1_payroll_batches(security=gusto_embedded.PostV1PayrollBatchesSecurity(
        system_access_auth=os.getenv("GUSTO_SYSTEM_ACCESS_AUTH", ""),
    ), idempotency_key="80a74f8b-2c16-45e5-9038-aa108849c6e6", batch_action=gusto_embedded.PostV1PayrollBatchesBatchAction.CANCEL, batch=[
        {
            "entity_type": gusto_embedded.PostV1PayrollBatchesEntityType.PAYROLL,
            "uuid": "f5ac6d4e-8400-4a52-a5cf-dea57b2ee65a",
            "company_uuid": "7cd3f4a2-0bf9-485a-bbc0-f6adbdf0246b",
        },
    ], x_gusto_api_version=gusto_embedded.PostV1PayrollBatchesHeaderXGustoAPIVersion.TWO_THOUSAND_AND_TWENTY_FIVE_MINUS_06_MINUS_15)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                    | Type                                                                                                                                                                                                                         | Required                                                                                                                                                                                                                     | Description                                                                                                                                                                                                                  | Example                                                                                                                                                                                                                      |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `security`                                                                                                                                                                                                                   | [models.PostV1PayrollBatchesSecurity](../../models/postv1payrollbatchessecurity.md)                                                                                                                                          | :heavy_check_mark:                                                                                                                                                                                                           | N/A                                                                                                                                                                                                                          |                                                                                                                                                                                                                              |
| `idempotency_key`                                                                                                                                                                                                            | *str*                                                                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                                           | A partner-generated unique identifier to ensure idempotency of the batch request. Scoped per partner.                                                                                                                        | 80a74f8b-2c16-45e5-9038-aa108849c6e6                                                                                                                                                                                         |
| `batch_action`                                                                                                                                                                                                               | [models.PostV1PayrollBatchesBatchAction](../../models/postv1payrollbatchesbatchaction.md)                                                                                                                                    | :heavy_check_mark:                                                                                                                                                                                                           | The action to perform on the batch. Only `cancel` is supported.                                                                                                                                                              | cancel                                                                                                                                                                                                                       |
| `batch`                                                                                                                                                                                                                      | List[[models.Batch](../../models/batch.md)]                                                                                                                                                                                  | :heavy_check_mark:                                                                                                                                                                                                           | Array of payrolls to cancel. Maximum 100 payrolls per request.                                                                                                                                                               |                                                                                                                                                                                                                              |
| `x_gusto_api_version`                                                                                                                                                                                                        | [Optional[models.PostV1PayrollBatchesHeaderXGustoAPIVersion]](../../models/postv1payrollbatchesheaderxgustoapiversion.md)                                                                                                    | :heavy_minus_sign:                                                                                                                                                                                                           | Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used. |                                                                                                                                                                                                                              |
| `retries`                                                                                                                                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                           | Configuration to override the default retry behavior of the client.                                                                                                                                                          |                                                                                                                                                                                                                              |

### Response

**[models.PayrollBatch](../../models/payrollbatch.md)**

### Errors

| Error Type                       | Status Code                      | Content Type                     |
| -------------------------------- | -------------------------------- | -------------------------------- |
| models.PayrollBatchConflictError | 409                              | application/json                 |
| models.UnprocessableEntityError1 | 422                              | application/json                 |
| models.APIError                  | 4XX, 5XX                         | \*/\*                            |

## get_v1_payroll_batches_payroll_batch_uuid

Returns the status and per-payroll results of a payroll cancellation batch.

Poll this endpoint until the batch `status` reaches a terminal value (`completed` or `failed`). Once terminal, the response includes the `results` array (one entry per authorized payroll, each with its own per-payroll `status` — `success` or `failed`) and the `exclusions` array (one entry per payroll that could not be processed). A cancel is atomic, so a per-payroll result is only ever `success` or `failed` — never `partial_success`.

Note that the top-level batch `status` (`pending` / `processing` / `completed` / `failed`) is the request lifecycle, distinct from the per-payroll `status` inside `results[]`. A `completed` batch does not imply every payroll was cancelled — inspect the array for per-payroll outcomes.

Results are stored in Redis with a limited TTL after completion. If the partner polls after results have expired, this endpoint returns 410 Gone — partners should re-submit a new batch.

📘 System Access Authentication

This endpoint uses the [Bearer Auth scheme with the system-level access token in the HTTP Authorization header](https://docs.gusto.com/embedded-payroll/docs/system-access)

scope: `payroll_batches:read`

### Example Usage

<!-- UsageSnippet language="python" operationID="get-v1-payroll_batches-payroll_batch_uuid" method="get" path="/v1/payroll_batches/{payroll_batch_uuid}" -->
```python
import gusto_embedded
from gusto_embedded import Gusto
import os


with Gusto() as gusto:

    res = gusto.payroll_cancellations.get_v1_payroll_batches_payroll_batch_uuid(security=gusto_embedded.GetV1PayrollBatchesPayrollBatchUUIDSecurity(
        system_access_auth=os.getenv("GUSTO_SYSTEM_ACCESS_AUTH", ""),
    ), payroll_batch_uuid="<id>", x_gusto_api_version=gusto_embedded.GetV1PayrollBatchesPayrollBatchUUIDHeaderXGustoAPIVersion.TWO_THOUSAND_AND_TWENTY_FIVE_MINUS_06_MINUS_15)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                    | Type                                                                                                                                                                                                                         | Required                                                                                                                                                                                                                     | Description                                                                                                                                                                                                                  |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `security`                                                                                                                                                                                                                   | [models.GetV1PayrollBatchesPayrollBatchUUIDSecurity](../../models/getv1payrollbatchespayrollbatchuuidsecurity.md)                                                                                                            | :heavy_check_mark:                                                                                                                                                                                                           | N/A                                                                                                                                                                                                                          |
| `payroll_batch_uuid`                                                                                                                                                                                                         | *str*                                                                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                                           | The UUID of the payroll cancellation batch returned by `POST /v1/payroll_batches`.                                                                                                                                           |
| `x_gusto_api_version`                                                                                                                                                                                                        | [Optional[models.GetV1PayrollBatchesPayrollBatchUUIDHeaderXGustoAPIVersion]](../../models/getv1payrollbatchespayrollbatchuuidheaderxgustoapiversion.md)                                                                      | :heavy_minus_sign:                                                                                                                                                                                                           | Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used. |
| `retries`                                                                                                                                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                           | Configuration to override the default retry behavior of the client.                                                                                                                                                          |

### Response

**[models.PayrollBatchResults](../../models/payrollbatchresults.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.NotFoundErrorObject | 404, 410                   | application/json           |
| models.APIError            | 4XX, 5XX                   | \*/\*                      |