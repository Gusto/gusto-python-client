# WireInRequests

## Overview

### Available Operations

* [get](#get) - Get a single Wire In Request
* [submit](#submit) - Submit a wire in request
* [list](#list) - Get all Wire In Requests for a company

## get

Fetch a Wire In Request.

scope: `payrolls:read`

### Example Usage

<!-- UsageSnippet language="python" operationID="get-wire_in_requests-wire_in_request_uuid" method="get" path="/v1/wire_in_requests/{wire_in_request_uuid}" -->
```python
import gusto_embedded
from gusto_embedded import Gusto
import os


with Gusto(
    company_access_auth=os.getenv("GUSTO_COMPANY_ACCESS_AUTH", ""),
) as gusto:

    res = gusto.wire_in_requests.get(wire_in_request_uuid="<id>", x_gusto_api_version=gusto_embedded.GetWireInRequestsWireInRequestUUIDHeaderXGustoAPIVersion.TWO_THOUSAND_AND_TWENTY_FIVE_MINUS_06_MINUS_15)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                    | Type                                                                                                                                                                                                                         | Required                                                                                                                                                                                                                     | Description                                                                                                                                                                                                                  |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `wire_in_request_uuid`                                                                                                                                                                                                       | *str*                                                                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                                           | The UUID of the Wire In Request                                                                                                                                                                                              |
| `x_gusto_api_version`                                                                                                                                                                                                        | [Optional[models.GetWireInRequestsWireInRequestUUIDHeaderXGustoAPIVersion]](../../models/getwireinrequestswireinrequestuuidheaderxgustoapiversion.md)                                                                        | :heavy_minus_sign:                                                                                                                                                                                                           | Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used. |
| `retries`                                                                                                                                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                           | Configuration to override the default retry behavior of the client.                                                                                                                                                          |

### Response

**[models.WireInRequest](../../models/wireinrequest.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.NotFoundErrorObject | 404                        | application/json           |
| models.APIError            | 4XX, 5XX                   | \*/\*                      |

## submit

Submit a wire in request for a payment

scope: `payrolls:run`

### Example Usage

<!-- UsageSnippet language="python" operationID="put-wire_in_requests-wire_in_request_uuid" method="put" path="/v1/wire_in_requests/{wire_in_request_uuid}" -->
```python
import gusto_embedded
from gusto_embedded import Gusto
import os


with Gusto(
    company_access_auth=os.getenv("GUSTO_COMPANY_ACCESS_AUTH", ""),
) as gusto:

    res = gusto.wire_in_requests.submit(wire_in_request_uuid="<id>", date_sent="2024-06-10", bank_name="Chase", amount_sent="314500.00", x_gusto_api_version=gusto_embedded.PutWireInRequestsWireInRequestUUIDHeaderXGustoAPIVersion.TWO_THOUSAND_AND_TWENTY_FIVE_MINUS_06_MINUS_15, additional_notes="Wire for 2024-06-15 payroll.")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                    | Type                                                                                                                                                                                                                         | Required                                                                                                                                                                                                                     | Description                                                                                                                                                                                                                  | Example                                                                                                                                                                                                                      |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `wire_in_request_uuid`                                                                                                                                                                                                       | *str*                                                                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                                           | The UUID of the Wire In Request                                                                                                                                                                                              |                                                                                                                                                                                                                              |
| `date_sent`                                                                                                                                                                                                                  | *str*                                                                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                                           | The date the wire was sent                                                                                                                                                                                                   | 2024-06-10                                                                                                                                                                                                                   |
| `bank_name`                                                                                                                                                                                                                  | *str*                                                                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                                           | Name of the bank sending the wire                                                                                                                                                                                            | Chase                                                                                                                                                                                                                        |
| `amount_sent`                                                                                                                                                                                                                | *str*                                                                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                                           | Amount of money sent                                                                                                                                                                                                         | 314500.00                                                                                                                                                                                                                    |
| `x_gusto_api_version`                                                                                                                                                                                                        | [Optional[models.PutWireInRequestsWireInRequestUUIDHeaderXGustoAPIVersion]](../../models/putwireinrequestswireinrequestuuidheaderxgustoapiversion.md)                                                                        | :heavy_minus_sign:                                                                                                                                                                                                           | Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used. |                                                                                                                                                                                                                              |
| `additional_notes`                                                                                                                                                                                                           | *Optional[str]*                                                                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                           | Additional notes                                                                                                                                                                                                             | Wire for 2024-06-15 payroll.                                                                                                                                                                                                 |
| `retries`                                                                                                                                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                           | Configuration to override the default retry behavior of the client.                                                                                                                                                          |                                                                                                                                                                                                                              |

### Response

**[models.WireInRequest](../../models/wireinrequest.md)**

### Errors

| Error Type                       | Status Code                      | Content Type                     |
| -------------------------------- | -------------------------------- | -------------------------------- |
| models.NotFoundErrorObject       | 404                              | application/json                 |
| models.UnprocessableEntityError1 | 422                              | application/json                 |
| models.APIError                  | 4XX, 5XX                         | \*/\*                            |

## list

Fetches all Wire In Requests for a company.

scope: `payrolls:read`

### Example Usage

<!-- UsageSnippet language="python" operationID="get-companies-company_uuid-wire_in_request_uuid" method="get" path="/v1/companies/{company_uuid}/wire_in_requests" -->
```python
import gusto_embedded
from gusto_embedded import Gusto
import os


with Gusto(
    company_access_auth=os.getenv("GUSTO_COMPANY_ACCESS_AUTH", ""),
) as gusto:

    res = gusto.wire_in_requests.list(company_uuid="<id>", x_gusto_api_version=gusto_embedded.GetCompaniesCompanyUUIDWireInRequestUUIDHeaderXGustoAPIVersion.TWO_THOUSAND_AND_TWENTY_FIVE_MINUS_06_MINUS_15)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                    | Type                                                                                                                                                                                                                         | Required                                                                                                                                                                                                                     | Description                                                                                                                                                                                                                  |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `company_uuid`                                                                                                                                                                                                               | *str*                                                                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                                           | The UUID of the company                                                                                                                                                                                                      |
| `x_gusto_api_version`                                                                                                                                                                                                        | [Optional[models.GetCompaniesCompanyUUIDWireInRequestUUIDHeaderXGustoAPIVersion]](../../models/getcompaniescompanyuuidwireinrequestuuidheaderxgustoapiversion.md)                                                            | :heavy_minus_sign:                                                                                                                                                                                                           | Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used. |
| `page`                                                                                                                                                                                                                       | *Optional[int]*                                                                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                           | The page that is requested. When unspecified, will load all objects unless endpoint forces pagination.                                                                                                                       |
| `per`                                                                                                                                                                                                                        | *Optional[int]*                                                                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                           | Number of objects per page. For majority of endpoints will default to 25                                                                                                                                                     |
| `retries`                                                                                                                                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                           | Configuration to override the default retry behavior of the client.                                                                                                                                                          |

### Response

**[List[models.WireInRequest]](../../models/.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |