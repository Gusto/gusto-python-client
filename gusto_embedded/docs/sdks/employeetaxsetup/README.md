# EmployeeTaxSetup

## Overview

### Available Operations

* [get_federal_taxes](#get_federal_taxes) - Get federal taxes for an employee
* [update_federal_taxes](#update_federal_taxes) - Update federal taxes for an employee
* [get_state_taxes](#get_state_taxes) - Get an employee's state taxes
* [update_state_taxes](#update_state_taxes) - Update an employee's state taxes

## get_federal_taxes

Returns federal tax information for an employee. The response structure varies based on the w4_data_type (pre_2020_w4 or rev_2020_w4).

scope: `employee_federal_taxes:read`

### Example Usage

<!-- UsageSnippet language="python" operationID="get-v1-employees-employee_id-federal_taxes" method="get" path="/v1/employees/{employee_uuid}/federal_taxes" -->
```python
import gusto_embedded
from gusto_embedded import Gusto
import os


with Gusto(
    company_access_auth=os.getenv("GUSTO_COMPANY_ACCESS_AUTH", ""),
) as gusto:

    res = gusto.employee_tax_setup.get_federal_taxes(employee_uuid="<id>", x_gusto_api_version=gusto_embedded.GetV1EmployeesEmployeeIDFederalTaxesHeaderXGustoAPIVersion.TWO_THOUSAND_AND_TWENTY_FIVE_MINUS_06_MINUS_15)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                    | Type                                                                                                                                                                                                                         | Required                                                                                                                                                                                                                     | Description                                                                                                                                                                                                                  |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `employee_uuid`                                                                                                                                                                                                              | *str*                                                                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                                           | The UUID of the employee                                                                                                                                                                                                     |
| `x_gusto_api_version`                                                                                                                                                                                                        | [Optional[models.GetV1EmployeesEmployeeIDFederalTaxesHeaderXGustoAPIVersion]](../../models/getv1employeesemployeeidfederaltaxesheaderxgustoapiversion.md)                                                                    | :heavy_minus_sign:                                                                                                                                                                                                           | Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used. |
| `retries`                                                                                                                                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                           | Configuration to override the default retry behavior of the client.                                                                                                                                                          |

### Response

**[models.EmployeeFederalTax](../../models/employeefederaltax.md)**

### Errors

| Error Type                      | Status Code                     | Content Type                    |
| ------------------------------- | ------------------------------- | ------------------------------- |
| models.NotFoundErrorObjectError | 404                             | application/json                |
| models.APIError                 | 4XX, 5XX                        | \*/\*                           |

## update_federal_taxes

Updates federal tax (W4) information for an employee. Only rev_2020_w4 format is accepted for updates.

scope: `employee_federal_taxes:write`

### Example Usage

<!-- UsageSnippet language="python" operationID="put-v1-employees-employee_id-federal_taxes" method="put" path="/v1/employees/{employee_uuid}/federal_taxes" -->
```python
import gusto_embedded
from gusto_embedded import Gusto
import os


with Gusto(
    company_access_auth=os.getenv("GUSTO_COMPANY_ACCESS_AUTH", ""),
) as gusto:

    res = gusto.employee_tax_setup.update_federal_taxes(employee_uuid="<id>", version="56a489ce86ed6c1b0f0cecc4050a0b01", w4_data_type=gusto_embedded.PutV1EmployeesEmployeeIDFederalTaxesW4DataType.REV_2020_W4, filing_status=gusto_embedded.FilingStatus.SINGLE, x_gusto_api_version=gusto_embedded.PutV1EmployeesEmployeeIDFederalTaxesHeaderXGustoAPIVersion.TWO_THOUSAND_AND_TWENTY_FIVE_MINUS_06_MINUS_15)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                    | Type                                                                                                                                                                                                                         | Required                                                                                                                                                                                                                     | Description                                                                                                                                                                                                                  | Example                                                                                                                                                                                                                      |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `employee_uuid`                                                                                                                                                                                                              | *str*                                                                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                                           | The UUID of the employee                                                                                                                                                                                                     |                                                                                                                                                                                                                              |
| `version`                                                                                                                                                                                                                    | *str*                                                                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                                           | The current version of the object. See the [versioning guide](https://docs.gusto.com/embedded-payroll/docs/versioning#object-layer) for information on how to use this field.                                                | 56a489ce86ed6c1b0f0cecc4050a0b01                                                                                                                                                                                             |
| `w4_data_type`                                                                                                                                                                                                               | [models.PutV1EmployeesEmployeeIDFederalTaxesW4DataType](../../models/putv1employeesemployeeidfederaltaxesw4datatype.md)                                                                                                      | :heavy_check_mark:                                                                                                                                                                                                           | The version of the W4 form. Only rev_2020_w4 is accepted for updates.                                                                                                                                                        |                                                                                                                                                                                                                              |
| `filing_status`                                                                                                                                                                                                              | [models.FilingStatus](../../models/filingstatus.md)                                                                                                                                                                          | :heavy_check_mark:                                                                                                                                                                                                           | Determines which tax return form an individual will use. One of: Single, Married, Head of Household, Exempt from withholding.                                                                                                | Single                                                                                                                                                                                                                       |
| `x_gusto_api_version`                                                                                                                                                                                                        | [Optional[models.PutV1EmployeesEmployeeIDFederalTaxesHeaderXGustoAPIVersion]](../../models/putv1employeesemployeeidfederaltaxesheaderxgustoapiversion.md)                                                                    | :heavy_minus_sign:                                                                                                                                                                                                           | Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used. |                                                                                                                                                                                                                              |
| `two_jobs`                                                                                                                                                                                                                   | *Optional[bool]*                                                                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                           | If there are only two jobs (e.g., you and your spouse each have a job), set to true.                                                                                                                                         |                                                                                                                                                                                                                              |
| `dependents_amount`                                                                                                                                                                                                          | *Optional[float]*                                                                                                                                                                                                            | :heavy_minus_sign:                                                                                                                                                                                                           | Amount for dependents; a dependent entitles the taxpayer to claim a dependency exemption.                                                                                                                                    |                                                                                                                                                                                                                              |
| `other_income`                                                                                                                                                                                                               | *Optional[float]*                                                                                                                                                                                                            | :heavy_minus_sign:                                                                                                                                                                                                           | Other income amount.                                                                                                                                                                                                         |                                                                                                                                                                                                                              |
| `deductions`                                                                                                                                                                                                                 | *Optional[float]*                                                                                                                                                                                                            | :heavy_minus_sign:                                                                                                                                                                                                           | Deductions other than the standard deduction to reduce withholding.                                                                                                                                                          |                                                                                                                                                                                                                              |
| `extra_withholding`                                                                                                                                                                                                          | *Optional[float]*                                                                                                                                                                                                            | :heavy_minus_sign:                                                                                                                                                                                                           | Additional amount to be withheld from each paycheck.                                                                                                                                                                         |                                                                                                                                                                                                                              |
| `federal_withholding_allowance`                                                                                                                                                                                              | *Optional[int]*                                                                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                           | Only applicable when w4_data_type is 'pre_2020_w4' (pre-2020 W4 forms are deprecated for updates).                                                                                                                           |                                                                                                                                                                                                                              |
| `additional_withholding`                                                                                                                                                                                                     | *Optional[float]*                                                                                                                                                                                                            | :heavy_minus_sign:                                                                                                                                                                                                           | Only applicable when w4_data_type is 'pre_2020_w4' (pre-2020 W4 forms are deprecated for updates).                                                                                                                           |                                                                                                                                                                                                                              |
| `retries`                                                                                                                                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                           | Configuration to override the default retry behavior of the client.                                                                                                                                                          |                                                                                                                                                                                                                              |

### Response

**[models.EmployeeFederalTax](../../models/employeefederaltax.md)**

### Errors

| Error Type                       | Status Code                      | Content Type                     |
| -------------------------------- | -------------------------------- | -------------------------------- |
| models.NotFoundErrorObjectError  | 404                              | application/json                 |
| models.UnprocessableEntityError1 | 409, 422                         | application/json                 |
| models.APIError                  | 4XX, 5XX                         | \*/\*                            |

## get_state_taxes

Get attributes relevant for an employee's state taxes.

The data required to correctly calculate an employee's state taxes varies by both home and work location. This API returns information about each question that must be answered grouped by state. Mostly commonly, an employee lives and works in the same state and will only have questions for a single state. The response contains metadata about each question, the type of answer expected, and the current answer stored in Gusto for that question.

Answers are represented by an array. Today, this array can only be empty or contain exactly one element, but is designed to allow for forward compatibility with effective-dated fields. The `valid_from` and `valid_up_to` fields are optional and currently ignored.

## About filing new hire reports
Payroll Admins are responsible for filing a new hire report for each Employee. The `file_new_hire_report` question will only be listed if:
- the `employee.onboarding_status` is one of the following:
  - `admin_onboarding_incomplete`
  - `self_onboarding_awaiting_admin_review`
- that employee's work state requires filing a new hire report

scope: `employee_state_taxes:read`

### Example Usage

<!-- UsageSnippet language="python" operationID="get-v1-employees-employee_id-state_taxes" method="get" path="/v1/employees/{employee_uuid}/state_taxes" -->
```python
import gusto_embedded
from gusto_embedded import Gusto
import os


with Gusto(
    company_access_auth=os.getenv("GUSTO_COMPANY_ACCESS_AUTH", ""),
) as gusto:

    res = gusto.employee_tax_setup.get_state_taxes(employee_uuid="<id>", x_gusto_api_version=gusto_embedded.GetV1EmployeesEmployeeIDStateTaxesHeaderXGustoAPIVersion.TWO_THOUSAND_AND_TWENTY_FIVE_MINUS_06_MINUS_15)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                    | Type                                                                                                                                                                                                                         | Required                                                                                                                                                                                                                     | Description                                                                                                                                                                                                                  |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `employee_uuid`                                                                                                                                                                                                              | *str*                                                                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                                           | The UUID of the employee                                                                                                                                                                                                     |
| `x_gusto_api_version`                                                                                                                                                                                                        | [Optional[models.GetV1EmployeesEmployeeIDStateTaxesHeaderXGustoAPIVersion]](../../models/getv1employeesemployeeidstatetaxesheaderxgustoapiversion.md)                                                                        | :heavy_minus_sign:                                                                                                                                                                                                           | Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used. |
| `retries`                                                                                                                                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                           | Configuration to override the default retry behavior of the client.                                                                                                                                                          |

### Response

**[List[models.EmployeeStateTaxesList]](../../models/.md)**

### Errors

| Error Type                      | Status Code                     | Content Type                    |
| ------------------------------- | ------------------------------- | ------------------------------- |
| models.NotFoundErrorObjectError | 404                             | application/json                |
| models.APIError                 | 4XX, 5XX                        | \*/\*                           |

## update_state_taxes

Update attributes relevant for an employee's state taxes.

As described for the GET endpoint, the answers must be supplied in the effective-dated format, but currently only a single answer will be accepted. The `valid_from` and `valid_up_to` fields are optional and currently ignored.

scope: `employee_state_taxes:write`

### Example Usage

<!-- UsageSnippet language="python" operationID="put-v1-employees-employee_id-state_taxes" method="put" path="/v1/employees/{employee_uuid}/state_taxes" -->
```python
import gusto_embedded
from gusto_embedded import Gusto
import os


with Gusto(
    company_access_auth=os.getenv("GUSTO_COMPANY_ACCESS_AUTH", ""),
) as gusto:

    res = gusto.employee_tax_setup.update_state_taxes(employee_uuid="<id>", states=[], x_gusto_api_version=gusto_embedded.PutV1EmployeesEmployeeIDStateTaxesHeaderXGustoAPIVersion.TWO_THOUSAND_AND_TWENTY_FIVE_MINUS_06_MINUS_15)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                    | Type                                                                                                                                                                                                                         | Required                                                                                                                                                                                                                     | Description                                                                                                                                                                                                                  |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `employee_uuid`                                                                                                                                                                                                              | *str*                                                                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                                           | The UUID of the employee                                                                                                                                                                                                     |
| `states`                                                                                                                                                                                                                     | List[[models.States](../../models/states.md)]                                                                                                                                                                                | :heavy_check_mark:                                                                                                                                                                                                           | N/A                                                                                                                                                                                                                          |
| `x_gusto_api_version`                                                                                                                                                                                                        | [Optional[models.PutV1EmployeesEmployeeIDStateTaxesHeaderXGustoAPIVersion]](../../models/putv1employeesemployeeidstatetaxesheaderxgustoapiversion.md)                                                                        | :heavy_minus_sign:                                                                                                                                                                                                           | Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used. |
| `retries`                                                                                                                                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                           | Configuration to override the default retry behavior of the client.                                                                                                                                                          |

### Response

**[List[models.EmployeeStateTaxesList]](../../models/.md)**

### Errors

| Error Type                       | Status Code                      | Content Type                     |
| -------------------------------- | -------------------------------- | -------------------------------- |
| models.NotFoundErrorObjectError  | 404                              | application/json                 |
| models.UnprocessableEntityError1 | 422                              | application/json                 |
| models.APIError                  | 4XX, 5XX                         | \*/\*                            |