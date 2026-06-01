# ContractorPaymentMethods

## Overview

### Available Operations

* [create_bank_account](#create_bank_account) - Create a contractor bank account

## create_bank_account

Creates a contractor bank account.

Note: We currently only support one bank account per contractor. Using this endpoint on a contractor who already has a bank account will just replace it.

scope: `contractor_payment_methods:write`

### Example Usage

<!-- UsageSnippet language="python" operationID="post-v1-contractors-contractor_uuid-bank_accounts" method="post" path="/v1/contractors/{contractor_uuid}/bank_accounts" -->
```python
import gusto_embedded_v_2026_06_15
from gusto_embedded_v_2026_06_15 import Gusto
import os


with Gusto(
    company_access_auth=os.getenv("GUSTO_COMPANY_ACCESS_AUTH", ""),
) as gusto:

    res = gusto.contractor_payment_methods.create_bank_account(contractor_uuid="<id>", name="<value>", routing_number="<value>", account_number="<value>", account_type=gusto_embedded_v_2026_06_15.ContractorBankAccountCreateRequestBodyAccountType.SAVINGS, x_gusto_api_version=gusto_embedded_v_2026_06_15.PostV1ContractorsContractorUUIDBankAccountsHeaderXGustoAPIVersion.TWO_THOUSAND_AND_TWENTY_SIX_MINUS_06_MINUS_15)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                    | Type                                                                                                                                                                                                                         | Required                                                                                                                                                                                                                     | Description                                                                                                                                                                                                                  |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `contractor_uuid`                                                                                                                                                                                                            | *str*                                                                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                                           | The UUID of the contractor                                                                                                                                                                                                   |
| `name`                                                                                                                                                                                                                       | *str*                                                                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                                           | Name for the bank account                                                                                                                                                                                                    |
| `routing_number`                                                                                                                                                                                                             | *str*                                                                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                                           | The bank account's routing number                                                                                                                                                                                            |
| `account_number`                                                                                                                                                                                                             | *str*                                                                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                                           | The bank account's account number                                                                                                                                                                                            |
| `account_type`                                                                                                                                                                                                               | [models.ContractorBankAccountCreateRequestBodyAccountType](../../models/contractorbankaccountcreaterequestbodyaccounttype.md)                                                                                                | :heavy_check_mark:                                                                                                                                                                                                           | Bank account type                                                                                                                                                                                                            |
| `x_gusto_api_version`                                                                                                                                                                                                        | [Optional[models.PostV1ContractorsContractorUUIDBankAccountsHeaderXGustoAPIVersion]](../../models/postv1contractorscontractoruuidbankaccountsheaderxgustoapiversion.md)                                                      | :heavy_minus_sign:                                                                                                                                                                                                           | Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used. |
| `retries`                                                                                                                                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                           | Configuration to override the default retry behavior of the client.                                                                                                                                                          |

### Response

**[models.ContractorBankAccount](../../models/contractorbankaccount.md)**

### Errors

| Error Type                       | Status Code                      | Content Type                     |
| -------------------------------- | -------------------------------- | -------------------------------- |
| models.NotFoundErrorObject       | 404                              | application/json                 |
| models.UnprocessableEntityError1 | 422                              | application/json                 |
| models.APIError                  | 4XX, 5XX                         | \*/\*                            |