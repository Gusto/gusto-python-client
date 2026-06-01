# EmployeesAnnualFicaWageReportAcceptance

Acceptance acknowledgement for an asynchronous employees annual FICA wage report. Returned with HTTP 202; poll the report status endpoint using `request_uuid`.


## Fields

| Field                                                                   | Type                                                                    | Required                                                                | Description                                                             |
| ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- |
| `request_uuid`                                                          | *str*                                                                   | :heavy_check_mark:                                                      | The UUID of the report request. Use this to poll for report completion. |
| `company_uuid`                                                          | *str*                                                                   | :heavy_check_mark:                                                      | The UUID of the company.                                                |
| `start_year`                                                            | *int*                                                                   | :heavy_check_mark:                                                      | The start year for the report.                                          |
| `end_year`                                                              | *int*                                                                   | :heavy_check_mark:                                                      | The end year for the report.                                            |