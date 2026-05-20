# ContractorPayments

## Overview

### Available Operations

* [get_receipt](#get_receipt) - Get a single contractor payment receipt
* [fund](#fund) - Fund a contractor payment [DEMO]
* [list](#list) - Get contractor payments for a company
* [create](#create) - Create a contractor payment
* [get](#get) - Get a single contractor payment
* [delete](#delete) - Cancel a contractor payment
* [preview](#preview) - Preview contractor payment debit date
* [get_v1_contractor_payments_contractor_payment_id_pdf](#get_v1_contractor_payments_contractor_payment_id_pdf) - Get a contractor payment PDF

## get_receipt

Returns a contractor payment receipt.

Notes:
* Receipts are only available for direct deposit payments and are only available once those payments have been funded.
* Payroll Receipt requests for payrolls which do not have receipts available (e.g. payment by check) will return a 404 status.
* Hour and dollar amounts are returned as string representations of numeric decimals.
* Dollar amounts are represented to the cent.
* If no data has yet be inserted for a given field, it defaults to “0.00” (for fixed amounts).

scope: `payrolls:read`

### Example Usage

<!-- UsageSnippet language="python" operationID="get-v1-contractor_payments-contractor_payment_uuid-receipt" method="get" path="/v1/contractor_payments/{contractor_payment_uuid}/receipt" -->
```python
import gusto_embedded
from gusto_embedded import Gusto
import os


with Gusto(
    company_access_auth=os.getenv("GUSTO_COMPANY_ACCESS_AUTH", ""),
) as gusto:

    res = gusto.contractor_payments.get_receipt(contractor_payment_uuid="<id>", x_gusto_api_version=gusto_embedded.GetV1ContractorPaymentsContractorPaymentUUIDReceiptHeaderXGustoAPIVersion.TWO_THOUSAND_AND_TWENTY_FIVE_MINUS_06_MINUS_15)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                    | Type                                                                                                                                                                                                                         | Required                                                                                                                                                                                                                     | Description                                                                                                                                                                                                                  |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `contractor_payment_uuid`                                                                                                                                                                                                    | *str*                                                                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                                           | The UUID of the contractor payment                                                                                                                                                                                           |
| `x_gusto_api_version`                                                                                                                                                                                                        | [Optional[models.GetV1ContractorPaymentsContractorPaymentUUIDReceiptHeaderXGustoAPIVersion]](../../models/getv1contractorpaymentscontractorpaymentuuidreceiptheaderxgustoapiversion.md)                                      | :heavy_minus_sign:                                                                                                                                                                                                           | Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used. |
| `retries`                                                                                                                                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                           | Configuration to override the default retry behavior of the client.                                                                                                                                                          |

### Response

**[models.ContractorPaymentReceipt](../../models/contractorpaymentreceipt.md)**

### Errors

| Error Type                      | Status Code                     | Content Type                    |
| ------------------------------- | ------------------------------- | ------------------------------- |
| models.NotFoundErrorObjectError | 404                             | application/json                |
| models.APIError                 | 4XX, 5XX                        | \*/\*                           |

## fund

> 🚧 Demo action
>
> This action is only available in the Demo environment

Simulate funding a contractor payment. Funding only occurs automatically in the production environment when bank transactions are generated. Use this action in the demo environment to transition a contractor payment's `status` from `Unfunded` to `Funded`. A `Funded` status is required for generating a contractor payment receipt.

scope: `payrolls:run`

### Example Usage

<!-- UsageSnippet language="python" operationID="get-v1-contractor_payments-contractor_payment_uuid-fund" method="put" path="/v1/contractor_payments/{contractor_payment_uuid}/fund" -->
```python
import gusto_embedded
from gusto_embedded import Gusto
import os


with Gusto(
    company_access_auth=os.getenv("GUSTO_COMPANY_ACCESS_AUTH", ""),
) as gusto:

    res = gusto.contractor_payments.fund(contractor_payment_uuid="<id>", x_gusto_api_version=gusto_embedded.GetV1ContractorPaymentsContractorPaymentUUIDFundHeaderXGustoAPIVersion.TWO_THOUSAND_AND_TWENTY_FIVE_MINUS_06_MINUS_15)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                    | Type                                                                                                                                                                                                                         | Required                                                                                                                                                                                                                     | Description                                                                                                                                                                                                                  |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `contractor_payment_uuid`                                                                                                                                                                                                    | *str*                                                                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                                           | The UUID of the contractor payment                                                                                                                                                                                           |
| `x_gusto_api_version`                                                                                                                                                                                                        | [Optional[models.GetV1ContractorPaymentsContractorPaymentUUIDFundHeaderXGustoAPIVersion]](../../models/getv1contractorpaymentscontractorpaymentuuidfundheaderxgustoapiversion.md)                                            | :heavy_minus_sign:                                                                                                                                                                                                           | Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used. |
| `retries`                                                                                                                                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                           | Configuration to override the default retry behavior of the client.                                                                                                                                                          |

### Response

**[models.ContractorPayment](../../models/contractorpayment.md)**

### Errors

| Error Type                       | Status Code                      | Content Type                     |
| -------------------------------- | -------------------------------- | -------------------------------- |
| models.NotFoundErrorObjectError  | 404                              | application/json                 |
| models.UnprocessableEntityError1 | 422                              | application/json                 |
| models.APIError                  | 4XX, 5XX                         | \*/\*                            |

## list

Returns an object containing individual contractor payments, within a given time period, including totals.

Results are returned in reverse chronological order (newest first).

scope: `payrolls:read`

### Example Usage

<!-- UsageSnippet language="python" operationID="get-v1-companies-company_id-contractor_payments" method="get" path="/v1/companies/{company_id}/contractor_payments" -->
```python
import gusto_embedded
from gusto_embedded import Gusto
import os


with Gusto(
    company_access_auth=os.getenv("GUSTO_COMPANY_ACCESS_AUTH", ""),
) as gusto:

    res = gusto.contractor_payments.list(company_id="<id>", start_date="2020-01-01", end_date="2020-12-31", x_gusto_api_version=gusto_embedded.GetV1CompaniesCompanyIDContractorPaymentsHeaderXGustoAPIVersion.TWO_THOUSAND_AND_TWENTY_FIVE_MINUS_06_MINUS_15)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                    | Type                                                                                                                                                                                                                         | Required                                                                                                                                                                                                                     | Description                                                                                                                                                                                                                  | Example                                                                                                                                                                                                                      |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `company_id`                                                                                                                                                                                                                 | *str*                                                                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                                           | The UUID of the company                                                                                                                                                                                                      |                                                                                                                                                                                                                              |
| `start_date`                                                                                                                                                                                                                 | *str*                                                                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                                           | The time period for which to retrieve contractor payments                                                                                                                                                                    | 2020-01-01                                                                                                                                                                                                                   |
| `end_date`                                                                                                                                                                                                                   | *str*                                                                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                                           | The time period for which to retrieve contractor payments. If left empty, defaults to today's date.                                                                                                                          | 2020-12-31                                                                                                                                                                                                                   |
| `x_gusto_api_version`                                                                                                                                                                                                        | [Optional[models.GetV1CompaniesCompanyIDContractorPaymentsHeaderXGustoAPIVersion]](../../models/getv1companiescompanyidcontractorpaymentsheaderxgustoapiversion.md)                                                          | :heavy_minus_sign:                                                                                                                                                                                                           | Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used. |                                                                                                                                                                                                                              |
| `contractor_uuid`                                                                                                                                                                                                            | *Optional[str]*                                                                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                           | The UUID of the contractor. When specified, will load all payments for that contractor.                                                                                                                                      |                                                                                                                                                                                                                              |
| `group_by_date`                                                                                                                                                                                                              | *Optional[bool]*                                                                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                           | Display contractor payments results group by check date if set to true.                                                                                                                                                      |                                                                                                                                                                                                                              |
| `page`                                                                                                                                                                                                                       | *Optional[int]*                                                                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                           | The page that is requested. When unspecified, will load all objects unless endpoint forces pagination.                                                                                                                       |                                                                                                                                                                                                                              |
| `per`                                                                                                                                                                                                                        | *Optional[int]*                                                                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                           | Number of objects per page. For majority of endpoints will default to 25                                                                                                                                                     |                                                                                                                                                                                                                              |
| `retries`                                                                                                                                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                           | Configuration to override the default retry behavior of the client.                                                                                                                                                          |                                                                                                                                                                                                                              |

### Response

**[models.GetV1CompaniesCompanyIDContractorPaymentsResponseBody](../../models/getv1companiescompanyidcontractorpaymentsresponsebody.md)**

### Errors

| Error Type                      | Status Code                     | Content Type                    |
| ------------------------------- | ------------------------------- | ------------------------------- |
| models.NotFoundErrorObjectError | 404                             | application/json                |
| models.APIError                 | 4XX, 5XX                        | \*/\*                           |

## create

Pay a contractor. Information needed depends on the contractor's wage type (hourly vs fixed)

scope: `payrolls:run`

### Example Usage

<!-- UsageSnippet language="python" operationID="post-v1-companies-company_id-contractor_payments" method="post" path="/v1/companies/{company_id}/contractor_payments" -->
```python
from datetime import date
import gusto_embedded
from gusto_embedded import Gusto
import os


with Gusto(
    company_access_auth=os.getenv("GUSTO_COMPANY_ACCESS_AUTH", ""),
) as gusto:

    res = gusto.contractor_payments.create(company_id="<id>", contractor_uuid="<id>", date_=date.fromisoformat("2020-01-01"), x_gusto_api_version=gusto_embedded.PostV1CompaniesCompanyIDContractorPaymentsHeaderXGustoAPIVersion.TWO_THOUSAND_AND_TWENTY_FIVE_MINUS_06_MINUS_15, payment_method=gusto_embedded.ContractorPaymentBodyPaymentMethod.DIRECT_DEPOSIT, wage="5000", hours="40", bonus="500", reimbursement="20")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                    | Type                                                                                                                                                                                                                         | Required                                                                                                                                                                                                                     | Description                                                                                                                                                                                                                  | Example                                                                                                                                                                                                                      |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `company_id`                                                                                                                                                                                                                 | *str*                                                                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                                           | The UUID of the company                                                                                                                                                                                                      |                                                                                                                                                                                                                              |
| `contractor_uuid`                                                                                                                                                                                                            | *str*                                                                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                                           | The contractor receiving the payment.                                                                                                                                                                                        |                                                                                                                                                                                                                              |
| `date_`                                                                                                                                                                                                                      | [datetime](https://docs.python.org/3/library/datetime.html#datetime-objects)                                                                                                                                                 | :heavy_check_mark:                                                                                                                                                                                                           | Date of contractor payment.                                                                                                                                                                                                  | 2020-01-01                                                                                                                                                                                                                   |
| `x_gusto_api_version`                                                                                                                                                                                                        | [Optional[models.PostV1CompaniesCompanyIDContractorPaymentsHeaderXGustoAPIVersion]](../../models/postv1companiescompanyidcontractorpaymentsheaderxgustoapiversion.md)                                                        | :heavy_minus_sign:                                                                                                                                                                                                           | Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used. |                                                                                                                                                                                                                              |
| `payment_method`                                                                                                                                                                                                             | [Optional[models.ContractorPaymentBodyPaymentMethod]](../../models/contractorpaymentbodypaymentmethod.md)                                                                                                                    | :heavy_minus_sign:                                                                                                                                                                                                           | N/A                                                                                                                                                                                                                          |                                                                                                                                                                                                                              |
| `wage`                                                                                                                                                                                                                       | *Optional[str]*                                                                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                           | If the contractor is on a fixed wage, this is the fixed wage payment for the contractor, regardless of hours worked.                                                                                                         | 5000                                                                                                                                                                                                                         |
| `hours`                                                                                                                                                                                                                      | *Optional[str]*                                                                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                           | If the contractor is on an hourly wage, this is the number of hours that the contractor worked for the payment.                                                                                                              | 40                                                                                                                                                                                                                           |
| `bonus`                                                                                                                                                                                                                      | *Optional[str]*                                                                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                           | If the contractor is on an hourly wage, this is the bonus the contractor earned.                                                                                                                                             | 500                                                                                                                                                                                                                          |
| `reimbursement`                                                                                                                                                                                                              | *Optional[str]*                                                                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                           | Reimbursed wages for the contractor.                                                                                                                                                                                         | 20                                                                                                                                                                                                                           |
| `retries`                                                                                                                                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                           | Configuration to override the default retry behavior of the client.                                                                                                                                                          |                                                                                                                                                                                                                              |

### Response

**[models.ContractorPayment](../../models/contractorpayment.md)**

### Errors

| Error Type                       | Status Code                      | Content Type                     |
| -------------------------------- | -------------------------------- | -------------------------------- |
| models.NotFoundErrorObjectError  | 404                              | application/json                 |
| models.UnprocessableEntityError1 | 422                              | application/json                 |
| models.APIError                  | 4XX, 5XX                         | \*/\*                            |

## get

Returns a single contractor payment.

scope: `payrolls:read`

### Example Usage

<!-- UsageSnippet language="python" operationID="get-v1-companies-company_id-contractor_payment-contractor-payment" method="get" path="/v1/companies/{company_id}/contractor_payments/{contractor_payment_id}" -->
```python
import gusto_embedded
from gusto_embedded import Gusto
import os


with Gusto(
    company_access_auth=os.getenv("GUSTO_COMPANY_ACCESS_AUTH", ""),
) as gusto:

    res = gusto.contractor_payments.get(company_id="<id>", contractor_payment_id="<id>", x_gusto_api_version=gusto_embedded.GetV1CompaniesCompanyIDContractorPaymentContractorPaymentHeaderXGustoAPIVersion.TWO_THOUSAND_AND_TWENTY_FIVE_MINUS_06_MINUS_15)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                    | Type                                                                                                                                                                                                                         | Required                                                                                                                                                                                                                     | Description                                                                                                                                                                                                                  |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `company_id`                                                                                                                                                                                                                 | *str*                                                                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                                           | The UUID of the company                                                                                                                                                                                                      |
| `contractor_payment_id`                                                                                                                                                                                                      | *str*                                                                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                                           | The UUID of the contractor payment                                                                                                                                                                                           |
| `x_gusto_api_version`                                                                                                                                                                                                        | [Optional[models.GetV1CompaniesCompanyIDContractorPaymentContractorPaymentHeaderXGustoAPIVersion]](../../models/getv1companiescompanyidcontractorpaymentcontractorpaymentheaderxgustoapiversion.md)                          | :heavy_minus_sign:                                                                                                                                                                                                           | Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used. |
| `retries`                                                                                                                                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                           | Configuration to override the default retry behavior of the client.                                                                                                                                                          |

### Response

**[models.ContractorPayment](../../models/contractorpayment.md)**

### Errors

| Error Type                      | Status Code                     | Content Type                    |
| ------------------------------- | ------------------------------- | ------------------------------- |
| models.NotFoundErrorObjectError | 404                             | application/json                |
| models.APIError                 | 4XX, 5XX                        | \*/\*                           |

## delete

Cancels and deletes a contractor payment. If the contractor payment has already started processing ("may_cancel": true), the payment cannot be cancelled.

scope: `payrolls:run`

### Example Usage

<!-- UsageSnippet language="python" operationID="delete-v1-companies-company_id-contractor_payment-contractor-payment" method="delete" path="/v1/companies/{company_id}/contractor_payments/{contractor_payment_id}" -->
```python
import gusto_embedded
from gusto_embedded import Gusto
import os


with Gusto(
    company_access_auth=os.getenv("GUSTO_COMPANY_ACCESS_AUTH", ""),
) as gusto:

    gusto.contractor_payments.delete(company_id="<id>", contractor_payment_id="<id>", x_gusto_api_version=gusto_embedded.DeleteV1CompaniesCompanyIDContractorPaymentContractorPaymentHeaderXGustoAPIVersion.TWO_THOUSAND_AND_TWENTY_FIVE_MINUS_06_MINUS_15)

    # Use the SDK ...

```

### Parameters

| Parameter                                                                                                                                                                                                                    | Type                                                                                                                                                                                                                         | Required                                                                                                                                                                                                                     | Description                                                                                                                                                                                                                  |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `company_id`                                                                                                                                                                                                                 | *str*                                                                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                                           | The UUID of the company                                                                                                                                                                                                      |
| `contractor_payment_id`                                                                                                                                                                                                      | *str*                                                                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                                           | The UUID of the contractor payment                                                                                                                                                                                           |
| `x_gusto_api_version`                                                                                                                                                                                                        | [Optional[models.DeleteV1CompaniesCompanyIDContractorPaymentContractorPaymentHeaderXGustoAPIVersion]](../../models/deletev1companiescompanyidcontractorpaymentcontractorpaymentheaderxgustoapiversion.md)                    | :heavy_minus_sign:                                                                                                                                                                                                           | Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used. |
| `retries`                                                                                                                                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                           | Configuration to override the default retry behavior of the client.                                                                                                                                                          |

### Errors

| Error Type                       | Status Code                      | Content Type                     |
| -------------------------------- | -------------------------------- | -------------------------------- |
| models.NotFoundErrorObjectError  | 404                              | application/json                 |
| models.UnprocessableEntityError1 | 422                              | application/json                 |
| models.APIError                  | 4XX, 5XX                         | \*/\*                            |

## preview

Returns a debit_date dependent on the ACH payment speed of the company.

If the payment method is Check or Historical payment, the debit_date will be the same as the check_date.

scope: `payrolls:read`

### Example Usage

<!-- UsageSnippet language="python" operationID="get-companies-company_uuid-contractor_payments-preview" method="get" path="/v1/companies/{company_uuid}/contractor_payments/preview" -->
```python
import gusto_embedded
from gusto_embedded import Gusto
import os


with Gusto(
    company_access_auth=os.getenv("GUSTO_COMPANY_ACCESS_AUTH", ""),
) as gusto:

    res = gusto.contractor_payments.preview(company_uuid="<id>", contractor_payments=[], x_gusto_api_version=gusto_embedded.GetCompaniesCompanyUUIDContractorPaymentsPreviewHeaderXGustoAPIVersion.TWO_THOUSAND_AND_TWENTY_FIVE_MINUS_06_MINUS_15)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                    | Type                                                                                                                                                                                                                         | Required                                                                                                                                                                                                                     | Description                                                                                                                                                                                                                  |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `company_uuid`                                                                                                                                                                                                               | *str*                                                                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                                           | The UUID of the company                                                                                                                                                                                                      |
| `contractor_payments`                                                                                                                                                                                                        | List[[models.ContractorPaymentsPreviewBodyContractorPayments](../../models/contractorpaymentspreviewbodycontractorpayments.md)]                                                                                              | :heavy_check_mark:                                                                                                                                                                                                           | A list of contractor payments to preview.                                                                                                                                                                                    |
| `x_gusto_api_version`                                                                                                                                                                                                        | [Optional[models.GetCompaniesCompanyUUIDContractorPaymentsPreviewHeaderXGustoAPIVersion]](../../models/getcompaniescompanyuuidcontractorpaymentspreviewheaderxgustoapiversion.md)                                            | :heavy_minus_sign:                                                                                                                                                                                                           | Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used. |
| `retries`                                                                                                                                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                           | Configuration to override the default retry behavior of the client.                                                                                                                                                          |

### Response

**[models.ContractorPaymentsPreview](../../models/contractorpaymentspreview.md)**

### Errors

| Error Type                       | Status Code                      | Content Type                     |
| -------------------------------- | -------------------------------- | -------------------------------- |
| models.NotFoundErrorObjectError  | 404                              | application/json                 |
| models.UnprocessableEntityError1 | 422                              | application/json                 |
| models.APIError                  | 4XX, 5XX                         | \*/\*                            |

## get_v1_contractor_payments_contractor_payment_id_pdf

Get a PDF document for a single contractor payment.

scope: `payrolls:read`

### Example Usage

<!-- UsageSnippet language="python" operationID="get-v1-contractor_payments-contractor_payment_id-pdf" method="get" path="/v1/contractor_payments/{contractor_payment_id}/pdf" -->
```python
import gusto_embedded
from gusto_embedded import Gusto
import os


with Gusto(
    company_access_auth=os.getenv("GUSTO_COMPANY_ACCESS_AUTH", ""),
) as gusto:

    gusto.contractor_payments.get_v1_contractor_payments_contractor_payment_id_pdf(contractor_payment_id="<id>", x_gusto_api_version=gusto_embedded.GetV1ContractorPaymentsContractorPaymentIDPdfHeaderXGustoAPIVersion.TWO_THOUSAND_AND_TWENTY_FIVE_MINUS_06_MINUS_15)

    # Use the SDK ...

```

### Parameters

| Parameter                                                                                                                                                                                                                    | Type                                                                                                                                                                                                                         | Required                                                                                                                                                                                                                     | Description                                                                                                                                                                                                                  |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `contractor_payment_id`                                                                                                                                                                                                      | *str*                                                                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                                           | The UUID of the contractor payment                                                                                                                                                                                           |
| `x_gusto_api_version`                                                                                                                                                                                                        | [Optional[models.GetV1ContractorPaymentsContractorPaymentIDPdfHeaderXGustoAPIVersion]](../../models/getv1contractorpaymentscontractorpaymentidpdfheaderxgustoapiversion.md)                                                  | :heavy_minus_sign:                                                                                                                                                                                                           | Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used. |
| `retries`                                                                                                                                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                           | Configuration to override the default retry behavior of the client.                                                                                                                                                          |

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |