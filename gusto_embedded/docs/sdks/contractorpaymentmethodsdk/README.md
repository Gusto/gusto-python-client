# ContractorPaymentMethod

## Overview

### Available Operations

* [get_bank_accounts](#get_bank_accounts) - Get all contractor bank accounts
* [get](#get) - Get a contractor's payment method
* [update](#update) - Update a contractor's payment method

## get_bank_accounts

Returns all contractor bank accounts.

scope: `contractor_payment_methods:read`

### Example Usage

<!-- UsageSnippet language="python" operationID="get-v1-contractors-contractor_uuid-bank_accounts" method="get" path="/v1/contractors/{contractor_uuid}/bank_accounts" -->
```python
import gusto_embedded
from gusto_embedded import Gusto
import os


with Gusto(
    company_access_auth=os.getenv("GUSTO_COMPANY_ACCESS_AUTH", ""),
) as gusto:

    res = gusto.contractor_payment_method.get_bank_accounts(contractor_uuid="<id>", x_gusto_api_version=gusto_embedded.GetV1ContractorsContractorUUIDBankAccountsHeaderXGustoAPIVersion.TWO_THOUSAND_AND_TWENTY_FIVE_MINUS_06_MINUS_15)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                    | Type                                                                                                                                                                                                                         | Required                                                                                                                                                                                                                     | Description                                                                                                                                                                                                                  |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `contractor_uuid`                                                                                                                                                                                                            | *str*                                                                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                                           | The UUID of the contractor                                                                                                                                                                                                   |
| `x_gusto_api_version`                                                                                                                                                                                                        | [Optional[models.GetV1ContractorsContractorUUIDBankAccountsHeaderXGustoAPIVersion]](../../models/getv1contractorscontractoruuidbankaccountsheaderxgustoapiversion.md)                                                        | :heavy_minus_sign:                                                                                                                                                                                                           | Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used. |
| `retries`                                                                                                                                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                           | Configuration to override the default retry behavior of the client.                                                                                                                                                          |

### Response

**[List[models.ContractorBankAccount]](../../models/.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.NotFoundErrorObject | 404                        | application/json           |
| models.APIError            | 4XX, 5XX                   | \*/\*                      |

## get

Fetches a contractor's payment method. A contractor payment method
describes how the payment should be split across the contractor's associated
bank accounts.

scope: `contractor_payment_methods:read`

### Example Usage

<!-- UsageSnippet language="python" operationID="get-v1-contractors-contractor_uuid-payment_method" method="get" path="/v1/contractors/{contractor_uuid}/payment_method" -->
```python
import gusto_embedded
from gusto_embedded import Gusto
import os


with Gusto(
    company_access_auth=os.getenv("GUSTO_COMPANY_ACCESS_AUTH", ""),
) as gusto:

    res = gusto.contractor_payment_method.get(contractor_uuid="<id>", x_gusto_api_version=gusto_embedded.GetV1ContractorsContractorUUIDPaymentMethodHeaderXGustoAPIVersion.TWO_THOUSAND_AND_TWENTY_FIVE_MINUS_06_MINUS_15)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                    | Type                                                                                                                                                                                                                         | Required                                                                                                                                                                                                                     | Description                                                                                                                                                                                                                  |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `contractor_uuid`                                                                                                                                                                                                            | *str*                                                                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                                           | The UUID of the contractor                                                                                                                                                                                                   |
| `x_gusto_api_version`                                                                                                                                                                                                        | [Optional[models.GetV1ContractorsContractorUUIDPaymentMethodHeaderXGustoAPIVersion]](../../models/getv1contractorscontractoruuidpaymentmethodheaderxgustoapiversion.md)                                                      | :heavy_minus_sign:                                                                                                                                                                                                           | Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used. |
| `retries`                                                                                                                                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                           | Configuration to override the default retry behavior of the client.                                                                                                                                                          |

### Response

**[models.ContractorPaymentMethod](../../models/contractorpaymentmethod.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.NotFoundErrorObject | 404                        | application/json           |
| models.APIError            | 4XX, 5XX                   | \*/\*                      |

## update

Updates a contractor's payment method. Note that creating a contractor
bank account will also update the contractor's payment method.

scope: `contractor_payment_methods:write`

### Example Usage

<!-- UsageSnippet language="python" operationID="put-v1-contractors-contractor_id-payment_method" method="put" path="/v1/contractors/{contractor_uuid}/payment_method" -->
```python
import gusto_embedded
from gusto_embedded import Gusto
import os


with Gusto(
    company_access_auth=os.getenv("GUSTO_COMPANY_ACCESS_AUTH", ""),
) as gusto:

    res = gusto.contractor_payment_method.update(contractor_uuid="<id>", version="63859768485e218ccf8a449bb60f14ed", type_=gusto_embedded.PutV1ContractorsContractorIDPaymentMethodType.DIRECT_DEPOSIT, x_gusto_api_version=gusto_embedded.PutV1ContractorsContractorIDPaymentMethodHeaderXGustoAPIVersion.TWO_THOUSAND_AND_TWENTY_FIVE_MINUS_06_MINUS_15)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                    | Type                                                                                                                                                                                                                         | Required                                                                                                                                                                                                                     | Description                                                                                                                                                                                                                  | Example                                                                                                                                                                                                                      |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `contractor_uuid`                                                                                                                                                                                                            | *str*                                                                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                                           | The UUID of the contractor                                                                                                                                                                                                   |                                                                                                                                                                                                                              |
| `version`                                                                                                                                                                                                                    | *str*                                                                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                                           | The current version of the object. See the [versioning guide](https://docs.gusto.com/embedded-payroll/docs/idempotency) for information on how to use this field.                                                            | 63859768485e218ccf8a449bb60f14ed                                                                                                                                                                                             |
| `type`                                                                                                                                                                                                                       | [models.PutV1ContractorsContractorIDPaymentMethodType](../../models/putv1contractorscontractoridpaymentmethodtype.md)                                                                                                        | :heavy_check_mark:                                                                                                                                                                                                           | The payment method type. If type is Direct Deposit, the contractor is required to have a bank account. See [Bank account endpoint](./post-v1-contractors-contractor_uuid-bank_accounts).                                     |                                                                                                                                                                                                                              |
| `x_gusto_api_version`                                                                                                                                                                                                        | [Optional[models.PutV1ContractorsContractorIDPaymentMethodHeaderXGustoAPIVersion]](../../models/putv1contractorscontractoridpaymentmethodheaderxgustoapiversion.md)                                                          | :heavy_minus_sign:                                                                                                                                                                                                           | Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used. |                                                                                                                                                                                                                              |
| `retries`                                                                                                                                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                           | Configuration to override the default retry behavior of the client.                                                                                                                                                          |                                                                                                                                                                                                                              |

### Response

**[models.ContractorPaymentMethod](../../models/contractorpaymentmethod.md)**

### Errors

| Error Type                       | Status Code                      | Content Type                     |
| -------------------------------- | -------------------------------- | -------------------------------- |
| models.NotFoundErrorObject       | 404                              | application/json                 |
| models.ConflictErrorObject       | 409                              | application/json                 |
| models.UnprocessableEntityError1 | 422                              | application/json                 |
| models.APIError                  | 4XX, 5XX                         | \*/\*                            |