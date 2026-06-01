# PayrollDigests

## Overview

### Available Operations

* [post_v1_payroll_digests](#post_v1_payroll_digests) - Create a payroll digest batch
* [get_v1_payroll_digests_payroll_digest_uuid](#get_v1_payroll_digests_payroll_digest_uuid) - Get a payroll digest batch

## post_v1_payroll_digests

Triggers an asynchronous computation of payroll digest data (statuses, blockers, pay periods, totals) across up to 25 companies that the partner is mapped to.

The batch is processed asynchronously. Use the returned batch UUID to poll `GET /v1/payroll_digests/{payroll_digest_uuid}` for status and results.

Idempotency is scoped per `(partner, idempotency_key)`. A duplicate POST with the same `idempotency_key` returns a 409 Conflict referencing the existing batch UUID — no duplicate computation occurs.

📘 System Access Authentication

This endpoint uses the [Bearer Auth scheme with the system-level access token in the HTTP Authorization header](https://docs.gusto.com/embedded-payroll/docs/system-access)

scope: `payroll_digests:write`

### Example Usage

<!-- UsageSnippet language="python" operationID="post-v1-payroll_digests" method="post" path="/v1/payroll_digests" -->
```python
import gusto_embedded_v_2026_06_15
from gusto_embedded_v_2026_06_15 import Gusto
import os


with Gusto() as gusto:

    res = gusto.payroll_digests.post_v1_payroll_digests(security=gusto_embedded_v_2026_06_15.PostV1PayrollDigestsSecurity(
        system_access_auth=os.getenv("GUSTO_SYSTEM_ACCESS_AUTH", ""),
    ), idempotency_key="80a74f8b-2c16-45e5-9038-aa108849c6e6", batch_action=gusto_embedded_v_2026_06_15.PostV1PayrollDigestsBatchAction.CREATE, batch=[], x_gusto_api_version=gusto_embedded_v_2026_06_15.PostV1PayrollDigestsHeaderXGustoAPIVersion.TWO_THOUSAND_AND_TWENTY_SIX_MINUS_06_MINUS_15)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                    | Type                                                                                                                                                                                                                         | Required                                                                                                                                                                                                                     | Description                                                                                                                                                                                                                  | Example                                                                                                                                                                                                                      |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `security`                                                                                                                                                                                                                   | [models.PostV1PayrollDigestsSecurity](../../models/postv1payrolldigestssecurity.md)                                                                                                                                          | :heavy_check_mark:                                                                                                                                                                                                           | N/A                                                                                                                                                                                                                          |                                                                                                                                                                                                                              |
| `idempotency_key`                                                                                                                                                                                                            | *str*                                                                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                                           | A partner-generated unique identifier to ensure idempotency of the batch request. Scoped per partner.                                                                                                                        | 80a74f8b-2c16-45e5-9038-aa108849c6e6                                                                                                                                                                                         |
| `batch_action`                                                                                                                                                                                                               | [models.PostV1PayrollDigestsBatchAction](../../models/postv1payrolldigestsbatchaction.md)                                                                                                                                    | :heavy_check_mark:                                                                                                                                                                                                           | The action to perform on the batch.                                                                                                                                                                                          | create                                                                                                                                                                                                                       |
| `batch`                                                                                                                                                                                                                      | List[[models.PostV1PayrollDigestsBatch](../../models/postv1payrolldigestsbatch.md)]                                                                                                                                          | :heavy_check_mark:                                                                                                                                                                                                           | Array of companies to fetch payroll digest data for. Maximum 25 companies per request.                                                                                                                                       |                                                                                                                                                                                                                              |
| `x_gusto_api_version`                                                                                                                                                                                                        | [Optional[models.PostV1PayrollDigestsHeaderXGustoAPIVersion]](../../models/postv1payrolldigestsheaderxgustoapiversion.md)                                                                                                    | :heavy_minus_sign:                                                                                                                                                                                                           | Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used. |                                                                                                                                                                                                                              |
| `retries`                                                                                                                                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                           | Configuration to override the default retry behavior of the client.                                                                                                                                                          |                                                                                                                                                                                                                              |

### Response

**[models.PayrollDigest](../../models/payrolldigest.md)**

### Errors

| Error Type                        | Status Code                       | Content Type                      |
| --------------------------------- | --------------------------------- | --------------------------------- |
| models.PayrollDigestConflictError | 409                               | application/json                  |
| models.UnprocessableEntityError1  | 422                               | application/json                  |
| models.APIError                   | 4XX, 5XX                          | \*/\*                             |

## get_v1_payroll_digests_payroll_digest_uuid

Returns the status and results of a payroll digest batch.

Poll this endpoint until the batch `status` reaches a terminal value (`completed` or `failed`). Once terminal, the response includes the full `results` array (one entry per attempted company, each with its own per-company `status` — `success`, `partial_success`, or `failed`) and the `exclusions` array (one entry per company that could not be looked up or processed).

Note that the top-level batch `status` (`pending` / `processing` / `completed` / `failed`) is distinct from the per-company `status` returned inside `results[]` and `exclusions[]`. A `completed` batch does not imply every company succeeded — inspect the arrays for per-company outcomes.

Results are stored in Redis with a short TTL after completion. If the partner polls after results have expired, this endpoint returns 410 Gone — partners should re-submit a new batch to fetch fresh data.

📘 System Access Authentication

This endpoint uses the [Bearer Auth scheme with the system-level access token in the HTTP Authorization header](https://docs.gusto.com/embedded-payroll/docs/system-access)

scope: `payroll_digests:read`

### Example Usage

<!-- UsageSnippet language="python" operationID="get-v1-payroll_digests-payroll_digest_uuid" method="get" path="/v1/payroll_digests/{payroll_digest_uuid}" -->
```python
import gusto_embedded_v_2026_06_15
from gusto_embedded_v_2026_06_15 import Gusto
import os


with Gusto() as gusto:

    res = gusto.payroll_digests.get_v1_payroll_digests_payroll_digest_uuid(security=gusto_embedded_v_2026_06_15.GetV1PayrollDigestsPayrollDigestUUIDSecurity(
        system_access_auth=os.getenv("GUSTO_SYSTEM_ACCESS_AUTH", ""),
    ), payroll_digest_uuid="<id>", x_gusto_api_version=gusto_embedded_v_2026_06_15.GetV1PayrollDigestsPayrollDigestUUIDHeaderXGustoAPIVersion.TWO_THOUSAND_AND_TWENTY_SIX_MINUS_06_MINUS_15)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                    | Type                                                                                                                                                                                                                         | Required                                                                                                                                                                                                                     | Description                                                                                                                                                                                                                  |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `security`                                                                                                                                                                                                                   | [models.GetV1PayrollDigestsPayrollDigestUUIDSecurity](../../models/getv1payrolldigestspayrolldigestuuidsecurity.md)                                                                                                          | :heavy_check_mark:                                                                                                                                                                                                           | N/A                                                                                                                                                                                                                          |
| `payroll_digest_uuid`                                                                                                                                                                                                        | *str*                                                                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                                           | The UUID of the payroll digest batch returned by `POST /v1/payroll_digests`.                                                                                                                                                 |
| `x_gusto_api_version`                                                                                                                                                                                                        | [Optional[models.GetV1PayrollDigestsPayrollDigestUUIDHeaderXGustoAPIVersion]](../../models/getv1payrolldigestspayrolldigestuuidheaderxgustoapiversion.md)                                                                    | :heavy_minus_sign:                                                                                                                                                                                                           | Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used. |
| `retries`                                                                                                                                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                           | Configuration to override the default retry behavior of the client.                                                                                                                                                          |

### Response

**[models.PayrollDigestResults](../../models/payrolldigestresults.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.NotFoundErrorObject | 404, 410                   | application/json           |
| models.APIError            | 4XX, 5XX                   | \*/\*                      |