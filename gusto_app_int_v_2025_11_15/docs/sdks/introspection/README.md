# Introspection

## Overview

### Available Operations

* [get_token_info](#get_token_info) - Get info about the current access token
* [revoke](#revoke) - Revoke access token
* [oauth_access_token](#oauth_access_token) - Create a System Access Token or Refresh an Access Token
* [disconnect_app_integration](#disconnect_app_integration) - Disconnect an app integration

## get_token_info

Returns scope and resource information associated with the current access token. Use this endpoint to verify the following for the current access token:
* Resource (company, employee, contractor, or application) and resource owner
* Access level

### Example Usage

<!-- UsageSnippet language="python" operationID="get-v1-token-info" method="get" path="/v1/token_info" -->
```python
import gusto_app_integration_v_2025_11_15
from gusto_app_integration_v_2025_11_15 import GustoAppIntegration


with GustoAppIntegration(
    company_access_auth="<YOUR_BEARER_TOKEN_HERE>",
) as gusto_app_integration:

    res = gusto_app_integration.introspection.get_token_info(x_gusto_api_version=gusto_app_integration_v_2025_11_15.XGustoAPIVersion.TWO_THOUSAND_AND_TWENTY_FIVE_MINUS_11_MINUS_15)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                    | Type                                                                                                                                                                                                                         | Required                                                                                                                                                                                                                     | Description                                                                                                                                                                                                                  |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `x_gusto_api_version`                                                                                                                                                                                                        | [Optional[models.XGustoAPIVersion]](../../models/xgustoapiversion.md)                                                                                                                                                        | :heavy_minus_sign:                                                                                                                                                                                                           | Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used. |
| `retries`                                                                                                                                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                           | Configuration to override the default retry behavior of the client.                                                                                                                                                          |

### Response

**[models.TokenInfo](../../models/tokeninfo.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## revoke

Revokes the given access token. After revoking, this token can no longer be used to make requests nor can it be refreshed.

### Example Usage

<!-- UsageSnippet language="python" operationID="revoke-access-token" method="post" path="/oauth/revoke" -->
```python
import gusto_app_integration_v_2025_11_15
from gusto_app_integration_v_2025_11_15 import GustoAppIntegration


with GustoAppIntegration() as gusto_app_integration:

    gusto_app_integration.introspection.revoke(client_id="<id>", client_secret="<value>", token="<value>", x_gusto_api_version=gusto_app_integration_v_2025_11_15.VersionHeader.TWO_THOUSAND_AND_TWENTY_FIVE_MINUS_11_MINUS_15)

    # Use the SDK ...

```

### Parameters

| Parameter                                                                                                                                                                                                                    | Type                                                                                                                                                                                                                         | Required                                                                                                                                                                                                                     | Description                                                                                                                                                                                                                  |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `client_id`                                                                                                                                                                                                                  | *str*                                                                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                                           | Your client id                                                                                                                                                                                                               |
| `client_secret`                                                                                                                                                                                                              | *str*                                                                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                                           | Your client secret                                                                                                                                                                                                           |
| `token`                                                                                                                                                                                                                      | *str*                                                                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                                           | The access token that will be revoked.                                                                                                                                                                                       |
| `x_gusto_api_version`                                                                                                                                                                                                        | [Optional[models.VersionHeader]](../../models/versionheader.md)                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                           | Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used. |
| `retries`                                                                                                                                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                           | Configuration to override the default retry behavior of the client.                                                                                                                                                          |

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## oauth_access_token

Creates a system access token or refreshes an oauth access token

### Example Usage

<!-- UsageSnippet language="python" operationID="oauth-access-token" method="post" path="/oauth/token" -->
```python
import gusto_app_integration_v_2025_11_15
from gusto_app_integration_v_2025_11_15 import GustoAppIntegration


with GustoAppIntegration() as gusto_app_integration:

    res = gusto_app_integration.introspection.oauth_access_token(body={
        "client_id": "qr6L_9FRkbMVL_GdwvrMW6Ef8tcU6NUxjWpOfqXqOG8",
        "client_secret": "3aQSHRB3596nZhm6NdNBELZ1u9xbZmvCrKpBhbZYq6w",
        "grant_type": "system_access",
    }, x_gusto_api_version=gusto_app_integration_v_2025_11_15.HeaderXGustoAPIVersion.TWO_THOUSAND_AND_TWENTY_FIVE_MINUS_11_MINUS_15)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                    | Type                                                                                                                                                                                                                         | Required                                                                                                                                                                                                                     | Description                                                                                                                                                                                                                  |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `body`                                                                                                                                                                                                                       | [models.OauthAccessTokenRequestBody](../../models/oauthaccesstokenrequestbody.md)                                                                                                                                            | :heavy_check_mark:                                                                                                                                                                                                           | N/A                                                                                                                                                                                                                          |
| `x_gusto_api_version`                                                                                                                                                                                                        | [Optional[models.HeaderXGustoAPIVersion]](../../models/headerxgustoapiversion.md)                                                                                                                                            | :heavy_minus_sign:                                                                                                                                                                                                           | Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used. |
| `retries`                                                                                                                                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                           | Configuration to override the default retry behavior of the client.                                                                                                                                                          |

### Response

**[models.Authentication](../../models/authentication.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## disconnect_app_integration

Disconnects the given company from the App Integration associated with the current system access token. If multiple users from that company are authorized with the App Integration, then their tokens will also be revoked.

📘 System Access Authentication

This endpoint uses the [Bearer Auth scheme with the system-level access token in the HTTP Authorization header](https://docs.gusto.com/embedded-payroll/docs/system-access)

scope: `companies:disconnect_app_integration`

### Example Usage

<!-- UsageSnippet language="python" operationID="post-v1-disconnect-app-integration" method="post" path="/v1/companies/{company_id}/disconnect_app_integration" -->
```python
import gusto_app_integration_v_2025_11_15
from gusto_app_integration_v_2025_11_15 import GustoAppIntegration


with GustoAppIntegration() as gusto_app_integration:

    gusto_app_integration.introspection.disconnect_app_integration(security=gusto_app_integration_v_2025_11_15.PostV1DisconnectAppIntegrationSecurity(
        system_access_auth="<YOUR_BEARER_TOKEN_HERE>",
    ), company_id="<id>", x_gusto_api_version=gusto_app_integration_v_2025_11_15.PostV1DisconnectAppIntegrationHeaderXGustoAPIVersion.TWO_THOUSAND_AND_TWENTY_FIVE_MINUS_11_MINUS_15)

    # Use the SDK ...

```

### Parameters

| Parameter                                                                                                                                                                                                                    | Type                                                                                                                                                                                                                         | Required                                                                                                                                                                                                                     | Description                                                                                                                                                                                                                  |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `security`                                                                                                                                                                                                                   | [models.PostV1DisconnectAppIntegrationSecurity](../../models/postv1disconnectappintegrationsecurity.md)                                                                                                                      | :heavy_check_mark:                                                                                                                                                                                                           | N/A                                                                                                                                                                                                                          |
| `company_id`                                                                                                                                                                                                                 | *str*                                                                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                                           | The UUID of the company                                                                                                                                                                                                      |
| `x_gusto_api_version`                                                                                                                                                                                                        | [Optional[models.PostV1DisconnectAppIntegrationHeaderXGustoAPIVersion]](../../models/postv1disconnectappintegrationheaderxgustoapiversion.md)                                                                                | :heavy_minus_sign:                                                                                                                                                                                                           | Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used. |
| `retries`                                                                                                                                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                           | Configuration to override the default retry behavior of the client.                                                                                                                                                          |

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.NotFoundErrorObject | 404                        | application/json           |
| models.APIError            | 4XX, 5XX                   | \*/\*                      |