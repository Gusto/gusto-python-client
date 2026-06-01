# BankAccounts

## Overview

### Available Operations

* [get](#get) - Get all company bank accounts
* [create](#create) - Create a company bank account
* [verify](#verify) - Verify a company bank account
* [create_from_plaid_token](#create_from_plaid_token) - Create a bank account from a plaid processor token
* [delete_v1_companies_company_id_bank_accounts_bank_account_id](#delete_v1_companies_company_id_bank_accounts_bank_account_id) - Delete a company bank account

## get

Returns company bank accounts. Currently, we only support a single default bank account per company.

scope: `company_bank_accounts:read`

### Example Usage

<!-- UsageSnippet language="python" operationID="get-v1-companies-company_id-bank-accounts" method="get" path="/v1/companies/{company_id}/bank_accounts" -->
```python
import gusto_embedded
from gusto_embedded import Gusto
import os


with Gusto(
    company_access_auth=os.getenv("GUSTO_COMPANY_ACCESS_AUTH", ""),
) as gusto:

    res = gusto.bank_accounts.get(company_id="<id>", x_gusto_api_version=gusto_embedded.GetV1CompaniesCompanyIDBankAccountsHeaderXGustoAPIVersion.TWO_THOUSAND_AND_TWENTY_FIVE_MINUS_06_MINUS_15)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                    | Type                                                                                                                                                                                                                         | Required                                                                                                                                                                                                                     | Description                                                                                                                                                                                                                  |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `company_id`                                                                                                                                                                                                                 | *str*                                                                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                                           | The UUID of the company                                                                                                                                                                                                      |
| `x_gusto_api_version`                                                                                                                                                                                                        | [Optional[models.GetV1CompaniesCompanyIDBankAccountsHeaderXGustoAPIVersion]](../../models/getv1companiescompanyidbankaccountsheaderxgustoapiversion.md)                                                                      | :heavy_minus_sign:                                                                                                                                                                                                           | Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used. |
| `retries`                                                                                                                                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                           | Configuration to override the default retry behavior of the client.                                                                                                                                                          |

### Response

**[List[models.CompanyBankAccount]](../../models/.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.NotFoundErrorObject | 404                        | application/json           |
| models.APIError            | 4XX, 5XX                   | \*/\*                      |

## create

This endpoint creates a new company bank account.

Upon being created, two verification deposits are automatically sent to the bank account, and the bank account's verification_status is 'awaiting_deposits'.

When the deposits are successfully transferred, the verification_status changes to 'ready_for_verification', at which point the verify endpoint can be used to verify the bank account.
After successful verification, the bank account's verification_status is 'verified'.


>🚧 Warning
>
> If a default bank account exists, it will be disabled and the new bank account will replace it as the company's default funding method.

scope: `company_bank_accounts:write`

### Example Usage

<!-- UsageSnippet language="python" operationID="post-v1-companies-company_id-bank-accounts" method="post" path="/v1/companies/{company_id}/bank_accounts" -->
```python
import gusto_embedded
from gusto_embedded import Gusto
import os


with Gusto(
    company_access_auth=os.getenv("GUSTO_COMPANY_ACCESS_AUTH", ""),
) as gusto:

    res = gusto.bank_accounts.create(company_id="<id>", routing_number="<value>", account_number="<value>", account_type=gusto_embedded.CompanyBankAccountRequestAccountType.SAVINGS, x_gusto_api_version=gusto_embedded.PostV1CompaniesCompanyIDBankAccountsHeaderXGustoAPIVersion.TWO_THOUSAND_AND_TWENTY_FIVE_MINUS_06_MINUS_15)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                    | Type                                                                                                                                                                                                                         | Required                                                                                                                                                                                                                     | Description                                                                                                                                                                                                                  |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `company_id`                                                                                                                                                                                                                 | *str*                                                                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                                           | The UUID of the company                                                                                                                                                                                                      |
| `routing_number`                                                                                                                                                                                                             | *str*                                                                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                                           | The bank routing number                                                                                                                                                                                                      |
| `account_number`                                                                                                                                                                                                             | *str*                                                                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                                           | The bank account number                                                                                                                                                                                                      |
| `account_type`                                                                                                                                                                                                               | [models.CompanyBankAccountRequestAccountType](../../models/companybankaccountrequestaccounttype.md)                                                                                                                          | :heavy_check_mark:                                                                                                                                                                                                           | The bank account type                                                                                                                                                                                                        |
| `x_gusto_api_version`                                                                                                                                                                                                        | [Optional[models.PostV1CompaniesCompanyIDBankAccountsHeaderXGustoAPIVersion]](../../models/postv1companiescompanyidbankaccountsheaderxgustoapiversion.md)                                                                    | :heavy_minus_sign:                                                                                                                                                                                                           | Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used. |
| `retries`                                                                                                                                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                           | Configuration to override the default retry behavior of the client.                                                                                                                                                          |

### Response

**[models.CompanyBankAccount](../../models/companybankaccount.md)**

### Errors

| Error Type                       | Status Code                      | Content Type                     |
| -------------------------------- | -------------------------------- | -------------------------------- |
| models.NotFoundErrorObject       | 404                              | application/json                 |
| models.UnprocessableEntityError1 | 422                              | application/json                 |
| models.APIError                  | 4XX, 5XX                         | \*/\*                            |

## verify

Verify a company bank account by confirming the two micro-deposits sent to the bank account.

Note that the order of the two deposits specified in request parameters does not matter.
There's a maximum of 5 verification attempts, after which we will automatically initiate a new set of micro-deposits and require the bank account to be verified with the new micro-deposits.

### Bank account verification in demo
In the demo environment, use the `POST /v1/companies/{company_id}/bank_accounts/{bank_account_uuid}/send_test_deposits` endpoint to simulate the micro-deposits transfer and return the two amounts in the response. You can call this endpoint as many times as you wish to retrieve the values of the two micro-deposits.

### Webhooks
- `company.bank_account.verified`: Fires when the company bank account is successfully verified.

### Related guides
- [Manage company bank accounts](doc:manage-company-bank-accounts)
- [Bank Account Events](doc:bank-account-events)

scope: `company_bank_accounts:write`

### Example Usage

<!-- UsageSnippet language="python" operationID="put-v1-companies-company_id-bank-accounts-verify" method="put" path="/v1/companies/{company_id}/bank_accounts/{bank_account_uuid}/verify" -->
```python
import gusto_embedded
from gusto_embedded import Gusto
import os


with Gusto(
    company_access_auth=os.getenv("GUSTO_COMPANY_ACCESS_AUTH", ""),
) as gusto:

    res = gusto.bank_accounts.verify(company_id="<id>", bank_account_uuid="<id>", deposit_1=8299.3, deposit_2=7367.9, x_gusto_api_version=gusto_embedded.PutV1CompaniesCompanyIDBankAccountsVerifyHeaderXGustoAPIVersion.TWO_THOUSAND_AND_TWENTY_FIVE_MINUS_06_MINUS_15)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                    | Type                                                                                                                                                                                                                         | Required                                                                                                                                                                                                                     | Description                                                                                                                                                                                                                  |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `company_id`                                                                                                                                                                                                                 | *str*                                                                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                                           | The UUID of the company                                                                                                                                                                                                      |
| `bank_account_uuid`                                                                                                                                                                                                          | *str*                                                                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                                           | The UUID of the company bank account                                                                                                                                                                                         |
| `deposit_1`                                                                                                                                                                                                                  | *float*                                                                                                                                                                                                                      | :heavy_check_mark:                                                                                                                                                                                                           | The first micro-deposit amount (order does not matter).                                                                                                                                                                      |
| `deposit_2`                                                                                                                                                                                                                  | *float*                                                                                                                                                                                                                      | :heavy_check_mark:                                                                                                                                                                                                           | The second micro-deposit amount (order does not matter).                                                                                                                                                                     |
| `x_gusto_api_version`                                                                                                                                                                                                        | [Optional[models.PutV1CompaniesCompanyIDBankAccountsVerifyHeaderXGustoAPIVersion]](../../models/putv1companiescompanyidbankaccountsverifyheaderxgustoapiversion.md)                                                          | :heavy_minus_sign:                                                                                                                                                                                                           | Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used. |
| `retries`                                                                                                                                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                           | Configuration to override the default retry behavior of the client.                                                                                                                                                          |

### Response

**[models.CompanyBankAccount](../../models/companybankaccount.md)**

### Errors

| Error Type                       | Status Code                      | Content Type                     |
| -------------------------------- | -------------------------------- | -------------------------------- |
| models.NotFoundErrorObject       | 404                              | application/json                 |
| models.UnprocessableEntityError1 | 422                              | application/json                 |
| models.APIError                  | 4XX, 5XX                         | \*/\*                            |

## create_from_plaid_token

This endpoint creates a new **verified** bank account by using a plaid processor token to retrieve its information.

> 📘
> To create a token please use the [plaid api](https://plaid.com/docs/api/processors/#processortokencreate) and select "gusto" as processor.

> 🚧 Warning - Company Bank Accounts
>
> If a default company bank account exists, it will be disabled and the new bank account will replace it as the company's default funding method.

scope: `plaid_processor:write`

### Example Usage

<!-- UsageSnippet language="python" operationID="post-v1-plaid-processor_token" method="post" path="/v1/plaid/processor_token" -->
```python
import gusto_embedded
from gusto_embedded import Gusto
import os


with Gusto(
    company_access_auth=os.getenv("GUSTO_COMPANY_ACCESS_AUTH", ""),
) as gusto:

    res = gusto.bank_accounts.create_from_plaid_token(owner_type=gusto_embedded.OwnerType.COMPANY, owner_id="<id>", processor_token="<value>", x_gusto_api_version=gusto_embedded.PostV1PlaidProcessorTokenHeaderXGustoAPIVersion.TWO_THOUSAND_AND_TWENTY_FIVE_MINUS_06_MINUS_15)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                    | Type                                                                                                                                                                                                                         | Required                                                                                                                                                                                                                     | Description                                                                                                                                                                                                                  |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `owner_type`                                                                                                                                                                                                                 | [models.OwnerType](../../models/ownertype.md)                                                                                                                                                                                | :heavy_check_mark:                                                                                                                                                                                                           | The owner type of the bank account                                                                                                                                                                                           |
| `owner_id`                                                                                                                                                                                                                   | *str*                                                                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                                           | The owner UUID of the bank account                                                                                                                                                                                           |
| `processor_token`                                                                                                                                                                                                            | *str*                                                                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                                           | The Plaid processor token                                                                                                                                                                                                    |
| `x_gusto_api_version`                                                                                                                                                                                                        | [Optional[models.PostV1PlaidProcessorTokenHeaderXGustoAPIVersion]](../../models/postv1plaidprocessortokenheaderxgustoapiversion.md)                                                                                          | :heavy_minus_sign:                                                                                                                                                                                                           | Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used. |
| `retries`                                                                                                                                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                           | Configuration to override the default retry behavior of the client.                                                                                                                                                          |

### Response

**[models.CompanyBankAccount](../../models/companybankaccount.md)**

### Errors

| Error Type                       | Status Code                      | Content Type                     |
| -------------------------------- | -------------------------------- | -------------------------------- |
| models.NotFoundErrorObject       | 404                              | application/json                 |
| models.UnprocessableEntityError1 | 422                              | application/json                 |
| models.APIError                  | 4XX, 5XX                         | \*/\*                            |

## delete_v1_companies_company_id_bank_accounts_bank_account_id

This endpoint disables a company bank account.

A bank account cannot be disabled if it is used for any unprocessed payments.

scope: `company_bank_accounts:write`

### Example Usage

<!-- UsageSnippet language="python" operationID="delete-v1-companies-company_id-bank-accounts-bank_account_id" method="delete" path="/v1/companies/{company_id}/bank_accounts/{bank_account_id}" -->
```python
import gusto_embedded
from gusto_embedded import Gusto
import os


with Gusto(
    company_access_auth=os.getenv("GUSTO_COMPANY_ACCESS_AUTH", ""),
) as gusto:

    gusto.bank_accounts.delete_v1_companies_company_id_bank_accounts_bank_account_id(company_id="<id>", bank_account_id="<id>", x_gusto_api_version=gusto_embedded.DeleteV1CompaniesCompanyIDBankAccountsBankAccountIDHeaderXGustoAPIVersion.TWO_THOUSAND_AND_TWENTY_FIVE_MINUS_06_MINUS_15)

    # Use the SDK ...

```

### Parameters

| Parameter                                                                                                                                                                                                                    | Type                                                                                                                                                                                                                         | Required                                                                                                                                                                                                                     | Description                                                                                                                                                                                                                  |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `company_id`                                                                                                                                                                                                                 | *str*                                                                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                                           | The UUID of the company                                                                                                                                                                                                      |
| `bank_account_id`                                                                                                                                                                                                            | *str*                                                                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                                           | The UUID of the company bank account                                                                                                                                                                                         |
| `x_gusto_api_version`                                                                                                                                                                                                        | [Optional[models.DeleteV1CompaniesCompanyIDBankAccountsBankAccountIDHeaderXGustoAPIVersion]](../../models/deletev1companiescompanyidbankaccountsbankaccountidheaderxgustoapiversion.md)                                      | :heavy_minus_sign:                                                                                                                                                                                                           | Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used. |
| `retries`                                                                                                                                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                           | Configuration to override the default retry behavior of the client.                                                                                                                                                          |

### Errors

| Error Type                       | Status Code                      | Content Type                     |
| -------------------------------- | -------------------------------- | -------------------------------- |
| models.NotFoundErrorObject       | 404                              | application/json                 |
| models.UnprocessableEntityError1 | 422                              | application/json                 |
| models.APIError                  | 4XX, 5XX                         | \*/\*                            |