## Python SDK Changes:
* `gusto_app_integration.webhooks.verify()`: 
  * `request.x_gusto_api_version` **Changed** (Breaking ⚠️)
    - `enum(2024_04_01)` **Removed** (Breaking ⚠️)
    - `enum(2025_06_15)` **Added**
  *  `response.subscription_types[].enum(payroll_sync)` **Added** (Breaking ⚠️)
  *  `error.status[404]` **Added**
* `gusto_app_integration.payrolls.get_for_company()`: 
  * `request` **Changed** (Breaking ⚠️)
    - `date_filter_by` **Added**
    - `include[].enum(taxes)` **Added**
    - `include_off_cycle` **Added**
    - `processed` **Added**
    - `processing_statuses` **Changed**
    - `sort_order` **Changed**
    - `x_gusto_api_version.enum(2024_04_01)` **Removed** (Breaking ⚠️)
    - `x_gusto_api_version.enum(2025_06_15)` **Added**
  * `response.[]` **Changed** (Breaking ⚠️)
    - `calculated_at` **Changed** (Breaking ⚠️)
    - `company_taxes` **Added**
    - `company_uuid` **Changed**
    - `credit_blockers[].unblock_options[]` **Changed** (Breaking ⚠️)
    - `fixed_withholding_rate` **Changed** (Breaking ⚠️)
    - `off_cycle_reason.enum(adhoc)` **Added** (Breaking ⚠️)
    - `partner_owned_disbursement` **Added**
    - `payroll_taxes` **Added**
    - `payroll_uuid` **Changed**
    - `processed_date` **Changed** (Breaking ⚠️)
    - `processed` **Changed**
    - `processing_request` **Added**
    - `reversal_payroll_uuids` **Removed** (Breaking ⚠️)
    - `skip_regular_deductions` **Changed** (Breaking ⚠️)
    - `submission_blockers[].unblock_options[].metadata` **Changed** (Breaking ⚠️)
    - `uuid` **Changed**
    - `withholding_pay_period` **Changed** (Breaking ⚠️)
  *  `error.status[404]` **Added**
* `gusto_app_integration.time_tracking.delete_time_tracking_time_sheets_time_sheet_uuid()`: 
  * `request.x_gusto_api_version` **Changed** (Breaking ⚠️)
    - `enum(2024_04_01)` **Removed** (Breaking ⚠️)
    - `enum(2025_06_15)` **Added**
  *  `error.status[404]` **Added**
* `gusto_app_integration.time_tracking.put_time_tracking_time_sheets_time_sheet_uuid()`: 
  * `request.x_gusto_api_version` **Changed** (Breaking ⚠️)
    - `enum(2024_04_01)` **Removed** (Breaking ⚠️)
    - `enum(2025_06_15)` **Added**
  *  `response.synced_to_payroll_at` **Added**
  *  `error.status[404]` **Added**
* `gusto_app_integration.time_tracking.get_time_tracking_time_sheets_time_sheet_uuid()`: 
  * `request.x_gusto_api_version` **Changed** (Breaking ⚠️)
    - `enum(2024_04_01)` **Removed** (Breaking ⚠️)
    - `enum(2025_06_15)` **Added**
  *  `response.synced_to_payroll_at` **Added**
  *  `error.status[404]` **Added**
* `gusto_app_integration.time_tracking.post_companies_company_uuid_time_tracking_time_sheets()`: 
  * `request.x_gusto_api_version` **Changed** (Breaking ⚠️)
    - `enum(2024_04_01)` **Removed** (Breaking ⚠️)
    - `enum(2025_06_15)` **Added**
  *  `response.synced_to_payroll_at` **Added**
  *  `error.status[404]` **Added**
* `gusto_app_integration.time_tracking.get_companies_company_uuid_time_tracking_time_sheets()`: 
  * `request` **Changed** (Breaking ⚠️)
    - `entity_type` **Changed**
    - `sort_by` **Changed**
    - `sort_order` **Changed**
    - `status` **Changed**
    - `x_gusto_api_version.enum(2024_04_01)` **Removed** (Breaking ⚠️)
    - `x_gusto_api_version.enum(2025_06_15)` **Added**
  *  `response.[].synced_to_payroll_at` **Added**
  *  `error.status[404]` **Added**
* `gusto_app_integration.events.get_all()`: 
  * `request` **Changed** (Breaking ⚠️)
    - `sort_order` **Changed**
    - `x_gusto_api_version.enum(2024_04_01)` **Removed** (Breaking ⚠️)
    - `x_gusto_api_version.enum(2025_06_15)` **Added**
  *  `error.status[422]` **Added**
* `gusto_app_integration.garnishments.get_child_support()`: 
  * `request.x_gusto_api_version` **Changed** (Breaking ⚠️)
    - `enum(2024_04_01)` **Removed** (Breaking ⚠️)
    - `enum(2025_06_15)` **Added**
  *  `error.status[404]` **Removed** (Breaking ⚠️)
* `gusto_app_integration.garnishments.update()`: 
  * `request` **Changed** (Breaking ⚠️)
    - `garnishment_type` **Added**
    - `total_amount` **Changed**
    - `x_gusto_api_version.enum(2024_04_01)` **Removed** (Breaking ⚠️)
    - `x_gusto_api_version.enum(2025_06_15)` **Added**
  *  `error.status[404]` **Added**
* `gusto_app_integration.garnishments.get_by_id()`: 
  * `request.x_gusto_api_version` **Changed** (Breaking ⚠️)
    - `enum(2024_04_01)` **Removed** (Breaking ⚠️)
    - `enum(2025_06_15)` **Added**
  *  `error.status[404]` **Added**
* `gusto_app_integration.garnishments.get()`: 
  * `request.x_gusto_api_version` **Changed** (Breaking ⚠️)
    - `enum(2024_04_01)` **Removed** (Breaking ⚠️)
    - `enum(2025_06_15)` **Added**
  *  `error.status[404]` **Added**
* `gusto_app_integration.garnishments.create()`: 
  * `request` **Changed** (Breaking ⚠️)
    - `total_amount` **Changed**
    - `x_gusto_api_version.enum(2024_04_01)` **Removed** (Breaking ⚠️)
    - `x_gusto_api_version.enum(2025_06_15)` **Added**
  *  `error.status[404]` **Added**
* `gusto_app_integration.employee_benefits.create_ytd_benefit_amounts_from_different_company()`: 
  * `request` **Changed** (Breaking ⚠️)
    - `benefit_type` **Changed** (Breaking ⚠️)
    - `x_gusto_api_version.enum(2024_04_01)` **Removed** (Breaking ⚠️)
    - `x_gusto_api_version.enum(2025_06_15)` **Added**
  *  `error.status[404]` **Added**
* `gusto_app_integration.employee_benefits.get_ytd_benefit_amounts_from_different_company()`: 
  * `request.x_gusto_api_version` **Changed** (Breaking ⚠️)
    - `enum(2024_04_01)` **Removed** (Breaking ⚠️)
    - `enum(2025_06_15)` **Added**
  *  `error.status[404]` **Added**
* `gusto_app_integration.employee_benefits.delete()`: 
  * `request.x_gusto_api_version` **Changed** (Breaking ⚠️)
    - `enum(2024_04_01)` **Removed** (Breaking ⚠️)
    - `enum(2025_06_15)` **Added**
  *  `error.status[422]` **Added**
* `gusto_app_integration.employee_benefits.update()`: 
  * `request` **Changed** (Breaking ⚠️)
    - `effective_date` **Added**
    - `expiration_date` **Added**
    - `x_gusto_api_version.enum(2024_04_01)` **Removed** (Breaking ⚠️)
    - `x_gusto_api_version.enum(2025_06_15)` **Added**
  * `response` **Changed** (Breaking ⚠️)
    - `additional_properties` **Added**
    - `catch_up` **Changed** (Breaking ⚠️)
    - `coverage_salary_multiplier` **Changed** (Breaking ⚠️)
    - `effective_date` **Added**
    - `expiration_date` **Added**
    - `retirement_loan_identifier` **Changed** (Breaking ⚠️)
  *  `error.status[404]` **Added**
* `gusto_app_integration.employee_benefits.get()`: 
  * `request.x_gusto_api_version` **Changed** (Breaking ⚠️)
    - `enum(2024_04_01)` **Removed** (Breaking ⚠️)
    - `enum(2025_06_15)` **Added**
  * `response` **Changed** (Breaking ⚠️)
    - `additional_properties` **Added**
    - `catch_up` **Changed** (Breaking ⚠️)
    - `coverage_salary_multiplier` **Changed** (Breaking ⚠️)
    - `effective_date` **Added**
    - `expiration_date` **Added**
    - `retirement_loan_identifier` **Changed** (Breaking ⚠️)
  *  `error.status[404]` **Added**
* `gusto_app_integration.employee_benefits.get_all()`: 
  * `request` **Changed** (Breaking ⚠️)
    - `include` **Added**
    - `x_gusto_api_version.enum(2024_04_01)` **Removed** (Breaking ⚠️)
    - `x_gusto_api_version.enum(2025_06_15)` **Added**
  * `response.[]` **Changed** (Breaking ⚠️)
    - `additional_properties` **Added**
    - `catch_up` **Changed** (Breaking ⚠️)
    - `coverage_salary_multiplier` **Changed** (Breaking ⚠️)
    - `effective_date` **Added**
    - `expiration_date` **Added**
    - `retirement_loan_identifier` **Changed** (Breaking ⚠️)
  *  `error.status[404]` **Added**
* `gusto_app_integration.employee_benefits.create()`: 
  * `request` **Changed** (Breaking ⚠️)
    - `effective_date` **Added**
    - `expiration_date` **Added**
    - `x_gusto_api_version.enum(2024_04_01)` **Removed** (Breaking ⚠️)
    - `x_gusto_api_version.enum(2025_06_15)` **Added**
  * `response` **Changed** (Breaking ⚠️)
    - `additional_properties` **Added**
    - `catch_up` **Changed** (Breaking ⚠️)
    - `coverage_salary_multiplier` **Changed** (Breaking ⚠️)
    - `effective_date` **Added**
    - `expiration_date` **Added**
    - `retirement_loan_identifier` **Changed** (Breaking ⚠️)
  *  `error.status[404]` **Added**
* `gusto_app_integration.company_benefits.get_requirements()`: 
  * `request.x_gusto_api_version` **Changed** (Breaking ⚠️)
    - `enum(2024_04_01)` **Removed** (Breaking ⚠️)
    - `enum(2025_06_15)` **Added**
  * `response` **Changed** (Breaking ⚠️)
    - `catch_up.choices` **Changed** (Breaking ⚠️)
    - `catch_up.default_value` **Changed** (Breaking ⚠️)
    - `company_contribution_annual_maximum.choices` **Changed** (Breaking ⚠️)
    - `company_contribution_annual_maximum.default_value` **Changed** (Breaking ⚠️)
    - `contribution.choices` **Changed** (Breaking ⚠️)
    - `contribution.default_value` **Changed** (Breaking ⚠️)
    - `coverage_amount.choices` **Changed** (Breaking ⚠️)
    - `coverage_amount.default_value` **Changed** (Breaking ⚠️)
    - `coverage_salary_multiplier.choices` **Changed** (Breaking ⚠️)
    - `coverage_salary_multiplier.default_value` **Changed** (Breaking ⚠️)
    - `deduct_as_percentage.choices` **Changed** (Breaking ⚠️)
    - `deduct_as_percentage.default_value` **Changed** (Breaking ⚠️)
    - `employee_deduction.choices` **Changed** (Breaking ⚠️)
    - `employee_deduction.default_value` **Changed** (Breaking ⚠️)
    - `limit_option.choices` **Changed** (Breaking ⚠️)
    - `limit_option.default_value` **Changed** (Breaking ⚠️)
  *  `error.status[404]` **Added**
* `gusto_app_integration.company_benefits.bulk_update_employee_benefits()`: 
  * `request` **Changed** (Breaking ⚠️)
    - `employee_benefits[].action` **Added**
    - `employee_benefits[].additional_properties` **Added**
    - `employee_benefits[].catch_up` **Changed**
    - `employee_benefits[].coverage_salary_multiplier` **Changed**
    - `employee_benefits[].effective_date` **Added**
    - `employee_benefits[].expiration_date` **Added**
    - `employee_benefits[].retirement_loan_identifier` **Changed**
    - `employee_benefits[].uuid` **Added**
    - `x_gusto_api_version.enum(2024_04_01)` **Removed** (Breaking ⚠️)
    - `x_gusto_api_version.enum(2025_06_15)` **Added**
  * `response.[]` **Changed** (Breaking ⚠️)
    - `additional_properties` **Added**
    - `catch_up` **Changed** (Breaking ⚠️)
    - `coverage_salary_multiplier` **Changed** (Breaking ⚠️)
    - `effective_date` **Added**
    - `expiration_date` **Added**
    - `retirement_loan_identifier` **Changed** (Breaking ⚠️)
  *  `error.status[404]` **Added**
* `gusto_app_integration.company_benefits.get_employee_benefits()`: 
  * `request` **Changed** (Breaking ⚠️)
    - `include` **Added**
    - `x_gusto_api_version.enum(2024_04_01)` **Removed** (Breaking ⚠️)
    - `x_gusto_api_version.enum(2025_06_15)` **Added**
  * `response.[]` **Changed** (Breaking ⚠️)
    - `additional_properties` **Added**
    - `catch_up` **Changed** (Breaking ⚠️)
    - `coverage_salary_multiplier` **Changed** (Breaking ⚠️)
    - `effective_date` **Added**
    - `expiration_date` **Added**
    - `retirement_loan_identifier` **Changed** (Breaking ⚠️)
  *  `error.status[404]` **Added**
* `gusto_app_integration.company_benefits.get_summary()`: 
  * `request.x_gusto_api_version` **Changed** (Breaking ⚠️)
    - `enum(2024_04_01)` **Removed** (Breaking ⚠️)
    - `enum(2025_06_15)` **Added**
  *  `response.employees` **Changed** (Breaking ⚠️)
  *  `error.status[404]` **Added**
* `gusto_app_integration.company_benefits.get()`: 
  * `request.x_gusto_api_version` **Changed** (Breaking ⚠️)
    - `enum(2024_04_01)` **Removed** (Breaking ⚠️)
    - `enum(2025_06_15)` **Added**
  *  `response.writable_by_application` **Added**
  *  `error.status[404]` **Removed** (Breaking ⚠️)
* `gusto_app_integration.company_benefits.list_supported()`: 
  * `request.x_gusto_api_version` **Changed** (Breaking ⚠️)
    - `enum(2024_04_01)` **Removed** (Breaking ⚠️)
    - `enum(2025_06_15)` **Added**
  *  `response.[].writable_by_application` **Added**
  *  `error.status[404]` **Removed** (Breaking ⚠️)
* `gusto_app_integration.company_benefits.delete()`: 
  * `request.x_gusto_api_version` **Changed** (Breaking ⚠️)
    - `enum(2024_04_01)` **Removed** (Breaking ⚠️)
    - `enum(2025_06_15)` **Added**
  *  `error.status[422]` **Removed** (Breaking ⚠️)
* `gusto_app_integration.company_benefits.update()`: 
  * `request` **Changed** (Breaking ⚠️)
    - `catch_up_type` **Added**
    - `responsible_for_employee_w2` **Added**
    - `responsible_for_employer_taxes` **Added**
    - `x_gusto_api_version.enum(2024_04_01)` **Removed** (Breaking ⚠️)
    - `x_gusto_api_version.enum(2025_06_15)` **Added**
  *  `response.catch_up_type` **Added**
  *  `error.status[404]` **Added**
* `gusto_app_integration.company_benefits.get_by_id()`: 
  * `request` **Changed** (Breaking ⚠️)
    - `include` **Added**
    - `x_gusto_api_version.enum(2024_04_01)` **Removed** (Breaking ⚠️)
    - `x_gusto_api_version.enum(2025_06_15)` **Added**
  * `response` **Changed** (Breaking ⚠️)
    - `catch_up_type` **Added**
    - `employee_benefits[].effective_date` **Added**
    - `employee_benefits[].expiration_date` **Added**
    - `employee_benefits[].uuid` **Removed** (Breaking ⚠️)
  *  `error.status[404]` **Added**
* `gusto_app_integration.company_benefits.list()`: 
  * `request` **Changed** (Breaking ⚠️)
    - `benefit_type` **Added**
    - `x_gusto_api_version.enum(2024_04_01)` **Removed** (Breaking ⚠️)
    - `x_gusto_api_version.enum(2025_06_15)` **Added**
  *  `response.[].catch_up_type` **Added**
  *  `error.status[404]` **Added**
