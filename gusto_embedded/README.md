# gusto

Developer-friendly & type-safe Python SDK specifically catered to leverage *gusto* API.

<div align="left">
    <a href="https://www.speakeasy.com/?utm_source=gusto&utm_campaign=python"><img src="https://custom-icon-badges.demolab.com/badge/-Built%20By%20Speakeasy-212015?style=for-the-badge&logoColor=FBE331&logo=speakeasy&labelColor=545454" /></a>
    <a href="https://opensource.org/licenses/MIT">
        <img src="https://img.shields.io/badge/License-MIT-blue.svg" style="width: 100px; height: 28px;" />
    </a>
</div>


<!-- Start Summary [summary] -->
## Summary

Gusto API: Welcome to Gusto's Embedded Payroll API documentation!
<!-- End Summary [summary] -->

<!-- Start Table of Contents [toc] -->
## Table of Contents
<!-- $toc-max-depth=2 -->
* [gusto](#gusto)
  * [SDK Installation](#sdk-installation)
  * [IDE Support](#ide-support)
  * [Example Usage](#example-usage)
  * [Authentication](#authentication)
  * [Available Resources and Operations](#available-resources-and-operations)
  * [File uploads](#file-uploads)
  * [Retries](#retries)
  * [Error Handling](#error-handling)
  * [Server Selection](#server-selection)
  * [Custom HTTP Client](#custom-http-client)
  * [Resource Management](#resource-management)
  * [Debugging](#debugging)
* [Development](#development)
  * [Maturity](#maturity)
  * [Contributions](#contributions)

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
pip install gusto_embedded
```

### Poetry

*Poetry* is a modern tool that simplifies dependency management and package publishing by using a single `pyproject.toml` file to handle project metadata and dependencies.

```bash
poetry add gusto_embedded
```

### Shell and script usage with `uv`

You can use this SDK in a Python shell with [uv](https://docs.astral.sh/uv/) and the `uvx` command that comes with it like so:

```shell
uvx --from gusto_embedded python
```

It's also possible to write a standalone Python script without needing to set up a whole project like so:

```python
#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.9"
# dependencies = [
#     "gusto_embedded",
# ]
# ///

from gusto_embedded import Gusto

sdk = Gusto(
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

## Example Usage

### Example

```python
# Synchronous Example
from gusto_embedded import Gusto
import os

auth_token = os.getenv("GUSTO_COMPANY_ACCESS_AUTH", None)
if auth_token is None:
	raise ValueError("GUSTO_COMPANY_ACCESS_AUTH is not set")

with Gusto(company_access_auth=auth_token) as gusto:
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
  auth_token = os.getenv("GUSTO_COMPANY_ACCESS_AUTH", None)
  if auth_token is None:
    raise ValueError("GUSTO_COMPANY_ACCESS_AUTH is not set")

  async with Gusto(company_access_auth=auth_token) as gusto:
      res = gusto.introspection.get_info_async()

      # Handle response
      print(res)

asyncio.run(main())
```

### Common workflows
A common workflow, as documented [in our docs](https://docs.gusto.com/embedded-payroll/docs/onboard-a-company), is to create a
new partner managed company. In this section we will illustrate using a system access token to create a partner managed
company. Then we will use the returned company access token for subsequent requests. We'll do this in the following steps.
1. [Create a Partner Managed Company](https://github.com/Gusto/gusto-python-client/blob/main/gusto_embedded/docs/sdks/companies/README.md#create_partner_managed)
2. [View](https://flows.gusto.com/terms) and [Accept](https://github.com/Gusto/gusto-python-client/blob/main/gusto_embedded/docs/sdks/companies/README.md#accept_terms_of_service) Terms of Service
3. [Create a Company Location](https://docs.gusto.com/embedded-payroll/docs/onboard-a-company#3-create-a-company-location)

```python
# Synchronous Example
from gusto_embedded import Gusto, PostV1PartnerManagedCompaniesSecurity
import os

system_auth_token = os.getenv("GUSTO_SYSTEM_ACCESS_AUTH", None)
if system_auth_token is None:
	raise ValueError("GUSTO_SYSTEM_ACCESS_AUTH is not set")

security = PostV1PartnerManagedCompaniesSecurity(system_access_auth=system_auth_token)
system_gusto = Gusto()
partner_managed_company_res = system_gusto.companies.create_partner_managed(
  security=security,
  user={
    "first_name": "Frank",
    "last_name": "Ocean",
    "email": "frank@example.com",
    "phone": "2345558899",
  },
  company={
      "name": "Frank's Ocean, LLC",
      "trade_name": "Frank’s Ocean",
      "ein": "123432989",
      "contractor_only": False,
  }
)

company_access_token = partner_managed_company_res.access_token
company_refresh_token = partner_managed_company_res.refresh_token
company_uuid = partner_managed_company_res.company_uuid

with Gusto(company_access_auth=company_access_token) as gusto:
    # Get company admin
    company_res = gusto.companies.get(company_id=company_uuid)
    primary_admin = company_res.primary_payroll_admin

    # Accept terms of service
    terms_of_service_res = gusto.companies.accept_terms_of_service(
      company_uuid=company_uuid,
      email=primary_admin.email,
      ip_address="...",
      external_user_id="..."
    )

    # Create a company location
    location_res = gusto.locations.create(
      company_id=company_uuid,
      phone_number="8009360383",
      street_1="425 2nd Street",
      city="San Francisco",
      state="CA",
      zip_code="94107",
      street_2="Suite 602"
    )
```
<!-- No SDK Example Usage [usage] -->

<!-- Start Authentication [security] -->
## Authentication

### Per-Client Security Schemes

This SDK supports the following security scheme globally:

| Name                  | Type | Scheme      | Environment Variable        |
| --------------------- | ---- | ----------- | --------------------------- |
| `company_access_auth` | http | HTTP Bearer | `GUSTO_COMPANY_ACCESS_AUTH` |

To authenticate with the API the `company_access_auth` parameter must be set when initializing the SDK client instance. For example:
```python
from gusto_embedded import Gusto
import os

with Gusto(
    company_access_auth=os.getenv("GUSTO_COMPANY_ACCESS_AUTH", ""),
) as gusto:

    res = gusto.introspection.get_info()

    # Handle response
    print(res)

```

### Per-Operation Security Schemes

Some operations in this SDK require the security scheme to be specified at the request level. For example:
```python
import gusto_embedded
from gusto_embedded import Gusto
import os

with Gusto() as gusto:

    res = gusto.companies.create_partner_managed(security=gusto_embedded.PostV1PartnerManagedCompaniesSecurity(
        system_access_auth=os.getenv("GUSTO_SYSTEM_ACCESS_AUTH", ""),
    ), user={
        "first_name": "Frank",
        "last_name": "Ocean",
        "email": "frank@example.com",
        "phone": "2345558899",
    }, company={
        "name": "Frank's Ocean, LLC",
        "trade_name": "Frank’s Ocean",
        "ein": "123456789",
        "contractor_only": False,
    })

    # Handle response
    print(res)

```
<!-- End Authentication [security] -->

<!-- Start Available Resources and Operations [operations] -->
## Available Resources and Operations

<details open>
<summary>Available methods</summary>

### [ach_transactions](docs/sdks/achtransactions/README.md)

* [get_all](docs/sdks/achtransactions/README.md#get_all) - Get all ACH transactions for a company

### [bank_accounts](docs/sdks/bankaccounts/README.md)

* [create](docs/sdks/bankaccounts/README.md#create) - Create a company bank account
* [get](docs/sdks/bankaccounts/README.md#get) - Get all company bank accounts
* [verify](docs/sdks/bankaccounts/README.md#verify) - Verify a company bank account
* [create_from_plaid_token](docs/sdks/bankaccounts/README.md#create_from_plaid_token) - Create a bank account from a plaid processor token

### [companies](docs/sdks/companies/README.md)

* [create_partner_managed](docs/sdks/companies/README.md#create_partner_managed) - Create a partner managed company
* [get](docs/sdks/companies/README.md#get) - Get a company
* [update](docs/sdks/companies/README.md#update) - Update a company
* [migrate](docs/sdks/companies/README.md#migrate) - Migrate company to embedded payroll
* [accept_terms_of_service](docs/sdks/companies/README.md#accept_terms_of_service) - Accept terms of service for a company user
* [retrieve_terms_of_service](docs/sdks/companies/README.md#retrieve_terms_of_service) - Retrieve terms of service status for a company user
* [create_admin](docs/sdks/companies/README.md#create_admin) - Create an admin for the company
* [list_admins](docs/sdks/companies/README.md#list_admins) - Get all the admins at a company
* [get_onboarding_status](docs/sdks/companies/README.md#get_onboarding_status) - Get the company's onboarding status
* [finish_onboarding](docs/sdks/companies/README.md#finish_onboarding) - Finish company onboarding
* [get_custom_fields](docs/sdks/companies/README.md#get_custom_fields) - Get the custom fields of a company

### [company_attachment](docs/sdks/companyattachmentsdk/README.md)

* [get_download_url](docs/sdks/companyattachmentsdk/README.md#get_download_url) - Get a temporary url to download the Company Attachment file

### [company_attachments](docs/sdks/companyattachments/README.md)

* [get_details](docs/sdks/companyattachments/README.md#get_details) - Get Company Attachment Details
* [get_list](docs/sdks/companyattachments/README.md#get_list) - Get List of Company Attachments
* [create](docs/sdks/companyattachments/README.md#create) - Create Company Attachment and Upload File

### [company_benefits](docs/sdks/companybenefits/README.md)

* [create](docs/sdks/companybenefits/README.md#create) - Create a company benefit
* [list](docs/sdks/companybenefits/README.md#list) - Get benefits for a company
* [get](docs/sdks/companybenefits/README.md#get) - Get a company benefit
* [update](docs/sdks/companybenefits/README.md#update) - Update a company benefit
* [delete](docs/sdks/companybenefits/README.md#delete) - Delete a company benefit
* [get_all](docs/sdks/companybenefits/README.md#get_all) - Get all benefits supported by Gusto
* [get_supported](docs/sdks/companybenefits/README.md#get_supported) - Get a supported benefit by ID
* [get_summary](docs/sdks/companybenefits/README.md#get_summary) - Get company benefit summary by company benefit id.
* [get_employee_benefits](docs/sdks/companybenefits/README.md#get_employee_benefits) - Get all employee benefits for a company benefit
* [update_employee_benefits](docs/sdks/companybenefits/README.md#update_employee_benefits) - Bulk update employee benefits for a company benefit
* [get_requirements](docs/sdks/companybenefits/README.md#get_requirements) - Get benefit fields requirements by ID

### [company_forms](docs/sdks/companyforms/README.md)

* [get_all](docs/sdks/companyforms/README.md#get_all) - Get all company forms
* [get](docs/sdks/companyforms/README.md#get) - Get a company form
* [get_pdf](docs/sdks/companyforms/README.md#get_pdf) - Get a company form pdf
* [sign](docs/sdks/companyforms/README.md#sign) - Sign a company form

### [contractor_documents](docs/sdks/contractordocuments/README.md)

* [get_all](docs/sdks/contractordocuments/README.md#get_all) - Get all contractor documents
* [get](docs/sdks/contractordocuments/README.md#get) - Get a contractor document
* [get_pdf](docs/sdks/contractordocuments/README.md#get_pdf) - Get the contractor document pdf
* [sign](docs/sdks/contractordocuments/README.md#sign) - Sign a contractor document

### [contractor_forms](docs/sdks/contractorforms/README.md)

* [list](docs/sdks/contractorforms/README.md#list) - Get all contractor forms
* [get](docs/sdks/contractorforms/README.md#get) - Get a contractor form
* [get_pdf](docs/sdks/contractorforms/README.md#get_pdf) - Get the contractor form pdf
* [generate1099](docs/sdks/contractorforms/README.md#generate1099) - Generate a 1099 form [DEMO]

### [contractor_payment_groups](docs/sdks/contractorpaymentgroups/README.md)

* [create](docs/sdks/contractorpaymentgroups/README.md#create) - Create a contractor payment group
* [get_list](docs/sdks/contractorpaymentgroups/README.md#get_list) - Get contractor payment groups for a company
* [preview](docs/sdks/contractorpaymentgroups/README.md#preview) - Preview a contractor payment group
* [get](docs/sdks/contractorpaymentgroups/README.md#get) - Fetch a contractor payment group
* [delete](docs/sdks/contractorpaymentgroups/README.md#delete) - Cancel a contractor payment group
* [fund](docs/sdks/contractorpaymentgroups/README.md#fund) - Fund a contractor payment group [DEMO]

### [contractor_payment_method](docs/sdks/contractorpaymentmethodsdk/README.md)

* [get_bank_accounts](docs/sdks/contractorpaymentmethodsdk/README.md#get_bank_accounts) - Get all contractor bank accounts
* [get](docs/sdks/contractorpaymentmethodsdk/README.md#get) - Get a contractor's payment method
* [update](docs/sdks/contractorpaymentmethodsdk/README.md#update) - Update a contractor's payment method

### [contractor_payment_methods](docs/sdks/contractorpaymentmethods/README.md)

* [create_bank_account](docs/sdks/contractorpaymentmethods/README.md#create_bank_account) - Create a contractor bank account

### [contractor_payments](docs/sdks/contractorpayments/README.md)

* [get_receipt](docs/sdks/contractorpayments/README.md#get_receipt) - Get a single contractor payment receipt
* [fund](docs/sdks/contractorpayments/README.md#fund) - Fund a contractor payment [DEMO]
* [create](docs/sdks/contractorpayments/README.md#create) - Create a contractor payment
* [list](docs/sdks/contractorpayments/README.md#list) - Get contractor payments for a company
* [get](docs/sdks/contractorpayments/README.md#get) - Get a single contractor payment
* [delete](docs/sdks/contractorpayments/README.md#delete) - Cancel a contractor payment
* [preview](docs/sdks/contractorpayments/README.md#preview) - Preview contractor payment debit date

### [contractors](docs/sdks/contractors/README.md)

* [create](docs/sdks/contractors/README.md#create) - Create a contractor
* [list](docs/sdks/contractors/README.md#list) - Get contractors of a company
* [get](docs/sdks/contractors/README.md#get) - Get a contractor
* [update](docs/sdks/contractors/README.md#update) - Update a contractor
* [delete](docs/sdks/contractors/README.md#delete) - Delete a contractor
* [get_onboarding_status](docs/sdks/contractors/README.md#get_onboarding_status) - Get the contractor's onboarding status
* [update_onboarding_status](docs/sdks/contractors/README.md#update_onboarding_status) - Change the contractor's onboarding status
* [get_address](docs/sdks/contractors/README.md#get_address) - Get a contractor address
* [update_address](docs/sdks/contractors/README.md#update_address) - Update a contractor's address

### [departments](docs/sdks/departments/README.md)

* [create](docs/sdks/departments/README.md#create) - Create a department
* [get_all](docs/sdks/departments/README.md#get_all) - Get all departments of a company
* [get](docs/sdks/departments/README.md#get) - Get a department
* [update](docs/sdks/departments/README.md#update) - Update a department
* [delete](docs/sdks/departments/README.md#delete) - Delete a department
* [add_people](docs/sdks/departments/README.md#add_people) - Add people to a department
* [remove_people](docs/sdks/departments/README.md#remove_people) - Remove people from a department

### [earning_types](docs/sdks/earningtypes/README.md)

* [create](docs/sdks/earningtypes/README.md#create) - Create a custom earning type
* [list](docs/sdks/earningtypes/README.md#list) - Get all earning types for a company
* [update](docs/sdks/earningtypes/README.md#update) - Update an earning type
* [delete](docs/sdks/earningtypes/README.md#delete) - Deactivate an earning type

### [employee_addresses](docs/sdks/employeeaddresses/README.md)

* [get](docs/sdks/employeeaddresses/README.md#get) - Get an employee's home addresses
* [create](docs/sdks/employeeaddresses/README.md#create) - Create an employee's home address
* [retrieve_home_address](docs/sdks/employeeaddresses/README.md#retrieve_home_address) - Get an employee's home address
* [update](docs/sdks/employeeaddresses/README.md#update) - Update an employee's home address
* [delete](docs/sdks/employeeaddresses/README.md#delete) - Delete an employee's home address
* [get_work_addresses](docs/sdks/employeeaddresses/README.md#get_work_addresses) - Get an employee's work addresses
* [create_work_address](docs/sdks/employeeaddresses/README.md#create_work_address) - Create an employee work address
* [retrieve_work_address](docs/sdks/employeeaddresses/README.md#retrieve_work_address) - Get an employee work address
* [update_work_address](docs/sdks/employeeaddresses/README.md#update_work_address) - Update an employee work address
* [delete_work_address](docs/sdks/employeeaddresses/README.md#delete_work_address) - Delete an employee's work address

### [employee_benefits](docs/sdks/employeebenefits/README.md)

* [create](docs/sdks/employeebenefits/README.md#create) - Create an employee benefit
* [get](docs/sdks/employeebenefits/README.md#get) - Get all benefits for an employee
* [retrieve](docs/sdks/employeebenefits/README.md#retrieve) - Get an employee benefit
* [update](docs/sdks/employeebenefits/README.md#update) - Update an employee benefit
* [delete](docs/sdks/employeebenefits/README.md#delete) - Delete an employee benefit
* [get_ytd_benefit_amounts_from_different_company](docs/sdks/employeebenefits/README.md#get_ytd_benefit_amounts_from_different_company) - Get year-to-date benefit amounts from a different company
* [create_ytd_benefit_amounts_from_different_company](docs/sdks/employeebenefits/README.md#create_ytd_benefit_amounts_from_different_company) - Create year-to-date benefit amounts from a different company

### [employee_employments](docs/sdks/employeeemployments/README.md)

* [create_termination](docs/sdks/employeeemployments/README.md#create_termination) - Create an employee termination
* [get_terminations](docs/sdks/employeeemployments/README.md#get_terminations) - Get terminations for an employee
* [delete_termination](docs/sdks/employeeemployments/README.md#delete_termination) - Delete an employee termination
* [update_termination](docs/sdks/employeeemployments/README.md#update_termination) - Update an employee termination
* [create_rehire](docs/sdks/employeeemployments/README.md#create_rehire) - Create an employee rehire
* [rehire](docs/sdks/employeeemployments/README.md#rehire) - Update an employee rehire
* [get_rehire](docs/sdks/employeeemployments/README.md#get_rehire) - Get an employee rehire
* [delete_rehire](docs/sdks/employeeemployments/README.md#delete_rehire) - Delete an employee rehire
* [get_history](docs/sdks/employeeemployments/README.md#get_history) - Get employment history for an employee

### [employee_forms](docs/sdks/employeeforms/README.md)

* [generate_w2](docs/sdks/employeeforms/README.md#generate_w2) - Generate a W2 form [DEMO]
* [list](docs/sdks/employeeforms/README.md#list) - Get all employee forms
* [get](docs/sdks/employeeforms/README.md#get) - Get an employee form
* [get_pdf](docs/sdks/employeeforms/README.md#get_pdf) - Get the employee form pdf
* [sign](docs/sdks/employeeforms/README.md#sign) - Sign an employee form

### [employee_payment_method](docs/sdks/employeepaymentmethodsdk/README.md)

* [create](docs/sdks/employeepaymentmethodsdk/README.md#create) - Create an employee bank account
* [delete_bank_account](docs/sdks/employeepaymentmethodsdk/README.md#delete_bank_account) - Delete an employee bank account
* [update_bank_account](docs/sdks/employeepaymentmethodsdk/README.md#update_bank_account) - Update an employee bank account
* [get](docs/sdks/employeepaymentmethodsdk/README.md#get) - Get an employee's payment method
* [update](docs/sdks/employeepaymentmethodsdk/README.md#update) - Update an employee's payment method

### [employee_payment_methods](docs/sdks/employeepaymentmethods/README.md)

* [get_bank_accounts](docs/sdks/employeepaymentmethods/README.md#get_bank_accounts) - Get all employee bank accounts

### [employee_tax_setup](docs/sdks/employeetaxsetup/README.md)

* [get_federal_taxes](docs/sdks/employeetaxsetup/README.md#get_federal_taxes) - Get an employee's federal taxes
* [update_federal_taxes](docs/sdks/employeetaxsetup/README.md#update_federal_taxes) - Update an employee's federal taxes
* [get_state_taxes](docs/sdks/employeetaxsetup/README.md#get_state_taxes) - Get an employee's state taxes
* [update_state_taxes](docs/sdks/employeetaxsetup/README.md#update_state_taxes) - Update an employee's state taxes

### [employees](docs/sdks/employees/README.md)

* [create](docs/sdks/employees/README.md#create) - Create an employee
* [list](docs/sdks/employees/README.md#list) - Get employees of a company
* [create_historical](docs/sdks/employees/README.md#create_historical) - Create a historical employee
* [get](docs/sdks/employees/README.md#get) - Get an employee
* [update](docs/sdks/employees/README.md#update) - Update an employee
* [delete](docs/sdks/employees/README.md#delete) - Delete an onboarding employee
* [get_custom_fields](docs/sdks/employees/README.md#get_custom_fields) - Get an employee's custom fields
* [update_onboarding_documents_config](docs/sdks/employees/README.md#update_onboarding_documents_config) - Update an employee's onboarding documents config
* [get_onboarding_status](docs/sdks/employees/README.md#get_onboarding_status) - Get the employee's onboarding status
* [update_onboarding_status](docs/sdks/employees/README.md#update_onboarding_status) - Update the employee's onboarding status
* [get_time_off_activities](docs/sdks/employees/README.md#get_time_off_activities) - Get employee time off activities

### [events](docs/sdks/events/README.md)

* [get](docs/sdks/events/README.md#get) - Get all events

### [external_payrolls](docs/sdks/externalpayrolls/README.md)

* [create](docs/sdks/externalpayrolls/README.md#create) - Create a new external payroll for a company
* [get](docs/sdks/externalpayrolls/README.md#get) - Get external payrolls for a company
* [retrieve](docs/sdks/externalpayrolls/README.md#retrieve) - Get an external payroll
* [delete](docs/sdks/externalpayrolls/README.md#delete) - Delete an external payroll
* [update](docs/sdks/externalpayrolls/README.md#update) - Update an external payroll
* [calculate_taxes](docs/sdks/externalpayrolls/README.md#calculate_taxes) - Get tax suggestions for an external payroll
* [list_tax_liabilities](docs/sdks/externalpayrolls/README.md#list_tax_liabilities) - Get tax liabilities
* [update_tax_liabilities](docs/sdks/externalpayrolls/README.md#update_tax_liabilities) - Update tax liabilities
* [finalize_tax_liabilities](docs/sdks/externalpayrolls/README.md#finalize_tax_liabilities) - Finalize tax liabilities options and convert into processed payrolls

### [federal_tax_details](docs/sdks/federaltaxdetailssdk/README.md)

* [get](docs/sdks/federaltaxdetailssdk/README.md#get) - Get Federal Tax Details
* [update](docs/sdks/federaltaxdetailssdk/README.md#update) - Update Federal Tax Details

### [flows](docs/sdks/flows/README.md)

* [create](docs/sdks/flows/README.md#create) - Create a flow

### [garnishments](docs/sdks/garnishments/README.md)

* [create](docs/sdks/garnishments/README.md#create) - Create a garnishment
* [list](docs/sdks/garnishments/README.md#list) - Get garnishments for an employee
* [get](docs/sdks/garnishments/README.md#get) - Get a garnishment
* [update](docs/sdks/garnishments/README.md#update) - Update a garnishment
* [get_child_support_data](docs/sdks/garnishments/README.md#get_child_support_data) - Get child support garnishment data

### [generated_documents](docs/sdks/generateddocuments/README.md)

* [get](docs/sdks/generateddocuments/README.md#get) - Get a generated document


### [historical_employees](docs/sdks/historicalemployees/README.md)

* [update](docs/sdks/historicalemployees/README.md#update) - Update a historical employee

### [holiday_pay_policies](docs/sdks/holidaypaypolicies/README.md)

* [get](docs/sdks/holidaypaypolicies/README.md#get) - Get a company's holiday pay policy
* [create](docs/sdks/holidaypaypolicies/README.md#create) - Create a holiday pay policy for a company
* [update](docs/sdks/holidaypaypolicies/README.md#update) - Update a company's holiday pay policy
* [delete](docs/sdks/holidaypaypolicies/README.md#delete) - Delete a company's holiday pay policy
* [add_employees](docs/sdks/holidaypaypolicies/README.md#add_employees) - Add employees to a company's holiday pay policy
* [remove_employees](docs/sdks/holidaypaypolicies/README.md#remove_employees) - Remove employees from a company's holiday pay policy
* [preview_paid_holidays](docs/sdks/holidaypaypolicies/README.md#preview_paid_holidays) - Preview a company's paid holidays

### [i9_verification](docs/sdks/i9verification/README.md)

* [get_authorization](docs/sdks/i9verification/README.md#get_authorization) - Get an employee's I-9 authorization
* [update](docs/sdks/i9verification/README.md#update) - Create or update an employee's I-9 authorization
* [get_document_options](docs/sdks/i9verification/README.md#get_document_options) - Get an employee's I-9 verification document options
* [get_documents](docs/sdks/i9verification/README.md#get_documents) - Get an employee's I-9 verification documents
* [create_documents](docs/sdks/i9verification/README.md#create_documents) - Create an employee's I-9 authorization verification documents
* [delete_document](docs/sdks/i9verification/README.md#delete_document) - Delete an employee's I-9 verification document
* [employer_sign](docs/sdks/i9verification/README.md#employer_sign) - Employer sign an employee's Form I-9

### [industry_selection](docs/sdks/industryselection/README.md)

* [get](docs/sdks/industryselection/README.md#get) - Get a company industry selection
* [update](docs/sdks/industryselection/README.md#update) - Update a company industry selection

### [introspection](docs/sdks/introspection/README.md)

* [get_info](docs/sdks/introspection/README.md#get_info) - Get info about the current access token
* [refresh_token](docs/sdks/introspection/README.md#refresh_token) - Refresh access token

### [invoices](docs/sdks/invoices/README.md)

* [get](docs/sdks/invoices/README.md#get) - Retrieve invoicing data for companies

### [jobs_and_compensations](docs/sdks/jobsandcompensations/README.md)

* [create_job](docs/sdks/jobsandcompensations/README.md#create_job) - Create a job
* [get_jobs](docs/sdks/jobsandcompensations/README.md#get_jobs) - Get jobs for an employee
* [get_job](docs/sdks/jobsandcompensations/README.md#get_job) - Get a job
* [update](docs/sdks/jobsandcompensations/README.md#update) - Update a job
* [delete](docs/sdks/jobsandcompensations/README.md#delete) - Delete an individual job
* [get_compensations](docs/sdks/jobsandcompensations/README.md#get_compensations) - Get compensations for a job
* [create_compensation](docs/sdks/jobsandcompensations/README.md#create_compensation) - Create a compensation
* [get_compensation](docs/sdks/jobsandcompensations/README.md#get_compensation) - Get a compensation
* [update_compensation](docs/sdks/jobsandcompensations/README.md#update_compensation) - Update a compensation
* [delete_compensation](docs/sdks/jobsandcompensations/README.md#delete_compensation) - Delete a compensation

### [locations](docs/sdks/locations/README.md)

* [create](docs/sdks/locations/README.md#create) - Create a company location
* [get](docs/sdks/locations/README.md#get) - Get company locations
* [retrieve](docs/sdks/locations/README.md#retrieve) - Get a location
* [update](docs/sdks/locations/README.md#update) - Update a location
* [get_minimum_wages](docs/sdks/locations/README.md#get_minimum_wages) - Get minimum wages for a location

### [notifications](docs/sdks/notifications/README.md)

* [get_details](docs/sdks/notifications/README.md#get_details) - Get a notification's details

### [pay_schedules](docs/sdks/payschedules/README.md)

* [create](docs/sdks/payschedules/README.md#create) - Create a new pay schedule
* [get_all](docs/sdks/payschedules/README.md#get_all) - Get the pay schedules for a company
* [get_preview](docs/sdks/payschedules/README.md#get_preview) - Preview pay schedule dates
* [get](docs/sdks/payschedules/README.md#get) - Get a pay schedule
* [update](docs/sdks/payschedules/README.md#update) - Update a pay schedule
* [get_pay_periods](docs/sdks/payschedules/README.md#get_pay_periods) - Get pay periods for a company
* [get_unprocessed_termination_periods](docs/sdks/payschedules/README.md#get_unprocessed_termination_periods) - Get termination pay periods for a company
* [get_assignments](docs/sdks/payschedules/README.md#get_assignments) - Get pay schedule assignments for a company
* [preview_assignment](docs/sdks/payschedules/README.md#preview_assignment) - Preview pay schedule assignments for a company
* [assign](docs/sdks/payschedules/README.md#assign) - Assign pay schedules for a company

### [payment_configs](docs/sdks/paymentconfigssdk/README.md)

* [get](docs/sdks/paymentconfigssdk/README.md#get) - Get a company's payment configs
* [update](docs/sdks/paymentconfigssdk/README.md#update) - Update a company's payment configs

### [payrolls](docs/sdks/payrolls/README.md)

* [create_off_cycle](docs/sdks/payrolls/README.md#create_off_cycle) - Create an off-cycle payroll
* [list](docs/sdks/payrolls/README.md#list) - Get all payrolls for a company
* [get_approved_reversals](docs/sdks/payrolls/README.md#get_approved_reversals) - Get approved payroll reversals
* [get](docs/sdks/payrolls/README.md#get) - Get a single payroll
* [update](docs/sdks/payrolls/README.md#update) - Update a payroll by ID
* [delete](docs/sdks/payrolls/README.md#delete) - Delete a payroll
* [prepare](docs/sdks/payrolls/README.md#prepare) - Prepare a payroll for update
* [get_receipt](docs/sdks/payrolls/README.md#get_receipt) - Get a single payroll receipt
* [get_blockers](docs/sdks/payrolls/README.md#get_blockers) - Get all payroll blockers for a company
* [skip](docs/sdks/payrolls/README.md#skip) - Skip a payroll
* [calculate_gross_up](docs/sdks/payrolls/README.md#calculate_gross_up) - Calculate gross up
* [calculate](docs/sdks/payrolls/README.md#calculate) - Calculate a payroll
* [submit](docs/sdks/payrolls/README.md#submit) - Submit payroll
* [cancel](docs/sdks/payrolls/README.md#cancel) - Cancel a payroll
* [get_pay_stub](docs/sdks/payrolls/README.md#get_pay_stub) - Get an employee pay stub (pdf)
* [get_pay_stubs](docs/sdks/payrolls/README.md#get_pay_stubs) - Get an employee's pay stubs
* [generate_printable_checks](docs/sdks/payrolls/README.md#generate_printable_checks) - Generate printable payroll checks (pdf)

### [recovery_cases](docs/sdks/recoverycases/README.md)

* [get](docs/sdks/recoverycases/README.md#get) - Get all recovery cases for a company
* [redebit](docs/sdks/recoverycases/README.md#redebit) - Initiate a redebit for a recovery case

### [reports](docs/sdks/reports/README.md)

* [create_custom](docs/sdks/reports/README.md#create_custom) - Create a custom report
* [get](docs/sdks/reports/README.md#get) - Get a report
* [get_template](docs/sdks/reports/README.md#get_template) - Get a report template

### [signatories](docs/sdks/signatories/README.md)

* [create](docs/sdks/signatories/README.md#create) - Create a signatory
* [list](docs/sdks/signatories/README.md#list) - Get all company signatories
* [invite](docs/sdks/signatories/README.md#invite) - Invite a signatory
* [update](docs/sdks/signatories/README.md#update) - Update a signatory
* [delete](docs/sdks/signatories/README.md#delete) - Delete a signatory

### [tax_requirements](docs/sdks/taxrequirements/README.md)

* [get](docs/sdks/taxrequirements/README.md#get) - Get State Tax Requirements
* [update_state](docs/sdks/taxrequirements/README.md#update_state) - Update State Tax Requirements
* [get_all](docs/sdks/taxrequirements/README.md#get_all) - Get All Tax Requirement States

### [time_off_policies](docs/sdks/timeoffpolicies/README.md)

* [calculate_accruing_time_off_hours](docs/sdks/timeoffpolicies/README.md#calculate_accruing_time_off_hours) - Calculate accruing time off hours
* [get](docs/sdks/timeoffpolicies/README.md#get) - Get a time off policy
* [update](docs/sdks/timeoffpolicies/README.md#update) - Update a time off policy
* [get_all](docs/sdks/timeoffpolicies/README.md#get_all) - Get all time off policies
* [create](docs/sdks/timeoffpolicies/README.md#create) - Create a time off policy
* [add_employees](docs/sdks/timeoffpolicies/README.md#add_employees) - Add employees to a time off policy
* [remove_employees](docs/sdks/timeoffpolicies/README.md#remove_employees) - Remove employees from a time off policy
* [update_balance](docs/sdks/timeoffpolicies/README.md#update_balance) - Update employee time off hour balances
* [deactivate](docs/sdks/timeoffpolicies/README.md#deactivate) - Deactivate a time off policy

### [webhooks](docs/sdks/webhooks/README.md)

* [create_subscription](docs/sdks/webhooks/README.md#create_subscription) - Create a webhook subscription
* [list_subscriptions](docs/sdks/webhooks/README.md#list_subscriptions) - List webhook subscriptions
* [update_subscription](docs/sdks/webhooks/README.md#update_subscription) - Update a webhook subscription
* [get_subscription](docs/sdks/webhooks/README.md#get_subscription) - Get a webhook subscription
* [delete_subscription](docs/sdks/webhooks/README.md#delete_subscription) - Delete a webhook subscription
* [verify](docs/sdks/webhooks/README.md#verify) - Verify the webhook subscription
* [request_verification_token](docs/sdks/webhooks/README.md#request_verification_token) - Request the webhook subscription verification_token

### [wire_in_requests](docs/sdks/wireinrequests/README.md)

* [get](docs/sdks/wireinrequests/README.md#get) - Get a single Wire In Request
* [submit](docs/sdks/wireinrequests/README.md#submit) - Submit a wire in request
* [list](docs/sdks/wireinrequests/README.md#list) - Get all Wire In Requests for a company

</details>
<!-- End Available Resources and Operations [operations] -->

<!-- Start File uploads [file-upload] -->
## File uploads

Certain SDK methods accept file objects as part of a request body or multi-part request. It is possible and typically recommended to upload files as a stream rather than reading the entire contents into memory. This avoids excessive memory consumption and potentially crashing with out-of-memory errors when working with very large files. The following example demonstrates how to attach a file stream to a request.

> [!TIP]
>
> For endpoints that handle file uploads bytes arrays can also be used. However, using streams is recommended for large files.
>

```python
import gusto_embedded
from gusto_embedded import Gusto
import os

with Gusto(
    company_access_auth=os.getenv("GUSTO_COMPANY_ACCESS_AUTH", ""),
) as gusto:

    res = gusto.company_attachments.create(company_id="<id>", document={
        "file_name": "example.file",
        "content": open("example.file", "rb"),
    }, category=gusto_embedded.PostV1CompaniesAttachmentCategory.GEP_NOTICE)

    # Handle response
    print(res)

```
<!-- End File uploads [file-upload] -->

<!-- Start Retries [retries] -->
## Retries

Some of the endpoints in this SDK support retries. If you use the SDK without any configuration, it will fall back to the default retry strategy provided by the API. However, the default retry strategy can be overridden on a per-operation basis, or across the entire SDK.

To change the default retry strategy for a single API call, simply provide a `RetryConfig` object to the call:
```python
from gusto_embedded import Gusto
from gusto_embedded.utils import BackoffStrategy, RetryConfig
import os

with Gusto(
    company_access_auth=os.getenv("GUSTO_COMPANY_ACCESS_AUTH", ""),
) as gusto:

    res = gusto.introspection.get_info(,
        RetryConfig("backoff", BackoffStrategy(1, 50, 1.1, 100), False))

    # Handle response
    print(res)

```

If you'd like to override the default retry strategy for all operations that support retries, you can use the `retry_config` optional parameter when initializing the SDK:
```python
from gusto_embedded import Gusto
from gusto_embedded.utils import BackoffStrategy, RetryConfig
import os

with Gusto(
    retry_config=RetryConfig("backoff", BackoffStrategy(1, 50, 1.1, 100), False),
    company_access_auth=os.getenv("GUSTO_COMPANY_ACCESS_AUTH", ""),
) as gusto:

    res = gusto.introspection.get_info()

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

When custom error responses are specified for an operation, the SDK may also raise their associated exceptions. You can refer to respective *Errors* tables in SDK docs for more details on possible exception types for each operation. For example, the `create_partner_managed_async` method may raise the following exceptions:

| Error Type                            | Status Code | Content Type     |
| ------------------------------------- | ----------- | ---------------- |
| models.UnprocessableEntityErrorObject | 422         | application/json |
| models.APIError                       | 4XX, 5XX    | \*/\*            |

### Example

```python
import gusto_embedded
from gusto_embedded import Gusto, models
import os

with Gusto() as gusto:
    res = None
    try:

        res = gusto.companies.create_partner_managed(security=gusto_embedded.PostV1PartnerManagedCompaniesSecurity(
            system_access_auth=os.getenv("GUSTO_SYSTEM_ACCESS_AUTH", ""),
        ), user={
            "first_name": "Frank",
            "last_name": "Ocean",
            "email": "frank@example.com",
            "phone": "2345558899",
        }, company={
            "name": "Frank's Ocean, LLC",
            "trade_name": "Frank’s Ocean",
            "ein": "123456789",
            "contractor_only": False,
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
from gusto_embedded import Gusto
import os

with Gusto(
    server="prod",
    company_access_auth=os.getenv("GUSTO_COMPANY_ACCESS_AUTH", ""),
) as gusto:

    res = gusto.introspection.get_info()

    # Handle response
    print(res)

```

### Override Server URL Per-Client

The default server can also be overridden globally by passing a URL to the `server_url: str` optional parameter when initializing the SDK client instance. For example:
```python
from gusto_embedded import Gusto
import os

with Gusto(
    server_url="https://api.gusto-demo.com",
    company_access_auth=os.getenv("GUSTO_COMPANY_ACCESS_AUTH", ""),
) as gusto:

    res = gusto.introspection.get_info()

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
from gusto_embedded import Gusto
import httpx

http_client = httpx.Client(headers={"x-custom-header": "someValue"})
s = Gusto(client=http_client)
```

or you could wrap the client with your own custom logic:
```python
from gusto_embedded import Gusto
from gusto_embedded.httpclient import AsyncHttpClient
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

s = Gusto(async_client=CustomClient(httpx.AsyncClient()))
```
<!-- End Custom HTTP Client [http-client] -->

<!-- Start Resource Management [resource-management] -->
## Resource Management

The `Gusto` class implements the context manager protocol and registers a finalizer function to close the underlying sync and async HTTPX clients it uses under the hood. This will close HTTP connections, release memory and free up other resources held by the SDK. In short-lived Python programs and notebooks that make a few SDK method calls, resource management may not be a concern. However, in longer-lived programs, it is beneficial to create a single SDK instance via a [context manager][context-manager] and reuse it across the application.

[context-manager]: https://docs.python.org/3/reference/datamodel.html#context-managers

```python
from gusto_embedded import Gusto
import os
def main():
    with Gusto(
        company_access_auth=os.getenv("GUSTO_COMPANY_ACCESS_AUTH", ""),
    ) as gusto:
        # Rest of application here...


# Or when using async:
async def amain():
    async with Gusto(
        company_access_auth=os.getenv("GUSTO_COMPANY_ACCESS_AUTH", ""),
    ) as gusto:
        # Rest of application here...
```
<!-- End Resource Management [resource-management] -->

<!-- Start Debugging [debug] -->
## Debugging

You can setup your SDK to emit debug logs for SDK requests and responses.

You can pass your own logger class directly into your SDK.
```python
from gusto_embedded import Gusto
import logging

logging.basicConfig(level=logging.DEBUG)
s = Gusto(debug_logger=logging.getLogger("gusto_embedded"))
```

You can also enable a default debug logger by setting an environment variable `GUSTO_DEBUG` to true.
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

### SDK Created by [Speakeasy](https://www.speakeasy.com/?utm_source=gusto&utm_campaign=python)
