# CompanyBenefits

## Overview

### Available Operations

* [list](#list) - Get benefits for a company
* [create](#create) - Create a company benefit
* [get_by_id](#get_by_id) - Get a company benefit
* [update](#update) - Update a company benefit
* [delete](#delete) - Delete a company benefit
* [list_supported](#list_supported) - Get all supported benefits
* [get](#get) - Get a supported benefit
* [get_summary](#get_summary) - Get company benefit summary by company benefit id.
* [get_employee_benefits](#get_employee_benefits) - Get all employee benefits for a company benefit
* [bulk_update_employee_benefits](#bulk_update_employee_benefits) - Bulk update employee benefits for a company benefit
* [get_requirements](#get_requirements) - Get benefit fields requirements by benefit type
* [get_v1_company_benefits_company_benefit_id_contribution_exclusions](#get_v1_company_benefits_company_benefit_id_contribution_exclusions) - Get contribution exclusions for a company benefit
* [put_v1_company_benefits_company_benefit_id_contribution_exclusions](#put_v1_company_benefits_company_benefit_id_contribution_exclusions) - Update contribution exclusions for a company benefit

## list

Company benefits represent the benefits that a company is offering to employees. This ties together a particular supported benefit with the company-specific information for the offering of that benefit.

Note that company benefits can be deactivated only when no employees are enrolled.

Benefits containing PHI are only visible to applications with the `company_benefits:read:phi` scope.

scope: `company_benefits:read`

### Example Usage

<!-- UsageSnippet language="python" operationID="get-v1-companies-company_id-company_benefits" method="get" path="/v1/companies/{company_id}/company_benefits" -->
```python
import gusto_app_integration
from gusto_app_integration import GustoAppIntegration


with GustoAppIntegration(
    company_access_auth="<YOUR_BEARER_TOKEN_HERE>",
) as gai_client:

    res = gai_client.company_benefits.list(company_id="<id>", x_gusto_api_version=gusto_app_integration.GetV1CompaniesCompanyIDCompanyBenefitsHeaderXGustoAPIVersion.TWO_THOUSAND_AND_TWENTY_FIVE_MINUS_06_MINUS_15)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                    | Type                                                                                                                                                                                                                         | Required                                                                                                                                                                                                                     | Description                                                                                                                                                                                                                  |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `company_id`                                                                                                                                                                                                                 | *str*                                                                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                                           | The UUID of the company                                                                                                                                                                                                      |
| `x_gusto_api_version`                                                                                                                                                                                                        | [Optional[models.GetV1CompaniesCompanyIDCompanyBenefitsHeaderXGustoAPIVersion]](../../models/getv1companiescompanyidcompanybenefitsheaderxgustoapiversion.md)                                                                | :heavy_minus_sign:                                                                                                                                                                                                           | Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used. |
| `active`                                                                                                                                                                                                                     | *Optional[bool]*                                                                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                           | Whether the benefit is currently active                                                                                                                                                                                      |
| `enrollment_count`                                                                                                                                                                                                           | *Optional[bool]*                                                                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                           | Whether to return employee enrollment count                                                                                                                                                                                  |
| `benefit_type`                                                                                                                                                                                                               | *Optional[str]*                                                                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                           | Filter by benefit type. Comma-separated list of benefit type IDs, i.e. `?benefit_type=5,105`                                                                                                                                 |
| `retries`                                                                                                                                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                           | Configuration to override the default retry behavior of the client.                                                                                                                                                          |

### Response

**[List[models.CompanyBenefit]](../../models/.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.NotFoundErrorObject | 404                        | application/json           |
| models.APIError            | 4XX, 5XX                   | \*/\*                      |

## create

Company benefits represent the benefits that a company is offering to employees. This ties together a particular supported benefit with the company-specific information for the offering of that benefit.

Note that company benefits can be deactivated only when no employees are enrolled.

When the application has the `company_benefits:write:benefit_type_limited` data scope, the application can only create company benefits for benefit types that are permitted for the application.

scope: `company_benefits:write`

### Example Usage

<!-- UsageSnippet language="python" operationID="post-v1-companies-company_id-company_benefits" method="post" path="/v1/companies/{company_id}/company_benefits" -->
```python
import gusto_app_integration
from gusto_app_integration import GustoAppIntegration


with GustoAppIntegration(
    company_access_auth="<YOUR_BEARER_TOKEN_HERE>",
) as gai_client:

    res = gai_client.company_benefits.create(company_id="<id>", description="hm pfft surge beyond", x_gusto_api_version=gusto_app_integration.PostV1CompaniesCompanyIDCompanyBenefitsHeaderXGustoAPIVersion.TWO_THOUSAND_AND_TWENTY_FIVE_MINUS_06_MINUS_15, active=True)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                                    | Type                                                                                                                                                                                                                                         | Required                                                                                                                                                                                                                                     | Description                                                                                                                                                                                                                                  |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `company_id`                                                                                                                                                                                                                                 | *str*                                                                                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                                                           | The UUID of the company                                                                                                                                                                                                                      |
| `description`                                                                                                                                                                                                                                | *str*                                                                                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                                                           | The description of the company benefit.For example, a company may offer multiple benefits with an ID of 1 (for Medical Insurance). The description would show something more specific like "Kaiser Permanente" or "Blue Cross/ Blue Shield". |
| `x_gusto_api_version`                                                                                                                                                                                                                        | [Optional[models.PostV1CompaniesCompanyIDCompanyBenefitsHeaderXGustoAPIVersion]](../../models/postv1companiescompanyidcompanybenefitsheaderxgustoapiversion.md)                                                                              | :heavy_minus_sign:                                                                                                                                                                                                                           | Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used.                 |
| `benefit_type`                                                                                                                                                                                                                               | *Optional[int]*                                                                                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                                           | The ID of the benefit to which the company benefit belongs.                                                                                                                                                                                  |
| `active`                                                                                                                                                                                                                                     | *Optional[bool]*                                                                                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                                           | Whether this benefit is active for employee participation.                                                                                                                                                                                   |
| `responsible_for_employer_taxes`                                                                                                                                                                                                             | *Optional[bool]*                                                                                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                                           | Whether the employer is subject to pay employer taxes when an employee is on leave. Only applicable to third party sick pay benefits.                                                                                                        |
| `responsible_for_employee_w2`                                                                                                                                                                                                                | *Optional[bool]*                                                                                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                                           | Whether the employer is subject to file W-2 forms for an employee on leave. Only applicable to third party sick pay benefits.                                                                                                                |
| `catch_up_type`                                                                                                                                                                                                                              | [OptionalNullable[models.CompanyBenefitCreateRequestCatchUpType]](../../models/companybenefitcreaterequestcatchuptype.md)                                                                                                                    | :heavy_minus_sign:                                                                                                                                                                                                                           | The type of catch-up contribution for this benefit, as required by Section 603 of the SECURE 2.0 Act. Only applicable to pre-tax 401(k) and 403(b) benefits.                                                                                 |
| `retries`                                                                                                                                                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                                           | Configuration to override the default retry behavior of the client.                                                                                                                                                                          |

### Response

**[models.CompanyBenefit](../../models/companybenefit.md)**

### Errors

| Error Type                            | Status Code                           | Content Type                          |
| ------------------------------------- | ------------------------------------- | ------------------------------------- |
| models.NotFoundErrorObject            | 404                                   | application/json                      |
| models.UnprocessableEntityErrorObject | 422                                   | application/json                      |
| models.APIError                       | 4XX, 5XX                              | \*/\*                                 |

## get_by_id

Company benefits represent the benefits that a company is offering to employees. This ties together a particular supported benefit with the company-specific information for the offering of that benefit.

Note that company benefits can be deactivated only when no employees are enrolled.

When with_employee_benefits parameter with true value is passed, employee_benefits:read scope is required to return employee_benefits.

scope: `company_benefits:read`

### Example Usage

<!-- UsageSnippet language="python" operationID="get-v1-company_benefits-company_benefit_id" method="get" path="/v1/company_benefits/{company_benefit_id}" -->
```python
import gusto_app_integration
from gusto_app_integration import GustoAppIntegration


with GustoAppIntegration(
    company_access_auth="<YOUR_BEARER_TOKEN_HERE>",
) as gai_client:

    res = gai_client.company_benefits.get_by_id(company_benefit_id="<id>", x_gusto_api_version=gusto_app_integration.GetV1CompanyBenefitsCompanyBenefitIDHeaderXGustoAPIVersion.TWO_THOUSAND_AND_TWENTY_FIVE_MINUS_06_MINUS_15)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                    | Type                                                                                                                                                                                                                         | Required                                                                                                                                                                                                                     | Description                                                                                                                                                                                                                  |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `company_benefit_id`                                                                                                                                                                                                         | *str*                                                                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                                           | The UUID of the company benefit                                                                                                                                                                                              |
| `x_gusto_api_version`                                                                                                                                                                                                        | [Optional[models.GetV1CompanyBenefitsCompanyBenefitIDHeaderXGustoAPIVersion]](../../models/getv1companybenefitscompanybenefitidheaderxgustoapiversion.md)                                                                    | :heavy_minus_sign:                                                                                                                                                                                                           | Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used. |
| `with_employee_benefits`                                                                                                                                                                                                     | *Optional[bool]*                                                                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                           | Whether to return employee benefits associated with the benefit                                                                                                                                                              |
| `include`                                                                                                                                                                                                                    | [Optional[models.GetV1CompanyBenefitsCompanyBenefitIDQueryParamInclude]](../../models/getv1companybenefitscompanybenefitidqueryparaminclude.md)                                                                              | :heavy_minus_sign:                                                                                                                                                                                                           | Available options:<br/>- all_benefits: If with_employee_benefits=true, include all effective dated benefits for each employee instead of only the current benefits.                                                          |
| `retries`                                                                                                                                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                           | Configuration to override the default retry behavior of the client.                                                                                                                                                          |

### Response

**[models.CompanyBenefitWithEmployeeBenefits](../../models/companybenefitwithemployeebenefits.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.NotFoundErrorObject | 404                        | application/json           |
| models.APIError            | 4XX, 5XX                   | \*/\*                      |

## update

Company benefits represent the benefits that a company is offering to employees. This ties together a particular supported benefit with the company-specific information for the offering of that benefit.

Note that company benefits can be deactivated only when no employees are enrolled.

When the application has the `company_benefits:write:benefit_type_limited` data scope, the application can only update company benefits for benefit types that are permitted for the application.

scope: `company_benefits:write`

### Example Usage

<!-- UsageSnippet language="python" operationID="put-v1-company_benefits-company_benefit_id" method="put" path="/v1/company_benefits/{company_benefit_id}" -->
```python
import gusto_app_integration
from gusto_app_integration import GustoAppIntegration


with GustoAppIntegration(
    company_access_auth="<YOUR_BEARER_TOKEN_HERE>",
) as gai_client:

    res = gai_client.company_benefits.update(company_benefit_id="<id>", version="<value>", x_gusto_api_version=gusto_app_integration.PutV1CompanyBenefitsCompanyBenefitIDHeaderXGustoAPIVersion.TWO_THOUSAND_AND_TWENTY_FIVE_MINUS_06_MINUS_15)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                                    | Type                                                                                                                                                                                                                                         | Required                                                                                                                                                                                                                                     | Description                                                                                                                                                                                                                                  |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `company_benefit_id`                                                                                                                                                                                                                         | *str*                                                                                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                                                           | The UUID of the company benefit                                                                                                                                                                                                              |
| `version`                                                                                                                                                                                                                                    | *str*                                                                                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                                                           | The current version of the object. See the [versioning guide](https://docs.gusto.com/embedded-payroll/docs/versioning#object-layer) for information on how to use this field.                                                                |
| `x_gusto_api_version`                                                                                                                                                                                                                        | [Optional[models.PutV1CompanyBenefitsCompanyBenefitIDHeaderXGustoAPIVersion]](../../models/putv1companybenefitscompanybenefitidheaderxgustoapiversion.md)                                                                                    | :heavy_minus_sign:                                                                                                                                                                                                                           | Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used.                 |
| `active`                                                                                                                                                                                                                                     | *Optional[bool]*                                                                                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                                           | Whether this benefit is active for employee participation. Company benefits may only be deactivated if no employees are actively participating.                                                                                              |
| `description`                                                                                                                                                                                                                                | *Optional[str]*                                                                                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                                           | The description of the company benefit.For example, a company may offer multiple benefits with an ID of 1 (for Medical Insurance). The description would show something more specific like "Kaiser Permanente" or "Blue Cross/ Blue Shield". |
| `responsible_for_employer_taxes`                                                                                                                                                                                                             | *Optional[bool]*                                                                                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                                           | Whether the employer is subject to pay employer taxes when an employee is on leave. Only applicable to short-term and long-term disability benefits (different from voluntary disability).                                                   |
| `responsible_for_employee_w2`                                                                                                                                                                                                                | *Optional[bool]*                                                                                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                                           | Whether the employer is subject to file W-2 forms for an employee on leave. Only applicable to short-term and long-term disability benefits (different from voluntary disability).                                                           |
| `catch_up_type`                                                                                                                                                                                                                              | [OptionalNullable[models.CompanyBenefitUpdateRequestCatchUpType]](../../models/companybenefitupdaterequestcatchuptype.md)                                                                                                                    | :heavy_minus_sign:                                                                                                                                                                                                                           | The type of catch-up contribution for this benefit, as required by Section 603 of the SECURE 2.0 Act. Only applicable to pre-tax 401(k) and 403(b) benefits.                                                                                 |
| `retries`                                                                                                                                                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                                           | Configuration to override the default retry behavior of the client.                                                                                                                                                                          |

### Response

**[models.CompanyBenefit](../../models/companybenefit.md)**

### Errors

| Error Type                            | Status Code                           | Content Type                          |
| ------------------------------------- | ------------------------------------- | ------------------------------------- |
| models.NotFoundErrorObject            | 404                                   | application/json                      |
| models.UnprocessableEntityErrorObject | 422                                   | application/json                      |
| models.APIError                       | 4XX, 5XX                              | \*/\*                                 |

## delete

The following must be true in order to delete a company benefit

  - There are no employee benefits associated with the company benefit
  - There are no payroll items associated with the company benefit
  - The benefit is not managed by a Partner or by Gusto (type must be 'External')

When the application has the `company_benefits:write:benefit_type_limited` data scope, the application can only delete company benefits for benefit types that are permitted for the application.

scope: `company_benefits:write`

### Example Usage

<!-- UsageSnippet language="python" operationID="delete-v1-company_benefits-company_benefit_id" method="delete" path="/v1/company_benefits/{company_benefit_id}" -->
```python
import gusto_app_integration
from gusto_app_integration import GustoAppIntegration


with GustoAppIntegration(
    company_access_auth="<YOUR_BEARER_TOKEN_HERE>",
) as gai_client:

    gai_client.company_benefits.delete(company_benefit_id="<id>", x_gusto_api_version=gusto_app_integration.DeleteV1CompanyBenefitsCompanyBenefitIDHeaderXGustoAPIVersion.TWO_THOUSAND_AND_TWENTY_FIVE_MINUS_06_MINUS_15)

    # Use the SDK ...

```

### Parameters

| Parameter                                                                                                                                                                                                                    | Type                                                                                                                                                                                                                         | Required                                                                                                                                                                                                                     | Description                                                                                                                                                                                                                  |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `company_benefit_id`                                                                                                                                                                                                         | *str*                                                                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                                           | The UUID of the company benefit                                                                                                                                                                                              |
| `x_gusto_api_version`                                                                                                                                                                                                        | [Optional[models.DeleteV1CompanyBenefitsCompanyBenefitIDHeaderXGustoAPIVersion]](../../models/deletev1companybenefitscompanybenefitidheaderxgustoapiversion.md)                                                              | :heavy_minus_sign:                                                                                                                                                                                                           | Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used. |
| `retries`                                                                                                                                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                           | Configuration to override the default retry behavior of the client.                                                                                                                                                          |

### Errors

| Error Type                            | Status Code                           | Content Type                          |
| ------------------------------------- | ------------------------------------- | ------------------------------------- |
| models.NotFoundErrorObject            | 404                                   | application/json                      |
| models.UnprocessableEntityErrorObject | 422                                   | application/json                      |
| models.APIError                       | 4XX, 5XX                              | \*/\*                                 |

## list_supported

Returns all benefits supported by Gusto. The benefit object in Gusto contains high level information about a particular benefit type and its tax considerations. When companies choose to offer a benefit, they are creating a Company Benefit object associated with a particular benefit.

scope: `benefits:read`

### Example Usage

<!-- UsageSnippet language="python" operationID="get-v1-benefits" method="get" path="/v1/benefits" -->
```python
import gusto_app_integration
from gusto_app_integration import GustoAppIntegration


with GustoAppIntegration(
    company_access_auth="<YOUR_BEARER_TOKEN_HERE>",
) as gai_client:

    res = gai_client.company_benefits.list_supported(x_gusto_api_version=gusto_app_integration.GetV1BenefitsHeaderXGustoAPIVersion.TWO_THOUSAND_AND_TWENTY_FIVE_MINUS_06_MINUS_15)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                    | Type                                                                                                                                                                                                                         | Required                                                                                                                                                                                                                     | Description                                                                                                                                                                                                                  |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `x_gusto_api_version`                                                                                                                                                                                                        | [Optional[models.GetV1BenefitsHeaderXGustoAPIVersion]](../../models/getv1benefitsheaderxgustoapiversion.md)                                                                                                                  | :heavy_minus_sign:                                                                                                                                                                                                           | Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used. |
| `retries`                                                                                                                                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                           | Configuration to override the default retry behavior of the client.                                                                                                                                                          |

### Response

**[List[models.SupportedBenefit]](../../models/.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## get

Returns a benefit supported by Gusto. The benefit object in Gusto contains high level information about a particular benefit type and its tax considerations. When companies choose to offer a benefit, they are creating a Company Benefit object associated with a particular benefit.

scope: `benefits:read`

### Example Usage

<!-- UsageSnippet language="python" operationID="get-v1-benefits-benefit_id" method="get" path="/v1/benefits/{benefit_id}" -->
```python
import gusto_app_integration
from gusto_app_integration import GustoAppIntegration


with GustoAppIntegration(
    company_access_auth="<YOUR_BEARER_TOKEN_HERE>",
) as gai_client:

    res = gai_client.company_benefits.get(benefit_id="<id>", x_gusto_api_version=gusto_app_integration.GetV1BenefitsBenefitIDHeaderXGustoAPIVersion.TWO_THOUSAND_AND_TWENTY_FIVE_MINUS_06_MINUS_15)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                    | Type                                                                                                                                                                                                                         | Required                                                                                                                                                                                                                     | Description                                                                                                                                                                                                                  |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `benefit_id`                                                                                                                                                                                                                 | *str*                                                                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                                           | The benefit type in Gusto.                                                                                                                                                                                                   |
| `x_gusto_api_version`                                                                                                                                                                                                        | [Optional[models.GetV1BenefitsBenefitIDHeaderXGustoAPIVersion]](../../models/getv1benefitsbenefitidheaderxgustoapiversion.md)                                                                                                | :heavy_minus_sign:                                                                                                                                                                                                           | Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used. |
| `retries`                                                                                                                                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                           | Configuration to override the default retry behavior of the client.                                                                                                                                                          |

### Response

**[models.SupportedBenefit](../../models/supportedbenefit.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## get_summary

Returns summary benefit data for the requested company benefit id.

Benefits containing PHI are only visible to applications with the `company_benefits:read:phi` scope.

scope: `company_benefits:read`

### Example Usage

<!-- UsageSnippet language="python" operationID="get-v1-benefits-company_benefit_id-summary" method="get" path="/v1/company_benefits/{company_benefit_id}/summary" -->
```python
import gusto_app_integration
from gusto_app_integration import GustoAppIntegration


with GustoAppIntegration(
    company_access_auth="<YOUR_BEARER_TOKEN_HERE>",
) as gai_client:

    res = gai_client.company_benefits.get_summary(company_benefit_id="<id>", x_gusto_api_version=gusto_app_integration.GetV1BenefitsCompanyBenefitIDSummaryHeaderXGustoAPIVersion.TWO_THOUSAND_AND_TWENTY_FIVE_MINUS_06_MINUS_15, start_date="2022-01-01", end_date="2022-12-31")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                    | Type                                                                                                                                                                                                                         | Required                                                                                                                                                                                                                     | Description                                                                                                                                                                                                                  | Example                                                                                                                                                                                                                      |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `company_benefit_id`                                                                                                                                                                                                         | *str*                                                                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                                           | The UUID of the company benefit                                                                                                                                                                                              |                                                                                                                                                                                                                              |
| `x_gusto_api_version`                                                                                                                                                                                                        | [Optional[models.GetV1BenefitsCompanyBenefitIDSummaryHeaderXGustoAPIVersion]](../../models/getv1benefitscompanybenefitidsummaryheaderxgustoapiversion.md)                                                                    | :heavy_minus_sign:                                                                                                                                                                                                           | Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used. |                                                                                                                                                                                                                              |
| `start_date`                                                                                                                                                                                                                 | *Optional[str]*                                                                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                           | The start date for which to retrieve company benefit summary                                                                                                                                                                 | 2022-01-01                                                                                                                                                                                                                   |
| `end_date`                                                                                                                                                                                                                   | *Optional[str]*                                                                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                           | The end date for which to retrieve company benefit summary. If left empty, defaults to today's date.                                                                                                                         | 2022-12-31                                                                                                                                                                                                                   |
| `detailed`                                                                                                                                                                                                                   | *Optional[bool]*                                                                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                           | Display employee payroll item summary                                                                                                                                                                                        |                                                                                                                                                                                                                              |
| `retries`                                                                                                                                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                           | Configuration to override the default retry behavior of the client.                                                                                                                                                          |                                                                                                                                                                                                                              |

### Response

**[models.BenefitSummary](../../models/benefitsummary.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.NotFoundErrorObject | 404                        | application/json           |
| models.APIError            | 4XX, 5XX                   | \*/\*                      |

## get_employee_benefits

Employee benefits represent an employee enrolled in a particular company benefit. It includes information specific to that employee's enrollment.

Returns an array of all employee benefits enrolled for this company benefit.

Benefits containing PHI are only visible to applications with the `employee_benefits:read:phi` scope.

scope: `employee_benefits:read`

### Example Usage

<!-- UsageSnippet language="python" operationID="get-v1-company_benefits-company_benefit_id-employee_benefits" method="get" path="/v1/company_benefits/{company_benefit_id}/employee_benefits" -->
```python
import gusto_app_integration
from gusto_app_integration import GustoAppIntegration


with GustoAppIntegration(
    company_access_auth="<YOUR_BEARER_TOKEN_HERE>",
) as gai_client:

    res = gai_client.company_benefits.get_employee_benefits(company_benefit_id="<id>", x_gusto_api_version=gusto_app_integration.GetV1CompanyBenefitsCompanyBenefitIDEmployeeBenefitsHeaderXGustoAPIVersion.TWO_THOUSAND_AND_TWENTY_FIVE_MINUS_06_MINUS_15)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                    | Type                                                                                                                                                                                                                         | Required                                                                                                                                                                                                                     | Description                                                                                                                                                                                                                  |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `company_benefit_id`                                                                                                                                                                                                         | *str*                                                                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                                           | The UUID of the company benefit                                                                                                                                                                                              |
| `x_gusto_api_version`                                                                                                                                                                                                        | [Optional[models.GetV1CompanyBenefitsCompanyBenefitIDEmployeeBenefitsHeaderXGustoAPIVersion]](../../models/getv1companybenefitscompanybenefitidemployeebenefitsheaderxgustoapiversion.md)                                    | :heavy_minus_sign:                                                                                                                                                                                                           | Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used. |
| `page`                                                                                                                                                                                                                       | *Optional[int]*                                                                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                           | The page that is requested. When unspecified, will load all objects unless endpoint forces pagination.                                                                                                                       |
| `per`                                                                                                                                                                                                                        | *Optional[int]*                                                                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                           | Number of objects per page. For majority of endpoints will default to 25                                                                                                                                                     |
| `include`                                                                                                                                                                                                                    | [Optional[models.GetV1CompanyBenefitsCompanyBenefitIDEmployeeBenefitsQueryParamInclude]](../../models/getv1companybenefitscompanybenefitidemployeebenefitsqueryparaminclude.md)                                              | :heavy_minus_sign:                                                                                                                                                                                                           | Available options:<br/>- all_benefits: Include all effective dated benefits for each employee instead of only the current benefits.                                                                                          |
| `retries`                                                                                                                                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                           | Configuration to override the default retry behavior of the client.                                                                                                                                                          |

### Response

**[List[models.EmployeeBenefit]](../../models/.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.NotFoundErrorObject | 404                        | application/json           |
| models.APIError            | 4XX, 5XX                   | \*/\*                      |

## bulk_update_employee_benefits

Employee benefits represent an employee enrolled in a particular company benefit. It includes information specific to that employee's enrollment.

Create or update(if the employee is already enrolled in the company benefit previously) an employee benefit for the company benefit.

Benefits containing PHI are only visible to applications with the `employee_benefits:read:phi` scope.

When the application has the `employee_benefits:write:benefit_type_limited` data scope, the application can only create or update employee benefits for benefit types that are permitted for the application.

scope: `employee_benefits:write`

### Example Usage

<!-- UsageSnippet language="python" operationID="put-v1-company_benefits-company_benefit_id-employee_benefits" method="put" path="/v1/company_benefits/{company_benefit_id}/employee_benefits" -->
```python
import gusto_app_integration
from gusto_app_integration import GustoAppIntegration


with GustoAppIntegration(
    company_access_auth="<YOUR_BEARER_TOKEN_HERE>",
) as gai_client:

    res = gai_client.company_benefits.bulk_update_employee_benefits(company_benefit_id="<id>", employee_benefits=[
        gusto_app_integration.EmployeeBenefitForCompanyBenefit(
            employee_uuid="<id>",
        ),
    ], x_gusto_api_version=gusto_app_integration.PutV1CompanyBenefitsCompanyBenefitIDEmployeeBenefitsHeaderXGustoAPIVersion.TWO_THOUSAND_AND_TWENTY_FIVE_MINUS_06_MINUS_15)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                    | Type                                                                                                                                                                                                                         | Required                                                                                                                                                                                                                     | Description                                                                                                                                                                                                                  |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `company_benefit_id`                                                                                                                                                                                                         | *str*                                                                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                                           | The UUID of the company benefit                                                                                                                                                                                              |
| `employee_benefits`                                                                                                                                                                                                          | List[[models.EmployeeBenefitForCompanyBenefit](../../models/employeebenefitforcompanybenefit.md)]                                                                                                                            | :heavy_check_mark:                                                                                                                                                                                                           | The list of employee benefits to create or update                                                                                                                                                                            |
| `x_gusto_api_version`                                                                                                                                                                                                        | [Optional[models.PutV1CompanyBenefitsCompanyBenefitIDEmployeeBenefitsHeaderXGustoAPIVersion]](../../models/putv1companybenefitscompanybenefitidemployeebenefitsheaderxgustoapiversion.md)                                    | :heavy_minus_sign:                                                                                                                                                                                                           | Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used. |
| `retries`                                                                                                                                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                           | Configuration to override the default retry behavior of the client.                                                                                                                                                          |

### Response

**[List[models.EmployeeBenefit]](../../models/.md)**

### Errors

| Error Type                            | Status Code                           | Content Type                          |
| ------------------------------------- | ------------------------------------- | ------------------------------------- |
| models.NotFoundErrorObject            | 404                                   | application/json                      |
| models.UnprocessableEntityErrorObject | 422                                   | application/json                      |
| models.APIError                       | 4XX, 5XX                              | \*/\*                                 |

## get_requirements

Returns the field requirements for a given benefit type.

scope: `benefits:read`

### Example Usage

<!-- UsageSnippet language="python" operationID="get-v1-benefits-benefits_id-requirements" method="get" path="/v1/benefits/{benefit_id}/requirements" -->
```python
import gusto_app_integration
from gusto_app_integration import GustoAppIntegration


with GustoAppIntegration(
    company_access_auth="<YOUR_BEARER_TOKEN_HERE>",
) as gai_client:

    res = gai_client.company_benefits.get_requirements(benefit_id="<id>", x_gusto_api_version=gusto_app_integration.GetV1BenefitsBenefitsIDRequirementsHeaderXGustoAPIVersion.TWO_THOUSAND_AND_TWENTY_FIVE_MINUS_06_MINUS_15)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                    | Type                                                                                                                                                                                                                         | Required                                                                                                                                                                                                                     | Description                                                                                                                                                                                                                  |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `benefit_id`                                                                                                                                                                                                                 | *str*                                                                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                                           | The benefit type in Gusto.                                                                                                                                                                                                   |
| `x_gusto_api_version`                                                                                                                                                                                                        | [Optional[models.GetV1BenefitsBenefitsIDRequirementsHeaderXGustoAPIVersion]](../../models/getv1benefitsbenefitsidrequirementsheaderxgustoapiversion.md)                                                                      | :heavy_minus_sign:                                                                                                                                                                                                           | Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used. |
| `retries`                                                                                                                                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                           | Configuration to override the default retry behavior of the client.                                                                                                                                                          |

### Response

**[models.BenefitTypeRequirements](../../models/benefittyperequirements.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.NotFoundErrorObject | 404                        | application/json           |
| models.APIError            | 4XX, 5XX                   | \*/\*                      |

## get_v1_company_benefits_company_benefit_id_contribution_exclusions

Returns all contributions for a given company benefit and whether they are excluded or not.

Currently this endpoint only works for 401-k and Roth 401-k benefit types.

scope: `company_benefits:read`

### Example Usage

<!-- UsageSnippet language="python" operationID="get-v1-company_benefits-company_benefit_id-contribution_exclusions" method="get" path="/v1/company_benefits/{company_benefit_id}/contribution_exclusions" -->
```python
import gusto_app_integration
from gusto_app_integration import GustoAppIntegration


with GustoAppIntegration(
    company_access_auth="<YOUR_BEARER_TOKEN_HERE>",
) as gai_client:

    res = gai_client.company_benefits.get_v1_company_benefits_company_benefit_id_contribution_exclusions(company_benefit_id="<id>", x_gusto_api_version=gusto_app_integration.GetV1CompanyBenefitsCompanyBenefitIDContributionExclusionsHeaderXGustoAPIVersion.TWO_THOUSAND_AND_TWENTY_FIVE_MINUS_06_MINUS_15)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                    | Type                                                                                                                                                                                                                         | Required                                                                                                                                                                                                                     | Description                                                                                                                                                                                                                  |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `company_benefit_id`                                                                                                                                                                                                         | *str*                                                                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                                           | The UUID of the company benefit                                                                                                                                                                                              |
| `x_gusto_api_version`                                                                                                                                                                                                        | [Optional[models.GetV1CompanyBenefitsCompanyBenefitIDContributionExclusionsHeaderXGustoAPIVersion]](../../models/getv1companybenefitscompanybenefitidcontributionexclusionsheaderxgustoapiversion.md)                        | :heavy_minus_sign:                                                                                                                                                                                                           | Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used. |
| `retries`                                                                                                                                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                           | Configuration to override the default retry behavior of the client.                                                                                                                                                          |

### Response

**[List[models.ContributionExclusion]](../../models/.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.NotFoundErrorObject | 404                        | application/json           |
| models.APIError            | 4XX, 5XX                   | \*/\*                      |

## put_v1_company_benefits_company_benefit_id_contribution_exclusions

Updates contribution exclusions for a given company benefit.

Currently this endpoint only works for 401-k and Roth 401-k benefit types.

scope: `company_benefits:write`

### Example Usage

<!-- UsageSnippet language="python" operationID="put-v1-company_benefits-company_benefit_id-contribution_exclusions" method="put" path="/v1/company_benefits/{company_benefit_id}/contribution_exclusions" -->
```python
import gusto_app_integration
from gusto_app_integration import GustoAppIntegration


with GustoAppIntegration(
    company_access_auth="<YOUR_BEARER_TOKEN_HERE>",
) as gai_client:

    res = gai_client.company_benefits.put_v1_company_benefits_company_benefit_id_contribution_exclusions(company_benefit_id="<id>", contribution_exclusions=[
        {
            "contribution_uuid": "082dfd3e-5b55-11f0-bb42-ab7136ba04e2",
            "contribution_type": "Bonus",
            "excluded": True,
        },
    ], x_gusto_api_version=gusto_app_integration.PutV1CompanyBenefitsCompanyBenefitIDContributionExclusionsHeaderXGustoAPIVersion.TWO_THOUSAND_AND_TWENTY_FIVE_MINUS_06_MINUS_15)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                    | Type                                                                                                                                                                                                                         | Required                                                                                                                                                                                                                     | Description                                                                                                                                                                                                                  |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `company_benefit_id`                                                                                                                                                                                                         | *str*                                                                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                                           | The UUID of the company benefit                                                                                                                                                                                              |
| `contribution_exclusions`                                                                                                                                                                                                    | List[[models.ContributionExclusion](../../models/contributionexclusion.md)]                                                                                                                                                  | :heavy_check_mark:                                                                                                                                                                                                           | The list of contribution exclusions to update                                                                                                                                                                                |
| `x_gusto_api_version`                                                                                                                                                                                                        | [Optional[models.PutV1CompanyBenefitsCompanyBenefitIDContributionExclusionsHeaderXGustoAPIVersion]](../../models/putv1companybenefitscompanybenefitidcontributionexclusionsheaderxgustoapiversion.md)                        | :heavy_minus_sign:                                                                                                                                                                                                           | Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used. |
| `retries`                                                                                                                                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                           | Configuration to override the default retry behavior of the client.                                                                                                                                                          |

### Response

**[List[models.ContributionExclusion]](../../models/.md)**

### Errors

| Error Type                            | Status Code                           | Content Type                          |
| ------------------------------------- | ------------------------------------- | ------------------------------------- |
| models.NotFoundErrorObject            | 404                                   | application/json                      |
| models.UnprocessableEntityErrorObject | 422                                   | application/json                      |
| models.APIError                       | 4XX, 5XX                              | \*/\*                                 |