* `gusto_app_integration.company_benefits.create()`: 
  * `request` **Changed** (Breaking ⚠️)
    - `catch_up_type` **Added**
    - `x_gusto_api_version.enum(2024_04_01)` **Removed** (Breaking ⚠️)
    - `x_gusto_api_version.enum(2025_06_15)` **Added**
  *  `response.catch_up_type` **Added**
  *  `error.status[404]` **Added**
* `gusto_app_integration.contractor_payments.get_by_id()`: 
  * `request.x_gusto_api_version` **Changed** (Breaking ⚠️)
    - `enum(2024_04_01)` **Removed** (Breaking ⚠️)
    - `enum(2025_06_15)` **Added**
  *  `error.status[404]` **Added**
* `gusto_app_integration.contractor_payments.get()`: 
  * `request.x_gusto_api_version` **Changed** (Breaking ⚠️)
    - `enum(2024_04_01)` **Removed** (Breaking ⚠️)
    - `enum(2025_06_15)` **Added**
  *  `error.status[404]` **Added**
* `gusto_app_integration.time_off_policies.calculate_accruing_time_off_hours()`: 
  * `request` **Changed** (Breaking ⚠️)
    - `double_overtime_hours_worked` **Changed** (Breaking ⚠️)
    - `overtime_hours_worked` **Changed** (Breaking ⚠️)
    - `pto_hours_used` **Changed** (Breaking ⚠️)
    - `regular_hours_worked` **Changed** (Breaking ⚠️)
    - `sick_hours_used` **Changed** (Breaking ⚠️)
    - `x_gusto_api_version.enum(2024_04_01)` **Removed** (Breaking ⚠️)
    - `x_gusto_api_version.enum(2025_06_15)` **Added**
  *  `error.status[404]` **Added**
* `gusto_app_integration.payrolls.prepare()`: 
  * `request` **Changed** (Breaking ⚠️)
    - `employee_uuids` **Added**
    - `page` **Added**
    - `per` **Added**
    - `sort_by` **Added**
    - `x_gusto_api_version.enum(2024_04_01)` **Removed** (Breaking ⚠️)
    - `x_gusto_api_version.enum(2025_06_15)` **Added**
  * `response` **Changed** (Breaking ⚠️)
    - `calculated_at` **Changed** (Breaking ⚠️)
    - `employee_compensations[].benefits` **Removed** (Breaking ⚠️)
    - `employee_compensations[].deductions[].amount_type` **Added**
    - `employee_compensations[].deductions[].updatable_via_payroll` **Added**
    - `employee_compensations[].deductions[].uuid` **Added**
    - `employee_compensations[].first_name` **Added**
    - `employee_compensations[].last_name` **Added**
    - `employee_compensations[].paid_time_off[].final_payout_unused_hours_input` **Changed** (Breaking ⚠️)
    - `employee_compensations[].payment_method.enum(historical)` **Added** (Breaking ⚠️)
    - `employee_compensations[].preferred_first_name` **Added**
    - `employee_compensations[].reimbursements` **Added**
    - `employee_compensations[].taxes` **Removed** (Breaking ⚠️)
    - `employee_compensations[].version` **Changed** (Breaking ⚠️)
    - `fixed_withholding_rate` **Changed** (Breaking ⚠️)
    - `off_cycle_reason.enum(adhoc)` **Added** (Breaking ⚠️)
    - `partner_owned_disbursement` **Added**
    - `processed_date` **Changed** (Breaking ⚠️)
    - `skip_regular_deductions` **Changed** (Breaking ⚠️)
    - `withholding_pay_period` **Changed** (Breaking ⚠️)
  * `error` **Changed**
    - `` **Added**
    - `status[422]` **Added**
* `gusto_app_integration.payrolls.update()`: 
  * `request` **Changed** (Breaking ⚠️)
    - `employee_compensations[].deductions` **Added**
    - `employee_compensations[].paid_time_off[].final_payout_unused_hours_input` **Changed**
    - `employee_compensations[].reimbursements` **Added**
    - `x_gusto_api_version.enum(2024_04_01)` **Removed** (Breaking ⚠️)
    - `x_gusto_api_version.enum(2025_06_15)` **Added**
  * `response` **Changed** (Breaking ⚠️)
    - `calculated_at` **Changed** (Breaking ⚠️)
    - `employee_compensations[].benefits` **Removed** (Breaking ⚠️)
    - `employee_compensations[].deductions[].amount_type` **Added**
    - `employee_compensations[].deductions[].updatable_via_payroll` **Added**
    - `employee_compensations[].deductions[].uuid` **Added**
    - `employee_compensations[].first_name` **Added**
    - `employee_compensations[].last_name` **Added**
    - `employee_compensations[].paid_time_off[].final_payout_unused_hours_input` **Changed** (Breaking ⚠️)
    - `employee_compensations[].payment_method.enum(historical)` **Added** (Breaking ⚠️)
    - `employee_compensations[].preferred_first_name` **Added**
    - `employee_compensations[].reimbursements` **Added**
    - `employee_compensations[].taxes` **Removed** (Breaking ⚠️)
    - `employee_compensations[].version` **Changed** (Breaking ⚠️)
    - `fixed_withholding_rate` **Changed** (Breaking ⚠️)
    - `off_cycle_reason.enum(adhoc)` **Added** (Breaking ⚠️)
    - `partner_owned_disbursement` **Added**
    - `processed_date` **Changed** (Breaking ⚠️)
    - `skip_regular_deductions` **Changed** (Breaking ⚠️)
    - `withholding_pay_period` **Changed** (Breaking ⚠️)
  *  `error.status[404]` **Added**
* `gusto_app_integration.payrolls.get()`: 
  * `request` **Changed** (Breaking ⚠️)
    - `include[].enum(payroll_taxes)` **Added**
    - `include[].enum(reversals)` **Added**
    - `include[].enum(risk_blockers)` **Added**
    - `include[].enum(totals)` **Added**
    - `page` **Added**
    - `per` **Added**
    - `sort_by` **Added**
    - `x_gusto_api_version.enum(2024_04_01)` **Removed** (Breaking ⚠️)
    - `x_gusto_api_version.enum(2025_06_15)` **Added**
  * `response` **Changed** (Breaking ⚠️)
    - `calculated_at` **Changed** (Breaking ⚠️)
    - `credit_blockers[].unblock_options[]` **Changed** (Breaking ⚠️)
    - `employee_compensations[].additional_properties` **Added**
    - `employee_compensations[].deductions[].amount_type` **Added**
    - `employee_compensations[].deductions[].updatable_via_payroll` **Added**
    - `employee_compensations[].deductions[].uuid` **Added**
    - `employee_compensations[].first_name` **Added**
    - `employee_compensations[].last_name` **Added**
    - `employee_compensations[].paid_time_off[].final_payout_unused_hours_input` **Changed** (Breaking ⚠️)
    - `employee_compensations[].payment_method.enum(historical)` **Added** (Breaking ⚠️)
    - `employee_compensations[].preferred_first_name` **Added**
    - `employee_compensations[].reimbursements` **Added**
    - `employee_compensations[].version` **Changed** (Breaking ⚠️)
    - `fixed_withholding_rate` **Changed** (Breaking ⚠️)
    - `off_cycle_reason.enum(adhoc)` **Added** (Breaking ⚠️)
    - `partner_owned_disbursement` **Added**
    - `payroll_taxes` **Added**
    - `processed_date` **Changed** (Breaking ⚠️)
    - `skip_regular_deductions` **Changed** (Breaking ⚠️)
    - `submission_blockers[].unblock_options[].metadata` **Changed** (Breaking ⚠️)
    - `withholding_pay_period` **Changed** (Breaking ⚠️)
  *  `error.status[404]` **Added**
* `gusto_app_integration.webhooks.request_verification_token()`: 
  * `request.x_gusto_api_version` **Changed** (Breaking ⚠️)
    - `enum(2024_04_01)` **Removed** (Breaking ⚠️)
    - `enum(2025_06_15)` **Added**
  *  `response.status[200]` **Added**
  *  `error.status[404]` **Added**
* `gusto_app_integration.webhooks.delete_subscription()`: 
  * `request.x_gusto_api_version` **Changed** (Breaking ⚠️)
    - `enum(2024_04_01)` **Removed** (Breaking ⚠️)
    - `enum(2025_06_15)` **Added**
  *  `error.status[404]` **Added**
