# PayrollSubmissionBlockerRequestType

Request object for resolving a submission blocker. Each submission_blocker should include a selected unblock option.


## Fields

| Field                                                            | Type                                                             | Required                                                         | Description                                                      |
| ---------------------------------------------------------------- | ---------------------------------------------------------------- | ---------------------------------------------------------------- | ---------------------------------------------------------------- |
| `blocker_type`                                                   | *str*                                                            | :heavy_check_mark:                                               | The type of submission_blocker that is blocking the payment.     |
| `selected_option`                                                | *str*                                                            | :heavy_check_mark:                                               | The selected option to unblock the payment's submission_blocker. |