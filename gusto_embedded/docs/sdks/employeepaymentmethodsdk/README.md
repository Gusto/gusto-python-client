# EmployeePaymentMethod

## Overview

### Available Operations

* [create](#create) - Create an employee bank account
* [update_bank_account](#update_bank_account) - Update an employee bank account
* [delete_bank_account](#delete_bank_account) - Delete an employee bank account
* [get](#get) - Get payment method for an employee
* [update](#update) - Update payment method for an employee

## create

Creates an employee bank account. An employee can have multiple bank accounts. Note that creating an employee bank account will also update the employee's payment method.

scope: `employee_payment_methods:write`

### Example Usage

<!-- UsageSnippet language="python" operationID="post-v1-employees-employee_id-bank_accounts" method="post" path="/v1/employees/{employee_id}/bank_accounts" -->
```python
import gusto_embedded
from gusto_embedded import Gusto
import os


with Gusto(
    company_access_auth=os.getenv("GUSTO_COMPANY_ACCESS_AUTH", ""),
) as gusto:

    res = gusto.employee_payment_method.create(employee_id="<id>", routing_number="266905059", account_number="5809431207", account_type=gusto_embedded.EmployeeBankAccountRequestAccountType.CHECKING, name="BoA Checking Account", x_gusto_api_version=gusto_embedded.PostV1EmployeesEmployeeIDBankAccountsHeaderXGustoAPIVersion.TWO_THOUSAND_AND_TWENTY_FIVE_MINUS_06_MINUS_15)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                    | Type                                                                                                                                                                                                                         | Required                                                                                                                                                                                                                     | Description                                                                                                                                                                                                                  | Example                                                                                                                                                                                                                      |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `employee_id`                                                                                                                                                                                                                | *str*                                                                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                                           | The UUID of the employee                                                                                                                                                                                                     |                                                                                                                                                                                                                              |
| `routing_number`                                                                                                                                                                                                             | *str*                                                                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                                           | The bank routing number (nine digits).                                                                                                                                                                                       | 266905059                                                                                                                                                                                                                    |
| `account_number`                                                                                                                                                                                                             | *str*                                                                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                                           | The bank account number.                                                                                                                                                                                                     | 5809431207                                                                                                                                                                                                                   |
| `account_type`                                                                                                                                                                                                               | [models.EmployeeBankAccountRequestAccountType](../../models/employeebankaccountrequestaccounttype.md)                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                                           | The bank account type.                                                                                                                                                                                                       | Checking                                                                                                                                                                                                                     |
| `name`                                                                                                                                                                                                                       | *str*                                                                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                                           | A name for the bank account (e.g. "Primary Checking").                                                                                                                                                                       | BoA Checking Account                                                                                                                                                                                                         |
| `x_gusto_api_version`                                                                                                                                                                                                        | [Optional[models.PostV1EmployeesEmployeeIDBankAccountsHeaderXGustoAPIVersion]](../../models/postv1employeesemployeeidbankaccountsheaderxgustoapiversion.md)                                                                  | :heavy_minus_sign:                                                                                                                                                                                                           | Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used. |                                                                                                                                                                                                                              |
| `retries`                                                                                                                                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                           | Configuration to override the default retry behavior of the client.                                                                                                                                                          |                                                                                                                                                                                                                              |

### Response

**[models.EmployeeBankAccount](../../models/employeebankaccount.md)**

### Errors

| Error Type                       | Status Code                      | Content Type                     |
| -------------------------------- | -------------------------------- | -------------------------------- |
| models.NotFoundErrorObject       | 404                              | application/json                 |
| models.UnprocessableEntityError1 | 422                              | application/json                 |
| models.APIError                  | 4XX, 5XX                         | \*/\*                            |

## update_bank_account

Updates an employee bank account.

scope: `employee_payment_methods:write`

### Example Usage

<!-- UsageSnippet language="python" operationID="put-v1-employees-employee_id-bank_accounts" method="put" path="/v1/employees/{employee_id}/bank_accounts/{bank_account_uuid}" -->
```python
import gusto_embedded
from gusto_embedded import Gusto
import os


with Gusto(
    company_access_auth=os.getenv("GUSTO_COMPANY_ACCESS_AUTH", ""),
) as gusto:

    res = gusto.employee_payment_method.update_bank_account(employee_id="<id>", bank_account_uuid="<id>", routing_number="266905059", account_number="5809431207", account_type=gusto_embedded.EmployeeBankAccountRequestAccountType.CHECKING, name="BoA Checking Account", x_gusto_api_version=gusto_embedded.PutV1EmployeesEmployeeIDBankAccountsHeaderXGustoAPIVersion.TWO_THOUSAND_AND_TWENTY_FIVE_MINUS_06_MINUS_15)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                    | Type                                                                                                                                                                                                                         | Required                                                                                                                                                                                                                     | Description                                                                                                                                                                                                                  | Example                                                                                                                                                                                                                      |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `employee_id`                                                                                                                                                                                                                | *str*                                                                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                                           | The UUID of the employee                                                                                                                                                                                                     |                                                                                                                                                                                                                              |
| `bank_account_uuid`                                                                                                                                                                                                          | *str*                                                                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                                           | The UUID of the bank account                                                                                                                                                                                                 |                                                                                                                                                                                                                              |
| `routing_number`                                                                                                                                                                                                             | *str*                                                                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                                           | The bank routing number (nine digits).                                                                                                                                                                                       | 266905059                                                                                                                                                                                                                    |
| `account_number`                                                                                                                                                                                                             | *str*                                                                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                                           | The bank account number.                                                                                                                                                                                                     | 5809431207                                                                                                                                                                                                                   |
| `account_type`                                                                                                                                                                                                               | [models.EmployeeBankAccountRequestAccountType](../../models/employeebankaccountrequestaccounttype.md)                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                                           | The bank account type.                                                                                                                                                                                                       | Checking                                                                                                                                                                                                                     |
| `name`                                                                                                                                                                                                                       | *str*                                                                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                                           | A name for the bank account (e.g. "Primary Checking").                                                                                                                                                                       | BoA Checking Account                                                                                                                                                                                                         |
| `x_gusto_api_version`                                                                                                                                                                                                        | [Optional[models.PutV1EmployeesEmployeeIDBankAccountsHeaderXGustoAPIVersion]](../../models/putv1employeesemployeeidbankaccountsheaderxgustoapiversion.md)                                                                    | :heavy_minus_sign:                                                                                                                                                                                                           | Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used. |                                                                                                                                                                                                                              |
| `retries`                                                                                                                                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                           | Configuration to override the default retry behavior of the client.                                                                                                                                                          |                                                                                                                                                                                                                              |

### Response

**[models.EmployeeBankAccount](../../models/employeebankaccount.md)**

### Errors

| Error Type                       | Status Code                      | Content Type                     |
| -------------------------------- | -------------------------------- | -------------------------------- |
| models.NotFoundErrorObject       | 404                              | application/json                 |
| models.UnprocessableEntityError1 | 422                              | application/json                 |
| models.APIError                  | 4XX, 5XX                         | \*/\*                            |

## delete_bank_account

Deletes an employee bank account. To update an employee's bank account details, delete the bank account first and create a new one.

scope: `employee_payment_methods:write`

### Example Usage

<!-- UsageSnippet language="python" operationID="delete-v1-employees-employee_id-bank_accounts-bank_account_id" method="delete" path="/v1/employees/{employee_id}/bank_accounts/{bank_account_uuid}" -->
```python
import gusto_embedded
from gusto_embedded import Gusto
import os


with Gusto(
    company_access_auth=os.getenv("GUSTO_COMPANY_ACCESS_AUTH", ""),
) as gusto:

    gusto.employee_payment_method.delete_bank_account(employee_id="<id>", bank_account_uuid="<id>", x_gusto_api_version=gusto_embedded.DeleteV1EmployeesEmployeeIDBankAccountsBankAccountIDHeaderXGustoAPIVersion.TWO_THOUSAND_AND_TWENTY_FIVE_MINUS_06_MINUS_15)

    # Use the SDK ...

```

### Parameters

| Parameter                                                                                                                                                                                                                    | Type                                                                                                                                                                                                                         | Required                                                                                                                                                                                                                     | Description                                                                                                                                                                                                                  |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `employee_id`                                                                                                                                                                                                                | *str*                                                                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                                           | The UUID of the employee                                                                                                                                                                                                     |
| `bank_account_uuid`                                                                                                                                                                                                          | *str*                                                                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                                           | The UUID of the bank account                                                                                                                                                                                                 |
| `x_gusto_api_version`                                                                                                                                                                                                        | [Optional[models.DeleteV1EmployeesEmployeeIDBankAccountsBankAccountIDHeaderXGustoAPIVersion]](../../models/deletev1employeesemployeeidbankaccountsbankaccountidheaderxgustoapiversion.md)                                    | :heavy_minus_sign:                                                                                                                                                                                                           | Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used. |
| `retries`                                                                                                                                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                           | Configuration to override the default retry behavior of the client.                                                                                                                                                          |

### Errors

| Error Type                       | Status Code                      | Content Type                     |
| -------------------------------- | -------------------------------- | -------------------------------- |
| models.NotFoundErrorObject       | 404                              | application/json                 |
| models.UnprocessableEntityError1 | 422                              | application/json                 |
| models.APIError                  | 4XX, 5XX                         | \*/\*                            |

## get

Returns the payment method for an employee (e.g. Check or Direct Deposit with split configuration).

scope: `employee_payment_methods:read`

### Example Usage

<!-- UsageSnippet language="python" operationID="get-v1-employees-employee_id-payment_method" method="get" path="/v1/employees/{employee_id}/payment_method" -->
```python
import gusto_embedded
from gusto_embedded import Gusto
import os


with Gusto(
    company_access_auth=os.getenv("GUSTO_COMPANY_ACCESS_AUTH", ""),
) as gusto:

    res = gusto.employee_payment_method.get(employee_id="<id>", x_gusto_api_version=gusto_embedded.GetV1EmployeesEmployeeIDPaymentMethodHeaderXGustoAPIVersion.TWO_THOUSAND_AND_TWENTY_FIVE_MINUS_06_MINUS_15)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                    | Type                                                                                                                                                                                                                         | Required                                                                                                                                                                                                                     | Description                                                                                                                                                                                                                  |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `employee_id`                                                                                                                                                                                                                | *str*                                                                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                                           | The UUID of the employee                                                                                                                                                                                                     |
| `x_gusto_api_version`                                                                                                                                                                                                        | [Optional[models.GetV1EmployeesEmployeeIDPaymentMethodHeaderXGustoAPIVersion]](../../models/getv1employeesemployeeidpaymentmethodheaderxgustoapiversion.md)                                                                  | :heavy_minus_sign:                                                                                                                                                                                                           | Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used. |
| `retries`                                                                                                                                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                           | Configuration to override the default retry behavior of the client.                                                                                                                                                          |

### Response

**[models.EmployeePaymentMethod](../../models/employeepaymentmethod.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.NotFoundErrorObject | 404                        | application/json           |
| models.APIError            | 4XX, 5XX                   | \*/\*                      |

## update

Updates the payment method for an employee. Can set to Check or Direct Deposit with split configuration.

scope: `employee_payment_methods:write`

### Example Usage

<!-- UsageSnippet language="python" operationID="put-v1-employees-employee_id-payment_method" method="put" path="/v1/employees/{employee_id}/payment_method" -->
```python
import gusto_embedded
from gusto_embedded import Gusto
import os


with Gusto(
    company_access_auth=os.getenv("GUSTO_COMPANY_ACCESS_AUTH", ""),
) as gusto:

    res = gusto.employee_payment_method.update(employee_id="<id>", version="63859768485e218ccf8a449bb60f14ed", type_=gusto_embedded.PutV1EmployeesEmployeeIDPaymentMethodType.CHECK, x_gusto_api_version=gusto_embedded.PutV1EmployeesEmployeeIDPaymentMethodHeaderXGustoAPIVersion.TWO_THOUSAND_AND_TWENTY_FIVE_MINUS_06_MINUS_15)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                    | Type                                                                                                                                                                                                                         | Required                                                                                                                                                                                                                     | Description                                                                                                                                                                                                                  | Example                                                                                                                                                                                                                      |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `employee_id`                                                                                                                                                                                                                | *str*                                                                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                                           | The UUID of the employee                                                                                                                                                                                                     |                                                                                                                                                                                                                              |
| `version`                                                                                                                                                                                                                    | *str*                                                                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                                           | The current version of the object. See the [versioning guide](https://docs.gusto.com/embedded-payroll/docs/versioning#object-layer) for information on how to use this field.                                                | 63859768485e218ccf8a449bb60f14ed                                                                                                                                                                                             |
| `type`                                                                                                                                                                                                                       | [models.PutV1EmployeesEmployeeIDPaymentMethodType](../../models/putv1employeesemployeeidpaymentmethodtype.md)                                                                                                                | :heavy_check_mark:                                                                                                                                                                                                           | The payment method type. If type is Check, split_by and splits do not need to be populated. If type is Direct Deposit, split_by and splits are required.                                                                     |                                                                                                                                                                                                                              |
| `x_gusto_api_version`                                                                                                                                                                                                        | [Optional[models.PutV1EmployeesEmployeeIDPaymentMethodHeaderXGustoAPIVersion]](../../models/putv1employeesemployeeidpaymentmethodheaderxgustoapiversion.md)                                                                  | :heavy_minus_sign:                                                                                                                                                                                                           | Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used. |                                                                                                                                                                                                                              |
| `split_by`                                                                                                                                                                                                                   | [OptionalNullable[models.PutV1EmployeesEmployeeIDPaymentMethodSplitBy]](../../models/putv1employeesemployeeidpaymentmethodsplitby.md)                                                                                        | :heavy_minus_sign:                                                                                                                                                                                                           | How the payment will be split. If Percentage, split amounts must add up to exactly 100. If Amount, values are in cents and the last split amount must be null to capture the remainder.                                      |                                                                                                                                                                                                                              |
| `splits`                                                                                                                                                                                                                     | List[[models.PutV1EmployeesEmployeeIDPaymentMethodSplits](../../models/putv1employeesemployeeidpaymentmethodsplits.md)]                                                                                                      | :heavy_minus_sign:                                                                                                                                                                                                           | Array of payment splits. Required when type is Direct Deposit.                                                                                                                                                               |                                                                                                                                                                                                                              |
| `retries`                                                                                                                                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                           | Configuration to override the default retry behavior of the client.                                                                                                                                                          |                                                                                                                                                                                                                              |

### Response

**[models.EmployeePaymentMethod](../../models/employeepaymentmethod.md)**

### Errors

| Error Type                       | Status Code                      | Content Type                     |
| -------------------------------- | -------------------------------- | -------------------------------- |
| models.NotFoundErrorObject       | 404                              | application/json                 |
| models.UnprocessableEntityError1 | 409, 422                         | application/json                 |
| models.APIError                  | 4XX, 5XX                         | \*/\*                            |