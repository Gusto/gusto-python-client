## Python SDK Changes:
* `gusto.pay_schedules.get_all()`: `response.[]` **Changed** (Breaking ⚠️)
    - `auto_payroll_enablement_blockers` **Removed** (Breaking ⚠️)
    - `auto_payroll` **Removed** (Breaking ⚠️)
    - `day_1` **Deprecated**
    - `day_2` **Deprecated**
    - `workweek_start_day` **Added**
* `gusto.payrolls.cancel()`: `response.pay_period` **Changed** (Breaking ⚠️)
    - `end_date` **Changed** (Breaking ⚠️)
    - `start_date` **Changed** (Breaking ⚠️)
* `gusto.payrolls.prepare()`: `response` **Changed** (Breaking ⚠️)
    - `employee_compensations[].custom_withholdings` **Added**
    - `employee_compensations[].fixed_compensations[].breakdowns` **Added**
    - `employee_compensations[].hourly_compensations[].breakdowns` **Added**
    - `employee_compensations[].paid_time_off[].approved_request_hours` **Added**
    - `pay_period.end_date` **Changed** (Breaking ⚠️)
    - `pay_period.start_date` **Changed** (Breaking ⚠️)
    - `workweeks` **Added**
* `gusto.payrolls.update()`: 
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
  *  `error.status[409]` **Added**
* `gusto.payrolls.get()`: `response` **Changed** (Breaking ⚠️)
    - `employee_compensations[].custom_withholdings` **Added**
    - `employee_compensations[].fixed_compensations[].breakdowns` **Added**
    - `employee_compensations[].hourly_compensations[].breakdowns` **Added**
    - `employee_compensations[].paid_time_off[].approved_request_hours` **Added**
    - `employee_compensations[].pay_adjustments` **Added**
    - `pay_period.end_date` **Changed** (Breaking ⚠️)
    - `pay_period.start_date` **Changed** (Breaking ⚠️)
* `gusto.payrolls.create_off_cycle()`: `response` **Changed** (Breaking ⚠️)
    - `employee_compensations[].custom_withholdings` **Added**
    - `employee_compensations[].fixed_compensations[].breakdowns` **Added**
    - `employee_compensations[].hourly_compensations[].breakdowns` **Added**
    - `employee_compensations[].paid_time_off[].approved_request_hours` **Added**
    - `pay_period.end_date` **Changed** (Breaking ⚠️)
    - `pay_period.start_date` **Changed** (Breaking ⚠️)
    - `workweeks` **Added**
* `gusto.payrolls.list()`: `response.[].pay_period` **Changed** (Breaking ⚠️)
    - `end_date` **Changed** (Breaking ⚠️)
    - `start_date` **Changed** (Breaking ⚠️)
* `gusto.webhooks.verify()`: `response.subscription_types[]` **Changed** (Breaking ⚠️)
    - `enum(time_off_request)` **Added** (Breaking ⚠️)
    - `enum(time_sheets_batch)` **Added** (Breaking ⚠️)
* `gusto.webhooks.update_subscription()`: 
  * `request.subscription_types[]` **Changed**
    - `enum(time_off_request)` **Added**
    - `enum(time_sheets_batch)` **Added**
  * `response.subscription_types[]` **Changed** (Breaking ⚠️)
    - `enum(time_off_request)` **Added** (Breaking ⚠️)
    - `enum(time_sheets_batch)` **Added** (Breaking ⚠️)
* `gusto.webhooks.get_subscription()`: `response.subscription_types[]` **Changed** (Breaking ⚠️)
    - `enum(time_off_request)` **Added** (Breaking ⚠️)
    - `enum(time_sheets_batch)` **Added** (Breaking ⚠️)
* `gusto.webhooks.create_subscription()`: 
  * `request.subscription_types[]` **Changed**
    - `enum(time_off_request)` **Added**
    - `enum(time_sheets_batch)` **Added**
  * `response.subscription_types[]` **Changed** (Breaking ⚠️)
    - `enum(time_off_request)` **Added** (Breaking ⚠️)
    - `enum(time_sheets_batch)` **Added** (Breaking ⚠️)
