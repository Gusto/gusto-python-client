# TreasuryTippedOccupationCodes

## Overview

### Available Operations

* [get_companies_company_uuid_treasury_tipped_occupation_codes](#get_companies_company_uuid_treasury_tipped_occupation_codes) - Get Treasury Tipped Occupation Codes

## get_companies_company_uuid_treasury_tipped_occupation_codes

Returns the full list of 71 U.S. Treasury Tipped Occupation Codes (TTOCs),
optionally filtered by category. Reference data; the response is identical
across companies and cached for one day (Cache-Control: max-age=86400).

scope: `jobs:read`

### Example Usage

<!-- UsageSnippet language="python" operationID="get-companies-company_uuid-treasury_tipped_occupation_codes" method="get" path="/v1/companies/{company_uuid}/treasury_tipped_occupation_codes" -->
```python
import gusto_embedded_v_2026_06_15
from gusto_embedded_v_2026_06_15 import Gusto
import os


with Gusto(
    company_access_auth=os.getenv("GUSTO_COMPANY_ACCESS_AUTH"),
) as gusto:

    res = gusto.treasury_tipped_occupation_codes.get_companies_company_uuid_treasury_tipped_occupation_codes(company_uuid="<id>", x_gusto_api_version=gusto_embedded_v_2026_06_15.GetCompaniesCompanyUUIDTreasuryTippedOccupationCodesHeaderXGustoAPIVersion.TWO_THOUSAND_AND_TWENTY_SIX_MINUS_06_MINUS_15)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                               | Type                                                                                                                                                                                                                                    | Required                                                                                                                                                                                                                                | Description                                                                                                                                                                                                                             |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `company_uuid`                                                                                                                                                                                                                          | *str*                                                                                                                                                                                                                                   | :heavy_check_mark:                                                                                                                                                                                                                      | The UUID of the company                                                                                                                                                                                                                 |
| `x_gusto_api_version`                                                                                                                                                                                                                   | [Optional[models.GetCompaniesCompanyUUIDTreasuryTippedOccupationCodesHeaderXGustoAPIVersion]](../../models/getcompaniescompanyuuidtreasurytippedoccupationcodesheaderxgustoapiversion.md)                                               | :heavy_minus_sign:                                                                                                                                                                                                                      | Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used.            |
| `category`                                                                                                                                                                                                                              | *Optional[str]*                                                                                                                                                                                                                         | :heavy_minus_sign:                                                                                                                                                                                                                      | Optional category filter. One of: Beverage & Food Service, Entertainment & Events, Hospitality & Guest Services, Home Services, Personal Services, Personal Appearance & Wellness, Recreation & Instruction, Transportation & Delivery. |
| `retries`                                                                                                                                                                                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                        | :heavy_minus_sign:                                                                                                                                                                                                                      | Configuration to override the default retry behavior of the client.                                                                                                                                                                     |

### Response

**[List[models.TreasuryTippedOccupationCode]](../../models/.md)**

### Errors

| Error Type                       | Status Code                      | Content Type                     |
| -------------------------------- | -------------------------------- | -------------------------------- |
| models.UnprocessableEntityError1 | 422                              | application/json                 |
| models.APIError                  | 4XX, 5XX                         | \*/\*                            |