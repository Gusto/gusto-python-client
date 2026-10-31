## Python SDK Changes:
* `gusto_app_integration.employees.get_by_id()`: `response` **Changed** (Breaking ⚠️)
    - `additional_properties` **Added**
    - `all_home_addresses` **Added**
    - `company_name` **Added**
    - `current_home_address` **Added**
    - `jobs[].current_compensation_uuid` **Changed** (Breaking ⚠️)
    - `jobs[].location.warnings` **Added**
* `gusto_app_integration.payrolls.prepare()`: `response` **Changed** (Breaking ⚠️)
    - `employee_compensations[].custom_withholdings` **Added**
    - `employee_compensations[].fixed_compensations[].breakdowns` **Added**
    - `employee_compensations[].hourly_compensations[].breakdowns` **Added**
    - `employee_compensations[].paid_time_off[].approved_request_hours` **Added**
    - `pay_period.end_date` **Changed** (Breaking ⚠️)
    - `pay_period.start_date` **Changed** (Breaking ⚠️)
    - `workweeks` **Added**
* `gusto_app_integration.payrolls.get_for_company()`: `response.[].pay_period` **Changed** (Breaking ⚠️)
    - `end_date` **Changed** (Breaking ⚠️)
    - `start_date` **Changed** (Breaking ⚠️)
* `gusto_app_integration.payrolls.update()`: 
  * `request.employee_compensations[]` **Changed**
    - `custom_withholdings` **Added**
    - `fixed_compensations[].breakdowns` **Added**
    - `hourly_compensations[].breakdowns` **Added**
  * `response` **Changed** (Breaking ⚠️)
    - `employee_compensations[].custom_withholdings` **Added**
    - `employee_compensations[].fixed_compensations[].breakdowns` **Added**
    - `employee_compensations[].hourly_compensations[].breakdowns` **Added**
    - `employee_compensations[].paid_time_off[].approved_request_hours` **Added**
    - `pay_period.end_date` **Changed** (Breaking ⚠️)
    - `pay_period.start_date` **Changed** (Breaking ⚠️)
    - `workweeks` **Added**
  * `errors[]` **Changed** (Breaking ⚠️)
    - `errors` **Removed** (Breaking ⚠️)
    - `metadata` **Removed** (Breaking ⚠️)
* `gusto_app_integration.payrolls.get()`: `response` **Changed** (Breaking ⚠️)
    - `employee_compensations[].benefits[].company_contribution` **Changed** (Breaking ⚠️)
    - `employee_compensations[].benefits[].employee_deduction` **Changed** (Breaking ⚠️)
    - `employee_compensations[].custom_withholdings` **Added**
    - `employee_compensations[].deductions[].amount` **Changed** (Breaking ⚠️)
    - `employee_compensations[].fixed_compensations[].breakdowns` **Added**
    - `employee_compensations[].hourly_compensations[].breakdowns` **Added**
    - `employee_compensations[].paid_time_off[].approved_request_hours` **Added**
    - `employee_compensations[].pay_adjustments` **Added**
    - `employee_compensations[].taxes[].amount` **Changed** (Breaking ⚠️)
    - `pay_period.end_date` **Changed** (Breaking ⚠️)
    - `pay_period.start_date` **Changed** (Breaking ⚠️)
* `gusto_app_integration.pay_schedules.list()`: `response.[]` **Changed** (Breaking ⚠️)
    - `auto_payroll_enablement_blockers` **Removed** (Breaking ⚠️)
    - `workweek_start_day` **Added**
* `gusto_app_integration.employees.create()`: `response.jobs[]` **Changed** (Breaking ⚠️)
    - `current_compensation_uuid` **Changed** (Breaking ⚠️)
    - `location.warnings` **Added**
* `gusto_app_integration.employees.get()`: `response.[]` **Changed** (Breaking ⚠️)
    - `company_name` **Added**
    - `jobs[].current_compensation_uuid` **Changed** (Breaking ⚠️)
    - `jobs[].location.warnings` **Added**
* `gusto_app_integration.employees.update()`: `response.jobs[]` **Changed** (Breaking ⚠️)
    - `current_compensation_uuid` **Changed** (Breaking ⚠️)
    - `location.warnings` **Added**
* `gusto_app_integration.introspection.revoke()`:  `request.x_gusto_api_version` **Changed**
* `gusto_app_integration.locations.update()`:  `response.warnings` **Added**
* `gusto_app_integration.earning_types.create()`: 
  * `request` **Changed**
    - `category` **Added**
    - `included_in_overtime_pay` **Added**
  * `response` **Changed**
    - `category` **Added**
    - `included_in_overtime_pay` **Added**
* `gusto_app_integration.earning_types.update()`: 
  * `request` **Changed**
    - `category` **Added**
    - `included_in_overtime_pay` **Added**
  * `response` **Changed**
    - `category` **Added**
    - `included_in_overtime_pay` **Added**
* `gusto_app_integration.time_tracking.post_companies_company_uuid_time_tracking_time_sheets_batches()`: **Added**
* `gusto_app_integration.contractors.create()`: 
  *  `request.work_email` **Added**
  *  `response.work_email` **Added**
* `gusto_app_integration.contractors.get()`: `response.[]` **Changed**
    - `additional_properties` **Added**
    - `company_name` **Added**
    - `work_email` **Added**
* `gusto_app_integration.contractors.update()`: 
  *  `request.work_email` **Added**
  *  `response.work_email` **Added**
* `gusto_app_integration.employee_addresses.list_home_addresses()`:  `response.[].warnings` **Added**
* `gusto_app_integration.employee_addresses.create()`:  `response.warnings` **Added**
* `gusto_app_integration.employee_addresses.get()`:  `response.warnings` **Added**
* `gusto_app_integration.employee_addresses.update()`:  `response.warnings` **Added**
* `gusto_app_integration.locations.get()`:  `response.warnings` **Added**
* `gusto_app_integration.earning_types.get()`: `response.default[]` **Changed**
    - `category` **Added**
    - `included_in_overtime_pay` **Added**
* `gusto_app_integration.locations.create()`:  `response.warnings` **Added**
* `gusto_app_integration.company_locations.list()`:  `response.[].warnings` **Added**
* `gusto_app_integration.contractors.get_by_id()`: `response` **Changed**
    - `additional_properties` **Added**
    - `company_name` **Added**
    - `work_email` **Added**
* `gusto_app_integration.pay_schedules.get()`:  `response.workweek_start_day` **Added**
* `gusto_app_integration.companies.provision()`:  `request.x_gusto_api_version` **Changed**
* `gusto_app_integration.reports.post_v1_companies_company_id_reports_employees_annual_fica_wage()`: **Removed** (Breaking ⚠️)
* `gusto_app_integration.contractors.get_v1_companies_company_id_contractors_payment_details()`: **Removed** (Breaking ⚠️)
* `gusto_app_integration.time_tracking.get_time_tracking_time_sheets_batches_time_sheets_batch_uuid()`: **Added**
* `gusto_app_integration.webhooks.list_subscriptions()`: `response.[].subscription_types[]` **Changed**
    - `enum(time_off_request)` **Added**
    - `enum(time_sheets_batch)` **Added**
* `gusto_app_integration.webhooks.create()`: 
  * `request.subscription_types[]` **Changed**
    - `enum(time_off_request)` **Added**
    - `enum(time_sheets_batch)` **Added**
  * `response.subscription_types[]` **Changed**
    - `enum(time_off_request)` **Added**
    - `enum(time_sheets_batch)` **Added**
* `gusto_app_integration.webhooks.get_subscription()`: `response.subscription_types[]` **Changed**
    - `enum(time_off_request)` **Added**
    - `enum(time_sheets_batch)` **Added**
* `gusto_app_integration.webhooks.update_subscription()`: 
  * `request.subscription_types[]` **Changed**
    - `enum(time_off_request)` **Added**
    - `enum(time_sheets_batch)` **Added**
  * `response.subscription_types[]` **Changed**
    - `enum(time_off_request)` **Added**
    - `enum(time_sheets_batch)` **Added**
* `gusto_app_integration.webhooks.verify()`: `response.subscription_types[]` **Changed**
    - `enum(time_off_request)` **Added**
    - `enum(time_sheets_batch)` **Added**
