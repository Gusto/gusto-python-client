# Jobs
(*jobs*)

## Overview

### Available Operations

* [get](#get) - Get a job
* [put_v1_jobs_job_id](#put_v1_jobs_job_id) - Update a job
* [delete](#delete) - Delete an individual job
* [get_v1_jobs_job_id_compensations](#get_v1_jobs_job_id_compensations) - Get compensations for a job

## get

Get a job.

scope: `jobs:read`

### Example Usage

```python
from gusto_embedded import Gusto
import os

with Gusto(
    company_access_auth=os.getenv("GUSTO_COMPANY_ACCESS_AUTH", ""),
) as gusto:

    res = gusto.jobs.get(job_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                    | Type                                                                                                                                                                                                                         | Required                                                                                                                                                                                                                     | Description                                                                                                                                                                                                                  |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `job_id`                                                                                                                                                                                                                     | *str*                                                                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                                           | The UUID of the job                                                                                                                                                                                                          |
| `include`                                                                                                                                                                                                                    | [Optional[models.GetV1JobsJobIDQueryParamInclude]](../../models/getv1jobsjobidqueryparaminclude.md)                                                                                                                          | :heavy_minus_sign:                                                                                                                                                                                                           | Available options:<br/>- all_compensations: Include all effective dated compensations for the job instead of only the current compensation                                                                                   |
| `x_gusto_api_version`                                                                                                                                                                                                        | [Optional[models.VersionHeader]](../../models/versionheader.md)                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                           | Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used. |
| `retries`                                                                                                                                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                           | Configuration to override the default retry behavior of the client.                                                                                                                                                          |

### Response

**[models.Job](../../models/job.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## put_v1_jobs_job_id

Update a job.

scope: `jobs:write`

### Example Usage

```python
from gusto_embedded import Gusto
import os

with Gusto(
    company_access_auth=os.getenv("GUSTO_COMPANY_ACCESS_AUTH", ""),
) as gusto:

    res = gusto.jobs.put_v1_jobs_job_id(job_id="<id>", version="gr78930htutrz444kuytr3s5hgxykuveb523fwl8sir", title="Regional Manager", hire_date="2020-12-21")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                                          | Type                                                                                                                                                                                                                                               | Required                                                                                                                                                                                                                                           | Description                                                                                                                                                                                                                                        |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `job_id`                                                                                                                                                                                                                                           | *str*                                                                                                                                                                                                                                              | :heavy_check_mark:                                                                                                                                                                                                                                 | The UUID of the job                                                                                                                                                                                                                                |
| `version`                                                                                                                                                                                                                                          | *str*                                                                                                                                                                                                                                              | :heavy_check_mark:                                                                                                                                                                                                                                 | The current version of the object. See the [versioning guide](https://docs.gusto.com/embedded-payroll/docs/versioning#object-layer) for information on how to use this field.                                                                      |
| `x_gusto_api_version`                                                                                                                                                                                                                              | [Optional[models.VersionHeader]](../../models/versionheader.md)                                                                                                                                                                                    | :heavy_minus_sign:                                                                                                                                                                                                                                 | Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used.                       |
| `title`                                                                                                                                                                                                                                            | *Optional[str]*                                                                                                                                                                                                                                    | :heavy_minus_sign:                                                                                                                                                                                                                                 | The job title                                                                                                                                                                                                                                      |
| `hire_date`                                                                                                                                                                                                                                        | *Optional[str]*                                                                                                                                                                                                                                    | :heavy_minus_sign:                                                                                                                                                                                                                                 | The date when the employee was hired or rehired for the job.                                                                                                                                                                                       |
| `two_percent_shareholder`                                                                                                                                                                                                                          | *Optional[bool]*                                                                                                                                                                                                                                   | :heavy_minus_sign:                                                                                                                                                                                                                                 | Whether the employee owns at least 2% of the company.                                                                                                                                                                                              |
| `state_wc_covered`                                                                                                                                                                                                                                 | *OptionalNullable[bool]*                                                                                                                                                                                                                           | :heavy_minus_sign:                                                                                                                                                                                                                                 | Whether this job is eligible for workers' compensation coverage in the state of Washington (WA).                                                                                                                                                   |
| `state_wc_class_code`                                                                                                                                                                                                                              | *OptionalNullable[str]*                                                                                                                                                                                                                            | :heavy_minus_sign:                                                                                                                                                                                                                                 | The risk class code for workers' compensation in Washington state. Please visit [Washington state's Risk Class page](https://www.lni.wa.gov/insurance/rates-risk-classes/risk-classes-for-workers-compensation/risk-class-lookup#/) to learn more. |
| `retries`                                                                                                                                                                                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                   | :heavy_minus_sign:                                                                                                                                                                                                                                 | Configuration to override the default retry behavior of the client.                                                                                                                                                                                |

### Response

**[models.Job](../../models/job.md)**

### Errors

| Error Type                            | Status Code                           | Content Type                          |
| ------------------------------------- | ------------------------------------- | ------------------------------------- |
| models.UnprocessableEntityErrorObject | 422                                   | application/json                      |
| models.APIError                       | 4XX, 5XX                              | \*/\*                                 |

## delete

Deletes a specific job that an employee holds.

scope: `jobs:write`

### Example Usage

```python
from gusto_embedded import Gusto
import os

with Gusto(
    company_access_auth=os.getenv("GUSTO_COMPANY_ACCESS_AUTH", ""),
) as gusto:

    gusto.jobs.delete(job_id="<id>")

    # Use the SDK ...

```

### Parameters

| Parameter                                                                                                                                                                                                                    | Type                                                                                                                                                                                                                         | Required                                                                                                                                                                                                                     | Description                                                                                                                                                                                                                  |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `job_id`                                                                                                                                                                                                                     | *str*                                                                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                                           | The UUID of the job                                                                                                                                                                                                          |
| `x_gusto_api_version`                                                                                                                                                                                                        | [Optional[models.VersionHeader]](../../models/versionheader.md)                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                           | Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used. |
| `retries`                                                                                                                                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                           | Configuration to override the default retry behavior of the client.                                                                                                                                                          |

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## get_v1_jobs_job_id_compensations

Compensations contain information on how much is paid out for a job. Jobs may have many compensations, but only one that is active. The current compensation is the one with the most recent `effective_date`. By default the API returns only the current compensation - see the `include` query parameter for retrieving all compensations.

Note: Currently the API does not support creating multiple compensations per job - creating a compensation with the same `job_uuid` as another will fail with a relevant error.

Use `flsa_status` to determine if an employee is eligible for overtime.

scope: `jobs:read`

### Example Usage

```python
from gusto_embedded import Gusto
import os

with Gusto(
    company_access_auth=os.getenv("GUSTO_COMPANY_ACCESS_AUTH", ""),
) as gusto:

    res = gusto.jobs.get_v1_jobs_job_id_compensations(job_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                    | Type                                                                                                                                                                                                                         | Required                                                                                                                                                                                                                     | Description                                                                                                                                                                                                                  |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `job_id`                                                                                                                                                                                                                     | *str*                                                                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                                           | The UUID of the job                                                                                                                                                                                                          |
| `page`                                                                                                                                                                                                                       | *Optional[float]*                                                                                                                                                                                                            | :heavy_minus_sign:                                                                                                                                                                                                           | The page that is requested. When unspecified, will load all objects unless endpoint forces pagination.                                                                                                                       |
| `per`                                                                                                                                                                                                                        | *Optional[float]*                                                                                                                                                                                                            | :heavy_minus_sign:                                                                                                                                                                                                           | Number of objects per page. For majority of endpoints will default to 25                                                                                                                                                     |
| `include`                                                                                                                                                                                                                    | [Optional[models.GetV1JobsJobIDCompensationsQueryParamInclude]](../../models/getv1jobsjobidcompensationsqueryparaminclude.md)                                                                                                | :heavy_minus_sign:                                                                                                                                                                                                           | Available options:<br/>- all_compensations: Include all effective dated compensations for each job instead of only the current compensation                                                                                  |
| `x_gusto_api_version`                                                                                                                                                                                                        | [Optional[models.VersionHeader]](../../models/versionheader.md)                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                           | Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used. |
| `retries`                                                                                                                                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                           | Configuration to override the default retry behavior of the client.                                                                                                                                                          |

### Response

**[List[models.Compensation]](../../models/.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |