# TimeTracking
(*time_tracking*)

## Overview

### Available Operations

* [get_companies_company_uuid_time_tracking_time_sheets](#get_companies_company_uuid_time_tracking_time_sheets) - Get all time sheets for a company
* [post_companies_company_uuid_time_tracking_time_sheets](#post_companies_company_uuid_time_tracking_time_sheets) - Create a time sheet
* [get_time_tracking_time_sheets_time_sheet_uuid](#get_time_tracking_time_sheets_time_sheet_uuid) - Get a time sheet
* [put_time_tracking_time_sheets_time_sheet_uuid](#put_time_tracking_time_sheets_time_sheet_uuid) - Update a time sheet
* [delete_time_tracking_time_sheets_time_sheet_uuid](#delete_time_tracking_time_sheets_time_sheet_uuid) - Delete a time sheet

## get_companies_company_uuid_time_tracking_time_sheets

Fetch all company's time sheets.

Time sheets represent the time worked by an employee or contractor for a given time range.
Hours are classified by pay classification, and can be regular, overtime, or double overtime.

scope: `time_sheet:read`

### Example Usage

```python
from gusto_app_integration import GustoAppIntegration


with GustoAppIntegration(
    company_access_auth="<YOUR_BEARER_TOKEN_HERE>",
) as gai_client:

    res = gai_client.time_tracking.get_companies_company_uuid_time_tracking_time_sheets(company_uuid="<id>")

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
| `sort_order`                                                                                                                                                                                                                 | [Optional[models.TimeSheetSortOrder]](../../models/timesheetsortorder.md)                                                                                                                                                    | :heavy_minus_sign:                                                                                                                                                                                                           | Sortinng order. One of: "asc", "desc"                                                                                                                                                                                        |
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

### Example Usage

```python
import gusto_app_integration
from gusto_app_integration import GustoAppIntegration
from gusto_app_integration.utils import parse_datetime


with GustoAppIntegration(
    company_access_auth="<YOUR_BEARER_TOKEN_HERE>",
) as gai_client:

    res = gai_client.time_tracking.post_companies_company_uuid_time_tracking_time_sheets(company_uuid="<id>", entity_uuid="123e4567-e89b-12d3-a456-426614174000", entity_type="Employee", time_zone="America/New_York", shift_started_at=parse_datetime("2024-06-10T09:00:00Z"), job_uuid="123e4567-e89b-12d3-a456-426614174000", shift_ended_at=parse_datetime("2024-06-10T17:00:00Z"), metadata={
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

```python
from gusto_app_integration import GustoAppIntegration


with GustoAppIntegration(
    company_access_auth="<YOUR_BEARER_TOKEN_HERE>",
) as gai_client:

    res = gai_client.time_tracking.get_time_tracking_time_sheets_time_sheet_uuid(time_sheet_uuid="<id>")

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

### Example Usage

```python
from gusto_app_integration import GustoAppIntegration
from gusto_app_integration.utils import parse_datetime


with GustoAppIntegration(
    company_access_auth="<YOUR_BEARER_TOKEN_HERE>",
) as gai_client:

    res = gai_client.time_tracking.put_time_tracking_time_sheets_time_sheet_uuid(time_sheet_uuid="<id>", version="72deb67e16f7b92713c00d3582fa6c68", entity_uuid="123e4567-e89b-12d3-a456-426614174000", entity_type="Employee", job_uuid="123e4567-e89b-12d3-a456-426614174000", time_zone="America/New_York", shift_started_at=parse_datetime("2024-06-10T09:00:00Z"), shift_ended_at=parse_datetime("2024-06-10T17:00:00Z"), metadata={
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

### Parameters

| Parameter                                                                                                                                                                                                                    | Type                                                                                                                                                                                                                         | Required                                                                                                                                                                                                                     | Description                                                                                                                                                                                                                  |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `time_sheet_uuid`                                                                                                                                                                                                            | *str*                                                                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                                           | UUID of the time sheet                                                                                                                                                                                                       |
| `version`                                                                                                                                                                                                                    | *str*                                                                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                                           | The current version of the object. See the [versioning guide](https://docs.gusto.com/embedded-payroll/docs/idempotency) for information on how to use this field.                                                            |
| `x_gusto_api_version`                                                                                                                                                                                                        | [Optional[models.VersionHeader]](../../models/versionheader.md)                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                           | Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used. |
| `entity_uuid`                                                                                                                                                                                                                | *Optional[str]*                                                                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                           | Unique identifier of the entity associated with the time sheet.                                                                                                                                                              |
| `entity_type`                                                                                                                                                                                                                | *Optional[str]*                                                                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                           | Type of entity associated with the time sheet.                                                                                                                                                                               |
| `job_uuid`                                                                                                                                                                                                                   | *Optional[str]*                                                                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                           | Unique identifier of the job for which time was tracked. Currently is only supported for employees.                                                                                                                          |
| `time_zone`                                                                                                                                                                                                                  | *Optional[str]*                                                                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                           | Time zone of where the time was tracked.                                                                                                                                                                                     |
| `shift_started_at`                                                                                                                                                                                                           | [date](https://docs.python.org/3/library/datetime.html#date-objects)                                                                                                                                                         | :heavy_minus_sign:                                                                                                                                                                                                           | The start time of the shift. Timestamp should be in ISO8601                                                                                                                                                                  |
| `shift_ended_at`                                                                                                                                                                                                             | [date](https://docs.python.org/3/library/datetime.html#date-objects)                                                                                                                                                         | :heavy_minus_sign:                                                                                                                                                                                                           | The end time of the shift. If the shift is still ongoing this will be null.                                                                                                                                                  |
| `metadata`                                                                                                                                                                                                                   | Dict[str, *str*]                                                                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                           | Metadata associated with the time sheet. Key-value pairs of arbitrary data. Both keys and values must be strings.                                                                                                            |
| `entries`                                                                                                                                                                                                                    | List[[models.PutTimeTrackingTimeSheetsTimeSheetUUIDEntries](../../models/puttimetrackingtimesheetstimesheetuuidentries.md)]                                                                                                  | :heavy_minus_sign:                                                                                                                                                                                                           | Entries associated with the time sheet.                                                                                                                                                                                      |
| `retries`                                                                                                                                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                           | Configuration to override the default retry behavior of the client.                                                                                                                                                          |

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

```python
from gusto_app_integration import GustoAppIntegration


with GustoAppIntegration(
    company_access_auth="<YOUR_BEARER_TOKEN_HERE>",
) as gai_client:

    gai_client.time_tracking.delete_time_tracking_time_sheets_time_sheet_uuid(time_sheet_uuid="<id>", version="<value>")

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