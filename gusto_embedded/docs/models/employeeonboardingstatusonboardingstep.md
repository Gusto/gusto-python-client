# EmployeeOnboardingStatusOnboardingStep


## Fields

| Field                                                   | Type                                                    | Required                                                | Description                                             |
| ------------------------------------------------------- | ------------------------------------------------------- | ------------------------------------------------------- | ------------------------------------------------------- |
| `title`                                                 | *Optional[str]*                                         | :heavy_minus_sign:                                      | User-friendly description of the onboarding step.       |
| `id`                                                    | *Optional[str]*                                         | :heavy_minus_sign:                                      | String identifier for the onboarding step.              |
| `required`                                              | *Optional[bool]*                                        | :heavy_minus_sign:                                      | When true, this step has been completed.                |
| `completed`                                             | *Optional[bool]*                                        | :heavy_minus_sign:                                      | When true, this step has been completed.                |
| `requirements`                                          | List[*str*]                                             | :heavy_minus_sign:                                      | A list of onboarding steps required to begin this step. |