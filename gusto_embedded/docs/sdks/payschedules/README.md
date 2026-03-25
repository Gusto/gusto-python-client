# PaySchedules

## Overview

### Available Operations

* [create](#create) - Create a new pay schedule
* [get_all](#get_all) - Get the pay schedules for a company
* [get_preview](#get_preview) - Preview pay schedule dates
* [get](#get) - Get a pay schedule
* [update](#update) - Update a pay schedule
* [get_pay_periods](#get_pay_periods) - Get pay periods for a company
* [get_unprocessed_termination_periods](#get_unprocessed_termination_periods) - Get termination pay periods for a company
* [get_assignments](#get_assignments) - Get pay schedule assignments for a company
* [preview_assignment](#preview_assignment) - Preview pay schedule assignments for a company
* [assign](#assign) - Assign pay schedules for a company

## create

If a company does not have any pay schedules, this endpoint creates a single pay schedule and assigns it to all employees (common during company onboarding).

If a company already has an active pay schedule and wants multiple pay schedules, this endpoint creates a pay schedule that is not assigned to any employee.

Be sure to [check state laws](https://www.dol.gov/agencies/whd/state/payday) to know what schedule is right for your customers. If an onboarded company misses their first pay date, the pay schedule may be automatically adjusted.

### Webhooks
- `pay_schedule.created`: Fires when a pay schedule is successfully created.

### Related guides
- [Create a pay schedule](doc:create-a-pay-schedule)
- [Pay Schedules](doc:pay-schedule-info)
- [Manage Pay Schedules via API](doc:manage-pay-schedules-api)

scope: `pay_schedules:write`

### Example Usage

<!-- UsageSnippet language="python" operationID="post-v1-companies-company_id-pay_schedules" method="post" path="/v1/companies/{company_id}/pay_schedules" -->
```python
from datetime import date
import gusto_embedded
from gusto_embedded import Gusto
import os


with Gusto(
    company_access_auth=os.getenv("GUSTO_COMPANY_ACCESS_AUTH", ""),
) as gusto:

    res = gusto.pay_schedules.create(company_id="<id>", frequency=gusto_embedded.PayScheduleFrequencyCreateUpdate.EVERY_WEEK, anchor_pay_date=date.fromisoformat("2026-02-12"), anchor_end_of_pay_period=date.fromisoformat("2025-08-20"), x_gusto_api_version=gusto_embedded.PostV1CompaniesCompanyIDPaySchedulesHeaderXGustoAPIVersion.TWO_THOUSAND_AND_TWENTY_FIVE_MINUS_06_MINUS_15)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                                                                                                                                                                                                                 | Type                                                                                                                                                                                                                                                                                                                                                                                                                      | Required                                                                                                                                                                                                                                                                                                                                                                                                                  | Description                                                                                                                                                                                                                                                                                                                                                                                                               |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `company_id`                                                                                                                                                                                                                                                                                                                                                                                                              | *str*                                                                                                                                                                                                                                                                                                                                                                                                                     | :heavy_check_mark:                                                                                                                                                                                                                                                                                                                                                                                                        | The UUID of the company                                                                                                                                                                                                                                                                                                                                                                                                   |
| `frequency`                                                                                                                                                                                                                                                                                                                                                                                                               | [models.PayScheduleFrequencyCreateUpdate](../../models/payschedulefrequencycreateupdate.md)                                                                                                                                                                                                                                                                                                                               | :heavy_check_mark:                                                                                                                                                                                                                                                                                                                                                                                                        | Pay frequency when creating or updating a schedule. Only weekly, bi-weekly, twice per month, and monthly are supported via the API.<br/><br/>- `Every week`: Weekly pay.<br/>- `Every other week`: Biweekly pay.<br/>- `Twice per month`: Two pay dates per month; require day_1 and day_2 (use 31 for last day of month).<br/>- `Monthly`: One pay date per month; require day_1 (1-31).<br/>                            |
| `anchor_pay_date`                                                                                                                                                                                                                                                                                                                                                                                                         | [datetime](https://docs.python.org/3/library/datetime.html#datetime-objects)                                                                                                                                                                                                                                                                                                                                              | :heavy_check_mark:                                                                                                                                                                                                                                                                                                                                                                                                        | ISO 8601 date (YYYY-MM-DD). Required for anchor and period dates in create, update, and preview requests.                                                                                                                                                                                                                                                                                                                 |
| `anchor_end_of_pay_period`                                                                                                                                                                                                                                                                                                                                                                                                | [datetime](https://docs.python.org/3/library/datetime.html#datetime-objects)                                                                                                                                                                                                                                                                                                                                              | :heavy_check_mark:                                                                                                                                                                                                                                                                                                                                                                                                        | ISO 8601 date (YYYY-MM-DD). Required for anchor and period dates in create, update, and preview requests.                                                                                                                                                                                                                                                                                                                 |
| `x_gusto_api_version`                                                                                                                                                                                                                                                                                                                                                                                                     | [Optional[models.PostV1CompaniesCompanyIDPaySchedulesHeaderXGustoAPIVersion]](../../models/postv1companiescompanyidpayschedulesheaderxgustoapiversion.md)                                                                                                                                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                        | Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used.                                                                                                                                                                                              |
| `day_1`                                                                                                                                                                                                                                                                                                                                                                                                                   | *OptionalNullable[int]*                                                                                                                                                                                                                                                                                                                                                                                                   | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                        | First pay day of the month (1-31).<br/>- **Twice per month, Monthly:** required.<br/>- **Every week, Every other week:** omit or null.<br/>                                                                                                                                                                                                                                                                               |
| `day_2`                                                                                                                                                                                                                                                                                                                                                                                                                   | *OptionalNullable[int]*                                                                                                                                                                                                                                                                                                                                                                                                   | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                        | Second pay day of the month (1-31); only for **Twice per month**.<br/>- Use 31 for last day of month (shorter months use the actual last day).<br/>- **Other frequencies:** omit or null.<br/>                                                                                                                                                                                                                            |
| `custom_name`                                                                                                                                                                                                                                                                                                                                                                                                             | *OptionalNullable[str]*                                                                                                                                                                                                                                                                                                                                                                                                   | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                        | Optional display name for the pay schedule.<br/><br/>When null or omitted, the system generates a description from the pay frequency and pay days (e.g. "every 1st and 15th of the month" for twice-monthly, "every 11th of the month" for monthly, "every Friday" for weekly). The response returns this generated value in `custom_name` when no custom name was set. When provided, the value you set is stored and returned.<br/> |
| `retries`                                                                                                                                                                                                                                                                                                                                                                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                                                                                                                                                                                          | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                        | Configuration to override the default retry behavior of the client.                                                                                                                                                                                                                                                                                                                                                       |

### Response

**[models.PaySchedule](../../models/payschedule.md)**

### Errors

| Error Type                            | Status Code                           | Content Type                          |
| ------------------------------------- | ------------------------------------- | ------------------------------------- |
| models.NotFoundErrorObject            | 404                                   | application/json                      |
| models.UnprocessableEntityErrorObject | 422                                   | application/json                      |
| models.APIError                       | 4XX, 5XX                              | \*/\*                                 |

## get_all

Returns all pay schedules for a company. The pay schedule object captures the details of when employees work and when they should be paid. A company can have multiple pay schedules.

scope: `pay_schedules:read`

### Example Usage

<!-- UsageSnippet language="python" operationID="get-v1-companies-company_id-pay_schedules" method="get" path="/v1/companies/{company_id}/pay_schedules" -->
```python
import gusto_embedded
from gusto_embedded import Gusto
import os


with Gusto(
    company_access_auth=os.getenv("GUSTO_COMPANY_ACCESS_AUTH", ""),
) as gusto:

    res = gusto.pay_schedules.get_all(company_id="<id>", x_gusto_api_version=gusto_embedded.GetV1CompaniesCompanyIDPaySchedulesHeaderXGustoAPIVersion.TWO_THOUSAND_AND_TWENTY_FIVE_MINUS_06_MINUS_15)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                    | Type                                                                                                                                                                                                                         | Required                                                                                                                                                                                                                     | Description                                                                                                                                                                                                                  |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `company_id`                                                                                                                                                                                                                 | *str*                                                                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                                           | The UUID of the company                                                                                                                                                                                                      |
| `x_gusto_api_version`                                                                                                                                                                                                        | [Optional[models.GetV1CompaniesCompanyIDPaySchedulesHeaderXGustoAPIVersion]](../../models/getv1companiescompanyidpayschedulesheaderxgustoapiversion.md)                                                                      | :heavy_minus_sign:                                                                                                                                                                                                           | Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used. |
| `page`                                                                                                                                                                                                                       | *Optional[int]*                                                                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                           | The page that is requested. When unspecified, will load all objects unless endpoint forces pagination.                                                                                                                       |
| `per`                                                                                                                                                                                                                        | *Optional[int]*                                                                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                           | Number of objects per page. For majority of endpoints will default to 25                                                                                                                                                     |
| `retries`                                                                                                                                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                           | Configuration to override the default retry behavior of the client.                                                                                                                                                          |

### Response

**[List[models.PaySchedule]](../../models/.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.NotFoundErrorObject | 404                        | application/json           |
| models.APIError            | 4XX, 5XX                   | \*/\*                      |

## get_preview

Returns a preview of pay period dates and holidays for the given parameters (e.g. frequency, anchor pay date) for the next 18 months. Use this before creating or updating a pay schedule to show expected check dates and payroll deadlines.

### Related guides
- [Create a pay schedule](doc:create-a-pay-schedule)
- [Manage Pay Schedules via API](doc:manage-pay-schedules-api)

scope: `pay_schedules:write`

### Example Usage

<!-- UsageSnippet language="python" operationID="get-v1-companies-company_id-pay_schedules-preview" method="get" path="/v1/companies/{company_id}/pay_schedules/preview" -->
```python
from datetime import date
import gusto_embedded
from gusto_embedded import Gusto
import os


with Gusto(
    company_access_auth=os.getenv("GUSTO_COMPANY_ACCESS_AUTH", ""),
) as gusto:

    res = gusto.pay_schedules.get_preview(company_id="<id>", frequency=gusto_embedded.Frequency.MONTHLY, anchor_pay_date=date.fromisoformat("2024-11-07"), anchor_end_of_pay_period=date.fromisoformat("2025-12-20"), x_gusto_api_version=gusto_embedded.GetV1CompaniesCompanyIDPaySchedulesPreviewHeaderXGustoAPIVersion.TWO_THOUSAND_AND_TWENTY_FIVE_MINUS_06_MINUS_15)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                    | Type                                                                                                                                                                                                                         | Required                                                                                                                                                                                                                     | Description                                                                                                                                                                                                                  |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `company_id`                                                                                                                                                                                                                 | *str*                                                                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                                           | The UUID of the company                                                                                                                                                                                                      |
| `frequency`                                                                                                                                                                                                                  | [models.Frequency](../../models/frequency.md)                                                                                                                                                                                | :heavy_check_mark:                                                                                                                                                                                                           | The frequency that employees on this pay schedule are paid.                                                                                                                                                                  |
| `anchor_pay_date`                                                                                                                                                                                                            | [datetime](https://docs.python.org/3/library/datetime.html#datetime-objects)                                                                                                                                                 | :heavy_check_mark:                                                                                                                                                                                                           | The first date that employees on this pay schedule are paid.                                                                                                                                                                 |
| `anchor_end_of_pay_period`                                                                                                                                                                                                   | [datetime](https://docs.python.org/3/library/datetime.html#datetime-objects)                                                                                                                                                 | :heavy_check_mark:                                                                                                                                                                                                           | The last date of the first pay period. This can be the same date as the anchor pay date.                                                                                                                                     |
| `x_gusto_api_version`                                                                                                                                                                                                        | [Optional[models.GetV1CompaniesCompanyIDPaySchedulesPreviewHeaderXGustoAPIVersion]](../../models/getv1companiescompanyidpayschedulespreviewheaderxgustoapiversion.md)                                                        | :heavy_minus_sign:                                                                                                                                                                                                           | Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used. |
| `day_1`                                                                                                                                                                                                                      | *Optional[int]*                                                                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                           | First pay day of the month (1-31).<br/>- **Twice per month, Monthly:** required.<br/>- **Every week, Every other week:** omit or null.                                                                                       |
| `day_2`                                                                                                                                                                                                                      | *Optional[int]*                                                                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                           | Second pay day of the month (1-31); only for **Twice per month**.<br/>- Use 31 for last day of month (shorter months use the actual last day).<br/>- **Other frequencies:** omit or null.                                    |
| `end_date`                                                                                                                                                                                                                   | [datetime](https://docs.python.org/3/library/datetime.html#datetime-objects)                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                                                                           | End date for the preview range. When unspecified, defaults to 18 months from today.                                                                                                                                          |
| `retries`                                                                                                                                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                           | Configuration to override the default retry behavior of the client.                                                                                                                                                          |

### Response

**[models.PaySchedulePreview](../../models/payschedulepreview.md)**

### Errors

| Error Type                            | Status Code                           | Content Type                          |
| ------------------------------------- | ------------------------------------- | ------------------------------------- |
| models.NotFoundErrorObject            | 404                                   | application/json                      |
| models.UnprocessableEntityErrorObject | 422                                   | application/json                      |
| models.APIError                       | 4XX, 5XX                              | \*/\*                                 |

## get

Returns a single pay schedule by UUID. The pay schedule object captures the details of when employees work and when they should be paid. A company can have multiple pay schedules.

scope: `pay_schedules:read`

### Example Usage

<!-- UsageSnippet language="python" operationID="get-v1-companies-company_id-pay_schedules-pay_schedule_id" method="get" path="/v1/companies/{company_id}/pay_schedules/{pay_schedule_id}" -->
```python
import gusto_embedded
from gusto_embedded import Gusto
import os


with Gusto(
    company_access_auth=os.getenv("GUSTO_COMPANY_ACCESS_AUTH", ""),
) as gusto:

    res = gusto.pay_schedules.get(company_id="<id>", pay_schedule_id="<id>", x_gusto_api_version=gusto_embedded.GetV1CompaniesCompanyIDPaySchedulesPayScheduleIDHeaderXGustoAPIVersion.TWO_THOUSAND_AND_TWENTY_FIVE_MINUS_06_MINUS_15)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                    | Type                                                                                                                                                                                                                         | Required                                                                                                                                                                                                                     | Description                                                                                                                                                                                                                  |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `company_id`                                                                                                                                                                                                                 | *str*                                                                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                                           | The UUID of the company                                                                                                                                                                                                      |
| `pay_schedule_id`                                                                                                                                                                                                            | *str*                                                                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                                           | The UUID of the pay schedule                                                                                                                                                                                                 |
| `x_gusto_api_version`                                                                                                                                                                                                        | [Optional[models.GetV1CompaniesCompanyIDPaySchedulesPayScheduleIDHeaderXGustoAPIVersion]](../../models/getv1companiescompanyidpayschedulespayscheduleidheaderxgustoapiversion.md)                                            | :heavy_minus_sign:                                                                                                                                                                                                           | Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used. |
| `retries`                                                                                                                                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                           | Configuration to override the default retry behavior of the client.                                                                                                                                                          |

### Response

**[models.PaySchedule](../../models/payschedule.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.NotFoundErrorObject | 404                        | application/json           |
| models.APIError            | 4XX, 5XX                   | \*/\*                      |

## update

Updates a pay schedule. The `version` parameter from the GET response is required for [optimistic concurrency](doc:api-fundamentals); a mismatch returns 409 Conflict.

### Pay schedules may be automatically adjusted
If an onboarded company misses their first pay date, the pay schedule may be automatically adjusted.

### Webhooks
- `pay_schedule.updated`: Fires when a pay schedule is successfully updated.

### Related guides
- [Create a pay schedule](doc:create-a-pay-schedule)
- [Manage Pay Schedules via API](doc:manage-pay-schedules-api)

scope: `pay_schedules:write`

### Example Usage

<!-- UsageSnippet language="python" operationID="put-v1-companies-company_id-pay_schedules-pay_schedule_id" method="put" path="/v1/companies/{company_id}/pay_schedules/{pay_schedule_id}" -->
```python
import gusto_embedded
from gusto_embedded import Gusto
import os


with Gusto(
    company_access_auth=os.getenv("GUSTO_COMPANY_ACCESS_AUTH", ""),
) as gusto:

    res = gusto.pay_schedules.update(company_id="<id>", pay_schedule_id="<id>", version="<value>", x_gusto_api_version=gusto_embedded.PutV1CompaniesCompanyIDPaySchedulesPayScheduleIDHeaderXGustoAPIVersion.TWO_THOUSAND_AND_TWENTY_FIVE_MINUS_06_MINUS_15)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                                                                                                                                                              | Type                                                                                                                                                                                                                                                                                                                                                                   | Required                                                                                                                                                                                                                                                                                                                                                               | Description                                                                                                                                                                                                                                                                                                                                                            |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `company_id`                                                                                                                                                                                                                                                                                                                                                           | *str*                                                                                                                                                                                                                                                                                                                                                                  | :heavy_check_mark:                                                                                                                                                                                                                                                                                                                                                     | The UUID of the company                                                                                                                                                                                                                                                                                                                                                |
| `pay_schedule_id`                                                                                                                                                                                                                                                                                                                                                      | *str*                                                                                                                                                                                                                                                                                                                                                                  | :heavy_check_mark:                                                                                                                                                                                                                                                                                                                                                     | The UUID of the pay schedule                                                                                                                                                                                                                                                                                                                                           |
| `version`                                                                                                                                                                                                                                                                                                                                                              | *str*                                                                                                                                                                                                                                                                                                                                                                  | :heavy_check_mark:                                                                                                                                                                                                                                                                                                                                                     | Current version of the pay schedule from the GET response; required for optimistic concurrency. Mismatch returns 409 Conflict.                                                                                                                                                                                                                                         |
| `x_gusto_api_version`                                                                                                                                                                                                                                                                                                                                                  | [Optional[models.PutV1CompaniesCompanyIDPaySchedulesPayScheduleIDHeaderXGustoAPIVersion]](../../models/putv1companiescompanyidpayschedulespayscheduleidheaderxgustoapiversion.md)                                                                                                                                                                                      | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                     | Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used.                                                                                                                                           |
| `auto_payroll`                                                                                                                                                                                                                                                                                                                                                         | *Optional[bool]*                                                                                                                                                                                                                                                                                                                                                       | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                     | When true, Autopayroll is enabled and payroll runs automatically one day before payroll deadlines. When false, payroll does not run automatically and must be run manually.<br/>For API versions before 2025-11-15 the request field is auto_pilot.<br/>                                                                                                               |
| `frequency`                                                                                                                                                                                                                                                                                                                                                            | [Optional[models.PayScheduleFrequencyCreateUpdate]](../../models/payschedulefrequencycreateupdate.md)                                                                                                                                                                                                                                                                  | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                     | Pay frequency when creating or updating a schedule. Only weekly, bi-weekly, twice per month, and monthly are supported via the API.<br/><br/>- `Every week`: Weekly pay.<br/>- `Every other week`: Biweekly pay.<br/>- `Twice per month`: Two pay dates per month; require day_1 and day_2 (use 31 for last day of month).<br/>- `Monthly`: One pay date per month; require day_1 (1-31).<br/> |
| `anchor_pay_date`                                                                                                                                                                                                                                                                                                                                                      | [datetime](https://docs.python.org/3/library/datetime.html#datetime-objects)                                                                                                                                                                                                                                                                                           | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                     | ISO 8601 date (YYYY-MM-DD). Required for anchor and period dates in create, update, and preview requests.                                                                                                                                                                                                                                                              |
| `anchor_end_of_pay_period`                                                                                                                                                                                                                                                                                                                                             | [datetime](https://docs.python.org/3/library/datetime.html#datetime-objects)                                                                                                                                                                                                                                                                                           | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                     | ISO 8601 date (YYYY-MM-DD). Required for anchor and period dates in create, update, and preview requests.                                                                                                                                                                                                                                                              |
| `day_1`                                                                                                                                                                                                                                                                                                                                                                | *OptionalNullable[int]*                                                                                                                                                                                                                                                                                                                                                | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                     | First pay day of the month (1–31). Required for Twice per month and Monthly; null for Every week and Every other week.<br/>                                                                                                                                                                                                                                            |
| `day_2`                                                                                                                                                                                                                                                                                                                                                                | *OptionalNullable[int]*                                                                                                                                                                                                                                                                                                                                                | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                     | Second pay day of the month (1–31); only for Twice per month. Use 31 for last day of month. Null for other frequencies.<br/>                                                                                                                                                                                                                                           |
| `custom_name`                                                                                                                                                                                                                                                                                                                                                          | *OptionalNullable[str]*                                                                                                                                                                                                                                                                                                                                                | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                     | Custom name for the pay schedule; null clears it.                                                                                                                                                                                                                                                                                                                      |
| `retries`                                                                                                                                                                                                                                                                                                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                                                                                                                                       | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                     | Configuration to override the default retry behavior of the client.                                                                                                                                                                                                                                                                                                    |

### Response

**[models.PaySchedule](../../models/payschedule.md)**

### Errors

| Error Type                            | Status Code                           | Content Type                          |
| ------------------------------------- | ------------------------------------- | ------------------------------------- |
| models.NotFoundErrorObject            | 404                                   | application/json                      |
| models.UnprocessableEntityErrorObject | 409, 422                              | application/json                      |
| models.APIError                       | 4XX, 5XX                              | \*/\*                                 |

## get_pay_periods

Pay periods are the foundation of payroll. Compensation, time & attendance, taxes, and expense reports all rely on when they happened.

To begin submitting information for a given payroll, we need to agree on the time period.

By default, this endpoint returns pay periods starting from 6 months ago to the date today. Use the `start_date` and `end_date` parameters to change the scope of the response. End dates can be up to 3 months in the future and there is no limit on start dates.

Starting in version 2023-04-01, the `eligible_employees` attribute was removed from the response. The eligible employees for a payroll are determined by the employee_compensations returned from the [PUT /v1/companies/{company_id}/payrolls/{payroll_id}/prepare](ref:put-v1-companies-company_id-payrolls-payroll_id-prepare) endpoint.

scope: `payrolls:read`

### Example Usage

<!-- UsageSnippet language="python" operationID="get-v1-companies-company_id-pay_periods" method="get" path="/v1/companies/{company_id}/pay_periods" -->
```python
import gusto_embedded
from gusto_embedded import Gusto
import os


with Gusto(
    company_access_auth=os.getenv("GUSTO_COMPANY_ACCESS_AUTH", ""),
) as gusto:

    res = gusto.pay_schedules.get_pay_periods(company_id="<id>", x_gusto_api_version=gusto_embedded.GetV1CompaniesCompanyIDPayPeriodsHeaderXGustoAPIVersion.TWO_THOUSAND_AND_TWENTY_FIVE_MINUS_06_MINUS_15)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                    | Type                                                                                                                                                                                                                         | Required                                                                                                                                                                                                                     | Description                                                                                                                                                                                                                  |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `company_id`                                                                                                                                                                                                                 | *str*                                                                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                                           | The UUID of the company                                                                                                                                                                                                      |
| `x_gusto_api_version`                                                                                                                                                                                                        | [Optional[models.GetV1CompaniesCompanyIDPayPeriodsHeaderXGustoAPIVersion]](../../models/getv1companiescompanyidpayperiodsheaderxgustoapiversion.md)                                                                          | :heavy_minus_sign:                                                                                                                                                                                                           | Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used. |
| `start_date`                                                                                                                                                                                                                 | [datetime](https://docs.python.org/3/library/datetime.html#datetime-objects)                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                                                                           | Start date (YYYY-MM-DD) for the pay periods range. Defaults to 6 months ago.                                                                                                                                                 |
| `end_date`                                                                                                                                                                                                                   | [datetime](https://docs.python.org/3/library/datetime.html#datetime-objects)                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                                                                           | End date (YYYY-MM-DD) for the pay periods range. Cannot be more than 3 months in the future. Defaults to today.                                                                                                              |
| `payroll_types`                                                                                                                                                                                                              | [Optional[models.PayrollTypes]](../../models/payrolltypes.md)                                                                                                                                                                | :heavy_minus_sign:                                                                                                                                                                                                           | Comma-separated list of payroll types to include (regular, transition). Defaults to regular only.                                                                                                                            |
| `retries`                                                                                                                                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                           | Configuration to override the default retry behavior of the client.                                                                                                                                                          |

### Response

**[List[models.PayPeriod]](../../models/.md)**

### Errors

| Error Type                            | Status Code                           | Content Type                          |
| ------------------------------------- | ------------------------------------- | ------------------------------------- |
| models.NotFoundErrorObject            | 404                                   | application/json                      |
| models.UnprocessableEntityErrorObject | 422                                   | application/json                      |
| models.APIError                       | 4XX, 5XX                              | \*/\*                                 |

## get_unprocessed_termination_periods

When a payroll admin terminates an employee and selects "Dismissal Payroll" as the employee's final payroll, their last pay period will appear on the list.

This endpoint returns the unprocessed pay periods for past and future terminated employees in a given company.

scope: `payrolls:read`

### Example Usage

<!-- UsageSnippet language="python" operationID="get-v1-companies-company_id-unprocessed_termination_pay_periods" method="get" path="/v1/companies/{company_id}/pay_periods/unprocessed_termination_pay_periods" example="Example" -->
```python
import gusto_embedded
from gusto_embedded import Gusto
import os


with Gusto(
    company_access_auth=os.getenv("GUSTO_COMPANY_ACCESS_AUTH", ""),
) as gusto:

    res = gusto.pay_schedules.get_unprocessed_termination_periods(company_id="<id>", x_gusto_api_version=gusto_embedded.VersionHeader.TWO_THOUSAND_AND_TWENTY_FIVE_MINUS_06_MINUS_15)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                    | Type                                                                                                                                                                                                                         | Required                                                                                                                                                                                                                     | Description                                                                                                                                                                                                                  |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `company_id`                                                                                                                                                                                                                 | *str*                                                                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                                           | The UUID of the company                                                                                                                                                                                                      |
| `x_gusto_api_version`                                                                                                                                                                                                        | [Optional[models.VersionHeader]](../../models/versionheader.md)                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                           | Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used. |
| `retries`                                                                                                                                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                           | Configuration to override the default retry behavior of the client.                                                                                                                                                          |

### Response

**[List[models.UnprocessedTerminationPayPeriod]](../../models/.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## get_assignments

This endpoint returns the current pay schedule assignment for a company, with pay schedule and employee/department mappings depending on the pay schedule type.

scope: `pay_schedules:read`

### Example Usage

<!-- UsageSnippet language="python" operationID="get-v1-companies-company_id-pay_schedules-assignments" method="get" path="/v1/companies/{company_id}/pay_schedules/assignments" example="Example" -->
```python
import gusto_embedded
from gusto_embedded import Gusto
import os


with Gusto(
    company_access_auth=os.getenv("GUSTO_COMPANY_ACCESS_AUTH", ""),
) as gusto:

    res = gusto.pay_schedules.get_assignments(company_id="<id>", x_gusto_api_version=gusto_embedded.VersionHeader.TWO_THOUSAND_AND_TWENTY_FIVE_MINUS_06_MINUS_15)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                    | Type                                                                                                                                                                                                                         | Required                                                                                                                                                                                                                     | Description                                                                                                                                                                                                                  |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `company_id`                                                                                                                                                                                                                 | *str*                                                                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                                           | The UUID of the company                                                                                                                                                                                                      |
| `x_gusto_api_version`                                                                                                                                                                                                        | [Optional[models.VersionHeader]](../../models/versionheader.md)                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                           | Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used. |
| `retries`                                                                                                                                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                           | Configuration to override the default retry behavior of the client.                                                                                                                                                          |

### Response

**[models.PayScheduleAssignment](../../models/payscheduleassignment.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## preview_assignment

This endpoint returns the employee changes, including pay period and transition pay periods, for changing the pay schedule.

scope: `pay_schedules:write`

### Example Usage: Basic

<!-- UsageSnippet language="python" operationID="post-v1-companies-company_id-pay_schedules-assignment_preview" method="post" path="/v1/companies/{company_id}/pay_schedules/assignment_preview" example="Basic" -->
```python
import gusto_embedded
from gusto_embedded import Gusto
import os


with Gusto(
    company_access_auth=os.getenv("GUSTO_COMPANY_ACCESS_AUTH", ""),
) as gusto:

    res = gusto.pay_schedules.preview_assignment(company_id="<id>", type_=gusto_embedded.PayScheduleAssignmentBodyType.BY_EMPLOYEE, x_gusto_api_version=gusto_embedded.VersionHeader.TWO_THOUSAND_AND_TWENTY_FIVE_MINUS_06_MINUS_15)

    # Handle response
    print(res)

```
### Example Usage: Example

<!-- UsageSnippet language="python" operationID="post-v1-companies-company_id-pay_schedules-assignment_preview" method="post" path="/v1/companies/{company_id}/pay_schedules/assignment_preview" example="Example" -->
```python
import gusto_embedded
from gusto_embedded import Gusto
import os


with Gusto(
    company_access_auth=os.getenv("GUSTO_COMPANY_ACCESS_AUTH", ""),
) as gusto:

    res = gusto.pay_schedules.preview_assignment(company_id="<id>", type_=gusto_embedded.PayScheduleAssignmentBodyType.BY_EMPLOYEE, x_gusto_api_version=gusto_embedded.VersionHeader.TWO_THOUSAND_AND_TWENTY_FIVE_MINUS_06_MINUS_15, employees=[
        {
            "employee_uuid": "f0238368-f2cf-43e2-9a07-b0265f2cec69",
            "pay_schedule_uuid": "c277ac52-9871-4a96-a1e6-0c449684602a",
        },
    ])

    # Handle response
    print(res)

```
### Example Usage: Nested

<!-- UsageSnippet language="python" operationID="post-v1-companies-company_id-pay_schedules-assignment_preview" method="post" path="/v1/companies/{company_id}/pay_schedules/assignment_preview" example="Nested" -->
```python
import gusto_embedded
from gusto_embedded import Gusto
import os


with Gusto(
    company_access_auth=os.getenv("GUSTO_COMPANY_ACCESS_AUTH", ""),
) as gusto:

    res = gusto.pay_schedules.preview_assignment(company_id="<id>", type_=gusto_embedded.PayScheduleAssignmentBodyType.BY_EMPLOYEE, x_gusto_api_version=gusto_embedded.VersionHeader.TWO_THOUSAND_AND_TWENTY_FIVE_MINUS_06_MINUS_15)

    # Handle response
    print(res)

```
### Example Usage: Resource

<!-- UsageSnippet language="python" operationID="post-v1-companies-company_id-pay_schedules-assignment_preview" method="post" path="/v1/companies/{company_id}/pay_schedules/assignment_preview" example="Resource" -->
```python
import gusto_embedded
from gusto_embedded import Gusto
import os


with Gusto(
    company_access_auth=os.getenv("GUSTO_COMPANY_ACCESS_AUTH", ""),
) as gusto:

    res = gusto.pay_schedules.preview_assignment(company_id="<id>", type_=gusto_embedded.PayScheduleAssignmentBodyType.BY_EMPLOYEE, x_gusto_api_version=gusto_embedded.VersionHeader.TWO_THOUSAND_AND_TWENTY_FIVE_MINUS_06_MINUS_15)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                    | Type                                                                                                                                                                                                                         | Required                                                                                                                                                                                                                     | Description                                                                                                                                                                                                                  |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `company_id`                                                                                                                                                                                                                 | *str*                                                                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                                           | The UUID of the company                                                                                                                                                                                                      |
| `type`                                                                                                                                                                                                                       | [Nullable[models.PayScheduleAssignmentBodyType]](../../models/payscheduleassignmentbodytype.md)                                                                                                                              | :heavy_check_mark:                                                                                                                                                                                                           | The pay schedule assignment type.                                                                                                                                                                                            |
| `x_gusto_api_version`                                                                                                                                                                                                        | [Optional[models.VersionHeader]](../../models/versionheader.md)                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                           | Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used. |
| `hourly_pay_schedule_uuid`                                                                                                                                                                                                   | *Optional[str]*                                                                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                           | Pay schedule for hourly employees.                                                                                                                                                                                           |
| `salaried_pay_schedule_uuid`                                                                                                                                                                                                 | *Optional[str]*                                                                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                           | Pay schedule for salaried employees.                                                                                                                                                                                         |
| `default_pay_schedule_uuid`                                                                                                                                                                                                  | *Optional[str]*                                                                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                           | Default pay schedule for employees.                                                                                                                                                                                          |
| `partial_assignment`                                                                                                                                                                                                         | *Optional[bool]*                                                                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                           | Indicates whether the request provides pay schedule assignments for a partial list of employees or departments of the company. By default, this is set to false.                                                             |
| `employees`                                                                                                                                                                                                                  | List[[models.EmployeesModel](../../models/employeesmodel.md)]                                                                                                                                                                | :heavy_minus_sign:                                                                                                                                                                                                           | List of employees and their pay schedules.                                                                                                                                                                                   |
| `departments`                                                                                                                                                                                                                | List[[models.DepartmentsModel](../../models/departmentsmodel.md)]                                                                                                                                                            | :heavy_minus_sign:                                                                                                                                                                                                           | List of departments and their pay schedules.                                                                                                                                                                                 |
| `retries`                                                                                                                                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                           | Configuration to override the default retry behavior of the client.                                                                                                                                                          |

### Response

**[models.PayScheduleAssignmentPreview](../../models/payscheduleassignmentpreview.md)**

### Errors

| Error Type                            | Status Code                           | Content Type                          |
| ------------------------------------- | ------------------------------------- | ------------------------------------- |
| models.UnprocessableEntityErrorObject | 422                                   | application/json                      |
| models.APIError                       | 4XX, 5XX                              | \*/\*                                 |

## assign

This endpoint assigns employees to pay schedules based on the schedule type.
For `by_employee` and `by_department` schedules, use the `partial_assignment` parameter to control the assignment scope. Set it to `true` for partial assignments (only some employees or departments at a time) and `false` for full assignments (all employees or departments at once).

scope: `pay_schedules:write`

### Example Usage: Basic

<!-- UsageSnippet language="python" operationID="post-v1-companies-company_id-pay_schedules-assign" method="post" path="/v1/companies/{company_id}/pay_schedules/assign" example="Basic" -->
```python
import gusto_embedded
from gusto_embedded import Gusto
import os


with Gusto(
    company_access_auth=os.getenv("GUSTO_COMPANY_ACCESS_AUTH", ""),
) as gusto:

    gusto.pay_schedules.assign(company_id="<id>", type_=gusto_embedded.PayScheduleAssignmentBodyType.HOURLY_SALARIED, x_gusto_api_version=gusto_embedded.VersionHeader.TWO_THOUSAND_AND_TWENTY_FIVE_MINUS_06_MINUS_15)

    # Use the SDK ...

```
### Example Usage: Example

<!-- UsageSnippet language="python" operationID="post-v1-companies-company_id-pay_schedules-assign" method="post" path="/v1/companies/{company_id}/pay_schedules/assign" example="Example" -->
```python
import gusto_embedded
from gusto_embedded import Gusto
import os


with Gusto(
    company_access_auth=os.getenv("GUSTO_COMPANY_ACCESS_AUTH", ""),
) as gusto:

    gusto.pay_schedules.assign(company_id="<id>", type_=gusto_embedded.PayScheduleAssignmentBodyType.BY_EMPLOYEE, x_gusto_api_version=gusto_embedded.VersionHeader.TWO_THOUSAND_AND_TWENTY_FIVE_MINUS_06_MINUS_15, employees=[
        {
            "employee_uuid": "f0238368-f2cf-43e2-9a07-b0265f2cec69",
            "pay_schedule_uuid": "c277ac52-9871-4a96-a1e6-0c449684602a",
        },
    ])

    # Use the SDK ...

```
### Example Usage: Nested

<!-- UsageSnippet language="python" operationID="post-v1-companies-company_id-pay_schedules-assign" method="post" path="/v1/companies/{company_id}/pay_schedules/assign" example="Nested" -->
```python
import gusto_embedded
from gusto_embedded import Gusto
import os


with Gusto(
    company_access_auth=os.getenv("GUSTO_COMPANY_ACCESS_AUTH", ""),
) as gusto:

    gusto.pay_schedules.assign(company_id="<id>", type_=gusto_embedded.PayScheduleAssignmentBodyType.HOURLY_SALARIED, x_gusto_api_version=gusto_embedded.VersionHeader.TWO_THOUSAND_AND_TWENTY_FIVE_MINUS_06_MINUS_15)

    # Use the SDK ...

```
### Example Usage: Resource

<!-- UsageSnippet language="python" operationID="post-v1-companies-company_id-pay_schedules-assign" method="post" path="/v1/companies/{company_id}/pay_schedules/assign" example="Resource" -->
```python
import gusto_embedded
from gusto_embedded import Gusto
import os


with Gusto(
    company_access_auth=os.getenv("GUSTO_COMPANY_ACCESS_AUTH", ""),
) as gusto:

    gusto.pay_schedules.assign(company_id="<id>", type_=gusto_embedded.PayScheduleAssignmentBodyType.HOURLY_SALARIED, x_gusto_api_version=gusto_embedded.VersionHeader.TWO_THOUSAND_AND_TWENTY_FIVE_MINUS_06_MINUS_15)

    # Use the SDK ...

```

### Parameters

| Parameter                                                                                                                                                                                                                    | Type                                                                                                                                                                                                                         | Required                                                                                                                                                                                                                     | Description                                                                                                                                                                                                                  |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `company_id`                                                                                                                                                                                                                 | *str*                                                                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                                           | The UUID of the company                                                                                                                                                                                                      |
| `type`                                                                                                                                                                                                                       | [Nullable[models.PayScheduleAssignmentBodyType]](../../models/payscheduleassignmentbodytype.md)                                                                                                                              | :heavy_check_mark:                                                                                                                                                                                                           | The pay schedule assignment type.                                                                                                                                                                                            |
| `x_gusto_api_version`                                                                                                                                                                                                        | [Optional[models.VersionHeader]](../../models/versionheader.md)                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                           | Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used. |
| `hourly_pay_schedule_uuid`                                                                                                                                                                                                   | *Optional[str]*                                                                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                           | Pay schedule for hourly employees.                                                                                                                                                                                           |
| `salaried_pay_schedule_uuid`                                                                                                                                                                                                 | *Optional[str]*                                                                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                           | Pay schedule for salaried employees.                                                                                                                                                                                         |
| `default_pay_schedule_uuid`                                                                                                                                                                                                  | *Optional[str]*                                                                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                           | Default pay schedule for employees.                                                                                                                                                                                          |
| `partial_assignment`                                                                                                                                                                                                         | *Optional[bool]*                                                                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                           | Indicates whether the request provides pay schedule assignments for a partial list of employees or departments of the company. By default, this is set to false.                                                             |
| `employees`                                                                                                                                                                                                                  | List[[models.EmployeesModel](../../models/employeesmodel.md)]                                                                                                                                                                | :heavy_minus_sign:                                                                                                                                                                                                           | List of employees and their pay schedules.                                                                                                                                                                                   |
| `departments`                                                                                                                                                                                                                | List[[models.DepartmentsModel](../../models/departmentsmodel.md)]                                                                                                                                                            | :heavy_minus_sign:                                                                                                                                                                                                           | List of departments and their pay schedules.                                                                                                                                                                                 |
| `retries`                                                                                                                                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                           | Configuration to override the default retry behavior of the client.                                                                                                                                                          |

### Errors

| Error Type                            | Status Code                           | Content Type                          |
| ------------------------------------- | ------------------------------------- | ------------------------------------- |
| models.UnprocessableEntityErrorObject | 422                                   | application/json                      |
| models.APIError                       | 4XX, 5XX                              | \*/\*                                 |