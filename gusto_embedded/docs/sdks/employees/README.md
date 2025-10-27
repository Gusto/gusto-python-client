# Employees
(*employees*)

## Overview

### Available Operations

* [list](#list) - Get employees of a company
* [create](#create) - Create an employee
* [get_v1_companies_company_id_employees_payment_details](#get_v1_companies_company_id_employees_payment_details) - Get employee payment details for a company
* [create_historical](#create_historical) - Create a historical employee
* [get](#get) - Get an employee
* [update](#update) - Update an employee.
* [delete](#delete) - Delete an onboarding employee
* [get_custom_fields](#get_custom_fields) - Get an employee's custom fields
* [update_onboarding_documents_config](#update_onboarding_documents_config) - Update an employee's onboarding documents config
* [get_onboarding_status](#get_onboarding_status) - Get the employee's onboarding status
* [update_onboarding_status](#update_onboarding_status) - Update the employee's onboarding status
* [get_time_off_activities](#get_time_off_activities) - Get employee time off activities

## list

Get all of the employees, onboarding, active and terminated, for a given company.

scope: `employees:read`


### Example Usage

<!-- UsageSnippet language="python" operationID="get-v1-companies-company_id-employees" method="get" path="/v1/companies/{company_id}/employees" -->
```python
import gusto_embedded
from gusto_embedded import Gusto
import os


with Gusto(
    company_access_auth=os.getenv("GUSTO_COMPANY_ACCESS_AUTH", ""),
) as gusto:

    res = gusto.employees.list(company_id="<id>", x_gusto_api_version=gusto_embedded.GetV1CompaniesCompanyIDEmployeesHeaderXGustoAPIVersion.TWO_THOUSAND_AND_TWENTY_FOUR_MINUS_04_MINUS_01)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                    | Type                                                                                                                                                                                                                         | Required                                                                                                                                                                                                                     | Description                                                                                                                                                                                                                  |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `company_id`                                                                                                                                                                                                                 | *str*                                                                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                                           | The UUID of the company                                                                                                                                                                                                      |
| `x_gusto_api_version`                                                                                                                                                                                                        | [Optional[models.GetV1CompaniesCompanyIDEmployeesHeaderXGustoAPIVersion]](../../models/getv1companiescompanyidemployeesheaderxgustoapiversion.md)                                                                            | :heavy_minus_sign:                                                                                                                                                                                                           | Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used. |
| `location_uuid`                                                                                                                                                                                                              | *Optional[str]*                                                                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                           | Filter employees by a specific primary work location                                                                                                                                                                         |
| `payroll_uuid`                                                                                                                                                                                                               | *Optional[str]*                                                                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                           | Filter employees by a specific payroll                                                                                                                                                                                       |
| `search_term`                                                                                                                                                                                                                | *Optional[str]*                                                                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                           | A string to search for in the object's names                                                                                                                                                                                 |
| `sort_by`                                                                                                                                                                                                                    | *Optional[str]*                                                                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                           | Sort employees by field. Cannot be used with search_term. Options: created_at, name, onboarding_status                                                                                                                       |
| `include`                                                                                                                                                                                                                    | List[[models.Include](../../models/include.md)]                                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                           | Include the requested attribute(s) in each employee response. Multiple options are comma separated.                                                                                                                          |
| `onboarded`                                                                                                                                                                                                                  | *Optional[bool]*                                                                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                           | Filters employees by those who have completed onboarding                                                                                                                                                                     |
| `onboarded_active`                                                                                                                                                                                                           | *Optional[bool]*                                                                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                           | Filters employees who are ready to work (onboarded AND active today)                                                                                                                                                         |
| `terminated`                                                                                                                                                                                                                 | *Optional[bool]*                                                                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                           | Filters employees by those who have been or are scheduled to be terminated                                                                                                                                                   |
| `terminated_today`                                                                                                                                                                                                           | *Optional[bool]*                                                                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                           | Filters employees by those who have been terminated and whose termination is in effect today (excludes active and scheduled to be terminated)                                                                                |
| `uuids`                                                                                                                                                                                                                      | List[*str*]                                                                                                                                                                                                                  | :heavy_minus_sign:                                                                                                                                                                                                           | Optional subset of employees to fetch.                                                                                                                                                                                       |
| `page`                                                                                                                                                                                                                       | *Optional[int]*                                                                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                           | The page that is requested. When unspecified, will load all objects unless endpoint forces pagination.                                                                                                                       |
| `per`                                                                                                                                                                                                                        | *Optional[int]*                                                                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                           | Number of objects per page. For majority of endpoints will default to 25                                                                                                                                                     |
| `retries`                                                                                                                                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                           | Configuration to override the default retry behavior of the client.                                                                                                                                                          |

### Response

**[List[models.ShowEmployees]](../../models/.md)**

### Errors

| Error Type                            | Status Code                           | Content Type                          |
| ------------------------------------- | ------------------------------------- | ------------------------------------- |
| models.UnprocessableEntityErrorObject | 404                                   | application/json                      |
| models.APIError                       | 4XX, 5XX                              | \*/\*                                 |

## create

        Create an employee.

        scope: `employees:manage`


### Example Usage

<!-- UsageSnippet language="python" operationID="post-v1-employees" method="post" path="/v1/companies/{company_id}/employees" -->
```python
import gusto_embedded
from gusto_embedded import Gusto
import os


with Gusto(
    company_access_auth=os.getenv("GUSTO_COMPANY_ACCESS_AUTH", ""),
) as gusto:

    res = gusto.employees.create(company_id="<id>", first_name="Linda", last_name="Kautzer", x_gusto_api_version=gusto_embedded.PostV1EmployeesHeaderXGustoAPIVersion.TWO_THOUSAND_AND_TWENTY_FOUR_MINUS_04_MINUS_01)

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
| `work_email`                                                                                                                                                                                                                 | *Optional[str]*                                                                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                           | The employee's work email address.                                                                                                                                                                                           |
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

## get_v1_companies_company_id_employees_payment_details

Fetches payment details for employees in a given company. Results are paginated.

Use the `employee_uuid` query parameter to filter for a single employee.
Use the `payroll_uuid` query parameter to filter for employees on a specific payroll.
Providing both `employee_uuid` and `payroll_uuid` will result in a 400 error.
An empty array is returned if the company has no employees or if no employees match the filter criteria.

The `encrypted_account_number` in the `splits` array is only visible if the `employee_payment_methods:read:account_number` scope is present.

Base scope: `employee_payment_methods:read`

### Example Usage

<!-- UsageSnippet language="python" operationID="get-v1-companies-company_id-employees-payment_details" method="get" path="/v1/companies/{company_id}/employees/payment_details" -->
```python
import gusto_embedded
from gusto_embedded import Gusto
import os


with Gusto(
    company_access_auth=os.getenv("GUSTO_COMPANY_ACCESS_AUTH", ""),
) as gusto:

    res = gusto.employees.get_v1_companies_company_id_employees_payment_details(company_id="<id>", x_gusto_api_version=gusto_embedded.VersionHeader.TWO_THOUSAND_AND_TWENTY_FOUR_MINUS_04_MINUS_01)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                    | Type                                                                                                                                                                                                                         | Required                                                                                                                                                                                                                     | Description                                                                                                                                                                                                                  |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `company_id`                                                                                                                                                                                                                 | *str*                                                                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                                           | The UUID of the company                                                                                                                                                                                                      |
| `employee_uuid`                                                                                                                                                                                                              | *Optional[str]*                                                                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                           | The UUID of a specific employee to fetch payment details for.                                                                                                                                                                |
| `payroll_uuid`                                                                                                                                                                                                               | *Optional[str]*                                                                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                           | The UUID of a specific payroll to fetch payment details for employees on that payroll.                                                                                                                                       |
| `page`                                                                                                                                                                                                                       | *Optional[int]*                                                                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                           | The page that is requested. When unspecified, will load all objects unless endpoint forces pagination.                                                                                                                       |
| `per`                                                                                                                                                                                                                        | *Optional[int]*                                                                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                           | Number of objects per page. For majority of endpoints will default to 25                                                                                                                                                     |
| `x_gusto_api_version`                                                                                                                                                                                                        | [Optional[models.VersionHeader]](../../models/versionheader.md)                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                           | Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used. |
| `retries`                                                                                                                                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                           | Configuration to override the default retry behavior of the client.                                                                                                                                                          |

### Response

**[List[models.EmployeePaymentDetail]](../../models/.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## create_historical

Create a historical employee, an employee that was previously dismissed from the company in the current year.

scope: `employees:manage`

### Example Usage

<!-- UsageSnippet language="python" operationID="post-v1-historical_employees" method="post" path="/v1/companies/{company_uuid}/historical_employees" -->
```python
from datetime import date
import gusto_embedded
from gusto_embedded import Gusto
import os


with Gusto(
    company_access_auth=os.getenv("GUSTO_COMPANY_ACCESS_AUTH", ""),
) as gusto:

    res = gusto.employees.create_historical(company_uuid="<id>", first_name="Soren", last_name="Kierkegaard", date_of_birth="1995-05-05T00:00:00Z", ssn="123456294", work_address={
        "location_uuid": "1da85d35-1910-4d5e-8e94-39e8cdfe8c9a",
    }, home_address={
        "street_1": "300 3rd Street",
        "street_2": None,
        "city": "San Francisco",
        "state": "CA",
        "zip": "94107",
    }, termination={
        "effective_date": date.fromisoformat("2022-09-15T00:00:00Z"),
    }, job={
        "hire_date": date.fromisoformat("2018-05-09T00:00:00Z"),
    }, x_gusto_api_version=gusto_embedded.VersionHeader.TWO_THOUSAND_AND_TWENTY_FOUR_MINUS_04_MINUS_01, middle_initial="A", preferred_first_name="Angel", employee_state_taxes={
        "wc_covered": True,
        "wc_class_code": "20992",
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                    | Type                                                                                                                                                                                                                         | Required                                                                                                                                                                                                                     | Description                                                                                                                                                                                                                  |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `company_uuid`                                                                                                                                                                                                               | *str*                                                                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                                           | The UUID of the company                                                                                                                                                                                                      |
| `first_name`                                                                                                                                                                                                                 | *str*                                                                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                                           | N/A                                                                                                                                                                                                                          |
| `last_name`                                                                                                                                                                                                                  | *str*                                                                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                                           | N/A                                                                                                                                                                                                                          |
| `date_of_birth`                                                                                                                                                                                                              | *str*                                                                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                                           | N/A                                                                                                                                                                                                                          |
| `ssn`                                                                                                                                                                                                                        | *str*                                                                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                                           | N/A                                                                                                                                                                                                                          |
| `work_address`                                                                                                                                                                                                               | [models.WorkAddress](../../models/workaddress.md)                                                                                                                                                                            | :heavy_check_mark:                                                                                                                                                                                                           | N/A                                                                                                                                                                                                                          |
| `home_address`                                                                                                                                                                                                               | [models.HistoricalEmployeeBodyHomeAddress](../../models/historicalemployeebodyhomeaddress.md)                                                                                                                                | :heavy_check_mark:                                                                                                                                                                                                           | N/A                                                                                                                                                                                                                          |
| `termination`                                                                                                                                                                                                                | [models.HistoricalEmployeeBodyTermination](../../models/historicalemployeebodytermination.md)                                                                                                                                | :heavy_check_mark:                                                                                                                                                                                                           | N/A                                                                                                                                                                                                                          |
| `job`                                                                                                                                                                                                                        | [models.HistoricalEmployeeBodyJob](../../models/historicalemployeebodyjob.md)                                                                                                                                                | :heavy_check_mark:                                                                                                                                                                                                           | N/A                                                                                                                                                                                                                          |
| `x_gusto_api_version`                                                                                                                                                                                                        | [Optional[models.VersionHeader]](../../models/versionheader.md)                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                           | Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used. |
| `middle_initial`                                                                                                                                                                                                             | *Optional[str]*                                                                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                           | N/A                                                                                                                                                                                                                          |
| `preferred_first_name`                                                                                                                                                                                                       | *Optional[str]*                                                                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                           | N/A                                                                                                                                                                                                                          |
| `email`                                                                                                                                                                                                                      | *Optional[str]*                                                                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                           | Optional. If provided, the email address will be saved to the employee.                                                                                                                                                      |
| `employee_state_taxes`                                                                                                                                                                                                       | [Optional[models.EmployeeStateTaxes]](../../models/employeestatetaxes.md)                                                                                                                                                    | :heavy_minus_sign:                                                                                                                                                                                                           | N/A                                                                                                                                                                                                                          |
| `retries`                                                                                                                                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                           | Configuration to override the default retry behavior of the client.                                                                                                                                                          |

### Response

**[models.Employee](../../models/employee.md)**

### Errors

| Error Type                            | Status Code                           | Content Type                          |
| ------------------------------------- | ------------------------------------- | ------------------------------------- |
| models.UnprocessableEntityErrorObject | 422                                   | application/json                      |
| models.APIError                       | 4XX, 5XX                              | \*/\*                                 |

## get

Get an employee.

scope: `employees:read`


### Example Usage

<!-- UsageSnippet language="python" operationID="get-v1-employees" method="get" path="/v1/employees/{employee_id}" -->
```python
import gusto_embedded
from gusto_embedded import Gusto
import os


with Gusto(
    company_access_auth=os.getenv("GUSTO_COMPANY_ACCESS_AUTH", ""),
) as gusto:

    res = gusto.employees.get(employee_id="<id>", x_gusto_api_version=gusto_embedded.GetV1EmployeesHeaderXGustoAPIVersion.TWO_THOUSAND_AND_TWENTY_FOUR_MINUS_04_MINUS_01)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                    | Type                                                                                                                                                                                                                         | Required                                                                                                                                                                                                                     | Description                                                                                                                                                                                                                  |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `employee_id`                                                                                                                                                                                                                | *str*                                                                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                                           | The UUID of the employee                                                                                                                                                                                                     |
| `x_gusto_api_version`                                                                                                                                                                                                        | [Optional[models.GetV1EmployeesHeaderXGustoAPIVersion]](../../models/getv1employeesheaderxgustoapiversion.md)                                                                                                                | :heavy_minus_sign:                                                                                                                                                                                                           | Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used. |
| `include`                                                                                                                                                                                                                    | List[[models.QueryParamInclude](../../models/queryparaminclude.md)]                                                                                                                                                          | :heavy_minus_sign:                                                                                                                                                                                                           | Include the requested attribute(s) in each employee response. Multiple options are comma separated.                                                                                                                          |
| `retries`                                                                                                                                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                           | Configuration to override the default retry behavior of the client.                                                                                                                                                          |

### Response

**[models.Employee](../../models/employee.md)**

### Errors

| Error Type                            | Status Code                           | Content Type                          |
| ------------------------------------- | ------------------------------------- | ------------------------------------- |
| models.UnprocessableEntityErrorObject | 404                                   | application/json                      |
| models.APIError                       | 4XX, 5XX                              | \*/\*                                 |

## update

Update an employee.

scope: `employees:write`


### Example Usage

<!-- UsageSnippet language="python" operationID="put-v1-employees" method="put" path="/v1/employees/{employee_id}" -->
```python
import gusto_embedded
from gusto_embedded import Gusto
import os


with Gusto(
    company_access_auth=os.getenv("GUSTO_COMPANY_ACCESS_AUTH", ""),
) as gusto:

    res = gusto.employees.update(employee_id="<id>", version="56d00c178bc7393b2a206ed6a86afcb4", x_gusto_api_version=gusto_embedded.PutV1EmployeesHeaderXGustoAPIVersion.TWO_THOUSAND_AND_TWENTY_FOUR_MINUS_04_MINUS_01, first_name="Weezy", middle_initial="F", last_name="Baby", email="tunechi@cashmoneyrecords.com", work_email="new.partner.work@example.com", date_of_birth="1991-01-31", ssn="824920233")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                    | Type                                                                                                                                                                                                                         | Required                                                                                                                                                                                                                     | Description                                                                                                                                                                                                                  | Example                                                                                                                                                                                                                      |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `employee_id`                                                                                                                                                                                                                | *str*                                                                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                                           | The UUID of the employee                                                                                                                                                                                                     |                                                                                                                                                                                                                              |
| `version`                                                                                                                                                                                                                    | *str*                                                                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                                           | The current version of the object. See the [versioning guide](https://docs.gusto.com/embedded-payroll/docs/idempotency) for information on how to use this field.                                                            | 56d00c178bc7393b2a206ed6a86afcb4                                                                                                                                                                                             |
| `x_gusto_api_version`                                                                                                                                                                                                        | [Optional[models.PutV1EmployeesHeaderXGustoAPIVersion]](../../models/putv1employeesheaderxgustoapiversion.md)                                                                                                                | :heavy_minus_sign:                                                                                                                                                                                                           | Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used. |                                                                                                                                                                                                                              |
| `first_name`                                                                                                                                                                                                                 | *Optional[str]*                                                                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                           | N/A                                                                                                                                                                                                                          | Weezy                                                                                                                                                                                                                        |
| `middle_initial`                                                                                                                                                                                                             | *OptionalNullable[str]*                                                                                                                                                                                                      | :heavy_minus_sign:                                                                                                                                                                                                           | N/A                                                                                                                                                                                                                          | F                                                                                                                                                                                                                            |
| `last_name`                                                                                                                                                                                                                  | *Optional[str]*                                                                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                           | N/A                                                                                                                                                                                                                          | Baby                                                                                                                                                                                                                         |
| `email`                                                                                                                                                                                                                      | *Optional[str]*                                                                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                           | N/A                                                                                                                                                                                                                          | tunechi@cashmoneyrecords.com                                                                                                                                                                                                 |
| `work_email`                                                                                                                                                                                                                 | *Optional[str]*                                                                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                           | N/A                                                                                                                                                                                                                          | new.partner.work@example.com                                                                                                                                                                                                 |
| `date_of_birth`                                                                                                                                                                                                              | *Optional[str]*                                                                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                           | N/A                                                                                                                                                                                                                          | 1991-01-31                                                                                                                                                                                                                   |
| `ssn`                                                                                                                                                                                                                        | *Optional[str]*                                                                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                           | N/A                                                                                                                                                                                                                          | 824920233                                                                                                                                                                                                                    |
| `preferred_first_name`                                                                                                                                                                                                       | *OptionalNullable[str]*                                                                                                                                                                                                      | :heavy_minus_sign:                                                                                                                                                                                                           | N/A                                                                                                                                                                                                                          |                                                                                                                                                                                                                              |
| `two_percent_shareholder`                                                                                                                                                                                                    | *Optional[bool]*                                                                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                           | Whether the employee is a two percent shareholder of the company. This field only applies to companies with an S-Corp entity type.                                                                                           |                                                                                                                                                                                                                              |
| `retries`                                                                                                                                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                           | Configuration to override the default retry behavior of the client.                                                                                                                                                          |                                                                                                                                                                                                                              |

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

<!-- UsageSnippet language="python" operationID="delete-v1-employee" method="delete" path="/v1/employees/{employee_id}" -->
```python
import gusto_embedded
from gusto_embedded import Gusto
import os


with Gusto(
    company_access_auth=os.getenv("GUSTO_COMPANY_ACCESS_AUTH", ""),
) as gusto:

    gusto.employees.delete(employee_id="<id>", x_gusto_api_version=gusto_embedded.DeleteV1EmployeeHeaderXGustoAPIVersion.TWO_THOUSAND_AND_TWENTY_FOUR_MINUS_04_MINUS_01)

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

<!-- UsageSnippet language="python" operationID="get-v1-employees-employee_id-custom_fields" method="get" path="/v1/employees/{employee_id}/custom_fields" -->
```python
import gusto_embedded
from gusto_embedded import Gusto
import os


with Gusto(
    company_access_auth=os.getenv("GUSTO_COMPANY_ACCESS_AUTH", ""),
) as gusto:

    res = gusto.employees.get_custom_fields(employee_id="<id>", x_gusto_api_version=gusto_embedded.VersionHeader.TWO_THOUSAND_AND_TWENTY_FOUR_MINUS_04_MINUS_01)

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

## update_onboarding_documents_config

Indicate whether to include the Form I-9 for an employee during the onboarding process.

scope: `employees:manage`

### Example Usage

<!-- UsageSnippet language="python" operationID="put-v1-employees-employee_id-onboarding_documents_config" method="put" path="/v1/employees/{employee_id}/onboarding_documents_config" -->
```python
import gusto_embedded
from gusto_embedded import Gusto
import os


with Gusto(
    company_access_auth=os.getenv("GUSTO_COMPANY_ACCESS_AUTH", ""),
) as gusto:

    res = gusto.employees.update_onboarding_documents_config(employee_id="<id>", x_gusto_api_version=gusto_embedded.VersionHeader.TWO_THOUSAND_AND_TWENTY_FOUR_MINUS_04_MINUS_01, i9_document=True)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                    | Type                                                                                                                                                                                                                         | Required                                                                                                                                                                                                                     | Description                                                                                                                                                                                                                  |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `employee_id`                                                                                                                                                                                                                | *str*                                                                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                                           | The UUID of the employee                                                                                                                                                                                                     |
| `x_gusto_api_version`                                                                                                                                                                                                        | [Optional[models.VersionHeader]](../../models/versionheader.md)                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                           | Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used. |
| `i9_document`                                                                                                                                                                                                                | *Optional[bool]*                                                                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                           | Whether to include Form I-9 for an employee during onboarding                                                                                                                                                                |
| `retries`                                                                                                                                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                           | Configuration to override the default retry behavior of the client.                                                                                                                                                          |

### Response

**[models.EmployeeOnboardingDocument](../../models/employeeonboardingdocument.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## get_onboarding_status

# Description
Retrieves an employee's onboarding status. The data returned helps inform the required onboarding steps and respective completion status.

scope: `employees:read`

## onboarding_status

### Admin-facilitated onboarding
| onboarding_status | Description |
|:------------------|------------:|
| `admin_onboarding_incomplete` | Admin needs to complete the full employee-onboarding. |
| `onboarding_completed` | Employee has been fully onboarded and verified. |

### Employee self-onboarding
| onboarding_status | Description |
|:------------------|------------:|
| `admin_onboarding_incomplete` | Admin needs to enter basic information about the employee. |
| `self_onboarding_pending_invite` | Admin has the intention to invite the employee to self-onboard (e.g., marking a checkbox), but the system has not yet sent the invitation. |
| `self_onboarding_invited` | Employee has been sent an invitation to self-onboard. |
| `self_onboarding_invited_started` | Employee has started the self-onboarding process. |
| `self_onboarding_invited_overdue` | Employee's start date has passed, and employee has still not completed self-onboarding. |
| `self_onboarding_completed_by_employee` | Employee has completed entering in their information. The status should be updated via API to "self_onboarding_awaiting_admin_review" from here, once the Admin has started reviewing. |
| `self_onboarding_awaiting_admin_review` | Admin has started to verify the employee's information. |
| `onboarding_completed` | Employee has been fully onboarded and verified. |

## onboarding_steps

| onboarding_steps | Requirement(s) to be completed |
|:-----------------|-------------------------------:|
| `personal_details` | Add employee's first name, last name, email, date of birth, social security number |
| `compensation_details` | Associate employee to a job & compensation. |
| `add_work_address` | Add employee work address. |
| `add_home_address` | Add employee home address. |
| `federal_tax_setup` | Set up federal tax withholdings. |
| `state_tax_setup` | Set up state tax withholdings. |
| `direct_deposit_setup` | (optional) Set up employee's direct deposit. |
| `employee_form_signing` | Employee forms (e.g., W4, direct deposit authorization) are generated & signed. |
| `file_new_hire_report` | File a new hire report for this employee. |
| `admin_review` | Admin reviews & confirms employee details (only required for Employee self-onboarding) |


### Example Usage

<!-- UsageSnippet language="python" operationID="get-v1-employees-employee_id-onboarding_status" method="get" path="/v1/employees/{employee_id}/onboarding_status" -->
```python
import gusto_embedded
from gusto_embedded import Gusto
import os


with Gusto(
    company_access_auth=os.getenv("GUSTO_COMPANY_ACCESS_AUTH", ""),
) as gusto:

    res = gusto.employees.get_onboarding_status(employee_id="<id>", x_gusto_api_version=gusto_embedded.GetV1EmployeesEmployeeIDOnboardingStatusHeaderXGustoAPIVersion.TWO_THOUSAND_AND_TWENTY_FOUR_MINUS_04_MINUS_01)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                    | Type                                                                                                                                                                                                                         | Required                                                                                                                                                                                                                     | Description                                                                                                                                                                                                                  |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `employee_id`                                                                                                                                                                                                                | *str*                                                                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                                           | The UUID of the employee                                                                                                                                                                                                     |
| `x_gusto_api_version`                                                                                                                                                                                                        | [Optional[models.GetV1EmployeesEmployeeIDOnboardingStatusHeaderXGustoAPIVersion]](../../models/getv1employeesemployeeidonboardingstatusheaderxgustoapiversion.md)                                                            | :heavy_minus_sign:                                                                                                                                                                                                           | Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used. |
| `retries`                                                                                                                                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                           | Configuration to override the default retry behavior of the client.                                                                                                                                                          |

### Response

**[models.EmployeeOnboardingStatus](../../models/employeeonboardingstatus.md)**

### Errors

| Error Type                            | Status Code                           | Content Type                          |
| ------------------------------------- | ------------------------------------- | ------------------------------------- |
| models.UnprocessableEntityErrorObject | 404                                   | application/json                      |
| models.APIError                       | 4XX, 5XX                              | \*/\*                                 |

## update_onboarding_status

        scope: `employees:manage`

        Updates an employee's onboarding status.
        Below is a list of valid onboarding status changes depending on the intended action to be performed on behalf of the employee.

        | Action | current onboarding_status | new onboarding_status |
        |:------------------|:------------:|----------:|
        | Mark an employee as self-onboarding | `admin_onboarding_incomplete` | `self_onboarding_pending_invite` |
        | Invite an employee to self-onboard | `admin_onboarding_incomplete` or `self_onboarding_pending_invite` | `self_onboarding_invited` |
        | Cancel an employee's self-onboarding | `self_onboarding_invited` or `self_onboarding_pending_invite` | `admin_onboarding_incomplete` |
        | Review an employee's self-onboarded info | `self_onboarding_completed_by_employee` | `self_onboarding_awaiting_admin_review` |
        | Finish an employee's onboarding | `admin_onboarding_incomplete` or `self_onboarding_awaiting_admin_review` | `onboarding_completed` |


### Example Usage

<!-- UsageSnippet language="python" operationID="put-v1-employees-employee_id-onboarding_status" method="put" path="/v1/employees/{employee_id}/onboarding_status" -->
```python
import gusto_embedded
from gusto_embedded import Gusto
import os


with Gusto(
    company_access_auth=os.getenv("GUSTO_COMPANY_ACCESS_AUTH", ""),
) as gusto:

    res = gusto.employees.update_onboarding_status(employee_id="<id>", onboarding_status=gusto_embedded.PutV1EmployeesEmployeeIDOnboardingStatusOnboardingStatus.ADMIN_ONBOARDING_INCOMPLETE, x_gusto_api_version=gusto_embedded.PutV1EmployeesEmployeeIDOnboardingStatusHeaderXGustoAPIVersion.TWO_THOUSAND_AND_TWENTY_FOUR_MINUS_04_MINUS_01)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                    | Type                                                                                                                                                                                                                         | Required                                                                                                                                                                                                                     | Description                                                                                                                                                                                                                  |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `employee_id`                                                                                                                                                                                                                | *str*                                                                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                                           | The UUID of the employee                                                                                                                                                                                                     |
| `onboarding_status`                                                                                                                                                                                                          | [models.PutV1EmployeesEmployeeIDOnboardingStatusOnboardingStatus](../../models/putv1employeesemployeeidonboardingstatusonboardingstatus.md)                                                                                  | :heavy_check_mark:                                                                                                                                                                                                           | Onboarding status value                                                                                                                                                                                                      |
| `x_gusto_api_version`                                                                                                                                                                                                        | [Optional[models.PutV1EmployeesEmployeeIDOnboardingStatusHeaderXGustoAPIVersion]](../../models/putv1employeesemployeeidonboardingstatusheaderxgustoapiversion.md)                                                            | :heavy_minus_sign:                                                                                                                                                                                                           | Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used. |
| `retries`                                                                                                                                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                           | Configuration to override the default retry behavior of the client.                                                                                                                                                          |

### Response

**[models.EmployeeOnboardingStatus](../../models/employeeonboardingstatus.md)**

### Errors

| Error Type                            | Status Code                           | Content Type                          |
| ------------------------------------- | ------------------------------------- | ------------------------------------- |
| models.UnprocessableEntityErrorObject | 404, 422                              | application/json                      |
| models.APIError                       | 4XX, 5XX                              | \*/\*                                 |

## get_time_off_activities

Get employee time off activities.

scope: `employee_time_off_activities:read`

### Example Usage

<!-- UsageSnippet language="python" operationID="get-version-employees-time_off_activities" method="get" path="/v1/employees/{employee_uuid}/time_off_activities" -->
```python
import gusto_embedded
from gusto_embedded import Gusto
import os


with Gusto(
    company_access_auth=os.getenv("GUSTO_COMPANY_ACCESS_AUTH", ""),
) as gusto:

    res = gusto.employees.get_time_off_activities(employee_uuid="<id>", time_off_type="<value>", x_gusto_api_version=gusto_embedded.VersionHeader.TWO_THOUSAND_AND_TWENTY_FOUR_MINUS_04_MINUS_01)

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