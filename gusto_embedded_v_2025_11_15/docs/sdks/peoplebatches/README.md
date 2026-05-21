# PeopleBatches

## Overview

### Available Operations

* [post_v1_companies_company_id_people_batches](#post_v1_companies_company_id_people_batches) - Create a people batch
* [get_v1_people_batches_people_batch_uuid](#get_v1_people_batches_people_batch_uuid) - Get a people batch

## post_v1_companies_company_id_people_batches

Creates a batch for bulk employee creation.

The batch is processed asynchronously. Use the returned batch UUID to poll for status and results.

scope: `people_batches:write`

### Example Usage

<!-- UsageSnippet language="python" operationID="post-v1-companies-company_id-people_batches" method="post" path="/v1/companies/{company_id}/people_batches" -->
```python
import gusto_embedded_v_2025_11_15
from gusto_embedded_v_2025_11_15 import Gusto
import os


with Gusto(
    company_access_auth=os.getenv("GUSTO_COMPANY_ACCESS_AUTH", ""),
) as gusto:

    res = gusto.people_batches.post_v1_companies_company_id_people_batches(company_id="<id>", idempotency_key="550e8400-e29b-41d4-a716-446655440000", batch_action=gusto_embedded_v_2025_11_15.BatchAction.CREATE, batch=[], x_gusto_api_version=gusto_embedded_v_2025_11_15.PostV1CompaniesCompanyIDPeopleBatchesHeaderXGustoAPIVersion.TWO_THOUSAND_AND_TWENTY_FIVE_MINUS_11_MINUS_15)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                    | Type                                                                                                                                                                                                                         | Required                                                                                                                                                                                                                     | Description                                                                                                                                                                                                                  | Example                                                                                                                                                                                                                      |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `company_id`                                                                                                                                                                                                                 | *str*                                                                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                                           | The UUID of the company                                                                                                                                                                                                      |                                                                                                                                                                                                                              |
| `idempotency_key`                                                                                                                                                                                                            | *str*                                                                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                                           | A unique identifier to ensure idempotency of the batch request                                                                                                                                                               | 550e8400-e29b-41d4-a716-446655440000                                                                                                                                                                                         |
| `batch_action`                                                                                                                                                                                                               | [models.BatchAction](../../models/batchaction.md)                                                                                                                                                                            | :heavy_check_mark:                                                                                                                                                                                                           | The action to perform on the batch                                                                                                                                                                                           | create                                                                                                                                                                                                                       |
| `batch`                                                                                                                                                                                                                      | List[[models.Batch](../../models/batch.md)]                                                                                                                                                                                  | :heavy_check_mark:                                                                                                                                                                                                           | Array of people to create                                                                                                                                                                                                    |                                                                                                                                                                                                                              |
| `x_gusto_api_version`                                                                                                                                                                                                        | [Optional[models.PostV1CompaniesCompanyIDPeopleBatchesHeaderXGustoAPIVersion]](../../models/postv1companiescompanyidpeoplebatchesheaderxgustoapiversion.md)                                                                  | :heavy_minus_sign:                                                                                                                                                                                                           | Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used. |                                                                                                                                                                                                                              |
| `retries`                                                                                                                                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                           | Configuration to override the default retry behavior of the client.                                                                                                                                                          |                                                                                                                                                                                                                              |

### Response

**[models.PeopleBatch](../../models/peoplebatch.md)**

### Errors

| Error Type                       | Status Code                      | Content Type                     |
| -------------------------------- | -------------------------------- | -------------------------------- |
| models.NotFoundErrorObjectError  | 404                              | application/json                 |
| models.PeopleBatchConflictError  | 409                              | application/json                 |
| models.UnprocessableEntityError1 | 422                              | application/json                 |
| models.APIError                  | 4XX, 5XX                         | \*/\*                            |

## get_v1_people_batches_people_batch_uuid

Returns the status and results of a people batch.

Poll this endpoint to check the batch processing status and retrieve results.

scope: `people_batches:read`

### Example Usage

<!-- UsageSnippet language="python" operationID="get-v1-people_batches-people_batch_uuid" method="get" path="/v1/people_batches/{people_batch_uuid}" -->
```python
import gusto_embedded_v_2025_11_15
from gusto_embedded_v_2025_11_15 import Gusto
import os


with Gusto(
    company_access_auth=os.getenv("GUSTO_COMPANY_ACCESS_AUTH", ""),
) as gusto:

    res = gusto.people_batches.get_v1_people_batches_people_batch_uuid(people_batch_uuid="<id>", x_gusto_api_version=gusto_embedded_v_2025_11_15.GetV1PeopleBatchesPeopleBatchUUIDHeaderXGustoAPIVersion.TWO_THOUSAND_AND_TWENTY_FIVE_MINUS_11_MINUS_15)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                    | Type                                                                                                                                                                                                                         | Required                                                                                                                                                                                                                     | Description                                                                                                                                                                                                                  |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `people_batch_uuid`                                                                                                                                                                                                          | *str*                                                                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                                           | The UUID of the people batch                                                                                                                                                                                                 |
| `x_gusto_api_version`                                                                                                                                                                                                        | [Optional[models.GetV1PeopleBatchesPeopleBatchUUIDHeaderXGustoAPIVersion]](../../models/getv1peoplebatchespeoplebatchuuidheaderxgustoapiversion.md)                                                                          | :heavy_minus_sign:                                                                                                                                                                                                           | Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used. |
| `retries`                                                                                                                                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                           | Configuration to override the default retry behavior of the client.                                                                                                                                                          |

### Response

**[models.PeopleBatchResults](../../models/peoplebatchresults.md)**

### Errors

| Error Type                      | Status Code                     | Content Type                    |
| ------------------------------- | ------------------------------- | ------------------------------- |
| models.NotFoundErrorObjectError | 404                             | application/json                |
| models.APIError                 | 4XX, 5XX                        | \*/\*                           |