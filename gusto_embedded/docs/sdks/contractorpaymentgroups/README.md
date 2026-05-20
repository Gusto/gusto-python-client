# ContractorPaymentGroups

## Overview

### Available Operations

* [get_list](#get_list) - Get contractor payment groups for a company
* [create](#create) - Create a contractor payment group
* [preview](#preview) - Preview a contractor payment group
* [get](#get) - Get a contractor payment group
* [delete](#delete) - Cancel a contractor payment group
* [fund](#fund) - Fund a contractor payment group [DEMO]
* [get_v1_contractor_payment_groups_id_partner_disbursements](#get_v1_contractor_payment_groups_id_partner_disbursements) - Get partner disbursements for a contractor payment group
* [patch_v1_contractor_payment_groups_id_partner_disbursements](#patch_v1_contractor_payment_groups_id_partner_disbursements) - Update partner disbursements for a contractor payment group

## get_list

Returns a list of minimal contractor payment groups within a given time period, including totals but not associated contractor payments.

scope: `payrolls:read`

### Example Usage

<!-- UsageSnippet language="python" operationID="get-v1-companies-company_id-contractor_payment_groups" method="get" path="/v1/companies/{company_id}/contractor_payment_groups" -->
```python
import gusto_embedded
from gusto_embedded import Gusto
import os


with Gusto(
    company_access_auth=os.getenv("GUSTO_COMPANY_ACCESS_AUTH", ""),
) as gusto:

    res = gusto.contractor_payment_groups.get_list(company_id="<id>", start_date="2020-01-01", end_date="2020-12-31", x_gusto_api_version=gusto_embedded.GetV1CompaniesCompanyIDContractorPaymentGroupsHeaderXGustoAPIVersion.TWO_THOUSAND_AND_TWENTY_FIVE_MINUS_06_MINUS_15)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                    | Type                                                                                                                                                                                                                         | Required                                                                                                                                                                                                                     | Description                                                                                                                                                                                                                  | Example                                                                                                                                                                                                                      |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `company_id`                                                                                                                                                                                                                 | *str*                                                                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                                           | The UUID of the company                                                                                                                                                                                                      |                                                                                                                                                                                                                              |
| `start_date`                                                                                                                                                                                                                 | *Optional[str]*                                                                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                           | The time period for which to retrieve contractor payment groups. Defaults to 6 months ago.                                                                                                                                   | 2020-01-01                                                                                                                                                                                                                   |
| `end_date`                                                                                                                                                                                                                   | *Optional[str]*                                                                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                           | The time period for which to retrieve contractor payment groups. Defaults to today's date.                                                                                                                                   | 2020-12-31                                                                                                                                                                                                                   |
| `page`                                                                                                                                                                                                                       | *Optional[int]*                                                                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                           | The page that is requested. When unspecified, will load all objects unless endpoint forces pagination.                                                                                                                       |                                                                                                                                                                                                                              |
| `per`                                                                                                                                                                                                                        | *Optional[int]*                                                                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                           | Number of objects per page. For majority of endpoints will default to 25                                                                                                                                                     |                                                                                                                                                                                                                              |
| `x_gusto_api_version`                                                                                                                                                                                                        | [Optional[models.GetV1CompaniesCompanyIDContractorPaymentGroupsHeaderXGustoAPIVersion]](../../models/getv1companiescompanyidcontractorpaymentgroupsheaderxgustoapiversion.md)                                                | :heavy_minus_sign:                                                                                                                                                                                                           | Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used. |                                                                                                                                                                                                                              |
| `retries`                                                                                                                                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                           | Configuration to override the default retry behavior of the client.                                                                                                                                                          |                                                                                                                                                                                                                              |

### Response

**[List[models.ContractorPaymentGroupWithBlockers]](../../models/.md)**

### Errors

| Error Type                      | Status Code                     | Content Type                    |
| ------------------------------- | ------------------------------- | ------------------------------- |
| models.NotFoundErrorObjectError | 404                             | application/json                |
| models.APIError                 | 4XX, 5XX                        | \*/\*                           |

## create

Pay a group of contractors. Information needed depends on the contractor's wage type (hourly vs fixed)

scope: `payrolls:run`

### Example Usage

<!-- UsageSnippet language="python" operationID="post-v1-companies-company_id-contractor_payment_groups" method="post" path="/v1/companies/{company_id}/contractor_payment_groups" -->
```python
from datetime import date
import gusto_embedded
from gusto_embedded import Gusto
import os


with Gusto(
    company_access_auth=os.getenv("GUSTO_COMPANY_ACCESS_AUTH", ""),
) as gusto:

    res = gusto.contractor_payment_groups.create(company_id="<id>", check_date=date.fromisoformat("2020-01-01"), creation_token="1d532d13-8f61-4a57-ad3c-b5fac1c6e05e", contractor_payments=[], x_gusto_api_version=gusto_embedded.PostV1CompaniesCompanyIDContractorPaymentGroupsHeaderXGustoAPIVersion.TWO_THOUSAND_AND_TWENTY_FIVE_MINUS_06_MINUS_15)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                    | Type                                                                                                                                                                                                                         | Required                                                                                                                                                                                                                     | Description                                                                                                                                                                                                                  | Example                                                                                                                                                                                                                      |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `company_id`                                                                                                                                                                                                                 | *str*                                                                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                                           | The UUID of the company                                                                                                                                                                                                      |                                                                                                                                                                                                                              |
| `check_date`                                                                                                                                                                                                                 | [datetime](https://docs.python.org/3/library/datetime.html#datetime-objects)                                                                                                                                                 | :heavy_check_mark:                                                                                                                                                                                                           | The payment check date                                                                                                                                                                                                       | 2020-01-01                                                                                                                                                                                                                   |
| `creation_token`                                                                                                                                                                                                             | *str*                                                                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                                           | A token used to make contractor payment group creation idempotent. The string must be unique for each group you intend to create.                                                                                            | 1d532d13-8f61-4a57-ad3c-b5fac1c6e05e                                                                                                                                                                                         |
| `contractor_payments`                                                                                                                                                                                                        | List[[models.PostV1CompaniesCompanyIDContractorPaymentGroupsContractorPayments](../../models/postv1companiescompanyidcontractorpaymentgroupscontractorpayments.md)]                                                          | :heavy_check_mark:                                                                                                                                                                                                           | N/A                                                                                                                                                                                                                          |                                                                                                                                                                                                                              |
| `x_gusto_api_version`                                                                                                                                                                                                        | [Optional[models.PostV1CompaniesCompanyIDContractorPaymentGroupsHeaderXGustoAPIVersion]](../../models/postv1companiescompanyidcontractorpaymentgroupsheaderxgustoapiversion.md)                                              | :heavy_minus_sign:                                                                                                                                                                                                           | Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used. |                                                                                                                                                                                                                              |
| `submission_blockers`                                                                                                                                                                                                        | List[[models.SubmissionBlockers](../../models/submissionblockers.md)]                                                                                                                                                        | :heavy_minus_sign:                                                                                                                                                                                                           | Optional array of submission blockers with selected unblock options. Returned from the preview endpoint and can be submitted with selected_option to resolve blockers.                                                       |                                                                                                                                                                                                                              |
| `retries`                                                                                                                                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                           | Configuration to override the default retry behavior of the client.                                                                                                                                                          |                                                                                                                                                                                                                              |

### Response

**[models.ContractorPaymentGroup](../../models/contractorpaymentgroup.md)**

### Errors

| Error Type                       | Status Code                      | Content Type                     |
| -------------------------------- | -------------------------------- | -------------------------------- |
| models.NotFoundErrorObjectError  | 404                              | application/json                 |
| models.UnprocessableEntityError1 | 422                              | application/json                 |
| models.APIError                  | 4XX, 5XX                         | \*/\*                            |

## preview

Preview a group of contractor payments. Request will validate inputs and return preview of the contractor payment group including the expected `debit_date`. The `uuid` field will be null in the response.

The returned `creation_token` is a required parameter in order to create the contractor payment group.

scope: `payrolls:read`

### Example Usage

<!-- UsageSnippet language="python" operationID="post-v1-companies-company_id-contractor_payment_groups-preview" method="post" path="/v1/companies/{company_id}/contractor_payment_groups/preview" -->
```python
import gusto_embedded
from gusto_embedded import Gusto
import os


with Gusto(
    company_access_auth=os.getenv("GUSTO_COMPANY_ACCESS_AUTH", ""),
) as gusto:

    res = gusto.contractor_payment_groups.preview(company_id="<id>", contractor_payments=[], x_gusto_api_version=gusto_embedded.PostV1CompaniesCompanyIDContractorPaymentGroupsPreviewHeaderXGustoAPIVersion.TWO_THOUSAND_AND_TWENTY_FIVE_MINUS_06_MINUS_15)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                    | Type                                                                                                                                                                                                                         | Required                                                                                                                                                                                                                     | Description                                                                                                                                                                                                                  |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `company_id`                                                                                                                                                                                                                 | *str*                                                                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                                           | The UUID of the company                                                                                                                                                                                                      |
| `contractor_payments`                                                                                                                                                                                                        | List[[models.PostV1CompaniesCompanyIDContractorPaymentGroupsPreviewContractorPayments](../../models/postv1companiescompanyidcontractorpaymentgroupspreviewcontractorpayments.md)]                                            | :heavy_check_mark:                                                                                                                                                                                                           | N/A                                                                                                                                                                                                                          |
| `x_gusto_api_version`                                                                                                                                                                                                        | [Optional[models.PostV1CompaniesCompanyIDContractorPaymentGroupsPreviewHeaderXGustoAPIVersion]](../../models/postv1companiescompanyidcontractorpaymentgroupspreviewheaderxgustoapiversion.md)                                | :heavy_minus_sign:                                                                                                                                                                                                           | Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used. |
| `check_date`                                                                                                                                                                                                                 | [datetime](https://docs.python.org/3/library/datetime.html#datetime-objects)                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                                                                           | Date when payments should be processed                                                                                                                                                                                       |
| `retries`                                                                                                                                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                           | Configuration to override the default retry behavior of the client.                                                                                                                                                          |

### Response

**[models.ContractorPaymentGroupPreview](../../models/contractorpaymentgrouppreview.md)**

### Errors

| Error Type                       | Status Code                      | Content Type                     |
| -------------------------------- | -------------------------------- | -------------------------------- |
| models.NotFoundErrorObjectError  | 404                              | application/json                 |
| models.UnprocessableEntityError1 | 422                              | application/json                 |
| models.APIError                  | 4XX, 5XX                         | \*/\*                            |

## get

Returns a contractor payment group with all associated contractor payments.

scope: `payrolls:read`

### Example Usage

<!-- UsageSnippet language="python" operationID="get-v1-contractor_payment_groups-contractor_payment_group_id" method="get" path="/v1/contractor_payment_groups/{contractor_payment_group_uuid}" -->
```python
import gusto_embedded
from gusto_embedded import Gusto
import os


with Gusto(
    company_access_auth=os.getenv("GUSTO_COMPANY_ACCESS_AUTH", ""),
) as gusto:

    res = gusto.contractor_payment_groups.get(contractor_payment_group_uuid="<id>", x_gusto_api_version=gusto_embedded.GetV1ContractorPaymentGroupsContractorPaymentGroupIDHeaderXGustoAPIVersion.TWO_THOUSAND_AND_TWENTY_FIVE_MINUS_06_MINUS_15)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                    | Type                                                                                                                                                                                                                         | Required                                                                                                                                                                                                                     | Description                                                                                                                                                                                                                  |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `contractor_payment_group_uuid`                                                                                                                                                                                              | *str*                                                                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                                           | The UUID of the contractor payment group                                                                                                                                                                                     |
| `x_gusto_api_version`                                                                                                                                                                                                        | [Optional[models.GetV1ContractorPaymentGroupsContractorPaymentGroupIDHeaderXGustoAPIVersion]](../../models/getv1contractorpaymentgroupscontractorpaymentgroupidheaderxgustoapiversion.md)                                    | :heavy_minus_sign:                                                                                                                                                                                                           | Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used. |
| `retries`                                                                                                                                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                           | Configuration to override the default retry behavior of the client.                                                                                                                                                          |

### Response

**[models.ContractorPaymentGroup](../../models/contractorpaymentgroup.md)**

### Errors

| Error Type                      | Status Code                     | Content Type                    |
| ------------------------------- | ------------------------------- | ------------------------------- |
| models.NotFoundErrorObjectError | 404                             | application/json                |
| models.APIError                 | 4XX, 5XX                        | \*/\*                           |

## delete

Cancels a contractor payment group and all associated contractor payments. All contractor payments must be cancellable, unfunded.

scope: `payrolls:run`

### Example Usage

<!-- UsageSnippet language="python" operationID="delete-v1-contractor_payment_groups-contractor_payment_group_id" method="delete" path="/v1/contractor_payment_groups/{contractor_payment_group_uuid}" -->
```python
import gusto_embedded
from gusto_embedded import Gusto
import os


with Gusto(
    company_access_auth=os.getenv("GUSTO_COMPANY_ACCESS_AUTH", ""),
) as gusto:

    gusto.contractor_payment_groups.delete(contractor_payment_group_uuid="<id>", x_gusto_api_version=gusto_embedded.DeleteV1ContractorPaymentGroupsContractorPaymentGroupIDHeaderXGustoAPIVersion.TWO_THOUSAND_AND_TWENTY_FIVE_MINUS_06_MINUS_15)

    # Use the SDK ...

```

### Parameters

| Parameter                                                                                                                                                                                                                    | Type                                                                                                                                                                                                                         | Required                                                                                                                                                                                                                     | Description                                                                                                                                                                                                                  |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `contractor_payment_group_uuid`                                                                                                                                                                                              | *str*                                                                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                                           | The UUID of the contractor payment group                                                                                                                                                                                     |
| `x_gusto_api_version`                                                                                                                                                                                                        | [Optional[models.DeleteV1ContractorPaymentGroupsContractorPaymentGroupIDHeaderXGustoAPIVersion]](../../models/deletev1contractorpaymentgroupscontractorpaymentgroupidheaderxgustoapiversion.md)                              | :heavy_minus_sign:                                                                                                                                                                                                           | Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used. |
| `retries`                                                                                                                                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                           | Configuration to override the default retry behavior of the client.                                                                                                                                                          |

### Errors

| Error Type                       | Status Code                      | Content Type                     |
| -------------------------------- | -------------------------------- | -------------------------------- |
| models.NotFoundErrorObjectError  | 404                              | application/json                 |
| models.UnprocessableEntityError1 | 422                              | application/json                 |
| models.APIError                  | 4XX, 5XX                         | \*/\*                            |

## fund

> 🚧 Demo action
> This action is only available in the Demo environment

Simulate funding a contractor payment group. Funding only occurs automatically in the production environment when bank transactions are generated. Use this action in the demo environment to transition a contractor payment group's `status` from `Unfunded` to `Funded`. A `Funded` status is required for generating a contractor payment receipt.

scope: `payrolls:run`

### Example Usage

<!-- UsageSnippet language="python" operationID="put-v1-contractor_payment_groups-contractor_payment_group_id-fund" method="put" path="/v1/contractor_payment_groups/{contractor_payment_group_uuid}/fund" -->
```python
import gusto_embedded
from gusto_embedded import Gusto
import os


with Gusto(
    company_access_auth=os.getenv("GUSTO_COMPANY_ACCESS_AUTH", ""),
) as gusto:

    res = gusto.contractor_payment_groups.fund(contractor_payment_group_uuid="<id>", x_gusto_api_version=gusto_embedded.PutV1ContractorPaymentGroupsContractorPaymentGroupIDFundHeaderXGustoAPIVersion.TWO_THOUSAND_AND_TWENTY_FIVE_MINUS_06_MINUS_15)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                    | Type                                                                                                                                                                                                                         | Required                                                                                                                                                                                                                     | Description                                                                                                                                                                                                                  |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `contractor_payment_group_uuid`                                                                                                                                                                                              | *str*                                                                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                                           | The UUID of the contractor payment group                                                                                                                                                                                     |
| `x_gusto_api_version`                                                                                                                                                                                                        | [Optional[models.PutV1ContractorPaymentGroupsContractorPaymentGroupIDFundHeaderXGustoAPIVersion]](../../models/putv1contractorpaymentgroupscontractorpaymentgroupidfundheaderxgustoapiversion.md)                            | :heavy_minus_sign:                                                                                                                                                                                                           | Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used. |
| `retries`                                                                                                                                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                           | Configuration to override the default retry behavior of the client.                                                                                                                                                          |

### Response

**[models.ContractorPaymentGroup](../../models/contractorpaymentgroup.md)**

### Errors

| Error Type                       | Status Code                      | Content Type                     |
| -------------------------------- | -------------------------------- | -------------------------------- |
| models.NotFoundErrorObjectError  | 404                              | application/json                 |
| models.UnprocessableEntityError1 | 422                              | application/json                 |
| models.APIError                  | 4XX, 5XX                         | \*/\*                            |

## get_v1_contractor_payment_groups_id_partner_disbursements

Get partner disbursements for a specific contractor payment group.

scope: `partner_disbursements:read`

### Example Usage

<!-- UsageSnippet language="python" operationID="get-v1-contractor_payment_groups-id-partner_disbursements" method="get" path="/v1/contractor_payment_groups/{id}/partner_disbursements" -->
```python
import gusto_embedded
from gusto_embedded import Gusto
import os


with Gusto(
    company_access_auth=os.getenv("GUSTO_COMPANY_ACCESS_AUTH", ""),
) as gusto:

    res = gusto.contractor_payment_groups.get_v1_contractor_payment_groups_id_partner_disbursements(id="<id>", x_gusto_api_version=gusto_embedded.GetV1ContractorPaymentGroupsIDPartnerDisbursementsHeaderXGustoAPIVersion.TWO_THOUSAND_AND_TWENTY_FIVE_MINUS_06_MINUS_15)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                    | Type                                                                                                                                                                                                                         | Required                                                                                                                                                                                                                     | Description                                                                                                                                                                                                                  |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `id`                                                                                                                                                                                                                         | *str*                                                                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                                           | The UUID of the contractor payment group                                                                                                                                                                                     |
| `x_gusto_api_version`                                                                                                                                                                                                        | [Optional[models.GetV1ContractorPaymentGroupsIDPartnerDisbursementsHeaderXGustoAPIVersion]](../../models/getv1contractorpaymentgroupsidpartnerdisbursementsheaderxgustoapiversion.md)                                        | :heavy_minus_sign:                                                                                                                                                                                                           | Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used. |
| `retries`                                                                                                                                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                           | Configuration to override the default retry behavior of the client.                                                                                                                                                          |

### Response

**[models.ContractorPaymentGroupPartnerDisbursements](../../models/contractorpaymentgrouppartnerdisbursements.md)**

### Errors

| Error Type                      | Status Code                     | Content Type                    |
| ------------------------------- | ------------------------------- | ------------------------------- |
| models.NotFoundErrorObjectError | 404                             | application/json                |
| models.APIError                 | 4XX, 5XX                        | \*/\*                           |

## patch_v1_contractor_payment_groups_id_partner_disbursements

Update partner disbursements for a specific contractor payment group.

scope: `partner_disbursements:write`

### Example Usage

<!-- UsageSnippet language="python" operationID="patch-v1-contractor_payment_groups-id-partner_disbursements" method="patch" path="/v1/contractor_payment_groups/{id}/partner_disbursements" -->
```python
import gusto_embedded
from gusto_embedded import Gusto
import os


with Gusto(
    company_access_auth=os.getenv("GUSTO_COMPANY_ACCESS_AUTH", ""),
) as gusto:

    res = gusto.contractor_payment_groups.patch_v1_contractor_payment_groups_id_partner_disbursements(id="<id>", disbursements=[
        {
            "contractor_payment_uuid": "9f8e7d6c-5b4a-3928-1c2d-3e4f5a6b7c8d",
        },
    ], x_gusto_api_version=gusto_embedded.PatchV1ContractorPaymentGroupsIDPartnerDisbursementsHeaderXGustoAPIVersion.TWO_THOUSAND_AND_TWENTY_FIVE_MINUS_06_MINUS_15)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                    | Type                                                                                                                                                                                                                         | Required                                                                                                                                                                                                                     | Description                                                                                                                                                                                                                  |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `id`                                                                                                                                                                                                                         | *str*                                                                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                                           | The UUID of the contractor payment group                                                                                                                                                                                     |
| `disbursements`                                                                                                                                                                                                              | List[[models.PatchV1ContractorPaymentGroupsIDPartnerDisbursementsDisbursements](../../models/patchv1contractorpaymentgroupsidpartnerdisbursementsdisbursements.md)]                                                          | :heavy_check_mark:                                                                                                                                                                                                           | N/A                                                                                                                                                                                                                          |
| `x_gusto_api_version`                                                                                                                                                                                                        | [Optional[models.PatchV1ContractorPaymentGroupsIDPartnerDisbursementsHeaderXGustoAPIVersion]](../../models/patchv1contractorpaymentgroupsidpartnerdisbursementsheaderxgustoapiversion.md)                                    | :heavy_minus_sign:                                                                                                                                                                                                           | Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used. |
| `retries`                                                                                                                                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                           | Configuration to override the default retry behavior of the client.                                                                                                                                                          |

### Response

**[models.ContractorPaymentGroupPartnerDisbursements](../../models/contractorpaymentgrouppartnerdisbursements.md)**

### Errors

| Error Type                       | Status Code                      | Content Type                     |
| -------------------------------- | -------------------------------- | -------------------------------- |
| models.NotFoundErrorObjectError  | 404                              | application/json                 |
| models.UnprocessableEntityError1 | 422                              | application/json                 |
| models.APIError                  | 4XX, 5XX                         | \*/\*                            |