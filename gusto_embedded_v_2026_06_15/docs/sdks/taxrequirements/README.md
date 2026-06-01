# TaxRequirements

## Overview

### Available Operations

* [get_all](#get_all) - Get all tax requirements for a company
* [get](#get) - Get tax requirements for a state
* [update_state](#update_state) - Update tax requirements for a state

## get_all

Retrieves all states for which a company has tax requirements, along with a boolean indicating whether tax setup
is complete for each state. Use this to determine which states still need tax setup during company onboarding.

scope: `company_tax_requirements:read`

### Example Usage

<!-- UsageSnippet language="python" operationID="get-v1-companies-company_uuid-tax_requirements" method="get" path="/v1/companies/{company_uuid}/tax_requirements" -->
```python
import gusto_embedded_v_2026_06_15
from gusto_embedded_v_2026_06_15 import Gusto
import os


with Gusto(
    company_access_auth=os.getenv("GUSTO_COMPANY_ACCESS_AUTH", ""),
) as gusto:

    res = gusto.tax_requirements.get_all(company_uuid="<id>", x_gusto_api_version=gusto_embedded_v_2026_06_15.GetV1CompaniesCompanyUUIDTaxRequirementsHeaderXGustoAPIVersion.TWO_THOUSAND_AND_TWENTY_SIX_MINUS_06_MINUS_15)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                    | Type                                                                                                                                                                                                                         | Required                                                                                                                                                                                                                     | Description                                                                                                                                                                                                                  |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `company_uuid`                                                                                                                                                                                                               | *str*                                                                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                                           | The UUID of the company                                                                                                                                                                                                      |
| `x_gusto_api_version`                                                                                                                                                                                                        | [Optional[models.GetV1CompaniesCompanyUUIDTaxRequirementsHeaderXGustoAPIVersion]](../../models/getv1companiescompanyuuidtaxrequirementsheaderxgustoapiversion.md)                                                            | :heavy_minus_sign:                                                                                                                                                                                                           | Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used. |
| `retries`                                                                                                                                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                           | Configuration to override the default retry behavior of the client.                                                                                                                                                          |

### Response

**[List[models.TaxRequirementStatesList]](../../models/.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.NotFoundErrorObject | 404                        | application/json           |
| models.APIError            | 4XX, 5XX                   | \*/\*                      |

## get

Retrieves the detailed tax requirements for a specific state. The response includes requirement sets grouped by
category (e.g., registrations, tax rates, deposit schedules), each containing individual requirements with their
current values, labels, and metadata describing the expected input format.

Use this to build dynamic UIs for tax setup or to read the current tax configuration for a state.

scope: `company_tax_requirements:read`

### Example Usage

<!-- UsageSnippet language="python" operationID="get-v1-companies-company_uuid-tax_requirements-state" method="get" path="/v1/companies/{company_uuid}/tax_requirements/{state}" -->
```python
import gusto_embedded_v_2026_06_15
from gusto_embedded_v_2026_06_15 import Gusto
import os


with Gusto(
    company_access_auth=os.getenv("GUSTO_COMPANY_ACCESS_AUTH", ""),
) as gusto:

    res = gusto.tax_requirements.get(company_uuid="<id>", state="CA", x_gusto_api_version=gusto_embedded_v_2026_06_15.GetV1CompaniesCompanyUUIDTaxRequirementsStateHeaderXGustoAPIVersion.TWO_THOUSAND_AND_TWENTY_SIX_MINUS_06_MINUS_15)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                    | Type                                                                                                                                                                                                                         | Required                                                                                                                                                                                                                     | Description                                                                                                                                                                                                                  | Example                                                                                                                                                                                                                      |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `company_uuid`                                                                                                                                                                                                               | *str*                                                                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                                           | The UUID of the company                                                                                                                                                                                                      |                                                                                                                                                                                                                              |
| `state`                                                                                                                                                                                                                      | *str*                                                                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                                           | The two-letter state abbreviation                                                                                                                                                                                            | CA                                                                                                                                                                                                                           |
| `x_gusto_api_version`                                                                                                                                                                                                        | [Optional[models.GetV1CompaniesCompanyUUIDTaxRequirementsStateHeaderXGustoAPIVersion]](../../models/getv1companiescompanyuuidtaxrequirementsstateheaderxgustoapiversion.md)                                                  | :heavy_minus_sign:                                                                                                                                                                                                           | Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used. |                                                                                                                                                                                                                              |
| `scheduling`                                                                                                                                                                                                                 | *Optional[bool]*                                                                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                           | When true, return "new" requirement sets with valid `effective_from` dates that are available to save new effective-dated values.                                                                                            |                                                                                                                                                                                                                              |
| `retries`                                                                                                                                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                           | Configuration to override the default retry behavior of the client.                                                                                                                                                          |                                                                                                                                                                                                                              |

### Response

**[models.TaxRequirementsState](../../models/taxrequirementsstate.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.NotFoundErrorObject | 404                        | application/json           |
| models.APIError            | 4XX, 5XX                   | \*/\*                      |

## update_state

Updates the tax requirement answers for a specific state. Submit answers to the requirement questions returned
by [GET /v1/companies/{company_uuid}/tax_requirements/{state}](ref:get-v1-companies-company_uuid-tax_requirements-state).

### Prerequisites

1. Retrieve current requirements via [GET /v1/companies/{company_uuid}/tax_requirements/{state}](ref:get-v1-companies-company_uuid-tax_requirements-state)
2. Ensure that each requirement set that you're updating includes the correct `key`, `state`, and `effective_from` values from the GET response

scope: `company_tax_requirements:write`

### Example Usage

<!-- UsageSnippet language="python" operationID="put-v1-companies-company_uuid-tax_requirements-state" method="put" path="/v1/companies/{company_uuid}/tax_requirements/{state}" -->
```python
import gusto_embedded_v_2026_06_15
from gusto_embedded_v_2026_06_15 import Gusto
import os


with Gusto(
    company_access_auth=os.getenv("GUSTO_COMPANY_ACCESS_AUTH", ""),
) as gusto:

    gusto.tax_requirements.update_state(company_uuid="<id>", state="CA", x_gusto_api_version=gusto_embedded_v_2026_06_15.PutV1CompaniesCompanyUUIDTaxRequirementsStateHeaderXGustoAPIVersion.TWO_THOUSAND_AND_TWENTY_SIX_MINUS_06_MINUS_15, requirement_sets=[
        {
            "key": "registrations",
            "state": "GA",
            "effective_from": "2022-01-01",
            "requirements": [
                {
                    "key": "71653ec0-00b5-4c66-a58b-22ecf21704c5",
                    "value": "1233214-AB",
                },
            ],
        },
    ])

    # Use the SDK ...

```

### Parameters

| Parameter                                                                                                                                                                                                                    | Type                                                                                                                                                                                                                         | Required                                                                                                                                                                                                                     | Description                                                                                                                                                                                                                  | Example                                                                                                                                                                                                                      |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `company_uuid`                                                                                                                                                                                                               | *str*                                                                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                                           | The UUID of the company                                                                                                                                                                                                      |                                                                                                                                                                                                                              |
| `state`                                                                                                                                                                                                                      | *str*                                                                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                                           | The two-letter state abbreviation                                                                                                                                                                                            | CA                                                                                                                                                                                                                           |
| `x_gusto_api_version`                                                                                                                                                                                                        | [Optional[models.PutV1CompaniesCompanyUUIDTaxRequirementsStateHeaderXGustoAPIVersion]](../../models/putv1companiescompanyuuidtaxrequirementsstateheaderxgustoapiversion.md)                                                  | :heavy_minus_sign:                                                                                                                                                                                                           | Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used. |                                                                                                                                                                                                                              |
| `requirement_sets`                                                                                                                                                                                                           | List[[models.TaxRequirementSetUpdate](../../models/taxrequirementsetupdate.md)]                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                           | Array of requirement sets to update. Each set corresponds to a category of requirements for the state.                                                                                                                       |                                                                                                                                                                                                                              |
| `retries`                                                                                                                                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                           | Configuration to override the default retry behavior of the client.                                                                                                                                                          |                                                                                                                                                                                                                              |

### Errors

| Error Type                       | Status Code                      | Content Type                     |
| -------------------------------- | -------------------------------- | -------------------------------- |
| models.NotFoundErrorObject       | 404                              | application/json                 |
| models.UnprocessableEntityError1 | 422                              | application/json                 |
| models.APIError                  | 4XX, 5XX                         | \*/\*                            |