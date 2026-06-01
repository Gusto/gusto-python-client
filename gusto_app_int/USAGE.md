<!-- Start SDK Example Usage [usage] -->
```python
# Synchronous Example
import gusto_app_integration
from gusto_app_integration import GustoAppIntegration


with GustoAppIntegration(
    company_access_auth="<YOUR_BEARER_TOKEN_HERE>",
) as gai_client:

    res = gai_client.introspection.get_token_info(x_gusto_api_version=gusto_app_integration.XGustoAPIVersion.TWO_THOUSAND_AND_TWENTY_FIVE_MINUS_06_MINUS_15)

    # Handle response
    print(res)
```

</br>

The same SDK client can also be used to make asynchronous requests by importing asyncio.

```python
# Asynchronous Example
import asyncio
import gusto_app_integration
from gusto_app_integration import GustoAppIntegration

async def main():

    async with GustoAppIntegration(
        company_access_auth="<YOUR_BEARER_TOKEN_HERE>",
    ) as gai_client:

        res = await gai_client.introspection.get_token_info_async(x_gusto_api_version=gusto_app_integration.XGustoAPIVersion.TWO_THOUSAND_AND_TWENTY_FIVE_MINUS_06_MINUS_15)

        # Handle response
        print(res)

asyncio.run(main())
```
<!-- End SDK Example Usage [usage] -->