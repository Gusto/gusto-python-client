# Companies

## Overview

### Available Operations

* [create_partner_managed](#create_partner_managed) - Create a partner managed company
* [get](#get) - Get a company
* [update](#update) - Update a company
* [migrate](#migrate) - Migrate company to embedded payroll
* [get_v1_partner_managed_companies_company_uuid_migration_readiness](#get_v1_partner_managed_companies_company_uuid_migration_readiness) - Check company migration readiness
* [accept_terms_of_service](#accept_terms_of_service) - Accept terms of service for a company user
* [retrieve_terms_of_service](#retrieve_terms_of_service) - Retrieve terms of service status for a company user
* [list_admins](#list_admins) - Get all the admins at a company
* [create_admin](#create_admin) - Create an admin for the company
* [get_onboarding_status](#get_onboarding_status) - Get company onboarding status
* [finish_onboarding](#finish_onboarding) - Finish company onboarding
* [get_custom_fields](#get_custom_fields) - Get the custom fields of a company

## create_partner_managed

Create a partner managed company. When you successfully call the API, it does the following:
* Creates a new company in Gusto
* Creates a new user using the provided email if the user does not already exist.
* Makes the user the primary payroll administrator of the new company.

In response, you will receive oauth access tokens for the created company.

IMPORTANT: the returned access and refresh tokens are reserved for this company only. They cannot be used to access other companies AND previously granted tokens cannot be used to access this company.

📘 System Access Authentication

This endpoint uses the [Bearer Auth scheme with the system-level access token in the HTTP Authorization header](https://docs.gusto.com/embedded-payroll/docs/system-access)

scope: `partner_managed_companies:manage`

### Example Usage

<!-- UsageSnippet language="python" operationID="post-v1-partner-managed-companies" method="post" path="/v1/partner_managed_companies" -->
```python
import gusto_embedded_v_2025_11_15
from gusto_embedded_v_2025_11_15 import Gusto
import os


with Gusto() as gusto:

    res = gusto.companies.create_partner_managed(security=gusto_embedded_v_2025_11_15.PostV1PartnerManagedCompaniesSecurity(
        system_access_auth=os.getenv("GUSTO_SYSTEM_ACCESS_AUTH", ""),
    ), user={
        "first_name": "Marco",
        "last_name": "Trantow",
        "email": "Jewell_Greenholt72@hotmail.com",
    }, company={
        "name": "<value>",
    }, x_gusto_api_version=gusto_embedded_v_2025_11_15.PostV1PartnerManagedCompaniesHeaderXGustoAPIVersion.TWO_THOUSAND_AND_TWENTY_FIVE_MINUS_11_MINUS_15)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                    | Type                                                                                                                                                                                                                         | Required                                                                                                                                                                                                                     | Description                                                                                                                                                                                                                  |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `security`                                                                                                                                                                                                                   | [models.PostV1PartnerManagedCompaniesSecurity](../../models/postv1partnermanagedcompaniessecurity.md)                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                                           | N/A                                                                                                                                                                                                                          |
| `user`                                                                                                                                                                                                                       | [models.User](../../models/user.md)                                                                                                                                                                                          | :heavy_check_mark:                                                                                                                                                                                                           | Information for the user who will be the primary payroll administrator for the new company.                                                                                                                                  |
| `company`                                                                                                                                                                                                                    | [models.PartnerManagedCompanyCreateRequestCompany](../../models/partnermanagedcompanycreaterequestcompany.md)                                                                                                                | :heavy_check_mark:                                                                                                                                                                                                           | N/A                                                                                                                                                                                                                          |
| `x_gusto_api_version`                                                                                                                                                                                                        | [Optional[models.PostV1PartnerManagedCompaniesHeaderXGustoAPIVersion]](../../models/postv1partnermanagedcompaniesheaderxgustoapiversion.md)                                                                                  | :heavy_minus_sign:                                                                                                                                                                                                           | Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used. |
| `retries`                                                                                                                                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                           | Configuration to override the default retry behavior of the client.                                                                                                                                                          |

### Response

**[models.PartnerManagedCompany](../../models/partnermanagedcompany.md)**

### Errors

| Error Type                       | Status Code                      | Content Type                     |
| -------------------------------- | -------------------------------- | -------------------------------- |
| models.UnprocessableEntityError1 | 422                              | application/json                 |
| models.APIError                  | 4XX, 5XX                         | \*/\*                            |

## get

Get a company.

The employees:read scope is required to return home_address and non-work locations.
The company_admin:read scope is required to return primary_payroll_admin.
The signatories:read scope is required to return primary_signatory.

scope: `companies:read`

### Example Usage

<!-- UsageSnippet language="python" operationID="get-v1-companies" method="get" path="/v1/companies/{company_id}" -->
```python
import gusto_embedded_v_2025_11_15
from gusto_embedded_v_2025_11_15 import Gusto
import os


with Gusto(
    company_access_auth=os.getenv("GUSTO_COMPANY_ACCESS_AUTH", ""),
) as gusto:

    res = gusto.companies.get(company_id="<id>", x_gusto_api_version=gusto_embedded_v_2025_11_15.GetV1CompaniesHeaderXGustoAPIVersion.TWO_THOUSAND_AND_TWENTY_FIVE_MINUS_11_MINUS_15)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                    | Type                                                                                                                                                                                                                         | Required                                                                                                                                                                                                                     | Description                                                                                                                                                                                                                  |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `company_id`                                                                                                                                                                                                                 | *str*                                                                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                                           | The UUID of the company                                                                                                                                                                                                      |
| `x_gusto_api_version`                                                                                                                                                                                                        | [Optional[models.GetV1CompaniesHeaderXGustoAPIVersion]](../../models/getv1companiesheaderxgustoapiversion.md)                                                                                                                | :heavy_minus_sign:                                                                                                                                                                                                           | Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used. |
| `retries`                                                                                                                                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                           | Configuration to override the default retry behavior of the client.                                                                                                                                                          |

### Response

**[models.Company](../../models/company.md)**

### Errors

| Error Type                      | Status Code                     | Content Type                    |
| ------------------------------- | ------------------------------- | ------------------------------- |
| models.NotFoundErrorObjectError | 404                             | application/json                |
| models.APIError                 | 4XX, 5XX                        | \*/\*                           |

## update

Update a company.

scope: `companies:write`

### Example Usage

<!-- UsageSnippet language="python" operationID="put-v1-companies" method="put" path="/v1/companies/{company_id}" -->
```python
import gusto_embedded_v_2025_11_15
from gusto_embedded_v_2025_11_15 import Gusto
import os


with Gusto(
    company_access_auth=os.getenv("GUSTO_COMPANY_ACCESS_AUTH", ""),
) as gusto:

    res = gusto.companies.update(company_id="<id>", contractor_only=True, x_gusto_api_version=gusto_embedded_v_2025_11_15.PutV1CompaniesHeaderXGustoAPIVersion.TWO_THOUSAND_AND_TWENTY_FIVE_MINUS_11_MINUS_15)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                                                                                                    | Type                                                                                                                                                                                                                                                                                                         | Required                                                                                                                                                                                                                                                                                                     | Description                                                                                                                                                                                                                                                                                                  |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `company_id`                                                                                                                                                                                                                                                                                                 | *str*                                                                                                                                                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                                                                                                                           | The UUID of the company                                                                                                                                                                                                                                                                                      |
| `contractor_only`                                                                                                                                                                                                                                                                                            | *bool*                                                                                                                                                                                                                                                                                                       | :heavy_check_mark:                                                                                                                                                                                                                                                                                           | Whether the company only supports contractors. Must be updated in order for the company to start supporting W-2 employees. Can only be updated from true to false. Note that updating this value will require additional onboarding steps to be completed in order for the company to support W-2 employees. |
| `x_gusto_api_version`                                                                                                                                                                                                                                                                                        | [Optional[models.PutV1CompaniesHeaderXGustoAPIVersion]](../../models/putv1companiesheaderxgustoapiversion.md)                                                                                                                                                                                                | :heavy_minus_sign:                                                                                                                                                                                                                                                                                           | Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used.                                                                                 |
| `retries`                                                                                                                                                                                                                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                                                                                                           | Configuration to override the default retry behavior of the client.                                                                                                                                                                                                                                          |

### Response

**[models.Company](../../models/company.md)**

### Errors

| Error Type                       | Status Code                      | Content Type                     |
| -------------------------------- | -------------------------------- | -------------------------------- |
| models.NotFoundErrorObjectError  | 404                              | application/json                 |
| models.UnprocessableEntityError1 | 422                              | application/json                 |
| models.APIError                  | 4XX, 5XX                         | \*/\*                            |

## migrate

Migrate an existing Gusto customer to your embedded payroll product.

### Prerequisites
Before calling this endpoint:
1. The customer must connect their Gusto account to your application using [OAuth2](doc:oauth2)
2. The customer must view and [accept the Embedded Payroll Terms of Service](ref:post-partner-managed-companies-company_uuid-accept_terms_of_service)

### Related guides
- [Migrate an existing company](doc:migrate-existing-company)

scope: `partner_managed_companies:write`

### Example Usage

<!-- UsageSnippet language="python" operationID="put-v1-partner-managed-companies-company-uuid-migrate" method="put" path="/v1/partner_managed_companies/{company_uuid}/migrate" -->
```python
import gusto_embedded_v_2025_11_15
from gusto_embedded_v_2025_11_15 import Gusto
import os


with Gusto(
    company_access_auth=os.getenv("GUSTO_COMPANY_ACCESS_AUTH", ""),
) as gusto:

    res = gusto.companies.migrate(company_uuid="<id>", email="Janice18@gmail.com", x_gusto_api_version=gusto_embedded_v_2025_11_15.PutV1PartnerManagedCompaniesCompanyUUIDMigrateHeaderXGustoAPIVersion.TWO_THOUSAND_AND_TWENTY_FIVE_MINUS_11_MINUS_15)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                                      | Type                                                                                                                                                                                                                                           | Required                                                                                                                                                                                                                                       | Description                                                                                                                                                                                                                                    |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `company_uuid`                                                                                                                                                                                                                                 | *str*                                                                                                                                                                                                                                          | :heavy_check_mark:                                                                                                                                                                                                                             | The UUID of the company                                                                                                                                                                                                                        |
| `email`                                                                                                                                                                                                                                        | *str*                                                                                                                                                                                                                                          | :heavy_check_mark:                                                                                                                                                                                                                             | Email of the company signatory who is authorized to accept our [Terms of Service](https://flows.gusto.com/terms) and migration decision. You can retrieve the signatory email from the `GET /v/1/companies/{company_id}/signatories` endpoint. |
| `x_gusto_api_version`                                                                                                                                                                                                                          | [Optional[models.PutV1PartnerManagedCompaniesCompanyUUIDMigrateHeaderXGustoAPIVersion]](../../models/putv1partnermanagedcompaniescompanyuuidmigrateheaderxgustoapiversion.md)                                                                  | :heavy_minus_sign:                                                                                                                                                                                                                             | Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used.                   |
| `ip_address`                                                                                                                                                                                                                                   | *Optional[str]*                                                                                                                                                                                                                                | :heavy_minus_sign:                                                                                                                                                                                                                             | The IP address of the signatory who viewed and accepted the Terms of Service.                                                                                                                                                                  |
| `external_user_id`                                                                                                                                                                                                                             | *Optional[str]*                                                                                                                                                                                                                                | :heavy_minus_sign:                                                                                                                                                                                                                             | The signatory's user ID on your platform.                                                                                                                                                                                                      |
| `retries`                                                                                                                                                                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                               | :heavy_minus_sign:                                                                                                                                                                                                                             | Configuration to override the default retry behavior of the client.                                                                                                                                                                            |

### Response

**[models.PartnerManagedCompanyMigrateResponse](../../models/partnermanagedcompanymigrateresponse.md)**

### Errors

| Error Type                       | Status Code                      | Content Type                     |
| -------------------------------- | -------------------------------- | -------------------------------- |
| models.NotFoundErrorObjectError  | 404                              | application/json                 |
| models.UnprocessableEntityError1 | 422                              | application/json                 |
| models.APIError                  | 4XX, 5XX                         | \*/\*                            |

## get_v1_partner_managed_companies_company_uuid_migration_readiness

Check if an existing Gusto customer is ready to be migrated to embedded payroll. This endpoint returns blockers and warnings associated with migrating the company and is recommended to be called before attempting to migrate a company.

scope: `partner_managed_companies:read`

### Example Usage

<!-- UsageSnippet language="python" operationID="get-v1-partner-managed-companies-company-uuid-migration_readiness" method="get" path="/v1/partner_managed_companies/{company_uuid}/migration_readiness" -->
```python
import gusto_embedded_v_2025_11_15
from gusto_embedded_v_2025_11_15 import Gusto
import os


with Gusto(
    company_access_auth=os.getenv("GUSTO_COMPANY_ACCESS_AUTH", ""),
) as gusto:

    res = gusto.companies.get_v1_partner_managed_companies_company_uuid_migration_readiness(company_uuid="<id>", x_gusto_api_version=gusto_embedded_v_2025_11_15.GetV1PartnerManagedCompaniesCompanyUUIDMigrationReadinessHeaderXGustoAPIVersion.TWO_THOUSAND_AND_TWENTY_FIVE_MINUS_11_MINUS_15)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                    | Type                                                                                                                                                                                                                         | Required                                                                                                                                                                                                                     | Description                                                                                                                                                                                                                  |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `company_uuid`                                                                                                                                                                                                               | *str*                                                                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                                           | The UUID of the company                                                                                                                                                                                                      |
| `x_gusto_api_version`                                                                                                                                                                                                        | [Optional[models.GetV1PartnerManagedCompaniesCompanyUUIDMigrationReadinessHeaderXGustoAPIVersion]](../../models/getv1partnermanagedcompaniescompanyuuidmigrationreadinessheaderxgustoapiversion.md)                          | :heavy_minus_sign:                                                                                                                                                                                                           | Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used. |
| `retries`                                                                                                                                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                           | Configuration to override the default retry behavior of the client.                                                                                                                                                          |

### Response

**[models.PartnerManagedCompanyMigrationReadinessResponse](../../models/partnermanagedcompanymigrationreadinessresponse.md)**

### Errors

| Error Type                      | Status Code                     | Content Type                    |
| ------------------------------- | ------------------------------- | ------------------------------- |
| models.NotFoundErrorObjectError | 404                             | application/json                |
| models.APIError                 | 4XX, 5XX                        | \*/\*                           |

## accept_terms_of_service

Accept the Gusto Embedded Payroll's [Terms of Service](https://flows.gusto.com/terms).
The user must have a role in the company in order to accept the Terms of Service.

scope: `terms_of_services:write`

### Example Usage

<!-- UsageSnippet language="python" operationID="post-partner-managed-companies-company_uuid-accept_terms_of_service" method="post" path="/v1/partner_managed_companies/{company_uuid}/accept_terms_of_service" -->
```python
import gusto_embedded_v_2025_11_15
from gusto_embedded_v_2025_11_15 import Gusto
import os


with Gusto(
    company_access_auth=os.getenv("GUSTO_COMPANY_ACCESS_AUTH", ""),
) as gusto:

    res = gusto.companies.accept_terms_of_service(company_uuid="<id>", email="Tabitha59@hotmail.com", ip_address="dad9:5ede:cdbf:8dae:abe7:3cac:a2bf:2c26", external_user_id="<id>", x_gusto_api_version=gusto_embedded_v_2025_11_15.PostPartnerManagedCompaniesCompanyUUIDAcceptTermsOfServiceHeaderXGustoAPIVersion.TWO_THOUSAND_AND_TWENTY_FIVE_MINUS_11_MINUS_15)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                    | Type                                                                                                                                                                                                                         | Required                                                                                                                                                                                                                     | Description                                                                                                                                                                                                                  |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `company_uuid`                                                                                                                                                                                                               | *str*                                                                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                                           | The UUID of the company                                                                                                                                                                                                      |
| `email`                                                                                                                                                                                                                      | *str*                                                                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                                           | The user's email address on Gusto. You can retrieve the user's email via company's `/admins`, `/employees`, `/signatories`, and `/contractors` endpoints.                                                                    |
| `ip_address`                                                                                                                                                                                                                 | *str*                                                                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                                           | The IP address of the user who viewed and accepted the Terms of Service.                                                                                                                                                     |
| `external_user_id`                                                                                                                                                                                                           | *str*                                                                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                                           | The user ID on your platform.                                                                                                                                                                                                |
| `x_gusto_api_version`                                                                                                                                                                                                        | [Optional[models.PostPartnerManagedCompaniesCompanyUUIDAcceptTermsOfServiceHeaderXGustoAPIVersion]](../../models/postpartnermanagedcompaniescompanyuuidaccepttermsofserviceheaderxgustoapiversion.md)                        | :heavy_minus_sign:                                                                                                                                                                                                           | Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used. |
| `retries`                                                                                                                                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                           | Configuration to override the default retry behavior of the client.                                                                                                                                                          |

### Response

**[models.PartnerManagedCompanyTermsOfServiceResponse](../../models/partnermanagedcompanytermsofserviceresponse.md)**

### Errors

| Error Type                       | Status Code                      | Content Type                     |
| -------------------------------- | -------------------------------- | -------------------------------- |
| models.NotFoundErrorObjectError  | 404                              | application/json                 |
| models.UnprocessableEntityError1 | 422                              | application/json                 |
| models.APIError                  | 4XX, 5XX                         | \*/\*                            |

## retrieve_terms_of_service

Retrieve the user acceptance status of the Gusto Embedded Payroll's [Terms of Service](https://flows.gusto.com/terms).

scope: `terms_of_services:read`

### Example Usage

<!-- UsageSnippet language="python" operationID="post-partner-managed-companies-company_uuid-retrieve_terms_of_service" method="post" path="/v1/partner_managed_companies/{company_uuid}/retrieve_terms_of_service" -->
```python
import gusto_embedded_v_2025_11_15
from gusto_embedded_v_2025_11_15 import Gusto
import os


with Gusto(
    company_access_auth=os.getenv("GUSTO_COMPANY_ACCESS_AUTH", ""),
) as gusto:

    res = gusto.companies.retrieve_terms_of_service(company_uuid="<id>", email="Laverne_Raynor-Ziemann@yahoo.com", x_gusto_api_version=gusto_embedded_v_2025_11_15.PostPartnerManagedCompaniesCompanyUUIDRetrieveTermsOfServiceHeaderXGustoAPIVersion.TWO_THOUSAND_AND_TWENTY_FIVE_MINUS_11_MINUS_15)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                    | Type                                                                                                                                                                                                                         | Required                                                                                                                                                                                                                     | Description                                                                                                                                                                                                                  |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `company_uuid`                                                                                                                                                                                                               | *str*                                                                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                                           | The UUID of the company                                                                                                                                                                                                      |
| `email`                                                                                                                                                                                                                      | *str*                                                                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                                           | The user's email address on Gusto. You can retrieve the user's email via company's `/admins`, `/employees`, `/signatories`, and `/contractors` endpoints.                                                                    |
| `x_gusto_api_version`                                                                                                                                                                                                        | [Optional[models.PostPartnerManagedCompaniesCompanyUUIDRetrieveTermsOfServiceHeaderXGustoAPIVersion]](../../models/postpartnermanagedcompaniescompanyuuidretrievetermsofserviceheaderxgustoapiversion.md)                    | :heavy_minus_sign:                                                                                                                                                                                                           | Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used. |
| `retries`                                                                                                                                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                           | Configuration to override the default retry behavior of the client.                                                                                                                                                          |

### Response

**[models.PartnerManagedCompanyTermsOfServiceResponse](../../models/partnermanagedcompanytermsofserviceresponse.md)**

### Errors

| Error Type                       | Status Code                      | Content Type                     |
| -------------------------------- | -------------------------------- | -------------------------------- |
| models.NotFoundErrorObjectError  | 404                              | application/json                 |
| models.UnprocessableEntityError1 | 422                              | application/json                 |
| models.APIError                  | 4XX, 5XX                         | \*/\*                            |

## list_admins

Returns a list of all the admins at a company

scope: `company_admin:read`

### Example Usage

<!-- UsageSnippet language="python" operationID="get-v1-companies-company_id-admins" method="get" path="/v1/companies/{company_id}/admins" -->
```python
import gusto_embedded_v_2025_11_15
from gusto_embedded_v_2025_11_15 import Gusto
import os


with Gusto(
    company_access_auth=os.getenv("GUSTO_COMPANY_ACCESS_AUTH", ""),
) as gusto:

    res = gusto.companies.list_admins(company_id="<id>", x_gusto_api_version=gusto_embedded_v_2025_11_15.GetV1CompaniesCompanyIDAdminsHeaderXGustoAPIVersion.TWO_THOUSAND_AND_TWENTY_FIVE_MINUS_11_MINUS_15)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                    | Type                                                                                                                                                                                                                         | Required                                                                                                                                                                                                                     | Description                                                                                                                                                                                                                  |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `company_id`                                                                                                                                                                                                                 | *str*                                                                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                                           | The UUID of the company                                                                                                                                                                                                      |
| `x_gusto_api_version`                                                                                                                                                                                                        | [Optional[models.GetV1CompaniesCompanyIDAdminsHeaderXGustoAPIVersion]](../../models/getv1companiescompanyidadminsheaderxgustoapiversion.md)                                                                                  | :heavy_minus_sign:                                                                                                                                                                                                           | Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used. |
| `page`                                                                                                                                                                                                                       | *Optional[int]*                                                                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                           | The page that is requested. When unspecified, will load all objects unless endpoint forces pagination.                                                                                                                       |
| `per`                                                                                                                                                                                                                        | *Optional[int]*                                                                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                           | Number of objects per page. For majority of endpoints will default to 25                                                                                                                                                     |
| `retries`                                                                                                                                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                           | Configuration to override the default retry behavior of the client.                                                                                                                                                          |

### Response

**[List[models.Admin]](../../models/.md)**

### Errors

| Error Type                      | Status Code                     | Content Type                    |
| ------------------------------- | ------------------------------- | ------------------------------- |
| models.NotFoundErrorObjectError | 404                             | application/json                |
| models.APIError                 | 4XX, 5XX                        | \*/\*                           |

## create_admin

Creates a new admin for a company.
If the email matches an existing user, this will create an admin account for the current user. Otherwise, this will create a new user.

scope: `company_admin:write`

### Example Usage

<!-- UsageSnippet language="python" operationID="post-v1-companies-company_id-admins" method="post" path="/v1/companies/{company_id}/admins" -->
```python
import gusto_embedded_v_2025_11_15
from gusto_embedded_v_2025_11_15 import Gusto
import os


with Gusto(
    company_access_auth=os.getenv("GUSTO_COMPANY_ACCESS_AUTH", ""),
) as gusto:

    res = gusto.companies.create_admin(company_id="<id>", first_name="John", last_name="Smith", email="jsmith99@gmail.com", x_gusto_api_version=gusto_embedded_v_2025_11_15.PostV1CompaniesCompanyIDAdminsHeaderXGustoAPIVersion.TWO_THOUSAND_AND_TWENTY_FIVE_MINUS_11_MINUS_15)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                    | Type                                                                                                                                                                                                                         | Required                                                                                                                                                                                                                     | Description                                                                                                                                                                                                                  | Example                                                                                                                                                                                                                      |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `company_id`                                                                                                                                                                                                                 | *str*                                                                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                                           | The UUID of the company                                                                                                                                                                                                      |                                                                                                                                                                                                                              |
| `first_name`                                                                                                                                                                                                                 | *str*                                                                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                                           | The first name of the admin.                                                                                                                                                                                                 | John                                                                                                                                                                                                                         |
| `last_name`                                                                                                                                                                                                                  | *str*                                                                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                                           | The last name of the admin.                                                                                                                                                                                                  | Smith                                                                                                                                                                                                                        |
| `email`                                                                                                                                                                                                                      | *str*                                                                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                                           | The email of the admin for Gusto's system. If the email matches an existing user, this will create an admin account for them.                                                                                                | jsmith99@gmail.com                                                                                                                                                                                                           |
| `x_gusto_api_version`                                                                                                                                                                                                        | [Optional[models.PostV1CompaniesCompanyIDAdminsHeaderXGustoAPIVersion]](../../models/postv1companiescompanyidadminsheaderxgustoapiversion.md)                                                                                | :heavy_minus_sign:                                                                                                                                                                                                           | Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used. |                                                                                                                                                                                                                              |
| `retries`                                                                                                                                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                           | Configuration to override the default retry behavior of the client.                                                                                                                                                          |                                                                                                                                                                                                                              |

### Response

**[models.Admin](../../models/admin.md)**

### Errors

| Error Type                       | Status Code                      | Content Type                     |
| -------------------------------- | -------------------------------- | -------------------------------- |
| models.NotFoundErrorObjectError  | 404                              | application/json                 |
| models.UnprocessableEntityError1 | 422                              | application/json                 |
| models.APIError                  | 4XX, 5XX                         | \*/\*                            |

## get_onboarding_status

Retrieves a company's onboarding status, including whether onboarding is complete and the list of
required onboarding steps with their respective completion state.

scope: `company_onboarding_status:read`

### Example Usage

<!-- UsageSnippet language="python" operationID="get-v1-company-onboarding-status" method="get" path="/v1/companies/{company_uuid}/onboarding_status" -->
```python
import gusto_embedded_v_2025_11_15
from gusto_embedded_v_2025_11_15 import Gusto
import os


with Gusto(
    company_access_auth=os.getenv("GUSTO_COMPANY_ACCESS_AUTH", ""),
) as gusto:

    res = gusto.companies.get_onboarding_status(company_uuid="7b1d0df1-6403-4a06-8768-c1dd7d24d27a", additional_steps="external_payroll", x_gusto_api_version=gusto_embedded_v_2025_11_15.GetV1CompanyOnboardingStatusHeaderXGustoAPIVersion.TWO_THOUSAND_AND_TWENTY_FIVE_MINUS_11_MINUS_15)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                    | Type                                                                                                                                                                                                                         | Required                                                                                                                                                                                                                     | Description                                                                                                                                                                                                                  | Example                                                                                                                                                                                                                      |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `company_uuid`                                                                                                                                                                                                               | *str*                                                                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                                           | The UUID of the company                                                                                                                                                                                                      | 7b1d0df1-6403-4a06-8768-c1dd7d24d27a                                                                                                                                                                                         |
| `additional_steps`                                                                                                                                                                                                           | *Optional[str]*                                                                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                           | Comma-delimited string of additional onboarding steps to include. Currently only supports the value "external_payroll".                                                                                                      | external_payroll                                                                                                                                                                                                             |
| `x_gusto_api_version`                                                                                                                                                                                                        | [Optional[models.GetV1CompanyOnboardingStatusHeaderXGustoAPIVersion]](../../models/getv1companyonboardingstatusheaderxgustoapiversion.md)                                                                                    | :heavy_minus_sign:                                                                                                                                                                                                           | Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used. |                                                                                                                                                                                                                              |
| `retries`                                                                                                                                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                           | Configuration to override the default retry behavior of the client.                                                                                                                                                          |                                                                                                                                                                                                                              |

### Response

**[models.CompanyOnboardingStatus](../../models/companyonboardingstatus.md)**

### Errors

| Error Type                      | Status Code                     | Content Type                    |
| ------------------------------- | ------------------------------- | ------------------------------- |
| models.NotFoundErrorObjectError | 404                             | application/json                |
| models.APIError                 | 4XX, 5XX                        | \*/\*                           |

## finish_onboarding

Finalize a company's onboarding process.

### Approve a company in demo

After a company is finished onboarding, Gusto requires an additional step to review and approve that company.
The company onboarding status is "onboarding_completed": false, until the API call is made to finish company
onboarding. In production environments, this step is required for risk-analysis purposes.

We provide the endpoint `PUT '/v1/companies/{company_uuid}/approve'` to facilitate company approvals in the demo environment.

```shell
PUT '/v1/companies/89771af8-b964-472e-8064-554dfbcb56d9/approve'

# Response: Company object, with company_status: 'Approved'
```

scope: `companies:write`

### Example Usage

<!-- UsageSnippet language="python" operationID="get-v1-company-finish-onboarding" method="put" path="/v1/companies/{company_uuid}/finish_onboarding" -->
```python
import gusto_embedded_v_2025_11_15
from gusto_embedded_v_2025_11_15 import Gusto
import os


with Gusto(
    company_access_auth=os.getenv("GUSTO_COMPANY_ACCESS_AUTH", ""),
) as gusto:

    res = gusto.companies.finish_onboarding(company_uuid="7b1d0df1-6403-4a06-8768-c1dd7d24d27a", x_gusto_api_version=gusto_embedded_v_2025_11_15.GetV1CompanyFinishOnboardingHeaderXGustoAPIVersion.TWO_THOUSAND_AND_TWENTY_FIVE_MINUS_11_MINUS_15)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                    | Type                                                                                                                                                                                                                         | Required                                                                                                                                                                                                                     | Description                                                                                                                                                                                                                  | Example                                                                                                                                                                                                                      |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `company_uuid`                                                                                                                                                                                                               | *str*                                                                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                                           | The UUID of the company                                                                                                                                                                                                      | 7b1d0df1-6403-4a06-8768-c1dd7d24d27a                                                                                                                                                                                         |
| `x_gusto_api_version`                                                                                                                                                                                                        | [Optional[models.GetV1CompanyFinishOnboardingHeaderXGustoAPIVersion]](../../models/getv1companyfinishonboardingheaderxgustoapiversion.md)                                                                                    | :heavy_minus_sign:                                                                                                                                                                                                           | Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used. |                                                                                                                                                                                                                              |
| `retries`                                                                                                                                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                           | Configuration to override the default retry behavior of the client.                                                                                                                                                          |                                                                                                                                                                                                                              |

### Response

**[models.CompanyOnboardingStatus](../../models/companyonboardingstatus.md)**

### Errors

| Error Type                       | Status Code                      | Content Type                     |
| -------------------------------- | -------------------------------- | -------------------------------- |
| models.NotFoundErrorObjectError  | 404                              | application/json                 |
| models.UnprocessableEntityError1 | 422                              | application/json                 |
| models.APIError                  | 4XX, 5XX                         | \*/\*                            |

## get_custom_fields

Returns a list of the custom fields of the company. Useful when you need to know the schema of custom fields for an entire company.

scope: `companies:read`

### Example Usage

<!-- UsageSnippet language="python" operationID="get-v1-companies-company_id-custom_fields" method="get" path="/v1/companies/{company_id}/custom_fields" -->
```python
import gusto_embedded_v_2025_11_15
from gusto_embedded_v_2025_11_15 import Gusto
import os


with Gusto(
    company_access_auth=os.getenv("GUSTO_COMPANY_ACCESS_AUTH", ""),
) as gusto:

    res = gusto.companies.get_custom_fields(company_id="<id>", x_gusto_api_version=gusto_embedded_v_2025_11_15.GetV1CompaniesCompanyIDCustomFieldsHeaderXGustoAPIVersion.TWO_THOUSAND_AND_TWENTY_FIVE_MINUS_11_MINUS_15)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                    | Type                                                                                                                                                                                                                         | Required                                                                                                                                                                                                                     | Description                                                                                                                                                                                                                  |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `company_id`                                                                                                                                                                                                                 | *str*                                                                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                                           | The UUID of the company                                                                                                                                                                                                      |
| `x_gusto_api_version`                                                                                                                                                                                                        | [Optional[models.GetV1CompaniesCompanyIDCustomFieldsHeaderXGustoAPIVersion]](../../models/getv1companiescompanyidcustomfieldsheaderxgustoapiversion.md)                                                                      | :heavy_minus_sign:                                                                                                                                                                                                           | Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used. |
| `page`                                                                                                                                                                                                                       | *Optional[int]*                                                                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                           | The page that is requested. When unspecified, will load all objects unless endpoint forces pagination.                                                                                                                       |
| `per`                                                                                                                                                                                                                        | *Optional[int]*                                                                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                           | Number of objects per page. For majority of endpoints will default to 25                                                                                                                                                     |
| `retries`                                                                                                                                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                           | Configuration to override the default retry behavior of the client.                                                                                                                                                          |

### Response

**[models.CompanyCustomFieldList](../../models/companycustomfieldlist.md)**

### Errors

| Error Type                      | Status Code                     | Content Type                    |
| ------------------------------- | ------------------------------- | ------------------------------- |
| models.NotFoundErrorObjectError | 404                             | application/json                |
| models.APIError                 | 4XX, 5XX                        | \*/\*                           |