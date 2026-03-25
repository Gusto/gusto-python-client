# TimeTracking

## Overview

### Available Operations

* [get_companies_company_uuid_time_tracking_time_sheets](#get_companies_company_uuid_time_tracking_time_sheets) - Get all time sheets for a company
* [post_companies_company_uuid_time_tracking_time_sheets](#post_companies_company_uuid_time_tracking_time_sheets) - Create a time sheet
* [get_time_tracking_time_sheets_time_sheet_uuid](#get_time_tracking_time_sheets_time_sheet_uuid) - Get a time sheet
* [put_time_tracking_time_sheets_time_sheet_uuid](#put_time_tracking_time_sheets_time_sheet_uuid) - Update a time sheet
* [delete_time_tracking_time_sheets_time_sheet_uuid](#delete_time_tracking_time_sheets_time_sheet_uuid) - Delete a time sheet
* [post_companies_company_uuid_time_tracking_payroll_syncs](#post_companies_company_uuid_time_tracking_payroll_syncs) - Create a payroll sync
* [get_time_tracking_payroll_syncs_payroll_sync_uuid](#get_time_tracking_payroll_syncs_payroll_sync_uuid) - Get a payroll sync

## get_companies_company_uuid_time_tracking_time_sheets

Fetch all company's time sheets.

Time sheets represent the time worked by an employee or contractor for a given time range.
Hours are classified by pay classification, and can be regular, overtime, or double overtime.

scope: `time_sheet:read`

### Example Usage

<!-- UsageSnippet language="python" operationID="get-companies-company_uuid-time_tracking-time_sheets" method="get" path="/v1/companies/{company_uuid}/time_tracking/time_sheets" example="Example" -->
```python
import gusto_app_integration
from gusto_app_integration import GustoAppIntegration


with GustoAppIntegration(
    company_access_auth="<YOUR_BEARER_TOKEN_HERE>",
) as gai_client:

    res = gai_client.time_tracking.get_companies_company_uuid_time_tracking_time_sheets(company_uuid="<id>", x_gusto_api_version=gusto_app_integration.VersionHeader.TWO_THOUSAND_AND_TWENTY_FIVE_MINUS_06_MINUS_15)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                    | Type                                                                                                                                                                                                                         | Required                                                                                                                                                                                                                     | Description                                                                                                                                                                                                                  |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `company_uuid`                                                                                                                                                                                                               | *str*                                                                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                                           | The UUID of the company                                                                                                                                                                                                      |
| `entity_uuids`                                                                                                                                                                                                               | List[*str*]                                                                                                                                                                                                                  | :heavy_minus_sign:                                                                                                                                                                                                           | Entity UUIDs that reported time sheets                                                                                                                                                                                       |
| `entity_type`                                                                                                                                                                                                                | [Optional[models.EntityType]](../../models/entitytype.md)                                                                                                                                                                    | :heavy_minus_sign:                                                                                                                                                                                                           | Type of entities to filter. One of: "Employee", "Contractor"                                                                                                                                                                 |
| `status`                                                                                                                                                                                                                     | [Optional[models.Status]](../../models/status.md)                                                                                                                                                                            | :heavy_minus_sign:                                                                                                                                                                                                           | Status of time sheets. One of: "approved", "pending", "rejected"                                                                                                                                                             |
| `sort_by`                                                                                                                                                                                                                    | [Optional[models.TimeSheetSortBy]](../../models/timesheetsortby.md)                                                                                                                                                          | :heavy_minus_sign:                                                                                                                                                                                                           | Field to sort by. One of: "created_at", "updated_at", "shift_started_at", "shift_ended_at"                                                                                                                                   |
| `sort_order`                                                                                                                                                                                                                 | [Optional[models.TimeSheetSortOrder]](../../models/timesheetsortorder.md)                                                                                                                                                    | :heavy_minus_sign:                                                                                                                                                                                                           | Sorting order. One of: "asc", "desc"                                                                                                                                                                                         |
| `before`                                                                                                                                                                                                                     | *Optional[str]*                                                                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                           | time sheets that were created before ISO 8601 timestamp. Filtering by "created_at"                                                                                                                                           |
| `after`                                                                                                                                                                                                                      | *Optional[str]*                                                                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                           | time sheets that were created before ISO 8601 timestamp. Filtering by "created_at"                                                                                                                                           |
| `page`                                                                                                                                                                                                                       | *Optional[int]*                                                                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                           | The page that is requested. When unspecified, will load all objects unless endpoint forces pagination.                                                                                                                       |
| `per`                                                                                                                                                                                                                        | *Optional[int]*                                                                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                           | Number of objects per page. For majority of endpoints will default to 25                                                                                                                                                     |
| `x_gusto_api_version`                                                                                                                                                                                                        | [Optional[models.VersionHeader]](../../models/versionheader.md)                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                           | Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used. |
| `retries`                                                                                                                                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                           | Configuration to override the default retry behavior of the client.                                                                                                                                                          |

### Response

**[List[models.TimeSheet]](../../models/.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## post_companies_company_uuid_time_tracking_time_sheets

Create a time sheet for a company.

Time sheets represent the time worked by an employee or contractor for a given time range.
Hours are classified by pay classification, and can be regular, overtime, or double overtime.

scope: `time_sheet:write`

### Example Usage: Example

<!-- UsageSnippet language="python" operationID="post-companies-company_uuid-time_tracking-time_sheets" method="post" path="/v1/companies/{company_uuid}/time_tracking/time_sheets" example="Example" -->
```python
import gusto_app_integration
from gusto_app_integration import GustoAppIntegration
from gusto_app_integration.utils import parse_datetime


with GustoAppIntegration(
    company_access_auth="<YOUR_BEARER_TOKEN_HERE>",
) as gai_client:

    res = gai_client.time_tracking.post_companies_company_uuid_time_tracking_time_sheets(company_uuid="<id>", entity_uuid="123e4567-e89b-12d3-a456-426614174000", entity_type="Employee", time_zone="America/New_York", shift_started_at=parse_datetime("2024-06-10T09:00:00Z"), x_gusto_api_version=gusto_app_integration.VersionHeader.TWO_THOUSAND_AND_TWENTY_FIVE_MINUS_06_MINUS_15, job_uuid="123e4567-e89b-12d3-a456-426614174000", shift_ended_at=parse_datetime("2024-06-10T17:00:00Z"), metadata={
        "custom_field": "custom value",
    }, entries=[
        {
            "hours_worked": 1.5,
            "pay_classification": gusto_app_integration.PostCompaniesCompanyUUIDTimeTrackingTimeSheetsPayClassification.REGULAR,
        },
    ])

    # Handle response
    print(res)

```
### Example Usage: example

<!-- UsageSnippet language="python" operationID="post-companies-company_uuid-time_tracking-time_sheets" method="post" path="/v1/companies/{company_uuid}/time_tracking/time_sheets" example="example" -->
```python
import gusto_app_integration
from gusto_app_integration import GustoAppIntegration
from gusto_app_integration.utils import parse_datetime


with GustoAppIntegration(
    company_access_auth="<YOUR_BEARER_TOKEN_HERE>",
) as gai_client:

    res = gai_client.time_tracking.post_companies_company_uuid_time_tracking_time_sheets(company_uuid="<id>", entity_uuid="<id>", entity_type="<value>", time_zone="America/Santarem", shift_started_at=parse_datetime("2026-09-10T06:26:36.108Z"), x_gusto_api_version=gusto_app_integration.VersionHeader.TWO_THOUSAND_AND_TWENTY_FIVE_MINUS_06_MINUS_15)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                    | Type                                                                                                                                                                                                                         | Required                                                                                                                                                                                                                     | Description                                                                                                                                                                                                                  |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `company_uuid`                                                                                                                                                                                                               | *str*                                                                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                                           | The UUID of the company                                                                                                                                                                                                      |
| `entity_uuid`                                                                                                                                                                                                                | *str*                                                                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                                           | Unique identifier of the entity associated with the time sheet.                                                                                                                                                              |
| `entity_type`                                                                                                                                                                                                                | *str*                                                                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                                           | Type of entity associated with the time sheet.                                                                                                                                                                               |
| `time_zone`                                                                                                                                                                                                                  | *str*                                                                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                                           | Time zone of where the time is tracked.                                                                                                                                                                                      |
| `shift_started_at`                                                                                                                                                                                                           | [date](https://docs.python.org/3/library/datetime.html#date-objects)                                                                                                                                                         | :heavy_check_mark:                                                                                                                                                                                                           | ISO 8601 timestamp of when the shift was started.                                                                                                                                                                            |
| `x_gusto_api_version`                                                                                                                                                                                                        | [Optional[models.VersionHeader]](../../models/versionheader.md)                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                           | Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used. |
| `job_uuid`                                                                                                                                                                                                                   | *Optional[str]*                                                                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                           | Unique identifier of the job for which time is tracked.                                                                                                                                                                      |
| `shift_ended_at`                                                                                                                                                                                                             | [date](https://docs.python.org/3/library/datetime.html#date-objects)                                                                                                                                                         | :heavy_minus_sign:                                                                                                                                                                                                           | ISO 8601 timestamp of when the shift was ended. If the shift is still ongoing you can omit this field.                                                                                                                       |
| `metadata`                                                                                                                                                                                                                   | Dict[str, *str*]                                                                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                           | Metadata associated with the time sheet. Key-value pairs of arbitrary data. Both keys and values must be strings.                                                                                                            |
| `entries`                                                                                                                                                                                                                    | List[[models.PostCompaniesCompanyUUIDTimeTrackingTimeSheetsEntries](../../models/postcompaniescompanyuuidtimetrackingtimesheetsentries.md)]                                                                                  | :heavy_minus_sign:                                                                                                                                                                                                           | Entries associated with the time sheet.                                                                                                                                                                                      |
| `retries`                                                                                                                                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                           | Configuration to override the default retry behavior of the client.                                                                                                                                                          |

### Response

**[models.TimeSheet](../../models/timesheet.md)**

### Errors

| Error Type                            | Status Code                           | Content Type                          |
| ------------------------------------- | ------------------------------------- | ------------------------------------- |
| models.UnprocessableEntityErrorObject | 422                                   | application/json                      |
| models.APIError                       | 4XX, 5XX                              | \*/\*                                 |

## get_time_tracking_time_sheets_time_sheet_uuid

Fetch a time sheet.

Time sheets represent the time worked by an employee or contractor for a given time range.
Hours are classified by pay classification, and can be regular, overtime, or double overtime.

scope: `time_sheet:read`

### Example Usage

<!-- UsageSnippet language="python" operationID="get-time_tracking-time_sheets-time_sheet_uuid" method="get" path="/v1/time_tracking/time_sheets/{time_sheet_uuid}" example="example" -->
```python
import gusto_app_integration
from gusto_app_integration import GustoAppIntegration


with GustoAppIntegration(
    company_access_auth="<YOUR_BEARER_TOKEN_HERE>",
) as gai_client:

    res = gai_client.time_tracking.get_time_tracking_time_sheets_time_sheet_uuid(time_sheet_uuid="<id>", x_gusto_api_version=gusto_app_integration.VersionHeader.TWO_THOUSAND_AND_TWENTY_FIVE_MINUS_06_MINUS_15)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                    | Type                                                                                                                                                                                                                         | Required                                                                                                                                                                                                                     | Description                                                                                                                                                                                                                  |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `time_sheet_uuid`                                                                                                                                                                                                            | *str*                                                                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                                           | UUID of the time sheet                                                                                                                                                                                                       |
| `x_gusto_api_version`                                                                                                                                                                                                        | [Optional[models.VersionHeader]](../../models/versionheader.md)                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                           | Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used. |
| `retries`                                                                                                                                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                           | Configuration to override the default retry behavior of the client.                                                                                                                                                          |

### Response

**[models.TimeSheet](../../models/timesheet.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## put_time_tracking_time_sheets_time_sheet_uuid

Update a time sheet.

Time sheets represent the time worked by an employee or contractor for a given time range.
Hours are classified by pay classification, and can be regular, overtime, or double overtime.

scope: `time_sheet:write`

### Example Usage: Basic

<!-- UsageSnippet language="python" operationID="put-time_tracking-time_sheets-time_sheet_uuid" method="put" path="/v1/time_tracking/time_sheets/{time_sheet_uuid}" example="Basic" -->
```python
import gusto_app_integration
from gusto_app_integration import GustoAppIntegration


with GustoAppIntegration(
    company_access_auth="<YOUR_BEARER_TOKEN_HERE>",
) as gai_client:

    res = gai_client.time_tracking.put_time_tracking_time_sheets_time_sheet_uuid(time_sheet_uuid="<id>", version="56d00c178bc7393b2a206ed6a86afcb4", x_gusto_api_version=gusto_app_integration.VersionHeader.TWO_THOUSAND_AND_TWENTY_FIVE_MINUS_06_MINUS_15)

    # Handle response
    print(res)

```
### Example Usage: Example

<!-- UsageSnippet language="python" operationID="put-time_tracking-time_sheets-time_sheet_uuid" method="put" path="/v1/time_tracking/time_sheets/{time_sheet_uuid}" example="Example" -->
```python
import gusto_app_integration
from gusto_app_integration import GustoAppIntegration
from gusto_app_integration.utils import parse_datetime


with GustoAppIntegration(
    company_access_auth="<YOUR_BEARER_TOKEN_HERE>",
) as gai_client:

    res = gai_client.time_tracking.put_time_tracking_time_sheets_time_sheet_uuid(time_sheet_uuid="<id>", version="72deb67e16f7b92713c00d3582fa6c68", x_gusto_api_version=gusto_app_integration.VersionHeader.TWO_THOUSAND_AND_TWENTY_FIVE_MINUS_06_MINUS_15, entity_uuid="123e4567-e89b-12d3-a456-426614174000", entity_type="Employee", job_uuid="123e4567-e89b-12d3-a456-426614174000", time_zone="America/New_York", shift_started_at=parse_datetime("2024-06-10T09:00:00Z"), shift_ended_at=parse_datetime("2024-06-10T17:00:00Z"), metadata={
        "custom_field": "custom value",
    }, entries=[
        {
            "uuid": "123e4567-e89b-12d3-a456-426614174000",
            "hours_worked": 1.5,
        },
    ])

    # Handle response
    print(res)

```
### Example Usage: Nested

<!-- UsageSnippet language="python" operationID="put-time_tracking-time_sheets-time_sheet_uuid" method="put" path="/v1/time_tracking/time_sheets/{time_sheet_uuid}" example="Nested" -->
```python
import gusto_app_integration
from gusto_app_integration import GustoAppIntegration


with GustoAppIntegration(
    company_access_auth="<YOUR_BEARER_TOKEN_HERE>",
) as gai_client:

    res = gai_client.time_tracking.put_time_tracking_time_sheets_time_sheet_uuid(time_sheet_uuid="<id>", version="56d00c178bc7393b2a206ed6a86afcb4", x_gusto_api_version=gusto_app_integration.VersionHeader.TWO_THOUSAND_AND_TWENTY_FIVE_MINUS_06_MINUS_15)

    # Handle response
    print(res)

```
### Example Usage: Resource

<!-- UsageSnippet language="python" operationID="put-time_tracking-time_sheets-time_sheet_uuid" method="put" path="/v1/time_tracking/time_sheets/{time_sheet_uuid}" example="Resource" -->
```python
import gusto_app_integration
from gusto_app_integration import GustoAppIntegration


with GustoAppIntegration(
    company_access_auth="<YOUR_BEARER_TOKEN_HERE>",
) as gai_client:

    res = gai_client.time_tracking.put_time_tracking_time_sheets_time_sheet_uuid(time_sheet_uuid="<id>", version="56d00c178bc7393b2a206ed6a86afcb4", x_gusto_api_version=gusto_app_integration.VersionHeader.TWO_THOUSAND_AND_TWENTY_FIVE_MINUS_06_MINUS_15)

    # Handle response
    print(res)

```
### Example Usage: example

<!-- UsageSnippet language="python" operationID="put-time_tracking-time_sheets-time_sheet_uuid" method="put" path="/v1/time_tracking/time_sheets/{time_sheet_uuid}" example="example" -->
```python
import gusto_app_integration
from gusto_app_integration import GustoAppIntegration


with GustoAppIntegration(
    company_access_auth="<YOUR_BEARER_TOKEN_HERE>",
) as gai_client:

    res = gai_client.time_tracking.put_time_tracking_time_sheets_time_sheet_uuid(time_sheet_uuid="<id>", version="56d00c178bc7393b2a206ed6a86afcb4", x_gusto_api_version=gusto_app_integration.VersionHeader.TWO_THOUSAND_AND_TWENTY_FIVE_MINUS_06_MINUS_15)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                    | Type                                                                                                                                                                                                                         | Required                                                                                                                                                                                                                     | Description                                                                                                                                                                                                                  | Example                                                                                                                                                                                                                      |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `time_sheet_uuid`                                                                                                                                                                                                            | *str*                                                                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                                           | UUID of the time sheet                                                                                                                                                                                                       |                                                                                                                                                                                                                              |
| `version`                                                                                                                                                                                                                    | *str*                                                                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                                           | The current version of the object. See the [versioning guide](https://docs.gusto.com/embedded-payroll/docs/idempotency) for information on how to use this field.                                                            | 56d00c178bc7393b2a206ed6a86afcb4                                                                                                                                                                                             |
| `x_gusto_api_version`                                                                                                                                                                                                        | [Optional[models.VersionHeader]](../../models/versionheader.md)                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                           | Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used. |                                                                                                                                                                                                                              |
| `entity_uuid`                                                                                                                                                                                                                | *Optional[str]*                                                                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                           | Unique identifier of the entity associated with the time sheet.                                                                                                                                                              |                                                                                                                                                                                                                              |
| `entity_type`                                                                                                                                                                                                                | *Optional[str]*                                                                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                           | Type of entity associated with the time sheet.                                                                                                                                                                               |                                                                                                                                                                                                                              |
| `job_uuid`                                                                                                                                                                                                                   | *Optional[str]*                                                                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                           | Unique identifier of the job for which time was tracked. Currently is only supported for employees.                                                                                                                          |                                                                                                                                                                                                                              |
| `time_zone`                                                                                                                                                                                                                  | *Optional[str]*                                                                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                           | Time zone of where the time was tracked.                                                                                                                                                                                     |                                                                                                                                                                                                                              |
| `shift_started_at`                                                                                                                                                                                                           | [date](https://docs.python.org/3/library/datetime.html#date-objects)                                                                                                                                                         | :heavy_minus_sign:                                                                                                                                                                                                           | The start time of the shift. Timestamp should be in ISO8601                                                                                                                                                                  |                                                                                                                                                                                                                              |
| `shift_ended_at`                                                                                                                                                                                                             | [date](https://docs.python.org/3/library/datetime.html#date-objects)                                                                                                                                                         | :heavy_minus_sign:                                                                                                                                                                                                           | The end time of the shift. If the shift is still ongoing this will be null.                                                                                                                                                  |                                                                                                                                                                                                                              |
| `metadata`                                                                                                                                                                                                                   | Dict[str, *str*]                                                                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                           | Metadata associated with the time sheet. Key-value pairs of arbitrary data. Both keys and values must be strings.                                                                                                            |                                                                                                                                                                                                                              |
| `entries`                                                                                                                                                                                                                    | List[[models.PutTimeTrackingTimeSheetsTimeSheetUUIDEntries](../../models/puttimetrackingtimesheetstimesheetuuidentries.md)]                                                                                                  | :heavy_minus_sign:                                                                                                                                                                                                           | Entries associated with the time sheet.                                                                                                                                                                                      |                                                                                                                                                                                                                              |
| `retries`                                                                                                                                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                           | Configuration to override the default retry behavior of the client.                                                                                                                                                          |                                                                                                                                                                                                                              |

### Response

**[models.TimeSheet](../../models/timesheet.md)**

### Errors

| Error Type                            | Status Code                           | Content Type                          |
| ------------------------------------- | ------------------------------------- | ------------------------------------- |
| models.UnprocessableEntityErrorObject | 422                                   | application/json                      |
| models.APIError                       | 4XX, 5XX                              | \*/\*                                 |

## delete_time_tracking_time_sheets_time_sheet_uuid

Delete a company's time sheet.

Time sheets represent the time worked by an employee or contractor for a given time range.
Hours are classified by pay classification, and can be regular, overtime, or double overtime.

scope: `time_sheet:write`

### Example Usage

<!-- UsageSnippet language="python" operationID="delete-time_tracking-time_sheets-time_sheet_uuid" method="delete" path="/v1/time_tracking/time_sheets/{time_sheet_uuid}" -->
```python
import gusto_app_integration
from gusto_app_integration import GustoAppIntegration


with GustoAppIntegration(
    company_access_auth="<YOUR_BEARER_TOKEN_HERE>",
) as gai_client:

    gai_client.time_tracking.delete_time_tracking_time_sheets_time_sheet_uuid(time_sheet_uuid="<id>", version="<value>", x_gusto_api_version=gusto_app_integration.VersionHeader.TWO_THOUSAND_AND_TWENTY_FIVE_MINUS_06_MINUS_15)

    # Use the SDK ...

```

### Parameters

| Parameter                                                                                                                                                                                                                    | Type                                                                                                                                                                                                                         | Required                                                                                                                                                                                                                     | Description                                                                                                                                                                                                                  |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `time_sheet_uuid`                                                                                                                                                                                                            | *str*                                                                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                                           | UUID of the time sheet                                                                                                                                                                                                       |
| `version`                                                                                                                                                                                                                    | *str*                                                                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                                           | The current version of the object. See the [versioning guide](https://docs.gusto.com/embedded-payroll/docs/idempotency) for information on how to use this field.                                                            |
| `x_gusto_api_version`                                                                                                                                                                                                        | [Optional[models.VersionHeader]](../../models/versionheader.md)                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                           | Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used. |
| `retries`                                                                                                                                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                           | Configuration to override the default retry behavior of the client.                                                                                                                                                          |

### Errors

| Error Type                            | Status Code                           | Content Type                          |
| ------------------------------------- | ------------------------------------- | ------------------------------------- |
| models.UnprocessableEntityErrorObject | 422                                   | application/json                      |
| models.APIError                       | 4XX, 5XX                              | \*/\*                                 |

## post_companies_company_uuid_time_tracking_payroll_syncs

Initiate a payroll sync for a company.

A payroll sync takes approved time sheet data and syncs it to the company's payroll.

### Asynchronous processing
This endpoint triggers an asynchronous operation — the response will return immediately with a status of `pending` while the sync processes in the background.

**To track completion:**

Subscribe (via [POST /v1/webhook_subscriptions](ref:post-v1-webhook-subscription)) to `PayrollSync` webhook events

scope: `payroll_syncs:write`

### Example Usage

<!-- UsageSnippet language="python" operationID="post-companies-company_uuid-time_tracking-payroll_syncs" method="post" path="/v1/companies/{company_id}/time_tracking/payroll_syncs" -->
```python
from datetime import date
import gusto_app_integration
from gusto_app_integration import GustoAppIntegration


with GustoAppIntegration(
    company_access_auth="<YOUR_BEARER_TOKEN_HERE>",
) as gai_client:

    res = gai_client.time_tracking.post_companies_company_uuid_time_tracking_payroll_syncs(company_id="<id>", kind=gusto_app_integration.Kind.REGULAR, pay_schedule_uuid="123e4567-e89b-12d3-a456-426614174000", pay_period_start_date=date.fromisoformat("2025-01-01"), pay_period_end_date=date.fromisoformat("2025-01-15"), x_gusto_api_version=gusto_app_integration.PostCompaniesCompanyUUIDTimeTrackingPayrollSyncsHeaderXGustoAPIVersion.TWO_THOUSAND_AND_TWENTY_FIVE_MINUS_06_MINUS_15)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                    | Type                                                                                                                                                                                                                         | Required                                                                                                                                                                                                                     | Description                                                                                                                                                                                                                  | Example                                                                                                                                                                                                                      |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `company_id`                                                                                                                                                                                                                 | *str*                                                                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                                           | The UUID of the company                                                                                                                                                                                                      |                                                                                                                                                                                                                              |
| `kind`                                                                                                                                                                                                                       | [models.Kind](../../models/kind.md)                                                                                                                                                                                          | :heavy_check_mark:                                                                                                                                                                                                           | The kind of payroll sync.<br/>- `regular`: A regular payroll sync<br/>                                                                                                                                                       | regular                                                                                                                                                                                                                      |
| `pay_schedule_uuid`                                                                                                                                                                                                          | *str*                                                                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                                           | Unique identifier of the pay schedule to sync time sheets for.                                                                                                                                                               | 123e4567-e89b-12d3-a456-426614174000                                                                                                                                                                                         |
| `pay_period_start_date`                                                                                                                                                                                                      | [datetime](https://docs.python.org/3/library/datetime.html#datetime-objects)                                                                                                                                                 | :heavy_check_mark:                                                                                                                                                                                                           | The start date of the pay period per ISO 8601 format.                                                                                                                                                                        | 2025-01-01                                                                                                                                                                                                                   |
| `pay_period_end_date`                                                                                                                                                                                                        | [datetime](https://docs.python.org/3/library/datetime.html#datetime-objects)                                                                                                                                                 | :heavy_check_mark:                                                                                                                                                                                                           | The end date of the pay period per ISO 8601 format.                                                                                                                                                                          | 2025-01-15                                                                                                                                                                                                                   |
| `x_gusto_api_version`                                                                                                                                                                                                        | [Optional[models.PostCompaniesCompanyUUIDTimeTrackingPayrollSyncsHeaderXGustoAPIVersion]](../../models/postcompaniescompanyuuidtimetrackingpayrollsyncsheaderxgustoapiversion.md)                                            | :heavy_minus_sign:                                                                                                                                                                                                           | Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used. |                                                                                                                                                                                                                              |
| `retries`                                                                                                                                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                           | Configuration to override the default retry behavior of the client.                                                                                                                                                          |                                                                                                                                                                                                                              |

### Response

**[models.PayrollSync](../../models/payrollsync.md)**

### Errors

| Error Type                            | Status Code                           | Content Type                          |
| ------------------------------------- | ------------------------------------- | ------------------------------------- |
| models.NotFoundErrorObject            | 404                                   | application/json                      |
| models.UnprocessableEntityErrorObject | 422                                   | application/json                      |
| models.APIError                       | 4XX, 5XX                              | \*/\*                                 |

## get_time_tracking_payroll_syncs_payroll_sync_uuid

Fetch a payroll sync.

A payroll sync represents the result of syncing approved time sheet data to payroll. Use this endpoint to check the status of a previously initiated sync.

scope: `payroll_syncs:read`

### Example Usage

<!-- UsageSnippet language="python" operationID="get-time_tracking-payroll_syncs-payroll_sync_uuid" method="get" path="/v1/time_tracking/payroll_syncs/{payroll_sync_uuid}" -->
```python
import gusto_app_integration
from gusto_app_integration import GustoAppIntegration


with GustoAppIntegration(
    company_access_auth="<YOUR_BEARER_TOKEN_HERE>",
) as gai_client:

    res = gai_client.time_tracking.get_time_tracking_payroll_syncs_payroll_sync_uuid(payroll_sync_uuid="7b1d0df1-6403-4a06-8768-c1dd7d24d27a", x_gusto_api_version=gusto_app_integration.GetTimeTrackingPayrollSyncsPayrollSyncUUIDHeaderXGustoAPIVersion.TWO_THOUSAND_AND_TWENTY_FIVE_MINUS_06_MINUS_15)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                    | Type                                                                                                                                                                                                                         | Required                                                                                                                                                                                                                     | Description                                                                                                                                                                                                                  | Example                                                                                                                                                                                                                      |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `payroll_sync_uuid`                                                                                                                                                                                                          | *str*                                                                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                                           | The UUID of the payroll sync                                                                                                                                                                                                 | 7b1d0df1-6403-4a06-8768-c1dd7d24d27a                                                                                                                                                                                         |
| `x_gusto_api_version`                                                                                                                                                                                                        | [Optional[models.GetTimeTrackingPayrollSyncsPayrollSyncUUIDHeaderXGustoAPIVersion]](../../models/gettimetrackingpayrollsyncspayrollsyncuuidheaderxgustoapiversion.md)                                                        | :heavy_minus_sign:                                                                                                                                                                                                           | Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used. |                                                                                                                                                                                                                              |
| `retries`                                                                                                                                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                           | Configuration to override the default retry behavior of the client.                                                                                                                                                          |                                                                                                                                                                                                                              |

### Response

**[models.PayrollSync](../../models/payrollsync.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.NotFoundErrorObject | 404                        | application/json           |
| models.APIError            | 4XX, 5XX                   | \*/\*                      |