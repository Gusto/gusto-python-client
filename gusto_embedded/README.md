# gusto

Developer-friendly & type-safe Python SDK specifically catered to leverage *gusto* API.

<div align="left">
    <a href="https://www.speakeasy.com/?utm_source=gusto&utm_campaign=python"><img src="https://custom-icon-badges.demolab.com/badge/-Built%20By%20Speakeasy-212015?style=for-the-badge&logoColor=FBE331&logo=speakeasy&labelColor=545454" /></a>
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
* [gusto](#gusto)
  * [SDK Installation](#sdk-installation)
  * [IDE Support](#ide-support)
  * [SDK Example Usage](#sdk-example-usage)
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

> [!TIP]
> To finish publishing your SDK to PyPI you must [run your first generation action](https://www.speakeasy.com/docs/github-setup#step-by-step-guide).


> [!NOTE]
> **Python version upgrade policy**
>
> Once a Python version reaches its [official end of life date](https://devguide.python.org/versions/), a 3-month grace period is provided for users to upgrade. Following this grace period, the minimum python version supported in the SDK will be updated.

The SDK can be installed with either *pip* or *poetry* package managers.

### PIP

*PIP* is the default package installer for Python, enabling easy installation and management of packages from PyPI via the command line.

```bash
pip install git+<UNSET>.git
```

### Poetry

*Poetry* is a modern tool that simplifies dependency management and package publishing by using a single `pyproject.toml` file to handle project metadata and dependencies.

```bash
poetry add git+<UNSET>.git
```

### Shell and script usage with `uv`

You can use this SDK in a Python shell with [uv](https://docs.astral.sh/uv/) and the `uvx` command that comes with it like so:

```shell
uvx --from gusto python
```

It's also possible to write a standalone Python script without needing to set up a whole project like so:

```python
#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.9"
# dependencies = [
#     "gusto",
# ]
# ///

from gusto import Gusto

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

<!-- Start SDK Example Usage [usage] -->
## SDK Example Usage

### Example

```python
# Synchronous Example
from gusto import Gusto
import os

with Gusto(
    company_access_auth=os.getenv("GUSTO_COMPANY_ACCESS_AUTH", ""),
) as g_client:

    res = g_client.introspection.get_v1_token_info()

    # Handle response
    print(res)
```

</br>

The same SDK client can also be used to make asychronous requests by importing asyncio.
```python
# Asynchronous Example
import asyncio
from gusto import Gusto
import os

async def main():
    async with Gusto(
        company_access_auth=os.getenv("GUSTO_COMPANY_ACCESS_AUTH", ""),
    ) as g_client:

        res = await g_client.introspection.get_v1_token_info_async()

        # Handle response
        print(res)

asyncio.run(main())
```
<!-- End SDK Example Usage [usage] -->

<!-- Start Authentication [security] -->
## Authentication

### Per-Client Security Schemes

This SDK supports the following security scheme globally:

| Name                  | Type | Scheme      | Environment Variable        |
| --------------------- | ---- | ----------- | --------------------------- |
| `company_access_auth` | http | HTTP Bearer | `GUSTO_COMPANY_ACCESS_AUTH` |

To authenticate with the API the `company_access_auth` parameter must be set when initializing the SDK client instance. For example:
```python
from gusto import Gusto
import os

with Gusto(
    company_access_auth=os.getenv("GUSTO_COMPANY_ACCESS_AUTH", ""),
) as g_client:

    res = g_client.introspection.get_v1_token_info()

    # Handle response
    print(res)

```

### Per-Operation Security Schemes

Some operations in this SDK require the security scheme to be specified at the request level. For example:
```python
import gusto
from gusto import Gusto
import os

with Gusto() as g_client:

    res = g_client.companies.post_v1_partner_managed_companies(security=gusto.PostV1PartnerManagedCompaniesSecurity(
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

* [list](docs/sdks/achtransactions/README.md#list) - Get all ACH transactions for a company

### [bank_accounts](docs/sdks/bankaccounts/README.md)

* [post_v1_companies_company_id_bank_accounts](docs/sdks/bankaccounts/README.md#post_v1_companies_company_id_bank_accounts) - Create a company bank account
* [get_v1_companies_company_id_bank_accounts](docs/sdks/bankaccounts/README.md#get_v1_companies_company_id_bank_accounts) - Get all company bank accounts
* [put_v1_companies_company_id_bank_accounts_verify](docs/sdks/bankaccounts/README.md#put_v1_companies_company_id_bank_accounts_verify) - Verify a company bank account
* [post_v1_plaid_processor_token](docs/sdks/bankaccounts/README.md#post_v1_plaid_processor_token) - Create a bank account from a plaid processor token

### [companies](docs/sdks/companies/README.md)

* [post_v1_partner_managed_companies](docs/sdks/companies/README.md#post_v1_partner_managed_companies) - Create a partner managed company
* [get_v1_companies](docs/sdks/companies/README.md#get_v1_companies) - Get a company
* [put_v1_companies](docs/sdks/companies/README.md#put_v1_companies) - Update a company
* [put_v1_partner_managed_companies_company_uuid_migrate](docs/sdks/companies/README.md#put_v1_partner_managed_companies_company_uuid_migrate) - Migrate company to embedded payroll
* [post_partner_managed_companies_company_uuid_accept_terms_of_service](docs/sdks/companies/README.md#post_partner_managed_companies_company_uuid_accept_terms_of_service) - Accept terms of service for a company user
* [post_partner_managed_companies_company_uuid_retrieve_terms_of_service](docs/sdks/companies/README.md#post_partner_managed_companies_company_uuid_retrieve_terms_of_service) - Retrieve terms of service status for a company user
* [post_v1_companies_company_id_admins](docs/sdks/companies/README.md#post_v1_companies_company_id_admins) - Create an admin for the company
* [get_v1_companies_company_id_admins](docs/sdks/companies/README.md#get_v1_companies_company_id_admins) - Get all the admins at a company
* [get_v1_company_onboarding_status](docs/sdks/companies/README.md#get_v1_company_onboarding_status) - Get the company's onboarding status
* [get_v1_company_finish_onboarding](docs/sdks/companies/README.md#get_v1_company_finish_onboarding) - Finish company onboarding
* [get_v1_companies_company_id_custom_fields](docs/sdks/companies/README.md#get_v1_companies_company_id_custom_fields) - Get the custom fields of a company

### [company_attachment](docs/sdks/companyattachmentsdk/README.md)

* [get_v1_companies_attachment](docs/sdks/companyattachmentsdk/README.md#get_v1_companies_attachment) - Get Company Attachment Details
* [get_v1_companies_attachment_url](docs/sdks/companyattachmentsdk/README.md#get_v1_companies_attachment_url) - Get a temporary url to download the Company Attachment file
* [get_v1_companies_attachments](docs/sdks/companyattachmentsdk/README.md#get_v1_companies_attachments) - Get List of Company Attachments
* [post_v1_companies_attachment](docs/sdks/companyattachmentsdk/README.md#post_v1_companies_attachment) - Create Company Attachment and Upload File

### [company_benefits](docs/sdks/companybenefits/README.md)

* [post_v1_companies_company_id_company_benefits](docs/sdks/companybenefits/README.md#post_v1_companies_company_id_company_benefits) - Create a company benefit
* [get_v1_companies_company_id_company_benefits](docs/sdks/companybenefits/README.md#get_v1_companies_company_id_company_benefits) - Get benefits for a company
* [get_v1_company_benefits_company_benefit_id](docs/sdks/companybenefits/README.md#get_v1_company_benefits_company_benefit_id) - Get a company benefit
* [put_v1_company_benefits_company_benefit_id](docs/sdks/companybenefits/README.md#put_v1_company_benefits_company_benefit_id) - Update a company benefit
* [delete_v1_company_benefits_company_benefit_id](docs/sdks/companybenefits/README.md#delete_v1_company_benefits_company_benefit_id) - Delete a company benefit
* [get_v1_benefits](docs/sdks/companybenefits/README.md#get_v1_benefits) - Get all benefits supported by Gusto
* [get_v1_benefits_benefit_id](docs/sdks/companybenefits/README.md#get_v1_benefits_benefit_id) - Get a supported benefit by ID
* [get_v1_benefits_company_benefit_id_summary](docs/sdks/companybenefits/README.md#get_v1_benefits_company_benefit_id_summary) - Get company benefit summary by company benefit id.
* [get_v1_company_benefits_company_benefit_id_employee_benefits](docs/sdks/companybenefits/README.md#get_v1_company_benefits_company_benefit_id_employee_benefits) - Get all employee benefits for a company benefit
* [bulk_update](docs/sdks/companybenefits/README.md#bulk_update) - Bulk update employee benefits for a company benefit
* [get_v1_benefits_benefits_id_requirements](docs/sdks/companybenefits/README.md#get_v1_benefits_benefits_id_requirements) - Get benefit fields requirements by ID

### [company_federal_taxes](docs/sdks/companyfederaltaxes/README.md)

* [get_details](docs/sdks/companyfederaltaxes/README.md#get_details) - Get Federal Tax Details

### [company_forms](docs/sdks/companyforms/README.md)

* [get_v1_company_forms](docs/sdks/companyforms/README.md#get_v1_company_forms) - Get all company forms
* [get_v1_company_form](docs/sdks/companyforms/README.md#get_v1_company_form) - Get a company form
* [get_v1_company_form_pdf](docs/sdks/companyforms/README.md#get_v1_company_form_pdf) - Get a company form pdf
* [put_v1_company_form_sign](docs/sdks/companyforms/README.md#put_v1_company_form_sign) - Sign a company form

### [compensations](docs/sdks/compensations/README.md)

* [update](docs/sdks/compensations/README.md#update) - Update a compensation
* [delete](docs/sdks/compensations/README.md#delete) - Delete a compensation

### [contractor_documents](docs/sdks/contractordocuments/README.md)

* [get_v1_contractor_documents](docs/sdks/contractordocuments/README.md#get_v1_contractor_documents) - Get all contractor documents
* [get_v1_contractor_document](docs/sdks/contractordocuments/README.md#get_v1_contractor_document) - Get a contractor document
* [get_v1_contractor_document_pdf](docs/sdks/contractordocuments/README.md#get_v1_contractor_document_pdf) - Get the contractor document pdf
* [put_v1_contractor_document_sign](docs/sdks/contractordocuments/README.md#put_v1_contractor_document_sign) - Sign a contractor document

### [contractor_forms](docs/sdks/contractorforms/README.md)

* [get_v1_contractor_form](docs/sdks/contractorforms/README.md#get_v1_contractor_form) - Get a contractor form
* [get_v1_contractor_form_pdf](docs/sdks/contractorforms/README.md#get_v1_contractor_form_pdf) - Get the contractor form pdf
* [post_v1_sandbox_generate_1099](docs/sdks/contractorforms/README.md#post_v1_sandbox_generate_1099) - Generate a 1099 form [DEMO]

### [contractor_payment_groups](docs/sdks/contractorpaymentgroups/README.md)

* [post_v1_companies_company_id_contractor_payment_groups](docs/sdks/contractorpaymentgroups/README.md#post_v1_companies_company_id_contractor_payment_groups) - Create a contractor payment group
* [get_v1_companies_company_id_contractor_payment_groups](docs/sdks/contractorpaymentgroups/README.md#get_v1_companies_company_id_contractor_payment_groups) - Get contractor payment groups for a company
* [post_v1_companies_company_id_contractor_payment_groups_preview](docs/sdks/contractorpaymentgroups/README.md#post_v1_companies_company_id_contractor_payment_groups_preview) - Preview a contractor payment group
* [get_v1_contractor_payment_groups_contractor_payment_group_id](docs/sdks/contractorpaymentgroups/README.md#get_v1_contractor_payment_groups_contractor_payment_group_id) - Fetch a contractor payment group
* [delete_v1_contractor_payment_groups_contractor_payment_group_id](docs/sdks/contractorpaymentgroups/README.md#delete_v1_contractor_payment_groups_contractor_payment_group_id) - Cancel a contractor payment group
* [put_v1_contractor_payment_groups_contractor_payment_group_id_fund](docs/sdks/contractorpaymentgroups/README.md#put_v1_contractor_payment_groups_contractor_payment_group_id_fund) - Fund a contractor payment group [DEMO]

### [contractor_payment_method](docs/sdks/contractorpaymentmethodsdk/README.md)

* [list_bank_accounts](docs/sdks/contractorpaymentmethodsdk/README.md#list_bank_accounts) - Get all contractor bank accounts

### [contractor_payment_methods](docs/sdks/contractorpaymentmethods/README.md)

* [create](docs/sdks/contractorpaymentmethods/README.md#create) - Create a contractor bank account
* [get_v1_contractors_contractor_uuid_payment_method](docs/sdks/contractorpaymentmethods/README.md#get_v1_contractors_contractor_uuid_payment_method) - Get a contractor's payment method

### [contractor_payments](docs/sdks/contractorpayments/README.md)

* [get_v1_contractor_payments_contractor_payment_uuid_receipt](docs/sdks/contractorpayments/README.md#get_v1_contractor_payments_contractor_payment_uuid_receipt) - Get a single contractor payment receipt
* [get_v1_contractor_payments_contractor_payment_uuid_fund](docs/sdks/contractorpayments/README.md#get_v1_contractor_payments_contractor_payment_uuid_fund) - Fund a contractor payment [DEMO]
* [post_v1_companies_company_id_contractor_payments](docs/sdks/contractorpayments/README.md#post_v1_companies_company_id_contractor_payments) - Create a contractor payment
* [get](docs/sdks/contractorpayments/README.md#get) - Get contractor payments for a company
* [get_by_id](docs/sdks/contractorpayments/README.md#get_by_id) - Get a single contractor payment
* [delete](docs/sdks/contractorpayments/README.md#delete) - Cancel a contractor payment
* [get_companies_company_uuid_contractor_payments_preview](docs/sdks/contractorpayments/README.md#get_companies_company_uuid_contractor_payments_preview) - Preview contractor payment debit date

### [contractors](docs/sdks/contractors/README.md)

* [post_v1_companies_company_uuid_contractors](docs/sdks/contractors/README.md#post_v1_companies_company_uuid_contractors) - Create a contractor
* [get_v1_companies_company_uuid_contractors](docs/sdks/contractors/README.md#get_v1_companies_company_uuid_contractors) - Get contractors of a company
* [get_v1_contractors_contractor_uuid](docs/sdks/contractors/README.md#get_v1_contractors_contractor_uuid) - Get a contractor
* [put_v1_contractors_contractor_uuid](docs/sdks/contractors/README.md#put_v1_contractors_contractor_uuid) - Update a contractor
* [delete_v1_contractors_contractor_uuid](docs/sdks/contractors/README.md#delete_v1_contractors_contractor_uuid) - Delete a contractor
* [get_v1_contractors_contractor_uuid_onboarding_status](docs/sdks/contractors/README.md#get_v1_contractors_contractor_uuid_onboarding_status) - Get the contractor's onboarding status
* [put_v1_contractors_contractor_uuid_onboarding_status](docs/sdks/contractors/README.md#put_v1_contractors_contractor_uuid_onboarding_status) - Change the contractor's onboarding status
* [get_v1_contractors_contractor_uuid_address](docs/sdks/contractors/README.md#get_v1_contractors_contractor_uuid_address) - Get a contractor address
* [put_v1_contractors_contractor_uuid_address](docs/sdks/contractors/README.md#put_v1_contractors_contractor_uuid_address) - Update a contractor's address
* [get_forms](docs/sdks/contractors/README.md#get_forms) - Get all contractor forms
* [put_v1_contractors_contractor_id_payment_method](docs/sdks/contractors/README.md#put_v1_contractors_contractor_id_payment_method) - Update a contractor's payment method

### [departments](docs/sdks/departments/README.md)

* [post_departments](docs/sdks/departments/README.md#post_departments) - Create a department
* [get_companies_departments](docs/sdks/departments/README.md#get_companies_departments) - Get all departments of a company
* [get_department](docs/sdks/departments/README.md#get_department) - Get a department
* [put_departments](docs/sdks/departments/README.md#put_departments) - Update a department
* [delete_department](docs/sdks/departments/README.md#delete_department) - Delete a department
* [put_add_people_to_department](docs/sdks/departments/README.md#put_add_people_to_department) - Add people to a department
* [put_remove_people_from_department](docs/sdks/departments/README.md#put_remove_people_from_department) - Remove people from a department

### [earning_types](docs/sdks/earningtypes/README.md)

* [post_v1_companies_company_id_earning_types](docs/sdks/earningtypes/README.md#post_v1_companies_company_id_earning_types) - Create a custom earning type
* [get_v1_companies_company_id_earning_types](docs/sdks/earningtypes/README.md#get_v1_companies_company_id_earning_types) - Get all earning types for a company
* [put_v1_companies_company_id_earning_types_earning_type_uuid](docs/sdks/earningtypes/README.md#put_v1_companies_company_id_earning_types_earning_type_uuid) - Update an earning type
* [delete_v1_companies_company_id_earning_types_earning_type_uuid](docs/sdks/earningtypes/README.md#delete_v1_companies_company_id_earning_types_earning_type_uuid) - Deactivate an earning type

### [employee_addresses](docs/sdks/employeeaddresses/README.md)

* [get_home](docs/sdks/employeeaddresses/README.md#get_home) - Get an employee's home addresses
* [post_v1_employees_employee_id_home_addresses](docs/sdks/employeeaddresses/README.md#post_v1_employees_employee_id_home_addresses) - Create an employee's home address
* [get](docs/sdks/employeeaddresses/README.md#get) - Get an employee's home address
* [delete](docs/sdks/employeeaddresses/README.md#delete) - Delete an employee's home address
* [list_work_addresses](docs/sdks/employeeaddresses/README.md#list_work_addresses) - Get an employee's work addresses
* [update](docs/sdks/employeeaddresses/README.md#update) - Update an employee work address

### [employee_bank_accounts](docs/sdks/employeebankaccounts/README.md)

* [delete](docs/sdks/employeebankaccounts/README.md#delete) - Delete an employee bank account

### [employee_benefits](docs/sdks/employeebenefits/README.md)

* [create](docs/sdks/employeebenefits/README.md#create) - Create an employee benefit
* [get_v1_employees_employee_id_employee_benefits](docs/sdks/employeebenefits/README.md#get_v1_employees_employee_id_employee_benefits) - Get all benefits for an employee
* [get_v1_employee_benefits_employee_benefit_id](docs/sdks/employeebenefits/README.md#get_v1_employee_benefits_employee_benefit_id) - Get an employee benefit
* [put_v1_employee_benefits_employee_benefit_id](docs/sdks/employeebenefits/README.md#put_v1_employee_benefits_employee_benefit_id) - Update an employee benefit
* [delete_v1_employee_benefits_employee_benefit_id](docs/sdks/employeebenefits/README.md#delete_v1_employee_benefits_employee_benefit_id) - Delete an employee benefit
* [create_ytd_benefit_amounts](docs/sdks/employeebenefits/README.md#create_ytd_benefit_amounts) - Create year-to-date benefit amounts from a different company
* [get_ytd_from_different_company](docs/sdks/employeebenefits/README.md#get_ytd_from_different_company) - Get year-to-date benefit amounts from a different company

### [employee_employments](docs/sdks/employeeemployments/README.md)

* [list_terminations](docs/sdks/employeeemployments/README.md#list_terminations) - Get terminations for an employee
* [put_v1_terminations_employee_id](docs/sdks/employeeemployments/README.md#put_v1_terminations_employee_id) - Update an employee termination
* [put_v1_employees_employee_id_rehire](docs/sdks/employeeemployments/README.md#put_v1_employees_employee_id_rehire) - Update an employee rehire
* [get_v1_employees_employee_id_rehire](docs/sdks/employeeemployments/README.md#get_v1_employees_employee_id_rehire) - Get an employee rehire
* [delete_v1_employees_employee_id_rehire](docs/sdks/employeeemployments/README.md#delete_v1_employees_employee_id_rehire) - Delete an employee rehire
* [get_v1_employees_employee_id_employment_history](docs/sdks/employeeemployments/README.md#get_v1_employees_employee_id_employment_history) - Get employment history for an employee

### [employee_forms](docs/sdks/employeeforms/README.md)

* [post_v1_sandbox_generate_w2](docs/sdks/employeeforms/README.md#post_v1_sandbox_generate_w2) - Generate a W2 form [DEMO]
* [get_v1_employee_forms](docs/sdks/employeeforms/README.md#get_v1_employee_forms) - Get all employee forms
* [get](docs/sdks/employeeforms/README.md#get) - Get an employee form
* [get_v1_employee_form_pdf](docs/sdks/employeeforms/README.md#get_v1_employee_form_pdf) - Get the employee form pdf
* [put_v1_employee_form_sign](docs/sdks/employeeforms/README.md#put_v1_employee_form_sign) - Sign an employee form

### [employee_onboarding](docs/sdks/employeeonboarding/README.md)

* [update_documents_config](docs/sdks/employeeonboarding/README.md#update_documents_config) - Update an employee's onboarding documents config

### [employee_payment_method](docs/sdks/employeepaymentmethodsdk/README.md)

* [get_all](docs/sdks/employeepaymentmethodsdk/README.md#get_all) - Get all employee bank accounts
* [put_v1_employees_employee_id_payment_method](docs/sdks/employeepaymentmethodsdk/README.md#put_v1_employees_employee_id_payment_method) - Update an employee's payment method

### [employee_payment_methods](docs/sdks/employeepaymentmethods/README.md)

* [post_v1_employees_employee_id_bank_accounts](docs/sdks/employeepaymentmethods/README.md#post_v1_employees_employee_id_bank_accounts) - Create an employee bank account
* [update](docs/sdks/employeepaymentmethods/README.md#update) - Update an employee bank account
* [get_v1_employees_employee_id_payment_method](docs/sdks/employeepaymentmethods/README.md#get_v1_employees_employee_id_payment_method) - Get an employee's payment method

### [employee_tax_setup](docs/sdks/employeetaxsetup/README.md)

* [get_v1_employees_employee_id_federal_taxes](docs/sdks/employeetaxsetup/README.md#get_v1_employees_employee_id_federal_taxes) - Get an employee's federal taxes
* [put_v1_employees_employee_id_federal_taxes](docs/sdks/employeetaxsetup/README.md#put_v1_employees_employee_id_federal_taxes) - Update an employee's federal taxes
* [get_v1_employees_employee_id_state_taxes](docs/sdks/employeetaxsetup/README.md#get_v1_employees_employee_id_state_taxes) - Get an employee's state taxes

### [employee_taxes](docs/sdks/employeetaxes/README.md)

* [update](docs/sdks/employeetaxes/README.md#update) - Update an employee's state taxes

### [employee_terminations](docs/sdks/employeeterminations/README.md)

* [create](docs/sdks/employeeterminations/README.md#create) - Create an employee termination

### [employees](docs/sdks/employees/README.md)

* [post_v1_employees](docs/sdks/employees/README.md#post_v1_employees) - Create an employee
* [list](docs/sdks/employees/README.md#list) - Get employees of a company
* [post_v1_historical_employees](docs/sdks/employees/README.md#post_v1_historical_employees) - Create a historical employee
* [update_historical_employee](docs/sdks/employees/README.md#update_historical_employee) - Update a historical employee
* [get](docs/sdks/employees/README.md#get) - Get an employee
* [put_v1_employees](docs/sdks/employees/README.md#put_v1_employees) - Update an employee
* [delete_v1_employee](docs/sdks/employees/README.md#delete_v1_employee) - Delete an onboarding employee
* [get_v1_employees_employee_id_custom_fields](docs/sdks/employees/README.md#get_v1_employees_employee_id_custom_fields) - Get an employee's custom fields
* [get_v1_employees_employee_id_onboarding_status](docs/sdks/employees/README.md#get_v1_employees_employee_id_onboarding_status) - Get the employee's onboarding status
* [put_v1_employees_employee_id_onboarding_status](docs/sdks/employees/README.md#put_v1_employees_employee_id_onboarding_status) - Update the employee's onboarding status
* [get_version_employees_time_off_activities](docs/sdks/employees/README.md#get_version_employees_time_off_activities) - Get employee time off activities
* [post_v1_employees_employee_id_rehire](docs/sdks/employees/README.md#post_v1_employees_employee_id_rehire) - Create an employee rehire
* [calculate_accruing_time_off_hours](docs/sdks/employees/README.md#calculate_accruing_time_off_hours) - Calculate accruing time off hours

### [events](docs/sdks/events/README.md)

* [get_events](docs/sdks/events/README.md#get_events) - Get all events

### [external_payrolls](docs/sdks/externalpayrolls/README.md)

* [post_v1_external_payroll](docs/sdks/externalpayrolls/README.md#post_v1_external_payroll) - Create a new external payroll for a company
* [get_v1_company_external_payrolls](docs/sdks/externalpayrolls/README.md#get_v1_company_external_payrolls) - Get external payrolls for a company
* [get_v1_external_payroll](docs/sdks/externalpayrolls/README.md#get_v1_external_payroll) - Get an external payroll
* [delete_v1_external_payroll](docs/sdks/externalpayrolls/README.md#delete_v1_external_payroll) - Delete an external payroll
* [put_v1_external_payroll](docs/sdks/externalpayrolls/README.md#put_v1_external_payroll) - Update an external payroll
* [get_v1_external_payroll_calculate_taxes](docs/sdks/externalpayrolls/README.md#get_v1_external_payroll_calculate_taxes) - Get tax suggestions for an external payroll
* [get_v1_tax_liabilities](docs/sdks/externalpayrolls/README.md#get_v1_tax_liabilities) - Get tax liabilities
* [put_v1_tax_liabilities](docs/sdks/externalpayrolls/README.md#put_v1_tax_liabilities) - Update tax liabilities
* [put_v1_tax_liabilities_finish](docs/sdks/externalpayrolls/README.md#put_v1_tax_liabilities_finish) - Finalize tax liabilities options and convert into processed payrolls

### [federal_tax_details](docs/sdks/federaltaxdetailssdk/README.md)

* [put_v1_companies_company_id_federal_tax_details](docs/sdks/federaltaxdetailssdk/README.md#put_v1_companies_company_id_federal_tax_details) - Update Federal Tax Details

### [flows](docs/sdks/flows/README.md)

* [post_v1_company_flows](docs/sdks/flows/README.md#post_v1_company_flows) - Create a flow

### [garnishments](docs/sdks/garnishments/README.md)

* [post_v1_employees_employee_id_garnishments](docs/sdks/garnishments/README.md#post_v1_employees_employee_id_garnishments) - Create a garnishment
* [get_v1_employees_employee_id_garnishments](docs/sdks/garnishments/README.md#get_v1_employees_employee_id_garnishments) - Get garnishments for an employee
* [get_by_id](docs/sdks/garnishments/README.md#get_by_id) - Get a garnishment
* [put_v1_garnishments_garnishment_id](docs/sdks/garnishments/README.md#put_v1_garnishments_garnishment_id) - Update a garnishment
* [get_v1_garnishments_child_support](docs/sdks/garnishments/README.md#get_v1_garnishments_child_support) - Get child support garnishment data

### [generated_documents](docs/sdks/generateddocuments/README.md)

* [get_v1_generated_documents_document_type_request_uuid](docs/sdks/generateddocuments/README.md#get_v1_generated_documents_document_type_request_uuid) - Get a generated document


### [holiday_pay_policies](docs/sdks/holidaypaypolicies/README.md)

* [get_companies_company_uuid_holiday_pay_policy](docs/sdks/holidaypaypolicies/README.md#get_companies_company_uuid_holiday_pay_policy) - Get a company's holiday pay policy
* [post_companies_company_uuid_holiday_pay_policy](docs/sdks/holidaypaypolicies/README.md#post_companies_company_uuid_holiday_pay_policy) - Create a holiday pay policy for a company
* [put_companies_company_uuid_holiday_pay_policy](docs/sdks/holidaypaypolicies/README.md#put_companies_company_uuid_holiday_pay_policy) - Update a company's holiday pay policy
* [delete_companies_company_uuid_holiday_pay_policy](docs/sdks/holidaypaypolicies/README.md#delete_companies_company_uuid_holiday_pay_policy) - Delete a company's holiday pay policy
* [put_companies_company_uuid_holiday_pay_policy_add](docs/sdks/holidaypaypolicies/README.md#put_companies_company_uuid_holiday_pay_policy_add) - Add employees to a company's holiday pay policy
* [put_companies_company_uuid_holiday_pay_policy_remove](docs/sdks/holidaypaypolicies/README.md#put_companies_company_uuid_holiday_pay_policy_remove) - Remove employees from a company's holiday pay policy
* [get_companies_company_uuid_paid_holidays](docs/sdks/holidaypaypolicies/README.md#get_companies_company_uuid_paid_holidays) - Preview a company's paid holidays

### [home_addresses](docs/sdks/homeaddresses/README.md)

* [update](docs/sdks/homeaddresses/README.md#update) - Update an employee's home address

### [i_9_verification](docs/sdks/i9verification/README.md)

* [get_v1_employees_employee_id_i9_authorization](docs/sdks/i9verification/README.md#get_v1_employees_employee_id_i9_authorization) - Get an employee's I-9 authorization
* [get_v1_employees_employee_id_i9_authorization_document_options](docs/sdks/i9verification/README.md#get_v1_employees_employee_id_i9_authorization_document_options) - Get an employee's I-9 verification document options
* [put_v1_employees_employee_id_i9_authorization_documents](docs/sdks/i9verification/README.md#put_v1_employees_employee_id_i9_authorization_documents) - Create an employee's I-9 authorization verification documents
* [put_v1_employees_employee_id_i9_authorization_employer_sign](docs/sdks/i9verification/README.md#put_v1_employees_employee_id_i9_authorization_employer_sign) - Employer sign an employee's Form I-9

### [i9_authorizations](docs/sdks/i9authorizations/README.md)

* [put_v1_employees_employee_id_i9_authorization](docs/sdks/i9authorizations/README.md#put_v1_employees_employee_id_i9_authorization) - Create or update an employee's I-9 authorization
* [get_v1_employees_employee_id_i9_authorization_documents](docs/sdks/i9authorizations/README.md#get_v1_employees_employee_id_i9_authorization_documents) - Get an employee's I-9 verification documents
* [delete_v1_employees_employee_id_i9_authorization_documents_document_id](docs/sdks/i9authorizations/README.md#delete_v1_employees_employee_id_i9_authorization_documents_document_id) - Delete an employee's I-9 verification document

### [industry_selections](docs/sdks/industryselections/README.md)

* [get_v1_company_industry](docs/sdks/industryselections/README.md#get_v1_company_industry) - Get a company industry selection
* [put_v1_company_industry](docs/sdks/industryselections/README.md#put_v1_company_industry) - Update a company industry selection

### [introspection](docs/sdks/introspection/README.md)

* [get_v1_token_info](docs/sdks/introspection/README.md#get_v1_token_info) - Get info about the current access token
* [refresh_access_token](docs/sdks/introspection/README.md#refresh_access_token) - Refresh access token

### [invoices](docs/sdks/invoices/README.md)

* [get_invoices_invoice_period](docs/sdks/invoices/README.md#get_invoices_invoice_period) - Retrieve invoicing data for companies

### [job_compensations](docs/sdks/jobcompensations/README.md)

* [create](docs/sdks/jobcompensations/README.md#create) - Create a compensation

### [jobs](docs/sdks/jobs/README.md)

* [get](docs/sdks/jobs/README.md#get) - Get a job
* [put_v1_jobs_job_id](docs/sdks/jobs/README.md#put_v1_jobs_job_id) - Update a job
* [delete](docs/sdks/jobs/README.md#delete) - Delete an individual job
* [get_v1_jobs_job_id_compensations](docs/sdks/jobs/README.md#get_v1_jobs_job_id_compensations) - Get compensations for a job

### [jobs_and_compensations](docs/sdks/jobsandcompensations/README.md)

* [create](docs/sdks/jobsandcompensations/README.md#create) - Create a job
* [list](docs/sdks/jobsandcompensations/README.md#list) - Get jobs for an employee
* [get_v1_compensations_compensation_id](docs/sdks/jobsandcompensations/README.md#get_v1_compensations_compensation_id) - Get a compensation

### [locations](docs/sdks/locations/README.md)

* [post_v1_companies_company_id_locations](docs/sdks/locations/README.md#post_v1_companies_company_id_locations) - Create a company location
* [list](docs/sdks/locations/README.md#list) - Get company locations
* [get_v1_locations_location_id](docs/sdks/locations/README.md#get_v1_locations_location_id) - Get a location
* [put_v1_locations_location_id](docs/sdks/locations/README.md#put_v1_locations_location_id) - Update a location
* [get_v1_locations_location_uuid_minimum_wages](docs/sdks/locations/README.md#get_v1_locations_location_uuid_minimum_wages) - Get minimum wages for a location

### [notifications](docs/sdks/notifications/README.md)

* [get_notifications_notification_uuid](docs/sdks/notifications/README.md#get_notifications_notification_uuid) - Get a notification's details

### [pay_schedules](docs/sdks/payschedules/README.md)

* [post_v1_companies_company_id_pay_schedules](docs/sdks/payschedules/README.md#post_v1_companies_company_id_pay_schedules) - Create a new pay schedule
* [list](docs/sdks/payschedules/README.md#list) - Get the pay schedules for a company
* [get_v1_companies_company_id_pay_schedules_preview](docs/sdks/payschedules/README.md#get_v1_companies_company_id_pay_schedules_preview) - Preview pay schedule dates
* [get_v1_companies_company_id_pay_schedules_pay_schedule_id](docs/sdks/payschedules/README.md#get_v1_companies_company_id_pay_schedules_pay_schedule_id) - Get a pay schedule
* [put_v1_companies_company_id_pay_schedules_pay_schedule_id](docs/sdks/payschedules/README.md#put_v1_companies_company_id_pay_schedules_pay_schedule_id) - Update a pay schedule
* [list_pay_periods](docs/sdks/payschedules/README.md#list_pay_periods) - Get pay periods for a company
* [get_v1_companies_company_id_unprocessed_termination_pay_periods](docs/sdks/payschedules/README.md#get_v1_companies_company_id_unprocessed_termination_pay_periods) - Get termination pay periods for a company
* [get_v1_companies_company_id_pay_schedules_assignments](docs/sdks/payschedules/README.md#get_v1_companies_company_id_pay_schedules_assignments) - Get pay schedule assignments for a company
* [post_v1_companies_company_id_pay_schedules_assignment_preview](docs/sdks/payschedules/README.md#post_v1_companies_company_id_pay_schedules_assignment_preview) - Preview pay schedule assignments for a company
* [post_v1_companies_company_id_pay_schedules_assign](docs/sdks/payschedules/README.md#post_v1_companies_company_id_pay_schedules_assign) - Assign pay schedules for a company

### [pay_stubs](docs/sdks/paystubs/README.md)

* [get](docs/sdks/paystubs/README.md#get) - Get an employee's pay stubs

### [payment_configs](docs/sdks/paymentconfigssdk/README.md)

* [get_v1_company_payment_configs](docs/sdks/paymentconfigssdk/README.md#get_v1_company_payment_configs) - Get a company's payment configs
* [put_v1_company_payment_configs](docs/sdks/paymentconfigssdk/README.md#put_v1_company_payment_configs) - Update a company's payment configs

### [payrolls](docs/sdks/payrolls/README.md)

* [post_v1_companies_company_id_payrolls](docs/sdks/payrolls/README.md#post_v1_companies_company_id_payrolls) - Create an off-cycle payroll
* [get_v1_companies_company_id_payrolls](docs/sdks/payrolls/README.md#get_v1_companies_company_id_payrolls) - Get all payrolls for a company
* [get_v1_companies_company_id_payroll_reversals](docs/sdks/payrolls/README.md#get_v1_companies_company_id_payroll_reversals) - Get approved payroll reversals
* [get_v1_companies_company_id_payrolls_payroll_id](docs/sdks/payrolls/README.md#get_v1_companies_company_id_payrolls_payroll_id) - Get a single payroll
* [put_v1_companies_company_id_payrolls](docs/sdks/payrolls/README.md#put_v1_companies_company_id_payrolls) - Update a payroll by ID
* [delete_v1_companies_company_id_payrolls](docs/sdks/payrolls/README.md#delete_v1_companies_company_id_payrolls) - Delete a payroll
* [put_v1_companies_company_id_payrolls_payroll_id_prepare](docs/sdks/payrolls/README.md#put_v1_companies_company_id_payrolls_payroll_id_prepare) - Prepare a payroll for update
* [get_v1_payment_receipts_payrolls_payroll_uuid](docs/sdks/payrolls/README.md#get_v1_payment_receipts_payrolls_payroll_uuid) - Get a single payroll receipt
* [list_blockers](docs/sdks/payrolls/README.md#list_blockers) - Get all payroll blockers for a company
* [post_companies_payroll_skip_company_uuid](docs/sdks/payrolls/README.md#post_companies_payroll_skip_company_uuid) - Skip a payroll
* [post_payrolls_gross_up_payroll_uuid](docs/sdks/payrolls/README.md#post_payrolls_gross_up_payroll_uuid) - Calculate gross up
* [put_v1_companies_company_id_payrolls_payroll_id_calculate](docs/sdks/payrolls/README.md#put_v1_companies_company_id_payrolls_payroll_id_calculate) - Calculate a payroll
* [put_v1_companies_company_id_payrolls_payroll_id_submit](docs/sdks/payrolls/README.md#put_v1_companies_company_id_payrolls_payroll_id_submit) - Submit payroll
* [put_api_v1_companies_company_id_payrolls_payroll_id_cancel](docs/sdks/payrolls/README.md#put_api_v1_companies_company_id_payrolls_payroll_id_cancel) - Cancel a payroll
* [get_v1_payrolls_payroll_uuid_employees_employee_uuid_pay_stub](docs/sdks/payrolls/README.md#get_v1_payrolls_payroll_uuid_employees_employee_uuid_pay_stub) - Get an employee pay stub (pdf)

### [payrolls_documents](docs/sdks/payrollsdocuments/README.md)

* [post_v1_payrolls_payroll_uuid_generated_documents_printable_payroll_checks](docs/sdks/payrollsdocuments/README.md#post_v1_payrolls_payroll_uuid_generated_documents_printable_payroll_checks) - Generate printable payroll checks (pdf)

### [recovery_cases](docs/sdks/recoverycases/README.md)

* [get_recovery_cases](docs/sdks/recoverycases/README.md#get_recovery_cases) - Get all recovery cases for a company
* [redebit_recovery_case](docs/sdks/recoverycases/README.md#redebit_recovery_case) - Initiate a redebit for a recovery case

### [report_templates](docs/sdks/reporttemplates/README.md)

* [get](docs/sdks/reporttemplates/README.md#get) - Get a report template

### [reports](docs/sdks/reports/README.md)

* [post_companies_company_uuid_reports](docs/sdks/reports/README.md#post_companies_company_uuid_reports) - Create a custom report
* [get_reports_report_uuid](docs/sdks/reports/README.md#get_reports_report_uuid) - Get a report

### [signatories](docs/sdks/signatories/README.md)

* [post_v1_company_signatories](docs/sdks/signatories/README.md#post_v1_company_signatories) - Create a signatory
* [get_v1_companies_company_uuid_signatories](docs/sdks/signatories/README.md#get_v1_companies_company_uuid_signatories) - Get all company signatories
* [post_v1_companies_company_uuid_signatories_invite](docs/sdks/signatories/README.md#post_v1_companies_company_uuid_signatories_invite) - Invite a signatory
* [put_v1_companies_company_uuid_signatories_signatory_uuid](docs/sdks/signatories/README.md#put_v1_companies_company_uuid_signatories_signatory_uuid) - Update a signatory
* [delete_v1_companies_company_uuid_signatories_signatory_uuid](docs/sdks/signatories/README.md#delete_v1_companies_company_uuid_signatories_signatory_uuid) - Delete a signatory

### [tax_requirements](docs/sdks/taxrequirements/README.md)

* [get_state_requirements](docs/sdks/taxrequirements/README.md#get_state_requirements) - Get State Tax Requirements
* [put_v1_companies_company_uuid_tax_requirements_state](docs/sdks/taxrequirements/README.md#put_v1_companies_company_uuid_tax_requirements_state) - Update State Tax Requirements
* [get_v1_companies_company_uuid_tax_requirements](docs/sdks/taxrequirements/README.md#get_v1_companies_company_uuid_tax_requirements) - Get All Tax Requirement States

### [terminations](docs/sdks/terminations/README.md)

* [delete](docs/sdks/terminations/README.md#delete) - Delete an employee termination

### [time_off_policies](docs/sdks/timeoffpolicies/README.md)

* [get](docs/sdks/timeoffpolicies/README.md#get) - Get a time off policy
* [put_time_off_policies_time_off_policy_uuid](docs/sdks/timeoffpolicies/README.md#put_time_off_policies_time_off_policy_uuid) - Update a time off policy
* [list](docs/sdks/timeoffpolicies/README.md#list) - Get all time off policies
* [post_companies_company_uuid_time_off_policies](docs/sdks/timeoffpolicies/README.md#post_companies_company_uuid_time_off_policies) - Create a time off policy
* [put_version_time_off_policies_time_off_policy_uuid_add_employees](docs/sdks/timeoffpolicies/README.md#put_version_time_off_policies_time_off_policy_uuid_add_employees) - Add employees to a time off policy
* [put_v1_time_off_policies_time_off_policy_uuid_remove_employees](docs/sdks/timeoffpolicies/README.md#put_v1_time_off_policies_time_off_policy_uuid_remove_employees) - Remove employees from a time off policy
* [put_version_time_off_policies_time_off_policy_uuid_balance](docs/sdks/timeoffpolicies/README.md#put_version_time_off_policies_time_off_policy_uuid_balance) - Update employee time off hour balances
* [put_v1_time_off_policies_time_off_policy_uuid_deactivate](docs/sdks/timeoffpolicies/README.md#put_v1_time_off_policies_time_off_policy_uuid_deactivate) - Deactivate a time off policy

### [webhook_subscriptions](docs/sdks/webhooksubscriptions/README.md)

* [delete_v1_webhook_subscription_uuid](docs/sdks/webhooksubscriptions/README.md#delete_v1_webhook_subscription_uuid) - Delete a webhook subscription
* [get_v1_webhook_subscription_verification_token_uuid](docs/sdks/webhooksubscriptions/README.md#get_v1_webhook_subscription_verification_token_uuid) - Request the webhook subscription verification_token

### [webhooks](docs/sdks/webhooks/README.md)

* [create](docs/sdks/webhooks/README.md#create) - Create a webhook subscription
* [list](docs/sdks/webhooks/README.md#list) - List webhook subscriptions
* [update](docs/sdks/webhooks/README.md#update) - Update a webhook subscription
* [get_v1_webhook_subscription_uuid](docs/sdks/webhooks/README.md#get_v1_webhook_subscription_uuid) - Get a webhook subscription
* [verify](docs/sdks/webhooks/README.md#verify) - Verify the webhook subscription

### [wire_in_requests](docs/sdks/wireinrequests/README.md)

* [get_wire_in_requests_wire_in_request_uuid](docs/sdks/wireinrequests/README.md#get_wire_in_requests_wire_in_request_uuid) - Get a single Wire In Request
* [submit](docs/sdks/wireinrequests/README.md#submit) - Submit a wire in request
* [list](docs/sdks/wireinrequests/README.md#list) - Get all Wire In Requests for a company

### [work_addresses](docs/sdks/workaddresses/README.md)

* [post_v1_employees_employee_id_work_addresses](docs/sdks/workaddresses/README.md#post_v1_employees_employee_id_work_addresses) - Create an employee work address
* [get](docs/sdks/workaddresses/README.md#get) - Get an employee work address
* [delete_v1_work_addresses_work_address_uuid](docs/sdks/workaddresses/README.md#delete_v1_work_addresses_work_address_uuid) - Delete an employee's work address

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
import gusto
from gusto import Gusto
import os

with Gusto(
    company_access_auth=os.getenv("GUSTO_COMPANY_ACCESS_AUTH", ""),
) as g_client:

    res = g_client.company_attachment.post_v1_companies_attachment(company_id="<id>", document={
        "file_name": "example.file",
        "content": open("example.file", "rb"),
    }, category=gusto.PostV1CompaniesAttachmentCategory.GEP_NOTICE)

    # Handle response
    print(res)

```
<!-- End File uploads [file-upload] -->

<!-- Start Retries [retries] -->
## Retries

Some of the endpoints in this SDK support retries. If you use the SDK without any configuration, it will fall back to the default retry strategy provided by the API. However, the default retry strategy can be overridden on a per-operation basis, or across the entire SDK.

To change the default retry strategy for a single API call, simply provide a `RetryConfig` object to the call:
```python
from gusto import Gusto
from gusto.utils import BackoffStrategy, RetryConfig
import os

with Gusto(
    company_access_auth=os.getenv("GUSTO_COMPANY_ACCESS_AUTH", ""),
) as g_client:

    res = g_client.introspection.get_v1_token_info(,
        RetryConfig("backoff", BackoffStrategy(1, 50, 1.1, 100), False))

    # Handle response
    print(res)

```

If you'd like to override the default retry strategy for all operations that support retries, you can use the `retry_config` optional parameter when initializing the SDK:
```python
from gusto import Gusto
from gusto.utils import BackoffStrategy, RetryConfig
import os

with Gusto(
    retry_config=RetryConfig("backoff", BackoffStrategy(1, 50, 1.1, 100), False),
    company_access_auth=os.getenv("GUSTO_COMPANY_ACCESS_AUTH", ""),
) as g_client:

    res = g_client.introspection.get_v1_token_info()

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

When custom error responses are specified for an operation, the SDK may also raise their associated exceptions. You can refer to respective *Errors* tables in SDK docs for more details on possible exception types for each operation. For example, the `post_v1_partner_managed_companies_async` method may raise the following exceptions:

| Error Type                            | Status Code | Content Type     |
| ------------------------------------- | ----------- | ---------------- |
| models.UnprocessableEntityErrorObject | 422         | application/json |
| models.APIError                       | 4XX, 5XX    | \*/\*            |

### Example

```python
import gusto
from gusto import Gusto, models
import os

with Gusto() as g_client:
    res = None
    try:

        res = g_client.companies.post_v1_partner_managed_companies(security=gusto.PostV1PartnerManagedCompaniesSecurity(
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

| Name   | Server                       |
| ------ | ---------------------------- |
| `demo` | `https://api.gusto-demo.com` |
| `prod` | `https://api.gusto.com`      |

#### Example

```python
from gusto import Gusto
import os

with Gusto(
    server="prod",
    company_access_auth=os.getenv("GUSTO_COMPANY_ACCESS_AUTH", ""),
) as g_client:

    res = g_client.introspection.get_v1_token_info()

    # Handle response
    print(res)

```

### Override Server URL Per-Client

The default server can also be overridden globally by passing a URL to the `server_url: str` optional parameter when initializing the SDK client instance. For example:
```python
from gusto import Gusto
import os

with Gusto(
    server_url="https://api.gusto-demo.com",
    company_access_auth=os.getenv("GUSTO_COMPANY_ACCESS_AUTH", ""),
) as g_client:

    res = g_client.introspection.get_v1_token_info()

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
from gusto import Gusto
import httpx

http_client = httpx.Client(headers={"x-custom-header": "someValue"})
s = Gusto(client=http_client)
```

or you could wrap the client with your own custom logic:
```python
from gusto import Gusto
from gusto.httpclient import AsyncHttpClient
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
from gusto import Gusto
import os
def main():
    with Gusto(
        company_access_auth=os.getenv("GUSTO_COMPANY_ACCESS_AUTH", ""),
    ) as g_client:
        # Rest of application here...


# Or when using async:
async def amain():
    async with Gusto(
        company_access_auth=os.getenv("GUSTO_COMPANY_ACCESS_AUTH", ""),
    ) as g_client:
        # Rest of application here...
```
<!-- End Resource Management [resource-management] -->

<!-- Start Debugging [debug] -->
## Debugging

You can setup your SDK to emit debug logs for SDK requests and responses.

You can pass your own logger class directly into your SDK.
```python
from gusto import Gusto
import logging

logging.basicConfig(level=logging.DEBUG)
s = Gusto(debug_logger=logging.getLogger("gusto"))
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
