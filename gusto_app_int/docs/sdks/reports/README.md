# Reports
(*reports*)

## Overview

### Available Operations

* [post_payrolls_payroll_uuid_reports_general_ledger](#post_payrolls_payroll_uuid_reports_general_ledger) - Create a general ledger report
* [get_reports_request_uuid](#get_reports_request_uuid) - Get a report

## post_payrolls_payroll_uuid_reports_general_ledger

Create a general ledger report for a payroll. The report can be aggregated by different dimensions such as job or department.

Use the `request_uuid` in the response with the [report GET endpoint](../reference/get-reports-request_uuid) to poll for the status and report URL upon completion. The retrieved report will be generated in a JSON format.

scope: `company_reports:write` OR `company_reports:write:general_ledger`

### Example Usage

<!-- UsageSnippet language="python" operationID="post-payrolls-payroll_uuid-reports-general_ledger" method="post" path="/v1/payrolls/{payroll_uuid}/reports/general_ledger" -->
```python
import gusto_app_integration
from gusto_app_integration import GustoAppIntegration


with GustoAppIntegration(
    company_access_auth="<YOUR_BEARER_TOKEN_HERE>",
) as gai_client:

    res = gai_client.reports.post_payrolls_payroll_uuid_reports_general_ledger(payroll_uuid="<id>", aggregation=gusto_app_integration.PostPayrollsPayrollUUIDReportsGeneralLedgerAggregation.DEFAULT, x_gusto_api_version=gusto_app_integration.VersionHeader.TWO_THOUSAND_AND_TWENTY_FOUR_MINUS_04_MINUS_01)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                    | Type                                                                                                                                                                                                                         | Required                                                                                                                                                                                                                     | Description                                                                                                                                                                                                                  |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `payroll_uuid`                                                                                                                                                                                                               | *str*                                                                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                                           | The UUID of the payroll                                                                                                                                                                                                      |
| `aggregation`                                                                                                                                                                                                                | [models.PostPayrollsPayrollUUIDReportsGeneralLedgerAggregation](../../models/postpayrollspayrolluuidreportsgeneralledgeraggregation.md)                                                                                      | :heavy_check_mark:                                                                                                                                                                                                           | The breakdown of the report. Use 'default' for no split.                                                                                                                                                                     |
| `x_gusto_api_version`                                                                                                                                                                                                        | [Optional[models.VersionHeader]](../../models/versionheader.md)                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                           | Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used. |
| `integration_type`                                                                                                                                                                                                           | [OptionalNullable[models.PostPayrollsPayrollUUIDReportsGeneralLedgerIntegrationType]](../../models/postpayrollspayrolluuidreportsgeneralledgerintegrationtype.md)                                                            | :heavy_minus_sign:                                                                                                                                                                                                           | The kind of integration set up for the company. Required when `aggregation` is 'integration'. Must be null if `aggregation` is not 'integration'.                                                                            |
| `retries`                                                                                                                                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                           | Configuration to override the default retry behavior of the client.                                                                                                                                                          |

### Response

**[models.GeneralLedgerReport](../../models/generalledgerreport.md)**

### Errors

| Error Type                            | Status Code                           | Content Type                          |
| ------------------------------------- | ------------------------------------- | ------------------------------------- |
| models.UnprocessableEntityErrorObject | 422                                   | application/json                      |
| models.APIError                       | 4XX, 5XX                              | \*/\*                                 |

## get_reports_request_uuid

Get a company's report given the `request_uuid`. The response will include the report request's status and, if complete, the report URL.

Reports containing PHI are inaccessible with `company_reports:read:tier_2_only` data scope

scope: `company_reports:read`

### Example Usage

<!-- UsageSnippet language="python" operationID="get-reports-request_uuid" method="get" path="/v1/reports/{request_uuid}" -->
```python
import gusto_app_integration
from gusto_app_integration import GustoAppIntegration


with GustoAppIntegration(
    company_access_auth="<YOUR_BEARER_TOKEN_HERE>",
) as gai_client:

    res = gai_client.reports.get_reports_request_uuid(request_uuid="<id>", x_gusto_api_version=gusto_app_integration.VersionHeader.TWO_THOUSAND_AND_TWENTY_FOUR_MINUS_04_MINUS_01)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                    | Type                                                                                                                                                                                                                         | Required                                                                                                                                                                                                                     | Description                                                                                                                                                                                                                  |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `request_uuid`                                                                                                                                                                                                               | *str*                                                                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                                           | The UUID of the request to generate a document. Generate document endpoints return request_uuids to be used with the GET generated document endpoint.                                                                        |
| `x_gusto_api_version`                                                                                                                                                                                                        | [Optional[models.VersionHeader]](../../models/versionheader.md)                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                           | Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used. |
| `retries`                                                                                                                                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                           | Configuration to override the default retry behavior of the client.                                                                                                                                                          |

### Response

**[models.Report](../../models/report.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |