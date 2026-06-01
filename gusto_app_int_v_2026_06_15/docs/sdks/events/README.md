# Events

## Overview

### Available Operations

* [get_all](#get_all) - Get all events

## get_all

Fetch all events, going back up to 30 days, that your partner application has the required scopes for. Note that a partner does NOT have to have verified webhook subscriptions in order to utilize this endpoint.

📘 System Access Authentication

This endpoint uses the [Bearer Auth scheme with the system-level access token in the HTTP Authorization header](https://docs.gusto.com/embedded-payroll/docs/system-access)

scope: `events:read`

### Example Usage

<!-- UsageSnippet language="python" operationID="get-events" method="get" path="/v1/events" -->
```python
import gusto_app_integration_v_2026_06_15
from gusto_app_integration_v_2026_06_15 import GustoAppIntegration


with GustoAppIntegration() as gusto_app_integration:

    res = gusto_app_integration.events.get_all(security=gusto_app_integration_v_2026_06_15.GetEventsSecurity(
        system_access_auth="<YOUR_BEARER_TOKEN_HERE>",
    ), x_gusto_api_version=gusto_app_integration_v_2026_06_15.GetEventsHeaderXGustoAPIVersion.TWO_THOUSAND_AND_TWENTY_SIX_MINUS_06_MINUS_15)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                    | Type                                                                                                                                                                                                                         | Required                                                                                                                                                                                                                     | Description                                                                                                                                                                                                                  |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `security`                                                                                                                                                                                                                   | [models.GetEventsSecurity](../../models/geteventssecurity.md)                                                                                                                                                                | :heavy_check_mark:                                                                                                                                                                                                           | N/A                                                                                                                                                                                                                          |
| `x_gusto_api_version`                                                                                                                                                                                                        | [Optional[models.GetEventsHeaderXGustoAPIVersion]](../../models/geteventsheaderxgustoapiversion.md)                                                                                                                          | :heavy_minus_sign:                                                                                                                                                                                                           | Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used. |
| `starting_after_uuid`                                                                                                                                                                                                        | *Optional[str]*                                                                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                           | A cursor for pagination. Returns all events occuring after the specified UUID (exclusive). Events are sorted according to the provided sort_order param.                                                                     |
| `resource_uuid`                                                                                                                                                                                                              | *Optional[str]*                                                                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                           | The UUID of the company. If not specified, will return all events for all companies.                                                                                                                                         |
| `limit`                                                                                                                                                                                                                      | *Optional[str]*                                                                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                           | Limits the number of objects returned in a single response, between 1 and 100. The default is 25                                                                                                                             |
| `event_type`                                                                                                                                                                                                                 | *Optional[str]*                                                                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                           | A string containing the exact event name (e.g. `employee.created`), or use a wildcard match to filter for a group of events (e.g. `employee.*`, `*.created`, `notification.*.created` etc.)                                  |
| `sort_order`                                                                                                                                                                                                                 | [Optional[models.SortOrder]](../../models/sortorder.md)                                                                                                                                                                      | :heavy_minus_sign:                                                                                                                                                                                                           | A string indicating whether to sort resulting events in ascending (asc) or descending (desc) chronological order. Events are sorted by their `timestamp`. Defaults to asc if left empty.                                     |
| `retries`                                                                                                                                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                           | Configuration to override the default retry behavior of the client.                                                                                                                                                          |

### Response

**[List[models.Event]](../../models/.md)**

### Errors

| Error Type                            | Status Code                           | Content Type                          |
| ------------------------------------- | ------------------------------------- | ------------------------------------- |
| models.UnprocessableEntityErrorObject | 422                                   | application/json                      |
| models.APIError                       | 4XX, 5XX                              | \*/\*                                 |