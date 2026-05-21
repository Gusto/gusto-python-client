# FederalTaxDetails

## Overview

### Available Operations

* [get](#get) - Get a company's federal tax details
* [update](#update) - Update a company's federal tax details

## get

Retrieves a company's federal tax details including EIN verification status, tax payer type, filing form, and other federal tax configuration.

scope: `company_federal_taxes:read`

### Example Usage

<!-- UsageSnippet language="python" operationID="get-v1-companies-company_id-federal_tax_details" method="get" path="/v1/companies/{company_id}/federal_tax_details" -->
```python
import gusto_embedded_v_2025_11_15
from gusto_embedded_v_2025_11_15 import Gusto
import os


with Gusto(
    company_access_auth=os.getenv("GUSTO_COMPANY_ACCESS_AUTH", ""),
) as gusto:

    res = gusto.federal_tax_details.get(company_id="7b1d0df1-6403-4a06-8768-c1dd7d24d27a", x_gusto_api_version=gusto_embedded_v_2025_11_15.GetV1CompaniesCompanyIDFederalTaxDetailsHeaderXGustoAPIVersion.TWO_THOUSAND_AND_TWENTY_FIVE_MINUS_11_MINUS_15)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                    | Type                                                                                                                                                                                                                         | Required                                                                                                                                                                                                                     | Description                                                                                                                                                                                                                  | Example                                                                                                                                                                                                                      |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `company_id`                                                                                                                                                                                                                 | *str*                                                                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                                           | The UUID of the company                                                                                                                                                                                                      | 7b1d0df1-6403-4a06-8768-c1dd7d24d27a                                                                                                                                                                                         |
| `x_gusto_api_version`                                                                                                                                                                                                        | [Optional[models.GetV1CompaniesCompanyIDFederalTaxDetailsHeaderXGustoAPIVersion]](../../models/getv1companiescompanyidfederaltaxdetailsheaderxgustoapiversion.md)                                                            | :heavy_minus_sign:                                                                                                                                                                                                           | Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used. |                                                                                                                                                                                                                              |
| `retries`                                                                                                                                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                           | Configuration to override the default retry behavior of the client.                                                                                                                                                          |                                                                                                                                                                                                                              |

### Response

**[models.FederalTaxDetails](../../models/federaltaxdetails.md)**

### Errors

| Error Type                      | Status Code                     | Content Type                    |
| ------------------------------- | ------------------------------- | ------------------------------- |
| models.NotFoundErrorObjectError | 404                             | application/json                |
| models.APIError                 | 4XX, 5XX                        | \*/\*                           |

## update

Updates a company's federal tax details including EIN, legal name, tax payer type, filing form, and S-Corp
taxation status. This information is required to onboard a company for use with Gusto Embedded Payroll.

### Prerequisites
Before calling this endpoint, retrieve the current federal tax details and `version` via [GET /v1/companies/{company_id}/federal_tax_details](ref:get-v1-companies-company_id-federal_tax_details)

### Webhooks
- `company.updated`: Fires when federal tax details for a company are successfully updated

**Setup:** [POST /v1/webhook_subscriptions](ref:post-v1-webhook-subscription) with `subscription_types`: `["Company"]`

scope: `company_federal_taxes:write`

### Example Usage

<!-- UsageSnippet language="python" operationID="put-v1-companies-company_id-federal_tax_details" method="put" path="/v1/companies/{company_id}/federal_tax_details" -->
```python
import gusto_embedded_v_2025_11_15
from gusto_embedded_v_2025_11_15 import Gusto
import os


with Gusto(
    company_access_auth=os.getenv("GUSTO_COMPANY_ACCESS_AUTH", ""),
) as gusto:

    res = gusto.federal_tax_details.update(company_id="7b1d0df1-6403-4a06-8768-c1dd7d24d27a", version="6cb95e00540706ca48d4577b3c839fbe", x_gusto_api_version=gusto_embedded_v_2025_11_15.PutV1CompaniesCompanyIDFederalTaxDetailsHeaderXGustoAPIVersion.TWO_THOUSAND_AND_TWENTY_FIVE_MINUS_11_MINUS_15, legal_name="Acme Corp.", ein="123456789", tax_payer_type=gusto_embedded_v_2025_11_15.FederalTaxDetailsUpdateTaxPayerType.LLP, filing_form=gusto_embedded_v_2025_11_15.FederalTaxDetailsUpdateFilingForm.NINE_HUNDRED_AND_FORTY_FOUR, taxable_as_scorp=False)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                         | Type                                                                                                                                                                                                                              | Required                                                                                                                                                                                                                          | Description                                                                                                                                                                                                                       | Example                                                                                                                                                                                                                           |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `company_id`                                                                                                                                                                                                                      | *str*                                                                                                                                                                                                                             | :heavy_check_mark:                                                                                                                                                                                                                | The UUID of the company                                                                                                                                                                                                           | 7b1d0df1-6403-4a06-8768-c1dd7d24d27a                                                                                                                                                                                              |
| `version`                                                                                                                                                                                                                         | *str*                                                                                                                                                                                                                             | :heavy_check_mark:                                                                                                                                                                                                                | The current version of the object. See the [versioning guide](https://docs.gusto.com/embedded-payroll/docs/idempotency) for information on how to use this field.                                                                 | 6cb95e00540706ca48d4577b3c839fbe                                                                                                                                                                                                  |
| `x_gusto_api_version`                                                                                                                                                                                                             | [Optional[models.PutV1CompaniesCompanyIDFederalTaxDetailsHeaderXGustoAPIVersion]](../../models/putv1companiescompanyidfederaltaxdetailsheaderxgustoapiversion.md)                                                                 | :heavy_minus_sign:                                                                                                                                                                                                                | Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used.      |                                                                                                                                                                                                                                   |
| `legal_name`                                                                                                                                                                                                                      | *Optional[str]*                                                                                                                                                                                                                   | :heavy_minus_sign:                                                                                                                                                                                                                | The legal name of the company                                                                                                                                                                                                     | Acme Corp.                                                                                                                                                                                                                        |
| `ein`                                                                                                                                                                                                                             | *Optional[str]*                                                                                                                                                                                                                   | :heavy_minus_sign:                                                                                                                                                                                                                | The company's Employer Identification Number (EIN). Must be 9 digits. Dashes are optional (e.g., '12-3456789' or '123456789').                                                                                                    | 123456789                                                                                                                                                                                                                         |
| `tax_payer_type`                                                                                                                                                                                                                  | [Optional[models.FederalTaxDetailsUpdateTaxPayerType]](../../models/federaltaxdetailsupdatetaxpayertype.md)                                                                                                                       | :heavy_minus_sign:                                                                                                                                                                                                                | What type of tax entity the company is. One of:<br/>- C-Corporation<br/>- S-Corporation<br/>- Sole proprietor<br/>- LLC<br/>- LLP<br/>- Limited partnership<br/>- Co-ownership<br/>- Association<br/>- Trusteeship<br/>- General partnership<br/>- Joint venture<br/>- Non-Profit | LLP                                                                                                                                                                                                                               |
| `filing_form`                                                                                                                                                                                                                     | [Optional[models.FederalTaxDetailsUpdateFilingForm]](../../models/federaltaxdetailsupdatefilingform.md)                                                                                                                           | :heavy_minus_sign:                                                                                                                                                                                                                | The form used by the company for federal tax filing. One of:<br/>- 941 (Quarterly federal tax return form)<br/>- 944 (Annual federal tax return form)                                                                             | 944                                                                                                                                                                                                                               |
| `taxable_as_scorp`                                                                                                                                                                                                                | *Optional[bool]*                                                                                                                                                                                                                  | :heavy_minus_sign:                                                                                                                                                                                                                | Whether the company is taxed as an S-Corporation                                                                                                                                                                                  | false                                                                                                                                                                                                                             |
| `retries`                                                                                                                                                                                                                         | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                  | :heavy_minus_sign:                                                                                                                                                                                                                | Configuration to override the default retry behavior of the client.                                                                                                                                                               |                                                                                                                                                                                                                                   |

### Response

**[models.FederalTaxDetails](../../models/federaltaxdetails.md)**

### Errors

| Error Type                       | Status Code                      | Content Type                     |
| -------------------------------- | -------------------------------- | -------------------------------- |
| models.NotFoundErrorObjectError  | 404                              | application/json                 |
| models.UnprocessableEntityError1 | 409, 422                         | application/json                 |
| models.APIError                  | 4XX, 5XX                         | \*/\*                            |