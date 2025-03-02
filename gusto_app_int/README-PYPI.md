# gusto_app_integration

Developer-friendly & type-safe Python SDK specifically catered to leverage *gusto_app_integration* API.

<div align="left">
    <a href="https://www.speakeasy.com/?utm_source=gusto-app-integration&utm_campaign=python"><img src="https://custom-icon-badges.demolab.com/badge/-Built%20By%20Speakeasy-212015?style=for-the-badge&logoColor=FBE331&logo=speakeasy&labelColor=545454" /></a>
    <a href="https://opensource.org/licenses/MIT">
        <img src="https://img.shields.io/badge/License-MIT-blue.svg" style="width: 100px; height: 28px;" />
    </a>
</div>


<br /><br />
> [!IMPORTANT]
> This SDK is not yet ready for production use. To complete setup please follow the steps outlined in your [workspace](https://app.speakeasy.com/org/gusto/ruby-sdk). Delete this section before > publishing to a package manager.

<!-- Start Summary [summary] -->
## Summary

Gusto API: Welcome to Gusto's Embedded Payroll API documentation!
<!-- End Summary [summary] -->

<!-- Start Table of Contents [toc] -->
## Table of Contents
<!-- $toc-max-depth=2 -->
* [gusto_app_integration](https://github.com/Gusto/gusto-python-client/blob/master/#gustoappintegration)
  * [SDK Installation](https://github.com/Gusto/gusto-python-client/blob/master/#sdk-installation)
  * [IDE Support](https://github.com/Gusto/gusto-python-client/blob/master/#ide-support)
  * [SDK Example Usage](https://github.com/Gusto/gusto-python-client/blob/master/#sdk-example-usage)
  * [Authentication](https://github.com/Gusto/gusto-python-client/blob/master/#authentication)
  * [Available Resources and Operations](https://github.com/Gusto/gusto-python-client/blob/master/#available-resources-and-operations)
  * [Retries](https://github.com/Gusto/gusto-python-client/blob/master/#retries)
  * [Error Handling](https://github.com/Gusto/gusto-python-client/blob/master/#error-handling)
  * [Server Selection](https://github.com/Gusto/gusto-python-client/blob/master/#server-selection)
  * [Custom HTTP Client](https://github.com/Gusto/gusto-python-client/blob/master/#custom-http-client)
  * [Resource Management](https://github.com/Gusto/gusto-python-client/blob/master/#resource-management)
  * [Debugging](https://github.com/Gusto/gusto-python-client/blob/master/#debugging)
* [Development](https://github.com/Gusto/gusto-python-client/blob/master/#development)
  * [Maturity](https://github.com/Gusto/gusto-python-client/blob/master/#maturity)
  * [Contributions](https://github.com/Gusto/gusto-python-client/blob/master/#contributions)

<!-- End Table of Contents [toc] -->

<!-- Start SDK Installation [installation] -->
## SDK Installation

> [!NOTE]
> **Python version upgrade policy**
>
> Once a Python version reaches its [official end of life date](https://devguide.python.org/versions/), a 3-month grace period is provided for users to upgrade. Following this grace period, the minimum python version supported in the SDK will be updated.

The SDK can be installed with either *pip* or *poetry* package managers.

### PIP

*PIP* is the default package installer for Python, enabling easy installation and management of packages from PyPI via the command line.

```bash
pip install gusto_app_integration
```

### Poetry

*Poetry* is a modern tool that simplifies dependency management and package publishing by using a single `pyproject.toml` file to handle project metadata and dependencies.

```bash
poetry add gusto_app_integration
```

### Shell and script usage with `uv`

You can use this SDK in a Python shell with [uv](https://docs.astral.sh/uv/) and the `uvx` command that comes with it like so:

```shell
uvx --from gusto_app_integration python
```

It's also possible to write a standalone Python script without needing to set up a whole project like so:

```python
#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.9"
# dependencies = [
#     "gusto_app_integration",
# ]
# ///

from gusto_app_integration import GustoAppIntegration

sdk = GustoAppIntegration(
  # SDK arguments
)

# Rest of script here...
```

Once that is saved to a file, you can run it with `uv run script.py` where
`script.py` can be replaced with the actual file name.
<!-- End SDK Installation [installation] -->

<!-- Start IDE Support [idesupport] -->
## IDE Support

### PyCharm

Generally, the SDK will work well with most IDEs out of the box. However, when using PyCharm, you can enjoy much better integration with Pydantic by installing an additional plugin.

- [PyCharm Pydantic Plugin](https://docs.pydantic.dev/latest/integrations/pycharm/)
<!-- End IDE Support [idesupport] -->

<!-- Start SDK Example Usage [usage] -->
## SDK Example Usage

### Example

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

<!-- Start Authentication [security] -->
## Authentication

### Per-Client Security Schemes

This SDK supports the following security scheme globally:

| Name                  | Type | Scheme      |
| --------------------- | ---- | ----------- |
| `company_access_auth` | http | HTTP Bearer |

To authenticate with the API the `company_access_auth` parameter must be set when initializing the SDK client instance. For example:
```python
from gusto_app_integration import GustoAppIntegration


with GustoAppIntegration(
    company_access_auth="<YOUR_BEARER_TOKEN_HERE>",
) as gai_client:

    res = gai_client.introspection.get_token_info()

    # Handle response
    print(res)

```

### Per-Operation Security Schemes

Some operations in this SDK require the security scheme to be specified at the request level. For example:
```python
import gusto_app_integration
from gusto_app_integration import GustoAppIntegration


with GustoAppIntegration() as gai_client:

    gai_client.introspection.disconnect_app_integration(security=gusto_app_integration.PostV1DisconnectAppIntegrationSecurity(
        system_access_auth="<YOUR_BEARER_TOKEN_HERE>",
    ), company_id="<id>")

    # Use the SDK ...

```
<!-- End Authentication [security] -->

<!-- Start Available Resources and Operations [operations] -->
## Available Resources and Operations

<details open>
<summary>Available methods</summary>

### [companies](https://github.com/Gusto/gusto-python-client/blob/master/docs/sdks/companies/README.md)

* [provision](https://github.com/Gusto/gusto-python-client/blob/master/docs/sdks/companies/README.md#provision) - Create a company
* [get](https://github.com/Gusto/gusto-python-client/blob/master/docs/sdks/companies/README.md#get) - Get a company
* [update](https://github.com/Gusto/gusto-python-client/blob/master/docs/sdks/companies/README.md#update) - Update a company
* [get_admins](https://github.com/Gusto/gusto-python-client/blob/master/docs/sdks/companies/README.md#get_admins) - Get all the admins at a company
* [get_custom_fields](https://github.com/Gusto/gusto-python-client/blob/master/docs/sdks/companies/README.md#get_custom_fields) - Get the custom fields of a company

### [company_benefits](https://github.com/Gusto/gusto-python-client/blob/master/docs/sdks/companybenefits/README.md)

* [create](https://github.com/Gusto/gusto-python-client/blob/master/docs/sdks/companybenefits/README.md#create) - Create a company benefit
* [list](https://github.com/Gusto/gusto-python-client/blob/master/docs/sdks/companybenefits/README.md#list) - Get benefits for a company
* [get_by_id](https://github.com/Gusto/gusto-python-client/blob/master/docs/sdks/companybenefits/README.md#get_by_id) - Get a company benefit
* [update](https://github.com/Gusto/gusto-python-client/blob/master/docs/sdks/companybenefits/README.md#update) - Update a company benefit
* [delete](https://github.com/Gusto/gusto-python-client/blob/master/docs/sdks/companybenefits/README.md#delete) - Delete a company benefit
* [list_supported](https://github.com/Gusto/gusto-python-client/blob/master/docs/sdks/companybenefits/README.md#list_supported) - Get all benefits supported by Gusto
* [get](https://github.com/Gusto/gusto-python-client/blob/master/docs/sdks/companybenefits/README.md#get) - Get a supported benefit by ID
* [get_summary](https://github.com/Gusto/gusto-python-client/blob/master/docs/sdks/companybenefits/README.md#get_summary) - Get company benefit summary by company benefit id.
* [get_employee_benefits](https://github.com/Gusto/gusto-python-client/blob/master/docs/sdks/companybenefits/README.md#get_employee_benefits) - Get all employee benefits for a company benefit
* [bulk_update_employee_benefits](https://github.com/Gusto/gusto-python-client/blob/master/docs/sdks/companybenefits/README.md#bulk_update_employee_benefits) - Bulk update employee benefits for a company benefit
* [get_requirements](https://github.com/Gusto/gusto-python-client/blob/master/docs/sdks/companybenefits/README.md#get_requirements) - Get benefit fields requirements by ID

### [company_locations](https://github.com/Gusto/gusto-python-client/blob/master/docs/sdks/companylocations/README.md)

* [list](https://github.com/Gusto/gusto-python-client/blob/master/docs/sdks/companylocations/README.md#list) - Get company locations

### [contractor_payment_groups](https://github.com/Gusto/gusto-python-client/blob/master/docs/sdks/contractorpaymentgroups/README.md)

* [get](https://github.com/Gusto/gusto-python-client/blob/master/docs/sdks/contractorpaymentgroups/README.md#get) - Get contractor payment groups for a company
* [preview](https://github.com/Gusto/gusto-python-client/blob/master/docs/sdks/contractorpaymentgroups/README.md#preview) - Preview a contractor payment group
* [fetch](https://github.com/Gusto/gusto-python-client/blob/master/docs/sdks/contractorpaymentgroups/README.md#fetch) - Fetch a contractor payment group

### [contractor_payments](https://github.com/Gusto/gusto-python-client/blob/master/docs/sdks/contractorpayments/README.md)

* [get](https://github.com/Gusto/gusto-python-client/blob/master/docs/sdks/contractorpayments/README.md#get) - Get contractor payments for a company
* [get_by_id](https://github.com/Gusto/gusto-python-client/blob/master/docs/sdks/contractorpayments/README.md#get_by_id) - Get a single contractor payment

### [contractors](https://github.com/Gusto/gusto-python-client/blob/master/docs/sdks/contractors/README.md)

* [create](https://github.com/Gusto/gusto-python-client/blob/master/docs/sdks/contractors/README.md#create) - Create a contractor
* [get](https://github.com/Gusto/gusto-python-client/blob/master/docs/sdks/contractors/README.md#get) - Get contractors of a company
* [get_by_id](https://github.com/Gusto/gusto-python-client/blob/master/docs/sdks/contractors/README.md#get_by_id) - Get a contractor
* [update](https://github.com/Gusto/gusto-python-client/blob/master/docs/sdks/contractors/README.md#update) - Update a contractor

### [departments](https://github.com/Gusto/gusto-python-client/blob/master/docs/sdks/departments/README.md)

* [create](https://github.com/Gusto/gusto-python-client/blob/master/docs/sdks/departments/README.md#create) - Create a department
* [get_all](https://github.com/Gusto/gusto-python-client/blob/master/docs/sdks/departments/README.md#get_all) - Get all departments of a company
* [get](https://github.com/Gusto/gusto-python-client/blob/master/docs/sdks/departments/README.md#get) - Get a department
* [update](https://github.com/Gusto/gusto-python-client/blob/master/docs/sdks/departments/README.md#update) - Update a department
* [delete](https://github.com/Gusto/gusto-python-client/blob/master/docs/sdks/departments/README.md#delete) - Delete a department
* [add_people](https://github.com/Gusto/gusto-python-client/blob/master/docs/sdks/departments/README.md#add_people) - Add people to a department
* [remove_people](https://github.com/Gusto/gusto-python-client/blob/master/docs/sdks/departments/README.md#remove_people) - Remove people from a department

### [earning_types](https://github.com/Gusto/gusto-python-client/blob/master/docs/sdks/earningtypes/README.md)

* [create](https://github.com/Gusto/gusto-python-client/blob/master/docs/sdks/earningtypes/README.md#create) - Create a custom earning type
* [get](https://github.com/Gusto/gusto-python-client/blob/master/docs/sdks/earningtypes/README.md#get) - Get all earning types for a company
* [update](https://github.com/Gusto/gusto-python-client/blob/master/docs/sdks/earningtypes/README.md#update) - Update an earning type
* [deactivate](https://github.com/Gusto/gusto-python-client/blob/master/docs/sdks/earningtypes/README.md#deactivate) - Deactivate an earning type

### [employee_addresses](https://github.com/Gusto/gusto-python-client/blob/master/docs/sdks/employeeaddresses/README.md)

* [list_home_addresses](https://github.com/Gusto/gusto-python-client/blob/master/docs/sdks/employeeaddresses/README.md#list_home_addresses) - Get an employee's home addresses
* [create](https://github.com/Gusto/gusto-python-client/blob/master/docs/sdks/employeeaddresses/README.md#create) - Create an employee's home address
* [get](https://github.com/Gusto/gusto-python-client/blob/master/docs/sdks/employeeaddresses/README.md#get) - Get an employee's home address
* [update](https://github.com/Gusto/gusto-python-client/blob/master/docs/sdks/employeeaddresses/README.md#update) - Update an employee's home address
* [delete_home_address](https://github.com/Gusto/gusto-python-client/blob/master/docs/sdks/employeeaddresses/README.md#delete_home_address) - Delete an employee's home address
* [get_work_addresses](https://github.com/Gusto/gusto-python-client/blob/master/docs/sdks/employeeaddresses/README.md#get_work_addresses) - Get an employee's work addresses
* [create_work_address](https://github.com/Gusto/gusto-python-client/blob/master/docs/sdks/employeeaddresses/README.md#create_work_address) - Create an employee work address
* [get_work_address](https://github.com/Gusto/gusto-python-client/blob/master/docs/sdks/employeeaddresses/README.md#get_work_address) - Get an employee work address
* [update_work_address](https://github.com/Gusto/gusto-python-client/blob/master/docs/sdks/employeeaddresses/README.md#update_work_address) - Update an employee work address
* [delete_work_address](https://github.com/Gusto/gusto-python-client/blob/master/docs/sdks/employeeaddresses/README.md#delete_work_address) - Delete an employee's work address

### [employee_benefits](https://github.com/Gusto/gusto-python-client/blob/master/docs/sdks/employeebenefits/README.md)

* [create](https://github.com/Gusto/gusto-python-client/blob/master/docs/sdks/employeebenefits/README.md#create) - Create an employee benefit
* [get_all](https://github.com/Gusto/gusto-python-client/blob/master/docs/sdks/employeebenefits/README.md#get_all) - Get all benefits for an employee
* [get](https://github.com/Gusto/gusto-python-client/blob/master/docs/sdks/employeebenefits/README.md#get) - Get an employee benefit
* [update](https://github.com/Gusto/gusto-python-client/blob/master/docs/sdks/employeebenefits/README.md#update) - Update an employee benefit
* [delete](https://github.com/Gusto/gusto-python-client/blob/master/docs/sdks/employeebenefits/README.md#delete) - Delete an employee benefit
* [get_ytd_benefit_amounts_from_different_company](https://github.com/Gusto/gusto-python-client/blob/master/docs/sdks/employeebenefits/README.md#get_ytd_benefit_amounts_from_different_company) - Get year-to-date benefit amounts from a different company
* [create_ytd_benefit_amounts_from_different_company](https://github.com/Gusto/gusto-python-client/blob/master/docs/sdks/employeebenefits/README.md#create_ytd_benefit_amounts_from_different_company) - Create year-to-date benefit amounts from a different company

### [employee_employments](https://github.com/Gusto/gusto-python-client/blob/master/docs/sdks/employeeemployments/README.md)

* [create_termination](https://github.com/Gusto/gusto-python-client/blob/master/docs/sdks/employeeemployments/README.md#create_termination) - Create an employee termination
* [delete_termination](https://github.com/Gusto/gusto-python-client/blob/master/docs/sdks/employeeemployments/README.md#delete_termination) - Delete an employee termination
* [update_termination](https://github.com/Gusto/gusto-python-client/blob/master/docs/sdks/employeeemployments/README.md#update_termination) - Update an employee termination
* [create_rehire](https://github.com/Gusto/gusto-python-client/blob/master/docs/sdks/employeeemployments/README.md#create_rehire) - Create an employee rehire
* [update_rehire](https://github.com/Gusto/gusto-python-client/blob/master/docs/sdks/employeeemployments/README.md#update_rehire) - Update an employee rehire
* [get_rehire](https://github.com/Gusto/gusto-python-client/blob/master/docs/sdks/employeeemployments/README.md#get_rehire) - Get an employee rehire
* [delete_rehire](https://github.com/Gusto/gusto-python-client/blob/master/docs/sdks/employeeemployments/README.md#delete_rehire) - Delete an employee rehire
* [get_history](https://github.com/Gusto/gusto-python-client/blob/master/docs/sdks/employeeemployments/README.md#get_history) - Get employment history for an employee

### [employees](https://github.com/Gusto/gusto-python-client/blob/master/docs/sdks/employees/README.md)

* [create](https://github.com/Gusto/gusto-python-client/blob/master/docs/sdks/employees/README.md#create) - Create an employee
* [get](https://github.com/Gusto/gusto-python-client/blob/master/docs/sdks/employees/README.md#get) - Get employees of a company
* [get_by_id](https://github.com/Gusto/gusto-python-client/blob/master/docs/sdks/employees/README.md#get_by_id) - Get an employee
* [update](https://github.com/Gusto/gusto-python-client/blob/master/docs/sdks/employees/README.md#update) - Update an employee
* [delete](https://github.com/Gusto/gusto-python-client/blob/master/docs/sdks/employees/README.md#delete) - Delete an onboarding employee
* [get_custom_fields](https://github.com/Gusto/gusto-python-client/blob/master/docs/sdks/employees/README.md#get_custom_fields) - Get an employee's custom fields
* [get_time_off_activities](https://github.com/Gusto/gusto-python-client/blob/master/docs/sdks/employees/README.md#get_time_off_activities) - Get employee time off activities
* [get_terminations](https://github.com/Gusto/gusto-python-client/blob/master/docs/sdks/employees/README.md#get_terminations) - Get terminations for an employee

### [events](https://github.com/Gusto/gusto-python-client/blob/master/docs/sdks/events/README.md)

* [get_all](https://github.com/Gusto/gusto-python-client/blob/master/docs/sdks/events/README.md#get_all) - Get all events

### [garnishments](https://github.com/Gusto/gusto-python-client/blob/master/docs/sdks/garnishments/README.md)

* [create](https://github.com/Gusto/gusto-python-client/blob/master/docs/sdks/garnishments/README.md#create) - Create a garnishment
* [get](https://github.com/Gusto/gusto-python-client/blob/master/docs/sdks/garnishments/README.md#get) - Get garnishments for an employee
* [get_by_id](https://github.com/Gusto/gusto-python-client/blob/master/docs/sdks/garnishments/README.md#get_by_id) - Get a garnishment
* [update](https://github.com/Gusto/gusto-python-client/blob/master/docs/sdks/garnishments/README.md#update) - Update a garnishment
* [get_child_support](https://github.com/Gusto/gusto-python-client/blob/master/docs/sdks/garnishments/README.md#get_child_support) - Get child support garnishment data


### [introspection](https://github.com/Gusto/gusto-python-client/blob/master/docs/sdks/introspection/README.md)

* [get_token_info](https://github.com/Gusto/gusto-python-client/blob/master/docs/sdks/introspection/README.md#get_token_info) - Get info about the current access token
* [revoke](https://github.com/Gusto/gusto-python-client/blob/master/docs/sdks/introspection/README.md#revoke) - Revoke access token
* [refresh_access_token](https://github.com/Gusto/gusto-python-client/blob/master/docs/sdks/introspection/README.md#refresh_access_token) - Refresh access token
* [disconnect_app_integration](https://github.com/Gusto/gusto-python-client/blob/master/docs/sdks/introspection/README.md#disconnect_app_integration) - Disconnect an app integration

### [jobs](https://github.com/Gusto/gusto-python-client/blob/master/docs/sdks/jobs/README.md)

* [create](https://github.com/Gusto/gusto-python-client/blob/master/docs/sdks/jobs/README.md#create) - Create a job
* [create_compensation](https://github.com/Gusto/gusto-python-client/blob/master/docs/sdks/jobs/README.md#create_compensation) - Create a compensation

### [jobs_and_compensations](https://github.com/Gusto/gusto-python-client/blob/master/docs/sdks/jobsandcompensations/README.md)

* [get_jobs](https://github.com/Gusto/gusto-python-client/blob/master/docs/sdks/jobsandcompensations/README.md#get_jobs) - Get jobs for an employee
* [get](https://github.com/Gusto/gusto-python-client/blob/master/docs/sdks/jobsandcompensations/README.md#get) - Get a job
* [update_job](https://github.com/Gusto/gusto-python-client/blob/master/docs/sdks/jobsandcompensations/README.md#update_job) - Update a job
* [delete](https://github.com/Gusto/gusto-python-client/blob/master/docs/sdks/jobsandcompensations/README.md#delete) - Delete an individual job
* [get_compensations_for_job](https://github.com/Gusto/gusto-python-client/blob/master/docs/sdks/jobsandcompensations/README.md#get_compensations_for_job) - Get compensations for a job
* [get_compensation](https://github.com/Gusto/gusto-python-client/blob/master/docs/sdks/jobsandcompensations/README.md#get_compensation) - Get a compensation
* [update_compensation](https://github.com/Gusto/gusto-python-client/blob/master/docs/sdks/jobsandcompensations/README.md#update_compensation) - Update a compensation
* [delete_compensation](https://github.com/Gusto/gusto-python-client/blob/master/docs/sdks/jobsandcompensations/README.md#delete_compensation) - Delete a compensation

### [locations](https://github.com/Gusto/gusto-python-client/blob/master/docs/sdks/locations/README.md)

* [create](https://github.com/Gusto/gusto-python-client/blob/master/docs/sdks/locations/README.md#create) - Create a company location
* [get](https://github.com/Gusto/gusto-python-client/blob/master/docs/sdks/locations/README.md#get) - Get a location
* [update](https://github.com/Gusto/gusto-python-client/blob/master/docs/sdks/locations/README.md#update) - Update a location
* [get_minimum_wages](https://github.com/Gusto/gusto-python-client/blob/master/docs/sdks/locations/README.md#get_minimum_wages) - Get minimum wages for a location

### [pay_schedules](https://github.com/Gusto/gusto-python-client/blob/master/docs/sdks/payschedules/README.md)

* [list](https://github.com/Gusto/gusto-python-client/blob/master/docs/sdks/payschedules/README.md#list) - Get the pay schedules for a company
* [get](https://github.com/Gusto/gusto-python-client/blob/master/docs/sdks/payschedules/README.md#get) - Get a pay schedule
* [get_pay_periods](https://github.com/Gusto/gusto-python-client/blob/master/docs/sdks/payschedules/README.md#get_pay_periods) - Get pay periods for a company
* [get_unprocessed_termination_pay_periods](https://github.com/Gusto/gusto-python-client/blob/master/docs/sdks/payschedules/README.md#get_unprocessed_termination_pay_periods) - Get termination pay periods for a company
* [get_assignments](https://github.com/Gusto/gusto-python-client/blob/master/docs/sdks/payschedules/README.md#get_assignments) - Get pay schedule assignments for a company

### [payrolls](https://github.com/Gusto/gusto-python-client/blob/master/docs/sdks/payrolls/README.md)

* [get_for_company](https://github.com/Gusto/gusto-python-client/blob/master/docs/sdks/payrolls/README.md#get_for_company) - Get all payrolls for a company
* [get](https://github.com/Gusto/gusto-python-client/blob/master/docs/sdks/payrolls/README.md#get) - Get a single payroll
* [update](https://github.com/Gusto/gusto-python-client/blob/master/docs/sdks/payrolls/README.md#update) - Update a payroll by ID
* [prepare](https://github.com/Gusto/gusto-python-client/blob/master/docs/sdks/payrolls/README.md#prepare) - Prepare a payroll for update

### [time_off_policies](https://github.com/Gusto/gusto-python-client/blob/master/docs/sdks/timeoffpolicies/README.md)

* [calculate_accruing_time_off_hours](https://github.com/Gusto/gusto-python-client/blob/master/docs/sdks/timeoffpolicies/README.md#calculate_accruing_time_off_hours) - Calculate accruing time off hours

### [webhooks](https://github.com/Gusto/gusto-python-client/blob/master/docs/sdks/webhooks/README.md)

* [create](https://github.com/Gusto/gusto-python-client/blob/master/docs/sdks/webhooks/README.md#create) - Create a webhook subscription
* [list_subscriptions](https://github.com/Gusto/gusto-python-client/blob/master/docs/sdks/webhooks/README.md#list_subscriptions) - List webhook subscriptions
* [update_subscription](https://github.com/Gusto/gusto-python-client/blob/master/docs/sdks/webhooks/README.md#update_subscription) - Update a webhook subscription
* [get_subscription](https://github.com/Gusto/gusto-python-client/blob/master/docs/sdks/webhooks/README.md#get_subscription) - Get a webhook subscription
* [delete_subscription](https://github.com/Gusto/gusto-python-client/blob/master/docs/sdks/webhooks/README.md#delete_subscription) - Delete a webhook subscription
* [verify](https://github.com/Gusto/gusto-python-client/blob/master/docs/sdks/webhooks/README.md#verify) - Verify the webhook subscription
* [request_verification_token](https://github.com/Gusto/gusto-python-client/blob/master/docs/sdks/webhooks/README.md#request_verification_token) - Request the webhook subscription verification_token

</details>
<!-- End Available Resources and Operations [operations] -->

<!-- Start Retries [retries] -->
## Retries

Some of the endpoints in this SDK support retries. If you use the SDK without any configuration, it will fall back to the default retry strategy provided by the API. However, the default retry strategy can be overridden on a per-operation basis, or across the entire SDK.

To change the default retry strategy for a single API call, simply provide a `RetryConfig` object to the call:
```python
from gusto_app_integration import GustoAppIntegration
from gusto_app_integration.utils import BackoffStrategy, RetryConfig


with GustoAppIntegration(
    company_access_auth="<YOUR_BEARER_TOKEN_HERE>",
) as gai_client:

    res = gai_client.introspection.get_token_info(,
        RetryConfig("backoff", BackoffStrategy(1, 50, 1.1, 100), False))

    # Handle response
    print(res)

```

If you'd like to override the default retry strategy for all operations that support retries, you can use the `retry_config` optional parameter when initializing the SDK:
```python
from gusto_app_integration import GustoAppIntegration
from gusto_app_integration.utils import BackoffStrategy, RetryConfig


with GustoAppIntegration(
    retry_config=RetryConfig("backoff", BackoffStrategy(1, 50, 1.1, 100), False),
    company_access_auth="<YOUR_BEARER_TOKEN_HERE>",
) as gai_client:

    res = gai_client.introspection.get_token_info()

    # Handle response
    print(res)

```
<!-- End Retries [retries] -->

<!-- Start Error Handling [errors] -->
## Error Handling

Handling errors in this SDK should largely match your expectations. All operations return a response object or raise an exception.

By default, an API error will raise a models.APIError exception, which has the following properties:

| Property        | Type             | Description           |
|-----------------|------------------|-----------------------|
| `.status_code`  | *int*            | The HTTP status code  |
| `.message`      | *str*            | The error message     |
| `.raw_response` | *httpx.Response* | The raw HTTP response |
| `.body`         | *str*            | The response content  |

When custom error responses are specified for an operation, the SDK may also raise their associated exceptions. You can refer to respective *Errors* tables in SDK docs for more details on possible exception types for each operation. For example, the `provision_async` method may raise the following exceptions:

| Error Type                            | Status Code | Content Type     |
| ------------------------------------- | ----------- | ---------------- |
| models.UnprocessableEntityErrorObject | 422         | application/json |
| models.APIError                       | 4XX, 5XX    | \*/\*            |

### Example

```python
import gusto_app_integration
from gusto_app_integration import GustoAppIntegration, models


with GustoAppIntegration() as gai_client:
    res = None
    try:

        res = gai_client.companies.provision(security=gusto_app_integration.PostV1ProvisionSecurity(
            system_access_auth="<YOUR_BEARER_TOKEN_HERE>",
        ), user={
            "first_name": "Frank",
            "last_name": "Ocean",
            "email": "frank@example.com",
            "phone": "2345558899",
        }, company={
            "name": "Frank's Ocean, LLC",
            "trade_name": "Frank’s Ocean",
            "ein": "123456789",
            "states": [
                "CO",
                "CA",
            ],
            "number_employees": 8,
            "addresses": [
                {
                    "street_1": "1201 16th Street Mall",
                    "street_2": "Suite 350",
                    "city": "Denver",
                    "zip_code": "80202",
                    "state": "CO",
                    "phone": "2345678900",
                    "is_primary": "true",
                },
                {
                    "street_1": "525 20th Street",
                    "city": "San Francisco",
                    "zip_code": "94107",
                    "state": "CA",
                    "phone": "2345678901",
                },
            ],
        })

        # Handle response
        print(res)

    except models.UnprocessableEntityErrorObject as e:
        # handle e.data: models.UnprocessableEntityErrorObjectData
        raise(e)
    except models.APIError as e:
        # handle exception
        raise(e)
```
<!-- End Error Handling [errors] -->

<!-- Start Server Selection [server] -->
## Server Selection

### Select Server by Name

You can override the default server globally by passing a server name to the `server: str` optional parameter when initializing the SDK client instance. The selected server will then be used as the default on the operations that use it. This table lists the names associated with the available servers:

| Name   | Server                       | Description |
| ------ | ---------------------------- | ----------- |
| `demo` | `https://api.gusto-demo.com` | Demo        |
| `prod` | `https://api.gusto.com`      | Prod        |

#### Example

```python
from gusto_app_integration import GustoAppIntegration


with GustoAppIntegration(
    server="prod",
    company_access_auth="<YOUR_BEARER_TOKEN_HERE>",
) as gai_client:

    res = gai_client.introspection.get_token_info()

    # Handle response
    print(res)

```

### Override Server URL Per-Client

The default server can also be overridden globally by passing a URL to the `server_url: str` optional parameter when initializing the SDK client instance. For example:
```python
from gusto_app_integration import GustoAppIntegration


with GustoAppIntegration(
    server_url="https://api.gusto-demo.com",
    company_access_auth="<YOUR_BEARER_TOKEN_HERE>",
) as gai_client:

    res = gai_client.introspection.get_token_info()

    # Handle response
    print(res)

```
<!-- End Server Selection [server] -->

<!-- Start Custom HTTP Client [http-client] -->
## Custom HTTP Client

The Python SDK makes API calls using the [httpx](https://www.python-httpx.org/) HTTP library.  In order to provide a convenient way to configure timeouts, cookies, proxies, custom headers, and other low-level configuration, you can initialize the SDK client with your own HTTP client instance.
Depending on whether you are using the sync or async version of the SDK, you can pass an instance of `HttpClient` or `AsyncHttpClient` respectively, which are Protocol's ensuring that the client has the necessary methods to make API calls.
This allows you to wrap the client with your own custom logic, such as adding custom headers, logging, or error handling, or you can just pass an instance of `httpx.Client` or `httpx.AsyncClient` directly.

For example, you could specify a header for every request that this sdk makes as follows:
```python
from gusto_app_integration import GustoAppIntegration
import httpx

http_client = httpx.Client(headers={"x-custom-header": "someValue"})
s = GustoAppIntegration(client=http_client)
```

or you could wrap the client with your own custom logic:
```python
from gusto_app_integration import GustoAppIntegration
from gusto_app_integration.httpclient import AsyncHttpClient
import httpx

class CustomClient(AsyncHttpClient):
    client: AsyncHttpClient

    def __init__(self, client: AsyncHttpClient):
        self.client = client

    async def send(
        self,
        request: httpx.Request,
        *,
        stream: bool = False,
        auth: Union[
            httpx._types.AuthTypes, httpx._client.UseClientDefault, None
        ] = httpx.USE_CLIENT_DEFAULT,
        follow_redirects: Union[
            bool, httpx._client.UseClientDefault
        ] = httpx.USE_CLIENT_DEFAULT,
    ) -> httpx.Response:
        request.headers["Client-Level-Header"] = "added by client"

        return await self.client.send(
            request, stream=stream, auth=auth, follow_redirects=follow_redirects
        )

    def build_request(
        self,
        method: str,
        url: httpx._types.URLTypes,
        *,
        content: Optional[httpx._types.RequestContent] = None,
        data: Optional[httpx._types.RequestData] = None,
        files: Optional[httpx._types.RequestFiles] = None,
        json: Optional[Any] = None,
        params: Optional[httpx._types.QueryParamTypes] = None,
        headers: Optional[httpx._types.HeaderTypes] = None,
        cookies: Optional[httpx._types.CookieTypes] = None,
        timeout: Union[
            httpx._types.TimeoutTypes, httpx._client.UseClientDefault
        ] = httpx.USE_CLIENT_DEFAULT,
        extensions: Optional[httpx._types.RequestExtensions] = None,
    ) -> httpx.Request:
        return self.client.build_request(
            method,
            url,
            content=content,
            data=data,
            files=files,
            json=json,
            params=params,
            headers=headers,
            cookies=cookies,
            timeout=timeout,
            extensions=extensions,
        )

s = GustoAppIntegration(async_client=CustomClient(httpx.AsyncClient()))
```
<!-- End Custom HTTP Client [http-client] -->

<!-- Start Resource Management [resource-management] -->
## Resource Management

The `GustoAppIntegration` class implements the context manager protocol and registers a finalizer function to close the underlying sync and async HTTPX clients it uses under the hood. This will close HTTP connections, release memory and free up other resources held by the SDK. In short-lived Python programs and notebooks that make a few SDK method calls, resource management may not be a concern. However, in longer-lived programs, it is beneficial to create a single SDK instance via a [context manager][context-manager] and reuse it across the application.

[context-manager]: https://docs.python.org/3/reference/datamodel.html#context-managers

```python
from gusto_app_integration import GustoAppIntegration
def main():

    with GustoAppIntegration(
        company_access_auth="<YOUR_BEARER_TOKEN_HERE>",
    ) as gai_client:
        # Rest of application here...


# Or when using async:
async def amain():

    async with GustoAppIntegration(
        company_access_auth="<YOUR_BEARER_TOKEN_HERE>",
    ) as gai_client:
        # Rest of application here...
```
<!-- End Resource Management [resource-management] -->

<!-- Start Debugging [debug] -->
## Debugging

You can setup your SDK to emit debug logs for SDK requests and responses.

You can pass your own logger class directly into your SDK.
```python
from gusto_app_integration import GustoAppIntegration
import logging

logging.basicConfig(level=logging.DEBUG)
s = GustoAppIntegration(debug_logger=logging.getLogger("gusto_app_integration"))
```
<!-- End Debugging [debug] -->

<!-- Placeholder for Future Speakeasy SDK Sections -->

# Development

## Maturity

This SDK is in beta, and there may be breaking changes between versions without a major version update. Therefore, we recommend pinning usage
to a specific package version. This way, you can install the same version each time without breaking changes unless you are intentionally
looking for the latest version.

## Contributions

While we value open-source contributions to this SDK, this library is generated programmatically. Any manual changes added to internal files will be overwritten on the next generation. 
We look forward to hearing your feedback. Feel free to open a PR or an issue with a proof of concept and we'll do our best to include it in a future release. 

### SDK Created by [Speakeasy](https://www.speakeasy.com/?utm_source=gusto-app-integration&utm_campaign=python)
