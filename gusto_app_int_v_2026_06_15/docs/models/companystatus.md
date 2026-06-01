# CompanyStatus

The status of the company in Gusto. "Approved" companies are approved to run payroll from a risk and compliance perspective. However, an approved company may still need to resolve other [payroll blockers](https://docs.gusto.com/embedded-payroll/docs/payroll-blockers) to be able to run payroll. "Not Approved" companies may not yet run payroll with Gusto and may need to complete onboarding or contact support. "Suspended" companies may not run payroll with Gusto. In order to unsuspend their account, the company must contact support.

## Example Usage

```python
from gusto_app_integration_v_2026_06_15.models import CompanyStatus

value = CompanyStatus.APPROVED

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name           | Value          |
| -------------- | -------------- |
| `APPROVED`     | Approved       |
| `NOT_APPROVED` | Not Approved   |
| `SUSPENDED`    | Suspended      |