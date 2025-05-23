# FederalTaxDetailsSDK
(*federal_tax_details*)

## Overview

### Available Operations

* [get](#get) - Get Federal Tax Details
* [update](#update) - Update Federal Tax Details

## get

Fetches attributes relevant for a company's federal taxes.

scope: `company_federal_taxes:read`

### Example Usage

```python
from gusto_embedded import Gusto
import os


with Gusto(
    company_access_auth=os.getenv("GUSTO_COMPANY_ACCESS_AUTH", ""),
) as gusto:

    res = gusto.federal_tax_details.get(company_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                    | Type                                                                                                                                                                                                                         | Required                                                                                                                                                                                                                     | Description                                                                                                                                                                                                                  |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `company_id`                                                                                                                                                                                                                 | *str*                                                                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                                           | The UUID of the company                                                                                                                                                                                                      |
| `x_gusto_api_version`                                                                                                                                                                                                        | [Optional[models.VersionHeader]](../../models/versionheader.md)                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                           | Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used. |
| `retries`                                                                                                                                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                           | Configuration to override the default retry behavior of the client.                                                                                                                                                          |

### Response

**[models.FederalTaxDetails](../../models/federaltaxdetails.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## update

Updates attributes relevant for a company's federal taxes.
This information is required is to onboard a company for use with Gusto Embedded Payroll.

scope: `company_federal_taxes:write`

### Example Usage

```python
import gusto_embedded
from gusto_embedded import Gusto
import os


with Gusto(
    company_access_auth=os.getenv("GUSTO_COMPANY_ACCESS_AUTH", ""),
) as gusto:

    res = gusto.federal_tax_details.update(company_id="<id>", version="6cb95e00540706ca48d4577b3c839fbe", legal_name="Acme Corp.", tax_payer_type=gusto_embedded.TaxPayerType.LLP, filing_form=gusto_embedded.FilingForm.NINE_HUNDRED_AND_FORTY_FOUR, taxable_as_scorp=False)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                    | Type                                                                                                                                                                                                                         | Required                                                                                                                                                                                                                     | Description                                                                                                                                                                                                                  |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `company_id`                                                                                                                                                                                                                 | *str*                                                                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                                           | The UUID of the company                                                                                                                                                                                                      |
| `version`                                                                                                                                                                                                                    | *str*                                                                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                                           | The current version of the object. See the [versioning guide](https://docs.gusto.com/embedded-payroll/docs/versioning#object-layer) for information on how to use this field.                                                |
| `x_gusto_api_version`                                                                                                                                                                                                        | [Optional[models.VersionHeader]](../../models/versionheader.md)                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                           | Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used. |
| `legal_name`                                                                                                                                                                                                                 | *Optional[str]*                                                                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                           | The legal name of the company                                                                                                                                                                                                |
| `ein`                                                                                                                                                                                                                        | *Optional[str]*                                                                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                           | The EIN of of the company                                                                                                                                                                                                    |
| `tax_payer_type`                                                                                                                                                                                                             | [Optional[models.TaxPayerType]](../../models/taxpayertype.md)                                                                                                                                                                | :heavy_minus_sign:                                                                                                                                                                                                           | What type of tax entity the company is                                                                                                                                                                                       |
| `filing_form`                                                                                                                                                                                                                | [Optional[models.FilingForm]](../../models/filingform.md)                                                                                                                                                                    | :heavy_minus_sign:                                                                                                                                                                                                           | The form used by the company for federal tax filing. One of:<br/>- 941 (Quarterly federal tax return)<br/>- 944 (Annual federal tax return)                                                                                  |
| `taxable_as_scorp`                                                                                                                                                                                                           | *Optional[bool]*                                                                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                           | Whether this company should be taxed as an S-Corporation                                                                                                                                                                     |
| `retries`                                                                                                                                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                           | Configuration to override the default retry behavior of the client.                                                                                                                                                          |

### Response

**[models.FederalTaxDetails](../../models/federaltaxdetails.md)**

### Errors

| Error Type                                 | Status Code                                | Content Type                               |
| ------------------------------------------ | ------------------------------------------ | ------------------------------------------ |
| models.UnprocessableEntityErrorObjectError | 422                                        | application/json                           |
| models.APIError                            | 4XX, 5XX                                   | \*/\*                                      |