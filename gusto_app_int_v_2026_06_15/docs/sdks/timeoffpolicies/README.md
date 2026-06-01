# TimeOffPolicies

## Overview

### Available Operations

* [calculate_accruing_time_off_hours](#calculate_accruing_time_off_hours) - Calculate accruing time off hours
* [get_v1_companies_company_uuid_time_off_policies](#get_v1_companies_company_uuid_time_off_policies) - Get all time off policies for a company
* [get_v1_time_off_policies_time_off_policy_uuid](#get_v1_time_off_policies_time_off_policy_uuid) - Get a time off policy
* [put_v1_time_off_policies_time_off_policy_uuid_add_employees](#put_v1_time_off_policies_time_off_policy_uuid_add_employees) - Add employees to a time off policy

## calculate_accruing_time_off_hours

Returns a list of accruing time off for each time off policy associated with the employee.

Factors affecting the accrued hours:

- the time off policy accrual method (whether they get pay per hour worked, per hour paid, with / without overtime, accumulate time off based on pay period / calendar year / anniversary)
- how many hours of work during this pay period
- how many hours of PTO / sick hours taken during this pay period (for per hour paid policies only)
- company pay schedule frequency (for per pay period)

If none of the parameters is passed in, the accrued time off hour will be 0.

scope: `payrolls:read`

### Example Usage

<!-- UsageSnippet language="python" operationID="post-v1-payrolls-payroll_id-calculate_accruing_time_off_hours" method="post" path="/v1/payrolls/{payroll_id}/employees/{employee_id}/calculate_accruing_time_off_hours" -->
```python
import gusto_app_integration_v_2026_06_15
from gusto_app_integration_v_2026_06_15 import GustoAppIntegration


with GustoAppIntegration(
    company_access_auth="<YOUR_BEARER_TOKEN_HERE>",
) as gusto_app_integration:

    res = gusto_app_integration.time_off_policies.calculate_accruing_time_off_hours(payroll_id="<id>", employee_id="<id>", x_gusto_api_version=gusto_app_integration_v_2026_06_15.PostV1PayrollsPayrollIDCalculateAccruingTimeOffHoursHeaderXGustoAPIVersion.TWO_THOUSAND_AND_TWENTY_SIX_MINUS_06_MINUS_15)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                    | Type                                                                                                                                                                                                                         | Required                                                                                                                                                                                                                     | Description                                                                                                                                                                                                                  |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `payroll_id`                                                                                                                                                                                                                 | *str*                                                                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                                           | The UUID of the payroll                                                                                                                                                                                                      |
| `employee_id`                                                                                                                                                                                                                | *str*                                                                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                                           | The UUID of the employee                                                                                                                                                                                                     |
| `x_gusto_api_version`                                                                                                                                                                                                        | [Optional[models.PostV1PayrollsPayrollIDCalculateAccruingTimeOffHoursHeaderXGustoAPIVersion]](../../models/postv1payrollspayrollidcalculateaccruingtimeoffhoursheaderxgustoapiversion.md)                                    | :heavy_minus_sign:                                                                                                                                                                                                           | Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used. |
| `regular_hours_worked`                                                                                                                                                                                                       | *OptionalNullable[str]*                                                                                                                                                                                                      | :heavy_minus_sign:                                                                                                                                                                                                           | Regular hours worked in this pay period                                                                                                                                                                                      |
| `overtime_hours_worked`                                                                                                                                                                                                      | *OptionalNullable[str]*                                                                                                                                                                                                      | :heavy_minus_sign:                                                                                                                                                                                                           | Overtime hours worked in this pay period                                                                                                                                                                                     |
| `double_overtime_hours_worked`                                                                                                                                                                                               | *OptionalNullable[str]*                                                                                                                                                                                                      | :heavy_minus_sign:                                                                                                                                                                                                           | Double overtime hours worked in this pay period                                                                                                                                                                              |
| `pto_hours_used`                                                                                                                                                                                                             | *OptionalNullable[str]*                                                                                                                                                                                                      | :heavy_minus_sign:                                                                                                                                                                                                           | Paid time off hours used in this pay period                                                                                                                                                                                  |
| `sick_hours_used`                                                                                                                                                                                                            | *OptionalNullable[str]*                                                                                                                                                                                                      | :heavy_minus_sign:                                                                                                                                                                                                           | Sick hours used in this pay period                                                                                                                                                                                           |
| `retries`                                                                                                                                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                           | Configuration to override the default retry behavior of the client.                                                                                                                                                          |

### Response

**[models.PayrollCalculateAccruingTimeOffHoursResponse](../../models/payrollcalculateaccruingtimeoffhoursresponse.md)**

### Errors

| Error Type                            | Status Code                           | Content Type                          |
| ------------------------------------- | ------------------------------------- | ------------------------------------- |
| models.NotFoundErrorObject            | 404                                   | application/json                      |
| models.UnprocessableEntityErrorObject | 422                                   | application/json                      |
| models.APIError                       | 4XX, 5XX                              | \*/\*                                 |

## get_v1_companies_company_uuid_time_off_policies

Get all time off policies for a company

scope: `time_off_policies:read`

### Example Usage

<!-- UsageSnippet language="python" operationID="get-v1-companies-company_uuid-time_off_policies" method="get" path="/v1/companies/{company_uuid}/time_off_policies" -->
```python
import gusto_app_integration_v_2026_06_15
from gusto_app_integration_v_2026_06_15 import GustoAppIntegration


with GustoAppIntegration(
    company_access_auth="<YOUR_BEARER_TOKEN_HERE>",
) as gusto_app_integration:

    res = gusto_app_integration.time_off_policies.get_v1_companies_company_uuid_time_off_policies(company_uuid="<id>", x_gusto_api_version=gusto_app_integration_v_2026_06_15.GetV1CompaniesCompanyUUIDTimeOffPoliciesHeaderXGustoAPIVersion.TWO_THOUSAND_AND_TWENTY_SIX_MINUS_06_MINUS_15)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                    | Type                                                                                                                                                                                                                         | Required                                                                                                                                                                                                                     | Description                                                                                                                                                                                                                  |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `company_uuid`                                                                                                                                                                                                               | *str*                                                                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                                           | The UUID of the company                                                                                                                                                                                                      |
| `x_gusto_api_version`                                                                                                                                                                                                        | [Optional[models.GetV1CompaniesCompanyUUIDTimeOffPoliciesHeaderXGustoAPIVersion]](../../models/getv1companiescompanyuuidtimeoffpoliciesheaderxgustoapiversion.md)                                                            | :heavy_minus_sign:                                                                                                                                                                                                           | Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used. |
| `retries`                                                                                                                                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                           | Configuration to override the default retry behavior of the client.                                                                                                                                                          |

### Response

**[List[models.TimeOffPolicy]](../../models/.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.NotFoundErrorObject | 404                        | application/json           |
| models.APIError            | 4XX, 5XX                   | \*/\*                      |

## get_v1_time_off_policies_time_off_policy_uuid

Get a time off policy

scope: `time_off_policies:read`

### Example Usage

<!-- UsageSnippet language="python" operationID="get-v1-time_off_policies-time_off_policy_uuid" method="get" path="/v1/time_off_policies/{time_off_policy_uuid}" -->
```python
import gusto_app_integration_v_2026_06_15
from gusto_app_integration_v_2026_06_15 import GustoAppIntegration


with GustoAppIntegration(
    company_access_auth="<YOUR_BEARER_TOKEN_HERE>",
) as gusto_app_integration:

    res = gusto_app_integration.time_off_policies.get_v1_time_off_policies_time_off_policy_uuid(time_off_policy_uuid="<id>", x_gusto_api_version=gusto_app_integration_v_2026_06_15.GetV1TimeOffPoliciesTimeOffPolicyUUIDHeaderXGustoAPIVersion.TWO_THOUSAND_AND_TWENTY_SIX_MINUS_06_MINUS_15)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                    | Type                                                                                                                                                                                                                         | Required                                                                                                                                                                                                                     | Description                                                                                                                                                                                                                  |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `time_off_policy_uuid`                                                                                                                                                                                                       | *str*                                                                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                                           | The UUID of the time off policy                                                                                                                                                                                              |
| `x_gusto_api_version`                                                                                                                                                                                                        | [Optional[models.GetV1TimeOffPoliciesTimeOffPolicyUUIDHeaderXGustoAPIVersion]](../../models/getv1timeoffpoliciestimeoffpolicyuuidheaderxgustoapiversion.md)                                                                  | :heavy_minus_sign:                                                                                                                                                                                                           | Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used. |
| `retries`                                                                                                                                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                           | Configuration to override the default retry behavior of the client.                                                                                                                                                          |

### Response

**[models.TimeOffPolicy](../../models/timeoffpolicy.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.NotFoundErrorObject | 404                        | application/json           |
| models.APIError            | 4XX, 5XX                   | \*/\*                      |

## put_v1_time_off_policies_time_off_policy_uuid_add_employees

Add employees to a time off policy. Employees are required to have at least one job to be added to a time off policy. Accepts starting balances for non-unlimited policies

scope: `time_off_policies:write`

### Example Usage

<!-- UsageSnippet language="python" operationID="put-v1-time_off_policies-time_off_policy_uuid-add_employees" method="put" path="/v1/time_off_policies/{time_off_policy_uuid}/add_employees" -->
```python
import gusto_app_integration_v_2026_06_15
from gusto_app_integration_v_2026_06_15 import GustoAppIntegration


with GustoAppIntegration(
    company_access_auth="<YOUR_BEARER_TOKEN_HERE>",
) as gusto_app_integration:

    res = gusto_app_integration.time_off_policies.put_v1_time_off_policies_time_off_policy_uuid_add_employees(time_off_policy_uuid="<id>", employees=[], x_gusto_api_version=gusto_app_integration_v_2026_06_15.PutV1TimeOffPoliciesTimeOffPolicyUUIDAddEmployeesHeaderXGustoAPIVersion.TWO_THOUSAND_AND_TWENTY_SIX_MINUS_06_MINUS_15)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                    | Type                                                                                                                                                                                                                         | Required                                                                                                                                                                                                                     | Description                                                                                                                                                                                                                  |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `time_off_policy_uuid`                                                                                                                                                                                                       | *str*                                                                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                                           | The UUID of the time off policy                                                                                                                                                                                              |
| `employees`                                                                                                                                                                                                                  | List[[models.PutV1TimeOffPoliciesTimeOffPolicyUUIDAddEmployeesEmployees](../../models/putv1timeoffpoliciestimeoffpolicyuuidaddemployeesemployees.md)]                                                                        | :heavy_check_mark:                                                                                                                                                                                                           | N/A                                                                                                                                                                                                                          |
| `x_gusto_api_version`                                                                                                                                                                                                        | [Optional[models.PutV1TimeOffPoliciesTimeOffPolicyUUIDAddEmployeesHeaderXGustoAPIVersion]](../../models/putv1timeoffpoliciestimeoffpolicyuuidaddemployeesheaderxgustoapiversion.md)                                          | :heavy_minus_sign:                                                                                                                                                                                                           | Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used. |
| `retries`                                                                                                                                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                           | Configuration to override the default retry behavior of the client.                                                                                                                                                          |

### Response

**[models.TimeOffPolicy](../../models/timeoffpolicy.md)**

### Errors

| Error Type                            | Status Code                           | Content Type                          |
| ------------------------------------- | ------------------------------------- | ------------------------------------- |
| models.NotFoundErrorObject            | 404                                   | application/json                      |
| models.UnprocessableEntityErrorObject | 422                                   | application/json                      |
| models.APIError                       | 4XX, 5XX                              | \*/\*                                 |