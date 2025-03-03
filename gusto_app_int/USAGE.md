<!-- Start SDK Example Usage [usage] -->
```python
# Synchronous Example
from gusto_app_integration import GustoAppIntegration


with GustoAppIntegration(
    company_access_auth="<YOUR_BEARER_TOKEN_HERE>",
) as gai_client:

    res = gai_client.introspection.get_token_info()

    # Handle response
    print(res)
```

</br>

The same SDK client can also be used to make asychronous requests by importing asyncio.
```python
# Asynchronous Example
import asyncio
from gusto_app_integration import GustoAppIntegration

async def main():

    async with GustoAppIntegration(
        company_access_auth="<YOUR_BEARER_TOKEN_HERE>",
    ) as gai_client:

        res = await gai_client.introspection.get_token_info_async()

        # Handle response
        print(res)

asyncio.run(main())
```
<!-- End SDK Example Usage [usage] -->