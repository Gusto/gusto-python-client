# EmployeeAddresses
(*employee_addresses*)

## Overview

### Available Operations

* [get](#get) - Get an employee's home addresses
* [create](#create) - Create an employee's home address
* [retrieve_home_address](#retrieve_home_address) - Get an employee's home address
* [update](#update) - Update an employee's home address
* [delete](#delete) - Delete an employee's home address
* [get_work_addresses](#get_work_addresses) - Get an employee's work addresses
* [create_work_address](#create_work_address) - Create an employee work address
* [retrieve_work_address](#retrieve_work_address) - Get an employee work address
* [update_work_address](#update_work_address) - Update an employee work address
* [delete_work_address](#delete_work_address) - Delete an employee's work address

## get

The home address of an employee is used to determine certain tax information about them. Addresses are geocoded on create and update to ensure validity.

Supports home address effective dating and courtesy withholding.

scope: `employees:read`


### Example Usage

<!-- UsageSnippet language="python" operationID="get-v1-employees-employee_id-home_addresses" method="get" path="/v1/employees/{employee_id}/home_addresses" -->
```python
import gusto_embedded
from gusto_embedded import Gusto
import os


with Gusto(
    company_access_auth=os.getenv("GUSTO_COMPANY_ACCESS_AUTH", ""),
) as gusto:

    res = gusto.employee_addresses.get(employee_id="<id>", x_gusto_api_version=gusto_embedded.GetV1EmployeesEmployeeIDHomeAddressesHeaderXGustoAPIVersion.TWO_THOUSAND_AND_TWENTY_FOUR_MINUS_04_MINUS_01)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                    | Type                                                                                                                                                                                                                         | Required                                                                                                                                                                                                                     | Description                                                                                                                                                                                                                  |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `employee_id`                                                                                                                                                                                                                | *str*                                                                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                                           | The UUID of the employee                                                                                                                                                                                                     |
| `x_gusto_api_version`                                                                                                                                                                                                        | [Optional[models.GetV1EmployeesEmployeeIDHomeAddressesHeaderXGustoAPIVersion]](../../models/getv1employeesemployeeidhomeaddressesheaderxgustoapiversion.md)                                                                  | :heavy_minus_sign:                                                                                                                                                                                                           | Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used. |
| `retries`                                                                                                                                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                           | Configuration to override the default retry behavior of the client.                                                                                                                                                          |

### Response

**[List[models.EmployeeAddress]](../../models/.md)**

### Errors

| Error Type                            | Status Code                           | Content Type                          |
| ------------------------------------- | ------------------------------------- | ------------------------------------- |
| models.UnprocessableEntityErrorObject | 404                                   | application/json                      |
| models.APIError                       | 4XX, 5XX                              | \*/\*                                 |

## create

The home address of an employee is used to determine certain tax information about them. Addresses are geocoded on create and update to ensure validity.

Supports home address effective dating and courtesy withholding.

scope: `employees:write`


### Example Usage

<!-- UsageSnippet language="python" operationID="post-v1-employees-employee_id-home_addresses" method="post" path="/v1/employees/{employee_id}/home_addresses" -->
```python
from datetime import date
import gusto_embedded
from gusto_embedded import Gusto
import os


with Gusto(
    company_access_auth=os.getenv("GUSTO_COMPANY_ACCESS_AUTH", ""),
) as gusto:

    res = gusto.employee_addresses.create(employee_id="<id>", x_gusto_api_version=gusto_embedded.PostV1EmployeesEmployeeIDHomeAddressesHeaderXGustoAPIVersion.TWO_THOUSAND_AND_TWENTY_FOUR_MINUS_04_MINUS_01, street_1="300 3rd Street", city="San Francisco", state="CA", zip_code="94107", effective_date=date.fromisoformat("2022-01-31"))

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                    | Type                                                                                                                                                                                                                         | Required                                                                                                                                                                                                                     | Description                                                                                                                                                                                                                  | Example                                                                                                                                                                                                                      |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `employee_id`                                                                                                                                                                                                                | *str*                                                                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                                           | The UUID of the employee                                                                                                                                                                                                     |                                                                                                                                                                                                                              |
| `x_gusto_api_version`                                                                                                                                                                                                        | [Optional[models.PostV1EmployeesEmployeeIDHomeAddressesHeaderXGustoAPIVersion]](../../models/postv1employeesemployeeidhomeaddressesheaderxgustoapiversion.md)                                                                | :heavy_minus_sign:                                                                                                                                                                                                           | Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used. |                                                                                                                                                                                                                              |
| `street_1`                                                                                                                                                                                                                   | *Optional[str]*                                                                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                           | N/A                                                                                                                                                                                                                          | 300 3rd Street                                                                                                                                                                                                               |
| `street_2`                                                                                                                                                                                                                   | *OptionalNullable[str]*                                                                                                                                                                                                      | :heavy_minus_sign:                                                                                                                                                                                                           | N/A                                                                                                                                                                                                                          |                                                                                                                                                                                                                              |
| `city`                                                                                                                                                                                                                       | *Optional[str]*                                                                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                           | N/A                                                                                                                                                                                                                          | San Francisco                                                                                                                                                                                                                |
| `state`                                                                                                                                                                                                                      | *Optional[str]*                                                                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                           | N/A                                                                                                                                                                                                                          | CA                                                                                                                                                                                                                           |
| `zip_code`                                                                                                                                                                                                                   | *Optional[str]*                                                                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                           | N/A                                                                                                                                                                                                                          | 94107                                                                                                                                                                                                                        |
| `effective_date`                                                                                                                                                                                                             | [datetime](https://docs.python.org/3/library/datetime.html#datetime-objects)                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                                                                           | N/A                                                                                                                                                                                                                          | 2022-01-31                                                                                                                                                                                                                   |
| `courtesy_withholding`                                                                                                                                                                                                       | *Optional[bool]*                                                                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                           | N/A                                                                                                                                                                                                                          |                                                                                                                                                                                                                              |
| `retries`                                                                                                                                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                           | Configuration to override the default retry behavior of the client.                                                                                                                                                          |                                                                                                                                                                                                                              |

### Response

**[models.EmployeeAddress](../../models/employeeaddress.md)**

### Errors

| Error Type                            | Status Code                           | Content Type                          |
| ------------------------------------- | ------------------------------------- | ------------------------------------- |
| models.UnprocessableEntityErrorObject | 404, 422                              | application/json                      |
| models.APIError                       | 4XX, 5XX                              | \*/\*                                 |

## retrieve_home_address

The home address of an employee is used to determine certain tax information about them. Addresses are geocoded on create and update to ensure validity.

Supports home address effective dating and courtesy withholding.

scope: `employees:read`


### Example Usage

<!-- UsageSnippet language="python" operationID="get-v1-home_addresses-home_address_uuid" method="get" path="/v1/home_addresses/{home_address_uuid}" -->
```python
import gusto_embedded
from gusto_embedded import Gusto
import os


with Gusto(
    company_access_auth=os.getenv("GUSTO_COMPANY_ACCESS_AUTH", ""),
) as gusto:

    res = gusto.employee_addresses.retrieve_home_address(home_address_uuid="<id>", x_gusto_api_version=gusto_embedded.GetV1HomeAddressesHomeAddressUUIDHeaderXGustoAPIVersion.TWO_THOUSAND_AND_TWENTY_FOUR_MINUS_04_MINUS_01)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                    | Type                                                                                                                                                                                                                         | Required                                                                                                                                                                                                                     | Description                                                                                                                                                                                                                  |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `home_address_uuid`                                                                                                                                                                                                          | *str*                                                                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                                           | The UUID of the home address                                                                                                                                                                                                 |
| `x_gusto_api_version`                                                                                                                                                                                                        | [Optional[models.GetV1HomeAddressesHomeAddressUUIDHeaderXGustoAPIVersion]](../../models/getv1homeaddresseshomeaddressuuidheaderxgustoapiversion.md)                                                                          | :heavy_minus_sign:                                                                                                                                                                                                           | Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used. |
| `retries`                                                                                                                                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                           | Configuration to override the default retry behavior of the client.                                                                                                                                                          |

### Response

**[models.EmployeeAddress](../../models/employeeaddress.md)**

### Errors

| Error Type                            | Status Code                           | Content Type                          |
| ------------------------------------- | ------------------------------------- | ------------------------------------- |
| models.UnprocessableEntityErrorObject | 404                                   | application/json                      |
| models.APIError                       | 4XX, 5XX                              | \*/\*                                 |

## update

The home address of an employee is used to determine certain tax information about them. Addresses are geocoded on create and update to ensure validity.

Supports home address effective dating and courtesy withholding.

scope: `employees:write`


### Example Usage

<!-- UsageSnippet language="python" operationID="put-v1-home_addresses-home_address_uuid" method="put" path="/v1/home_addresses/{home_address_uuid}" -->
```python
import gusto_embedded
from gusto_embedded import Gusto
import os


with Gusto(
    company_access_auth=os.getenv("GUSTO_COMPANY_ACCESS_AUTH", ""),
) as gusto:

    res = gusto.employee_addresses.update(home_address_uuid="<id>", version="56d00c178bc7393b2a206ed6a86afcb4", x_gusto_api_version=gusto_embedded.PutV1HomeAddressesHomeAddressUUIDHeaderXGustoAPIVersion.TWO_THOUSAND_AND_TWENTY_FOUR_MINUS_04_MINUS_01)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                    | Type                                                                                                                                                                                                                         | Required                                                                                                                                                                                                                     | Description                                                                                                                                                                                                                  | Example                                                                                                                                                                                                                      |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `home_address_uuid`                                                                                                                                                                                                          | *str*                                                                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                                           | The UUID of the home address                                                                                                                                                                                                 |                                                                                                                                                                                                                              |
| `version`                                                                                                                                                                                                                    | *str*                                                                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                                           | The current version of the object. See the [versioning guide](https://docs.gusto.com/embedded-payroll/docs/idempotency) for information on how to use this field.                                                            | 56d00c178bc7393b2a206ed6a86afcb4                                                                                                                                                                                             |
| `x_gusto_api_version`                                                                                                                                                                                                        | [Optional[models.PutV1HomeAddressesHomeAddressUUIDHeaderXGustoAPIVersion]](../../models/putv1homeaddresseshomeaddressuuidheaderxgustoapiversion.md)                                                                          | :heavy_minus_sign:                                                                                                                                                                                                           | Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used. |                                                                                                                                                                                                                              |
| `street_1`                                                                                                                                                                                                                   | *Optional[str]*                                                                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                           | N/A                                                                                                                                                                                                                          |                                                                                                                                                                                                                              |
| `street_2`                                                                                                                                                                                                                   | *OptionalNullable[str]*                                                                                                                                                                                                      | :heavy_minus_sign:                                                                                                                                                                                                           | N/A                                                                                                                                                                                                                          |                                                                                                                                                                                                                              |
| `city`                                                                                                                                                                                                                       | *Optional[str]*                                                                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                           | N/A                                                                                                                                                                                                                          |                                                                                                                                                                                                                              |
| `state`                                                                                                                                                                                                                      | *Optional[str]*                                                                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                           | N/A                                                                                                                                                                                                                          |                                                                                                                                                                                                                              |
| `zip_code`                                                                                                                                                                                                                   | *Optional[str]*                                                                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                           | N/A                                                                                                                                                                                                                          |                                                                                                                                                                                                                              |
| `effective_date`                                                                                                                                                                                                             | [datetime](https://docs.python.org/3/library/datetime.html#datetime-objects)                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                                                                           | N/A                                                                                                                                                                                                                          |                                                                                                                                                                                                                              |
| `courtesy_withholding`                                                                                                                                                                                                       | *Optional[bool]*                                                                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                           | N/A                                                                                                                                                                                                                          |                                                                                                                                                                                                                              |
| `retries`                                                                                                                                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                           | Configuration to override the default retry behavior of the client.                                                                                                                                                          |                                                                                                                                                                                                                              |

### Response

**[models.EmployeeAddress](../../models/employeeaddress.md)**

### Errors

| Error Type                            | Status Code                           | Content Type                          |
| ------------------------------------- | ------------------------------------- | ------------------------------------- |
| models.UnprocessableEntityErrorObject | 404, 422                              | application/json                      |
| models.APIError                       | 4XX, 5XX                              | \*/\*                                 |

## delete

Used for deleting an employee's home address. Cannot delete the employee's active home address.

scope: `employees:write`


### Example Usage

<!-- UsageSnippet language="python" operationID="delete-v1-home_addresses-home_address_uuid" method="delete" path="/v1/home_addresses/{home_address_uuid}" -->
```python
import gusto_embedded
from gusto_embedded import Gusto
import os


with Gusto(
    company_access_auth=os.getenv("GUSTO_COMPANY_ACCESS_AUTH", ""),
) as gusto:

    gusto.employee_addresses.delete(home_address_uuid="<id>", x_gusto_api_version=gusto_embedded.DeleteV1HomeAddressesHomeAddressUUIDHeaderXGustoAPIVersion.TWO_THOUSAND_AND_TWENTY_FOUR_MINUS_04_MINUS_01)

    # Use the SDK ...

```

### Parameters

| Parameter                                                                                                                                                                                                                    | Type                                                                                                                                                                                                                         | Required                                                                                                                                                                                                                     | Description                                                                                                                                                                                                                  |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `home_address_uuid`                                                                                                                                                                                                          | *str*                                                                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                                           | The UUID of the home address                                                                                                                                                                                                 |
| `x_gusto_api_version`                                                                                                                                                                                                        | [Optional[models.DeleteV1HomeAddressesHomeAddressUUIDHeaderXGustoAPIVersion]](../../models/deletev1homeaddresseshomeaddressuuidheaderxgustoapiversion.md)                                                                    | :heavy_minus_sign:                                                                                                                                                                                                           | Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used. |
| `retries`                                                                                                                                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                           | Configuration to override the default retry behavior of the client.                                                                                                                                                          |

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## get_work_addresses

Returns a list of an employee's work addresses. Each address includes its effective
date and a boolean signifying if it is the currently active work address.

scope: `employees:read`


### Example Usage

<!-- UsageSnippet language="python" operationID="get-v1-employees-employee_id-work_addresses" method="get" path="/v1/employees/{employee_id}/work_addresses" -->
```python
import gusto_embedded
from gusto_embedded import Gusto
import os


with Gusto(
    company_access_auth=os.getenv("GUSTO_COMPANY_ACCESS_AUTH", ""),
) as gusto:

    res = gusto.employee_addresses.get_work_addresses(employee_id="<id>", x_gusto_api_version=gusto_embedded.GetV1EmployeesEmployeeIDWorkAddressesHeaderXGustoAPIVersion.TWO_THOUSAND_AND_TWENTY_FOUR_MINUS_04_MINUS_01)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                    | Type                                                                                                                                                                                                                         | Required                                                                                                                                                                                                                     | Description                                                                                                                                                                                                                  |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `employee_id`                                                                                                                                                                                                                | *str*                                                                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                                           | The UUID of the employee                                                                                                                                                                                                     |
| `x_gusto_api_version`                                                                                                                                                                                                        | [Optional[models.GetV1EmployeesEmployeeIDWorkAddressesHeaderXGustoAPIVersion]](../../models/getv1employeesemployeeidworkaddressesheaderxgustoapiversion.md)                                                                  | :heavy_minus_sign:                                                                                                                                                                                                           | Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used. |
| `retries`                                                                                                                                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                           | Configuration to override the default retry behavior of the client.                                                                                                                                                          |

### Response

**[List[models.EmployeeWorkAddress]](../../models/.md)**

### Errors

| Error Type                            | Status Code                           | Content Type                          |
| ------------------------------------- | ------------------------------------- | ------------------------------------- |
| models.UnprocessableEntityErrorObject | 404                                   | application/json                      |
| models.APIError                       | 4XX, 5XX                              | \*/\*                                 |

## create_work_address

The work address of an employee describes when an employee began working at an associated company location.

scope: `employees:manage`


### Example Usage

<!-- UsageSnippet language="python" operationID="post-v1-employees-employee_id-work_addresses" method="post" path="/v1/employees/{employee_id}/work_addresses" -->
```python
from datetime import date
import gusto_embedded
from gusto_embedded import Gusto
import os


with Gusto(
    company_access_auth=os.getenv("GUSTO_COMPANY_ACCESS_AUTH", ""),
) as gusto:

    res = gusto.employee_addresses.create_work_address(employee_id="<id>", x_gusto_api_version=gusto_embedded.PostV1EmployeesEmployeeIDWorkAddressesHeaderXGustoAPIVersion.TWO_THOUSAND_AND_TWENTY_FOUR_MINUS_04_MINUS_01, location_uuid="6a119be7-b4b0-4e27-aaa0-89d5f2524635", effective_date=date.fromisoformat("2023-05-15"))

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                    | Type                                                                                                                                                                                                                         | Required                                                                                                                                                                                                                     | Description                                                                                                                                                                                                                  | Example                                                                                                                                                                                                                      |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `employee_id`                                                                                                                                                                                                                | *str*                                                                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                                           | The UUID of the employee                                                                                                                                                                                                     |                                                                                                                                                                                                                              |
| `x_gusto_api_version`                                                                                                                                                                                                        | [Optional[models.PostV1EmployeesEmployeeIDWorkAddressesHeaderXGustoAPIVersion]](../../models/postv1employeesemployeeidworkaddressesheaderxgustoapiversion.md)                                                                | :heavy_minus_sign:                                                                                                                                                                                                           | Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used. |                                                                                                                                                                                                                              |
| `location_uuid`                                                                                                                                                                                                              | *Optional[str]*                                                                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                           | Reference to a company location                                                                                                                                                                                              | 6a119be7-b4b0-4e27-aaa0-89d5f2524635                                                                                                                                                                                         |
| `effective_date`                                                                                                                                                                                                             | [datetime](https://docs.python.org/3/library/datetime.html#datetime-objects)                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                                                                           | Date the employee began working at the company location                                                                                                                                                                      | 2023-05-15                                                                                                                                                                                                                   |
| `retries`                                                                                                                                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                           | Configuration to override the default retry behavior of the client.                                                                                                                                                          |                                                                                                                                                                                                                              |

### Response

**[models.EmployeeWorkAddress](../../models/employeeworkaddress.md)**

### Errors

| Error Type                            | Status Code                           | Content Type                          |
| ------------------------------------- | ------------------------------------- | ------------------------------------- |
| models.UnprocessableEntityErrorObject | 404, 422                              | application/json                      |
| models.APIError                       | 4XX, 5XX                              | \*/\*                                 |

## retrieve_work_address

The work address of an employee is used for payroll tax purposes.

scope: `employees:read`


### Example Usage

<!-- UsageSnippet language="python" operationID="get-v1-work_addresses-work_address_uuid" method="get" path="/v1/work_addresses/{work_address_uuid}" -->
```python
import gusto_embedded
from gusto_embedded import Gusto
import os


with Gusto(
    company_access_auth=os.getenv("GUSTO_COMPANY_ACCESS_AUTH", ""),
) as gusto:

    res = gusto.employee_addresses.retrieve_work_address(work_address_uuid="<id>", x_gusto_api_version=gusto_embedded.GetV1WorkAddressesWorkAddressUUIDHeaderXGustoAPIVersion.TWO_THOUSAND_AND_TWENTY_FOUR_MINUS_04_MINUS_01)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                    | Type                                                                                                                                                                                                                         | Required                                                                                                                                                                                                                     | Description                                                                                                                                                                                                                  |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `work_address_uuid`                                                                                                                                                                                                          | *str*                                                                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                                           | The UUID of the work address                                                                                                                                                                                                 |
| `x_gusto_api_version`                                                                                                                                                                                                        | [Optional[models.GetV1WorkAddressesWorkAddressUUIDHeaderXGustoAPIVersion]](../../models/getv1workaddressesworkaddressuuidheaderxgustoapiversion.md)                                                                          | :heavy_minus_sign:                                                                                                                                                                                                           | Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used. |
| `retries`                                                                                                                                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                           | Configuration to override the default retry behavior of the client.                                                                                                                                                          |

### Response

**[models.EmployeeWorkAddress](../../models/employeeworkaddress.md)**

### Errors

| Error Type                            | Status Code                           | Content Type                          |
| ------------------------------------- | ------------------------------------- | ------------------------------------- |
| models.UnprocessableEntityErrorObject | 404                                   | application/json                      |
| models.APIError                       | 4XX, 5XX                              | \*/\*                                 |

## update_work_address

The work address of an employee is used for payroll tax purposes.

scope: `employees:manage`


### Example Usage

<!-- UsageSnippet language="python" operationID="put-v1-work_addresses-work_address_uuid" method="put" path="/v1/work_addresses/{work_address_uuid}" -->
```python
from datetime import date
import gusto_embedded
from gusto_embedded import Gusto
import os


with Gusto(
    company_access_auth=os.getenv("GUSTO_COMPANY_ACCESS_AUTH", ""),
) as gusto:

    res = gusto.employee_addresses.update_work_address(work_address_uuid="<id>", version="56d00c178bc7393b2a206ed6a86afcb4", x_gusto_api_version=gusto_embedded.PutV1WorkAddressesWorkAddressUUIDHeaderXGustoAPIVersion.TWO_THOUSAND_AND_TWENTY_FOUR_MINUS_04_MINUS_01, location_uuid="6a119be7-b4b0-4e27-aaa0-89d5f2524635", effective_date=date.fromisoformat("2023-05-15"))

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                    | Type                                                                                                                                                                                                                         | Required                                                                                                                                                                                                                     | Description                                                                                                                                                                                                                  | Example                                                                                                                                                                                                                      |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `work_address_uuid`                                                                                                                                                                                                          | *str*                                                                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                                           | The UUID of the work address                                                                                                                                                                                                 |                                                                                                                                                                                                                              |
| `version`                                                                                                                                                                                                                    | *str*                                                                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                                           | The current version of the object. See the [versioning guide](https://docs.gusto.com/embedded-payroll/docs/idempotency) for information on how to use this field.                                                            | 56d00c178bc7393b2a206ed6a86afcb4                                                                                                                                                                                             |
| `x_gusto_api_version`                                                                                                                                                                                                        | [Optional[models.PutV1WorkAddressesWorkAddressUUIDHeaderXGustoAPIVersion]](../../models/putv1workaddressesworkaddressuuidheaderxgustoapiversion.md)                                                                          | :heavy_minus_sign:                                                                                                                                                                                                           | Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used. |                                                                                                                                                                                                                              |
| `location_uuid`                                                                                                                                                                                                              | *Optional[str]*                                                                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                           | Reference to a company location                                                                                                                                                                                              | 6a119be7-b4b0-4e27-aaa0-89d5f2524635                                                                                                                                                                                         |
| `effective_date`                                                                                                                                                                                                             | [datetime](https://docs.python.org/3/library/datetime.html#datetime-objects)                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                                                                           | N/A                                                                                                                                                                                                                          | 2023-05-15                                                                                                                                                                                                                   |
| `retries`                                                                                                                                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                           | Configuration to override the default retry behavior of the client.                                                                                                                                                          |                                                                                                                                                                                                                              |

### Response

**[models.EmployeeWorkAddress](../../models/employeeworkaddress.md)**

### Errors

| Error Type                            | Status Code                           | Content Type                          |
| ------------------------------------- | ------------------------------------- | ------------------------------------- |
| models.UnprocessableEntityErrorObject | 404, 422                              | application/json                      |
| models.APIError                       | 4XX, 5XX                              | \*/\*                                 |

## delete_work_address

Used for deleting an employee's work address. Cannot delete the employee's active work address.

scope: `employees:manage`


### Example Usage

<!-- UsageSnippet language="python" operationID="delete-v1-work_addresses-work_address_uuid" method="delete" path="/v1/work_addresses/{work_address_uuid}" -->
```python
import gusto_embedded
from gusto_embedded import Gusto
import os


with Gusto(
    company_access_auth=os.getenv("GUSTO_COMPANY_ACCESS_AUTH", ""),
) as gusto:

    gusto.employee_addresses.delete_work_address(work_address_uuid="<id>", x_gusto_api_version=gusto_embedded.DeleteV1WorkAddressesWorkAddressUUIDHeaderXGustoAPIVersion.TWO_THOUSAND_AND_TWENTY_FOUR_MINUS_04_MINUS_01)

    # Use the SDK ...

```

### Parameters

| Parameter                                                                                                                                                                                                                    | Type                                                                                                                                                                                                                         | Required                                                                                                                                                                                                                     | Description                                                                                                                                                                                                                  |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `work_address_uuid`                                                                                                                                                                                                          | *str*                                                                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                                           | The UUID of the work address                                                                                                                                                                                                 |
| `x_gusto_api_version`                                                                                                                                                                                                        | [Optional[models.DeleteV1WorkAddressesWorkAddressUUIDHeaderXGustoAPIVersion]](../../models/deletev1workaddressesworkaddressuuidheaderxgustoapiversion.md)                                                                    | :heavy_minus_sign:                                                                                                                                                                                                           | Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used. |
| `retries`                                                                                                                                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                           | Configuration to override the default retry behavior of the client.                                                                                                                                                          |

### Errors

| Error Type                            | Status Code                           | Content Type                          |
| ------------------------------------- | ------------------------------------- | ------------------------------------- |
| models.UnprocessableEntityErrorObject | 404, 422                              | application/json                      |
| models.APIError                       | 4XX, 5XX                              | \*/\*                                 |