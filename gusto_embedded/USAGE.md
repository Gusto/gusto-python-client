<!-- Start SDK Example Usage [usage] -->
```python
# Synchronous Example
import gusto_embedded
from gusto_embedded import Gusto
import os


with Gusto(
    company_access_auth=os.getenv("GUSTO_COMPANY_ACCESS_AUTH", ""),
) as gusto:

    res = gusto.ach_transactions.get_all(company_uuid="<id>", x_gusto_api_version=gusto_embedded.XGustoAPIVersion.TWO_THOUSAND_AND_TWENTY_FIVE_MINUS_06_MINUS_15)

    # Handle response
    print(res)
```

</br>

The same SDK client can also be used to make asynchronous requests by importing asyncio.

```python
# Asynchronous Example
import asyncio
import gusto_embedded
from gusto_embedded import Gusto
import os

async def main():

    async with Gusto(
        company_access_auth=os.getenv("GUSTO_COMPANY_ACCESS_AUTH", ""),
    ) as gusto:

        res = await gusto.ach_transactions.get_all_async(company_uuid="<id>", x_gusto_api_version=gusto_embedded.XGustoAPIVersion.TWO_THOUSAND_AND_TWENTY_FIVE_MINUS_06_MINUS_15)

        # Handle response
        print(res)

asyncio.run(main())
```
<!-- End SDK Example Usage [usage] -->