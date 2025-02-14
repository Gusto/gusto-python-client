<!-- Start SDK Example Usage [usage] -->
```python
# Synchronous Example
from gusto_embedded import Gusto
import os

with Gusto(
    company_access_auth=os.getenv("GUSTO_COMPANY_ACCESS_AUTH", ""),
) as gusto:

    res = gusto.introspection.get_info()

    # Handle response
    print(res)
```

</br>

The same SDK client can also be used to make asychronous requests by importing asyncio.
```python
# Asynchronous Example
import asyncio
from gusto_embedded import Gusto
import os

async def main():
    async with Gusto(
        company_access_auth=os.getenv("GUSTO_COMPANY_ACCESS_AUTH", ""),
    ) as gusto:

        res = await gusto.introspection.get_info_async()

        # Handle response
        print(res)

asyncio.run(main())
```
<!-- End SDK Example Usage [usage] -->