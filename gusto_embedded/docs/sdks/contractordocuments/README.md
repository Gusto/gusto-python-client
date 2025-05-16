# ContractorDocuments
(*contractor_documents*)

## Overview

### Available Operations

* [get_all](#get_all) - Get all contractor documents
* [get](#get) - Get a contractor document
* [get_pdf](#get_pdf) - Get the contractor document pdf
* [sign](#sign) - Sign a contractor document

## get_all

Get a list of all contractor's documents

scope: `contractor_documents:read`

### Example Usage

```python
from gusto_embedded import Gusto
import os


with Gusto(
    company_access_auth=os.getenv("GUSTO_COMPANY_ACCESS_AUTH", ""),
) as gusto:

    res = gusto.contractor_documents.get_all(contractor_uuid="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                    | Type                                                                                                                                                                                                                         | Required                                                                                                                                                                                                                     | Description                                                                                                                                                                                                                  |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `contractor_uuid`                                                                                                                                                                                                            | *str*                                                                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                                           | The UUID of the contractor                                                                                                                                                                                                   |
| `x_gusto_api_version`                                                                                                                                                                                                        | [Optional[models.VersionHeader]](../../models/versionheader.md)                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                           | Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used. |
| `retries`                                                                                                                                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                           | Configuration to override the default retry behavior of the client.                                                                                                                                                          |

### Response

**[List[models.Document]](../../models/.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## get

Get a contractor document.

scope: `contractor_documents:read`

### Example Usage

```python
from gusto_embedded import Gusto
import os


with Gusto(
    company_access_auth=os.getenv("GUSTO_COMPANY_ACCESS_AUTH", ""),
) as gusto:

    res = gusto.contractor_documents.get(document_uuid="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                    | Type                                                                                                                                                                                                                         | Required                                                                                                                                                                                                                     | Description                                                                                                                                                                                                                  |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `document_uuid`                                                                                                                                                                                                              | *str*                                                                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                                           | The ID or UUID of the document                                                                                                                                                                                               |
| `x_gusto_api_version`                                                                                                                                                                                                        | [Optional[models.VersionHeader]](../../models/versionheader.md)                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                           | Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used. |
| `retries`                                                                                                                                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                           | Configuration to override the default retry behavior of the client.                                                                                                                                                          |

### Response

**[models.Document](../../models/document.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## get_pdf

Get the contractor document pdf.

scope: `contractor_documents:read`

### Example Usage

```python
from gusto_embedded import Gusto
import os


with Gusto(
    company_access_auth=os.getenv("GUSTO_COMPANY_ACCESS_AUTH", ""),
) as gusto:

    res = gusto.contractor_documents.get_pdf(document_uuid="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                    | Type                                                                                                                                                                                                                         | Required                                                                                                                                                                                                                     | Description                                                                                                                                                                                                                  |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `document_uuid`                                                                                                                                                                                                              | *str*                                                                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                                           | The ID or UUID of the document                                                                                                                                                                                               |
| `x_gusto_api_version`                                                                                                                                                                                                        | [Optional[models.VersionHeader]](../../models/versionheader.md)                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                           | Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used. |
| `retries`                                                                                                                                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                           | Configuration to override the default retry behavior of the client.                                                                                                                                                          |

### Response

**[models.DocumentPdf](../../models/documentpdf.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## sign

Sign a contractor document.

scope: `contractor_documents:write`

### Example Usage

```python
from gusto_embedded import Gusto
import os


with Gusto(
    company_access_auth=os.getenv("GUSTO_COMPANY_ACCESS_AUTH", ""),
) as gusto:

    res = gusto.contractor_documents.sign(document_uuid="<id>", fields=[
        {},
        {},
        {},
    ], agree=True)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                                      | Type                                                                                                                                                                                                                                           | Required                                                                                                                                                                                                                                       | Description                                                                                                                                                                                                                                    |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `document_uuid`                                                                                                                                                                                                                                | *str*                                                                                                                                                                                                                                          | :heavy_check_mark:                                                                                                                                                                                                                             | The ID or UUID of the document                                                                                                                                                                                                                 |
| `fields`                                                                                                                                                                                                                                       | List[[models.PutV1ContractorDocumentSignFields](../../models/putv1contractordocumentsignfields.md)]                                                                                                                                            | :heavy_check_mark:                                                                                                                                                                                                                             | List of fields and the values they will be set to.                                                                                                                                                                                             |
| `agree`                                                                                                                                                                                                                                        | *bool*                                                                                                                                                                                                                                         | :heavy_check_mark:                                                                                                                                                                                                                             | Whether you agree to sign electronically                                                                                                                                                                                                       |
| `x_gusto_client_ip`                                                                                                                                                                                                                            | *Optional[str]*                                                                                                                                                                                                                                | :heavy_minus_sign:                                                                                                                                                                                                                             | Optional header to supply the IP address. This can be used to supply the IP address for signature endpoints instead of the signed_by_ip_address parameter.                                                                                     |
| `x_gusto_api_version`                                                                                                                                                                                                                          | [Optional[models.VersionHeader]](../../models/versionheader.md)                                                                                                                                                                                | :heavy_minus_sign:                                                                                                                                                                                                                             | Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used.                   |
| `signed_by_ip_address`                                                                                                                                                                                                                         | *Optional[str]*                                                                                                                                                                                                                                | :heavy_minus_sign:                                                                                                                                                                                                                             | The IP address of the signatory who signed the form. You must provide the IP address with either this parameter OR you can leave out this parameter and set the IP address in the request header using the `x-gusto-client-ip` header instead. |
| `retries`                                                                                                                                                                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                               | :heavy_minus_sign:                                                                                                                                                                                                                             | Configuration to override the default retry behavior of the client.                                                                                                                                                                            |

### Response

**[models.DocumentSigned](../../models/documentsigned.md)**

### Errors

| Error Type                                 | Status Code                                | Content Type                               |
| ------------------------------------------ | ------------------------------------------ | ------------------------------------------ |
| models.UnprocessableEntityErrorObjectError | 422                                        | application/json                           |
| models.APIError                            | 4XX, 5XX                                   | \*/\*                                      |