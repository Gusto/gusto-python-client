# Flows

## Overview

### Available Operations

* [create](#create) - Create a flow

## create

Generate a link to access a pre-built workflow in Gusto white-label UI. For security, all generated flows will expire within 1 hour of inactivity or 24 hours from creation time, whichever comes first.

You can see a list of all possible flow types in our [Flow Types](https://docs.gusto.com/embedded-payroll/docs/flow-types) guide.

You can also mix and match flow_types in the same category to create custom flows suitable for your needs.

For instance, to create a custom onboarding flow that only includes `add_addresses`, `add_employees`, and `sign_all_forms` steps, simply stitch those flow_types together into a comma delimited string:

```json
{
  "flow_type": "add_addresses,add_employees,sign_all_forms"
}
```

Please be mindful of data dependencies in each step to achieve the best user experience.

For more information and in-depth guides review the [Getting Started](https://docs.gusto.com/embedded-payroll/docs/flows-getting-started) guide for flows.

scope: `flows:write`

### Example Usage

<!-- UsageSnippet language="python" operationID="post-v1-company-flows" method="post" path="/v1/companies/{company_uuid}/flows" -->
```python
import gusto_embedded_v_2026_06_15
from gusto_embedded_v_2026_06_15 import Gusto
import os


with Gusto(
    company_access_auth=os.getenv("GUSTO_COMPANY_ACCESS_AUTH", ""),
) as gusto:

    res = gusto.flows.create(company_uuid="<id>", flow_type="company_onboarding", x_gusto_api_version=gusto_embedded_v_2026_06_15.PostV1CompanyFlowsHeaderXGustoAPIVersion.TWO_THOUSAND_AND_TWENTY_SIX_MINUS_06_MINUS_15)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                    | Type                                                                                                                                                                                                                         | Required                                                                                                                                                                                                                     | Description                                                                                                                                                                                                                  | Example                                                                                                                                                                                                                      |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `company_uuid`                                                                                                                                                                                                               | *str*                                                                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                                           | The UUID of the company                                                                                                                                                                                                      |                                                                                                                                                                                                                              |
| `flow_type`                                                                                                                                                                                                                  | *str*                                                                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                                           | The type of flow to generate. Multiple flow types can be combined by separating them with commas (e.g., "add_addresses,add_employees,sign_all_forms").                                                                       | company_onboarding                                                                                                                                                                                                           |
| `x_gusto_api_version`                                                                                                                                                                                                        | [Optional[models.PostV1CompanyFlowsHeaderXGustoAPIVersion]](../../models/postv1companyflowsheaderxgustoapiversion.md)                                                                                                        | :heavy_minus_sign:                                                                                                                                                                                                           | Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used. |                                                                                                                                                                                                                              |
| `entity_uuid`                                                                                                                                                                                                                | *Optional[str]*                                                                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                           | UUID of the target entity applicable to the flow. This field is optional for company flows.                                                                                                                                  |                                                                                                                                                                                                                              |
| `entity_type`                                                                                                                                                                                                                | [Optional[models.CreateFlowRequestEntityType]](../../models/createflowrequestentitytype.md)                                                                                                                                  | :heavy_minus_sign:                                                                                                                                                                                                           | The type of target entity applicable to the flow. This field is optional for company flows.                                                                                                                                  |                                                                                                                                                                                                                              |
| `options`                                                                                                                                                                                                                    | Dict[str, *Any*]                                                                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                           | Optional configuration object that varies based on the flow_type. This can contain arbitrary key-value pairs specific to the flow being generated.                                                                           |                                                                                                                                                                                                                              |
| `retries`                                                                                                                                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                           | Configuration to override the default retry behavior of the client.                                                                                                                                                          |                                                                                                                                                                                                                              |

### Response

**[models.Flow](../../models/flow.md)**

### Errors

| Error Type                       | Status Code                      | Content Type                     |
| -------------------------------- | -------------------------------- | -------------------------------- |
| models.NotFoundErrorObject       | 404                              | application/json                 |
| models.UnprocessableEntityError1 | 422                              | application/json                 |
| models.APIError                  | 4XX, 5XX                         | \*/\*                            |