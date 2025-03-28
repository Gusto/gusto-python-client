# Suspensions
(*companies.suspensions*)

## Overview

### Available Operations

* [get](#get) - Get suspensions for this company
* [suspend](#suspend) - Suspend a company's account

## get

Get existing suspension records for this company. A company may have multiple suspension records if they have suspended their Gusto account more than once. 

> 📘 To check if company is already suspended
>
> To determine if a company is _currently_ suspended, use the `is_suspended` and `company_status` fields in the [Get a company](https://docs.gusto.com/embedded-payroll/reference/get-v1-companies) endpoint.

scope: `company_suspensions:read`

### Example Usage

```python
from gusto_embedded import Gusto
import os


with Gusto(
    company_access_auth=os.getenv("GUSTO_COMPANY_ACCESS_AUTH", ""),
) as gusto:

    res = gusto.companies.suspensions.get(company_uuid="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                    | Type                                                                                                                                                                                                                         | Required                                                                                                                                                                                                                     | Description                                                                                                                                                                                                                  |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `company_uuid`                                                                                                                                                                                                               | *str*                                                                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                                           | The UUID of the company                                                                                                                                                                                                      |
| `x_gusto_api_version`                                                                                                                                                                                                        | [Optional[models.VersionHeader]](../../models/versionheader.md)                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                           | Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used. |
| `retries`                                                                                                                                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                           | Configuration to override the default retry behavior of the client.                                                                                                                                                          |

### Response

**[List[models.CompanySuspension]](../../models/.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## suspend

Use this endpoint to suspend a company. After suspension, company will no longer be able to run payroll but will retain access to their information, such as retrieving employee info or retrieving past payrolls.

scope: `company_suspensions:write`

### Example Usage

```python
import gusto_embedded
from gusto_embedded import Gusto
import os


with Gusto(
    company_access_auth=os.getenv("GUSTO_COMPANY_ACCESS_AUTH", ""),
) as gusto:

    res = gusto.companies.suspensions.suspend(company_uuid="<id>", file_quarterly_forms=True, file_yearly_forms=True, reconcile_tax_method=gusto_embedded.PostCompaniesCompanyUUIDSuspensionsReconcileTaxMethod.PAY_TAXES, reason=gusto_embedded.Reason.SWITCHING_PROVIDER, leaving_for=gusto_embedded.LeavingFor.OTHER)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                                                                                           | Type                                                                                                                                                                                                                                                                                                | Required                                                                                                                                                                                                                                                                                            | Description                                                                                                                                                                                                                                                                                         |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `company_uuid`                                                                                                                                                                                                                                                                                      | *str*                                                                                                                                                                                                                                                                                               | :heavy_check_mark:                                                                                                                                                                                                                                                                                  | The UUID of the company                                                                                                                                                                                                                                                                             |
| `file_quarterly_forms`                                                                                                                                                                                                                                                                              | *bool*                                                                                                                                                                                                                                                                                              | :heavy_check_mark:                                                                                                                                                                                                                                                                                  | Should Gusto file quarterly tax forms on behalf of the company? The correct answer can depend on why the company is suspending their account, and how taxes are being reconciled.                                                                                                                   |
| `file_yearly_forms`                                                                                                                                                                                                                                                                                 | *bool*                                                                                                                                                                                                                                                                                              | :heavy_check_mark:                                                                                                                                                                                                                                                                                  | Should Gusto file yearly tax forms on behalf of the company? The correct answer can depend on why the company is suspending their account, and how taxes are being reconciled.                                                                                                                      |
| `reconcile_tax_method`                                                                                                                                                                                                                                                                              | [models.PostCompaniesCompanyUUIDSuspensionsReconcileTaxMethod](../../models/postcompaniescompanyuuidsuspensionsreconciletaxmethod.md)                                                                                                                                                               | :heavy_check_mark:                                                                                                                                                                                                                                                                                  | How Gusto will handle taxes already collected.                                                                                                                                                                                                                                                      |
| `reason`                                                                                                                                                                                                                                                                                            | [models.Reason](../../models/reason.md)                                                                                                                                                                                                                                                             | :heavy_check_mark:                                                                                                                                                                                                                                                                                  | Explanation for why the company is suspending their account.<br/><br/>> 🚧 FEIN or entity type changes require Customer Support<br/>><br/>> If a company is switching FEIN or changing their entity type, this change must be performed by Gusto Customer Support and cannot be performed via the API at this time. |
| `x_gusto_api_version`                                                                                                                                                                                                                                                                               | [Optional[models.VersionHeader]](../../models/versionheader.md)                                                                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                                                                                                                  | Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used.                                                                        |
| `comments`                                                                                                                                                                                                                                                                                          | *Optional[str]*                                                                                                                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                                                                                                                  | User-supplied comments describing why they are suspending their account.                                                                                                                                                                                                                            |
| `leaving_for`                                                                                                                                                                                                                                                                                       | [Optional[models.LeavingFor]](../../models/leavingfor.md)                                                                                                                                                                                                                                           | :heavy_minus_sign:                                                                                                                                                                                                                                                                                  | Which competitor the company is joining instead. Required if `reason` is `'switching_provider'`.                                                                                                                                                                                                    |
| `retries`                                                                                                                                                                                                                                                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                                                                    | :heavy_minus_sign:                                                                                                                                                                                                                                                                                  | Configuration to override the default retry behavior of the client.                                                                                                                                                                                                                                 |

### Response

**[models.CompanySuspension](../../models/companysuspension.md)**

### Errors

| Error Type                            | Status Code                           | Content Type                          |
| ------------------------------------- | ------------------------------------- | ------------------------------------- |
| models.UnprocessableEntityErrorObject | 422                                   | application/json                      |
| models.APIError                       | 4XX, 5XX                              | \*/\*                                 |