* `gusto_app_integration.introspection.get_token_info()`: 
  * `request.x_gusto_api_version` **Changed** (Breaking ⚠️)
    - `enum(2024_04_01)` **Removed** (Breaking ⚠️)
    - `enum(2025_06_15)` **Added**
  * `response` **Changed**
    - `resource.type` **Changed**
    - `resource.uuid` **Changed**
    - `resource_owner.type` **Changed**
    - `resource_owner.uuid` **Changed**
    - `scope` **Changed**
* `gusto_app_integration.introspection.revoke()`: `request.x_gusto_api_version` **Changed** (Breaking ⚠️)
    - `enum(2024_04_01)` **Removed** (Breaking ⚠️)
    - `enum(2025_06_15)` **Added**
* `gusto_app_integration.introspection.disconnect_app_integration()`: 
  * `request.x_gusto_api_version` **Changed** (Breaking ⚠️)
    - `enum(2024_04_01)` **Removed** (Breaking ⚠️)
    - `enum(2025_06_15)` **Added**
  *  `error.status[404]` **Added**
* `gusto_app_integration.companies.provision()`: 
  * `request.x_gusto_api_version` **Changed** (Breaking ⚠️)
    - `enum(2024_04_01)` **Removed** (Breaking ⚠️)
    - `enum(2025_06_15)` **Added**
  *  `error.status[401]` **Removed** (Breaking ⚠️)
* `gusto_app_integration.companies.get()`: 
  * `request.x_gusto_api_version` **Changed** (Breaking ⚠️)
    - `enum(2024_04_01)` **Removed** (Breaking ⚠️)
    - `enum(2025_06_15)` **Added**
  * `response` **Changed** (Breaking ⚠️)
    - `compensations.fixed[].uuid` **Added**
    - `compensations.hourly[].uuid` **Added**
    - `compensations.paid_time_off[].uuid` **Added**
    - `is_high_risk_business` **Added**
    - `is_marijuana_business` **Added**
    - `locations[].inactive` **Added**
    - `locations[].zip_code` **Added**
    - `locations[].zip` **Removed** (Breaking ⚠️)
    - `primary_signatory.home_address.zip_code` **Added**
    - `primary_signatory.home_address.zip` **Removed** (Breaking ⚠️)
  *  `error.status[404]` **Added**
* `gusto_app_integration.companies.update()`: 
  * `request.x_gusto_api_version` **Changed** (Breaking ⚠️)
    - `enum(2024_04_01)` **Removed** (Breaking ⚠️)
    - `enum(2025_06_15)` **Added**
  * `response` **Changed** (Breaking ⚠️)
    - `compensations.fixed[].uuid` **Added**
    - `compensations.hourly[].uuid` **Added**
    - `compensations.paid_time_off[].uuid` **Added**
    - `is_high_risk_business` **Added**
    - `is_marijuana_business` **Added**
    - `locations[].inactive` **Added**
    - `locations[].zip_code` **Added**
    - `locations[].zip` **Removed** (Breaking ⚠️)
    - `primary_signatory.home_address.zip_code` **Added**
    - `primary_signatory.home_address.zip` **Removed** (Breaking ⚠️)
  *  `error.status[404]` **Added**
* `gusto_app_integration.companies.get_admins()`: 
  * `request.x_gusto_api_version` **Changed** (Breaking ⚠️)
    - `enum(2024_04_01)` **Removed** (Breaking ⚠️)
    - `enum(2025_06_15)` **Added**
  *  `response.[].phone` **Added**
  *  `error.status[404]` **Added**
* `gusto_app_integration.companies.get_custom_fields()`: 
  * `request.x_gusto_api_version` **Changed** (Breaking ⚠️)
    - `enum(2024_04_01)` **Removed** (Breaking ⚠️)
    - `enum(2025_06_15)` **Added**
  *  `response.custom_fields[].description` **Changed** (Breaking ⚠️)
  *  `error.status[404]` **Added**
* `gusto_app_integration.locations.create()`: 
  * `request` **Changed** (Breaking ⚠️)
    - `country` **Added**
    - `x_gusto_api_version.enum(2024_04_01)` **Removed** (Breaking ⚠️)
    - `x_gusto_api_version.enum(2025_06_15)` **Added**
  * `response` **Changed** (Breaking ⚠️)
    - `inactive` **Added**
    - `zip_code` **Added**
    - `zip` **Removed** (Breaking ⚠️)
  *  `error.status[404]` **Added**
* `gusto_app_integration.locations.get()`: 
  * `request.x_gusto_api_version` **Changed** (Breaking ⚠️)
    - `enum(2024_04_01)` **Removed** (Breaking ⚠️)
    - `enum(2025_06_15)` **Added**
  * `response` **Changed** (Breaking ⚠️)
    - `inactive` **Added**
    - `zip_code` **Added**
    - `zip` **Removed** (Breaking ⚠️)
  * `errors[]` **Changed** (Breaking ⚠️)
    - `errors` **Removed** (Breaking ⚠️)
    - `metadata` **Removed** (Breaking ⚠️)
* `gusto_app_integration.employee_employments.update_termination()`: 
  * `request` **Changed** (Breaking ⚠️)
    - `run_termination_payroll` **Changed**
    - `x_gusto_api_version.enum(2024_04_01)` **Removed** (Breaking ⚠️)
    - `x_gusto_api_version.enum(2025_06_15)` **Added**
  * `errors[]` **Changed** (Breaking ⚠️)
    - `errors` **Removed** (Breaking ⚠️)
    - `metadata` **Removed** (Breaking ⚠️)
* `gusto_app_integration.locations.get_minimum_wages()`: 
  * `request.x_gusto_api_version` **Changed** (Breaking ⚠️)
    - `enum(2024_04_01)` **Removed** (Breaking ⚠️)
    - `enum(2025_06_15)` **Added**
  * `errors[]` **Changed** (Breaking ⚠️)
    - `errors` **Removed** (Breaking ⚠️)
    - `metadata` **Removed** (Breaking ⚠️)
* `gusto_app_integration.company_locations.list()`: 
  * `request.x_gusto_api_version` **Changed** (Breaking ⚠️)
    - `enum(2024_04_01)` **Removed** (Breaking ⚠️)
    - `enum(2025_06_15)` **Added**
  * `response.[]` **Changed** (Breaking ⚠️)
    - `inactive` **Added**
    - `zip_code` **Added**
    - `zip` **Removed** (Breaking ⚠️)
  *  `error.status[404]` **Added**
* `gusto_app_integration.pay_schedules.list()`: 
  * `request.x_gusto_api_version` **Changed** (Breaking ⚠️)
    - `enum(2024_04_01)` **Removed** (Breaking ⚠️)
    - `enum(2025_06_15)` **Added**
  * `response.[]` **Changed** (Breaking ⚠️)
    - `anchor_end_of_pay_period` **Changed** (Breaking ⚠️)
    - `anchor_pay_date` **Changed** (Breaking ⚠️)
    - `auto_payroll_enablement_blockers` **Added**
    - `auto_payroll` **Added**
  *  `error.status[404]` **Added**
* `gusto_app_integration.pay_schedules.get()`: 
  * `request.x_gusto_api_version` **Changed** (Breaking ⚠️)
    - `enum(2024_04_01)` **Removed** (Breaking ⚠️)
    - `enum(2025_06_15)` **Added**
  * `response` **Changed** (Breaking ⚠️)
    - `anchor_end_of_pay_period` **Changed** (Breaking ⚠️)
    - `anchor_pay_date` **Changed** (Breaking ⚠️)
    - `auto_payroll_enablement_blockers` **Added**
    - `auto_payroll` **Added**
  *  `error.status[404]` **Added**
* `gusto_app_integration.pay_schedules.get_pay_periods()`: 
  * `request` **Changed** (Breaking ⚠️)
    - `end_date` **Changed** (Breaking ⚠️)
    - `payroll_types` **Changed** (Breaking ⚠️)
    - `start_date` **Changed** (Breaking ⚠️)
    - `x_gusto_api_version.enum(2024_04_01)` **Removed** (Breaking ⚠️)
    - `x_gusto_api_version.enum(2025_06_15)` **Added**
  * `error` **Changed**
    - `` **Added**
    - `status[422]` **Added**
* `gusto_app_integration.pay_schedules.get_unprocessed_termination_pay_periods()`: 
  * `request.x_gusto_api_version` **Changed** (Breaking ⚠️)
    - `enum(2024_04_01)` **Removed** (Breaking ⚠️)
    - `enum(2025_06_15)` **Added**
  *  `error.status[404]` **Added**
* `gusto_app_integration.pay_schedules.get_assignments()`: 
  * `request.x_gusto_api_version` **Changed** (Breaking ⚠️)
    - `enum(2024_04_01)` **Removed** (Breaking ⚠️)
    - `enum(2025_06_15)` **Added**
  *  `response.employees[].pay_schedule_uuid` **Changed** (Breaking ⚠️)
  *  `error.status[404]` **Added**
* `gusto_app_integration.employees.get()`: 
  * `request` **Changed** (Breaking ⚠️)
    - `include[].enum(all_home_addresses)` **Added**
    - `include[].enum(current_home_address)` **Added**
    - `include[].enum(portal_invitations)` **Added**
    - `location_uuid` **Added**
    - `onboarded_active` **Added**
    - `onboarded` **Added**
    - `payroll_uuid` **Added**
    - `sort_by` **Added**
    - `terminated_today` **Added**
    - `uuids` **Added**
    - `x_gusto_api_version.enum(2024_04_01)` **Removed** (Breaking ⚠️)
    - `x_gusto_api_version.enum(2025_06_15)` **Added**
  * `response.[]` **Changed** (Breaking ⚠️)
    - `additional_properties` **Added**
    - `all_home_addresses` **Added**
    - `applicable_tax_ids` **Added**
    - `current_home_address` **Added**
    - `custom_fields[].description` **Changed** (Breaking ⚠️)
    - `department_uuid` **Added**
    - `eligible_paid_time_off[].accrual_balance` **Changed** (Breaking ⚠️)
    - `eligible_paid_time_off[].accrual_method` **Changed** (Breaking ⚠️)
    - `eligible_paid_time_off[].accrual_period` **Changed** (Breaking ⚠️)
    - `eligible_paid_time_off[].accrual_rate` **Changed** (Breaking ⚠️)
    - `eligible_paid_time_off[].accrual_unit` **Changed** (Breaking ⚠️)
    - `eligible_paid_time_off[].name` **Changed** (Breaking ⚠️)
    - `eligible_paid_time_off[].policy_name` **Changed** (Breaking ⚠️)
    - `eligible_paid_time_off[].policy_uuid` **Changed** (Breaking ⚠️)
    - `employee_code` **Added**
    - `flsa_status` **Added**
    - `hidden_ssn` **Added**
    - `hired_at` **Added**
    - `historical` **Added**
    - `jobs[].compensations[].title` **Added**
    - `jobs[].location_uuid` **Added**
    - `jobs[].location` **Added**
    - `member_portal_invitation_status` **Added**
    - `partner_portal_invitation_sent` **Added**
    - `title` **Added**
  * `errors[]` **Changed** (Breaking ⚠️)
    - `errors` **Removed** (Breaking ⚠️)
    - `metadata` **Removed** (Breaking ⚠️)
* `gusto_app_integration.employees.create()`: 
  * `request` **Changed** (Breaking ⚠️)
    - `email` **Changed**
    - `work_email` **Added**
    - `x_gusto_api_version.enum(2024_04_01)` **Removed** (Breaking ⚠️)
    - `x_gusto_api_version.enum(2025_06_15)` **Added**
  * `response` **Changed** (Breaking ⚠️)
    - `applicable_tax_ids` **Added**
    - `custom_fields[].description` **Changed** (Breaking ⚠️)
    - `department_uuid` **Added**
    - `eligible_paid_time_off[].accrual_balance` **Changed** (Breaking ⚠️)
    - `eligible_paid_time_off[].accrual_method` **Changed** (Breaking ⚠️)
    - `eligible_paid_time_off[].accrual_period` **Changed** (Breaking ⚠️)
    - `eligible_paid_time_off[].accrual_rate` **Changed** (Breaking ⚠️)
    - `eligible_paid_time_off[].accrual_unit` **Changed** (Breaking ⚠️)
    - `eligible_paid_time_off[].name` **Changed** (Breaking ⚠️)
    - `eligible_paid_time_off[].policy_name` **Changed** (Breaking ⚠️)
    - `eligible_paid_time_off[].policy_uuid` **Changed** (Breaking ⚠️)
    - `employee_code` **Added**
    - `flsa_status` **Added**
    - `hidden_ssn` **Added**
    - `hired_at` **Added**
    - `historical` **Added**
    - `jobs[].compensations[].title` **Added**
    - `jobs[].location_uuid` **Added**
    - `jobs[].location` **Added**
    - `member_portal_invitation_status` **Added**
    - `partner_portal_invitation_sent` **Added**
    - `title` **Added**
  * `errors[]` **Changed** (Breaking ⚠️)
    - `errors` **Removed** (Breaking ⚠️)
    - `metadata` **Removed** (Breaking ⚠️)
* `gusto_app_integration.employees.get_by_id()`: 
  * `request` **Changed** (Breaking ⚠️)
    - `include[].enum(all_home_addresses)` **Added**
    - `include[].enum(current_home_address)` **Added**
    - `include[].enum(portal_invitations)` **Added**
    - `x_gusto_api_version.enum(2024_04_01)` **Removed** (Breaking ⚠️)
    - `x_gusto_api_version.enum(2025_06_15)` **Added**
  * `response` **Changed** (Breaking ⚠️)
    - `applicable_tax_ids` **Added**
    - `custom_fields[].description` **Changed** (Breaking ⚠️)
    - `department_uuid` **Added**
    - `eligible_paid_time_off[].accrual_balance` **Changed** (Breaking ⚠️)
    - `eligible_paid_time_off[].accrual_method` **Changed** (Breaking ⚠️)
    - `eligible_paid_time_off[].accrual_period` **Changed** (Breaking ⚠️)
    - `eligible_paid_time_off[].accrual_rate` **Changed** (Breaking ⚠️)
    - `eligible_paid_time_off[].accrual_unit` **Changed** (Breaking ⚠️)
    - `eligible_paid_time_off[].name` **Changed** (Breaking ⚠️)
    - `eligible_paid_time_off[].policy_name` **Changed** (Breaking ⚠️)
    - `eligible_paid_time_off[].policy_uuid` **Changed** (Breaking ⚠️)
    - `employee_code` **Added**
    - `flsa_status` **Added**
    - `hidden_ssn` **Added**
    - `hired_at` **Added**
    - `historical` **Added**
    - `jobs[].compensations[].title` **Added**
    - `jobs[].location_uuid` **Added**
    - `jobs[].location` **Added**
    - `member_portal_invitation_status` **Added**
    - `partner_portal_invitation_sent` **Added**
    - `title` **Added**
  *  `error.status[404]` **Added**
* `gusto_app_integration.employees.update()`: 
  * `request` **Changed** (Breaking ⚠️)
    - `work_email` **Added**
    - `x_gusto_api_version` **Changed** (Breaking ⚠️)
  * `response` **Changed** (Breaking ⚠️)
    - `applicable_tax_ids` **Added**
    - `custom_fields[].description` **Changed** (Breaking ⚠️)
    - `department_uuid` **Added**
    - `eligible_paid_time_off[].accrual_balance` **Changed** (Breaking ⚠️)
    - `eligible_paid_time_off[].accrual_method` **Changed** (Breaking ⚠️)
    - `eligible_paid_time_off[].accrual_period` **Changed** (Breaking ⚠️)
    - `eligible_paid_time_off[].accrual_rate` **Changed** (Breaking ⚠️)
    - `eligible_paid_time_off[].accrual_unit` **Changed** (Breaking ⚠️)
    - `eligible_paid_time_off[].name` **Changed** (Breaking ⚠️)
    - `eligible_paid_time_off[].policy_name` **Changed** (Breaking ⚠️)
    - `eligible_paid_time_off[].policy_uuid` **Changed** (Breaking ⚠️)
    - `employee_code` **Added**
    - `flsa_status` **Added**
    - `hidden_ssn` **Added**
    - `hired_at` **Added**
    - `historical` **Added**
    - `jobs[].compensations[].title` **Added**
    - `jobs[].location_uuid` **Added**
    - `jobs[].location` **Added**
    - `member_portal_invitation_status` **Added**
    - `partner_portal_invitation_sent` **Added**
    - `title` **Added**
  * `errors[]` **Changed** (Breaking ⚠️)
    - `errors` **Removed** (Breaking ⚠️)
    - `metadata` **Removed** (Breaking ⚠️)
* `gusto_app_integration.employees.delete()`: 
  * `request.x_gusto_api_version` **Changed** (Breaking ⚠️)
    - `enum(2024_04_01)` **Removed** (Breaking ⚠️)
    - `enum(2025_06_15)` **Added**
  * `error` **Changed**
    - `` **Added**
* `gusto_app_integration.employees.get_custom_fields()`: 
  * `request.x_gusto_api_version` **Changed** (Breaking ⚠️)
    - `enum(2024_04_01)` **Removed** (Breaking ⚠️)
    - `enum(2025_06_15)` **Added**
  *  `response.custom_fields[].description` **Changed** (Breaking ⚠️)
  *  `error.status[404]` **Added**
* `gusto_app_integration.employees.get_time_off_activities()`: 
  * `request.x_gusto_api_version` **Changed** (Breaking ⚠️)
    - `enum(2024_04_01)` **Removed** (Breaking ⚠️)
    - `enum(2025_06_15)` **Added**
  *  `response` **Changed** (Breaking ⚠️)
  * `error` **Changed**
    - `` **Added**
    - `status[422]` **Added**
* `gusto_app_integration.employee_employments.create_termination()`: 
  * `request` **Changed** (Breaking ⚠️)
    - `run_termination_payroll` **Changed**
    - `x_gusto_api_version.enum(2024_04_01)` **Removed** (Breaking ⚠️)
    - `x_gusto_api_version.enum(2025_06_15)` **Added**
  *  `error.status[404]` **Added**
* `gusto_app_integration.departments.create()`: 
  * `request` **Changed** (Breaking ⚠️)
    - `title` **Changed** (Breaking ⚠️)
    - `x_gusto_api_version.enum(2024_04_01)` **Removed** (Breaking ⚠️)
    - `x_gusto_api_version.enum(2025_06_15)` **Added**
  *  `error.status[404]` **Added**
* `gusto_app_integration.departments.get_all()`: 
  * `request.x_gusto_api_version` **Changed** (Breaking ⚠️)
    - `enum(2024_04_01)` **Removed** (Breaking ⚠️)
    - `enum(2025_06_15)` **Added**
  *  `error.status[404]` **Added**
* `gusto_app_integration.departments.get()`: 
  * `request.x_gusto_api_version` **Changed** (Breaking ⚠️)
    - `enum(2024_04_01)` **Removed** (Breaking ⚠️)
    - `enum(2025_06_15)` **Added**
  *  `error.status[404]` **Added**
* `gusto_app_integration.departments.update()`: 
  * `request` **Changed** (Breaking ⚠️)
    - `title` **Changed** (Breaking ⚠️)
    - `x_gusto_api_version.enum(2024_04_01)` **Removed** (Breaking ⚠️)
    - `x_gusto_api_version.enum(2025_06_15)` **Added**
  * `error` **Changed**
    - `` **Added**
    - `status[409]` **Added**
* `gusto_app_integration.departments.delete()`: 
  * `request.x_gusto_api_version` **Changed** (Breaking ⚠️)
    - `enum(2024_04_01)` **Removed** (Breaking ⚠️)
    - `enum(2025_06_15)` **Added**
  *  `error.status[404]` **Added**
* `gusto_app_integration.departments.add_people()`: 
  * `request` **Changed** (Breaking ⚠️)
    - `version` **Changed** (Breaking ⚠️)
    - `x_gusto_api_version.enum(2024_04_01)` **Removed** (Breaking ⚠️)
    - `x_gusto_api_version.enum(2025_06_15)` **Added**
  * `error` **Changed**
    - `` **Added**
    - `status[422]` **Added**
* `gusto_app_integration.departments.remove_people()`: 
  * `request` **Changed** (Breaking ⚠️)
    - `version` **Changed** (Breaking ⚠️)
    - `x_gusto_api_version.enum(2024_04_01)` **Removed** (Breaking ⚠️)
    - `x_gusto_api_version.enum(2025_06_15)` **Added**
  * `error` **Changed**
    - `` **Added**
    - `status[422]` **Added**
* `gusto_app_integration.employees.get_terminations()`: 
  * `request.x_gusto_api_version` **Changed** (Breaking ⚠️)
    - `enum(2024_04_01)` **Removed** (Breaking ⚠️)
    - `enum(2025_06_15)` **Added**
  *  `error.status[404]` **Added**
* `gusto_app_integration.employee_employments.delete_termination()`: 
  * `request.x_gusto_api_version` **Changed** (Breaking ⚠️)
    - `enum(2024_04_01)` **Removed** (Breaking ⚠️)
    - `enum(2025_06_15)` **Added**
  * `error` **Changed** (Breaking ⚠️)
    - `errors[].errors` **Removed** (Breaking ⚠️)
    - `errors[].metadata` **Removed** (Breaking ⚠️)
    - `status[422]` **Added**
* `gusto_app_integration.locations.update()`: 
  * `request.x_gusto_api_version` **Changed** (Breaking ⚠️)
    - `enum(2024_04_01)` **Removed** (Breaking ⚠️)
    - `enum(2025_06_15)` **Added**
  * `response` **Changed** (Breaking ⚠️)
    - `inactive` **Added**
    - `zip_code` **Added**
    - `zip` **Removed** (Breaking ⚠️)
  * `errors[]` **Changed** (Breaking ⚠️)
    - `errors` **Removed** (Breaking ⚠️)
    - `metadata` **Removed** (Breaking ⚠️)
* `gusto_app_integration.employee_employments.create_rehire()`: 
  * `request.x_gusto_api_version` **Changed** (Breaking ⚠️)
    - `enum(2024_04_01)` **Removed** (Breaking ⚠️)
    - `enum(2025_06_15)` **Added**
  *  `error.status[404]` **Added**
* `gusto_app_integration.employee_employments.update_rehire()`: 
  * `request.x_gusto_api_version` **Changed** (Breaking ⚠️)
    - `enum(2024_04_01)` **Removed** (Breaking ⚠️)
    - `enum(2025_06_15)` **Added**
  * `errors[]` **Changed** (Breaking ⚠️)
    - `errors` **Removed** (Breaking ⚠️)
    - `metadata` **Removed** (Breaking ⚠️)
* `gusto_app_integration.employee_employments.get_rehire()`: 
  * `request.x_gusto_api_version` **Changed** (Breaking ⚠️)
    - `enum(2024_04_01)` **Removed** (Breaking ⚠️)
    - `enum(2025_06_15)` **Added**
  *  `response.status[204]` **Added** (Breaking ⚠️)
  * `errors[]` **Changed** (Breaking ⚠️)
    - `errors` **Removed** (Breaking ⚠️)
    - `metadata` **Removed** (Breaking ⚠️)
* `gusto_app_integration.employee_employments.delete_rehire()`: 
  * `request.x_gusto_api_version` **Changed** (Breaking ⚠️)
    - `enum(2024_04_01)` **Removed** (Breaking ⚠️)
    - `enum(2025_06_15)` **Added**
  * `error` **Changed** (Breaking ⚠️)
    - `errors[].errors` **Removed** (Breaking ⚠️)
    - `errors[].metadata` **Removed** (Breaking ⚠️)
    - `status[422]` **Added**
* `gusto_app_integration.employee_employments.get_history()`: 
  * `request.x_gusto_api_version` **Changed** (Breaking ⚠️)
    - `enum(2024_04_01)` **Removed** (Breaking ⚠️)
    - `enum(2025_06_15)` **Added**
  *  `response.[].termination_date` **Changed** (Breaking ⚠️)
  * `errors[]` **Changed** (Breaking ⚠️)
    - `errors` **Removed** (Breaking ⚠️)
    - `metadata` **Removed** (Breaking ⚠️)
* `gusto_app_integration.employee_addresses.list_home_addresses()`: 
  * `request.x_gusto_api_version` **Changed** (Breaking ⚠️)
    - `enum(2024_04_01)` **Removed** (Breaking ⚠️)
    - `enum(2025_06_15)` **Added**
  * `response.[]` **Changed** (Breaking ⚠️)
    - `uuid` **Changed**
    - `version` **Changed**
    - `zip_code` **Added**
    - `zip` **Removed** (Breaking ⚠️)
  *  `error.status[404]` **Added**
* `gusto_app_integration.employee_addresses.create()`: 
  * `request` **Changed** (Breaking ⚠️)
    - `effective_date` **Changed**
    - `x_gusto_api_version.enum(2024_04_01)` **Removed** (Breaking ⚠️)
    - `x_gusto_api_version.enum(2025_06_15)` **Added**
  * `response` **Changed** (Breaking ⚠️)
    - `uuid` **Changed**
    - `version` **Changed**
    - `zip_code` **Added**
    - `zip` **Removed** (Breaking ⚠️)
  *  `error.status[404]` **Added**
* `gusto_app_integration.employee_addresses.get()`: 
  * `request.x_gusto_api_version` **Changed** (Breaking ⚠️)
    - `enum(2024_04_01)` **Removed** (Breaking ⚠️)
    - `enum(2025_06_15)` **Added**
  * `response` **Changed** (Breaking ⚠️)
    - `uuid` **Changed**
    - `version` **Changed**
    - `zip_code` **Added**
    - `zip` **Removed** (Breaking ⚠️)
  *  `error.status[404]` **Added**
* `gusto_app_integration.employee_addresses.update()`: 
  * `request` **Changed** (Breaking ⚠️)
    - `effective_date` **Changed**
    - `x_gusto_api_version.enum(2024_04_01)` **Removed** (Breaking ⚠️)
    - `x_gusto_api_version.enum(2025_06_15)` **Added**
  * `response` **Changed** (Breaking ⚠️)
    - `uuid` **Changed**
    - `version` **Changed**
    - `zip_code` **Added**
    - `zip` **Removed** (Breaking ⚠️)
  *  `error.status[404]` **Added**
* `gusto_app_integration.employee_addresses.delete_home_address()`: 
  * `request.x_gusto_api_version` **Changed** (Breaking ⚠️)
    - `enum(2024_04_01)` **Removed** (Breaking ⚠️)
    - `enum(2025_06_15)` **Added**
  *  `error.status[404]` **Added**
* `gusto_app_integration.employee_addresses.get_work_addresses()`: 
  * `request.x_gusto_api_version` **Changed** (Breaking ⚠️)
    - `enum(2024_04_01)` **Removed** (Breaking ⚠️)
    - `enum(2025_06_15)` **Added**
  * `response.[]` **Changed** (Breaking ⚠️)
    - `zip_code` **Added**
    - `zip` **Removed** (Breaking ⚠️)
  *  `error.status[404]` **Added**
* `gusto_app_integration.employee_addresses.create_work_address()`: 
  * `request.x_gusto_api_version` **Changed** (Breaking ⚠️)
    - `enum(2024_04_01)` **Removed** (Breaking ⚠️)
    - `enum(2025_06_15)` **Added**
  * `response` **Changed** (Breaking ⚠️)
    - `zip_code` **Added**
    - `zip` **Removed** (Breaking ⚠️)
  *  `error.status[404]` **Added**
* `gusto_app_integration.employee_addresses.get_work_address()`: 
  * `request.x_gusto_api_version` **Changed** (Breaking ⚠️)
    - `enum(2024_04_01)` **Removed** (Breaking ⚠️)
    - `enum(2025_06_15)` **Added**
  * `response` **Changed** (Breaking ⚠️)
    - `zip_code` **Added**
    - `zip` **Removed** (Breaking ⚠️)
  *  `error.status[404]` **Added**
* `gusto_app_integration.employee_addresses.update_work_address()`: 
  * `request.x_gusto_api_version` **Changed** (Breaking ⚠️)
    - `enum(2024_04_01)` **Removed** (Breaking ⚠️)
    - `enum(2025_06_15)` **Added**
  * `response` **Changed** (Breaking ⚠️)
    - `zip_code` **Added**
    - `zip` **Removed** (Breaking ⚠️)
  *  `error.status[404]` **Added**
* `gusto_app_integration.employee_addresses.delete_work_address()`: 
  * `request.x_gusto_api_version` **Changed** (Breaking ⚠️)
    - `enum(2024_04_01)` **Removed** (Breaking ⚠️)
    - `enum(2025_06_15)` **Added**
  *  `error.status[404]` **Added**
* `gusto_app_integration.jobs.create_compensation()`: 
  * `request` **Changed** (Breaking ⚠️)
    - `rate` **Changed** (Breaking ⚠️)
    - `title` **Added**
    - `x_gusto_api_version.enum(2024_04_01)` **Removed** (Breaking ⚠️)
    - `x_gusto_api_version.enum(2025_06_15)` **Added**
  *  `response.title` **Added**
  *  `error.status[404]` **Added**
* `gusto_app_integration.jobs_and_compensations.get_compensations_for_job()`: 
  * `request.x_gusto_api_version` **Changed** (Breaking ⚠️)
    - `enum(2024_04_01)` **Removed** (Breaking ⚠️)
    - `enum(2025_06_15)` **Added**
  *  `response.[].title` **Added**
  *  `error.status[404]` **Added**
* `gusto_app_integration.jobs_and_compensations.get_compensation()`: 
  * `request.x_gusto_api_version` **Changed** (Breaking ⚠️)
    - `enum(2024_04_01)` **Removed** (Breaking ⚠️)
    - `enum(2025_06_15)` **Added**
  *  `response.title` **Added**
  *  `error.status[404]` **Added**
* `gusto_app_integration.jobs_and_compensations.update_compensation()`: 
  * `request` **Changed** (Breaking ⚠️)
    - `effective_date` **Added**
    - `title` **Added**
    - `x_gusto_api_version.enum(2024_04_01)` **Removed** (Breaking ⚠️)
    - `x_gusto_api_version.enum(2025_06_15)` **Added**
  *  `response.title` **Added**
  *  `error.status[404]` **Added**
* `gusto_app_integration.jobs_and_compensations.delete_compensation()`: 
  * `request.x_gusto_api_version` **Changed** (Breaking ⚠️)
    - `enum(2024_04_01)` **Removed** (Breaking ⚠️)
    - `enum(2025_06_15)` **Added**
  * `error` **Changed**
    - `` **Added**
    - `status[422]` **Added**
* `gusto_app_integration.earning_types.create()`: 
  * `request` **Changed** (Breaking ⚠️)
    - `name` **Changed**
    - `x_gusto_api_version.enum(2024_04_01)` **Removed** (Breaking ⚠️)
    - `x_gusto_api_version.enum(2025_06_15)` **Added**
  *  `response.active` **Added**
  *  `error.status[404]` **Added**
* `gusto_app_integration.earning_types.get()`: 
  * `request.x_gusto_api_version` **Changed** (Breaking ⚠️)
    - `enum(2024_04_01)` **Removed** (Breaking ⚠️)
    - `enum(2025_06_15)` **Added**
  *  `response.default[].active` **Added**
  *  `error.status[404]` **Added**
* `gusto_app_integration.earning_types.update()`: 
  * `request.x_gusto_api_version` **Changed** (Breaking ⚠️)
    - `enum(2024_04_01)` **Removed** (Breaking ⚠️)
    - `enum(2025_06_15)` **Added**
  *  `response.active` **Added**
  *  `error.status[404]` **Added**
* `gusto_app_integration.earning_types.deactivate()`: `request.x_gusto_api_version` **Changed** (Breaking ⚠️)
    - `enum(2024_04_01)` **Removed** (Breaking ⚠️)
    - `enum(2025_06_15)` **Added**
* `gusto_app_integration.contractors.create()`: 
  * `request.x_gusto_api_version` **Changed** (Breaking ⚠️)
    - `enum(2024_04_01)` **Removed** (Breaking ⚠️)
    - `enum(2025_06_15)` **Added**
  * `response` **Changed** (Breaking ⚠️)
    - `address.zip_code` **Added**
    - `address.zip` **Removed** (Breaking ⚠️)
    - `department_title` **Added**
    - `department` **Added**
    - `dismissal_cancellation_eligible` **Added**
    - `dismissal_date` **Added**
    - `file_new_hire_report` **Changed** (Breaking ⚠️)
    - `member_portal_invitation_status` **Added**
    - `partner_portal_invitation_sent` **Added**
    - `rehire_cancellation_eligible` **Added**
    - `upcoming_employment` **Added**
  *  `error.status[404]` **Added**
* `gusto_app_integration.contractors.get()`: 
  * `request` **Changed** (Breaking ⚠️)
    - `include` **Added**
    - `onboarded_active` **Added**
    - `onboarded` **Added**
    - `sort_by` **Added**
    - `terminated_today` **Added**
    - `terminated` **Added**
    - `x_gusto_api_version.enum(2024_04_01)` **Removed** (Breaking ⚠️)
    - `x_gusto_api_version.enum(2025_06_15)` **Added**
  * `response.[]` **Changed** (Breaking ⚠️)
    - `address.zip_code` **Added**
    - `address.zip` **Removed** (Breaking ⚠️)
    - `department_title` **Added**
    - `department` **Added**
    - `dismissal_cancellation_eligible` **Added**
    - `dismissal_date` **Added**
    - `file_new_hire_report` **Changed** (Breaking ⚠️)
    - `member_portal_invitation_status` **Added**
    - `partner_portal_invitation_sent` **Added**
    - `rehire_cancellation_eligible` **Added**
    - `upcoming_employment` **Added**
  *  `error.status[404]` **Added**
