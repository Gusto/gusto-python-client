# IndustrySelection

## Overview

### Available Operations

* [get](#get) - Get a company industry selection
* [update](#update) - Update a company industry selection

## get

Returns the industry classification for a company, including NAICS code, SIC codes, and industry title.

scope: `companies:read`

### Example Usage

<!-- UsageSnippet language="python" operationID="get-v1-company-industry" method="get" path="/v1/companies/{company_id}/industry_selection" -->
```python
import gusto_embedded
from gusto_embedded import Gusto
import os


with Gusto(
    company_access_auth=os.getenv("GUSTO_COMPANY_ACCESS_AUTH", ""),
) as gusto:

    res = gusto.industry_selection.get(company_id="<id>", x_gusto_api_version=gusto_embedded.GetV1CompanyIndustryHeaderXGustoAPIVersion.TWO_THOUSAND_AND_TWENTY_FIVE_MINUS_06_MINUS_15)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                    | Type                                                                                                                                                                                                                         | Required                                                                                                                                                                                                                     | Description                                                                                                                                                                                                                  |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `company_id`                                                                                                                                                                                                                 | *str*                                                                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                                           | The UUID of the company                                                                                                                                                                                                      |
| `x_gusto_api_version`                                                                                                                                                                                                        | [Optional[models.GetV1CompanyIndustryHeaderXGustoAPIVersion]](../../models/getv1companyindustryheaderxgustoapiversion.md)                                                                                                    | :heavy_minus_sign:                                                                                                                                                                                                           | Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used. |
| `retries`                                                                                                                                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                           | Configuration to override the default retry behavior of the client.                                                                                                                                                          |

### Response

**[models.Industry](../../models/industry.md)**

### Errors

| Error Type                      | Status Code                     | Content Type                    |
| ------------------------------- | ------------------------------- | ------------------------------- |
| models.NotFoundErrorObjectError | 404                             | application/json                |
| models.APIError                 | 4XX, 5XX                        | \*/\*                           |

## update

Update the industry classification for a company by passing in a [NAICS code](https://www.naics.com).

Optionally provide an industry title and [SIC codes](https://siccode.com/). If you do not provide SIC codes,
we will use the NAICS code to perform an internal lookup.

Our UI leverages [Middesk API](https://docs.middesk.com/reference/introduction) to determine industry
classification codes.

scope: `companies:write`

### Example Usage

<!-- UsageSnippet language="python" operationID="put-v1-company-industry" method="put" path="/v1/companies/{company_id}/industry_selection" -->
```python
import gusto_embedded
from gusto_embedded import Gusto
import os


with Gusto(
    company_access_auth=os.getenv("GUSTO_COMPANY_ACCESS_AUTH", ""),
) as gusto:

    res = gusto.industry_selection.update(company_id="<id>", naics_code="611420", x_gusto_api_version=gusto_embedded.PutV1CompanyIndustryHeaderXGustoAPIVersion.TWO_THOUSAND_AND_TWENTY_FIVE_MINUS_06_MINUS_15, title="Computer Training", sic_codes=[
        "8243",
    ])

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                                                               | Type                                                                                                                                                                                                                                                                    | Required                                                                                                                                                                                                                                                                | Description                                                                                                                                                                                                                                                             | Example                                                                                                                                                                                                                                                                 |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `company_id`                                                                                                                                                                                                                                                            | *str*                                                                                                                                                                                                                                                                   | :heavy_check_mark:                                                                                                                                                                                                                                                      | The UUID of the company                                                                                                                                                                                                                                                 |                                                                                                                                                                                                                                                                         |
| `naics_code`                                                                                                                                                                                                                                                            | *str*                                                                                                                                                                                                                                                                   | :heavy_check_mark:                                                                                                                                                                                                                                                      | North American Industry Classification System (NAICS) is used to classify businesses with a six digit number based on the primary type of work the business performs.                                                                                                   | 611420                                                                                                                                                                                                                                                                  |
| `x_gusto_api_version`                                                                                                                                                                                                                                                   | [Optional[models.PutV1CompanyIndustryHeaderXGustoAPIVersion]](../../models/putv1companyindustryheaderxgustoapiversion.md)                                                                                                                                               | :heavy_minus_sign:                                                                                                                                                                                                                                                      | Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used.                                            |                                                                                                                                                                                                                                                                         |
| `title`                                                                                                                                                                                                                                                                 | *OptionalNullable[str]*                                                                                                                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                                                                                                                      | Industry title                                                                                                                                                                                                                                                          | Computer Training                                                                                                                                                                                                                                                       |
| `sic_codes`                                                                                                                                                                                                                                                             | List[*str*]                                                                                                                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                                                                      | A list of Standard Industrial Classification (SIC) codes, which are four digit numbers that categorize the industries that companies belong to based on their business activities. If sic_codes is not passed in, we will perform an internal lookup with `naics_code`. |                                                                                                                                                                                                                                                                         |
| `retries`                                                                                                                                                                                                                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                                        | :heavy_minus_sign:                                                                                                                                                                                                                                                      | Configuration to override the default retry behavior of the client.                                                                                                                                                                                                     |                                                                                                                                                                                                                                                                         |

### Response

**[models.Industry](../../models/industry.md)**

### Errors

| Error Type                       | Status Code                      | Content Type                     |
| -------------------------------- | -------------------------------- | -------------------------------- |
| models.NotFoundErrorObjectError  | 404                              | application/json                 |
| models.UnprocessableEntityError1 | 422                              | application/json                 |
| models.APIError                  | 4XX, 5XX                         | \*/\*                            |