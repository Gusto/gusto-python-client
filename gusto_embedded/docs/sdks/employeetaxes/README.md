# EmployeeTaxes
(*employee_taxes*)

## Overview

### Available Operations

* [update](#update) - Update an employee's state taxes

## update

Update attributes relevant for an employee's state taxes.

As described for the GET endpoint, the answers must be supplied in the effective-dated format, but currently only a single answer will be accepted - `valid_from` and `valid_up_to` must be `"2010-01-01"` and `null` respectively.

scope: `employee_state_taxes:write`

### Example Usage

```python
from gusto_embedded import Gusto
import os

with Gusto(
    company_access_auth=os.getenv("GUSTO_COMPANY_ACCESS_AUTH", ""),
) as gusto:

    res = gusto.employee_taxes.update(employee_uuid="<id>", states=[
        {
            "state": "CA",
            "questions": [
                {
                    "key": "filing_status",
                    "answers": [
                        {
                            "value": "M",
                            "valid_from": "2010-01-01",
                            "valid_up_to": None,
                        },
                    ],
                },
                {
                    "key": "withholding_allowance",
                    "answers": [
                        {
                            "value": "2",
                            "valid_from": "2010-01-01",
                            "valid_up_to": None,
                        },
                    ],
                },
                {
                    "key": "additional_withholding",
                    "answers": [
                        {
                            "value": "25.0",
                            "valid_from": "2010-01-01",
                            "valid_up_to": None,
                        },
                    ],
                },
                {
                    "key": "file_new_hire_report",
                    "answers": [
                        {
                            "value": "true",
                            "valid_from": "2010-01-01",
                            "valid_up_to": None,
                        },
                    ],
                },
            ],
        },
    ])

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                    | Type                                                                                                                                                                                                                         | Required                                                                                                                                                                                                                     | Description                                                                                                                                                                                                                  |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `employee_uuid`                                                                                                                                                                                                              | *str*                                                                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                                           | The UUID of the employee                                                                                                                                                                                                     |
| `states`                                                                                                                                                                                                                     | List[[models.States](../../models/states.md)]                                                                                                                                                                                | :heavy_check_mark:                                                                                                                                                                                                           | N/A                                                                                                                                                                                                                          |
| `x_gusto_api_version`                                                                                                                                                                                                        | [Optional[models.VersionHeader]](../../models/versionheader.md)                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                           | Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used. |
| `retries`                                                                                                                                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                           | Configuration to override the default retry behavior of the client.                                                                                                                                                          |

### Response

**[List[models.EmployeeStateTax]](../../models/.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |