# InformationRequests

## Overview

### Available Operations

* [get_information_requests](#get_information_requests) - Get all information requests for a company
* [submit](#submit) - Submit information request responses

## get_information_requests

Fetch all information requests for a company.

scope: `information_requests:read`

### Example Usage

<!-- UsageSnippet language="python" operationID="get-information-requests" method="get" path="/v1/companies/{company_uuid}/information_requests" -->
```python
import gusto_embedded
from gusto_embedded import Gusto
import os


with Gusto(
    company_access_auth=os.getenv("GUSTO_COMPANY_ACCESS_AUTH", ""),
) as gusto:

    res = gusto.information_requests.get_information_requests(company_uuid="<id>", x_gusto_api_version=gusto_embedded.GetInformationRequestsHeaderXGustoAPIVersion.TWO_THOUSAND_AND_TWENTY_FIVE_MINUS_06_MINUS_15, sort_by="payroll_blocker:asc")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                    | Type                                                                                                                                                                                                                         | Required                                                                                                                                                                                                                     | Description                                                                                                                                                                                                                  | Example                                                                                                                                                                                                                      |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `company_uuid`                                                                                                                                                                                                               | *str*                                                                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                                           | The UUID of the company                                                                                                                                                                                                      |                                                                                                                                                                                                                              |
| `x_gusto_api_version`                                                                                                                                                                                                        | [Optional[models.GetInformationRequestsHeaderXGustoAPIVersion]](../../models/getinformationrequestsheaderxgustoapiversion.md)                                                                                                | :heavy_minus_sign:                                                                                                                                                                                                           | Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used. |                                                                                                                                                                                                                              |
| `sort_by`                                                                                                                                                                                                                    | *Optional[str]*                                                                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                           | Sort by one or more fields. Options: payroll_blocker, status, type. Append `:asc` or `:desc` to specify direction (e.g., `payroll_blocker:asc`). Defaults to ascending.                                                      | payroll_blocker:asc                                                                                                                                                                                                          |
| `retries`                                                                                                                                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                           | Configuration to override the default retry behavior of the client.                                                                                                                                                          |                                                                                                                                                                                                                              |

### Response

**[List[models.InformationRequest]](../../models/.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.NotFoundErrorObject | 404                        | application/json           |
| models.APIError            | 4XX, 5XX                   | \*/\*                      |

## submit

Submit responses to an information request.
Supports both text responses and file uploads (multipart/form-data).
Maximum file size: 120MB.

scope: `information_requests:write`

### Example Usage: Basic

<!-- UsageSnippet language="python" operationID="submit-information-request" method="put" path="/v1/information_requests/{information_request_uuid}/submit" example="Basic" -->
```python
from gusto_embedded import Gusto
import os


with Gusto(
    company_access_auth=os.getenv("GUSTO_COMPANY_ACCESS_AUTH", ""),
) as gusto:

    res = gusto.information_requests.submit(information_request_uuid="<id>")

    # Handle response
    print(res)

```
### Example Usage: Nested

<!-- UsageSnippet language="python" operationID="submit-information-request" method="put" path="/v1/information_requests/{information_request_uuid}/submit" example="Nested" -->
```python
from gusto_embedded import Gusto
import os


with Gusto(
    company_access_auth=os.getenv("GUSTO_COMPANY_ACCESS_AUTH", ""),
) as gusto:

    res = gusto.information_requests.submit(information_request_uuid="<id>")

    # Handle response
    print(res)

```
### Example Usage: Resource

<!-- UsageSnippet language="python" operationID="submit-information-request" method="put" path="/v1/information_requests/{information_request_uuid}/submit" example="Resource" -->
```python
from gusto_embedded import Gusto
import os


with Gusto(
    company_access_auth=os.getenv("GUSTO_COMPANY_ACCESS_AUTH", ""),
) as gusto:

    res = gusto.information_requests.submit(information_request_uuid="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                           | Type                                                                                                                | Required                                                                                                            | Description                                                                                                         |
| ------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------- |
| `information_request_uuid`                                                                                          | *str*                                                                                                               | :heavy_check_mark:                                                                                                  | The UUID of the information request                                                                                 |
| `required_questions`                                                                                                | List[[models.SubmitInformationRequestRequiredQuestions](../../models/submitinformationrequestrequiredquestions.md)] | :heavy_minus_sign:                                                                                                  | N/A                                                                                                                 |
| `retries`                                                                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                    | :heavy_minus_sign:                                                                                                  | Configuration to override the default retry behavior of the client.                                                 |

### Response

**[models.InformationRequest](../../models/informationrequest.md)**

### Errors

| Error Type                       | Status Code                      | Content Type                     |
| -------------------------------- | -------------------------------- | -------------------------------- |
| models.UnprocessableEntityError1 | 422                              | application/json                 |
| models.APIError                  | 4XX, 5XX                         | \*/\*                            |