## Python SDK Changes:
* `gusto.payrolls.get()`: `response.employee_compensations[]` **Changed** (Breaking ⚠️)
    - `benefits[].company_contribution` **Changed** (Breaking ⚠️)
    - `benefits[].employee_deduction` **Changed** (Breaking ⚠️)
    - `custom_withholdings` **Added**
    - `deductions[].amount` **Changed** (Breaking ⚠️)
    - `taxes[].amount` **Changed** (Breaking ⚠️)
* `gusto.payrolls.create_off_cycle()`: 
  *  `request.employee_uuids` **Changed** (Breaking ⚠️)
  *  `response.employee_compensations[].custom_withholdings` **Added**
* `gusto.contractors.post_v1_contractors_contractor_uuid_rehire()`:  `error.status[422]` **Added**
* `gusto.contractors.list()`:  `response.[].work_email` **Added**
* `gusto.contractor_payments.get_v1_contractor_payments_contractor_payment_id_pdf()`: **Added**
* `gusto.contractor_payments.list()`: **Added**
* `gusto.contractor_payments.create()`: **Added**
* `gusto.contractor_payments.get()`: **Added**
* `gusto.contractors.post_v1_contractors_contractor_uuid_termination()`:  `error.status[422]` **Added**
* `gusto.contractor_payments.preview()`: **Added**
* `gusto.contractor_payments.get_receipt()`: **Added**
* `gusto.contractor_payments.fund()`: **Added**
* `gusto.member_portal_invitations.post_v1_employees_employee_id_member_portal_invitations()`: **Added**
* `gusto.member_portal_invitations.get_v1_employees_employee_id_member_portal_invitations()`: **Added**
* `gusto.member_portal_invitations.delete_v1_employees_employee_id_member_portal_invitations()`: **Added**
* `gusto.member_portal_invitations.post_v1_contractors_contractor_uuid_member_portal_invitations()`: **Added**
* `gusto.companies.put_v1_partner_managed_companies_company_uuid_disassociate()`: **Added**
* `gusto.member_portal_invitations.delete_v1_contractors_contractor_uuid_member_portal_invitations()`: **Added**
* `gusto.payroll_cancellations.post_v1_payroll_batches()`: **Added**
* `gusto.payroll_cancellations.get_v1_payroll_batches_payroll_batch_uuid()`: **Added**
* `gusto.reverse_wire_transactions.get_reverse_wire_transactions()`: **Added**
* `gusto.tax_payments.get_tax_payments()`: **Added**
* `gusto.tax_payments.get_tax_payment()`: **Added**
* `gusto.contractor_payments.list()`: **Removed** (Breaking ⚠️)
* `gusto.contractor_payments.create()`: **Removed** (Breaking ⚠️)
* `gusto.contractor_payments.get()`: **Removed** (Breaking ⚠️)
* `gusto.contractor_payments.delete()`: **Removed** (Breaking ⚠️)
* `gusto.contractor_payments.preview()`: **Removed** (Breaking ⚠️)
* `gusto.contractor_payments.get_receipt()`: **Removed** (Breaking ⚠️)
* `gusto.contractor_payments.fund()`: **Removed** (Breaking ⚠️)
* `gusto.contractor_payments.get_v1_contractor_payments_contractor_payment_id_pdf()`: **Removed** (Breaking ⚠️)
* `gusto.companies.suspensions.suspend()`: `request.leaving_for` **Changed**
    - `enum(other_peo)` **Added**
    - `enum(toast)` **Added**
* `gusto.tax_requirements.get()`: `response.requirement_sets[].requirements[]` **Changed**
    - `default_value_applied` **Added**
    - `payroll_blocking` **Added**
* `gusto.federal_tax_details.update()`:  `error.status[403]` **Added**
* `gusto.jobs_and_compensations.get_job()`:  `response.location.warnings` **Added**
* `gusto.jobs_and_compensations.update()`:  `response.location.warnings` **Added**
* `gusto.jobs_and_compensations.get_jobs()`:  `response.[].location.warnings` **Added**
* `gusto.jobs_and_compensations.create_job()`:  `response.location.warnings` **Added**
* `gusto.contractors.get_address()`:  `response.warnings` **Added**
* `gusto.contractors.update_address()`:  `response.warnings` **Added**
* `gusto.member_portal_invitations.get_v1_contractors_contractor_uuid_member_portal_invitations()`: **Added**
* `gusto.contractor_payments.get_v1_contractors_contractor_uuid_payments()`: **Added**
* `gusto.contractor_payments.delete()`: **Added**
* `gusto.contractors.delete_v1_contractors_contractor_uuid_termination()`:  `error.status[422]` **Added**
* `gusto.contractors.get()`:  `response.work_email` **Added**
* `gusto.contractors.update()`: 
  *  `request.work_email` **Added**
  *  `response.work_email` **Added**
* `gusto.contractors.delete_v1_contractors_contractor_uuid_rehire()`:  `error.status[422]` **Added**
* `gusto.contractors.create()`: 
  *  `request.work_email` **Added**
  *  `response.work_email` **Added**
* `gusto.contractor_payment_groups.patch_v1_contractor_payment_groups_id_partner_disbursements()`: 
  * `request.disbursements[].payment_method` **Changed**
    - `enum(correction_payment)` **Added**
    - `enum(historical_payment)` **Added**
* `gusto.employees.get()`:  `response.jobs[].location.warnings` **Added**
* `gusto.employees.update()`:  `response.jobs[].location.warnings` **Added**
* `gusto.employees.list()`:  `response.[].jobs[].location.warnings` **Added**
* `gusto.employees.create()`:  `response.jobs[].location.warnings` **Added**
* `gusto.employees.get_onboarding_status()`:  `response.blockers` **Added**
* `gusto.employees.update_onboarding_status()`:  `response.blockers` **Added**
* `gusto.employees.create_historical()`:  `response.jobs[].location.warnings` **Added**
* `gusto.reports.create_custom()`: `request` **Changed**
    - `columns[].enum(additional_earnings)` **Added**
    - `columns[].enum(employee_state_income_tax)` **Added**
    - `date_filter_type` **Added**
    - `groupings` **Changed**
* `gusto.payrolls.get_approved_reversals()`:  `request.x_gusto_api_version` **Changed**
* `gusto.reports.get_v1_bulk_reports_request_uuid()`: **Added**
* `gusto.payrolls.update()`: 
  *  `request.employee_compensations[].custom_withholdings` **Added**
  *  `response.employee_compensations[].custom_withholdings` **Added**
* `gusto.reports.post_v1_bulk_reports()`: **Added**
* `gusto.payrolls.get_receipt()`: `request` **Changed**
    - `page` **Added**
    - `per` **Added**
* `gusto.payrolls.prepare()`:  `response.employee_compensations[].custom_withholdings` **Added**
* `gusto.payrolls.skip()`:  `error.status[409]` **Added**
* `gusto.generated_documents.get()`:  `request.x_gusto_api_version` **Changed**
* `gusto.historical_employees.update()`:  `response.jobs[].location.warnings` **Added**
* `gusto.employee_addresses.get()`:  `response.[].warnings` **Added**
* `gusto.employee_addresses.create()`:  `response.warnings` **Added**
* `gusto.employee_addresses.retrieve_home_address()`:  `response.warnings` **Added**
* `gusto.employee_addresses.update()`:  `response.warnings` **Added**
* `gusto.locations.retrieve()`:  `response.warnings` **Added**
* `gusto.locations.update()`:  `response.warnings` **Added**
* `gusto.locations.get()`:  `response.[].warnings` **Added**
* `gusto.locations.create()`:  `response.warnings` **Added**
* `gusto.pay_schedules.get_preview()`:  `request.pay_schedule_uuid` **Added**
* `gusto.webhooks.list_subscriptions()`:  `response.[].subscription_types[].enum(time_off_request)` **Added**
* `gusto.webhooks.create_subscription()`: 
  *  `request.subscription_types[].enum(time_off_request)` **Added**
  *  `response.subscription_types[].enum(time_off_request)` **Added**
* `gusto.webhooks.get_subscription()`:  `response.subscription_types[].enum(time_off_request)` **Added**
* `gusto.webhooks.update_subscription()`: 
  *  `request.subscription_types[].enum(time_off_request)` **Added**
  *  `response.subscription_types[].enum(time_off_request)` **Added**
* `gusto.webhooks.verify()`:  `response.subscription_types[].enum(time_off_request)` **Added**
