# TimeOffRequests
(*time_off_requests*)

## Overview

### Available Operations

* [get_v1_companies_company_id_time_off_requests](#get_v1_companies_company_id_time_off_requests) - Get time off requests for a company

## get_v1_companies_company_id_time_off_requests

Get all time off requests, past and present, for a company.

In order to reduce the number of time off requests returned in a single response, or to retrieve time off requests from a time period of interest, you may use the `start_date` and `end_date` parameters.

You may provide both or either parameters to scope the returned data. For example:

`?start_date=2019-01-01`

Returns all time off requests where the request start date is equal to or after January 1, 2019.

`?end_date=2019-01-01`

Returns all time off requests where the request end date is equal to or before January 1, 2019.

`?start_date=2019-05-01&end_date=2019-08-31`

Returns all time off requests where the request start date is equal to or after May 1, 2019 and the request end date is equal to or before August 31, 2019.

`scope: time_off_requests:read`


### Example Usage

<!-- UsageSnippet language="python" operationID="get-v1-companies-company_id-time_off_requests" method="get" path="/v1/companies/{company_id}/time_off_requests" -->
```python
import gusto_app_integration
from gusto_app_integration import GustoAppIntegration


with GustoAppIntegration(
    company_access_auth="<YOUR_BEARER_TOKEN_HERE>",
) as gai_client:

    res = gai_client.time_off_requests.get_v1_companies_company_id_time_off_requests(company_id="<id>", x_gusto_api_version=gusto_app_integration.GetV1CompaniesCompanyIDTimeOffRequestsHeaderXGustoAPIVersion.TWO_THOUSAND_AND_TWENTY_FOUR_MINUS_04_MINUS_01)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                    | Type                                                                                                                                                                                                                         | Required                                                                                                                                                                                                                     | Description                                                                                                                                                                                                                  |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `company_id`                                                                                                                                                                                                                 | *str*                                                                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                                           | The company UUID                                                                                                                                                                                                             |
| `x_gusto_api_version`                                                                                                                                                                                                        | [Optional[models.GetV1CompaniesCompanyIDTimeOffRequestsHeaderXGustoAPIVersion]](../../models/getv1companiescompanyidtimeoffrequestsheaderxgustoapiversion.md)                                                                | :heavy_minus_sign:                                                                                                                                                                                                           | Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used. |
| `start_date`                                                                                                                                                                                                                 | *Optional[str]*                                                                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                           | Filter time off requests starting on or after this date                                                                                                                                                                      |
| `end_date`                                                                                                                                                                                                                   | *Optional[str]*                                                                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                           | Filter time off requests ending on or before this date                                                                                                                                                                       |
| `retries`                                                                                                                                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                           | Configuration to override the default retry behavior of the client.                                                                                                                                                          |

### Response

**[List[models.TimeOffRequest]](../../models/.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |