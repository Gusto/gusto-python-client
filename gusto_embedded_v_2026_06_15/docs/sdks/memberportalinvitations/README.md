# MemberPortalInvitations

## Overview

### Available Operations

* [post_v1_employees_employee_id_member_portal_invitations](#post_v1_employees_employee_id_member_portal_invitations) - Create an employee member portal invitation
* [get_v1_employees_employee_id_member_portal_invitations](#get_v1_employees_employee_id_member_portal_invitations) - Get an employee member portal invitation
* [delete_v1_employees_employee_id_member_portal_invitations](#delete_v1_employees_employee_id_member_portal_invitations) - Cancel an employee member portal invitation
* [post_v1_contractors_contractor_uuid_member_portal_invitations](#post_v1_contractors_contractor_uuid_member_portal_invitations) - Create a contractor member portal invitation
* [get_v1_contractors_contractor_uuid_member_portal_invitations](#get_v1_contractors_contractor_uuid_member_portal_invitations) - Get a contractor member portal invitation
* [delete_v1_contractors_contractor_uuid_member_portal_invitations](#delete_v1_contractors_contractor_uuid_member_portal_invitations) - Cancel a contractor member portal invitation

## post_v1_employees_employee_id_member_portal_invitations

Generates a member portal invitation for the specified employee. If the employee already has an invitation and its token has expired, calling this endpoint regenerates the invitation and overrides the prior token.

scope: `member_portal_invitation:write`

### Example Usage

<!-- UsageSnippet language="python" operationID="post-v1-employees-employee_id-member_portal_invitations" method="post" path="/v1/employees/{employee_id}/member_portal_invitations" -->
```python
import gusto_embedded_v_2026_06_15
from gusto_embedded_v_2026_06_15 import Gusto
import os


with Gusto(
    company_access_auth=os.getenv("GUSTO_COMPANY_ACCESS_AUTH", ""),
) as gusto:

    gusto.member_portal_invitations.post_v1_employees_employee_id_member_portal_invitations(employee_id="<id>", x_gusto_api_version=gusto_embedded_v_2026_06_15.PostV1EmployeesEmployeeIDMemberPortalInvitationsHeaderXGustoAPIVersion.TWO_THOUSAND_AND_TWENTY_SIX_MINUS_06_MINUS_15)

    # Use the SDK ...

```

### Parameters

| Parameter                                                                                                                                                                                                                    | Type                                                                                                                                                                                                                         | Required                                                                                                                                                                                                                     | Description                                                                                                                                                                                                                  |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `employee_id`                                                                                                                                                                                                                | *str*                                                                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                                           | The UUID of the employee                                                                                                                                                                                                     |
| `x_gusto_api_version`                                                                                                                                                                                                        | [Optional[models.PostV1EmployeesEmployeeIDMemberPortalInvitationsHeaderXGustoAPIVersion]](../../models/postv1employeesemployeeidmemberportalinvitationsheaderxgustoapiversion.md)                                            | :heavy_minus_sign:                                                                                                                                                                                                           | Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used. |
| `retries`                                                                                                                                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                           | Configuration to override the default retry behavior of the client.                                                                                                                                                          |

### Errors

| Error Type                       | Status Code                      | Content Type                     |
| -------------------------------- | -------------------------------- | -------------------------------- |
| models.NotFoundErrorObject       | 404                              | application/json                 |
| models.UnprocessableEntityError1 | 422                              | application/json                 |
| models.APIError                  | 4XX, 5XX                         | \*/\*                            |

## get_v1_employees_employee_id_member_portal_invitations

Returns the current status of an employee's member portal invitation (`pending`, `sent`, `verified`, `complete`, or `cancelled`) along with an `expired` flag indicating whether the invitation can still be acted on by the employee.

scope: `member_portal_invitation:read`

### Example Usage

<!-- UsageSnippet language="python" operationID="get-v1-employees-employee_id-member_portal_invitations" method="get" path="/v1/employees/{employee_id}/member_portal_invitations" -->
```python
import gusto_embedded_v_2026_06_15
from gusto_embedded_v_2026_06_15 import Gusto
import os


with Gusto(
    company_access_auth=os.getenv("GUSTO_COMPANY_ACCESS_AUTH", ""),
) as gusto:

    res = gusto.member_portal_invitations.get_v1_employees_employee_id_member_portal_invitations(employee_id="<id>", x_gusto_api_version=gusto_embedded_v_2026_06_15.GetV1EmployeesEmployeeIDMemberPortalInvitationsHeaderXGustoAPIVersion.TWO_THOUSAND_AND_TWENTY_SIX_MINUS_06_MINUS_15)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                    | Type                                                                                                                                                                                                                         | Required                                                                                                                                                                                                                     | Description                                                                                                                                                                                                                  |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `employee_id`                                                                                                                                                                                                                | *str*                                                                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                                           | The UUID of the employee                                                                                                                                                                                                     |
| `x_gusto_api_version`                                                                                                                                                                                                        | [Optional[models.GetV1EmployeesEmployeeIDMemberPortalInvitationsHeaderXGustoAPIVersion]](../../models/getv1employeesemployeeidmemberportalinvitationsheaderxgustoapiversion.md)                                              | :heavy_minus_sign:                                                                                                                                                                                                           | Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used. |
| `retries`                                                                                                                                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                           | Configuration to override the default retry behavior of the client.                                                                                                                                                          |

### Response

**[models.MemberPortalInvitation](../../models/memberportalinvitation.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.NotFoundErrorObject | 404                        | application/json           |
| models.APIError            | 4XX, 5XX                   | \*/\*                      |

## delete_v1_employees_employee_id_member_portal_invitations

Cancels the member portal invitation for the specified employee.

Note: this endpoint does not cancel the employee's self-onboarding flow. If you want the company admin to take full control of onboarding the employee, cancel the self-onboarding request instead.

scope: `member_portal_invitation:write`

### Example Usage

<!-- UsageSnippet language="python" operationID="delete-v1-employees-employee_id-member_portal_invitations" method="delete" path="/v1/employees/{employee_id}/member_portal_invitations" -->
```python
import gusto_embedded_v_2026_06_15
from gusto_embedded_v_2026_06_15 import Gusto
import os


with Gusto(
    company_access_auth=os.getenv("GUSTO_COMPANY_ACCESS_AUTH", ""),
) as gusto:

    gusto.member_portal_invitations.delete_v1_employees_employee_id_member_portal_invitations(employee_id="<id>", x_gusto_api_version=gusto_embedded_v_2026_06_15.DeleteV1EmployeesEmployeeIDMemberPortalInvitationsHeaderXGustoAPIVersion.TWO_THOUSAND_AND_TWENTY_SIX_MINUS_06_MINUS_15)

    # Use the SDK ...

```

### Parameters

| Parameter                                                                                                                                                                                                                    | Type                                                                                                                                                                                                                         | Required                                                                                                                                                                                                                     | Description                                                                                                                                                                                                                  |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `employee_id`                                                                                                                                                                                                                | *str*                                                                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                                           | The UUID of the employee                                                                                                                                                                                                     |
| `x_gusto_api_version`                                                                                                                                                                                                        | [Optional[models.DeleteV1EmployeesEmployeeIDMemberPortalInvitationsHeaderXGustoAPIVersion]](../../models/deletev1employeesemployeeidmemberportalinvitationsheaderxgustoapiversion.md)                                        | :heavy_minus_sign:                                                                                                                                                                                                           | Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used. |
| `retries`                                                                                                                                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                           | Configuration to override the default retry behavior of the client.                                                                                                                                                          |

### Errors

| Error Type                       | Status Code                      | Content Type                     |
| -------------------------------- | -------------------------------- | -------------------------------- |
| models.NotFoundErrorObject       | 404                              | application/json                 |
| models.UnprocessableEntityError1 | 422                              | application/json                 |
| models.APIError                  | 4XX, 5XX                         | \*/\*                            |

## post_v1_contractors_contractor_uuid_member_portal_invitations

Generates a member portal invitation for the specified contractor. If the contractor already has an invitation and its token has expired, calling this endpoint regenerates the invitation and overrides the prior token.

scope: `member_portal_invitation:write`

### Example Usage

<!-- UsageSnippet language="python" operationID="post-v1-contractors-contractor_uuid-member_portal_invitations" method="post" path="/v1/contractors/{contractor_uuid}/member_portal_invitations" -->
```python
import gusto_embedded_v_2026_06_15
from gusto_embedded_v_2026_06_15 import Gusto
import os


with Gusto(
    company_access_auth=os.getenv("GUSTO_COMPANY_ACCESS_AUTH", ""),
) as gusto:

    gusto.member_portal_invitations.post_v1_contractors_contractor_uuid_member_portal_invitations(contractor_uuid="<id>", x_gusto_api_version=gusto_embedded_v_2026_06_15.PostV1ContractorsContractorUUIDMemberPortalInvitationsHeaderXGustoAPIVersion.TWO_THOUSAND_AND_TWENTY_SIX_MINUS_06_MINUS_15)

    # Use the SDK ...

```

### Parameters

| Parameter                                                                                                                                                                                                                    | Type                                                                                                                                                                                                                         | Required                                                                                                                                                                                                                     | Description                                                                                                                                                                                                                  |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `contractor_uuid`                                                                                                                                                                                                            | *str*                                                                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                                           | The UUID of the contractor                                                                                                                                                                                                   |
| `x_gusto_api_version`                                                                                                                                                                                                        | [Optional[models.PostV1ContractorsContractorUUIDMemberPortalInvitationsHeaderXGustoAPIVersion]](../../models/postv1contractorscontractoruuidmemberportalinvitationsheaderxgustoapiversion.md)                                | :heavy_minus_sign:                                                                                                                                                                                                           | Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used. |
| `retries`                                                                                                                                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                           | Configuration to override the default retry behavior of the client.                                                                                                                                                          |

### Errors

| Error Type                       | Status Code                      | Content Type                     |
| -------------------------------- | -------------------------------- | -------------------------------- |
| models.NotFoundErrorObject       | 404                              | application/json                 |
| models.UnprocessableEntityError1 | 422                              | application/json                 |
| models.APIError                  | 4XX, 5XX                         | \*/\*                            |

## get_v1_contractors_contractor_uuid_member_portal_invitations

Returns the current status of a contractor's member portal invitation (`pending`, `sent`, `verified`, `complete`, or `cancelled`) along with an `expired` flag indicating whether the invitation can still be acted on by the contractor.

scope: `member_portal_invitation:read`

### Example Usage

<!-- UsageSnippet language="python" operationID="get-v1-contractors-contractor_uuid-member_portal_invitations" method="get" path="/v1/contractors/{contractor_uuid}/member_portal_invitations" -->
```python
import gusto_embedded_v_2026_06_15
from gusto_embedded_v_2026_06_15 import Gusto
import os


with Gusto(
    company_access_auth=os.getenv("GUSTO_COMPANY_ACCESS_AUTH", ""),
) as gusto:

    res = gusto.member_portal_invitations.get_v1_contractors_contractor_uuid_member_portal_invitations(contractor_uuid="<id>", x_gusto_api_version=gusto_embedded_v_2026_06_15.GetV1ContractorsContractorUUIDMemberPortalInvitationsHeaderXGustoAPIVersion.TWO_THOUSAND_AND_TWENTY_SIX_MINUS_06_MINUS_15)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                    | Type                                                                                                                                                                                                                         | Required                                                                                                                                                                                                                     | Description                                                                                                                                                                                                                  |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `contractor_uuid`                                                                                                                                                                                                            | *str*                                                                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                                           | The UUID of the contractor                                                                                                                                                                                                   |
| `x_gusto_api_version`                                                                                                                                                                                                        | [Optional[models.GetV1ContractorsContractorUUIDMemberPortalInvitationsHeaderXGustoAPIVersion]](../../models/getv1contractorscontractoruuidmemberportalinvitationsheaderxgustoapiversion.md)                                  | :heavy_minus_sign:                                                                                                                                                                                                           | Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used. |
| `retries`                                                                                                                                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                           | Configuration to override the default retry behavior of the client.                                                                                                                                                          |

### Response

**[models.MemberPortalInvitation](../../models/memberportalinvitation.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.NotFoundErrorObject | 404                        | application/json           |
| models.APIError            | 4XX, 5XX                   | \*/\*                      |

## delete_v1_contractors_contractor_uuid_member_portal_invitations

Cancels the member portal invitation for the specified contractor.

Note: this endpoint does not cancel the contractor's self-onboarding flow. If you want the company admin to take full control of onboarding the contractor, cancel the self-onboarding request instead.

scope: `member_portal_invitation:write`

### Example Usage

<!-- UsageSnippet language="python" operationID="delete-v1-contractors-contractor_uuid-member_portal_invitations" method="delete" path="/v1/contractors/{contractor_uuid}/member_portal_invitations" -->
```python
import gusto_embedded_v_2026_06_15
from gusto_embedded_v_2026_06_15 import Gusto
import os


with Gusto(
    company_access_auth=os.getenv("GUSTO_COMPANY_ACCESS_AUTH", ""),
) as gusto:

    gusto.member_portal_invitations.delete_v1_contractors_contractor_uuid_member_portal_invitations(contractor_uuid="<id>", x_gusto_api_version=gusto_embedded_v_2026_06_15.DeleteV1ContractorsContractorUUIDMemberPortalInvitationsHeaderXGustoAPIVersion.TWO_THOUSAND_AND_TWENTY_SIX_MINUS_06_MINUS_15)

    # Use the SDK ...

```

### Parameters

| Parameter                                                                                                                                                                                                                    | Type                                                                                                                                                                                                                         | Required                                                                                                                                                                                                                     | Description                                                                                                                                                                                                                  |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `contractor_uuid`                                                                                                                                                                                                            | *str*                                                                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                                           | The UUID of the contractor                                                                                                                                                                                                   |
| `x_gusto_api_version`                                                                                                                                                                                                        | [Optional[models.DeleteV1ContractorsContractorUUIDMemberPortalInvitationsHeaderXGustoAPIVersion]](../../models/deletev1contractorscontractoruuidmemberportalinvitationsheaderxgustoapiversion.md)                            | :heavy_minus_sign:                                                                                                                                                                                                           | Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used. |
| `retries`                                                                                                                                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                           | Configuration to override the default retry behavior of the client.                                                                                                                                                          |

### Errors

| Error Type                       | Status Code                      | Content Type                     |
| -------------------------------- | -------------------------------- | -------------------------------- |
| models.NotFoundErrorObject       | 404                              | application/json                 |
| models.UnprocessableEntityError1 | 422                              | application/json                 |
| models.APIError                  | 4XX, 5XX                         | \*/\*                            |