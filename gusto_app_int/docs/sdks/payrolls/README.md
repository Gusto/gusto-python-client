# Payrolls
(*payrolls*)

## Overview

### Available Operations

* [get_for_company](#get_for_company) - Get all payrolls for a company
* [get](#get) - Get a single payroll
* [update](#update) - Update a payroll by ID
* [prepare](#prepare) - Prepare a payroll for update

## get_for_company

Returns a list of payrolls for a company. You can change the payrolls returned by updating the processing_status, payroll_types, start_date, & end_date params.

By default, will return processed, regular payrolls for the past 6 months.

Notes:
* Dollar amounts are returned as string representations of numeric decimals, are represented to the cent.
* end_date can be at most 3 months in the future and start_date and end_date can't be more than 1 year apart.

scope: `payrolls:read`

### Example Usage

```python
import gusto_app_integration
from gusto_app_integration import GustoAppIntegration


with GustoAppIntegration(
    company_access_auth="<YOUR_BEARER_TOKEN_HERE>",
) as gai_client:

    res = gai_client.payrolls.get_for_company(company_id="<id>", sort_order=gusto_app_integration.SortOrder.ASC)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                                                                                            | Type                                                                                                                                                                                                                                                                                                 | Required                                                                                                                                                                                                                                                                                             | Description                                                                                                                                                                                                                                                                                          | Example                                                                                                                                                                                                                                                                                              |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `company_id`                                                                                                                                                                                                                                                                                         | *str*                                                                                                                                                                                                                                                                                                | :heavy_check_mark:                                                                                                                                                                                                                                                                                   | The UUID of the company                                                                                                                                                                                                                                                                              |                                                                                                                                                                                                                                                                                                      |
| `processing_statuses`                                                                                                                                                                                                                                                                                | List[[models.ProcessingStatuses](../../models/processingstatuses.md)]                                                                                                                                                                                                                                | :heavy_minus_sign:                                                                                                                                                                                                                                                                                   | Whether to include processed and/or unprocessed payrolls in the response, defaults to processed, for multiple attributes comma separate the values, i.e. `?processing_statuses=processed,unprocessed`                                                                                                |                                                                                                                                                                                                                                                                                                      |
| `payroll_types`                                                                                                                                                                                                                                                                                      | List[[models.PayrollTypes](../../models/payrolltypes.md)]                                                                                                                                                                                                                                            | :heavy_minus_sign:                                                                                                                                                                                                                                                                                   | Whether to include regular and/or off_cycle payrolls in the response, defaults to regular, for multiple attributes comma separate the values, i.e. `?payroll_types=regular,off_cycle`                                                                                                                |                                                                                                                                                                                                                                                                                                      |
| `include`                                                                                                                                                                                                                                                                                            | List[[models.GetV1CompaniesCompanyIDPayrollsQueryParamInclude](../../models/getv1companiescompanyidpayrollsqueryparaminclude.md)]                                                                                                                                                                    | :heavy_minus_sign:                                                                                                                                                                                                                                                                                   | Include the requested attribute in the response. The risk_blockers option will include submission_blockers and credit_blockers if applicable. In v2023-04-01 totals are no longer included by default. For multiple attributes comma separate the values, i.e. `?include=totals,payroll_status_meta` |                                                                                                                                                                                                                                                                                                      |
| `start_date`                                                                                                                                                                                                                                                                                         | *Optional[str]*                                                                                                                                                                                                                                                                                      | :heavy_minus_sign:                                                                                                                                                                                                                                                                                   | Return payrolls whose pay period is after the start date                                                                                                                                                                                                                                             |                                                                                                                                                                                                                                                                                                      |
| `end_date`                                                                                                                                                                                                                                                                                           | *Optional[str]*                                                                                                                                                                                                                                                                                      | :heavy_minus_sign:                                                                                                                                                                                                                                                                                   | Return payrolls whose pay period is before the end date. If left empty, defaults to today's date.                                                                                                                                                                                                    |                                                                                                                                                                                                                                                                                                      |
| `sort_order`                                                                                                                                                                                                                                                                                         | [Optional[models.SortOrder]](../../models/sortorder.md)                                                                                                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                                                                                                   | A string indicating whether to sort resulting events in ascending (asc) or descending (desc) chronological order. Events are sorted by their `timestamp`. Defaults to asc if left empty.                                                                                                             | asc                                                                                                                                                                                                                                                                                                  |
| `page`                                                                                                                                                                                                                                                                                               | *Optional[int]*                                                                                                                                                                                                                                                                                      | :heavy_minus_sign:                                                                                                                                                                                                                                                                                   | The page that is requested. When unspecified, will load all objects unless endpoint forces pagination.                                                                                                                                                                                               |                                                                                                                                                                                                                                                                                                      |
| `per`                                                                                                                                                                                                                                                                                                | *Optional[int]*                                                                                                                                                                                                                                                                                      | :heavy_minus_sign:                                                                                                                                                                                                                                                                                   | Number of objects per page. For majority of endpoints will default to 25                                                                                                                                                                                                                             |                                                                                                                                                                                                                                                                                                      |
| `x_gusto_api_version`                                                                                                                                                                                                                                                                                | [Optional[models.VersionHeader]](../../models/versionheader.md)                                                                                                                                                                                                                                      | :heavy_minus_sign:                                                                                                                                                                                                                                                                                   | Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used.                                                                         |                                                                                                                                                                                                                                                                                                      |
| `retries`                                                                                                                                                                                                                                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                                                                                                                   | Configuration to override the default retry behavior of the client.                                                                                                                                                                                                                                  |                                                                                                                                                                                                                                                                                                      |

### Response

**[List[models.PayrollMinimal]](../../models/.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## get

Returns a payroll. If payroll is calculated or processed, will return employee_compensations and totals.

Notes:
* Hour and dollar amounts are returned as string representations of numeric decimals.
* Hours are represented to the thousands place; dollar amounts are represented to the cent.
* Every eligible compensation is returned for each employee. If no data has yet be inserted for a given field, it defaults to “0.00” (for fixed amounts) or “0.000” (for hours ).
* To return future payrolls, you must include an `end_date` in the future.
* When include parameter with benefits value is passed, employee_benefits:read scope is required to return benefits
  * Benefits containing PHI are only visible with the `employee_benefits:read:phi` scope

scope: `payrolls:read`

### Example Usage

```python
from gusto_app_integration import GustoAppIntegration


with GustoAppIntegration(
    company_access_auth="<YOUR_BEARER_TOKEN_HERE>",
) as gai_client:

    res = gai_client.payrolls.get(company_id="<id>", payroll_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                    | Type                                                                                                                                                                                                                         | Required                                                                                                                                                                                                                     | Description                                                                                                                                                                                                                  |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `company_id`                                                                                                                                                                                                                 | *str*                                                                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                                           | The UUID of the company                                                                                                                                                                                                      |
| `payroll_id`                                                                                                                                                                                                                 | *str*                                                                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                                           | The UUID of the payroll                                                                                                                                                                                                      |
| `include`                                                                                                                                                                                                                    | List[[models.GetV1CompaniesCompanyIDPayrollsPayrollIDQueryParamInclude](../../models/getv1companiescompanyidpayrollspayrollidqueryparaminclude.md)]                                                                          | :heavy_minus_sign:                                                                                                                                                                                                           | Include the requested attribute in the response, for multiple attributes comma separate the values, i.e. `?include=benefits,deductions,taxes`                                                                                |
| `x_gusto_api_version`                                                                                                                                                                                                        | [Optional[models.VersionHeader]](../../models/versionheader.md)                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                           | Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used. |
| `retries`                                                                                                                                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                           | Configuration to override the default retry behavior of the client.                                                                                                                                                          |

### Response

**[models.Payroll](../../models/payroll.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## update

This endpoint allows you to update information for one or more employees for a specific **unprocessed** payroll.  You can think of the **unprocessed**
payroll object as a template of fields that you can update.  You cannot modify the structure of the payroll object through this endpoint, only values
of the fields included in the payroll.  If you do not include specific employee compensations or fixed/hourly compensations in your request body, they
will not be removed from the payroll.

scope: `payrolls:write`

### Example Usage

```python
from gusto_app_integration import GustoAppIntegration


with GustoAppIntegration(
    company_access_auth="<YOUR_BEARER_TOKEN_HERE>",
) as gai_client:

    res = gai_client.payrolls.update(company_id="<id>", payroll_id="<id>", employee_compensations=[
        {},
        {},
        {},
    ])

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                    | Type                                                                                                                                                                                                                         | Required                                                                                                                                                                                                                     | Description                                                                                                                                                                                                                  |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `company_id`                                                                                                                                                                                                                 | *str*                                                                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                                           | The UUID of the company                                                                                                                                                                                                      |
| `payroll_id`                                                                                                                                                                                                                 | *str*                                                                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                                           | The UUID of the payroll                                                                                                                                                                                                      |
| `employee_compensations`                                                                                                                                                                                                     | List[[models.EmployeeCompensations](../../models/employeecompensations.md)]                                                                                                                                                  | :heavy_check_mark:                                                                                                                                                                                                           | N/A                                                                                                                                                                                                                          |
| `x_gusto_api_version`                                                                                                                                                                                                        | [Optional[models.VersionHeader]](../../models/versionheader.md)                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                           | Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used. |
| `retries`                                                                                                                                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                           | Configuration to override the default retry behavior of the client.                                                                                                                                                          |

### Response

**[models.PayrollPrepared](../../models/payrollprepared.md)**

### Errors

| Error Type                            | Status Code                           | Content Type                          |
| ------------------------------------- | ------------------------------------- | ------------------------------------- |
| models.UnprocessableEntityErrorObject | 422                                   | application/json                      |
| models.APIError                       | 4XX, 5XX                              | \*/\*                                 |

## prepare

This endpoint will build the payroll and get it ready for making updates. This includes adding/removing eligible employees from the Payroll and updating the check_date, payroll_deadline, and payroll_status_meta dates & times.

Notes:
 * Will null out calculated_at & totals if a payroll has already been calculated.
 * Will return the version param used for updating the payroll

scope: `payrolls:write`

### Example Usage

```python
from gusto_app_integration import GustoAppIntegration


with GustoAppIntegration(
    company_access_auth="<YOUR_BEARER_TOKEN_HERE>",
) as gai_client:

    res = gai_client.payrolls.prepare(company_id="<id>", payroll_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                    | Type                                                                                                                                                                                                                         | Required                                                                                                                                                                                                                     | Description                                                                                                                                                                                                                  |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `company_id`                                                                                                                                                                                                                 | *str*                                                                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                                           | The UUID of the company                                                                                                                                                                                                      |
| `payroll_id`                                                                                                                                                                                                                 | *str*                                                                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                                           | The UUID of the payroll                                                                                                                                                                                                      |
| `x_gusto_api_version`                                                                                                                                                                                                        | [Optional[models.VersionHeader]](../../models/versionheader.md)                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                           | Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used. |
| `retries`                                                                                                                                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                           | Configuration to override the default retry behavior of the client.                                                                                                                                                          |

### Response

**[models.PayrollPrepared](../../models/payrollprepared.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |