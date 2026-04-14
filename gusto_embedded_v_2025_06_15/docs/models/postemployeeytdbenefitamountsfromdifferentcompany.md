# PostEmployeeYtdBenefitAmountsFromDifferentCompany


## Fields

| Field                                                                   | Type                                                                    | Required                                                                | Description                                                             |
| ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- |
| `benefit_type`                                                          | *Optional[int]*                                                         | :heavy_minus_sign:                                                      | The benefit type supported by Gusto.                                    |
| `tax_year`                                                              | *float*                                                                 | :heavy_check_mark:                                                      | The tax year for which this amount applies.                             |
| `ytd_employee_deduction_amount`                                         | *Optional[str]*                                                         | :heavy_minus_sign:                                                      | The year-to-date employee deduction made outside the current company.   |
| `ytd_company_contribution_amount`                                       | *Optional[str]*                                                         | :heavy_minus_sign:                                                      | The year-to-date company contribution made outside the current company. |