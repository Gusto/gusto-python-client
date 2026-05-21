# Signatories

## Overview

### Available Operations

* [list](#list) - Get the signatories for a company
* [create](#create) - Create a signatory
* [invite](#invite) - Invite a signatory
* [update](#update) - Update a signatory
* [delete](#delete) - Delete a signatory

## list

Returns the signatories for a company. A company has at most one signatory.

## Related guides
- [Signatory Events](doc:signatory-events)

scope: `signatories:read`

### Example Usage

<!-- UsageSnippet language="python" operationID="get-v1-companies-company_uuid-signatories" method="get" path="/v1/companies/{company_uuid}/signatories" -->
```python
import gusto_embedded_v_2025_11_15
from gusto_embedded_v_2025_11_15 import Gusto
import os


with Gusto(
    company_access_auth=os.getenv("GUSTO_COMPANY_ACCESS_AUTH", ""),
) as gusto:

    res = gusto.signatories.list(company_uuid="<id>", x_gusto_api_version=gusto_embedded_v_2025_11_15.GetV1CompaniesCompanyUUIDSignatoriesHeaderXGustoAPIVersion.TWO_THOUSAND_AND_TWENTY_FIVE_MINUS_11_MINUS_15)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                    | Type                                                                                                                                                                                                                         | Required                                                                                                                                                                                                                     | Description                                                                                                                                                                                                                  |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `company_uuid`                                                                                                                                                                                                               | *str*                                                                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                                           | The UUID of the company                                                                                                                                                                                                      |
| `x_gusto_api_version`                                                                                                                                                                                                        | [Optional[models.GetV1CompaniesCompanyUUIDSignatoriesHeaderXGustoAPIVersion]](../../models/getv1companiescompanyuuidsignatoriesheaderxgustoapiversion.md)                                                                    | :heavy_minus_sign:                                                                                                                                                                                                           | Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used. |
| `retries`                                                                                                                                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                           | Configuration to override the default retry behavior of the client.                                                                                                                                                          |

### Response

**[List[models.Signatory]](../../models/.md)**

### Errors

| Error Type                      | Status Code                     | Content Type                    |
| ------------------------------- | ------------------------------- | ------------------------------- |
| models.NotFoundErrorObjectError | 404                             | application/json                |
| models.APIError                 | 4XX, 5XX                        | \*/\*                           |

## create

Creates a company signatory with complete information. The company must not already have a signatory.

A signatory can legally sign forms once the identity verification process is successful. The signatory should be an officer, owner, general partner or LLC member manager, plan administrator, fiduciary, or an authorized representative who is designated to sign agreements on the company's behalf. An officer is the president, vice president, treasurer, chief accounting officer, etc. There can only be a single primary signatory in a company.

### Webhooks
- `signatory.created`: Fires when a signatory is successfully created.

### Related guides
- [Signatory Events](doc:signatory-events)

scope: `signatories:manage`

### Example Usage

<!-- UsageSnippet language="python" operationID="post-v1-company-signatories" method="post" path="/v1/companies/{company_uuid}/signatories" -->
```python
from datetime import date
import gusto_embedded_v_2025_11_15
from gusto_embedded_v_2025_11_15 import Gusto
import os


with Gusto(
    company_access_auth=os.getenv("GUSTO_COMPANY_ACCESS_AUTH", ""),
) as gusto:

    res = gusto.signatories.create(company_uuid="<id>", first_name="Ed", last_name="Reichert", title="<value>", phone="914.468.8146 x29683", birthday=date.fromisoformat("2026-11-04"), email="Mariah_Huel64@gmail.com", ssn="<value>", home_address={
        "street_1": "<value>",
        "city": "East Paxtonborough",
        "state": "Rhode Island",
        "zip": "37195",
    }, x_gusto_api_version=gusto_embedded_v_2025_11_15.PostV1CompanySignatoriesHeaderXGustoAPIVersion.TWO_THOUSAND_AND_TWENTY_FIVE_MINUS_11_MINUS_15)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                    | Type                                                                                                                                                                                                                         | Required                                                                                                                                                                                                                     | Description                                                                                                                                                                                                                  |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `company_uuid`                                                                                                                                                                                                               | *str*                                                                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                                           | The UUID of the company                                                                                                                                                                                                      |
| `first_name`                                                                                                                                                                                                                 | *str*                                                                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                                           | The signatory's first name.                                                                                                                                                                                                  |
| `last_name`                                                                                                                                                                                                                  | *str*                                                                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                                           | The signatory's last name.                                                                                                                                                                                                   |
| `title`                                                                                                                                                                                                                      | *str*                                                                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                                           | The signatory's title (e.g. CEO, President).                                                                                                                                                                                 |
| `phone`                                                                                                                                                                                                                      | *str*                                                                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                                           | The signatory's phone number.                                                                                                                                                                                                |
| `birthday`                                                                                                                                                                                                                   | [datetime](https://docs.python.org/3/library/datetime.html#datetime-objects)                                                                                                                                                 | :heavy_check_mark:                                                                                                                                                                                                           | The signatory's date of birth.                                                                                                                                                                                               |
| `email`                                                                                                                                                                                                                      | *str*                                                                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                                           | The signatory's email address.                                                                                                                                                                                               |
| `ssn`                                                                                                                                                                                                                        | *str*                                                                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                                           | The signatory's SSN.                                                                                                                                                                                                         |
| `home_address`                                                                                                                                                                                                               | [models.SignatoryCreateRequestHomeAddress](../../models/signatorycreaterequesthomeaddress.md)                                                                                                                                | :heavy_check_mark:                                                                                                                                                                                                           | The signatory's home address.                                                                                                                                                                                                |
| `x_gusto_api_version`                                                                                                                                                                                                        | [Optional[models.PostV1CompanySignatoriesHeaderXGustoAPIVersion]](../../models/postv1companysignatoriesheaderxgustoapiversion.md)                                                                                            | :heavy_minus_sign:                                                                                                                                                                                                           | Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used. |
| `middle_initial`                                                                                                                                                                                                             | *Optional[str]*                                                                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                           | N/A                                                                                                                                                                                                                          |
| `retries`                                                                                                                                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                           | Configuration to override the default retry behavior of the client.                                                                                                                                                          |

### Response

**[models.Signatory](../../models/signatory.md)**

### Errors

| Error Type                       | Status Code                      | Content Type                     |
| -------------------------------- | -------------------------------- | -------------------------------- |
| models.NotFoundErrorObjectError  | 404                              | application/json                 |
| models.UnprocessableEntityError1 | 422                              | application/json                 |
| models.APIError                  | 4XX, 5XX                         | \*/\*                            |

## invite

Creates a signatory with minimal information. This signatory can be invited to provide more information through the [Update a signatory](ref:put-v1-companies-company_uuid-signatories-signatory_uuid) endpoint. This will start the identity verification process and allow the signatory to be verified to sign documents.

## Related guides
- [Signatory Events](doc:signatory-events)

scope: `signatories:manage`

### Example Usage

<!-- UsageSnippet language="python" operationID="post-v1-companies-company_uuid-signatories-invite" method="post" path="/v1/companies/{company_uuid}/signatories/invite" -->
```python
import gusto_embedded_v_2025_11_15
from gusto_embedded_v_2025_11_15 import Gusto
import os


with Gusto(
    company_access_auth=os.getenv("GUSTO_COMPANY_ACCESS_AUTH", ""),
) as gusto:

    res = gusto.signatories.invite(company_uuid="<id>", first_name="Madelyn", last_name="Littel", email="Harmon_Heidenreich@yahoo.com", x_gusto_api_version=gusto_embedded_v_2025_11_15.PostV1CompaniesCompanyUUIDSignatoriesInviteHeaderXGustoAPIVersion.TWO_THOUSAND_AND_TWENTY_FIVE_MINUS_11_MINUS_15)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                    | Type                                                                                                                                                                                                                         | Required                                                                                                                                                                                                                     | Description                                                                                                                                                                                                                  |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `company_uuid`                                                                                                                                                                                                               | *str*                                                                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                                           | The UUID of the company                                                                                                                                                                                                      |
| `first_name`                                                                                                                                                                                                                 | *str*                                                                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                                           | The signatory's first name.                                                                                                                                                                                                  |
| `last_name`                                                                                                                                                                                                                  | *str*                                                                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                                           | The signatory's last name.                                                                                                                                                                                                   |
| `email`                                                                                                                                                                                                                      | *str*                                                                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                                           | The signatory's email address.                                                                                                                                                                                               |
| `x_gusto_api_version`                                                                                                                                                                                                        | [Optional[models.PostV1CompaniesCompanyUUIDSignatoriesInviteHeaderXGustoAPIVersion]](../../models/postv1companiescompanyuuidsignatoriesinviteheaderxgustoapiversion.md)                                                      | :heavy_minus_sign:                                                                                                                                                                                                           | Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used. |
| `middle_initial`                                                                                                                                                                                                             | *Optional[str]*                                                                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                           | N/A                                                                                                                                                                                                                          |
| `title`                                                                                                                                                                                                                      | *Optional[str]*                                                                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                           | The signatory's title (e.g. CEO, President).                                                                                                                                                                                 |
| `phone`                                                                                                                                                                                                                      | *Optional[str]*                                                                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                           | The signatory's phone number.                                                                                                                                                                                                |
| `birthday`                                                                                                                                                                                                                   | [datetime](https://docs.python.org/3/library/datetime.html#datetime-objects)                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                                                                           | The signatory's date of birth.                                                                                                                                                                                               |
| `ssn`                                                                                                                                                                                                                        | *Optional[str]*                                                                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                           | The signatory's SSN. Required for create with complete information; not used for invite.                                                                                                                                     |
| `home_address`                                                                                                                                                                                                               | [Optional[models.SignatoryInviteRequestHomeAddress]](../../models/signatoryinviterequesthomeaddress.md)                                                                                                                      | :heavy_minus_sign:                                                                                                                                                                                                           | The signatory's home address.                                                                                                                                                                                                |
| `retries`                                                                                                                                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                           | Configuration to override the default retry behavior of the client.                                                                                                                                                          |

### Response

**[models.Signatory](../../models/signatory.md)**

### Errors

| Error Type                       | Status Code                      | Content Type                     |
| -------------------------------- | -------------------------------- | -------------------------------- |
| models.NotFoundErrorObjectError  | 404                              | application/json                 |
| models.UnprocessableEntityError1 | 422                              | application/json                 |
| models.APIError                  | 4XX, 5XX                         | \*/\*                            |

## update

Updates a signatory that has been either invited or created. If the signatory has been created with minimal information through the [Invite a signatory](ref:post-v1-companies-company_uuid-signatories-invite) endpoint, then the first update must contain all attributes specified in the request body in order to start the identity verification process.

## Related guides
- [Signatory Events](doc:signatory-events)

scope: `signatories:write`

### Example Usage

<!-- UsageSnippet language="python" operationID="put-v1-companies-company_uuid-signatories-signatory_uuid" method="put" path="/v1/companies/{company_uuid}/signatories/{signatory_uuid}" -->
```python
import gusto_embedded_v_2025_11_15
from gusto_embedded_v_2025_11_15 import Gusto
import os


with Gusto(
    company_access_auth=os.getenv("GUSTO_COMPANY_ACCESS_AUTH", ""),
) as gusto:

    res = gusto.signatories.update(company_uuid="<id>", signatory_uuid="<id>", version="<value>", x_gusto_api_version=gusto_embedded_v_2025_11_15.PutV1CompaniesCompanyUUIDSignatoriesSignatoryUUIDHeaderXGustoAPIVersion.TWO_THOUSAND_AND_TWENTY_FIVE_MINUS_11_MINUS_15)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                    | Type                                                                                                                                                                                                                         | Required                                                                                                                                                                                                                     | Description                                                                                                                                                                                                                  |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `company_uuid`                                                                                                                                                                                                               | *str*                                                                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                                           | The UUID of the company                                                                                                                                                                                                      |
| `signatory_uuid`                                                                                                                                                                                                             | *str*                                                                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                                           | The UUID of the signatory                                                                                                                                                                                                    |
| `version`                                                                                                                                                                                                                    | *str*                                                                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                                           | Current version of the signatory (required for optimistic concurrency).                                                                                                                                                      |
| `x_gusto_api_version`                                                                                                                                                                                                        | [Optional[models.PutV1CompaniesCompanyUUIDSignatoriesSignatoryUUIDHeaderXGustoAPIVersion]](../../models/putv1companiescompanyuuidsignatoriessignatoryuuidheaderxgustoapiversion.md)                                          | :heavy_minus_sign:                                                                                                                                                                                                           | Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used. |
| `first_name`                                                                                                                                                                                                                 | *Optional[str]*                                                                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                           | N/A                                                                                                                                                                                                                          |
| `middle_initial`                                                                                                                                                                                                             | *Optional[str]*                                                                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                           | N/A                                                                                                                                                                                                                          |
| `last_name`                                                                                                                                                                                                                  | *Optional[str]*                                                                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                           | N/A                                                                                                                                                                                                                          |
| `title`                                                                                                                                                                                                                      | *Optional[str]*                                                                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                           | N/A                                                                                                                                                                                                                          |
| `phone`                                                                                                                                                                                                                      | *Optional[str]*                                                                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                           | N/A                                                                                                                                                                                                                          |
| `birthday`                                                                                                                                                                                                                   | [datetime](https://docs.python.org/3/library/datetime.html#datetime-objects)                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                                                                           | N/A                                                                                                                                                                                                                          |
| `ssn`                                                                                                                                                                                                                        | *Optional[str]*                                                                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                           | The signatory's SSN.                                                                                                                                                                                                         |
| `home_address`                                                                                                                                                                                                               | [Optional[models.SignatoryUpdateRequestHomeAddress]](../../models/signatoryupdaterequesthomeaddress.md)                                                                                                                      | :heavy_minus_sign:                                                                                                                                                                                                           | N/A                                                                                                                                                                                                                          |
| `retries`                                                                                                                                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                           | Configuration to override the default retry behavior of the client.                                                                                                                                                          |

### Response

**[models.Signatory](../../models/signatory.md)**

### Errors

| Error Type                       | Status Code                      | Content Type                     |
| -------------------------------- | -------------------------------- | -------------------------------- |
| models.NotFoundErrorObjectError  | 404                              | application/json                 |
| models.UnprocessableEntityError1 | 409, 422                         | application/json                 |
| models.APIError                  | 4XX, 5XX                         | \*/\*                            |

## delete

Deletes a company signatory.

## Related guides
- [Signatory Events](doc:signatory-events)

scope: `signatories:manage`

### Example Usage

<!-- UsageSnippet language="python" operationID="delete-v1-companies-company_uuid-signatories-signatory_uuid" method="delete" path="/v1/companies/{company_uuid}/signatories/{signatory_uuid}" -->
```python
import gusto_embedded_v_2025_11_15
from gusto_embedded_v_2025_11_15 import Gusto
import os


with Gusto(
    company_access_auth=os.getenv("GUSTO_COMPANY_ACCESS_AUTH", ""),
) as gusto:

    gusto.signatories.delete(company_uuid="<id>", signatory_uuid="<id>", x_gusto_api_version=gusto_embedded_v_2025_11_15.DeleteV1CompaniesCompanyUUIDSignatoriesSignatoryUUIDHeaderXGustoAPIVersion.TWO_THOUSAND_AND_TWENTY_FIVE_MINUS_11_MINUS_15)

    # Use the SDK ...

```

### Parameters

| Parameter                                                                                                                                                                                                                    | Type                                                                                                                                                                                                                         | Required                                                                                                                                                                                                                     | Description                                                                                                                                                                                                                  |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `company_uuid`                                                                                                                                                                                                               | *str*                                                                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                                           | The UUID of the company                                                                                                                                                                                                      |
| `signatory_uuid`                                                                                                                                                                                                             | *str*                                                                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                                           | The UUID of the signatory                                                                                                                                                                                                    |
| `x_gusto_api_version`                                                                                                                                                                                                        | [Optional[models.DeleteV1CompaniesCompanyUUIDSignatoriesSignatoryUUIDHeaderXGustoAPIVersion]](../../models/deletev1companiescompanyuuidsignatoriessignatoryuuidheaderxgustoapiversion.md)                                    | :heavy_minus_sign:                                                                                                                                                                                                           | Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used. |
| `retries`                                                                                                                                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                           | Configuration to override the default retry behavior of the client.                                                                                                                                                          |

### Errors

| Error Type                      | Status Code                     | Content Type                    |
| ------------------------------- | ------------------------------- | ------------------------------- |
| models.NotFoundErrorObjectError | 404                             | application/json                |
| models.APIError                 | 4XX, 5XX                        | \*/\*                           |