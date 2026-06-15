## Python SDK Changes:
* `gusto.webhooks.verify()`:  `response.subscription_types[].enum(time_off_request)` **Added** (Breaking ⚠️)
* `gusto.webhooks.get_subscription()`:  `response.subscription_types[].enum(time_off_request)` **Added** (Breaking ⚠️)
* `gusto.webhooks.update_subscription()`: 
  *  `request.subscription_types[].enum(time_off_request)` **Added**
  *  `response.subscription_types[].enum(time_off_request)` **Added** (Breaking ⚠️)
* `gusto.webhooks.list_subscriptions()`:  `response.[].subscription_types[].enum(time_off_request)` **Added** (Breaking ⚠️)
* `gusto.webhooks.create_subscription()`: 
  *  `request.subscription_types[].enum(time_off_request)` **Added**
  *  `response.subscription_types[].enum(time_off_request)` **Added** (Breaking ⚠️)
* `gusto.contractors.delete_v1_contractors_contractor_uuid_rehire()`:  `error.status[422]` **Added**
* `gusto.pay_schedules.get_preview()`:  `request.pay_schedule_uuid` **Added**
* `gusto.contractors.post_v1_contractors_contractor_uuid_rehire()`:  `error.status[422]` **Added**
* `gusto.employees.update_onboarding_status()`:  `response.blockers` **Added**
* `gusto.contractors.delete_v1_contractors_contractor_uuid_termination()`:  `error.status[422]` **Added**
* `gusto.contractors.post_v1_contractors_contractor_uuid_termination()`:  `error.status[422]` **Added**
* `gusto.employees.get_onboarding_status()`:  `response.blockers` **Added**
* `gusto.contractor_payments.get_v1_contractors_contractor_uuid_payments()`: **Added**
* `gusto.payrolls.get_approved_reversals()`:  `request.x_gusto_api_version` **Changed**
* `gusto.payrolls.update()`: 
  *  `request.employee_compensations[].custom_withholdings` **Added**
* `gusto.generated_documents.get()`:  `request.x_gusto_api_version` **Changed**
