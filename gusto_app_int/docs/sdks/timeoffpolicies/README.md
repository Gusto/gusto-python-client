# TimeOffPolicies
(*time_off_policies*)

## Overview

### Available Operations

* [calculate_accruing_time_off_hours](#calculate_accruing_time_off_hours) - Calculate accruing time off hours

## calculate_accruing_time_off_hours

Returns a list of accruing time off for each time off policy associated with the employee.

Factors affecting the accrued hours:
  * the time off policy accrual method (whether they get pay per hour worked, per hour paid, with / without overtime, accumulate time off based on pay period / calendar year / anniversary)
  * how many hours of work during this pay period
  * how many hours of PTO / sick hours taken during this pay period (for per hour paid policies only)
  * company pay schedule frequency (for per pay period)

If none of the parameters is passed in, the accrued time off hour will be 0.

scope: `payrolls:read`

### Example Usage

```python
from gusto_app_integration import GustoAppIntegration


with GustoAppIntegration(
    company_access_auth="<YOUR_BEARER_TOKEN_HERE>",
) as gai_client:

    res = gai_client.time_off_policies.calculate_accruing_time_off_hours(payroll_id="<id>", employee_id="<id>", regular_hours_worked=30.25, overtime_hours_worked=10, double_overtime_hours_worked=0, pto_hours_used=5.5, sick_hours_used=0)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                    | Type                                                                                                                                                                                                                         | Required                                                                                                                                                                                                                     | Description                                                                                                                                                                                                                  |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `payroll_id`                                                                                                                                                                                                                 | *str*                                                                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                                           | The UUID of the payroll                                                                                                                                                                                                      |
| `employee_id`                                                                                                                                                                                                                | *str*                                                                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                                           | The UUID of the employee                                                                                                                                                                                                     |
| `x_gusto_api_version`                                                                                                                                                                                                        | [Optional[models.VersionHeader]](../../models/versionheader.md)                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                           | Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used. |
| `regular_hours_worked`                                                                                                                                                                                                       | *Optional[float]*                                                                                                                                                                                                            | :heavy_minus_sign:                                                                                                                                                                                                           | regular hours worked in this pay period                                                                                                                                                                                      |
| `overtime_hours_worked`                                                                                                                                                                                                      | *Optional[float]*                                                                                                                                                                                                            | :heavy_minus_sign:                                                                                                                                                                                                           | overtime hours worked in this pay period                                                                                                                                                                                     |
| `double_overtime_hours_worked`                                                                                                                                                                                               | *Optional[float]*                                                                                                                                                                                                            | :heavy_minus_sign:                                                                                                                                                                                                           | double overtime hours worked in this pay period                                                                                                                                                                              |
| `pto_hours_used`                                                                                                                                                                                                             | *Optional[float]*                                                                                                                                                                                                            | :heavy_minus_sign:                                                                                                                                                                                                           | paid time off hours used in this pay period                                                                                                                                                                                  |
| `sick_hours_used`                                                                                                                                                                                                            | *Optional[float]*                                                                                                                                                                                                            | :heavy_minus_sign:                                                                                                                                                                                                           | sick hours used in this pay period                                                                                                                                                                                           |
| `retries`                                                                                                                                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                           | Configuration to override the default retry behavior of the client.                                                                                                                                                          |

### Response

**[List[models.AccruingTimeOffHour]](../../models/.md)**

### Errors

| Error Type                            | Status Code                           | Content Type                          |
| ------------------------------------- | ------------------------------------- | ------------------------------------- |
| models.UnprocessableEntityErrorObject | 422                                   | application/json                      |
| models.APIError                       | 4XX, 5XX                              | \*/\*                                 |