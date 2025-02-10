# TimeOffPolicies
(*time_off_policies*)

## Overview

### Available Operations

* [get](#get) - Get a time off policy
* [put_time_off_policies_time_off_policy_uuid](#put_time_off_policies_time_off_policy_uuid) - Update a time off policy
* [list](#list) - Get all time off policies
* [post_companies_company_uuid_time_off_policies](#post_companies_company_uuid_time_off_policies) - Create a time off policy
* [put_version_time_off_policies_time_off_policy_uuid_add_employees](#put_version_time_off_policies_time_off_policy_uuid_add_employees) - Add employees to a time off policy
* [put_v1_time_off_policies_time_off_policy_uuid_remove_employees](#put_v1_time_off_policies_time_off_policy_uuid_remove_employees) - Remove employees from a time off policy
* [put_version_time_off_policies_time_off_policy_uuid_balance](#put_version_time_off_policies_time_off_policy_uuid_balance) - Update employee time off hour balances
* [put_v1_time_off_policies_time_off_policy_uuid_deactivate](#put_v1_time_off_policies_time_off_policy_uuid_deactivate) - Deactivate a time off policy

## get

Get a time off policy

scope: `time_off_policies:read`

### Example Usage

```python
from gusto import Gusto
import os

with Gusto(
    company_access_auth=os.getenv("GUSTO_COMPANY_ACCESS_AUTH", ""),
) as g_client:

    res = g_client.time_off_policies.get(time_off_policy_uuid="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                    | Type                                                                                                                                                                                                                         | Required                                                                                                                                                                                                                     | Description                                                                                                                                                                                                                  |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `time_off_policy_uuid`                                                                                                                                                                                                       | *str*                                                                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                                           | The UUID of the company time off policy                                                                                                                                                                                      |
| `x_gusto_api_version`                                                                                                                                                                                                        | [Optional[models.VersionHeader]](../../models/versionheader.md)                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                           | Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used. |
| `retries`                                                                                                                                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                           | Configuration to override the default retry behavior of the client.                                                                                                                                                          |

### Response

**[models.TimeOffPolicy](../../models/timeoffpolicy.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## put_time_off_policies_time_off_policy_uuid

Update a time off policy

scope: `time_off_policies:write`

### Example Usage

```python
import gusto
from gusto import Gusto
import os

with Gusto(
    company_access_auth=os.getenv("GUSTO_COMPANY_ACCESS_AUTH", ""),
) as g_client:

    res = g_client.time_off_policies.put_time_off_policies_time_off_policy_uuid(time_off_policy_uuid="<id>", name="Hourly Vacation Policy", accrual_method=gusto.AccrualMethod.PER_HOUR_PAID, accrual_rate="4.0", accrual_rate_unit="80.0", paid_out_on_termination=True, accrual_waiting_period_days=30, carryover_limit_hours="200.0", max_accrual_hours_per_year="120.0", max_hours="240.0")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                                                                    | Type                                                                                                                                                                                                                                                                         | Required                                                                                                                                                                                                                                                                     | Description                                                                                                                                                                                                                                                                  |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `time_off_policy_uuid`                                                                                                                                                                                                                                                       | *str*                                                                                                                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                                                                                           | The UUID of the company time off policy                                                                                                                                                                                                                                      |
| `x_gusto_api_version`                                                                                                                                                                                                                                                        | [Optional[models.VersionHeader]](../../models/versionheader.md)                                                                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                                                                           | Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used.                                                 |
| `name`                                                                                                                                                                                                                                                                       | *Optional[str]*                                                                                                                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                                                                           | Name of the time off policy                                                                                                                                                                                                                                                  |
| `accrual_method`                                                                                                                                                                                                                                                             | [Optional[models.AccrualMethod]](../../models/accrualmethod.md)                                                                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                                                                           | Accrual method of the time off policy                                                                                                                                                                                                                                        |
| `accrual_rate`                                                                                                                                                                                                                                                               | *Optional[str]*                                                                                                                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                                                                           | The rate at which the time off hours will accrue for an employee on the policy. Represented as a float, e.g. "40.0".                                                                                                                                                         |
| `accrual_rate_unit`                                                                                                                                                                                                                                                          | *Optional[str]*                                                                                                                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                                                                           | The number of hours an employee has to work or be paid for to accrue the number of hours set in the accrual rate. Only used for hourly policies (per_hour_paid, per_hour_paid_no_overtime, per_hour_work, per_hour_worked_no_overtime). Represented as a float, e.g. "40.0". |
| `paid_out_on_termination`                                                                                                                                                                                                                                                    | *Optional[bool]*                                                                                                                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                                                                           | Boolean representing if an employee's accrued time off hours will be paid out on termination                                                                                                                                                                                 |
| `accrual_waiting_period_days`                                                                                                                                                                                                                                                | *Optional[int]*                                                                                                                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                                                                           | Number of days before an employee on the policy will begin accruing time off hours. If accrual_method is per_anniversary_year, per_calendar_year, or unlimited, then accrual_waiting_period_days should be 0.                                                                |
| `carryover_limit_hours`                                                                                                                                                                                                                                                      | *Optional[str]*                                                                                                                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                                                                           | The max number of hours an employee can carryover from one year to the next. If accrual_method is unlimited, then carryover_limit_hours must be blank.                                                                                                                       |
| `max_accrual_hours_per_year`                                                                                                                                                                                                                                                 | *Optional[str]*                                                                                                                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                                                                           | The max number of hours an employee can accrue in a year. If accrual_method is unlimited, then max_accrual_hours_per_year must be blank.                                                                                                                                     |
| `max_hours`                                                                                                                                                                                                                                                                  | *Optional[str]*                                                                                                                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                                                                           | The max number of hours an employee can accrue. If accrual_method is unlimited, then max_hours must be blank.                                                                                                                                                                |
| `retries`                                                                                                                                                                                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                                                                           | Configuration to override the default retry behavior of the client.                                                                                                                                                                                                          |

### Response

**[models.TimeOffPolicy](../../models/timeoffpolicy.md)**

### Errors

| Error Type                            | Status Code                           | Content Type                          |
| ------------------------------------- | ------------------------------------- | ------------------------------------- |
| models.UnprocessableEntityErrorObject | 422                                   | application/json                      |
| models.APIError                       | 4XX, 5XX                              | \*/\*                                 |

## list

Get all time off policies for a company

scope: `time_off_policies:read`

### Example Usage

```python
from gusto import Gusto
import os

with Gusto(
    company_access_auth=os.getenv("GUSTO_COMPANY_ACCESS_AUTH", ""),
) as g_client:

    res = g_client.time_off_policies.list(company_uuid="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                    | Type                                                                                                                                                                                                                         | Required                                                                                                                                                                                                                     | Description                                                                                                                                                                                                                  |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `company_uuid`                                                                                                                                                                                                               | *str*                                                                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                                           | The UUID of the company                                                                                                                                                                                                      |
| `x_gusto_api_version`                                                                                                                                                                                                        | [Optional[models.VersionHeader]](../../models/versionheader.md)                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                           | Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used. |
| `retries`                                                                                                                                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                           | Configuration to override the default retry behavior of the client.                                                                                                                                                          |

### Response

**[List[models.TimeOffPolicy]](../../models/.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## post_companies_company_uuid_time_off_policies

Create a time off policy

scope: `time_off_policies:write`

### Example Usage

```python
import gusto
from gusto import Gusto
import os

with Gusto(
    company_access_auth=os.getenv("GUSTO_COMPANY_ACCESS_AUTH", ""),
) as g_client:

    res = g_client.time_off_policies.post_companies_company_uuid_time_off_policies(company_uuid="<id>", name="Unlimited Vacation Policy", policy_type="vacation", accrual_method=gusto.PostCompaniesCompanyUUIDTimeOffPoliciesAccrualMethod.UNLIMITED)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                                                                    | Type                                                                                                                                                                                                                                                                         | Required                                                                                                                                                                                                                                                                     | Description                                                                                                                                                                                                                                                                  |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `company_uuid`                                                                                                                                                                                                                                                               | *str*                                                                                                                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                                                                                           | The UUID of the company                                                                                                                                                                                                                                                      |
| `name`                                                                                                                                                                                                                                                                       | *str*                                                                                                                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                                                                                           | Name of the time off policy                                                                                                                                                                                                                                                  |
| `policy_type`                                                                                                                                                                                                                                                                | *str*                                                                                                                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                                                                                           | Type of the time off policy. Currently only "vacation" and "sick" are supported                                                                                                                                                                                              |
| `accrual_method`                                                                                                                                                                                                                                                             | [models.PostCompaniesCompanyUUIDTimeOffPoliciesAccrualMethod](../../models/postcompaniescompanyuuidtimeoffpoliciesaccrualmethod.md)                                                                                                                                          | :heavy_check_mark:                                                                                                                                                                                                                                                           | Accrual method of the time off policy                                                                                                                                                                                                                                        |
| `x_gusto_api_version`                                                                                                                                                                                                                                                        | [Optional[models.VersionHeader]](../../models/versionheader.md)                                                                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                                                                           | Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used.                                                 |
| `accrual_rate`                                                                                                                                                                                                                                                               | *Optional[str]*                                                                                                                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                                                                           | The rate at which the time off hours will accrue for an employee on the policy. Represented as a float, e.g. "40.0".                                                                                                                                                         |
| `accrual_rate_unit`                                                                                                                                                                                                                                                          | *Optional[str]*                                                                                                                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                                                                           | The number of hours an employee has to work or be paid for to accrue the number of hours set in the accrual rate. Only used for hourly policies (per_hour_paid, per_hour_paid_no_overtime, per_hour_work, per_hour_worked_no_overtime). Represented as a float, e.g. "40.0". |
| `paid_out_on_termination`                                                                                                                                                                                                                                                    | *Optional[bool]*                                                                                                                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                                                                           | Boolean representing if an employee's accrued time off hours will be paid out on termination                                                                                                                                                                                 |
| `accrual_waiting_period_days`                                                                                                                                                                                                                                                | *Optional[int]*                                                                                                                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                                                                           | Number of days before an employee on the policy will begin accruing time off hours. If accrual_method is per_anniversary_year, per_calendar_year, or unlimited, then accrual_waiting_period_days should be 0.                                                                |
| `carryover_limit_hours`                                                                                                                                                                                                                                                      | *Optional[str]*                                                                                                                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                                                                           | The max number of hours an employee can carryover from one year to the next. If accrual_method is unlimited, then carryover_limit_hours must be blank.                                                                                                                       |
| `max_accrual_hours_per_year`                                                                                                                                                                                                                                                 | *Optional[str]*                                                                                                                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                                                                           | The max number of hours an employee can accrue in a year. If accrual_method is unlimited, then max_accrual_hours_per_year must be blank.                                                                                                                                     |
| `max_hours`                                                                                                                                                                                                                                                                  | *Optional[str]*                                                                                                                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                                                                           | The max number of hours an employee can accrue. If accrual_method is unlimited, then max_hours must be blank.                                                                                                                                                                |
| `retries`                                                                                                                                                                                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                                                                           | Configuration to override the default retry behavior of the client.                                                                                                                                                                                                          |

### Response

**[models.TimeOffPolicy](../../models/timeoffpolicy.md)**

### Errors

| Error Type                            | Status Code                           | Content Type                          |
| ------------------------------------- | ------------------------------------- | ------------------------------------- |
| models.UnprocessableEntityErrorObject | 422                                   | application/json                      |
| models.APIError                       | 4XX, 5XX                              | \*/\*                                 |

## put_version_time_off_policies_time_off_policy_uuid_add_employees

Add employees to a time off policy. Employees are required to have at least one job to be added to a time off policy. Accepts starting balances for non-unlimited policies

scope: `time_off_policies:write`

### Example Usage

```python
from gusto import Gusto
import os

with Gusto(
    company_access_auth=os.getenv("GUSTO_COMPANY_ACCESS_AUTH", ""),
) as g_client:

    res = g_client.time_off_policies.put_version_time_off_policies_time_off_policy_uuid_add_employees(time_off_policy_uuid="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                    | Type                                                                                                                                                                                                                         | Required                                                                                                                                                                                                                     | Description                                                                                                                                                                                                                  |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `time_off_policy_uuid`                                                                                                                                                                                                       | *str*                                                                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                                           | The UUID of the company time off policy                                                                                                                                                                                      |
| `x_gusto_api_version`                                                                                                                                                                                                        | [Optional[models.VersionHeader]](../../models/versionheader.md)                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                           | Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used. |
| `employees`                                                                                                                                                                                                                  | List[[models.PutVersionTimeOffPoliciesTimeOffPolicyUUIDAddEmployeesEmployees](../../models/putversiontimeoffpoliciestimeoffpolicyuuidaddemployeesemployees.md)]                                                              | :heavy_minus_sign:                                                                                                                                                                                                           | N/A                                                                                                                                                                                                                          |
| `retries`                                                                                                                                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                           | Configuration to override the default retry behavior of the client.                                                                                                                                                          |

### Response

**[models.TimeOffPolicy](../../models/timeoffpolicy.md)**

### Errors

| Error Type                            | Status Code                           | Content Type                          |
| ------------------------------------- | ------------------------------------- | ------------------------------------- |
| models.UnprocessableEntityErrorObject | 422                                   | application/json                      |
| models.APIError                       | 4XX, 5XX                              | \*/\*                                 |

## put_v1_time_off_policies_time_off_policy_uuid_remove_employees

Remove employees from a time off policy

scope: `time_off_policies:write`

### Example Usage

```python
from gusto import Gusto
import os

with Gusto(
    company_access_auth=os.getenv("GUSTO_COMPANY_ACCESS_AUTH", ""),
) as g_client:

    res = g_client.time_off_policies.put_v1_time_off_policies_time_off_policy_uuid_remove_employees(time_off_policy_uuid="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                    | Type                                                                                                                                                                                                                         | Required                                                                                                                                                                                                                     | Description                                                                                                                                                                                                                  |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `time_off_policy_uuid`                                                                                                                                                                                                       | *str*                                                                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                                           | The UUID of the company time off policy                                                                                                                                                                                      |
| `x_gusto_api_version`                                                                                                                                                                                                        | [Optional[models.VersionHeader]](../../models/versionheader.md)                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                           | Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used. |
| `employees`                                                                                                                                                                                                                  | List[[models.PutV1TimeOffPoliciesTimeOffPolicyUUIDRemoveEmployeesEmployees](../../models/putv1timeoffpoliciestimeoffpolicyuuidremoveemployeesemployees.md)]                                                                  | :heavy_minus_sign:                                                                                                                                                                                                           | N/A                                                                                                                                                                                                                          |
| `retries`                                                                                                                                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                           | Configuration to override the default retry behavior of the client.                                                                                                                                                          |

### Response

**[models.TimeOffPolicy](../../models/timeoffpolicy.md)**

### Errors

| Error Type                            | Status Code                           | Content Type                          |
| ------------------------------------- | ------------------------------------- | ------------------------------------- |
| models.UnprocessableEntityErrorObject | 422                                   | application/json                      |
| models.APIError                       | 4XX, 5XX                              | \*/\*                                 |

## put_version_time_off_policies_time_off_policy_uuid_balance

Updates time off hours balances for employees for a time off policy

scope: `time_off_policies:write`

### Example Usage

```python
from gusto import Gusto
import os

with Gusto(
    company_access_auth=os.getenv("GUSTO_COMPANY_ACCESS_AUTH", ""),
) as g_client:

    res = g_client.time_off_policies.put_version_time_off_policies_time_off_policy_uuid_balance(time_off_policy_uuid="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                    | Type                                                                                                                                                                                                                         | Required                                                                                                                                                                                                                     | Description                                                                                                                                                                                                                  |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `time_off_policy_uuid`                                                                                                                                                                                                       | *str*                                                                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                                           | The UUID of the company time off policy                                                                                                                                                                                      |
| `x_gusto_api_version`                                                                                                                                                                                                        | [Optional[models.VersionHeader]](../../models/versionheader.md)                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                           | Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used. |
| `employees`                                                                                                                                                                                                                  | List[[models.PutVersionTimeOffPoliciesTimeOffPolicyUUIDBalanceEmployees](../../models/putversiontimeoffpoliciestimeoffpolicyuuidbalanceemployees.md)]                                                                        | :heavy_minus_sign:                                                                                                                                                                                                           | N/A                                                                                                                                                                                                                          |
| `retries`                                                                                                                                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                           | Configuration to override the default retry behavior of the client.                                                                                                                                                          |

### Response

**[models.TimeOffPolicy](../../models/timeoffpolicy.md)**

### Errors

| Error Type                            | Status Code                           | Content Type                          |
| ------------------------------------- | ------------------------------------- | ------------------------------------- |
| models.UnprocessableEntityErrorObject | 422                                   | application/json                      |
| models.APIError                       | 4XX, 5XX                              | \*/\*                                 |

## put_v1_time_off_policies_time_off_policy_uuid_deactivate

Deactivate a time off policy

scope: `time_off_policies:write`

### Example Usage

```python
from gusto import Gusto
import os

with Gusto(
    company_access_auth=os.getenv("GUSTO_COMPANY_ACCESS_AUTH", ""),
) as g_client:

    res = g_client.time_off_policies.put_v1_time_off_policies_time_off_policy_uuid_deactivate(time_off_policy_uuid="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                    | Type                                                                                                                                                                                                                         | Required                                                                                                                                                                                                                     | Description                                                                                                                                                                                                                  |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `time_off_policy_uuid`                                                                                                                                                                                                       | *str*                                                                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                                           | The UUID of the company time off policy                                                                                                                                                                                      |
| `x_gusto_api_version`                                                                                                                                                                                                        | [Optional[models.VersionHeader]](../../models/versionheader.md)                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                           | Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used. |
| `retries`                                                                                                                                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                           | Configuration to override the default retry behavior of the client.                                                                                                                                                          |

### Response

**[models.TimeOffPolicy](../../models/timeoffpolicy.md)**

### Errors

| Error Type                            | Status Code                           | Content Type                          |
| ------------------------------------- | ------------------------------------- | ------------------------------------- |
| models.UnprocessableEntityErrorObject | 422                                   | application/json                      |
| models.APIError                       | 4XX, 5XX                              | \*/\*                                 |