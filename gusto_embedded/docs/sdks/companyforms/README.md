# CompanyForms

## Overview

### Available Operations

* [get_all](#get_all) - Get all company forms
* [get](#get) - Get a company form
* [get_pdf](#get_pdf) - Get a company form pdf
* [sign](#sign) - Sign a company form

## get_all

Get a list of all company's forms

### Related guides
- [Company Forms](doc:company-form)

scope: `company_forms:read`

### Example Usage

<!-- UsageSnippet language="python" operationID="get-v1-company-forms" method="get" path="/v1/companies/{company_id}/forms" -->
```python
import gusto_embedded
from gusto_embedded import Gusto
import os


with Gusto(
    company_access_auth=os.getenv("GUSTO_COMPANY_ACCESS_AUTH", ""),
) as gusto:

    res = gusto.company_forms.get_all(company_id="<id>", x_gusto_api_version=gusto_embedded.GetV1CompanyFormsHeaderXGustoAPIVersion.TWO_THOUSAND_AND_TWENTY_FIVE_MINUS_06_MINUS_15, sort_by="created_at:asc")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                    | Type                                                                                                                                                                                                                         | Required                                                                                                                                                                                                                     | Description                                                                                                                                                                                                                  | Example                                                                                                                                                                                                                      |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `company_id`                                                                                                                                                                                                                 | *str*                                                                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                                           | The UUID of the company                                                                                                                                                                                                      |                                                                                                                                                                                                                              |
| `x_gusto_api_version`                                                                                                                                                                                                        | [Optional[models.GetV1CompanyFormsHeaderXGustoAPIVersion]](../../models/getv1companyformsheaderxgustoapiversion.md)                                                                                                          | :heavy_minus_sign:                                                                                                                                                                                                           | Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used. |                                                                                                                                                                                                                              |
| `sort_by`                                                                                                                                                                                                                    | *Optional[str]*                                                                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                           | Sort by one or more fields. Options: created_at, name, year, quarter, draft, document_content_type. Append `:asc` or `:desc` to specify direction (e.g., `created_at:asc`). Defaults to ascending.                           | created_at:asc                                                                                                                                                                                                               |
| `page`                                                                                                                                                                                                                       | *Optional[int]*                                                                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                           | The page that is requested. When unspecified, will load all objects unless endpoint forces pagination.                                                                                                                       |                                                                                                                                                                                                                              |
| `per`                                                                                                                                                                                                                        | *Optional[int]*                                                                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                           | Number of objects per page. For majority of endpoints will default to 25                                                                                                                                                     |                                                                                                                                                                                                                              |
| `retries`                                                                                                                                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                           | Configuration to override the default retry behavior of the client.                                                                                                                                                          |                                                                                                                                                                                                                              |

### Response

**[List[models.Form]](../../models/.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.NotFoundErrorObject | 404                        | application/json           |
| models.APIError            | 4XX, 5XX                   | \*/\*                      |

## get

Get a company form

scope: `company_forms:read`

### Example Usage

<!-- UsageSnippet language="python" operationID="get-v1-company-form" method="get" path="/v1/forms/{form_id}" -->
```python
import gusto_embedded
from gusto_embedded import Gusto
import os


with Gusto(
    company_access_auth=os.getenv("GUSTO_COMPANY_ACCESS_AUTH", ""),
) as gusto:

    res = gusto.company_forms.get(form_id="<id>", x_gusto_api_version=gusto_embedded.GetV1CompanyFormHeaderXGustoAPIVersion.TWO_THOUSAND_AND_TWENTY_FIVE_MINUS_06_MINUS_15)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                    | Type                                                                                                                                                                                                                         | Required                                                                                                                                                                                                                     | Description                                                                                                                                                                                                                  |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `form_id`                                                                                                                                                                                                                    | *str*                                                                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                                           | The UUID of the form                                                                                                                                                                                                         |
| `x_gusto_api_version`                                                                                                                                                                                                        | [Optional[models.GetV1CompanyFormHeaderXGustoAPIVersion]](../../models/getv1companyformheaderxgustoapiversion.md)                                                                                                            | :heavy_minus_sign:                                                                                                                                                                                                           | Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used. |
| `retries`                                                                                                                                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                           | Configuration to override the default retry behavior of the client.                                                                                                                                                          |

### Response

**[models.Form](../../models/form.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.NotFoundErrorObject | 404                        | application/json           |
| models.APIError            | 4XX, 5XX                   | \*/\*                      |

## get_pdf

Get the link to the form PDF

scope: `company_forms:read`

### Example Usage

<!-- UsageSnippet language="python" operationID="get-v1-company-form-pdf" method="get" path="/v1/forms/{form_id}/pdf" -->
```python
import gusto_embedded
from gusto_embedded import Gusto
import os


with Gusto(
    company_access_auth=os.getenv("GUSTO_COMPANY_ACCESS_AUTH", ""),
) as gusto:

    res = gusto.company_forms.get_pdf(form_id="<id>", x_gusto_api_version=gusto_embedded.GetV1CompanyFormPdfHeaderXGustoAPIVersion.TWO_THOUSAND_AND_TWENTY_FIVE_MINUS_06_MINUS_15)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                    | Type                                                                                                                                                                                                                         | Required                                                                                                                                                                                                                     | Description                                                                                                                                                                                                                  |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `form_id`                                                                                                                                                                                                                    | *str*                                                                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                                           | The UUID of the form                                                                                                                                                                                                         |
| `x_gusto_api_version`                                                                                                                                                                                                        | [Optional[models.GetV1CompanyFormPdfHeaderXGustoAPIVersion]](../../models/getv1companyformpdfheaderxgustoapiversion.md)                                                                                                      | :heavy_minus_sign:                                                                                                                                                                                                           | Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used. |
| `retries`                                                                                                                                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                           | Configuration to override the default retry behavior of the client.                                                                                                                                                          |

### Response

**[models.FormPdf](../../models/formpdf.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.NotFoundErrorObject | 404                        | application/json           |
| models.APIError            | 4XX, 5XX                   | \*/\*                      |

## sign

Sign a company form. Company forms must be signed by the company signatory.

scope: `company_forms:sign`

### Example Usage

<!-- UsageSnippet language="python" operationID="put-v1-company-form-sign" method="put" path="/v1/forms/{form_id}/sign" -->
```python
import gusto_embedded
from gusto_embedded import Gusto
import os


with Gusto(
    company_access_auth=os.getenv("GUSTO_COMPANY_ACCESS_AUTH", ""),
) as gusto:

    res = gusto.company_forms.sign(form_id="<id>", signature_text="<value>", agree=True, x_gusto_api_version=gusto_embedded.PutV1CompanyFormSignHeaderXGustoAPIVersion.TWO_THOUSAND_AND_TWENTY_FIVE_MINUS_06_MINUS_15)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                                                                        | Type                                                                                                                                                                                                                                                                             | Required                                                                                                                                                                                                                                                                         | Description                                                                                                                                                                                                                                                                      |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `form_id`                                                                                                                                                                                                                                                                        | *str*                                                                                                                                                                                                                                                                            | :heavy_check_mark:                                                                                                                                                                                                                                                               | The UUID of the form                                                                                                                                                                                                                                                             |
| `signature_text`                                                                                                                                                                                                                                                                 | *str*                                                                                                                                                                                                                                                                            | :heavy_check_mark:                                                                                                                                                                                                                                                               | The signature                                                                                                                                                                                                                                                                    |
| `agree`                                                                                                                                                                                                                                                                          | *bool*                                                                                                                                                                                                                                                                           | :heavy_check_mark:                                                                                                                                                                                                                                                               | Whether you agree to sign electronically                                                                                                                                                                                                                                         |
| `x_gusto_api_version`                                                                                                                                                                                                                                                            | [Optional[models.PutV1CompanyFormSignHeaderXGustoAPIVersion]](../../models/putv1companyformsignheaderxgustoapiversion.md)                                                                                                                                                        | :heavy_minus_sign:                                                                                                                                                                                                                                                               | Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used.                                                     |
| `x_gusto_client_ip`                                                                                                                                                                                                                                                              | *Optional[str]*                                                                                                                                                                                                                                                                  | :heavy_minus_sign:                                                                                                                                                                                                                                                               | Optional header to supply the IP address. This can be used to supply the IP address for signature endpoints instead of the signed_by_ip_address parameter.                                                                                                                       |
| `signed_by_ip_address`                                                                                                                                                                                                                                                           | *Optional[str]*                                                                                                                                                                                                                                                                  | :heavy_minus_sign:                                                                                                                                                                                                                                                               | The IP address of the signatory who signed the form. Both IPv4 AND IPv6 are supported. You must provide the IP address with either this parameter OR you can leave out this parameter and set the IP address in the request header using the `x-gusto-client-ip` header instead. |
| `retries`                                                                                                                                                                                                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                                                                                                                               | Configuration to override the default retry behavior of the client.                                                                                                                                                                                                              |

### Response

**[models.Form](../../models/form.md)**

### Errors

| Error Type                       | Status Code                      | Content Type                     |
| -------------------------------- | -------------------------------- | -------------------------------- |
| models.NotFoundErrorObject       | 404                              | application/json                 |
| models.UnprocessableEntityError1 | 422                              | application/json                 |
| models.APIError                  | 4XX, 5XX                         | \*/\*                            |