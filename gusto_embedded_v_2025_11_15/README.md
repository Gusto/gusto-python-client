# gusto_embedded_v_2025_11_15

Developer-friendly & type-safe Python SDK specifically catered to leverage *gusto_embedded_v_2025_11_15* API.

[![Built by Speakeasy](https://img.shields.io/badge/Built_by-SPEAKEASY-374151?style=for-the-badge&labelColor=f3f4f6)](https://www.speakeasy.com/?utm_source=gusto-embedded-v-2025-11-15&utm_campaign=python)
[![License: MIT](https://img.shields.io/badge/LICENSE_//_MIT-3b5bdb?style=for-the-badge&labelColor=eff6ff)](https://opensource.org/licenses/MIT)


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
* [gusto_embedded_v_2025_11_15](#gustoembeddedv20251115)
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

> [!NOTE]
> **Python version upgrade policy**
>
> Once a Python version reaches its [official end of life date](https://devguide.python.org/versions/), a 3-month grace period is provided for users to upgrade. Following this grace period, the minimum python version supported in the SDK will be updated.

The SDK can be installed with *uv*, *pip*, or *poetry* package managers.

### uv

*uv* is a fast Python package installer and resolver, designed as a drop-in replacement for pip and pip-tools. It's recommended for its speed and modern Python tooling capabilities.

```bash
uv add gusto_embedded_v_2025_11_15
```

### PIP

*PIP* is the default package installer for Python, enabling easy installation and management of packages from PyPI via the command line.

```bash
pip install gusto_embedded_v_2025_11_15
```

### Poetry

*Poetry* is a modern tool that simplifies dependency management and package publishing by using a single `pyproject.toml` file to handle project metadata and dependencies.

```bash
poetry add gusto_embedded_v_2025_11_15
```

### Shell and script usage with `uv`

You can use this SDK in a Python shell with [uv](https://docs.astral.sh/uv/) and the `uvx` command that comes with it like so:

```shell
uvx --from gusto_embedded_v_2025_11_15 python
```

It's also possible to write a standalone Python script without needing to set up a whole project like so:

```python
#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.10"
# dependencies = [
#     "gusto_embedded_v_2025_11_15",
# ]
# ///

from gusto_embedded_v_2025_11_15 import Gusto

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
import gusto_embedded_v_2025_11_15
from gusto_embedded_v_2025_11_15 import Gusto
import os


with Gusto(
    company_access_auth=os.getenv("GUSTO_COMPANY_ACCESS_AUTH", ""),
) as gusto:

    res = gusto.introspection.get_info(x_gusto_api_version=gusto_embedded_v_2025_11_15.XGustoAPIVersion.TWO_THOUSAND_AND_TWENTY_FIVE_MINUS_11_MINUS_15)

    # Handle response
    print(res)
```

</br>

The same SDK client can also be used to make asynchronous requests by importing asyncio.

```python
# Asynchronous Example
import asyncio
import gusto_embedded_v_2025_11_15
from gusto_embedded_v_2025_11_15 import Gusto
import os

async def main():

    async with Gusto(
        company_access_auth=os.getenv("GUSTO_COMPANY_ACCESS_AUTH", ""),
    ) as gusto:

        res = await gusto.introspection.get_info_async(x_gusto_api_version=gusto_embedded_v_2025_11_15.XGustoAPIVersion.TWO_THOUSAND_AND_TWENTY_FIVE_MINUS_11_MINUS_15)

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
import gusto_embedded_v_2025_11_15
from gusto_embedded_v_2025_11_15 import Gusto
import os


with Gusto(
    company_access_auth=os.getenv("GUSTO_COMPANY_ACCESS_AUTH", ""),
) as gusto:

    res = gusto.introspection.get_info(x_gusto_api_version=gusto_embedded_v_2025_11_15.XGustoAPIVersion.TWO_THOUSAND_AND_TWENTY_FIVE_MINUS_11_MINUS_15)

    # Handle response
    print(res)

```

### Per-Operation Security Schemes

Some operations in this SDK require the security scheme to be specified at the request level. For example:
```python
import gusto_embedded_v_2025_11_15
from gusto_embedded_v_2025_11_15 import Gusto
import os


with Gusto() as gusto:

    res = gusto.companies.create_partner_managed(security=gusto_embedded_v_2025_11_15.PostV1PartnerManagedCompaniesSecurity(
        system_access_auth=os.getenv("GUSTO_SYSTEM_ACCESS_AUTH", ""),
    ), user={
        "first_name": "Marco",
        "last_name": "Trantow",
        "email": "Jewell_Greenholt72@hotmail.com",
    }, company={
        "name": "<value>",
    }, x_gusto_api_version=gusto_embedded_v_2025_11_15.PostV1PartnerManagedCompaniesHeaderXGustoAPIVersion.TWO_THOUSAND_AND_TWENTY_FIVE_MINUS_11_MINUS_15)

    # Handle response
    print(res)

```
<!-- End Authentication [security] -->

<!-- Start Available Resources and Operations [operations] -->
## Available Resources and Operations

<details open>
<summary>Available methods</summary>

### [AchTransactions](docs/sdks/achtransactions/README.md)

* [get_all](docs/sdks/achtransactions/README.md#get_all) - Get all ACH transactions for a company

### [BankAccounts](docs/sdks/bankaccounts/README.md)

* [get](docs/sdks/bankaccounts/README.md#get) - Get all company bank accounts
* [create](docs/sdks/bankaccounts/README.md#create) - Create a company bank account
* [verify](docs/sdks/bankaccounts/README.md#verify) - Verify a company bank account
* [create_from_plaid_token](docs/sdks/bankaccounts/README.md#create_from_plaid_token) - Create a bank account from a plaid processor token
* [delete_v1_companies_company_id_bank_accounts_bank_account_id](docs/sdks/bankaccounts/README.md#delete_v1_companies_company_id_bank_accounts_bank_account_id) - Delete a company bank account

### [Companies](docs/sdks/companies/README.md)

* [create_partner_managed](docs/sdks/companies/README.md#create_partner_managed) - Create a partner managed company
* [get](docs/sdks/companies/README.md#get) - Get a company
* [update](docs/sdks/companies/README.md#update) - Update a company
* [migrate](docs/sdks/companies/README.md#migrate) - Migrate company to embedded payroll
* [get_v1_partner_managed_companies_company_uuid_migration_readiness](docs/sdks/companies/README.md#get_v1_partner_managed_companies_company_uuid_migration_readiness) - Check company migration readiness
* [accept_terms_of_service](docs/sdks/companies/README.md#accept_terms_of_service) - Accept terms of service for a company user
* [retrieve_terms_of_service](docs/sdks/companies/README.md#retrieve_terms_of_service) - Retrieve terms of service status for a company user
* [list_admins](docs/sdks/companies/README.md#list_admins) - Get all the admins at a company
* [create_admin](docs/sdks/companies/README.md#create_admin) - Create an admin for the company
* [get_onboarding_status](docs/sdks/companies/README.md#get_onboarding_status) - Get company onboarding status
* [finish_onboarding](docs/sdks/companies/README.md#finish_onboarding) - Finish company onboarding
* [get_custom_fields](docs/sdks/companies/README.md#get_custom_fields) - Get the custom fields of a company

### [Companies.Suspensions](docs/sdks/suspensions/README.md)

* [get](docs/sdks/suspensions/README.md#get) - Get suspensions for this company
* [suspend](docs/sdks/suspensions/README.md#suspend) - Suspend a company's account

### [CompanyAttachment](docs/sdks/companyattachmentsdk/README.md)

* [get_download_url](docs/sdks/companyattachmentsdk/README.md#get_download_url) - Get a temporary url to download the Company Attachment file

### [CompanyAttachments](docs/sdks/companyattachments/README.md)

* [get_details](docs/sdks/companyattachments/README.md#get_details) - Get Company Attachment Details
* [get_list](docs/sdks/companyattachments/README.md#get_list) - Get List of Company Attachments
* [create](docs/sdks/companyattachments/README.md#create) - Create Company Attachment and Upload File

### [CompanyBenefits](docs/sdks/companybenefits/README.md)

* [list](docs/sdks/companybenefits/README.md#list) - Get benefits for a company
* [create](docs/sdks/companybenefits/README.md#create) - Create a company benefit
* [get](docs/sdks/companybenefits/README.md#get) - Get a company benefit
* [update](docs/sdks/companybenefits/README.md#update) - Update a company benefit
* [delete](docs/sdks/companybenefits/README.md#delete) - Delete a company benefit
* [get_all](docs/sdks/companybenefits/README.md#get_all) - Get all supported benefits
* [get_supported](docs/sdks/companybenefits/README.md#get_supported) - Get a supported benefit
* [get_summary](docs/sdks/companybenefits/README.md#get_summary) - Get company benefit summary by company benefit id.
* [get_employee_benefits](docs/sdks/companybenefits/README.md#get_employee_benefits) - Get all employee benefits for a company benefit
* [update_employee_benefits](docs/sdks/companybenefits/README.md#update_employee_benefits) - Bulk update employee benefits for a company benefit
* [get_requirements](docs/sdks/companybenefits/README.md#get_requirements) - Get benefit fields requirements by benefit type
* [get_v1_company_benefits_company_benefit_id_contribution_exclusions](docs/sdks/companybenefits/README.md#get_v1_company_benefits_company_benefit_id_contribution_exclusions) - Get contribution exclusions for a company benefit
* [put_v1_company_benefits_company_benefit_id_contribution_exclusions](docs/sdks/companybenefits/README.md#put_v1_company_benefits_company_benefit_id_contribution_exclusions) - Update contribution exclusions for a company benefit

### [CompanyForms](docs/sdks/companyforms/README.md)

* [get_all](docs/sdks/companyforms/README.md#get_all) - Get all company forms
* [get](docs/sdks/companyforms/README.md#get) - Get a company form
* [get_pdf](docs/sdks/companyforms/README.md#get_pdf) - Get a company form pdf
* [sign](docs/sdks/companyforms/README.md#sign) - Sign a company form

### [ContractorDocuments](docs/sdks/contractordocuments/README.md)

* [get_all](docs/sdks/contractordocuments/README.md#get_all) - Get all contractor documents
* [get](docs/sdks/contractordocuments/README.md#get) - Get a contractor document
* [get_pdf](docs/sdks/contractordocuments/README.md#get_pdf) - Get the contractor document pdf
* [sign](docs/sdks/contractordocuments/README.md#sign) - Sign a contractor document

### [ContractorForms](docs/sdks/contractorforms/README.md)

* [list](docs/sdks/contractorforms/README.md#list) - Get all contractor forms
* [get](docs/sdks/contractorforms/README.md#get) - Get a contractor form
* [get_pdf](docs/sdks/contractorforms/README.md#get_pdf) - Get the contractor form pdf
* [generate1099](docs/sdks/contractorforms/README.md#generate1099) - Generate a 1099 form [DEMO]

### [ContractorPaymentGroups](docs/sdks/contractorpaymentgroups/README.md)

* [get_list](docs/sdks/contractorpaymentgroups/README.md#get_list) - Get contractor payment groups for a company
* [create](docs/sdks/contractorpaymentgroups/README.md#create) - Create a contractor payment group
* [preview](docs/sdks/contractorpaymentgroups/README.md#preview) - Preview a contractor payment group
* [get](docs/sdks/contractorpaymentgroups/README.md#get) - Get a contractor payment group
* [delete](docs/sdks/contractorpaymentgroups/README.md#delete) - Cancel a contractor payment group
* [fund](docs/sdks/contractorpaymentgroups/README.md#fund) - Fund a contractor payment group [DEMO]
* [get_v1_contractor_payment_groups_id_partner_disbursements](docs/sdks/contractorpaymentgroups/README.md#get_v1_contractor_payment_groups_id_partner_disbursements) - Get partner disbursements for a contractor payment group
* [patch_v1_contractor_payment_groups_id_partner_disbursements](docs/sdks/contractorpaymentgroups/README.md#patch_v1_contractor_payment_groups_id_partner_disbursements) - Update partner disbursements for a contractor payment group

### [ContractorPaymentMethod](docs/sdks/contractorpaymentmethodsdk/README.md)

* [get_bank_accounts](docs/sdks/contractorpaymentmethodsdk/README.md#get_bank_accounts) - Get all contractor bank accounts
* [get](docs/sdks/contractorpaymentmethodsdk/README.md#get) - Get a contractor's payment method
* [update](docs/sdks/contractorpaymentmethodsdk/README.md#update) - Update a contractor's payment method

### [ContractorPaymentMethods](docs/sdks/contractorpaymentmethods/README.md)

* [create_bank_account](docs/sdks/contractorpaymentmethods/README.md#create_bank_account) - Create a contractor bank account

### [ContractorPayments](docs/sdks/contractorpayments/README.md)

* [get_receipt](docs/sdks/contractorpayments/README.md#get_receipt) - Get a single contractor payment receipt
* [fund](docs/sdks/contractorpayments/README.md#fund) - Fund a contractor payment [DEMO]
* [list](docs/sdks/contractorpayments/README.md#list) - Get contractor payments for a company
* [create](docs/sdks/contractorpayments/README.md#create) - Create a contractor payment
* [get](docs/sdks/contractorpayments/README.md#get) - Get a single contractor payment
* [delete](docs/sdks/contractorpayments/README.md#delete) - Cancel a contractor payment
* [preview](docs/sdks/contractorpayments/README.md#preview) - Preview contractor payment debit date
* [get_v1_contractor_payments_contractor_payment_id_pdf](docs/sdks/contractorpayments/README.md#get_v1_contractor_payments_contractor_payment_id_pdf) - Get a contractor payment PDF

### [Contractors](docs/sdks/contractors/README.md)

* [list](docs/sdks/contractors/README.md#list) - Get contractors of a company
* [create](docs/sdks/contractors/README.md#create) - Create a contractor
* [get](docs/sdks/contractors/README.md#get) - Get a contractor
* [update](docs/sdks/contractors/README.md#update) - Update a contractor
* [delete](docs/sdks/contractors/README.md#delete) - Delete a contractor
* [get_onboarding_status](docs/sdks/contractors/README.md#get_onboarding_status) - Get the contractor's onboarding status
* [update_onboarding_status](docs/sdks/contractors/README.md#update_onboarding_status) - Change the contractor's onboarding status
* [get_address](docs/sdks/contractors/README.md#get_address) - Get a contractor address
* [update_address](docs/sdks/contractors/README.md#update_address) - Create or update a contractor's address
* [get_v1_companies_company_id_contractors_payment_details](docs/sdks/contractors/README.md#get_v1_companies_company_id_contractors_payment_details) - List contractor payment details
* [post_v1_contractors_contractor_uuid_rehire](docs/sdks/contractors/README.md#post_v1_contractors_contractor_uuid_rehire) - Schedule a contractor rehire
* [delete_v1_contractors_contractor_uuid_rehire](docs/sdks/contractors/README.md#delete_v1_contractors_contractor_uuid_rehire) - Cancel a pending contractor rehire
* [post_v1_contractors_contractor_uuid_termination](docs/sdks/contractors/README.md#post_v1_contractors_contractor_uuid_termination) - Schedule a contractor termination
* [delete_v1_contractors_contractor_uuid_termination](docs/sdks/contractors/README.md#delete_v1_contractors_contractor_uuid_termination) - Cancel a pending contractor termination

### [Departments](docs/sdks/departments/README.md)

* [get_all](docs/sdks/departments/README.md#get_all) - Get all departments of a company
* [create](docs/sdks/departments/README.md#create) - Create a department
* [get](docs/sdks/departments/README.md#get) - Get a department
* [update](docs/sdks/departments/README.md#update) - Update a department
* [delete](docs/sdks/departments/README.md#delete) - Delete a department
* [add_people](docs/sdks/departments/README.md#add_people) - Add people to a department
* [remove_people](docs/sdks/departments/README.md#remove_people) - Remove people from a department

### [EarningTypes](docs/sdks/earningtypes/README.md)

* [list](docs/sdks/earningtypes/README.md#list) - Get all earning types for a company
* [create](docs/sdks/earningtypes/README.md#create) - Create a custom earning type
* [update](docs/sdks/earningtypes/README.md#update) - Update an earning type
* [delete](docs/sdks/earningtypes/README.md#delete) - Deactivate an earning type

### [EmployeeAddresses](docs/sdks/employeeaddresses/README.md)

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

### [EmployeeBenefits](docs/sdks/employeebenefits/README.md)

* [get](docs/sdks/employeebenefits/README.md#get) - Get all benefits for an employee
* [create](docs/sdks/employeebenefits/README.md#create) - Create an employee benefit
* [retrieve](docs/sdks/employeebenefits/README.md#retrieve) - Get an employee benefit
* [update](docs/sdks/employeebenefits/README.md#update) - Update an employee benefit
* [delete](docs/sdks/employeebenefits/README.md#delete) - Delete an employee benefit
* [get_ytd_benefit_amounts_from_different_company](docs/sdks/employeebenefits/README.md#get_ytd_benefit_amounts_from_different_company) - Get year-to-date benefit amounts from a different company
* [create_ytd_benefit_amounts_from_different_company](docs/sdks/employeebenefits/README.md#create_ytd_benefit_amounts_from_different_company) - Create year-to-date benefit amounts from a different company
* [get_v1_employees_employee_uuid_section603_high_earner_statuses](docs/sdks/employeebenefits/README.md#get_v1_employees_employee_uuid_section603_high_earner_statuses) - Get all Section 603 high earner statuses for an employee
* [post_v1_employees_employee_uuid_section603_high_earner_statuses](docs/sdks/employeebenefits/README.md#post_v1_employees_employee_uuid_section603_high_earner_statuses) - Create a Section 603 high earner status
* [get_v1_employees_employee_uuid_section603_high_earner_statuses_effective_year](docs/sdks/employeebenefits/README.md#get_v1_employees_employee_uuid_section603_high_earner_statuses_effective_year) - Get a Section 603 high earner status for a specific year
* [patch_v1_employees_employee_uuid_section603_high_earner_statuses_effective_year](docs/sdks/employeebenefits/README.md#patch_v1_employees_employee_uuid_section603_high_earner_statuses_effective_year) - Update a Section 603 high earner status

### [EmployeeEmployments](docs/sdks/employeeemployments/README.md)

* [get_terminations](docs/sdks/employeeemployments/README.md#get_terminations) - Get terminations for an employee
* [create_termination](docs/sdks/employeeemployments/README.md#create_termination) - Create an employee termination
* [delete_termination](docs/sdks/employeeemployments/README.md#delete_termination) - Delete an employee termination
* [update_termination](docs/sdks/employeeemployments/README.md#update_termination) - Update an employee termination
* [get_rehire](docs/sdks/employeeemployments/README.md#get_rehire) - Get an employee rehire
* [create_rehire](docs/sdks/employeeemployments/README.md#create_rehire) - Create an employee rehire
* [rehire](docs/sdks/employeeemployments/README.md#rehire) - Update an employee rehire
* [delete_rehire](docs/sdks/employeeemployments/README.md#delete_rehire) - Delete an employee rehire
* [get_history](docs/sdks/employeeemployments/README.md#get_history) - Get employment history for an employee
* [get_v1_terminations_employee_id](docs/sdks/employeeemployments/README.md#get_v1_terminations_employee_id) - Get an employee termination

### [EmployeeForms](docs/sdks/employeeforms/README.md)

* [generate_w2](docs/sdks/employeeforms/README.md#generate_w2) - Generate a W2 form [DEMO]
* [list](docs/sdks/employeeforms/README.md#list) - Get all employee forms
* [get](docs/sdks/employeeforms/README.md#get) - Get an employee form
* [get_pdf](docs/sdks/employeeforms/README.md#get_pdf) - Get the employee form pdf
* [sign](docs/sdks/employeeforms/README.md#sign) - Sign an employee form

### [EmployeePaymentMethod](docs/sdks/employeepaymentmethodsdk/README.md)

* [create](docs/sdks/employeepaymentmethodsdk/README.md#create) - Create an employee bank account
* [update_bank_account](docs/sdks/employeepaymentmethodsdk/README.md#update_bank_account) - Update an employee bank account
* [delete_bank_account](docs/sdks/employeepaymentmethodsdk/README.md#delete_bank_account) - Delete an employee bank account
* [get](docs/sdks/employeepaymentmethodsdk/README.md#get) - Get payment method for an employee
* [update](docs/sdks/employeepaymentmethodsdk/README.md#update) - Update payment method for an employee

### [EmployeePaymentMethods](docs/sdks/employeepaymentmethods/README.md)

* [get_bank_accounts](docs/sdks/employeepaymentmethods/README.md#get_bank_accounts) - List employee bank accounts

### [Employees](docs/sdks/employees/README.md)

* [list](docs/sdks/employees/README.md#list) - Get employees of a company
* [create](docs/sdks/employees/README.md#create) - Create an employee
* [get_v1_companies_company_id_employees_payment_details](docs/sdks/employees/README.md#get_v1_companies_company_id_employees_payment_details) - Get employee payment details for a company
* [create_historical](docs/sdks/employees/README.md#create_historical) - Create a historical employee
* [get](docs/sdks/employees/README.md#get) - Get an employee
* [update](docs/sdks/employees/README.md#update) - Update an employee.
* [delete](docs/sdks/employees/README.md#delete) - Delete an onboarding employee
* [get_custom_fields](docs/sdks/employees/README.md#get_custom_fields) - Get an employee's custom fields
* [update_onboarding_documents_config](docs/sdks/employees/README.md#update_onboarding_documents_config) - Update employee onboarding documents config
* [get_onboarding_status](docs/sdks/employees/README.md#get_onboarding_status) - Get the employee's onboarding status
* [update_onboarding_status](docs/sdks/employees/README.md#update_onboarding_status) - Update the employee's onboarding status
* [get_time_off_activities](docs/sdks/employees/README.md#get_time_off_activities) - Get employee time off activities

### [EmployeeTaxSetup](docs/sdks/employeetaxsetup/README.md)

* [get_federal_taxes](docs/sdks/employeetaxsetup/README.md#get_federal_taxes) - Get federal taxes for an employee
* [update_federal_taxes](docs/sdks/employeetaxsetup/README.md#update_federal_taxes) - Update federal taxes for an employee
* [get_state_taxes](docs/sdks/employeetaxsetup/README.md#get_state_taxes) - Get an employee's state taxes
* [update_state_taxes](docs/sdks/employeetaxsetup/README.md#update_state_taxes) - Update an employee's state taxes

### [Events](docs/sdks/events/README.md)

* [get](docs/sdks/events/README.md#get) - Get all events

### [ExternalPayrolls](docs/sdks/externalpayrolls/README.md)

* [get](docs/sdks/externalpayrolls/README.md#get) - Get external payrolls for a company
* [create](docs/sdks/externalpayrolls/README.md#create) - Create an external payroll for a company
* [retrieve](docs/sdks/externalpayrolls/README.md#retrieve) - Get an external payroll
* [update](docs/sdks/externalpayrolls/README.md#update) - Update an external payroll
* [delete](docs/sdks/externalpayrolls/README.md#delete) - Delete an external payroll
* [calculate_taxes](docs/sdks/externalpayrolls/README.md#calculate_taxes) - Get tax suggestions for an external payroll
* [list_tax_liabilities](docs/sdks/externalpayrolls/README.md#list_tax_liabilities) - Get tax liabilities
* [update_tax_liabilities](docs/sdks/externalpayrolls/README.md#update_tax_liabilities) - Update tax liabilities
* [finalize_tax_liabilities](docs/sdks/externalpayrolls/README.md#finalize_tax_liabilities) - Finalize tax liabilities options and convert into processed payrolls

### [FederalTaxDetails](docs/sdks/federaltaxdetailssdk/README.md)

* [get](docs/sdks/federaltaxdetailssdk/README.md#get) - Get a company's federal tax details
* [update](docs/sdks/federaltaxdetailssdk/README.md#update) - Update a company's federal tax details

### [Flows](docs/sdks/flows/README.md)

* [create](docs/sdks/flows/README.md#create) - Create a flow

### [Garnishments](docs/sdks/garnishments/README.md)

* [list](docs/sdks/garnishments/README.md#list) - Get garnishments for an employee
* [create](docs/sdks/garnishments/README.md#create) - Create a garnishment
* [get](docs/sdks/garnishments/README.md#get) - Get a garnishment
* [update](docs/sdks/garnishments/README.md#update) - Update a garnishment
* [get_child_support_data](docs/sdks/garnishments/README.md#get_child_support_data) - Get child support garnishment data

### [GeneratedDocuments](docs/sdks/generateddocuments/README.md)

* [get](docs/sdks/generateddocuments/README.md#get) - Get a generated document

### [HistoricalEmployees](docs/sdks/historicalemployees/README.md)

* [update](docs/sdks/historicalemployees/README.md#update) - Update a historical employee

### [HolidayPayPolicies](docs/sdks/holidaypaypolicies/README.md)

* [get](docs/sdks/holidaypaypolicies/README.md#get) - Get a company's holiday pay policy
* [create](docs/sdks/holidaypaypolicies/README.md#create) - Create a holiday pay policy for a company
* [update](docs/sdks/holidaypaypolicies/README.md#update) - Update a company's holiday pay policy
* [delete](docs/sdks/holidaypaypolicies/README.md#delete) - Delete a company's holiday pay policy
* [add_employees](docs/sdks/holidaypaypolicies/README.md#add_employees) - Add employees to a company's holiday pay policy
* [remove_employees](docs/sdks/holidaypaypolicies/README.md#remove_employees) - Remove employees from a company's holiday pay policy
* [preview_paid_holidays](docs/sdks/holidaypaypolicies/README.md#preview_paid_holidays) - Preview a company's paid holidays

### [I9Verification](docs/sdks/i9verification/README.md)

* [get_authorization](docs/sdks/i9verification/README.md#get_authorization) - Get an employee's I-9 authorization
* [update](docs/sdks/i9verification/README.md#update) - Create or update an employee's I-9 authorization
* [get_document_options](docs/sdks/i9verification/README.md#get_document_options) - Get an employee's I-9 verification document options
* [get_documents](docs/sdks/i9verification/README.md#get_documents) - Get an employee's I-9 verification documents
* [create_documents](docs/sdks/i9verification/README.md#create_documents) - Create an employee's I-9 authorization verification documents
* [delete_document](docs/sdks/i9verification/README.md#delete_document) - Delete an employee's I-9 verification document
* [employer_sign](docs/sdks/i9verification/README.md#employer_sign) - Employer sign an employee's Form I-9

### [IndustrySelection](docs/sdks/industryselection/README.md)

* [get](docs/sdks/industryselection/README.md#get) - Get a company industry selection
* [update](docs/sdks/industryselection/README.md#update) - Update a company industry selection

### [InformationRequests](docs/sdks/informationrequests/README.md)

* [get_information_requests](docs/sdks/informationrequests/README.md#get_information_requests) - Get all information requests for a company
* [submit](docs/sdks/informationrequests/README.md#submit) - Submit information request responses

### [Introspection](docs/sdks/introspection/README.md)

* [get_info](docs/sdks/introspection/README.md#get_info) - Get info about the current access token
* [oauth_access_token](docs/sdks/introspection/README.md#oauth_access_token) - Create a System Access Token or Refresh an Access Token

### [Invoices](docs/sdks/invoices/README.md)

* [get](docs/sdks/invoices/README.md#get) - Retrieve invoicing data for companies

### [JobsAndCompensations](docs/sdks/jobsandcompensations/README.md)

* [get_jobs](docs/sdks/jobsandcompensations/README.md#get_jobs) - Get jobs for an employee
* [create_job](docs/sdks/jobsandcompensations/README.md#create_job) - Create a job
* [get_job](docs/sdks/jobsandcompensations/README.md#get_job) - Get a job
* [update](docs/sdks/jobsandcompensations/README.md#update) - Update a job
* [delete](docs/sdks/jobsandcompensations/README.md#delete) - Delete an individual job
* [get_compensations](docs/sdks/jobsandcompensations/README.md#get_compensations) - Get compensations for a job
* [create_compensation](docs/sdks/jobsandcompensations/README.md#create_compensation) - Create a compensation
* [get_compensation](docs/sdks/jobsandcompensations/README.md#get_compensation) - Get a compensation
* [update_compensation](docs/sdks/jobsandcompensations/README.md#update_compensation) - Update a compensation
* [delete_compensation](docs/sdks/jobsandcompensations/README.md#delete_compensation) - Delete a compensation

### [Locations](docs/sdks/locations/README.md)

* [get](docs/sdks/locations/README.md#get) - Get all company locations
* [create](docs/sdks/locations/README.md#create) - Create a company location
* [retrieve](docs/sdks/locations/README.md#retrieve) - Get a location
* [update](docs/sdks/locations/README.md#update) - Update a location
* [get_minimum_wages](docs/sdks/locations/README.md#get_minimum_wages) - Get minimum wages for a location

### [Notifications](docs/sdks/notifications/README.md)

* [get_details](docs/sdks/notifications/README.md#get_details) - Get a notification's details
* [get_company_notifications](docs/sdks/notifications/README.md#get_company_notifications) - Get notifications for company

### [PaymentConfigs](docs/sdks/paymentconfigssdk/README.md)

* [get](docs/sdks/paymentconfigssdk/README.md#get) - Get a company's payment configs
* [update](docs/sdks/paymentconfigssdk/README.md#update) - Update a company's payment configs

### [Payrolls](docs/sdks/payrolls/README.md)

* [list](docs/sdks/payrolls/README.md#list) - Get all payrolls for a company
* [create_off_cycle](docs/sdks/payrolls/README.md#create_off_cycle) - Create an off-cycle payroll
* [get_approved_reversals](docs/sdks/payrolls/README.md#get_approved_reversals) - Get approved payroll reversals
* [get](docs/sdks/payrolls/README.md#get) - Get a single payroll
* [update](docs/sdks/payrolls/README.md#update) - Update a payroll by ID
* [delete](docs/sdks/payrolls/README.md#delete) - Delete a payroll
* [prepare](docs/sdks/payrolls/README.md#prepare) - Prepare a payroll for update
* [get_receipt](docs/sdks/payrolls/README.md#get_receipt) - Get a single payroll receipt
* [get_blockers](docs/sdks/payrolls/README.md#get_blockers) - Get all payroll blockers for a company
* [skip](docs/sdks/payrolls/README.md#skip) - Skip a payroll
* [calculate_gross_up](docs/sdks/payrolls/README.md#calculate_gross_up) - Calculate gross up for a payroll
* [calculate](docs/sdks/payrolls/README.md#calculate) - Calculate a payroll
* [submit](docs/sdks/payrolls/README.md#submit) - Submit payroll
* [cancel](docs/sdks/payrolls/README.md#cancel) - Cancel a payroll
* [get_pay_stub](docs/sdks/payrolls/README.md#get_pay_stub) - Get an employee pay stub (pdf)
* [get_pay_stubs](docs/sdks/payrolls/README.md#get_pay_stubs) - Get an employee's pay stubs
* [generate_printable_checks](docs/sdks/payrolls/README.md#generate_printable_checks) - Generate printable payroll checks (pdf)
* [get_v1_companies_company_id_payrolls_id_partner_disbursements](docs/sdks/payrolls/README.md#get_v1_companies_company_id_payrolls_id_partner_disbursements) - Get partner disbursements for a payroll
* [patch_v1_companies_company_id_payrolls_id_partner_disbursements](docs/sdks/payrolls/README.md#patch_v1_companies_company_id_payrolls_id_partner_disbursements) - Update partner disbursements for a payroll

### [PaySchedules](docs/sdks/payschedules/README.md)

* [get_all](docs/sdks/payschedules/README.md#get_all) - Get the pay schedules for a company
* [create](docs/sdks/payschedules/README.md#create) - Create a new pay schedule
* [get_preview](docs/sdks/payschedules/README.md#get_preview) - Preview pay schedule dates
* [get](docs/sdks/payschedules/README.md#get) - Get a pay schedule
* [update](docs/sdks/payschedules/README.md#update) - Update a pay schedule
* [get_pay_periods](docs/sdks/payschedules/README.md#get_pay_periods) - Get pay periods for a company
* [get_unprocessed_termination_periods](docs/sdks/payschedules/README.md#get_unprocessed_termination_periods) - Get termination pay periods for a company
* [get_assignments](docs/sdks/payschedules/README.md#get_assignments) - Get pay schedule assignments for a company
* [preview_assignment](docs/sdks/payschedules/README.md#preview_assignment) - Preview pay schedule assignments for a company
* [assign](docs/sdks/payschedules/README.md#assign) - Assign pay schedules for a company

### [PeopleBatches](docs/sdks/peoplebatches/README.md)

* [post_v1_companies_company_id_people_batches](docs/sdks/peoplebatches/README.md#post_v1_companies_company_id_people_batches) - Create a people batch
* [get_v1_people_batches_people_batch_uuid](docs/sdks/peoplebatches/README.md#get_v1_people_batches_people_batch_uuid) - Get a people batch

### [RecoveryCases](docs/sdks/recoverycases/README.md)

* [get](docs/sdks/recoverycases/README.md#get) - Get all recovery cases for a company
* [redebit](docs/sdks/recoverycases/README.md#redebit) - Initiate a redebit for a recovery case

### [Reimbursements](docs/sdks/reimbursements/README.md)

* [get_v1_employees_employee_id_recurring_reimbursements](docs/sdks/reimbursements/README.md#get_v1_employees_employee_id_recurring_reimbursements) - Get recurring reimbursements for an employee
* [post_v1_employees_employee_id_recurring_reimbursements](docs/sdks/reimbursements/README.md#post_v1_employees_employee_id_recurring_reimbursements) - Create a recurring reimbursement
* [get_v1_recurring_reimbursements](docs/sdks/reimbursements/README.md#get_v1_recurring_reimbursements) - Get a recurring reimbursement
* [put_v1_recurring_reimbursements](docs/sdks/reimbursements/README.md#put_v1_recurring_reimbursements) - Update a recurring reimbursement
* [delete_v1_recurring_reimbursements](docs/sdks/reimbursements/README.md#delete_v1_recurring_reimbursements) - Delete a recurring reimbursement

### [Reports](docs/sdks/reports/README.md)

* [create_custom](docs/sdks/reports/README.md#create_custom) - Create a custom report
* [post_payrolls_payroll_uuid_reports_general_ledger](docs/sdks/reports/README.md#post_payrolls_payroll_uuid_reports_general_ledger) - Create a general ledger report
* [get_reports_request_uuid](docs/sdks/reports/README.md#get_reports_request_uuid) - Get a report
* [get_template](docs/sdks/reports/README.md#get_template) - Get a report template
* [post_v1_companies_company_id_reports_employees_annual_fica_wage](docs/sdks/reports/README.md#post_v1_companies_company_id_reports_employees_annual_fica_wage) - Create an employees annual FICA wage report

### [SalaryEstimates](docs/sdks/salaryestimates/README.md)

* [post_v1_employees_employee_id_salary_estimates](docs/sdks/salaryestimates/README.md#post_v1_employees_employee_id_salary_estimates) - Create a salary estimate for an employee
* [get_v1_salary_estimates_id](docs/sdks/salaryestimates/README.md#get_v1_salary_estimates_id) - Get a salary estimate
* [put_v1_salary_estimates_id](docs/sdks/salaryestimates/README.md#put_v1_salary_estimates_id) - Update a salary estimate
* [post_v1_salary_estimates_uuid_accept](docs/sdks/salaryestimates/README.md#post_v1_salary_estimates_uuid_accept) - Accept a salary estimate
* [get_v1_salary_estimates_occupations](docs/sdks/salaryestimates/README.md#get_v1_salary_estimates_occupations) - Search for BLS occupations

### [Signatories](docs/sdks/signatories/README.md)

* [list](docs/sdks/signatories/README.md#list) - Get the signatories for a company
* [create](docs/sdks/signatories/README.md#create) - Create a signatory
* [invite](docs/sdks/signatories/README.md#invite) - Invite a signatory
* [update](docs/sdks/signatories/README.md#update) - Update a signatory
* [delete](docs/sdks/signatories/README.md#delete) - Delete a signatory

### [TaxRequirements](docs/sdks/taxrequirements/README.md)

* [get](docs/sdks/taxrequirements/README.md#get) - Get tax requirements for a state
* [update_state](docs/sdks/taxrequirements/README.md#update_state) - Update tax requirements for a state
* [get_all](docs/sdks/taxrequirements/README.md#get_all) - Get all tax requirements for a company

### [TimeOffRequests](docs/sdks/timeoffrequests/README.md)

* [post_v1_companies_company_uuid_time_off_admin_approved_requests](docs/sdks/timeoffrequests/README.md#post_v1_companies_company_uuid_time_off_admin_approved_requests) - Create an admin-approved time off request
* [get_v1_companies_company_uuid_time_off_balances](docs/sdks/timeoffrequests/README.md#get_v1_companies_company_uuid_time_off_balances) - Get time off balances for a company
* [get_v1_companies_company_uuid_time_off_requests](docs/sdks/timeoffrequests/README.md#get_v1_companies_company_uuid_time_off_requests) - List time off requests for a company
* [post_v1_companies_company_uuid_time_off_requests](docs/sdks/timeoffrequests/README.md#post_v1_companies_company_uuid_time_off_requests) - Create a time off request
* [post_v1_companies_company_uuid_time_off_requests_preview](docs/sdks/timeoffrequests/README.md#post_v1_companies_company_uuid_time_off_requests_preview) - Preview a time off request
* [get_v1_time_off_requests_time_off_request_uuid](docs/sdks/timeoffrequests/README.md#get_v1_time_off_requests_time_off_request_uuid) - Get a time off request
* [delete_v1_time_off_requests_time_off_request_uuid](docs/sdks/timeoffrequests/README.md#delete_v1_time_off_requests_time_off_request_uuid) - Delete a time off request
* [put_v1_time_off_requests_time_off_request_uuid_approve](docs/sdks/timeoffrequests/README.md#put_v1_time_off_requests_time_off_request_uuid_approve) - Approve a time off request
* [put_v1_time_off_requests_time_off_request_uuid_decline](docs/sdks/timeoffrequests/README.md#put_v1_time_off_requests_time_off_request_uuid_decline) - Decline a time off request

### [TimeOffPolicies](docs/sdks/timeoffpolicies/README.md)

* [calculate_accruing_time_off_hours](docs/sdks/timeoffpolicies/README.md#calculate_accruing_time_off_hours) - Calculate accruing time off hours
* [get](docs/sdks/timeoffpolicies/README.md#get) - Get a time off policy
* [update](docs/sdks/timeoffpolicies/README.md#update) - Update a time off policy
* [get_all](docs/sdks/timeoffpolicies/README.md#get_all) - Get all time off policies for a company
* [create](docs/sdks/timeoffpolicies/README.md#create) - Create a time off policy
* [add_employees](docs/sdks/timeoffpolicies/README.md#add_employees) - Add employees to a time off policy
* [remove_employees](docs/sdks/timeoffpolicies/README.md#remove_employees) - Remove employees from a time off policy
* [update_balance](docs/sdks/timeoffpolicies/README.md#update_balance) - Update employee time off balances
* [deactivate](docs/sdks/timeoffpolicies/README.md#deactivate) - Deactivate a time off policy

### [Webhooks](docs/sdks/webhooks/README.md)

* [list_subscriptions](docs/sdks/webhooks/README.md#list_subscriptions) - List webhook subscriptions
* [create_subscription](docs/sdks/webhooks/README.md#create_subscription) - Create a webhook subscription
* [get_subscription](docs/sdks/webhooks/README.md#get_subscription) - Get a webhook subscription
* [update_subscription](docs/sdks/webhooks/README.md#update_subscription) - Update a webhook subscription
* [delete_subscription](docs/sdks/webhooks/README.md#delete_subscription) - Delete a webhook subscription
* [verify](docs/sdks/webhooks/README.md#verify) - Verify a webhook subscription
* [request_verification_token](docs/sdks/webhooks/README.md#request_verification_token) - Request a verification token for a webhook subscription
* [get_v1_webhooks_health_check](docs/sdks/webhooks/README.md#get_v1_webhooks_health_check) - Get the webhooks health status

### [WireInRequests](docs/sdks/wireinrequests/README.md)

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
import gusto_embedded_v_2025_11_15
from gusto_embedded_v_2025_11_15 import Gusto
import os


with Gusto(
    company_access_auth=os.getenv("GUSTO_COMPANY_ACCESS_AUTH", ""),
) as gusto:

    res = gusto.company_attachments.create(company_id="<id>", document={
        "file_name": "example.file",
        "content": open("example.file", "rb"),
    }, category=gusto_embedded_v_2025_11_15.CompanyAttachmentCreateRequestBodyCategory.GEP_NOTICE, x_gusto_api_version=gusto_embedded_v_2025_11_15.PostV1CompaniesAttachmentHeaderXGustoAPIVersion.TWO_THOUSAND_AND_TWENTY_FIVE_MINUS_11_MINUS_15)

    # Handle response
    print(res)

```
<!-- End File uploads [file-upload] -->

<!-- Start Retries [retries] -->
## Retries

Some of the endpoints in this SDK support retries. If you use the SDK without any configuration, it will fall back to the default retry strategy provided by the API. However, the default retry strategy can be overridden on a per-operation basis, or across the entire SDK.

To change the default retry strategy for a single API call, simply provide a `RetryConfig` object to the call:
```python
import gusto_embedded_v_2025_11_15
from gusto_embedded_v_2025_11_15 import Gusto
from gusto_embedded_v_2025_11_15.utils import BackoffStrategy, RetryConfig
import os


with Gusto(
    company_access_auth=os.getenv("GUSTO_COMPANY_ACCESS_AUTH", ""),
) as gusto:

    res = gusto.introspection.get_info(x_gusto_api_version=gusto_embedded_v_2025_11_15.XGustoAPIVersion.TWO_THOUSAND_AND_TWENTY_FIVE_MINUS_11_MINUS_15,
        RetryConfig("backoff", BackoffStrategy(1, 50, 1.1, 100), False))

    # Handle response
    print(res)

```

If you'd like to override the default retry strategy for all operations that support retries, you can use the `retry_config` optional parameter when initializing the SDK:
```python
import gusto_embedded_v_2025_11_15
from gusto_embedded_v_2025_11_15 import Gusto
from gusto_embedded_v_2025_11_15.utils import BackoffStrategy, RetryConfig
import os


with Gusto(
    retry_config=RetryConfig("backoff", BackoffStrategy(1, 50, 1.1, 100), False),
    company_access_auth=os.getenv("GUSTO_COMPANY_ACCESS_AUTH", ""),
) as gusto:

    res = gusto.introspection.get_info(x_gusto_api_version=gusto_embedded_v_2025_11_15.XGustoAPIVersion.TWO_THOUSAND_AND_TWENTY_FIVE_MINUS_11_MINUS_15)

    # Handle response
    print(res)

```
<!-- End Retries [retries] -->

<!-- Start Error Handling [errors] -->
## Error Handling

[`GustoError`](./src/gusto_embedded_v_2025_11_15/models/gustoerror.py) is the base class for all HTTP error responses. It has the following properties:

| Property           | Type             | Description                                                                             |
| ------------------ | ---------------- | --------------------------------------------------------------------------------------- |
| `err.message`      | `str`            | Error message                                                                           |
| `err.status_code`  | `int`            | HTTP response status code eg `404`                                                      |
| `err.headers`      | `httpx.Headers`  | HTTP response headers                                                                   |
| `err.body`         | `str`            | HTTP body. Can be empty string if no body is returned.                                  |
| `err.raw_response` | `httpx.Response` | Raw HTTP response                                                                       |
| `err.data`         |                  | Optional. Some errors may contain structured data. [See Error Classes](#error-classes). |

### Example
```python
import gusto_embedded_v_2025_11_15
from gusto_embedded_v_2025_11_15 import Gusto, models
import os


with Gusto() as gusto:
    res = None
    try:

        res = gusto.companies.create_partner_managed(security=gusto_embedded_v_2025_11_15.PostV1PartnerManagedCompaniesSecurity(
            system_access_auth=os.getenv("GUSTO_SYSTEM_ACCESS_AUTH", ""),
        ), user={
            "first_name": "Marco",
            "last_name": "Trantow",
            "email": "Jewell_Greenholt72@hotmail.com",
        }, company={
            "name": "<value>",
        }, x_gusto_api_version=gusto_embedded_v_2025_11_15.PostV1PartnerManagedCompaniesHeaderXGustoAPIVersion.TWO_THOUSAND_AND_TWENTY_FIVE_MINUS_11_MINUS_15)

        # Handle response
        print(res)


    except models.GustoError as e:
        # The base class for HTTP error responses
        print(e.message)
        print(e.status_code)
        print(e.body)
        print(e.headers)
        print(e.raw_response)

        # Depending on the method different errors may be thrown
        if isinstance(e, models.UnprocessableEntityError1):
            print(e.data.errors)  # List[gusto_embedded_v_2025_11_15.EntityErrorObject]
```

### Error Classes
**Primary errors:**
* [`GustoError`](./src/gusto_embedded_v_2025_11_15/models/gustoerror.py): The base class for HTTP error responses.
  * [`NotFoundErrorObjectError`](./src/gusto_embedded_v_2025_11_15/models/notfounderrorobjecterror.py): Not Found     The requested resource does not exist. Make sure the provided ID/UUID is valid. *

<details><summary>Less common errors (9)</summary>

<br />

**Network errors:**
* [`httpx.RequestError`](https://www.python-httpx.org/exceptions/#httpx.RequestError): Base class for request errors.
    * [`httpx.ConnectError`](https://www.python-httpx.org/exceptions/#httpx.ConnectError): HTTP client was unable to make a request to a server.
    * [`httpx.TimeoutException`](https://www.python-httpx.org/exceptions/#httpx.TimeoutException): HTTP request timed out.


**Inherit from [`GustoError`](./src/gusto_embedded_v_2025_11_15/models/gustoerror.py)**:
* [`UnprocessableEntityError1`](./src/gusto_embedded_v_2025_11_15/models/unprocessableentityerror1.py): Unprocessable Entity    This may happen when the body of your request contains errors such as `invalid_attribute_value`, or the request fails due to an `invalid_operation`. See the [Errors Categories](https://docs.gusto.com/embedded-payroll/docs/error-categories) guide for more details. Applicable to 152 of 297 methods.*
* [`ConflictErrorObject`](./src/gusto_embedded_v_2025_11_15/models/conflicterrorobject.py): Conflict    This error occurs when the resource version provided does not match the current version. Retrieve the latest version and retry. Status code `409`. Applicable to 2 of 297 methods.*
* [`PeopleBatchConflictError`](./src/gusto_embedded_v_2025_11_15/models/peoplebatchconflicterror.py): Error response when a people batch idempotency key conflict occurs. Status code `409`. Applicable to 1 of 297 methods.*
* [`PayrollBlockersError`](./src/gusto_embedded_v_2025_11_15/models/payrollblockerserror.py): Payroll Blockers Error  For detailed information, see the [Payroll Blockers guide](https://docs.gusto.com/embedded-payroll/docs/payroll-blockers). Status code `422`. Applicable to 1 of 297 methods.*
* [`ResponseValidationError`](./src/gusto_embedded_v_2025_11_15/models/responsevalidationerror.py): Type mismatch between the response data and the expected Pydantic model. Provides access to the Pydantic validation error via the `cause` attribute.

</details>

\* Check [the method documentation](#available-resources-and-operations) to see if the error is applicable.
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
import gusto_embedded_v_2025_11_15
from gusto_embedded_v_2025_11_15 import Gusto
import os


with Gusto(
    server="demo",
    company_access_auth=os.getenv("GUSTO_COMPANY_ACCESS_AUTH", ""),
) as gusto:

    res = gusto.introspection.get_info(x_gusto_api_version=gusto_embedded_v_2025_11_15.XGustoAPIVersion.TWO_THOUSAND_AND_TWENTY_FIVE_MINUS_11_MINUS_15)

    # Handle response
    print(res)

```

### Override Server URL Per-Client

The default server can also be overridden globally by passing a URL to the `server_url: str` optional parameter when initializing the SDK client instance. For example:
```python
import gusto_embedded_v_2025_11_15
from gusto_embedded_v_2025_11_15 import Gusto
import os


with Gusto(
    server_url="https://api.gusto-demo.com",
    company_access_auth=os.getenv("GUSTO_COMPANY_ACCESS_AUTH", ""),
) as gusto:

    res = gusto.introspection.get_info(x_gusto_api_version=gusto_embedded_v_2025_11_15.XGustoAPIVersion.TWO_THOUSAND_AND_TWENTY_FIVE_MINUS_11_MINUS_15)

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
from gusto_embedded_v_2025_11_15 import Gusto
import httpx

http_client = httpx.Client(headers={"x-custom-header": "someValue"})
s = Gusto(client=http_client)
```

or you could wrap the client with your own custom logic:
```python
from gusto_embedded_v_2025_11_15 import Gusto
from gusto_embedded_v_2025_11_15.httpclient import AsyncHttpClient
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
from gusto_embedded_v_2025_11_15 import Gusto
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
from gusto_embedded_v_2025_11_15 import Gusto
import logging

logging.basicConfig(level=logging.DEBUG)
s = Gusto(debug_logger=logging.getLogger("gusto_embedded_v_2025_11_15"))
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

### SDK Created by [Speakeasy](https://www.speakeasy.com/?utm_source=gusto-embedded-v-2025-11-15&utm_campaign=python)