* `gusto_app_integration.contractors.get_by_id()`: 
  * `request` **Changed** (Breaking ⚠️)
    - `include` **Added**
    - `x_gusto_api_version.enum(2024_04_01)` **Removed** (Breaking ⚠️)
    - `x_gusto_api_version.enum(2025_06_15)` **Added**
  * `response` **Changed** (Breaking ⚠️)
    - `address.zip_code` **Added**
    - `address.zip` **Removed** (Breaking ⚠️)
    - `department_title` **Added**
    - `department` **Added**
    - `dismissal_cancellation_eligible` **Added**
    - `dismissal_date` **Added**
    - `file_new_hire_report` **Changed** (Breaking ⚠️)
    - `member_portal_invitation_status` **Added**
    - `partner_portal_invitation_sent` **Added**
    - `rehire_cancellation_eligible` **Added**
    - `upcoming_employment` **Added**
  *  `error.status[404]` **Added**
* `gusto_app_integration.contractors.update()`: 
  * `request.x_gusto_api_version` **Changed** (Breaking ⚠️)
    - `enum(2024_04_01)` **Removed** (Breaking ⚠️)
    - `enum(2025_06_15)` **Added**
  * `response` **Changed** (Breaking ⚠️)
    - `address.zip_code` **Added**
    - `address.zip` **Removed** (Breaking ⚠️)
    - `department_title` **Added**
    - `department` **Added**
    - `dismissal_cancellation_eligible` **Added**
    - `dismissal_date` **Added**
    - `file_new_hire_report` **Changed** (Breaking ⚠️)
    - `member_portal_invitation_status` **Added**
    - `partner_portal_invitation_sent` **Added**
    - `rehire_cancellation_eligible` **Added**
    - `upcoming_employment` **Added**
  * `error` **Changed**
    - `` **Added**
    - `status[409]` **Added**
* `gusto_app_integration.webhooks.create()`: 
  * `request` **Changed** (Breaking ⚠️)
    - `subscription_types[].enum(payroll_sync)` **Added**
    - `subscription_types[].enum(people_batch)` **Added**
    - `x_gusto_api_version.enum(2024_04_01)` **Removed** (Breaking ⚠️)
    - `x_gusto_api_version.enum(2025_06_15)` **Added**
  *  `response.subscription_types[].enum(payroll_sync)` **Added** (Breaking ⚠️)
  *  `error.status[404]` **Removed** (Breaking ⚠️)
* `gusto_app_integration.webhooks.list_subscriptions()`: 
  * `request.x_gusto_api_version` **Changed** (Breaking ⚠️)
    - `enum(2024_04_01)` **Removed** (Breaking ⚠️)
    - `enum(2025_06_15)` **Added**
  *  `response.[].subscription_types[].enum(payroll_sync)` **Added** (Breaking ⚠️)
  *  `error.status[404]` **Removed** (Breaking ⚠️)
* `gusto_app_integration.webhooks.update_subscription()`: 
  * `request` **Changed** (Breaking ⚠️)
    - `subscription_types[].enum(payroll_sync)` **Added**
    - `subscription_types[].enum(people_batch)` **Added**
    - `x_gusto_api_version.enum(2024_04_01)` **Removed** (Breaking ⚠️)
    - `x_gusto_api_version.enum(2025_06_15)` **Added**
  *  `response.subscription_types[].enum(payroll_sync)` **Added** (Breaking ⚠️)
  *  `error.status[404]` **Added**
* `gusto_app_integration.webhooks.get_subscription()`: 
  * `request.x_gusto_api_version` **Changed** (Breaking ⚠️)
    - `enum(2024_04_01)` **Removed** (Breaking ⚠️)
    - `enum(2025_06_15)` **Added**
  *  `response.subscription_types[].enum(payroll_sync)` **Added** (Breaking ⚠️)
  *  `error.status[404]` **Added**
* `gusto_app_integration.reimbursements.get_v1_recurring_reimbursements()`: **Added**
* `gusto_app_integration.salary_estimates.get_v1_salary_estimates_occupations()`: **Added**
* `gusto_app_integration.contractor_payment_groups.preview()`: **Removed** (Breaking ⚠️)
* `gusto_app_integration.employee_employments.get_v1_terminations_employee_id()`: **Added**
* `gusto_app_integration.contractor_payment_groups.get()`: **Removed** (Breaking ⚠️)
* `gusto_app_integration.jobs_and_compensations.delete()`: **Removed** (Breaking ⚠️)
* `gusto_app_integration.jobs_and_compensations.update_job()`: **Removed** (Breaking ⚠️)
* `gusto_app_integration.jobs_and_compensations.get()`: **Removed** (Breaking ⚠️)
* `gusto_app_integration.jobs_and_compensations.get_jobs()`: **Removed** (Breaking ⚠️)
* `gusto_app_integration.jobs.create()`: **Removed** (Breaking ⚠️)
* `gusto_app_integration.introspection.refresh_access_token()`: **Removed** (Breaking ⚠️)
* `gusto_app_integration.reimbursements.delete_v1_recurring_reimbursements()`: **Added**
* `gusto_app_integration.reimbursements.put_v1_recurring_reimbursements()`: **Added**
* `gusto_app_integration.salary_estimates.put_v1_salary_estimates_id()`: **Added**
* `gusto_app_integration.reimbursements.post_v1_employees_employee_id_recurring_reimbursements()`: **Added**
* `gusto_app_integration.reimbursements.get_v1_employees_employee_id_recurring_reimbursements()`: **Added**
* `gusto_app_integration.time_tracking.post_companies_company_uuid_time_tracking_payroll_syncs()`: **Added**
* `gusto_app_integration.contractor_payment_groups.fetch()`: **Removed** (Breaking ⚠️)
* `gusto_app_integration.introspection.oauth_access_token()`: **Added**
* `gusto_app_integration.salary_estimates.post_v1_salary_estimates_uuid_accept()`: **Added**
* `gusto_app_integration.time_tracking.get_time_tracking_payroll_syncs_payroll_sync_uuid()`: **Added**
* `gusto_app_integration.time_off_requests.get_v1_companies_company_id_time_off_requests()`: **Added**
* `gusto_app_integration.notifications.get_company_notifications()`: **Added**
* `gusto_app_integration.salary_estimates.post_v1_employees_employee_id_salary_estimates()`: **Added**
* `gusto_app_integration.salary_estimates.get_v1_salary_estimates_id()`: **Added**
* `gusto_app_integration.employee_benefits.patch_v1_employees_employee_uuid_section603_high_earner_statuses_effective_year()`: **Added**
* `gusto_app_integration.employee_benefits.get_v1_employees_employee_uuid_section603_high_earner_statuses_effective_year()`: **Added**
* `gusto_app_integration.employee_benefits.post_v1_employees_employee_uuid_section603_high_earner_statuses()`: **Added**
* `gusto_app_integration.employee_benefits.get_v1_employees_employee_uuid_section603_high_earner_statuses()`: **Added**
* `gusto_app_integration.company_benefits.put_v1_company_benefits_company_benefit_id_contribution_exclusions()`: **Added**
* `gusto_app_integration.company_benefits.get_v1_company_benefits_company_benefit_id_contribution_exclusions()`: **Added**
* `gusto_app_integration.reports.post_v1_companies_company_id_reports_employees_annual_fica_wage()`: **Added**
* `gusto_app_integration.reports.get_reports_request_uuid()`: **Added**
* `gusto_app_integration.reports.post_payrolls_payroll_uuid_reports_general_ledger()`: **Added**
* `gusto_app_integration.time_off_policies.put_v1_time_off_policies_time_off_policy_uuid_add_employees()`: **Added**
* `gusto_app_integration.time_off_policies.get_v1_companies_company_uuid_time_off_policies()`: **Added**
* `gusto_app_integration.time_off_policies.get_v1_time_off_policies_time_off_policy_uuid()`: **Added**
* `gusto_app_integration.webhooks.get_v1_webhooks_health_check()`: **Added**
* `gusto_app_integration.contractors.get_v1_companies_company_id_contractors_payment_details()`: **Added**
