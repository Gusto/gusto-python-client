# JobsAndCompensations
(*jobs_and_compensations*)

## Overview

### Available Operations

* [create](#create) - Create a job
* [list](#list) - Get jobs for an employee
* [get_compensation](#get_compensation) - Get a compensation

## create

Create a job.

scope: `jobs:write`

### Example Usage

```python
from gusto import Gusto
import os

with Gusto(
    company_access_auth=os.getenv("GUSTO_COMPANY_ACCESS_AUTH", ""),
) as g_client:

    res = g_client.jobs_and_compensations.create(employee_id="<id>", title="Regional Manager", hire_date="2020-12-21")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                                          | Type                                                                                                                                                                                                                                               | Required                                                                                                                                                                                                                                           | Description                                                                                                                                                                                                                                        |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `employee_id`                                                                                                                                                                                                                                      | *str*                                                                                                                                                                                                                                              | :heavy_check_mark:                                                                                                                                                                                                                                 | The UUID of the employee                                                                                                                                                                                                                           |
| `title`                                                                                                                                                                                                                                            | *str*                                                                                                                                                                                                                                              | :heavy_check_mark:                                                                                                                                                                                                                                 | The job title                                                                                                                                                                                                                                      |
| `hire_date`                                                                                                                                                                                                                                        | *str*                                                                                                                                                                                                                                              | :heavy_check_mark:                                                                                                                                                                                                                                 | The date when the employee was hired or rehired for the job.                                                                                                                                                                                       |
| `x_gusto_api_version`                                                                                                                                                                                                                              | [Optional[models.VersionHeader]](../../models/versionheader.md)                                                                                                                                                                                    | :heavy_minus_sign:                                                                                                                                                                                                                                 | Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used.                       |
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

## list

Get all of the jobs that an employee holds.

scope: `jobs:read`

### Example Usage

```python
from gusto import Gusto
import os

with Gusto(
    company_access_auth=os.getenv("GUSTO_COMPANY_ACCESS_AUTH", ""),
) as g_client:

    res = g_client.jobs_and_compensations.list(employee_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                    | Type                                                                                                                                                                                                                         | Required                                                                                                                                                                                                                     | Description                                                                                                                                                                                                                  |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `employee_id`                                                                                                                                                                                                                | *str*                                                                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                                           | The UUID of the employee                                                                                                                                                                                                     |
| `page`                                                                                                                                                                                                                       | *Optional[float]*                                                                                                                                                                                                            | :heavy_minus_sign:                                                                                                                                                                                                           | The page that is requested. When unspecified, will load all objects unless endpoint forces pagination.                                                                                                                       |
| `per`                                                                                                                                                                                                                        | *Optional[float]*                                                                                                                                                                                                            | :heavy_minus_sign:                                                                                                                                                                                                           | Number of objects per page. For majority of endpoints will default to 25                                                                                                                                                     |
| `include`                                                                                                                                                                                                                    | [Optional[models.GetV1EmployeesEmployeeIDJobsQueryParamInclude]](../../models/getv1employeesemployeeidjobsqueryparaminclude.md)                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                           | Available options:<br/>- all_compensations: Include all effective dated compensations for each job instead of only the current compensation                                                                                  |
| `x_gusto_api_version`                                                                                                                                                                                                        | [Optional[models.VersionHeader]](../../models/versionheader.md)                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                           | Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used. |
| `retries`                                                                                                                                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                           | Configuration to override the default retry behavior of the client.                                                                                                                                                          |

### Response

**[List[models.Job]](../../models/.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## get_compensation

Compensations contain information on how much is paid out for a job. Jobs may have many compensations, but only one that is active. The current compensation is the one with the most recent `effective_date`.

scope: `jobs:read`


### Example Usage

```python
from gusto import Gusto
import os

with Gusto(
    company_access_auth=os.getenv("GUSTO_COMPANY_ACCESS_AUTH", ""),
) as g_client:

    res = g_client.jobs_and_compensations.get_compensation(compensation_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                    | Type                                                                                                                                                                                                                         | Required                                                                                                                                                                                                                     | Description                                                                                                                                                                                                                  |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `compensation_id`                                                                                                                                                                                                            | *str*                                                                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                                           | The UUID of the compensation                                                                                                                                                                                                 |
| `x_gusto_api_version`                                                                                                                                                                                                        | [Optional[models.VersionHeader]](../../models/versionheader.md)                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                           | Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used. |
| `retries`                                                                                                                                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                           | Configuration to override the default retry behavior of the client.                                                                                                                                                          |

### Response

**[models.Compensation](../../models/compensation.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |