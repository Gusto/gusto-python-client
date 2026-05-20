# Key

A unique identifier for the payroll blocker reason. For a complete list of blockers and their meanings, see the [Payroll Blockers guide](https://docs.gusto.com/embedded-payroll/docs/payroll-blockers).

## Example Usage

```python
from gusto_embedded.models import Key

value = Key.COMPANY_OWNERSHIP_REQUIRED
```


## Values

| Name                              | Value                             |
| --------------------------------- | --------------------------------- |
| `COMPANY_OWNERSHIP_REQUIRED`      | company_ownership_required        |
| `CONTRACTOR_ONLY_COMPANY`         | contractor_only_company           |
| `EFTPS_IN_ERROR`                  | eftps_in_error                    |
| `GEOCODE_ERROR`                   | geocode_error                     |
| `GEOCODE_NEEDED`                  | geocode_needed                    |
| `INVALID_SIGNATORY`               | invalid_signatory                 |
| `MISSING_ADDRESSES`               | missing_addresses                 |
| `MISSING_BANK_INFO`               | missing_bank_info                 |
| `MISSING_BANK_VERIFICATION`       | missing_bank_verification         |
| `MISSING_EMPLOYEE_SETUP`          | missing_employee_setup            |
| `MISSING_FEDERAL_TAX_SETUP`       | missing_federal_tax_setup         |
| `MISSING_FORMS`                   | missing_forms                     |
| `MISSING_INDUSTRY_SELECTION`      | missing_industry_selection        |
| `MISSING_PAY_SCHEDULE`            | missing_pay_schedule              |
| `MISSING_SIGNATORY`               | missing_signatory                 |
| `MISSING_STATE_TAX_SETUP`         | missing_state_tax_setup           |
| `NEEDS_APPROVAL`                  | needs_approval                    |
| `NEEDS_ONBOARDING`                | needs_onboarding                  |
| `PAY_SCHEDULE_SETUP_NOT_COMPLETE` | pay_schedule_setup_not_complete   |
| `PENDING_INFORMATION_REQUEST`     | pending_information_request       |
| `PENDING_PAYROLL_REVIEW`          | pending_payroll_review            |
| `PENDING_RECOVERY_CASE`           | pending_recovery_case             |
| `SOFT_SUSPENDED`                  | soft_suspended                    |
| `SUSPENDED`                       | suspended                         |