* `gusto.webhooks.list_subscriptions()`: `response.[].subscription_types[]` **Changed** (Breaking ⚠️)
    - `enum(time_off_request)` **Added** (Breaking ⚠️)
    - `enum(time_sheets_batch)` **Added** (Breaking ⚠️)
* `gusto.jobs_and_compensations.update()`: `response` **Changed** (Breaking ⚠️)
    - `current_compensation_uuid` **Changed** (Breaking ⚠️)
    - `location.warnings` **Added**
* `gusto.jobs_and_compensations.get_job()`: `response` **Changed** (Breaking ⚠️)
    - `current_compensation_uuid` **Changed** (Breaking ⚠️)
    - `location.warnings` **Added**
* `gusto.jobs_and_compensations.create_job()`: `response` **Changed** (Breaking ⚠️)
    - `current_compensation_uuid` **Changed** (Breaking ⚠️)
    - `location.warnings` **Added**
* `gusto.jobs_and_compensations.get_jobs()`: `response.[]` **Changed** (Breaking ⚠️)
    - `current_compensation_uuid` **Changed** (Breaking ⚠️)
    - `location.warnings` **Added**
* `gusto.historical_employees.update()`: `response.jobs[]` **Changed** (Breaking ⚠️)
    - `current_compensation_uuid` **Changed** (Breaking ⚠️)
    - `location.warnings` **Added**
* `gusto.employees.update()`: `response.jobs[]` **Changed** (Breaking ⚠️)
    - `current_compensation_uuid` **Changed** (Breaking ⚠️)
    - `location.warnings` **Added**
* `gusto.employees.get()`: `response` **Changed** (Breaking ⚠️)
    - `additional_properties` **Added**
    - `all_home_addresses` **Added**
    - `company_name` **Added**
    - `current_home_address` **Added**
    - `jobs[].current_compensation_uuid` **Changed** (Breaking ⚠️)
    - `jobs[].location.warnings` **Added**
* `gusto.employees.create_historical()`: `response.jobs[]` **Changed** (Breaking ⚠️)
    - `current_compensation_uuid` **Changed** (Breaking ⚠️)
    - `location.warnings` **Added**
* `gusto.employees.create()`: `response.jobs[]` **Changed** (Breaking ⚠️)
    - `current_compensation_uuid` **Changed** (Breaking ⚠️)
    - `location.warnings` **Added**
* `gusto.employees.list()`: `response.[]` **Changed** (Breaking ⚠️)
    - `company_name` **Added**
    - `jobs[].current_compensation_uuid` **Changed** (Breaking ⚠️)
    - `jobs[].location.warnings` **Added**
* `gusto.tax_payments.get_tax_payment()`: **Added**
* `gusto.member_portal_invitations.post_v1_employees_employee_id_member_portal_invitations()`: **Added**
* `gusto.contractor_payments.fund()`: **Removed** (Breaking ⚠️)
* `gusto.contractor_payments.list()`: **Removed** (Breaking ⚠️)
* `gusto.contractor_payments.create()`: **Removed** (Breaking ⚠️)
* `gusto.contractor_payments.get()`: **Removed** (Breaking ⚠️)
* `gusto.contractor_payments.delete()`: **Removed** (Breaking ⚠️)
* `gusto.contractor_payments.preview()`: **Removed** (Breaking ⚠️)
* `gusto.contractor_payments.get_v1_contractor_payments_contractor_payment_id_pdf()`: **Removed** (Breaking ⚠️)
* `gusto.companies.suspensions.suspend()`: `request.leaving_for` **Changed**
    - `enum(other_peo)` **Added**
    - `enum(rippling_peo)` **Added**
    - `enum(sequoia_one)` **Added**
    - `enum(toast)` **Added**
* `gusto.federal_tax_details.update()`:  `error.status[403]` **Added**
* `gusto.locations.get()`:  `response.[].warnings` **Added**
* `gusto.locations.create()`:  `response.warnings` **Added**
* `gusto.locations.retrieve()`:  `response.warnings` **Added**
* `gusto.locations.update()`:  `response.warnings` **Added**
* `gusto.companies.put_v1_partner_managed_companies_company_uuid_disassociate()`: **Added**
* `gusto.pay_schedules.create()`: 
  * `request` **Changed**
    - `day_1` **Deprecated**
    - `day_2` **Deprecated**
    - `first_pay_period_end_day` **Added**
    - `first_pay_period_pay_day` **Added**
    - `second_pay_period_end_day` **Added**
    - `second_pay_period_pay_day` **Added**
    - `workweek_start_day` **Added**
  * `response` **Changed**
    - `day_1` **Deprecated**
    - `day_2` **Deprecated**
    - `first_pay_period_end_day` **Added**
    - `first_pay_period_pay_day` **Added**
    - `second_pay_period_end_day` **Added**
    - `second_pay_period_pay_day` **Added**
    - `workweek_start_day` **Added**
* `gusto.pay_schedules.get_preview()`: `request` **Changed**
    - `day_1` **Deprecated**
    - `day_2` **Deprecated**
    - `first_pay_period_end_day` **Added**
    - `first_pay_period_pay_day` **Added**
    - `pay_schedule_uuid` **Added**
    - `second_pay_period_end_day` **Added**
    - `second_pay_period_pay_day` **Added**
* `gusto.pay_schedules.get()`: `response` **Changed**
    - `day_1` **Deprecated**
    - `day_2` **Deprecated**
    - `first_pay_period_end_day` **Added**
    - `first_pay_period_pay_day` **Added**
    - `second_pay_period_end_day` **Added**
    - `second_pay_period_pay_day` **Added**
    - `workweek_start_day` **Added**
* `gusto.pay_schedules.update()`: 
  * `request` **Changed**
    - `day_1` **Deprecated**
    - `day_2` **Deprecated**
    - `first_pay_period_end_day` **Added**
    - `first_pay_period_pay_day` **Added**
    - `second_pay_period_end_day` **Added**
    - `second_pay_period_pay_day` **Added**
    - `workweek_start_day` **Added**
  * `response` **Changed**
    - `day_1` **Deprecated**
    - `day_2` **Deprecated**
    - `first_pay_period_end_day` **Added**
    - `first_pay_period_pay_day` **Added**
    - `second_pay_period_end_day` **Added**
    - `second_pay_period_pay_day` **Added**
    - `workweek_start_day` **Added**
* `gusto.tax_payments.get_tax_payments()`: **Added**
* `gusto.reverse_wire_transactions.get_reverse_wire_transactions()`: **Added**
* `gusto.payroll_cancellations.get_v1_payroll_batches_payroll_batch_uuid()`: **Added**
* `gusto.payroll_cancellations.post_v1_payroll_batches()`: **Added**
* `gusto.member_portal_invitations.delete_v1_contractors_contractor_uuid_member_portal_invitations()`: **Added**
* `gusto.employees.get_onboarding_status()`:  `response.blockers` **Added**
* `gusto.employees.update_onboarding_status()`:  `response.blockers` **Added**
* `gusto.member_portal_invitations.get_v1_contractors_contractor_uuid_member_portal_invitations()`: **Added**
* `gusto.employee_addresses.get()`:  `response.[].warnings` **Added**
* `gusto.employee_addresses.create()`:  `response.warnings` **Added**
* `gusto.employee_addresses.retrieve_home_address()`:  `response.warnings` **Added**
* `gusto.employee_addresses.update()`:  `response.warnings` **Added**
* `gusto.member_portal_invitations.post_v1_contractors_contractor_uuid_member_portal_invitations()`: **Added**
* `gusto.member_portal_invitations.delete_v1_employees_employee_id_member_portal_invitations()`: **Added**
* `gusto.member_portal_invitations.get_v1_employees_employee_id_member_portal_invitations()`: **Added**
* `gusto.contractor_payments.get_receipt()`: **Removed** (Breaking ⚠️)
* `gusto.earning_types.list()`: `response.default[]` **Changed**
    - `category` **Added**
    - `included_in_overtime_pay` **Added**
* `gusto.earning_types.create()`: 
  * `request` **Changed**
    - `category` **Added**
    - `included_in_overtime_pay` **Added**
  * `response` **Changed**
    - `category` **Added**
    - `included_in_overtime_pay` **Added**
* `gusto.earning_types.update()`: 
  * `request` **Changed**
    - `category` **Added**
    - `included_in_overtime_pay` **Added**
  * `response` **Changed**
    - `category` **Added**
    - `included_in_overtime_pay` **Added**
* `gusto.contractors.list()`: `response.[]` **Changed**
    - `additional_properties` **Added**
    - `company_name` **Added**
    - `work_email` **Added**
* `gusto.contractors.create()`: 
  *  `request.work_email` **Added**
  *  `response.work_email` **Added**
* `gusto.contractors.get()`: `response` **Changed**
    - `additional_properties` **Added**
    - `company_name` **Added**
    - `work_email` **Added**
* `gusto.contractors.update()`: 
  *  `request.work_email` **Added**
  *  `response.work_email` **Added**
* `gusto.contractors.get_address()`:  `response.warnings` **Added**
* `gusto.contractors.update_address()`:  `response.warnings` **Added**
* `gusto.contractors.post_v1_contractors_contractor_uuid_rehire()`:  `error.status[422]` **Added**
* `gusto.contractors.delete_v1_contractors_contractor_uuid_rehire()`:  `error.status[422]` **Added**
* `gusto.contractors.post_v1_contractors_contractor_uuid_termination()`:  `error.status[422]` **Added**
* `gusto.contractors.delete_v1_contractors_contractor_uuid_termination()`:  `error.status[422]` **Added**
* `gusto.contractor_payments.fund()`: **Added**
* `gusto.contractor_payments.get_receipt()`: **Added**
* `gusto.contractor_payments.preview()`: **Added**
* `gusto.contractor_payments.delete()`: **Added**
* `gusto.contractor_payments.get()`: **Added**
* `gusto.contractor_payments.create()`: **Added**
* `gusto.contractor_payments.list()`: **Added**
* `gusto.payrolls.get_approved_reversals()`:  `request.x_gusto_api_version` **Changed**
* `gusto.contractor_payments.get_v1_contractor_payments_contractor_payment_id_pdf()`: **Added**
* `gusto.contractor_payments.get_v1_contractors_contractor_uuid_payments()`: **Added**
* `gusto.reports.get_v1_bulk_reports_request_uuid()`: **Added**
* `gusto.payrolls.get_receipt()`: `request` **Changed**
    - `page` **Added**
    - `per` **Added**
* `gusto.payrolls.skip()`:  `error.status[409]` **Added**
* `gusto.reports.post_v1_bulk_reports()`: **Added**
* `gusto.time_off_policies.add_employees()`:  `error.status[409]` **Added**
* `gusto.time_off_policies.remove_employees()`:  `error.status[409]` **Added**
* `gusto.contractor_payment_groups.patch_v1_contractor_payment_groups_id_partner_disbursements()`: 
  * `request.disbursements[].payment_method` **Changed**
    - `enum(correction_payment)` **Added**
    - `enum(historical_payment)` **Added**
* `gusto.generated_documents.get()`:  `request.x_gusto_api_version` **Changed**
* `gusto.reports.create_custom()`: `request` **Changed**
    - `columns[].enum(additional_earnings)` **Added**
    - `columns[].enum(employee_state_income_tax)` **Added**
    - `date_filter_type` **Added**
    - `groupings` **Changed**
* `gusto.tax_requirements.get()`: `response.requirement_sets[].requirements[]` **Changed**
    - `default_value_applied` **Added**
    - `payroll_blocking` **Added**
