# TimeOffRequests

## Overview

### Available Operations

* [post_v1_companies_company_uuid_time_off_admin_approved_requests](#post_v1_companies_company_uuid_time_off_admin_approved_requests) - Create an admin-approved time off request
* [get_v1_companies_company_uuid_time_off_balances](#get_v1_companies_company_uuid_time_off_balances) - Get time off balances for a company
* [get_v1_companies_company_uuid_time_off_requests](#get_v1_companies_company_uuid_time_off_requests) - List time off requests for a company
* [post_v1_companies_company_uuid_time_off_requests](#post_v1_companies_company_uuid_time_off_requests) - Create a time off request
* [post_v1_companies_company_uuid_time_off_requests_preview](#post_v1_companies_company_uuid_time_off_requests_preview) - Preview a time off request
* [get_v1_time_off_requests_time_off_request_uuid](#get_v1_time_off_requests_time_off_request_uuid) - Get a time off request
* [delete_v1_time_off_requests_time_off_request_uuid](#delete_v1_time_off_requests_time_off_request_uuid) - Delete a time off request
* [put_v1_time_off_requests_time_off_request_uuid_approve](#put_v1_time_off_requests_time_off_request_uuid_approve) - Approve a time off request
* [put_v1_time_off_requests_time_off_request_uuid_decline](#put_v1_time_off_requests_time_off_request_uuid_decline) - Decline a time off request

## post_v1_companies_company_uuid_time_off_admin_approved_requests

Create a pre-approved time off request on behalf of an employee (admin or system initiated).
The request is always created with approved status.

scope: `time_off_requests:manage`

### Example Usage

<!-- UsageSnippet language="python" operationID="post-v1-companies-company_uuid-time_off-admin_approved_requests" method="post" path="/v1/companies/{company_uuid}/time_off/admin_approved_requests" -->
```python
import gusto_embedded
from gusto_embedded import Gusto
import os


with Gusto(
    company_access_auth=os.getenv("GUSTO_COMPANY_ACCESS_AUTH", ""),
) as gusto:

    res = gusto.time_off_requests.post_v1_companies_company_uuid_time_off_admin_approved_requests(company_uuid="<id>", employee_uuid="<id>", policy_uuid="<id>", start_date="<value>", end_date="<value>", days={
        "key": "<value>",
        "key1": "<value>",
        "key2": "<value>",
    }, x_gusto_api_version=gusto_embedded.PostV1CompaniesCompanyUUIDTimeOffAdminApprovedRequestsHeaderXGustoAPIVersion.TWO_THOUSAND_AND_TWENTY_FIVE_MINUS_06_MINUS_15)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                    | Type                                                                                                                                                                                                                         | Required                                                                                                                                                                                                                     | Description                                                                                                                                                                                                                  |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `company_uuid`                                                                                                                                                                                                               | *str*                                                                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                                           | The UUID of the company                                                                                                                                                                                                      |
| `employee_uuid`                                                                                                                                                                                                              | *str*                                                                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                                           | The UUID of the employee                                                                                                                                                                                                     |
| `policy_uuid`                                                                                                                                                                                                                | *str*                                                                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                                           | The UUID of the time off policy                                                                                                                                                                                              |
| `start_date`                                                                                                                                                                                                                 | *str*                                                                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                                           | The start date of the time off request (YYYY-MM-DD)                                                                                                                                                                          |
| `end_date`                                                                                                                                                                                                                   | *str*                                                                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                                           | The end date of the time off request (YYYY-MM-DD)                                                                                                                                                                            |
| `days`                                                                                                                                                                                                                       | Dict[str, *str*]                                                                                                                                                                                                             | :heavy_check_mark:                                                                                                                                                                                                           | An object where keys are dates in YYYY-MM-DD format and values are hours as string decimals (e.g. {"2025-01-20": "8.000"})                                                                                                   |
| `x_gusto_api_version`                                                                                                                                                                                                        | [Optional[models.PostV1CompaniesCompanyUUIDTimeOffAdminApprovedRequestsHeaderXGustoAPIVersion]](../../models/postv1companiescompanyuuidtimeoffadminapprovedrequestsheaderxgustoapiversion.md)                                | :heavy_minus_sign:                                                                                                                                                                                                           | Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used. |
| `employer_note`                                                                                                                                                                                                              | *Optional[str]*                                                                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                           | A note from the employer about the request                                                                                                                                                                                   |
| `approver_uuid`                                                                                                                                                                                                              | *Optional[str]*                                                                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                           | The UUID of the approving admin. Defaults to the primary payroll admin.                                                                                                                                                      |
| `retries`                                                                                                                                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                           | Configuration to override the default retry behavior of the client.                                                                                                                                                          |

### Response

**[models.EmbeddedTimeOffRequest](../../models/embeddedtimeoffrequest.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.NotFoundErrorObject | 404                        | application/json           |
| models.APIError            | 4XX, 5XX                   | \*/\*                      |

## get_v1_companies_company_uuid_time_off_balances

Get time off balances for all employees in a company

scope: `time_off_requests:read`

### Example Usage

<!-- UsageSnippet language="python" operationID="get-v1-companies-company_uuid-time_off-balances" method="get" path="/v1/companies/{company_uuid}/time_off/balances" -->
```python
import gusto_embedded
from gusto_embedded import Gusto
import os


with Gusto(
    company_access_auth=os.getenv("GUSTO_COMPANY_ACCESS_AUTH", ""),
) as gusto:

    res = gusto.time_off_requests.get_v1_companies_company_uuid_time_off_balances(company_uuid="<id>", x_gusto_api_version=gusto_embedded.GetV1CompaniesCompanyUUIDTimeOffBalancesHeaderXGustoAPIVersion.TWO_THOUSAND_AND_TWENTY_FIVE_MINUS_06_MINUS_15)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                    | Type                                                                                                                                                                                                                         | Required                                                                                                                                                                                                                     | Description                                                                                                                                                                                                                  |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `company_uuid`                                                                                                                                                                                                               | *str*                                                                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                                           | The UUID of the company                                                                                                                                                                                                      |
| `x_gusto_api_version`                                                                                                                                                                                                        | [Optional[models.GetV1CompaniesCompanyUUIDTimeOffBalancesHeaderXGustoAPIVersion]](../../models/getv1companiescompanyuuidtimeoffbalancesheaderxgustoapiversion.md)                                                            | :heavy_minus_sign:                                                                                                                                                                                                           | Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used. |
| `employee_uuids`                                                                                                                                                                                                             | *Optional[str]*                                                                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                           | Filter by employee UUIDs (comma-separated)                                                                                                                                                                                   |
| `policy_uuids`                                                                                                                                                                                                               | *Optional[str]*                                                                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                           | Filter by time off policy UUIDs (comma-separated)                                                                                                                                                                            |
| `page`                                                                                                                                                                                                                       | *Optional[int]*                                                                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                           | The page that is requested                                                                                                                                                                                                   |
| `per`                                                                                                                                                                                                                        | *Optional[int]*                                                                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                           | Number of objects per page                                                                                                                                                                                                   |
| `retries`                                                                                                                                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                           | Configuration to override the default retry behavior of the client.                                                                                                                                                          |

### Response

**[List[models.EmbeddedTimeOffBalance]](../../models/.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.NotFoundErrorObject | 404                        | application/json           |
| models.APIError            | 4XX, 5XX                   | \*/\*                      |

## get_v1_companies_company_uuid_time_off_requests

Get all time off requests for a company. Supports filtering by status, employee, and date ranges.

Possible statuses:
- `pending` — awaiting approval
- `approved` — approved by an admin but not yet processed in a payroll
- `declined` — declined by an admin
- `consumed` — processed in a completed payroll

Allowed values for `status`: pending, approved, declined, consumed.

scope: `time_off_requests:read`

### Example Usage

<!-- UsageSnippet language="python" operationID="get-v1-companies-company_uuid-time_off-requests" method="get" path="/v1/companies/{company_uuid}/time_off/requests" -->
```python
import gusto_embedded
from gusto_embedded import Gusto
import os


with Gusto(
    company_access_auth=os.getenv("GUSTO_COMPANY_ACCESS_AUTH", ""),
) as gusto:

    res = gusto.time_off_requests.get_v1_companies_company_uuid_time_off_requests(company_uuid="<id>", x_gusto_api_version=gusto_embedded.GetV1CompaniesCompanyUUIDTimeOffRequestsHeaderXGustoAPIVersion.TWO_THOUSAND_AND_TWENTY_FIVE_MINUS_06_MINUS_15)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                    | Type                                                                                                                                                                                                                         | Required                                                                                                                                                                                                                     | Description                                                                                                                                                                                                                  |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `company_uuid`                                                                                                                                                                                                               | *str*                                                                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                                           | The UUID of the company                                                                                                                                                                                                      |
| `x_gusto_api_version`                                                                                                                                                                                                        | [Optional[models.GetV1CompaniesCompanyUUIDTimeOffRequestsHeaderXGustoAPIVersion]](../../models/getv1companiescompanyuuidtimeoffrequestsheaderxgustoapiversion.md)                                                            | :heavy_minus_sign:                                                                                                                                                                                                           | Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used. |
| `employee_uuids`                                                                                                                                                                                                             | *Optional[str]*                                                                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                           | Filter by employee UUIDs. Comma-separated for multiple values.                                                                                                                                                               |
| `status`                                                                                                                                                                                                                     | *Optional[str]*                                                                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                           | Filter by request status. Comma-separated for multiple values (e.g. pending,approved,declined,consumed).                                                                                                                     |
| `start_date`                                                                                                                                                                                                                 | *Optional[str]*                                                                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                           | Filter requests that overlap with this start date                                                                                                                                                                            |
| `end_date`                                                                                                                                                                                                                   | *Optional[str]*                                                                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                           | Filter requests that overlap with this end date                                                                                                                                                                              |
| `sort_order`                                                                                                                                                                                                                 | *Optional[str]*                                                                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                           | Sort order by start_date (asc or desc, defaults to desc)                                                                                                                                                                     |
| `page`                                                                                                                                                                                                                       | *Optional[int]*                                                                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                           | The page that is requested                                                                                                                                                                                                   |
| `per`                                                                                                                                                                                                                        | *Optional[int]*                                                                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                           | Number of objects per page                                                                                                                                                                                                   |
| `retries`                                                                                                                                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                           | Configuration to override the default retry behavior of the client.                                                                                                                                                          |

### Response

**[List[models.EmbeddedTimeOffRequest]](../../models/.md)**

### Errors

| Error Type                       | Status Code                      | Content Type                     |
| -------------------------------- | -------------------------------- | -------------------------------- |
| models.NotFoundErrorObject       | 404                              | application/json                 |
| models.UnprocessableEntityError1 | 422                              | application/json                 |
| models.APIError                  | 4XX, 5XX                         | \*/\*                            |

## post_v1_companies_company_uuid_time_off_requests

Create a time off request for an employee

scope: `time_off_requests:write`

### Example Usage

<!-- UsageSnippet language="python" operationID="post-v1-companies-company_uuid-time_off-requests" method="post" path="/v1/companies/{company_uuid}/time_off/requests" -->
```python
import gusto_embedded
from gusto_embedded import Gusto
import os


with Gusto(
    company_access_auth=os.getenv("GUSTO_COMPANY_ACCESS_AUTH", ""),
) as gusto:

    res = gusto.time_off_requests.post_v1_companies_company_uuid_time_off_requests(company_uuid="<id>", employee_uuid="<id>", policy_uuid="<id>", start_date="<value>", end_date="<value>", days={
        "key": "<value>",
        "key1": "<value>",
        "key2": "<value>",
    }, x_gusto_api_version=gusto_embedded.PostV1CompaniesCompanyUUIDTimeOffRequestsHeaderXGustoAPIVersion.TWO_THOUSAND_AND_TWENTY_FIVE_MINUS_06_MINUS_15)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                    | Type                                                                                                                                                                                                                         | Required                                                                                                                                                                                                                     | Description                                                                                                                                                                                                                  |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `company_uuid`                                                                                                                                                                                                               | *str*                                                                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                                           | The UUID of the company                                                                                                                                                                                                      |
| `employee_uuid`                                                                                                                                                                                                              | *str*                                                                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                                           | The UUID of the employee                                                                                                                                                                                                     |
| `policy_uuid`                                                                                                                                                                                                                | *str*                                                                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                                           | The UUID of the time off policy                                                                                                                                                                                              |
| `start_date`                                                                                                                                                                                                                 | *str*                                                                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                                           | The start date of the time off request (YYYY-MM-DD)                                                                                                                                                                          |
| `end_date`                                                                                                                                                                                                                   | *str*                                                                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                                           | The end date of the time off request (YYYY-MM-DD)                                                                                                                                                                            |
| `days`                                                                                                                                                                                                                       | Dict[str, *str*]                                                                                                                                                                                                             | :heavy_check_mark:                                                                                                                                                                                                           | An object where keys are dates in YYYY-MM-DD format and values are hours as string decimals (e.g. {"2025-01-20": "8.000"})                                                                                                   |
| `x_gusto_api_version`                                                                                                                                                                                                        | [Optional[models.PostV1CompaniesCompanyUUIDTimeOffRequestsHeaderXGustoAPIVersion]](../../models/postv1companiescompanyuuidtimeoffrequestsheaderxgustoapiversion.md)                                                          | :heavy_minus_sign:                                                                                                                                                                                                           | Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used. |
| `employee_note`                                                                                                                                                                                                              | *Optional[str]*                                                                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                           | A note from the employee about the request                                                                                                                                                                                   |
| `retries`                                                                                                                                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                           | Configuration to override the default retry behavior of the client.                                                                                                                                                          |

### Response

**[models.EmbeddedTimeOffRequest](../../models/embeddedtimeoffrequest.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.NotFoundErrorObject | 404                        | application/json           |
| models.APIError            | 4XX, 5XX                   | \*/\*                      |

## post_v1_companies_company_uuid_time_off_requests_preview

Preview a time off request to see balance impact before creating

scope: `time_off_requests:read`

### Example Usage

<!-- UsageSnippet language="python" operationID="post-v1-companies-company_uuid-time_off-requests-preview" method="post" path="/v1/companies/{company_uuid}/time_off/requests/preview" -->
```python
import gusto_embedded
from gusto_embedded import Gusto
import os


with Gusto(
    company_access_auth=os.getenv("GUSTO_COMPANY_ACCESS_AUTH", ""),
) as gusto:

    res = gusto.time_off_requests.post_v1_companies_company_uuid_time_off_requests_preview(company_uuid="<id>", employee_uuid="<id>", policy_uuid="<id>", start_date="<value>", end_date="<value>", days={
        "key": "<value>",
        "key1": "<value>",
        "key2": "<value>",
    }, x_gusto_api_version=gusto_embedded.PostV1CompaniesCompanyUUIDTimeOffRequestsPreviewHeaderXGustoAPIVersion.TWO_THOUSAND_AND_TWENTY_FIVE_MINUS_06_MINUS_15)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                    | Type                                                                                                                                                                                                                         | Required                                                                                                                                                                                                                     | Description                                                                                                                                                                                                                  |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `company_uuid`                                                                                                                                                                                                               | *str*                                                                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                                           | The UUID of the company                                                                                                                                                                                                      |
| `employee_uuid`                                                                                                                                                                                                              | *str*                                                                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                                           | The UUID of the employee                                                                                                                                                                                                     |
| `policy_uuid`                                                                                                                                                                                                                | *str*                                                                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                                           | The UUID of the time off policy                                                                                                                                                                                              |
| `start_date`                                                                                                                                                                                                                 | *str*                                                                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                                           | The start date of the time off request (YYYY-MM-DD)                                                                                                                                                                          |
| `end_date`                                                                                                                                                                                                                   | *str*                                                                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                                           | The end date of the time off request (YYYY-MM-DD)                                                                                                                                                                            |
| `days`                                                                                                                                                                                                                       | Dict[str, *str*]                                                                                                                                                                                                             | :heavy_check_mark:                                                                                                                                                                                                           | An object where keys are dates in YYYY-MM-DD format and values are hours as string decimals (e.g. {"2025-01-20": "8.000"})                                                                                                   |
| `x_gusto_api_version`                                                                                                                                                                                                        | [Optional[models.PostV1CompaniesCompanyUUIDTimeOffRequestsPreviewHeaderXGustoAPIVersion]](../../models/postv1companiescompanyuuidtimeoffrequestspreviewheaderxgustoapiversion.md)                                            | :heavy_minus_sign:                                                                                                                                                                                                           | Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used. |
| `request_uuid`                                                                                                                                                                                                               | *Optional[str]*                                                                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                           | The UUID of an existing time off request to preview changes for                                                                                                                                                              |
| `retries`                                                                                                                                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                           | Configuration to override the default retry behavior of the client.                                                                                                                                                          |

### Response

**[models.EmbeddedTimeOffRequestPreview](../../models/embeddedtimeoffrequestpreview.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.NotFoundErrorObject | 404                        | application/json           |
| models.APIError            | 4XX, 5XX                   | \*/\*                      |

## get_v1_time_off_requests_time_off_request_uuid

Get a single time off request by UUID

scope: `time_off_requests:read`

### Example Usage

<!-- UsageSnippet language="python" operationID="get-v1-time_off-requests-time_off_request_uuid" method="get" path="/v1/time_off/requests/{time_off_request_uuid}" -->
```python
import gusto_embedded
from gusto_embedded import Gusto
import os


with Gusto(
    company_access_auth=os.getenv("GUSTO_COMPANY_ACCESS_AUTH", ""),
) as gusto:

    res = gusto.time_off_requests.get_v1_time_off_requests_time_off_request_uuid(time_off_request_uuid="<id>", x_gusto_api_version=gusto_embedded.GetV1TimeOffRequestsTimeOffRequestUUIDHeaderXGustoAPIVersion.TWO_THOUSAND_AND_TWENTY_FIVE_MINUS_06_MINUS_15)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                    | Type                                                                                                                                                                                                                         | Required                                                                                                                                                                                                                     | Description                                                                                                                                                                                                                  |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `time_off_request_uuid`                                                                                                                                                                                                      | *str*                                                                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                                           | The UUID of the time off request                                                                                                                                                                                             |
| `x_gusto_api_version`                                                                                                                                                                                                        | [Optional[models.GetV1TimeOffRequestsTimeOffRequestUUIDHeaderXGustoAPIVersion]](../../models/getv1timeoffrequeststimeoffrequestuuidheaderxgustoapiversion.md)                                                                | :heavy_minus_sign:                                                                                                                                                                                                           | Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used. |
| `retries`                                                                                                                                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                           | Configuration to override the default retry behavior of the client.                                                                                                                                                          |

### Response

**[models.EmbeddedTimeOffRequest](../../models/embeddedtimeoffrequest.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.NotFoundErrorObject | 404                        | application/json           |
| models.APIError            | 4XX, 5XX                   | \*/\*                      |

## delete_v1_time_off_requests_time_off_request_uuid

Delete a time off request

scope: `time_off_requests:write`

### Example Usage

<!-- UsageSnippet language="python" operationID="delete-v1-time_off-requests-time_off_request_uuid" method="delete" path="/v1/time_off/requests/{time_off_request_uuid}" -->
```python
import gusto_embedded
from gusto_embedded import Gusto
import os


with Gusto(
    company_access_auth=os.getenv("GUSTO_COMPANY_ACCESS_AUTH", ""),
) as gusto:

    gusto.time_off_requests.delete_v1_time_off_requests_time_off_request_uuid(time_off_request_uuid="<id>", x_gusto_api_version=gusto_embedded.DeleteV1TimeOffRequestsTimeOffRequestUUIDHeaderXGustoAPIVersion.TWO_THOUSAND_AND_TWENTY_FIVE_MINUS_06_MINUS_15)

    # Use the SDK ...

```

### Parameters

| Parameter                                                                                                                                                                                                                    | Type                                                                                                                                                                                                                         | Required                                                                                                                                                                                                                     | Description                                                                                                                                                                                                                  |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `time_off_request_uuid`                                                                                                                                                                                                      | *str*                                                                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                                           | The UUID of the time off request                                                                                                                                                                                             |
| `x_gusto_api_version`                                                                                                                                                                                                        | [Optional[models.DeleteV1TimeOffRequestsTimeOffRequestUUIDHeaderXGustoAPIVersion]](../../models/deletev1timeoffrequeststimeoffrequestuuidheaderxgustoapiversion.md)                                                          | :heavy_minus_sign:                                                                                                                                                                                                           | Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used. |
| `retries`                                                                                                                                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                           | Configuration to override the default retry behavior of the client.                                                                                                                                                          |

### Errors

| Error Type                       | Status Code                      | Content Type                     |
| -------------------------------- | -------------------------------- | -------------------------------- |
| models.NotFoundErrorObject       | 404                              | application/json                 |
| models.UnprocessableEntityError1 | 422                              | application/json                 |
| models.APIError                  | 4XX, 5XX                         | \*/\*                            |

## put_v1_time_off_requests_time_off_request_uuid_approve

Approve a pending time off request. Optionally override the dates and hours.

Only requests with a `pending` status can be approved. Attempting to approve a request that has already been `declined` or `consumed` will fail with a 422 error.

scope: `time_off_requests:manage`

### Example Usage

<!-- UsageSnippet language="python" operationID="put-v1-time_off-requests-time_off_request_uuid-approve" method="put" path="/v1/time_off/requests/{time_off_request_uuid}/approve" -->
```python
import gusto_embedded
from gusto_embedded import Gusto
import os


with Gusto(
    company_access_auth=os.getenv("GUSTO_COMPANY_ACCESS_AUTH", ""),
) as gusto:

    res = gusto.time_off_requests.put_v1_time_off_requests_time_off_request_uuid_approve(time_off_request_uuid="<id>", x_gusto_api_version=gusto_embedded.PutV1TimeOffRequestsTimeOffRequestUUIDApproveHeaderXGustoAPIVersion.TWO_THOUSAND_AND_TWENTY_FIVE_MINUS_06_MINUS_15)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                    | Type                                                                                                                                                                                                                         | Required                                                                                                                                                                                                                     | Description                                                                                                                                                                                                                  |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `time_off_request_uuid`                                                                                                                                                                                                      | *str*                                                                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                                           | The UUID of the time off request                                                                                                                                                                                             |
| `x_gusto_api_version`                                                                                                                                                                                                        | [Optional[models.PutV1TimeOffRequestsTimeOffRequestUUIDApproveHeaderXGustoAPIVersion]](../../models/putv1timeoffrequeststimeoffrequestuuidapproveheaderxgustoapiversion.md)                                                  | :heavy_minus_sign:                                                                                                                                                                                                           | Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used. |
| `approver_uuid`                                                                                                                                                                                                              | *Optional[str]*                                                                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                           | The UUID of the admin approving the request. Defaults to the company's primary payroll admin.                                                                                                                                |
| `employer_note`                                                                                                                                                                                                              | *Optional[str]*                                                                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                           | A note from the employer about the approval                                                                                                                                                                                  |
| `days`                                                                                                                                                                                                                       | Dict[str, *str*]                                                                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                           | An object where keys are dates in YYYY-MM-DD format and values are hours as string decimals (e.g. {"2025-01-20": "8.000"}). Use this to override the requested hours.                                                        |
| `retries`                                                                                                                                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                           | Configuration to override the default retry behavior of the client.                                                                                                                                                          |

### Response

**[models.EmbeddedTimeOffRequest](../../models/embeddedtimeoffrequest.md)**

### Errors

| Error Type                       | Status Code                      | Content Type                     |
| -------------------------------- | -------------------------------- | -------------------------------- |
| models.NotFoundErrorObject       | 404                              | application/json                 |
| models.UnprocessableEntityError1 | 422                              | application/json                 |
| models.APIError                  | 4XX, 5XX                         | \*/\*                            |

## put_v1_time_off_requests_time_off_request_uuid_decline

Decline a pending or approved time off request. Requires an employer_note.

scope: `time_off_requests:manage`

### Example Usage

<!-- UsageSnippet language="python" operationID="put-v1-time_off-requests-time_off_request_uuid-decline" method="put" path="/v1/time_off/requests/{time_off_request_uuid}/decline" -->
```python
import gusto_embedded
from gusto_embedded import Gusto
import os


with Gusto(
    company_access_auth=os.getenv("GUSTO_COMPANY_ACCESS_AUTH", ""),
) as gusto:

    res = gusto.time_off_requests.put_v1_time_off_requests_time_off_request_uuid_decline(time_off_request_uuid="<id>", employer_note="<value>", x_gusto_api_version=gusto_embedded.PutV1TimeOffRequestsTimeOffRequestUUIDDeclineHeaderXGustoAPIVersion.TWO_THOUSAND_AND_TWENTY_FIVE_MINUS_06_MINUS_15)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                    | Type                                                                                                                                                                                                                         | Required                                                                                                                                                                                                                     | Description                                                                                                                                                                                                                  |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `time_off_request_uuid`                                                                                                                                                                                                      | *str*                                                                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                                           | The UUID of the time off request                                                                                                                                                                                             |
| `employer_note`                                                                                                                                                                                                              | *str*                                                                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                                           | Note explaining why the request was declined                                                                                                                                                                                 |
| `x_gusto_api_version`                                                                                                                                                                                                        | [Optional[models.PutV1TimeOffRequestsTimeOffRequestUUIDDeclineHeaderXGustoAPIVersion]](../../models/putv1timeoffrequeststimeoffrequestuuiddeclineheaderxgustoapiversion.md)                                                  | :heavy_minus_sign:                                                                                                                                                                                                           | Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used. |
| `approver_uuid`                                                                                                                                                                                                              | *Optional[str]*                                                                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                           | The UUID of the admin declining the request. Defaults to the company's primary payroll admin.                                                                                                                                |
| `retries`                                                                                                                                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                           | Configuration to override the default retry behavior of the client.                                                                                                                                                          |

### Response

**[models.EmbeddedTimeOffRequest](../../models/embeddedtimeoffrequest.md)**

### Errors

| Error Type                       | Status Code                      | Content Type                     |
| -------------------------------- | -------------------------------- | -------------------------------- |
| models.NotFoundErrorObject       | 404                              | application/json                 |
| models.UnprocessableEntityError1 | 422                              | application/json                 |
| models.APIError                  | 4XX, 5XX                         | \*/\*                            |