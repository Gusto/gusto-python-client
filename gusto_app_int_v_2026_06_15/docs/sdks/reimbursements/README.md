# Reimbursements

## Overview

### Available Operations

* [get_v1_employees_employee_id_recurring_reimbursements](#get_v1_employees_employee_id_recurring_reimbursements) - Get recurring reimbursements for an employee
* [post_v1_employees_employee_id_recurring_reimbursements](#post_v1_employees_employee_id_recurring_reimbursements) - Create a recurring reimbursement
* [get_v1_recurring_reimbursements](#get_v1_recurring_reimbursements) - Get a recurring reimbursement
* [put_v1_recurring_reimbursements](#put_v1_recurring_reimbursements) - Update a recurring reimbursement
* [delete_v1_recurring_reimbursements](#delete_v1_recurring_reimbursements) - Delete a recurring reimbursement

## get_v1_employees_employee_id_recurring_reimbursements

Get all active recurring reimbursements for an employee.

scope: `reimbursements:read`

### Example Usage

<!-- UsageSnippet language="python" operationID="get-v1-employees-employee_id-recurring_reimbursements" method="get" path="/v1/employees/{employee_id}/recurring_reimbursements" -->
```python
import gusto_app_integration_v_2026_06_15
from gusto_app_integration_v_2026_06_15 import GustoAppIntegration


with GustoAppIntegration(
    company_access_auth="<YOUR_BEARER_TOKEN_HERE>",
) as gusto_app_integration:

    res = gusto_app_integration.reimbursements.get_v1_employees_employee_id_recurring_reimbursements(employee_id="<id>", x_gusto_api_version=gusto_app_integration_v_2026_06_15.GetV1EmployeesEmployeeIDRecurringReimbursementsHeaderXGustoAPIVersion.TWO_THOUSAND_AND_TWENTY_SIX_MINUS_06_MINUS_15)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                    | Type                                                                                                                                                                                                                         | Required                                                                                                                                                                                                                     | Description                                                                                                                                                                                                                  |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `employee_id`                                                                                                                                                                                                                | *str*                                                                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                                           | The UUID of the employee                                                                                                                                                                                                     |
| `x_gusto_api_version`                                                                                                                                                                                                        | [Optional[models.GetV1EmployeesEmployeeIDRecurringReimbursementsHeaderXGustoAPIVersion]](../../models/getv1employeesemployeeidrecurringreimbursementsheaderxgustoapiversion.md)                                              | :heavy_minus_sign:                                                                                                                                                                                                           | Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used. |
| `page`                                                                                                                                                                                                                       | *Optional[int]*                                                                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                           | The page that is requested. When unspecified, will load all objects unless endpoint forces pagination.                                                                                                                       |
| `per`                                                                                                                                                                                                                        | *Optional[int]*                                                                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                           | Number of objects per page. For majority of endpoints will default to 25                                                                                                                                                     |
| `retries`                                                                                                                                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                           | Configuration to override the default retry behavior of the client.                                                                                                                                                          |

### Response

**[List[models.RecurringReimbursement]](../../models/.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.NotFoundErrorObject | 404                        | application/json           |
| models.APIError            | 4XX, 5XX                   | \*/\*                      |

## post_v1_employees_employee_id_recurring_reimbursements

Create a recurring reimbursement for an employee.

scope: `reimbursements:write`

### Example Usage

<!-- UsageSnippet language="python" operationID="post-v1-employees-employee_id-recurring_reimbursements" method="post" path="/v1/employees/{employee_id}/recurring_reimbursements" -->
```python
import gusto_app_integration_v_2026_06_15
from gusto_app_integration_v_2026_06_15 import GustoAppIntegration


with GustoAppIntegration(
    company_access_auth="<YOUR_BEARER_TOKEN_HERE>",
) as gusto_app_integration:

    res = gusto_app_integration.reimbursements.post_v1_employees_employee_id_recurring_reimbursements(employee_id="<id>", description="as procrastinate produce provided gracefully huzzah likewise when", amount=2610.77, x_gusto_api_version=gusto_app_integration_v_2026_06_15.PostV1EmployeesEmployeeIDRecurringReimbursementsHeaderXGustoAPIVersion.TWO_THOUSAND_AND_TWENTY_SIX_MINUS_06_MINUS_15)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                    | Type                                                                                                                                                                                                                         | Required                                                                                                                                                                                                                     | Description                                                                                                                                                                                                                  |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `employee_id`                                                                                                                                                                                                                | *str*                                                                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                                           | The UUID of the employee                                                                                                                                                                                                     |
| `description`                                                                                                                                                                                                                | *str*                                                                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                                           | The description of the reimbursement                                                                                                                                                                                         |
| `amount`                                                                                                                                                                                                                     | *float*                                                                                                                                                                                                                      | :heavy_check_mark:                                                                                                                                                                                                           | The dollar amount of the reimbursement                                                                                                                                                                                       |
| `x_gusto_api_version`                                                                                                                                                                                                        | [Optional[models.PostV1EmployeesEmployeeIDRecurringReimbursementsHeaderXGustoAPIVersion]](../../models/postv1employeesemployeeidrecurringreimbursementsheaderxgustoapiversion.md)                                            | :heavy_minus_sign:                                                                                                                                                                                                           | Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used. |
| `retries`                                                                                                                                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                           | Configuration to override the default retry behavior of the client.                                                                                                                                                          |

### Response

**[models.RecurringReimbursement](../../models/recurringreimbursement.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.NotFoundErrorObject | 404, 422                   | application/json           |
| models.APIError            | 4XX, 5XX                   | \*/\*                      |

## get_v1_recurring_reimbursements

Get a specific recurring reimbursement.

scope: `reimbursements:read`

### Example Usage

<!-- UsageSnippet language="python" operationID="get-v1-recurring_reimbursements" method="get" path="/v1/recurring_reimbursements/{id}" -->
```python
import gusto_app_integration_v_2026_06_15
from gusto_app_integration_v_2026_06_15 import GustoAppIntegration


with GustoAppIntegration(
    company_access_auth="<YOUR_BEARER_TOKEN_HERE>",
) as gusto_app_integration:

    res = gusto_app_integration.reimbursements.get_v1_recurring_reimbursements(id="<id>", x_gusto_api_version=gusto_app_integration_v_2026_06_15.GetV1RecurringReimbursementsHeaderXGustoAPIVersion.TWO_THOUSAND_AND_TWENTY_SIX_MINUS_06_MINUS_15)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                    | Type                                                                                                                                                                                                                         | Required                                                                                                                                                                                                                     | Description                                                                                                                                                                                                                  |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `id`                                                                                                                                                                                                                         | *str*                                                                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                                           | The UUID of the reimbursement                                                                                                                                                                                                |
| `x_gusto_api_version`                                                                                                                                                                                                        | [Optional[models.GetV1RecurringReimbursementsHeaderXGustoAPIVersion]](../../models/getv1recurringreimbursementsheaderxgustoapiversion.md)                                                                                    | :heavy_minus_sign:                                                                                                                                                                                                           | Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used. |
| `retries`                                                                                                                                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                           | Configuration to override the default retry behavior of the client.                                                                                                                                                          |

### Response

**[models.RecurringReimbursement](../../models/recurringreimbursement.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.NotFoundErrorObject | 404                        | application/json           |
| models.APIError            | 4XX, 5XX                   | \*/\*                      |

## put_v1_recurring_reimbursements

Update a recurring reimbursement.

scope: `reimbursements:write`

### Example Usage

<!-- UsageSnippet language="python" operationID="put-v1-recurring_reimbursements" method="put" path="/v1/recurring_reimbursements/{id}" -->
```python
import gusto_app_integration_v_2026_06_15
from gusto_app_integration_v_2026_06_15 import GustoAppIntegration


with GustoAppIntegration(
    company_access_auth="<YOUR_BEARER_TOKEN_HERE>",
) as gusto_app_integration:

    res = gusto_app_integration.reimbursements.put_v1_recurring_reimbursements(id="<id>", version="56d00c178bc7393b2a206ed6a86afcb4", x_gusto_api_version=gusto_app_integration_v_2026_06_15.PutV1RecurringReimbursementsHeaderXGustoAPIVersion.TWO_THOUSAND_AND_TWENTY_SIX_MINUS_06_MINUS_15)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                    | Type                                                                                                                                                                                                                         | Required                                                                                                                                                                                                                     | Description                                                                                                                                                                                                                  | Example                                                                                                                                                                                                                      |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `id`                                                                                                                                                                                                                         | *str*                                                                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                                           | The UUID of the reimbursement                                                                                                                                                                                                |                                                                                                                                                                                                                              |
| `version`                                                                                                                                                                                                                    | *str*                                                                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                                           | The current version of the object. See the [versioning guide](https://docs.gusto.com/embedded-payroll/docs/idempotency) for information on how to use this field.                                                            | 56d00c178bc7393b2a206ed6a86afcb4                                                                                                                                                                                             |
| `x_gusto_api_version`                                                                                                                                                                                                        | [Optional[models.PutV1RecurringReimbursementsHeaderXGustoAPIVersion]](../../models/putv1recurringreimbursementsheaderxgustoapiversion.md)                                                                                    | :heavy_minus_sign:                                                                                                                                                                                                           | Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used. |                                                                                                                                                                                                                              |
| `description`                                                                                                                                                                                                                | *Optional[str]*                                                                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                           | The description of the reimbursement                                                                                                                                                                                         |                                                                                                                                                                                                                              |
| `amount`                                                                                                                                                                                                                     | *Optional[float]*                                                                                                                                                                                                            | :heavy_minus_sign:                                                                                                                                                                                                           | The dollar amount of the reimbursement                                                                                                                                                                                       |                                                                                                                                                                                                                              |
| `retries`                                                                                                                                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                           | Configuration to override the default retry behavior of the client.                                                                                                                                                          |                                                                                                                                                                                                                              |

### Response

**[models.RecurringReimbursement](../../models/recurringreimbursement.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.NotFoundErrorObject | 404, 409, 422              | application/json           |
| models.APIError            | 4XX, 5XX                   | \*/\*                      |

## delete_v1_recurring_reimbursements

Delete (soft delete) a recurring reimbursement for an employee.

scope: `reimbursements:write`

### Example Usage

<!-- UsageSnippet language="python" operationID="delete-v1-recurring_reimbursements" method="delete" path="/v1/recurring_reimbursements/{id}" -->
```python
import gusto_app_integration_v_2026_06_15
from gusto_app_integration_v_2026_06_15 import GustoAppIntegration


with GustoAppIntegration(
    company_access_auth="<YOUR_BEARER_TOKEN_HERE>",
) as gusto_app_integration:

    gusto_app_integration.reimbursements.delete_v1_recurring_reimbursements(id="<id>", x_gusto_api_version=gusto_app_integration_v_2026_06_15.DeleteV1RecurringReimbursementsHeaderXGustoAPIVersion.TWO_THOUSAND_AND_TWENTY_SIX_MINUS_06_MINUS_15)

    # Use the SDK ...

```

### Parameters

| Parameter                                                                                                                                                                                                                    | Type                                                                                                                                                                                                                         | Required                                                                                                                                                                                                                     | Description                                                                                                                                                                                                                  |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `id`                                                                                                                                                                                                                         | *str*                                                                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                                           | The UUID of the reimbursement                                                                                                                                                                                                |
| `x_gusto_api_version`                                                                                                                                                                                                        | [Optional[models.DeleteV1RecurringReimbursementsHeaderXGustoAPIVersion]](../../models/deletev1recurringreimbursementsheaderxgustoapiversion.md)                                                                              | :heavy_minus_sign:                                                                                                                                                                                                           | Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used. |
| `retries`                                                                                                                                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                           | Configuration to override the default retry behavior of the client.                                                                                                                                                          |

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.NotFoundErrorObject | 404                        | application/json           |
| models.APIError            | 4XX, 5XX                   | \*/\*                      |