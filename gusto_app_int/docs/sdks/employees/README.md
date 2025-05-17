# Employees
(*employees*)

## Overview

### Available Operations

* [get](#get) - Get employees of a company
* [create](#create) - Create an employee
* [get_by_id](#get_by_id) - Get an employee
* [update](#update) - Update an employee.
* [delete](#delete) - Delete an onboarding employee
* [get_custom_fields](#get_custom_fields) - Get an employee's custom fields
* [get_time_off_activities](#get_time_off_activities) - Get employee time off activities
* [get_terminations](#get_terminations) - Get terminations for an employee

## get

Get all of the employees, onboarding, active and terminated, for a given company.

scope: `employees:read`


### Example Usage

```python
from gusto_app_integration import GustoAppIntegration


with GustoAppIntegration(
    company_access_auth="<YOUR_BEARER_TOKEN_HERE>",
) as gai_client:

    res = gai_client.employees.get(company_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                                                                                      | Type                                                                                                                                                                                                                                                                                           | Required                                                                                                                                                                                                                                                                                       | Description                                                                                                                                                                                                                                                                                    |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `company_id`                                                                                                                                                                                                                                                                                   | *str*                                                                                                                                                                                                                                                                                          | :heavy_check_mark:                                                                                                                                                                                                                                                                             | The UUID of the company                                                                                                                                                                                                                                                                        |
| `x_gusto_api_version`                                                                                                                                                                                                                                                                          | [Optional[models.GetV1CompaniesCompanyIDEmployeesHeaderXGustoAPIVersion]](../../models/getv1companiescompanyidemployeesheaderxgustoapiversion.md)                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                                                                                             | Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used.                                                                   |
| `search_term`                                                                                                                                                                                                                                                                                  | *Optional[str]*                                                                                                                                                                                                                                                                                | :heavy_minus_sign:                                                                                                                                                                                                                                                                             | A string to search for in the object's names                                                                                                                                                                                                                                                   |
| `include`                                                                                                                                                                                                                                                                                      | List[[models.Include](../../models/include.md)]                                                                                                                                                                                                                                                | :heavy_minus_sign:                                                                                                                                                                                                                                                                             | Include the requested attribute(s) in each employee response, multiple options are comma separated. Available options:<br/>- all_compensations: Include all effective dated compensations for each job instead of only the current compensation<br/>- custom_fields: Include employees' custom fields<br/> |
| `terminated`                                                                                                                                                                                                                                                                                   | *Optional[bool]*                                                                                                                                                                                                                                                                               | :heavy_minus_sign:                                                                                                                                                                                                                                                                             | Filters employees by the provided boolean                                                                                                                                                                                                                                                      |
| `page`                                                                                                                                                                                                                                                                                         | *Optional[int]*                                                                                                                                                                                                                                                                                | :heavy_minus_sign:                                                                                                                                                                                                                                                                             | The page that is requested. When unspecified, will load all objects unless endpoint forces pagination.                                                                                                                                                                                         |
| `per`                                                                                                                                                                                                                                                                                          | *Optional[int]*                                                                                                                                                                                                                                                                                | :heavy_minus_sign:                                                                                                                                                                                                                                                                             | Number of objects per page. For majority of endpoints will default to 25                                                                                                                                                                                                                       |
| `retries`                                                                                                                                                                                                                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                                                               | :heavy_minus_sign:                                                                                                                                                                                                                                                                             | Configuration to override the default retry behavior of the client.                                                                                                                                                                                                                            |

### Response

**[List[models.Employee]](../../models/.md)**

### Errors

| Error Type                            | Status Code                           | Content Type                          |
| ------------------------------------- | ------------------------------------- | ------------------------------------- |
| models.UnprocessableEntityErrorObject | 404                                   | application/json                      |
| models.APIError                       | 4XX, 5XX                              | \*/\*                                 |

## create

        Create an employee.

        scope: `employees:manage`


### Example Usage

```python
from gusto_app_integration import GustoAppIntegration


with GustoAppIntegration(
    company_access_auth="<YOUR_BEARER_TOKEN_HERE>",
) as gai_client:

    res = gai_client.employees.create(company_id="<id>", first_name="Karl", last_name="The Fog")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                    | Type                                                                                                                                                                                                                         | Required                                                                                                                                                                                                                     | Description                                                                                                                                                                                                                  |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `company_id`                                                                                                                                                                                                                 | *str*                                                                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                                           | Company ID                                                                                                                                                                                                                   |
| `first_name`                                                                                                                                                                                                                 | *str*                                                                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                                           | N/A                                                                                                                                                                                                                          |
| `last_name`                                                                                                                                                                                                                  | *str*                                                                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                                           | N/A                                                                                                                                                                                                                          |
| `x_gusto_api_version`                                                                                                                                                                                                        | [Optional[models.PostV1EmployeesHeaderXGustoAPIVersion]](../../models/postv1employeesheaderxgustoapiversion.md)                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                           | Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used. |
| `middle_initial`                                                                                                                                                                                                             | *Optional[str]*                                                                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                           | N/A                                                                                                                                                                                                                          |
| `email`                                                                                                                                                                                                                      | *Optional[str]*                                                                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                           | The employee's personal email address.                                                                                                                                                                                       |
| `date_of_birth`                                                                                                                                                                                                              | [datetime](https://docs.python.org/3/library/datetime.html#datetime-objects)                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                                                                           | N/A                                                                                                                                                                                                                          |
| `ssn`                                                                                                                                                                                                                        | *Optional[str]*                                                                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                           | N/A                                                                                                                                                                                                                          |
| `preferred_first_name`                                                                                                                                                                                                       | *Optional[str]*                                                                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                           | N/A                                                                                                                                                                                                                          |
| `self_onboarding`                                                                                                                                                                                                            | *Optional[bool]*                                                                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                           | If true, employee is expected to self-onboard. If false, payroll admin is expected to enter in the employee's onboarding information                                                                                         |
| `retries`                                                                                                                                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                           | Configuration to override the default retry behavior of the client.                                                                                                                                                          |

### Response

**[models.Employee](../../models/employee.md)**

### Errors

| Error Type                            | Status Code                           | Content Type                          |
| ------------------------------------- | ------------------------------------- | ------------------------------------- |
| models.UnprocessableEntityErrorObject | 404, 422                              | application/json                      |
| models.APIError                       | 4XX, 5XX                              | \*/\*                                 |

## get_by_id

Get an employee.

scope: `employees:read`


### Example Usage

```python
from gusto_app_integration import GustoAppIntegration


with GustoAppIntegration(
    company_access_auth="<YOUR_BEARER_TOKEN_HERE>",
) as gai_client:

    res = gai_client.employees.get_by_id(employee_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                                                                                      | Type                                                                                                                                                                                                                                                                                           | Required                                                                                                                                                                                                                                                                                       | Description                                                                                                                                                                                                                                                                                    |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `employee_id`                                                                                                                                                                                                                                                                                  | *str*                                                                                                                                                                                                                                                                                          | :heavy_check_mark:                                                                                                                                                                                                                                                                             | The UUID of the employee                                                                                                                                                                                                                                                                       |
| `x_gusto_api_version`                                                                                                                                                                                                                                                                          | [Optional[models.GetV1EmployeesHeaderXGustoAPIVersion]](../../models/getv1employeesheaderxgustoapiversion.md)                                                                                                                                                                                  | :heavy_minus_sign:                                                                                                                                                                                                                                                                             | Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used.                                                                   |
| `include`                                                                                                                                                                                                                                                                                      | List[[models.QueryParamInclude](../../models/queryparaminclude.md)]                                                                                                                                                                                                                            | :heavy_minus_sign:                                                                                                                                                                                                                                                                             | Include the requested attribute(s) in each employee response, multiple options are comma separated. Available options:<br/>- all_compensations: Include all effective dated compensations for each job instead of only the current compensation<br/>- custom_fields: Include employees' custom fields<br/> |
| `retries`                                                                                                                                                                                                                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                                                               | :heavy_minus_sign:                                                                                                                                                                                                                                                                             | Configuration to override the default retry behavior of the client.                                                                                                                                                                                                                            |

### Response

**[models.Employee](../../models/employee.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## update

Update an employee.

scope: `employees:write`


### Example Usage

```python
from gusto_app_integration import GustoAppIntegration


with GustoAppIntegration(
    company_access_auth="<YOUR_BEARER_TOKEN_HERE>",
) as gai_client:

    res = gai_client.employees.update(employee_id="<id>", version="9294130ed6ff0c1735ef7b4148c1f320", first_name="Weezy", middle_initial="F", last_name="Baby", email="tunechi@cashmoneyrecords.com", date_of_birth="1991-01-31", ssn="824920233")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                         | Type                                                                                                                                                              | Required                                                                                                                                                          | Description                                                                                                                                                       |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `employee_id`                                                                                                                                                     | *str*                                                                                                                                                             | :heavy_check_mark:                                                                                                                                                | The UUID of the employee                                                                                                                                          |
| `version`                                                                                                                                                         | *str*                                                                                                                                                             | :heavy_check_mark:                                                                                                                                                | The current version of the object. See the [versioning guide](https://docs.gusto.com/embedded-payroll/docs/idempotency) for information on how to use this field. |
| `x_gusto_api_version`                                                                                                                                             | *Optional[str]*                                                                                                                                                   | :heavy_minus_sign:                                                                                                                                                | N/A                                                                                                                                                               |
| `first_name`                                                                                                                                                      | *Optional[str]*                                                                                                                                                   | :heavy_minus_sign:                                                                                                                                                | N/A                                                                                                                                                               |
| `middle_initial`                                                                                                                                                  | *OptionalNullable[str]*                                                                                                                                           | :heavy_minus_sign:                                                                                                                                                | N/A                                                                                                                                                               |
| `last_name`                                                                                                                                                       | *Optional[str]*                                                                                                                                                   | :heavy_minus_sign:                                                                                                                                                | N/A                                                                                                                                                               |
| `email`                                                                                                                                                           | *Optional[str]*                                                                                                                                                   | :heavy_minus_sign:                                                                                                                                                | N/A                                                                                                                                                               |
| `date_of_birth`                                                                                                                                                   | *Optional[str]*                                                                                                                                                   | :heavy_minus_sign:                                                                                                                                                | N/A                                                                                                                                                               |
| `ssn`                                                                                                                                                             | *Optional[str]*                                                                                                                                                   | :heavy_minus_sign:                                                                                                                                                | N/A                                                                                                                                                               |
| `preferred_first_name`                                                                                                                                            | *OptionalNullable[str]*                                                                                                                                           | :heavy_minus_sign:                                                                                                                                                | N/A                                                                                                                                                               |
| `two_percent_shareholder`                                                                                                                                         | *Optional[bool]*                                                                                                                                                  | :heavy_minus_sign:                                                                                                                                                | Whether the employee is a two percent shareholder of the company. This field only applies to companies with an S-Corp entity type.                                |
| `retries`                                                                                                                                                         | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                  | :heavy_minus_sign:                                                                                                                                                | Configuration to override the default retry behavior of the client.                                                                                               |

### Response

**[models.Employee](../../models/employee.md)**

### Errors

| Error Type                            | Status Code                           | Content Type                          |
| ------------------------------------- | ------------------------------------- | ------------------------------------- |
| models.UnprocessableEntityErrorObject | 404, 409, 422                         | application/json                      |
| models.APIError                       | 4XX, 5XX                              | \*/\*                                 |

## delete

Use this endpoint to delete an employee who is in onboarding. Deleting
an onboarded employee is not allowed and will return a 422 response. Please check out the Terminations api
if you need to terminate an onboarded employee.

scope: `employees:manage`


### Example Usage

```python
from gusto_app_integration import GustoAppIntegration


with GustoAppIntegration(
    company_access_auth="<YOUR_BEARER_TOKEN_HERE>",
) as gai_client:

    gai_client.employees.delete(employee_id="<id>")

    # Use the SDK ...

```

### Parameters

| Parameter                                                                                                                                                                                                                    | Type                                                                                                                                                                                                                         | Required                                                                                                                                                                                                                     | Description                                                                                                                                                                                                                  |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `employee_id`                                                                                                                                                                                                                | *str*                                                                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                                           | The UUID of the employee                                                                                                                                                                                                     |
| `x_gusto_api_version`                                                                                                                                                                                                        | [Optional[models.DeleteV1EmployeeHeaderXGustoAPIVersion]](../../models/deletev1employeeheaderxgustoapiversion.md)                                                                                                            | :heavy_minus_sign:                                                                                                                                                                                                           | Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used. |
| `retries`                                                                                                                                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                           | Configuration to override the default retry behavior of the client.                                                                                                                                                          |

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## get_custom_fields

Returns a list of the employee's custom fields.

scope: `employees:read`

### Example Usage

```python
from gusto_app_integration import GustoAppIntegration


with GustoAppIntegration(
    company_access_auth="<YOUR_BEARER_TOKEN_HERE>",
) as gai_client:

    res = gai_client.employees.get_custom_fields(employee_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                    | Type                                                                                                                                                                                                                         | Required                                                                                                                                                                                                                     | Description                                                                                                                                                                                                                  |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `employee_id`                                                                                                                                                                                                                | *str*                                                                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                                           | The UUID of the employee                                                                                                                                                                                                     |
| `page`                                                                                                                                                                                                                       | *Optional[int]*                                                                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                           | The page that is requested. When unspecified, will load all objects unless endpoint forces pagination.                                                                                                                       |
| `per`                                                                                                                                                                                                                        | *Optional[int]*                                                                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                           | Number of objects per page. For majority of endpoints will default to 25                                                                                                                                                     |
| `x_gusto_api_version`                                                                                                                                                                                                        | [Optional[models.VersionHeader]](../../models/versionheader.md)                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                           | Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used. |
| `retries`                                                                                                                                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                           | Configuration to override the default retry behavior of the client.                                                                                                                                                          |

### Response

**[models.GetV1EmployeesEmployeeIDCustomFieldsResponseBody](../../models/getv1employeesemployeeidcustomfieldsresponsebody.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## get_time_off_activities

Get employee time off activities.

scope: `employee_time_off_activities:read`

### Example Usage

```python
from gusto_app_integration import GustoAppIntegration


with GustoAppIntegration(
    company_access_auth="<YOUR_BEARER_TOKEN_HERE>",
) as gai_client:

    res = gai_client.employees.get_time_off_activities(employee_uuid="<id>", time_off_type="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                    | Type                                                                                                                                                                                                                         | Required                                                                                                                                                                                                                     | Description                                                                                                                                                                                                                  |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `employee_uuid`                                                                                                                                                                                                              | *str*                                                                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                                           | The UUID of the employee                                                                                                                                                                                                     |
| `time_off_type`                                                                                                                                                                                                              | *str*                                                                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                                           | The time off type name you want to query data for. ex: 'sick' or 'vacation'                                                                                                                                                  |
| `x_gusto_api_version`                                                                                                                                                                                                        | [Optional[models.VersionHeader]](../../models/versionheader.md)                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                           | Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used. |
| `retries`                                                                                                                                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                           | Configuration to override the default retry behavior of the client.                                                                                                                                                          |

### Response

**[models.TimeOffActivity](../../models/timeoffactivity.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## get_terminations

Terminations are created whenever an employee is scheduled to leave the company. The only things required are an effective date (their last day of work) and whether they should receive their wages in a one-off termination payroll or with the rest of the company.

Note that some states require employees to receive their final wages within 24 hours (unless they consent otherwise,) in which case running a one-off payroll may be the only option.

scope: `employments:read`

### Example Usage

```python
from gusto_app_integration import GustoAppIntegration


with GustoAppIntegration(
    company_access_auth="<YOUR_BEARER_TOKEN_HERE>",
) as gai_client:

    res = gai_client.employees.get_terminations(employee_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                    | Type                                                                                                                                                                                                                         | Required                                                                                                                                                                                                                     | Description                                                                                                                                                                                                                  |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `employee_id`                                                                                                                                                                                                                | *str*                                                                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                                           | The UUID of the employee                                                                                                                                                                                                     |
| `x_gusto_api_version`                                                                                                                                                                                                        | [Optional[models.VersionHeader]](../../models/versionheader.md)                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                           | Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used. |
| `retries`                                                                                                                                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                           | Configuration to override the default retry behavior of the client.                                                                                                                                                          |

### Response

**[List[models.Termination]](../../models/.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |