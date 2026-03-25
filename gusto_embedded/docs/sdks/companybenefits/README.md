# CompanyBenefits

## Overview

### Available Operations

* [create](#create) - Create a company benefit
* [list](#list) - Get benefits for a company
* [get](#get) - Get a company benefit
* [update](#update) - Update a company benefit
* [delete](#delete) - Delete a company benefit
* [get_all](#get_all) - Get all benefits supported by Gusto
* [get_supported](#get_supported) - Get a supported benefit by ID
* [get_summary](#get_summary) - Get company benefit summary by company benefit id.
* [get_employee_benefits](#get_employee_benefits) - Get all employee benefits for a company benefit
* [update_employee_benefits](#update_employee_benefits) - Bulk update employee benefits for a company benefit
* [get_requirements](#get_requirements) - Get benefit fields requirements by ID
* [get_v1_company_benefits_company_benefit_id_contribution_exclusions](#get_v1_company_benefits_company_benefit_id_contribution_exclusions) - Get contribution exclusions for a company benefit
* [put_v1_company_benefits_company_benefit_id_contribution_exclusions](#put_v1_company_benefits_company_benefit_id_contribution_exclusions) - Update contribution exclusions for a company benefit

## create

Company benefits represent the benefits that a company is offering to employees. This ties together a particular supported benefit with the company-specific information for the offering of that benefit.

Note that company benefits can be deactivated only when no employees are enrolled.

When the application has the `company_benefits:write:benefit_type_limited` data scope, the application can only create company benefits for benefit types that are permitted for the application.

scope: `company_benefits:write`

### Example Usage: Basic

<!-- UsageSnippet language="python" operationID="post-v1-companies-company_id-company_benefits" method="post" path="/v1/companies/{company_id}/company_benefits" example="Basic" -->
```python
import gusto_embedded
from gusto_embedded import Gusto
import os


with Gusto(
    company_access_auth=os.getenv("GUSTO_COMPANY_ACCESS_AUTH", ""),
) as gusto:

    res = gusto.company_benefits.create(company_id="<id>", description="hm pfft surge beyond", x_gusto_api_version=gusto_embedded.VersionHeader.TWO_THOUSAND_AND_TWENTY_FIVE_MINUS_06_MINUS_15, active=True)

    # Handle response
    print(res)

```
### Example Usage: Example

<!-- UsageSnippet language="python" operationID="post-v1-companies-company_id-company_benefits" method="post" path="/v1/companies/{company_id}/company_benefits" example="Example" -->
```python
import gusto_embedded
from gusto_embedded import Gusto
import os


with Gusto(
    company_access_auth=os.getenv("GUSTO_COMPANY_ACCESS_AUTH", ""),
) as gusto:

    res = gusto.company_benefits.create(company_id="<id>", description="hm pfft surge beyond", x_gusto_api_version=gusto_embedded.VersionHeader.TWO_THOUSAND_AND_TWENTY_FIVE_MINUS_06_MINUS_15, active=True)

    # Handle response
    print(res)

```
### Example Usage: Nested

<!-- UsageSnippet language="python" operationID="post-v1-companies-company_id-company_benefits" method="post" path="/v1/companies/{company_id}/company_benefits" example="Nested" -->
```python
import gusto_embedded
from gusto_embedded import Gusto
import os


with Gusto(
    company_access_auth=os.getenv("GUSTO_COMPANY_ACCESS_AUTH", ""),
) as gusto:

    res = gusto.company_benefits.create(company_id="<id>", description="hm pfft surge beyond", x_gusto_api_version=gusto_embedded.VersionHeader.TWO_THOUSAND_AND_TWENTY_FIVE_MINUS_06_MINUS_15, active=True)

    # Handle response
    print(res)

```
### Example Usage: Resource

<!-- UsageSnippet language="python" operationID="post-v1-companies-company_id-company_benefits" method="post" path="/v1/companies/{company_id}/company_benefits" example="Resource" -->
```python
import gusto_embedded
from gusto_embedded import Gusto
import os


with Gusto(
    company_access_auth=os.getenv("GUSTO_COMPANY_ACCESS_AUTH", ""),
) as gusto:

    res = gusto.company_benefits.create(company_id="<id>", description="hm pfft surge beyond", x_gusto_api_version=gusto_embedded.VersionHeader.TWO_THOUSAND_AND_TWENTY_FIVE_MINUS_06_MINUS_15, active=True)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                                     | Type                                                                                                                                                                                                                                          | Required                                                                                                                                                                                                                                      | Description                                                                                                                                                                                                                                   |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `company_id`                                                                                                                                                                                                                                  | *str*                                                                                                                                                                                                                                         | :heavy_check_mark:                                                                                                                                                                                                                            | The UUID of the company                                                                                                                                                                                                                       |
| `description`                                                                                                                                                                                                                                 | *str*                                                                                                                                                                                                                                         | :heavy_check_mark:                                                                                                                                                                                                                            | The description of the company benefit. For example, a company may offer multiple benefits with an ID of 1 (for Medical Insurance). The description would show something more specific like “Kaiser Permanente” or “Blue Cross/ Blue Shield”. |
| `x_gusto_api_version`                                                                                                                                                                                                                         | [Optional[models.VersionHeader]](../../models/versionheader.md)                                                                                                                                                                               | :heavy_minus_sign:                                                                                                                                                                                                                            | Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used.                  |
| `benefit_type`                                                                                                                                                                                                                                | *Optional[int]*                                                                                                                                                                                                                               | :heavy_minus_sign:                                                                                                                                                                                                                            | The ID of the benefit to which the company benefit belongs.                                                                                                                                                                                   |
| `active`                                                                                                                                                                                                                                      | *Optional[bool]*                                                                                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                                            | Whether this benefit is active for employee participation.                                                                                                                                                                                    |
| `responsible_for_employer_taxes`                                                                                                                                                                                                              | *Optional[bool]*                                                                                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                                            | Whether the employer is subject to pay employer taxes when an employee is on leave. Only applicable to third party sick pay benefits.                                                                                                         |
| `responsible_for_employee_w2`                                                                                                                                                                                                                 | *Optional[bool]*                                                                                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                                            | Whether the employer is subject to file W-2 forms for an employee on leave. Only applicable to third party sick pay benefits.                                                                                                                 |
| `catch_up_type`                                                                                                                                                                                                                               | [OptionalNullable[models.PostV1CompaniesCompanyIDCompanyBenefitsCatchUpType]](../../models/postv1companiescompanyidcompanybenefitscatchuptype.md)                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                                            | The type of catch-up contribution for this benefit, as required by Section 603 of the SECURE 2.0 Act. Only applicable to pre-tax 401(k) and 403(b) benefits.                                                                                  |
| `retries`                                                                                                                                                                                                                                     | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                                            | Configuration to override the default retry behavior of the client.                                                                                                                                                                           |

### Response

**[models.CompanyBenefit](../../models/companybenefit.md)**

### Errors

| Error Type                            | Status Code                           | Content Type                          |
| ------------------------------------- | ------------------------------------- | ------------------------------------- |
| models.UnprocessableEntityErrorObject | 422                                   | application/json                      |
| models.APIError                       | 4XX, 5XX                              | \*/\*                                 |

## list

Company benefits represent the benefits that a company is offering to employees. This ties together a particular supported benefit with the company-specific information for the offering of that benefit.

Note that company benefits can be deactivated only when no employees are enrolled.

Benefits containing PHI are only visible to applications with the `company_benefits:read:phi` scope.

scope: `company_benefits:read`

### Example Usage

<!-- UsageSnippet language="python" operationID="get-v1-companies-company_id-company_benefits" method="get" path="/v1/companies/{company_id}/company_benefits" example="Example" -->
```python
import gusto_embedded
from gusto_embedded import Gusto
import os


with Gusto(
    company_access_auth=os.getenv("GUSTO_COMPANY_ACCESS_AUTH", ""),
) as gusto:

    res = gusto.company_benefits.list(company_id="<id>", x_gusto_api_version=gusto_embedded.VersionHeader.TWO_THOUSAND_AND_TWENTY_FIVE_MINUS_06_MINUS_15)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                    | Type                                                                                                                                                                                                                         | Required                                                                                                                                                                                                                     | Description                                                                                                                                                                                                                  |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `company_id`                                                                                                                                                                                                                 | *str*                                                                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                                           | The UUID of the company                                                                                                                                                                                                      |
| `active`                                                                                                                                                                                                                     | *Optional[bool]*                                                                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                           | Whether the benefit is currently active                                                                                                                                                                                      |
| `enrollment_count`                                                                                                                                                                                                           | *Optional[bool]*                                                                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                           | Whether to return employee enrollment count                                                                                                                                                                                  |
| `benefit_type`                                                                                                                                                                                                               | *Optional[str]*                                                                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                           | Filter by benefit type. Comma-separated list of benefit type IDs, i.e. `?benefit_type=5,105`                                                                                                                                 |
| `x_gusto_api_version`                                                                                                                                                                                                        | [Optional[models.VersionHeader]](../../models/versionheader.md)                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                           | Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used. |
| `retries`                                                                                                                                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                           | Configuration to override the default retry behavior of the client.                                                                                                                                                          |

### Response

**[List[models.CompanyBenefit]](../../models/.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## get

Company benefits represent the benefits that a company is offering to employees. This ties together a particular supported benefit with the company-specific information for the offering of that benefit.

Note that company benefits can be deactivated only when no employees are enrolled.

When with_employee_benefits parameter with true value is passed, employee_benefits:read scope is required to return employee_benefits.

scope: `company_benefits:read`

### Example Usage

<!-- UsageSnippet language="python" operationID="get-v1-company_benefits-company_benefit_id" method="get" path="/v1/company_benefits/{company_benefit_id}" example="Example" -->
```python
import gusto_embedded
from gusto_embedded import Gusto
import os


with Gusto(
    company_access_auth=os.getenv("GUSTO_COMPANY_ACCESS_AUTH", ""),
) as gusto:

    res = gusto.company_benefits.get(company_benefit_id="<id>", x_gusto_api_version=gusto_embedded.VersionHeader.TWO_THOUSAND_AND_TWENTY_FIVE_MINUS_06_MINUS_15)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                    | Type                                                                                                                                                                                                                         | Required                                                                                                                                                                                                                     | Description                                                                                                                                                                                                                  |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `company_benefit_id`                                                                                                                                                                                                         | *str*                                                                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                                           | The UUID of the company benefit                                                                                                                                                                                              |
| `with_employee_benefits`                                                                                                                                                                                                     | *Optional[bool]*                                                                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                           | Whether to return employee benefits associated with the benefit                                                                                                                                                              |
| `include`                                                                                                                                                                                                                    | [Optional[models.GetV1CompanyBenefitsCompanyBenefitIDQueryParamInclude]](../../models/getv1companybenefitscompanybenefitidqueryparaminclude.md)                                                                              | :heavy_minus_sign:                                                                                                                                                                                                           | Available options:<br/>- all_benefits: If with_employee_benefits=true, include all effective dated benefits for each employee instead of only the current benefits.                                                          |
| `x_gusto_api_version`                                                                                                                                                                                                        | [Optional[models.VersionHeader]](../../models/versionheader.md)                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                           | Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used. |
| `retries`                                                                                                                                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                           | Configuration to override the default retry behavior of the client.                                                                                                                                                          |

### Response

**[models.CompanyBenefitWithEmployeeBenefits](../../models/companybenefitwithemployeebenefits.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## update

Company benefits represent the benefits that a company is offering to employees. This ties together a particular supported benefit with the company-specific information for the offering of that benefit.

Note that company benefits can be deactivated only when no employees are enrolled.

When the application has the `company_benefits:write:benefit_type_limited` data scope, the application can only update company benefits for benefit types that are permitted for the application.

scope: `company_benefits:write`

### Example Usage: Basic

<!-- UsageSnippet language="python" operationID="put-v1-company_benefits-company_benefit_id" method="put" path="/v1/company_benefits/{company_benefit_id}" example="Basic" -->
```python
import gusto_embedded
from gusto_embedded import Gusto
import os


with Gusto(
    company_access_auth=os.getenv("GUSTO_COMPANY_ACCESS_AUTH", ""),
) as gusto:

    res = gusto.company_benefits.update(company_benefit_id="<id>", version="<value>", x_gusto_api_version=gusto_embedded.VersionHeader.TWO_THOUSAND_AND_TWENTY_FIVE_MINUS_06_MINUS_15)

    # Handle response
    print(res)

```
### Example Usage: Example

<!-- UsageSnippet language="python" operationID="put-v1-company_benefits-company_benefit_id" method="put" path="/v1/company_benefits/{company_benefit_id}" example="Example" -->
```python
import gusto_embedded
from gusto_embedded import Gusto
import os


with Gusto(
    company_access_auth=os.getenv("GUSTO_COMPANY_ACCESS_AUTH", ""),
) as gusto:

    res = gusto.company_benefits.update(company_benefit_id="<id>", version="98jr3289h3298hr9329gf9egskt3kagri32qqgiqe3872", x_gusto_api_version=gusto_embedded.VersionHeader.TWO_THOUSAND_AND_TWENTY_FIVE_MINUS_06_MINUS_15, active=False)

    # Handle response
    print(res)

```
### Example Usage: Nested

<!-- UsageSnippet language="python" operationID="put-v1-company_benefits-company_benefit_id" method="put" path="/v1/company_benefits/{company_benefit_id}" example="Nested" -->
```python
import gusto_embedded
from gusto_embedded import Gusto
import os


with Gusto(
    company_access_auth=os.getenv("GUSTO_COMPANY_ACCESS_AUTH", ""),
) as gusto:

    res = gusto.company_benefits.update(company_benefit_id="<id>", version="<value>", x_gusto_api_version=gusto_embedded.VersionHeader.TWO_THOUSAND_AND_TWENTY_FIVE_MINUS_06_MINUS_15)

    # Handle response
    print(res)

```
### Example Usage: Resource

<!-- UsageSnippet language="python" operationID="put-v1-company_benefits-company_benefit_id" method="put" path="/v1/company_benefits/{company_benefit_id}" example="Resource" -->
```python
import gusto_embedded
from gusto_embedded import Gusto
import os


with Gusto(
    company_access_auth=os.getenv("GUSTO_COMPANY_ACCESS_AUTH", ""),
) as gusto:

    res = gusto.company_benefits.update(company_benefit_id="<id>", version="<value>", x_gusto_api_version=gusto_embedded.VersionHeader.TWO_THOUSAND_AND_TWENTY_FIVE_MINUS_06_MINUS_15)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                                     | Type                                                                                                                                                                                                                                          | Required                                                                                                                                                                                                                                      | Description                                                                                                                                                                                                                                   |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `company_benefit_id`                                                                                                                                                                                                                          | *str*                                                                                                                                                                                                                                         | :heavy_check_mark:                                                                                                                                                                                                                            | The UUID of the company benefit                                                                                                                                                                                                               |
| `version`                                                                                                                                                                                                                                     | *str*                                                                                                                                                                                                                                         | :heavy_check_mark:                                                                                                                                                                                                                            | The current version of the object. See the [versioning guide](https://docs.gusto.com/embedded-payroll/docs/versioning#object-layer) for information on how to use this field.                                                                 |
| `x_gusto_api_version`                                                                                                                                                                                                                         | [Optional[models.VersionHeader]](../../models/versionheader.md)                                                                                                                                                                               | :heavy_minus_sign:                                                                                                                                                                                                                            | Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used.                  |
| `active`                                                                                                                                                                                                                                      | *Optional[bool]*                                                                                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                                            | Whether this benefit is active for employee participation. Company benefits may only be deactivated if no employees are actively participating.                                                                                               |
| `description`                                                                                                                                                                                                                                 | *Optional[str]*                                                                                                                                                                                                                               | :heavy_minus_sign:                                                                                                                                                                                                                            | The description of the company benefit. For example, a company may offer multiple benefits with an ID of 1 (for Medical Insurance). The description would show something more specific like “Kaiser Permanente” or “Blue Cross/ Blue Shield”. |
| `responsible_for_employer_taxes`                                                                                                                                                                                                              | *Optional[bool]*                                                                                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                                            | Whether the employer is subject to pay employer taxes when an employee is on leave. Only applicable to short-term and long-term disability benefits (different from voluntary disability).                                                    |
| `responsible_for_employee_w2`                                                                                                                                                                                                                 | *Optional[bool]*                                                                                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                                            | Whether the employer is subject to file W-2 forms for an employee on leave. Only applicable to short-term and long-term disability benefits (different from voluntary disability).                                                            |
| `catch_up_type`                                                                                                                                                                                                                               | [OptionalNullable[models.PutV1CompanyBenefitsCompanyBenefitIDCatchUpType]](../../models/putv1companybenefitscompanybenefitidcatchuptype.md)                                                                                                   | :heavy_minus_sign:                                                                                                                                                                                                                            | The type of catch-up contribution for this benefit, as required by Section 603 of the SECURE 2.0 Act. Only applicable to pre-tax 401(k) and 403(b) benefits.                                                                                  |
| `retries`                                                                                                                                                                                                                                     | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                                            | Configuration to override the default retry behavior of the client.                                                                                                                                                                           |

### Response

**[models.CompanyBenefit](../../models/companybenefit.md)**

### Errors

| Error Type                            | Status Code                           | Content Type                          |
| ------------------------------------- | ------------------------------------- | ------------------------------------- |
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
import gusto_embedded
from gusto_embedded import Gusto
import os


with Gusto(
    company_access_auth=os.getenv("GUSTO_COMPANY_ACCESS_AUTH", ""),
) as gusto:

    gusto.company_benefits.delete(company_benefit_id="<id>", x_gusto_api_version=gusto_embedded.VersionHeader.TWO_THOUSAND_AND_TWENTY_FIVE_MINUS_06_MINUS_15)

    # Use the SDK ...

```

### Parameters

| Parameter                                                                                                                                                                                                                    | Type                                                                                                                                                                                                                         | Required                                                                                                                                                                                                                     | Description                                                                                                                                                                                                                  |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `company_benefit_id`                                                                                                                                                                                                         | *str*                                                                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                                           | The UUID of the company benefit                                                                                                                                                                                              |
| `x_gusto_api_version`                                                                                                                                                                                                        | [Optional[models.VersionHeader]](../../models/versionheader.md)                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                           | Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used. |
| `retries`                                                                                                                                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                           | Configuration to override the default retry behavior of the client.                                                                                                                                                          |

### Errors

| Error Type                            | Status Code                           | Content Type                          |
| ------------------------------------- | ------------------------------------- | ------------------------------------- |
| models.UnprocessableEntityErrorObject | 422                                   | application/json                      |
| models.APIError                       | 4XX, 5XX                              | \*/\*                                 |

## get_all

Returns all benefits supported by Gusto.

The benefit object in Gusto contains high level information about a particular benefit type and its tax considerations. When companies choose to offer a benefit, they are creating a Company Benefit object associated with a particular benefit.

scope: `benefits:read`

### Example Usage

<!-- UsageSnippet language="python" operationID="get-v1-benefits" method="get" path="/v1/benefits" example="Supported Benefits" -->
```python
import gusto_embedded
from gusto_embedded import Gusto
import os


with Gusto(
    company_access_auth=os.getenv("GUSTO_COMPANY_ACCESS_AUTH", ""),
) as gusto:

    res = gusto.company_benefits.get_all(x_gusto_api_version=gusto_embedded.VersionHeader.TWO_THOUSAND_AND_TWENTY_FIVE_MINUS_06_MINUS_15)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                    | Type                                                                                                                                                                                                                         | Required                                                                                                                                                                                                                     | Description                                                                                                                                                                                                                  |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `x_gusto_api_version`                                                                                                                                                                                                        | [Optional[models.VersionHeader]](../../models/versionheader.md)                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                           | Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used. |
| `retries`                                                                                                                                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                           | Configuration to override the default retry behavior of the client.                                                                                                                                                          |

### Response

**[List[models.SupportedBenefit]](../../models/.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## get_supported

Returns a benefit supported by Gusto.

The benefit object in Gusto contains high level information about a particular benefit type and its tax considerations. When companies choose to offer a benefit, they are creating a Company Benefit object associated with a particular benefit.

scope: `benefits:read`

### Example Usage

<!-- UsageSnippet language="python" operationID="get-v1-benefits-benefit_id" method="get" path="/v1/benefits/{benefit_id}" example="Example" -->
```python
import gusto_embedded
from gusto_embedded import Gusto
import os


with Gusto(
    company_access_auth=os.getenv("GUSTO_COMPANY_ACCESS_AUTH", ""),
) as gusto:

    res = gusto.company_benefits.get_supported(benefit_id="<id>", x_gusto_api_version=gusto_embedded.VersionHeader.TWO_THOUSAND_AND_TWENTY_FIVE_MINUS_06_MINUS_15)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                    | Type                                                                                                                                                                                                                         | Required                                                                                                                                                                                                                     | Description                                                                                                                                                                                                                  |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `benefit_id`                                                                                                                                                                                                                 | *str*                                                                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                                           | The benefit type in Gusto.                                                                                                                                                                                                   |
| `x_gusto_api_version`                                                                                                                                                                                                        | [Optional[models.VersionHeader]](../../models/versionheader.md)                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                           | Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used. |
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

<!-- UsageSnippet language="python" operationID="get-v1-benefits-company_benefit_id-summary" method="get" path="/v1/company_benefits/{company_benefit_id}/summary" example="Example" -->
```python
import gusto_embedded
from gusto_embedded import Gusto
import os


with Gusto(
    company_access_auth=os.getenv("GUSTO_COMPANY_ACCESS_AUTH", ""),
) as gusto:

    res = gusto.company_benefits.get_summary(company_benefit_id="<id>", start_date="2022-01-01", end_date="2022-12-31", x_gusto_api_version=gusto_embedded.VersionHeader.TWO_THOUSAND_AND_TWENTY_FIVE_MINUS_06_MINUS_15)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                    | Type                                                                                                                                                                                                                         | Required                                                                                                                                                                                                                     | Description                                                                                                                                                                                                                  | Example                                                                                                                                                                                                                      |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `company_benefit_id`                                                                                                                                                                                                         | *str*                                                                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                                           | The UUID of the company benefit                                                                                                                                                                                              |                                                                                                                                                                                                                              |
| `start_date`                                                                                                                                                                                                                 | *Optional[str]*                                                                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                           | The start date for which to retrieve company benefit summary                                                                                                                                                                 | 2022-01-01                                                                                                                                                                                                                   |
| `end_date`                                                                                                                                                                                                                   | *Optional[str]*                                                                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                           | The end date for which to retrieve company benefit summary. If left empty, defaults to today's date.                                                                                                                         | 2022-12-31                                                                                                                                                                                                                   |
| `detailed`                                                                                                                                                                                                                   | *Optional[bool]*                                                                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                           | Display employee payroll item summary                                                                                                                                                                                        |                                                                                                                                                                                                                              |
| `x_gusto_api_version`                                                                                                                                                                                                        | [Optional[models.VersionHeader]](../../models/versionheader.md)                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                           | Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used. |                                                                                                                                                                                                                              |
| `retries`                                                                                                                                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                           | Configuration to override the default retry behavior of the client.                                                                                                                                                          |                                                                                                                                                                                                                              |

### Response

**[models.BenefitSummary](../../models/benefitsummary.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## get_employee_benefits

Employee benefits represent an employee enrolled in a particular company benefit. It includes information specific to that employee’s enrollment.

Returns an array of all employee benefits enrolled for this company benefit.

Benefits containing PHI are only visible to applications with the `employee_benefits:read:phi` scope.

scope: `employee_benefits:read`

### Example Usage

<!-- UsageSnippet language="python" operationID="get-v1-company_benefits-company_benefit_id-employee_benefits" method="get" path="/v1/company_benefits/{company_benefit_id}/employee_benefits" example="Example" -->
```python
import gusto_embedded
from gusto_embedded import Gusto
import os


with Gusto(
    company_access_auth=os.getenv("GUSTO_COMPANY_ACCESS_AUTH", ""),
) as gusto:

    res = gusto.company_benefits.get_employee_benefits(company_benefit_id="<id>", x_gusto_api_version=gusto_embedded.VersionHeader.TWO_THOUSAND_AND_TWENTY_FIVE_MINUS_06_MINUS_15)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                    | Type                                                                                                                                                                                                                         | Required                                                                                                                                                                                                                     | Description                                                                                                                                                                                                                  |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `company_benefit_id`                                                                                                                                                                                                         | *str*                                                                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                                           | The UUID of the company benefit                                                                                                                                                                                              |
| `page`                                                                                                                                                                                                                       | *Optional[int]*                                                                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                           | The page that is requested. When unspecified, will load all objects unless endpoint forces pagination.                                                                                                                       |
| `per`                                                                                                                                                                                                                        | *Optional[int]*                                                                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                           | Number of objects per page. For majority of endpoints will default to 25                                                                                                                                                     |
| `include`                                                                                                                                                                                                                    | [Optional[models.GetV1CompanyBenefitsCompanyBenefitIDEmployeeBenefitsQueryParamInclude]](../../models/getv1companybenefitscompanybenefitidemployeebenefitsqueryparaminclude.md)                                              | :heavy_minus_sign:                                                                                                                                                                                                           | Available options:<br/>- all_benefits: Include all effective dated benefits for each employee instead of only the current benefits.                                                                                          |
| `x_gusto_api_version`                                                                                                                                                                                                        | [Optional[models.VersionHeader]](../../models/versionheader.md)                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                           | Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used. |
| `retries`                                                                                                                                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                           | Configuration to override the default retry behavior of the client.                                                                                                                                                          |

### Response

**[List[models.EmployeeBenefit]](../../models/.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## update_employee_benefits

Employee benefits represent an employee enrolled in a particular company benefit. It includes information specific to that employee's enrollment.

Create or update(if the employee is already enrolled in the company benefit previously) an employee benefit for the company benefit.

Benefits containing PHI are only visible to applications with the `employee_benefits:read:phi` scope.

When the application has the `employee_benefits:write:benefit_type_limited` data scope, the application can only create or update employee benefits for benefit types that are permitted for the application.

scope: `employee_benefits:write`

### Example Usage: Basic

<!-- UsageSnippet language="python" operationID="put-v1-company_benefits-company_benefit_id-employee_benefits" method="put" path="/v1/company_benefits/{company_benefit_id}/employee_benefits" example="Basic" -->
```python
import gusto_embedded
from gusto_embedded import Gusto
import os


with Gusto(
    company_access_auth=os.getenv("GUSTO_COMPANY_ACCESS_AUTH", ""),
) as gusto:

    res = gusto.company_benefits.update_employee_benefits(company_benefit_id="<id>", employee_benefits=[
        {
            "employee_uuid": "<id>",
        },
    ], x_gusto_api_version=gusto_embedded.VersionHeader.TWO_THOUSAND_AND_TWENTY_FIVE_MINUS_06_MINUS_15)

    # Handle response
    print(res)

```
### Example Usage: Example

<!-- UsageSnippet language="python" operationID="put-v1-company_benefits-company_benefit_id-employee_benefits" method="put" path="/v1/company_benefits/{company_benefit_id}/employee_benefits" example="Example" -->
```python
import gusto_embedded
from gusto_embedded import Gusto
import os


with Gusto(
    company_access_auth=os.getenv("GUSTO_COMPANY_ACCESS_AUTH", ""),
) as gusto:

    res = gusto.company_benefits.update_employee_benefits(company_benefit_id="<id>", employee_benefits=[
        {
            "version": "09j3d29jqdpj92109j9j2d90dq",
            "employee_deduction": "250.00",
            "employee_uuid": "8f9f3f68-8fd3-499d-ade7-4a052e56494e",
        },
    ], x_gusto_api_version=gusto_embedded.VersionHeader.TWO_THOUSAND_AND_TWENTY_FIVE_MINUS_06_MINUS_15)

    # Handle response
    print(res)

```
### Example Usage: Nested

<!-- UsageSnippet language="python" operationID="put-v1-company_benefits-company_benefit_id-employee_benefits" method="put" path="/v1/company_benefits/{company_benefit_id}/employee_benefits" example="Nested" -->
```python
import gusto_embedded
from gusto_embedded import Gusto
import os


with Gusto(
    company_access_auth=os.getenv("GUSTO_COMPANY_ACCESS_AUTH", ""),
) as gusto:

    res = gusto.company_benefits.update_employee_benefits(company_benefit_id="<id>", employee_benefits=[
        {
            "employee_uuid": "<id>",
        },
    ], x_gusto_api_version=gusto_embedded.VersionHeader.TWO_THOUSAND_AND_TWENTY_FIVE_MINUS_06_MINUS_15)

    # Handle response
    print(res)

```
### Example Usage: Resource

<!-- UsageSnippet language="python" operationID="put-v1-company_benefits-company_benefit_id-employee_benefits" method="put" path="/v1/company_benefits/{company_benefit_id}/employee_benefits" example="Resource" -->
```python
import gusto_embedded
from gusto_embedded import Gusto
import os


with Gusto(
    company_access_auth=os.getenv("GUSTO_COMPANY_ACCESS_AUTH", ""),
) as gusto:

    res = gusto.company_benefits.update_employee_benefits(company_benefit_id="<id>", employee_benefits=[
        {
            "employee_uuid": "<id>",
        },
    ], x_gusto_api_version=gusto_embedded.VersionHeader.TWO_THOUSAND_AND_TWENTY_FIVE_MINUS_06_MINUS_15)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                    | Type                                                                                                                                                                                                                         | Required                                                                                                                                                                                                                     | Description                                                                                                                                                                                                                  |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `company_benefit_id`                                                                                                                                                                                                         | *str*                                                                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                                           | The UUID of the company benefit                                                                                                                                                                                              |
| `employee_benefits`                                                                                                                                                                                                          | List[[models.EmployeeBenefitForCompanyBenefit](../../models/employeebenefitforcompanybenefit.md)]                                                                                                                            | :heavy_check_mark:                                                                                                                                                                                                           | The list of employee benefits to create or update                                                                                                                                                                            |
| `x_gusto_api_version`                                                                                                                                                                                                        | [Optional[models.VersionHeader]](../../models/versionheader.md)                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                           | Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used. |
| `retries`                                                                                                                                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                           | Configuration to override the default retry behavior of the client.                                                                                                                                                          |

### Response

**[List[models.EmployeeBenefit]](../../models/.md)**

### Errors

| Error Type                            | Status Code                           | Content Type                          |
| ------------------------------------- | ------------------------------------- | ------------------------------------- |
| models.UnprocessableEntityErrorObject | 422                                   | application/json                      |
| models.APIError                       | 4XX, 5XX                              | \*/\*                                 |

## get_requirements

Returns field requirements for the requested benefit type.

scope: `benefits:read`

### Example Usage

<!-- UsageSnippet language="python" operationID="get-v1-benefits-benefits_id-requirements" method="get" path="/v1/benefits/{benefit_id}/requirements" example="Example" -->
```python
import gusto_embedded
from gusto_embedded import Gusto
import os


with Gusto(
    company_access_auth=os.getenv("GUSTO_COMPANY_ACCESS_AUTH", ""),
) as gusto:

    res = gusto.company_benefits.get_requirements(benefit_id="<id>", x_gusto_api_version=gusto_embedded.VersionHeader.TWO_THOUSAND_AND_TWENTY_FIVE_MINUS_06_MINUS_15)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                    | Type                                                                                                                                                                                                                         | Required                                                                                                                                                                                                                     | Description                                                                                                                                                                                                                  |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `benefit_id`                                                                                                                                                                                                                 | *str*                                                                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                                           | The benefit type in Gusto.                                                                                                                                                                                                   |
| `x_gusto_api_version`                                                                                                                                                                                                        | [Optional[models.VersionHeader]](../../models/versionheader.md)                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                           | Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used. |
| `retries`                                                                                                                                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                           | Configuration to override the default retry behavior of the client.                                                                                                                                                          |

### Response

**[models.BenefitTypeRequirements](../../models/benefittyperequirements.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## get_v1_company_benefits_company_benefit_id_contribution_exclusions

Returns all contributions for a given company benefit and whether they are excluded or not.

Currently this endpoint only works for 401-k and Roth 401-k benefit types.

scope: `company_benefits:read`

### Example Usage

<!-- UsageSnippet language="python" operationID="get-v1-company_benefits-company_benefit_id-contribution_exclusions" method="get" path="/v1/company_benefits/{company_benefit_id}/contribution_exclusions" example="Example" -->
```python
import gusto_embedded
from gusto_embedded import Gusto
import os


with Gusto(
    company_access_auth=os.getenv("GUSTO_COMPANY_ACCESS_AUTH", ""),
) as gusto:

    res = gusto.company_benefits.get_v1_company_benefits_company_benefit_id_contribution_exclusions(company_benefit_id="<id>", x_gusto_api_version=gusto_embedded.VersionHeader.TWO_THOUSAND_AND_TWENTY_FIVE_MINUS_06_MINUS_15)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                    | Type                                                                                                                                                                                                                         | Required                                                                                                                                                                                                                     | Description                                                                                                                                                                                                                  |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `company_benefit_id`                                                                                                                                                                                                         | *str*                                                                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                                           | The UUID of the company benefit                                                                                                                                                                                              |
| `x_gusto_api_version`                                                                                                                                                                                                        | [Optional[models.VersionHeader]](../../models/versionheader.md)                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                           | Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used. |
| `retries`                                                                                                                                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                           | Configuration to override the default retry behavior of the client.                                                                                                                                                          |

### Response

**[List[models.ContributionExclusion]](../../models/.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## put_v1_company_benefits_company_benefit_id_contribution_exclusions

Updates contribution exclusions for a given company benefit.

Currently this endpoint only works for 401-k and Roth 401-k benefit types.

scope: `company_benefits:write`

### Example Usage: Basic

<!-- UsageSnippet language="python" operationID="put-v1-company_benefits-company_benefit_id-contribution_exclusions" method="put" path="/v1/company_benefits/{company_benefit_id}/contribution_exclusions" example="Basic" -->
```python
import gusto_embedded
from gusto_embedded import Gusto
import os


with Gusto(
    company_access_auth=os.getenv("GUSTO_COMPANY_ACCESS_AUTH", ""),
) as gusto:

    res = gusto.company_benefits.put_v1_company_benefits_company_benefit_id_contribution_exclusions(company_benefit_id="<id>", contribution_exclusions=[
        {
            "contribution_uuid": "<id>",
            "contribution_type": "<value>",
            "excluded": True,
        },
    ], x_gusto_api_version=gusto_embedded.VersionHeader.TWO_THOUSAND_AND_TWENTY_FIVE_MINUS_06_MINUS_15)

    # Handle response
    print(res)

```
### Example Usage: Example

<!-- UsageSnippet language="python" operationID="put-v1-company_benefits-company_benefit_id-contribution_exclusions" method="put" path="/v1/company_benefits/{company_benefit_id}/contribution_exclusions" example="Example" -->
```python
import gusto_embedded
from gusto_embedded import Gusto
import os


with Gusto(
    company_access_auth=os.getenv("GUSTO_COMPANY_ACCESS_AUTH", ""),
) as gusto:

    res = gusto.company_benefits.put_v1_company_benefits_company_benefit_id_contribution_exclusions(company_benefit_id="<id>", contribution_exclusions=[
        {
            "contribution_uuid": "082dfd3e-5b55-11f0-bb42-ab7136ba04e2",
            "contribution_type": "Bonus",
            "excluded": True,
        },
        {
            "contribution_uuid": "082e034c-5b55-11f0-bb42-ab7136ba04e2",
            "contribution_type": "Commission",
            "excluded": False,
        },
        {
            "contribution_uuid": "082e1f6c-5b55-11f0-bb42-ab7136ba04e2",
            "contribution_type": "Regular",
            "excluded": True,
        },
    ], x_gusto_api_version=gusto_embedded.VersionHeader.TWO_THOUSAND_AND_TWENTY_FIVE_MINUS_06_MINUS_15)

    # Handle response
    print(res)

```
### Example Usage: Nested

<!-- UsageSnippet language="python" operationID="put-v1-company_benefits-company_benefit_id-contribution_exclusions" method="put" path="/v1/company_benefits/{company_benefit_id}/contribution_exclusions" example="Nested" -->
```python
import gusto_embedded
from gusto_embedded import Gusto
import os


with Gusto(
    company_access_auth=os.getenv("GUSTO_COMPANY_ACCESS_AUTH", ""),
) as gusto:

    res = gusto.company_benefits.put_v1_company_benefits_company_benefit_id_contribution_exclusions(company_benefit_id="<id>", contribution_exclusions=[
        {
            "contribution_uuid": "<id>",
            "contribution_type": "<value>",
            "excluded": True,
        },
    ], x_gusto_api_version=gusto_embedded.VersionHeader.TWO_THOUSAND_AND_TWENTY_FIVE_MINUS_06_MINUS_15)

    # Handle response
    print(res)

```
### Example Usage: Resource

<!-- UsageSnippet language="python" operationID="put-v1-company_benefits-company_benefit_id-contribution_exclusions" method="put" path="/v1/company_benefits/{company_benefit_id}/contribution_exclusions" example="Resource" -->
```python
import gusto_embedded
from gusto_embedded import Gusto
import os


with Gusto(
    company_access_auth=os.getenv("GUSTO_COMPANY_ACCESS_AUTH", ""),
) as gusto:

    res = gusto.company_benefits.put_v1_company_benefits_company_benefit_id_contribution_exclusions(company_benefit_id="<id>", contribution_exclusions=[
        {
            "contribution_uuid": "<id>",
            "contribution_type": "<value>",
            "excluded": True,
        },
    ], x_gusto_api_version=gusto_embedded.VersionHeader.TWO_THOUSAND_AND_TWENTY_FIVE_MINUS_06_MINUS_15)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                    | Type                                                                                                                                                                                                                         | Required                                                                                                                                                                                                                     | Description                                                                                                                                                                                                                  |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `company_benefit_id`                                                                                                                                                                                                         | *str*                                                                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                                           | The UUID of the company benefit                                                                                                                                                                                              |
| `contribution_exclusions`                                                                                                                                                                                                    | List[[models.ContributionExclusion](../../models/contributionexclusion.md)]                                                                                                                                                  | :heavy_check_mark:                                                                                                                                                                                                           | The list of contribution exclusions to update                                                                                                                                                                                |
| `x_gusto_api_version`                                                                                                                                                                                                        | [Optional[models.VersionHeader]](../../models/versionheader.md)                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                           | Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used. |
| `retries`                                                                                                                                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                           | Configuration to override the default retry behavior of the client.                                                                                                                                                          |

### Response

**[List[models.ContributionExclusion]](../../models/.md)**

### Errors

| Error Type                            | Status Code                           | Content Type                          |
| ------------------------------------- | ------------------------------------- | ------------------------------------- |
| models.UnprocessableEntityErrorObject | 422                                   | application/json                      |
| models.APIError                       | 4XX, 5XX                              | \*/\*                                 |