# ExternalPayrolls

## Overview

### Available Operations

* [get](#get) - Get external payrolls for a company
* [create](#create) - Create an external payroll for a company
* [retrieve](#retrieve) - Get an external payroll
* [update](#update) - Update an external payroll
* [delete](#delete) - Delete an external payroll
* [calculate_taxes](#calculate_taxes) - Get tax suggestions for an external payroll
* [list_tax_liabilities](#list_tax_liabilities) - Get tax liabilities
* [update_tax_liabilities](#update_tax_liabilities) - Update tax liabilities
* [finalize_tax_liabilities](#finalize_tax_liabilities) - Finalize tax liabilities options and convert into processed payrolls

## get

Get external payrolls for a company.

scope: `external_payrolls:read`

### Example Usage

<!-- UsageSnippet language="python" operationID="get-v1-company-external-payrolls" method="get" path="/v1/companies/{company_uuid}/external_payrolls" -->
```python
import gusto_embedded
from gusto_embedded import Gusto
import os


with Gusto(
    company_access_auth=os.getenv("GUSTO_COMPANY_ACCESS_AUTH", ""),
) as gusto:

    res = gusto.external_payrolls.get(company_uuid="<id>", x_gusto_api_version=gusto_embedded.GetV1CompanyExternalPayrollsHeaderXGustoAPIVersion.TWO_THOUSAND_AND_TWENTY_FIVE_MINUS_06_MINUS_15)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                    | Type                                                                                                                                                                                                                         | Required                                                                                                                                                                                                                     | Description                                                                                                                                                                                                                  |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `company_uuid`                                                                                                                                                                                                               | *str*                                                                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                                           | The UUID of the company                                                                                                                                                                                                      |
| `x_gusto_api_version`                                                                                                                                                                                                        | [Optional[models.GetV1CompanyExternalPayrollsHeaderXGustoAPIVersion]](../../models/getv1companyexternalpayrollsheaderxgustoapiversion.md)                                                                                    | :heavy_minus_sign:                                                                                                                                                                                                           | Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used. |
| `page`                                                                                                                                                                                                                       | *Optional[int]*                                                                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                           | The page that is requested. When unspecified, will load all objects unless endpoint forces pagination.                                                                                                                       |
| `per`                                                                                                                                                                                                                        | *Optional[int]*                                                                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                           | Number of objects per page. For majority of endpoints will default to 25                                                                                                                                                     |
| `retries`                                                                                                                                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                           | Configuration to override the default retry behavior of the client.                                                                                                                                                          |

### Response

**[List[models.ExternalPayrollBasic]](../../models/.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.NotFoundErrorObject | 404                        | application/json           |
| models.APIError            | 4XX, 5XX                   | \*/\*                      |

## create

Creates a new external payroll for a company.

scope: `external_payrolls:write`

### Example Usage

<!-- UsageSnippet language="python" operationID="post-v1-external-payroll" method="post" path="/v1/companies/{company_uuid}/external_payrolls" -->
```python
from datetime import date
import gusto_embedded
from gusto_embedded import Gusto
import os


with Gusto(
    company_access_auth=os.getenv("GUSTO_COMPANY_ACCESS_AUTH", ""),
) as gusto:

    res = gusto.external_payrolls.create(company_uuid="<id>", check_date=date.fromisoformat("2022-06-03"), payment_period_start_date=date.fromisoformat("2022-05-15"), payment_period_end_date=date.fromisoformat("2022-05-30"), x_gusto_api_version=gusto_embedded.PostV1ExternalPayrollHeaderXGustoAPIVersion.TWO_THOUSAND_AND_TWENTY_FIVE_MINUS_06_MINUS_15)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                    | Type                                                                                                                                                                                                                         | Required                                                                                                                                                                                                                     | Description                                                                                                                                                                                                                  | Example                                                                                                                                                                                                                      |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `company_uuid`                                                                                                                                                                                                               | *str*                                                                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                                           | The UUID of the company                                                                                                                                                                                                      |                                                                                                                                                                                                                              |
| `check_date`                                                                                                                                                                                                                 | [datetime](https://docs.python.org/3/library/datetime.html#datetime-objects)                                                                                                                                                 | :heavy_check_mark:                                                                                                                                                                                                           | The check date of the external payroll.                                                                                                                                                                                      | 2022-06-03                                                                                                                                                                                                                   |
| `payment_period_start_date`                                                                                                                                                                                                  | [datetime](https://docs.python.org/3/library/datetime.html#datetime-objects)                                                                                                                                                 | :heavy_check_mark:                                                                                                                                                                                                           | The start date of the external payroll payment period.                                                                                                                                                                       | 2022-05-15                                                                                                                                                                                                                   |
| `payment_period_end_date`                                                                                                                                                                                                    | [datetime](https://docs.python.org/3/library/datetime.html#datetime-objects)                                                                                                                                                 | :heavy_check_mark:                                                                                                                                                                                                           | The end date of the external payroll payment period.                                                                                                                                                                         | 2022-05-30                                                                                                                                                                                                                   |
| `x_gusto_api_version`                                                                                                                                                                                                        | [Optional[models.PostV1ExternalPayrollHeaderXGustoAPIVersion]](../../models/postv1externalpayrollheaderxgustoapiversion.md)                                                                                                  | :heavy_minus_sign:                                                                                                                                                                                                           | Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used. |                                                                                                                                                                                                                              |
| `retries`                                                                                                                                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                           | Configuration to override the default retry behavior of the client.                                                                                                                                                          |                                                                                                                                                                                                                              |

### Response

**[models.ExternalPayroll](../../models/externalpayroll.md)**

### Errors

| Error Type                       | Status Code                      | Content Type                     |
| -------------------------------- | -------------------------------- | -------------------------------- |
| models.NotFoundErrorObject       | 404                              | application/json                 |
| models.UnprocessableEntityError1 | 422                              | application/json                 |
| models.APIError                  | 4XX, 5XX                         | \*/\*                            |

## retrieve

Get an external payroll for a given company.

scope: `external_payrolls:read`

### Example Usage

<!-- UsageSnippet language="python" operationID="get-v1-external-payroll" method="get" path="/v1/companies/{company_uuid}/external_payrolls/{external_payroll_id}" -->
```python
import gusto_embedded
from gusto_embedded import Gusto
import os


with Gusto(
    company_access_auth=os.getenv("GUSTO_COMPANY_ACCESS_AUTH", ""),
) as gusto:

    res = gusto.external_payrolls.retrieve(company_uuid="<id>", external_payroll_id="<id>", x_gusto_api_version=gusto_embedded.GetV1ExternalPayrollHeaderXGustoAPIVersion.TWO_THOUSAND_AND_TWENTY_FIVE_MINUS_06_MINUS_15)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                    | Type                                                                                                                                                                                                                         | Required                                                                                                                                                                                                                     | Description                                                                                                                                                                                                                  |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `company_uuid`                                                                                                                                                                                                               | *str*                                                                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                                           | The UUID of the company                                                                                                                                                                                                      |
| `external_payroll_id`                                                                                                                                                                                                        | *str*                                                                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                                           | The UUID of the external payroll                                                                                                                                                                                             |
| `x_gusto_api_version`                                                                                                                                                                                                        | [Optional[models.GetV1ExternalPayrollHeaderXGustoAPIVersion]](../../models/getv1externalpayrollheaderxgustoapiversion.md)                                                                                                    | :heavy_minus_sign:                                                                                                                                                                                                           | Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used. |
| `retries`                                                                                                                                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                           | Configuration to override the default retry behavior of the client.                                                                                                                                                          |

### Response

**[models.ExternalPayroll](../../models/externalpayroll.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.NotFoundErrorObject | 404                        | application/json           |
| models.APIError            | 4XX, 5XX                   | \*/\*                      |

## update

Update an external payroll with a list of external payroll items.

scope: `external_payrolls:write`

### Example Usage

<!-- UsageSnippet language="python" operationID="put-v1-external-payroll" method="put" path="/v1/companies/{company_uuid}/external_payrolls/{external_payroll_id}" -->
```python
import gusto_embedded
from gusto_embedded import Gusto
import os


with Gusto(
    company_access_auth=os.getenv("GUSTO_COMPANY_ACCESS_AUTH", ""),
) as gusto:

    res = gusto.external_payrolls.update(company_uuid="<id>", external_payroll_id="<id>", external_payroll_items=[
        {
            "employee_uuid": "44f7cba9-7a3d-4f08-b7bd-6fcf5211f8ca",
            "earnings": [
                {
                    "earning_type": gusto_embedded.ExternalPayrollUpdateRequestEarningType.COMPANY_PAY_TYPE,
                    "earning_id": 1,
                    "amount": "10000.00",
                    "hours": "80.0",
                },
            ],
            "benefits": [
                {
                    "benefit_id": 22,
                    "company_contribution_amount": "100.00",
                    "employee_deduction_amount": "50.00",
                },
            ],
            "taxes": [
                {
                    "tax_id": 1,
                    "amount": "400.00",
                },
            ],
        },
    ], x_gusto_api_version=gusto_embedded.PutV1ExternalPayrollHeaderXGustoAPIVersion.TWO_THOUSAND_AND_TWENTY_FIVE_MINUS_06_MINUS_15)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                    | Type                                                                                                                                                                                                                         | Required                                                                                                                                                                                                                     | Description                                                                                                                                                                                                                  |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `company_uuid`                                                                                                                                                                                                               | *str*                                                                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                                           | The UUID of the company                                                                                                                                                                                                      |
| `external_payroll_id`                                                                                                                                                                                                        | *str*                                                                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                                           | The UUID of the external payroll                                                                                                                                                                                             |
| `external_payroll_items`                                                                                                                                                                                                     | List[[models.ExternalPayrollUpdateRequestExternalPayrollItems](../../models/externalpayrollupdaterequestexternalpayrollitems.md)]                                                                                            | :heavy_check_mark:                                                                                                                                                                                                           | Payroll items for each employee in the external payroll.                                                                                                                                                                     |
| `x_gusto_api_version`                                                                                                                                                                                                        | [Optional[models.PutV1ExternalPayrollHeaderXGustoAPIVersion]](../../models/putv1externalpayrollheaderxgustoapiversion.md)                                                                                                    | :heavy_minus_sign:                                                                                                                                                                                                           | Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used. |
| `replace_fields`                                                                                                                                                                                                             | *Optional[bool]*                                                                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                           | Patch update external payroll items when set to true, otherwise it will overwrite the previous changes.                                                                                                                      |
| `retries`                                                                                                                                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                           | Configuration to override the default retry behavior of the client.                                                                                                                                                          |

### Response

**[models.ExternalPayroll](../../models/externalpayroll.md)**

### Errors

| Error Type                       | Status Code                      | Content Type                     |
| -------------------------------- | -------------------------------- | -------------------------------- |
| models.NotFoundErrorObject       | 404                              | application/json                 |
| models.UnprocessableEntityError1 | 422                              | application/json                 |
| models.APIError                  | 4XX, 5XX                         | \*/\*                            |

## delete

Delete an external payroll.

scope: `external_payrolls:write`

### Example Usage

<!-- UsageSnippet language="python" operationID="delete-v1-external-payroll" method="delete" path="/v1/companies/{company_uuid}/external_payrolls/{external_payroll_id}" -->
```python
import gusto_embedded
from gusto_embedded import Gusto
import os


with Gusto(
    company_access_auth=os.getenv("GUSTO_COMPANY_ACCESS_AUTH", ""),
) as gusto:

    gusto.external_payrolls.delete(company_uuid="<id>", external_payroll_id="<id>", x_gusto_api_version=gusto_embedded.DeleteV1ExternalPayrollHeaderXGustoAPIVersion.TWO_THOUSAND_AND_TWENTY_FIVE_MINUS_06_MINUS_15)

    # Use the SDK ...

```

### Parameters

| Parameter                                                                                                                                                                                                                    | Type                                                                                                                                                                                                                         | Required                                                                                                                                                                                                                     | Description                                                                                                                                                                                                                  |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `company_uuid`                                                                                                                                                                                                               | *str*                                                                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                                           | The UUID of the company                                                                                                                                                                                                      |
| `external_payroll_id`                                                                                                                                                                                                        | *str*                                                                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                                           | The UUID of the external payroll                                                                                                                                                                                             |
| `x_gusto_api_version`                                                                                                                                                                                                        | [Optional[models.DeleteV1ExternalPayrollHeaderXGustoAPIVersion]](../../models/deletev1externalpayrollheaderxgustoapiversion.md)                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                           | Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used. |
| `retries`                                                                                                                                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                           | Configuration to override the default retry behavior of the client.                                                                                                                                                          |

### Errors

| Error Type                       | Status Code                      | Content Type                     |
| -------------------------------- | -------------------------------- | -------------------------------- |
| models.NotFoundErrorObject       | 404                              | application/json                 |
| models.UnprocessableEntityError1 | 422                              | application/json                 |
| models.APIError                  | 4XX, 5XX                         | \*/\*                            |

## calculate_taxes

Get tax suggestions for an external payroll. Earnings and/or benefits data must be saved prior to the calculation in order to retrieve accurate tax calculation.

scope: `external_payrolls:read`

### Example Usage

<!-- UsageSnippet language="python" operationID="get-v1-external-payroll-calculate-taxes" method="get" path="/v1/companies/{company_uuid}/external_payrolls/{external_payroll_id}/calculate_taxes" -->
```python
import gusto_embedded
from gusto_embedded import Gusto
import os


with Gusto(
    company_access_auth=os.getenv("GUSTO_COMPANY_ACCESS_AUTH", ""),
) as gusto:

    res = gusto.external_payrolls.calculate_taxes(company_uuid="<id>", external_payroll_id="<id>", x_gusto_api_version=gusto_embedded.GetV1ExternalPayrollCalculateTaxesHeaderXGustoAPIVersion.TWO_THOUSAND_AND_TWENTY_FIVE_MINUS_06_MINUS_15)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                    | Type                                                                                                                                                                                                                         | Required                                                                                                                                                                                                                     | Description                                                                                                                                                                                                                  |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `company_uuid`                                                                                                                                                                                                               | *str*                                                                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                                           | The UUID of the company                                                                                                                                                                                                      |
| `external_payroll_id`                                                                                                                                                                                                        | *str*                                                                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                                           | The UUID of the external payroll                                                                                                                                                                                             |
| `x_gusto_api_version`                                                                                                                                                                                                        | [Optional[models.GetV1ExternalPayrollCalculateTaxesHeaderXGustoAPIVersion]](../../models/getv1externalpayrollcalculatetaxesheaderxgustoapiversion.md)                                                                        | :heavy_minus_sign:                                                                                                                                                                                                           | Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used. |
| `retries`                                                                                                                                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                           | Configuration to override the default retry behavior of the client.                                                                                                                                                          |

### Response

**[List[models.ExternalPayrollTaxSuggestions]](../../models/.md)**

### Errors

| Error Type                       | Status Code                      | Content Type                     |
| -------------------------------- | -------------------------------- | -------------------------------- |
| models.NotFoundErrorObject       | 404                              | application/json                 |
| models.UnprocessableEntityError1 | 422                              | application/json                 |
| models.APIError                  | 4XX, 5XX                         | \*/\*                            |

## list_tax_liabilities

Get tax liabilities from aggregate external payrolls for a company.

scope: `external_payrolls:read`

### Example Usage

<!-- UsageSnippet language="python" operationID="get-v1-tax-liabilities" method="get" path="/v1/companies/{company_uuid}/external_payrolls/tax_liabilities" -->
```python
import gusto_embedded
from gusto_embedded import Gusto
import os


with Gusto(
    company_access_auth=os.getenv("GUSTO_COMPANY_ACCESS_AUTH", ""),
) as gusto:

    res = gusto.external_payrolls.list_tax_liabilities(company_uuid="<id>", x_gusto_api_version=gusto_embedded.GetV1TaxLiabilitiesHeaderXGustoAPIVersion.TWO_THOUSAND_AND_TWENTY_FIVE_MINUS_06_MINUS_15)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                    | Type                                                                                                                                                                                                                         | Required                                                                                                                                                                                                                     | Description                                                                                                                                                                                                                  |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `company_uuid`                                                                                                                                                                                                               | *str*                                                                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                                           | The UUID of the company                                                                                                                                                                                                      |
| `x_gusto_api_version`                                                                                                                                                                                                        | [Optional[models.GetV1TaxLiabilitiesHeaderXGustoAPIVersion]](../../models/getv1taxliabilitiesheaderxgustoapiversion.md)                                                                                                      | :heavy_minus_sign:                                                                                                                                                                                                           | Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used. |
| `retries`                                                                                                                                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                           | Configuration to override the default retry behavior of the client.                                                                                                                                                          |

### Response

**[List[models.TaxLiabilitiesSelections]](../../models/.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.NotFoundErrorObject | 404                        | application/json           |
| models.APIError            | 4XX, 5XX                   | \*/\*                      |

## update_tax_liabilities

Update tax liabilities for a company.

scope: `external_payrolls:write`

### Example Usage

<!-- UsageSnippet language="python" operationID="put-v1-tax-liabilities" method="put" path="/v1/companies/{company_uuid}/external_payrolls/tax_liabilities" -->
```python
import gusto_embedded
from gusto_embedded import Gusto
import os


with Gusto(
    company_access_auth=os.getenv("GUSTO_COMPANY_ACCESS_AUTH", ""),
) as gusto:

    res = gusto.external_payrolls.update_tax_liabilities(company_uuid="<id>", liability_selections=[], x_gusto_api_version=gusto_embedded.PutV1TaxLiabilitiesHeaderXGustoAPIVersion.TWO_THOUSAND_AND_TWENTY_FIVE_MINUS_06_MINUS_15)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                    | Type                                                                                                                                                                                                                         | Required                                                                                                                                                                                                                     | Description                                                                                                                                                                                                                  |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `company_uuid`                                                                                                                                                                                                               | *str*                                                                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                                           | The UUID of the company                                                                                                                                                                                                      |
| `liability_selections`                                                                                                                                                                                                       | List[[models.LiabilitySelections](../../models/liabilityselections.md)]                                                                                                                                                      | :heavy_check_mark:                                                                                                                                                                                                           | Tax liability selections to record for the company's external payrolls.                                                                                                                                                      |
| `x_gusto_api_version`                                                                                                                                                                                                        | [Optional[models.PutV1TaxLiabilitiesHeaderXGustoAPIVersion]](../../models/putv1taxliabilitiesheaderxgustoapiversion.md)                                                                                                      | :heavy_minus_sign:                                                                                                                                                                                                           | Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used. |
| `retries`                                                                                                                                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                           | Configuration to override the default retry behavior of the client.                                                                                                                                                          |

### Response

**[List[models.TaxLiabilitiesSelections]](../../models/.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.NotFoundErrorObject | 404                        | application/json           |
| models.APIError            | 4XX, 5XX                   | \*/\*                      |

## finalize_tax_liabilities

Finalizes tax liabilities for a company. All external payrolls edit action will be disabled.

### Asynchronous processing
This endpoint triggers an asynchronous operation. The external payrolls will be processed in the background after finalization.

scope: `external_payrolls:write`

### Example Usage

<!-- UsageSnippet language="python" operationID="put-v1-tax-liabilities-finish" method="put" path="/v1/companies/{company_uuid}/external_payrolls/tax_liabilities/finish" -->
```python
import gusto_embedded
from gusto_embedded import Gusto
import os


with Gusto(
    company_access_auth=os.getenv("GUSTO_COMPANY_ACCESS_AUTH", ""),
) as gusto:

    gusto.external_payrolls.finalize_tax_liabilities(company_uuid="<id>", x_gusto_api_version=gusto_embedded.PutV1TaxLiabilitiesFinishHeaderXGustoAPIVersion.TWO_THOUSAND_AND_TWENTY_FIVE_MINUS_06_MINUS_15)

    # Use the SDK ...

```

### Parameters

| Parameter                                                                                                                                                                                                                    | Type                                                                                                                                                                                                                         | Required                                                                                                                                                                                                                     | Description                                                                                                                                                                                                                  |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `company_uuid`                                                                                                                                                                                                               | *str*                                                                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                                           | The UUID of the company                                                                                                                                                                                                      |
| `x_gusto_api_version`                                                                                                                                                                                                        | [Optional[models.PutV1TaxLiabilitiesFinishHeaderXGustoAPIVersion]](../../models/putv1taxliabilitiesfinishheaderxgustoapiversion.md)                                                                                          | :heavy_minus_sign:                                                                                                                                                                                                           | Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used. |
| `retries`                                                                                                                                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                           | Configuration to override the default retry behavior of the client.                                                                                                                                                          |

### Errors

| Error Type                       | Status Code                      | Content Type                     |
| -------------------------------- | -------------------------------- | -------------------------------- |
| models.NotFoundErrorObject       | 404                              | application/json                 |
| models.UnprocessableEntityError1 | 422                              | application/json                 |
| models.APIError                  | 4XX, 5XX                         | \*/\*                            |