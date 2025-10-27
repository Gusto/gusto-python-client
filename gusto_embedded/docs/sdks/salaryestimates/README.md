# SalaryEstimates
(*salary_estimates*)

## Overview

### Available Operations

* [post_v1_employees_employee_id_salary_estimates](#post_v1_employees_employee_id_salary_estimates) - Create a salary estimate for an employee
* [get_v1_salary_estimates_id](#get_v1_salary_estimates_id) - Get a salary estimate
* [put_v1_salary_estimates_id](#put_v1_salary_estimates_id) - Update a salary estimate
* [post_v1_salary_estimates_uuid_accept](#post_v1_salary_estimates_uuid_accept) - Accept a salary estimate
* [get_v1_salary_estimates_occupations](#get_v1_salary_estimates_occupations) - Search for BLS occupations

## post_v1_employees_employee_id_salary_estimates

Create a salary estimate for an employee. This endpoint helps calculate a reasonable salary for S Corp owners based on their occupation, experience level, location, and business revenue.

A salary estimate must include:
- Annual net revenue of the business
- ZIP code for location-based salary data
- One or more occupations with experience levels and time percentages (must sum to 100%)

Only one in-progress salary estimate can exist per employee at a time. If an in-progress estimate already exists, you must either accept it or use the update endpoint.

scope: `salary_estimates:write`


### Example Usage

<!-- UsageSnippet language="python" operationID="post-v1-employees-employee_id-salary_estimates" method="post" path="/v1/employees/{employee_id}/salary_estimates" -->
```python
import gusto_embedded
from gusto_embedded import Gusto
import os


with Gusto(
    company_access_auth=os.getenv("GUSTO_COMPANY_ACCESS_AUTH", ""),
) as gusto:

    res = gusto.salary_estimates.post_v1_employees_employee_id_salary_estimates(employee_id="<id>", zip_code="94107", occupations=[], x_gusto_api_version=gusto_embedded.PostV1EmployeesEmployeeIDSalaryEstimatesHeaderXGustoAPIVersion.TWO_THOUSAND_AND_TWENTY_FOUR_MINUS_04_MINUS_01, annual_net_revenue=500000)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                    | Type                                                                                                                                                                                                                         | Required                                                                                                                                                                                                                     | Description                                                                                                                                                                                                                  | Example                                                                                                                                                                                                                      |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `employee_id`                                                                                                                                                                                                                | *str*                                                                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                                           | The UUID of the employee                                                                                                                                                                                                     |                                                                                                                                                                                                                              |
| `zip_code`                                                                                                                                                                                                                   | *str*                                                                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                                           | The ZIP code for location-based salary calculations                                                                                                                                                                          | 94107                                                                                                                                                                                                                        |
| `occupations`                                                                                                                                                                                                                | List[[models.PostV1EmployeesEmployeeIDSalaryEstimatesOccupations](../../models/postv1employeesemployeeidsalaryestimatesoccupations.md)]                                                                                      | :heavy_check_mark:                                                                                                                                                                                                           | Array of occupations. Time percentages must sum to 100%.                                                                                                                                                                     |                                                                                                                                                                                                                              |
| `x_gusto_api_version`                                                                                                                                                                                                        | [Optional[models.PostV1EmployeesEmployeeIDSalaryEstimatesHeaderXGustoAPIVersion]](../../models/postv1employeesemployeeidsalaryestimatesheaderxgustoapiversion.md)                                                            | :heavy_minus_sign:                                                                                                                                                                                                           | Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used. |                                                                                                                                                                                                                              |
| `annual_net_revenue`                                                                                                                                                                                                         | *OptionalNullable[float]*                                                                                                                                                                                                    | :heavy_minus_sign:                                                                                                                                                                                                           | The annual net revenue of the business (must be greater than 0)                                                                                                                                                              | 500000                                                                                                                                                                                                                       |
| `retries`                                                                                                                                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                           | Configuration to override the default retry behavior of the client.                                                                                                                                                          |                                                                                                                                                                                                                              |

### Response

**[models.SalaryEstimate](../../models/salaryestimate.md)**

### Errors

| Error Type                            | Status Code                           | Content Type                          |
| ------------------------------------- | ------------------------------------- | ------------------------------------- |
| models.UnprocessableEntityErrorObject | 404, 422                              | application/json                      |
| models.APIError                       | 4XX, 5XX                              | \*/\*                                 |

## get_v1_salary_estimates_id

Retrieve a salary estimate by its UUID. Returns the estimated salary calculation along with all occupation details, revenue, and location information.

scope: `salary_estimates:read`


### Example Usage

<!-- UsageSnippet language="python" operationID="get-v1-salary_estimates-id" method="get" path="/v1/salary_estimates/{uuid}" -->
```python
import gusto_embedded
from gusto_embedded import Gusto
import os


with Gusto(
    company_access_auth=os.getenv("GUSTO_COMPANY_ACCESS_AUTH", ""),
) as gusto:

    res = gusto.salary_estimates.get_v1_salary_estimates_id(uuid="3c9d1f7e-adda-44fb-ba0e-7e5843661514", x_gusto_api_version=gusto_embedded.GetV1SalaryEstimatesIDHeaderXGustoAPIVersion.TWO_THOUSAND_AND_TWENTY_FOUR_MINUS_04_MINUS_01)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                    | Type                                                                                                                                                                                                                         | Required                                                                                                                                                                                                                     | Description                                                                                                                                                                                                                  |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `uuid`                                                                                                                                                                                                                       | *str*                                                                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                                           | The UUID of the salary estimate                                                                                                                                                                                              |
| `x_gusto_api_version`                                                                                                                                                                                                        | [Optional[models.GetV1SalaryEstimatesIDHeaderXGustoAPIVersion]](../../models/getv1salaryestimatesidheaderxgustoapiversion.md)                                                                                                | :heavy_minus_sign:                                                                                                                                                                                                           | Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used. |
| `retries`                                                                                                                                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                           | Configuration to override the default retry behavior of the client.                                                                                                                                                          |

### Response

**[models.SalaryEstimate](../../models/salaryestimate.md)**

### Errors

| Error Type                            | Status Code                           | Content Type                          |
| ------------------------------------- | ------------------------------------- | ------------------------------------- |
| models.UnprocessableEntityErrorObject | 404                                   | application/json                      |
| models.APIError                       | 4XX, 5XX                              | \*/\*                                 |

## put_v1_salary_estimates_id

Update an existing salary estimate. You can modify the annual net revenue, ZIP code, and occupations.

The salary estimate must not be finalized (accepted). Once accepted, salary estimates become read-only for record-keeping purposes.

scope: `salary_estimates:write`


### Example Usage

<!-- UsageSnippet language="python" operationID="put-v1-salary_estimates-id" method="put" path="/v1/salary_estimates/{uuid}" -->
```python
import gusto_embedded
from gusto_embedded import Gusto
import os


with Gusto(
    company_access_auth=os.getenv("GUSTO_COMPANY_ACCESS_AUTH", ""),
) as gusto:

    res = gusto.salary_estimates.put_v1_salary_estimates_id(uuid="969f5dac-57dd-4091-b195-2546171d3a76", zip_code="94107", occupations=[
        {
            "code": "151252",
            "experience_level": gusto_embedded.PutV1SalaryEstimatesIDExperienceLevel.EXPERT,
            "time_percentage": "0.6",
            "primary": True,
        },
    ], x_gusto_api_version=gusto_embedded.PutV1SalaryEstimatesIDHeaderXGustoAPIVersion.TWO_THOUSAND_AND_TWENTY_FOUR_MINUS_04_MINUS_01, annual_net_revenue=600000)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                    | Type                                                                                                                                                                                                                         | Required                                                                                                                                                                                                                     | Description                                                                                                                                                                                                                  | Example                                                                                                                                                                                                                      |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `uuid`                                                                                                                                                                                                                       | *str*                                                                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                                           | The UUID of the salary estimate                                                                                                                                                                                              |                                                                                                                                                                                                                              |
| `zip_code`                                                                                                                                                                                                                   | *str*                                                                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                                           | The ZIP code for location-based salary calculations                                                                                                                                                                          | 94107                                                                                                                                                                                                                        |
| `occupations`                                                                                                                                                                                                                | List[[models.PutV1SalaryEstimatesIDOccupations](../../models/putv1salaryestimatesidoccupations.md)]                                                                                                                          | :heavy_check_mark:                                                                                                                                                                                                           | Array of occupations. Time percentages must sum to 100%.                                                                                                                                                                     |                                                                                                                                                                                                                              |
| `x_gusto_api_version`                                                                                                                                                                                                        | [Optional[models.PutV1SalaryEstimatesIDHeaderXGustoAPIVersion]](../../models/putv1salaryestimatesidheaderxgustoapiversion.md)                                                                                                | :heavy_minus_sign:                                                                                                                                                                                                           | Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used. |                                                                                                                                                                                                                              |
| `annual_net_revenue`                                                                                                                                                                                                         | *OptionalNullable[float]*                                                                                                                                                                                                    | :heavy_minus_sign:                                                                                                                                                                                                           | The annual net revenue of the business (must be greater than 0)                                                                                                                                                              | 600000                                                                                                                                                                                                                       |
| `retries`                                                                                                                                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                           | Configuration to override the default retry behavior of the client.                                                                                                                                                          |                                                                                                                                                                                                                              |

### Response

**[models.SalaryEstimate](../../models/salaryestimate.md)**

### Errors

| Error Type                            | Status Code                           | Content Type                          |
| ------------------------------------- | ------------------------------------- | ------------------------------------- |
| models.UnprocessableEntityErrorObject | 404, 422                              | application/json                      |
| models.APIError                       | 4XX, 5XX                              | \*/\*                                 |

## post_v1_salary_estimates_uuid_accept

Accept and finalize a salary estimate. This associates the estimate with an employee job and marks it as accepted.

Once accepted, the salary estimate becomes read-only for record-keeping purposes. The accepted salary can then be used to set up compensation for the employee.

scope: `salary_estimates:write`


### Example Usage

<!-- UsageSnippet language="python" operationID="post-v1-salary_estimates-uuid-accept" method="post" path="/v1/salary_estimates/{uuid}/accept" -->
```python
import gusto_embedded
from gusto_embedded import Gusto
import os


with Gusto(
    company_access_auth=os.getenv("GUSTO_COMPANY_ACCESS_AUTH", ""),
) as gusto:

    res = gusto.salary_estimates.post_v1_salary_estimates_uuid_accept(uuid="22c00075-fa4c-4bdc-91e3-f72ab8ec7a1d", employee_job_uuid="7f5d3d93-6d6f-48c0-9f4e-cd12c2d3e4b2", x_gusto_api_version=gusto_embedded.PostV1SalaryEstimatesUUIDAcceptHeaderXGustoAPIVersion.TWO_THOUSAND_AND_TWENTY_FOUR_MINUS_04_MINUS_01)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                    | Type                                                                                                                                                                                                                         | Required                                                                                                                                                                                                                     | Description                                                                                                                                                                                                                  | Example                                                                                                                                                                                                                      |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `uuid`                                                                                                                                                                                                                       | *str*                                                                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                                           | The UUID of the salary estimate                                                                                                                                                                                              |                                                                                                                                                                                                                              |
| `employee_job_uuid`                                                                                                                                                                                                          | *str*                                                                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                                           | The UUID of the employee job to associate with this salary estimate                                                                                                                                                          | 7f5d3d93-6d6f-48c0-9f4e-cd12c2d3e4b2                                                                                                                                                                                         |
| `x_gusto_api_version`                                                                                                                                                                                                        | [Optional[models.PostV1SalaryEstimatesUUIDAcceptHeaderXGustoAPIVersion]](../../models/postv1salaryestimatesuuidacceptheaderxgustoapiversion.md)                                                                              | :heavy_minus_sign:                                                                                                                                                                                                           | Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used. |                                                                                                                                                                                                                              |
| `retries`                                                                                                                                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                           | Configuration to override the default retry behavior of the client.                                                                                                                                                          |                                                                                                                                                                                                                              |

### Response

**[models.SalaryEstimate](../../models/salaryestimate.md)**

### Errors

| Error Type                            | Status Code                           | Content Type                          |
| ------------------------------------- | ------------------------------------- | ------------------------------------- |
| models.UnprocessableEntityErrorObject | 404, 422                              | application/json                      |
| models.APIError                       | 4XX, 5XX                              | \*/\*                                 |

## get_v1_salary_estimates_occupations

Search for Bureau of Labor Statistics (BLS) occupations by name or keyword. This endpoint helps users find the appropriate occupation codes to use when creating or updating salary estimates.

Returns a list of matching occupations with their codes, titles, and descriptions.

U0001F4D8 System Access Authentication

This endpoint uses the [Bearer Auth scheme with the system-level access token in the HTTP Authorization header](https://docs.gusto.com/embedded-payroll/docs/system-access)

scope: `salary_estimates:read`


### Example Usage

<!-- UsageSnippet language="python" operationID="get-v1-salary_estimates-occupations" method="get" path="/v1/salary_estimates/occupations" -->
```python
import gusto_embedded
from gusto_embedded import Gusto
import os


with Gusto() as gusto:

    res = gusto.salary_estimates.get_v1_salary_estimates_occupations(security=gusto_embedded.GetV1SalaryEstimatesOccupationsSecurity(
        system_access_auth=os.getenv("GUSTO_SYSTEM_ACCESS_AUTH", ""),
    ), search="software", x_gusto_api_version=gusto_embedded.GetV1SalaryEstimatesOccupationsHeaderXGustoAPIVersion.TWO_THOUSAND_AND_TWENTY_FOUR_MINUS_04_MINUS_01)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                    | Type                                                                                                                                                                                                                         | Required                                                                                                                                                                                                                     | Description                                                                                                                                                                                                                  | Example                                                                                                                                                                                                                      |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `security`                                                                                                                                                                                                                   | [models.GetV1SalaryEstimatesOccupationsSecurity](../../models/getv1salaryestimatesoccupationssecurity.md)                                                                                                                    | :heavy_check_mark:                                                                                                                                                                                                           | N/A                                                                                                                                                                                                                          |                                                                                                                                                                                                                              |
| `search`                                                                                                                                                                                                                     | *str*                                                                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                                           | Search term for occupation (minimum 3 characters)                                                                                                                                                                            | software                                                                                                                                                                                                                     |
| `x_gusto_api_version`                                                                                                                                                                                                        | [Optional[models.GetV1SalaryEstimatesOccupationsHeaderXGustoAPIVersion]](../../models/getv1salaryestimatesoccupationsheaderxgustoapiversion.md)                                                                              | :heavy_minus_sign:                                                                                                                                                                                                           | Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used. |                                                                                                                                                                                                                              |
| `retries`                                                                                                                                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                           | Configuration to override the default retry behavior of the client.                                                                                                                                                          |                                                                                                                                                                                                                              |

### Response

**[List[models.BLSOccupation]](../../models/.md)**

### Errors

| Error Type                            | Status Code                           | Content Type                          |
| ------------------------------------- | ------------------------------------- | ------------------------------------- |
| models.UnprocessableEntityErrorObject | 422                                   | application/json                      |
| models.APIError                       | 4XX, 5XX                              | \*/\*                                 |