<!-- Start SDK Example Usage [usage] -->
```python
# Synchronous Example
import gusto_app_integration_v_2026_06_15
from gusto_app_integration_v_2026_06_15 import GustoAppIntegration


with GustoAppIntegration(
    company_access_auth="<YOUR_BEARER_TOKEN_HERE>",
) as gusto_app_integration:

    res = gusto_app_integration.companies.get_admins(company_id="<id>", x_gusto_api_version=gusto_app_integration_v_2026_06_15.XGustoAPIVersion.TWO_THOUSAND_AND_TWENTY_SIX_MINUS_06_MINUS_15)

    # Handle response
    print(res)
```

</br>

The same SDK client can also be used to make asynchronous requests by importing asyncio.

```python
# Asynchronous Example
import asyncio
import gusto_app_integration_v_2026_06_15
from gusto_app_integration_v_2026_06_15 import GustoAppIntegration

async def main():

    async with GustoAppIntegration(
        company_access_auth="<YOUR_BEARER_TOKEN_HERE>",
    ) as gusto_app_integration:

        res = await gusto_app_integration.companies.get_admins_async(company_id="<id>", x_gusto_api_version=gusto_app_integration_v_2026_06_15.XGustoAPIVersion.TWO_THOUSAND_AND_TWENTY_SIX_MINUS_06_MINUS_15)

        # Handle response
        print(res)

asyncio.run(main())
```
<!-- End SDK Example Usage [usage] -->