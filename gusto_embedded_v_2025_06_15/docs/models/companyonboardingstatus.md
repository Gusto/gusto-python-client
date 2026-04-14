# CompanyOnboardingStatus

The representation of a company's onboarding status


## Fields

| Field                                                      | Type                                                       | Required                                                   | Description                                                |
| ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- |
| `uuid`                                                     | *str*                                                      | :heavy_check_mark:                                         | the UUID of the company                                    |
| `onboarding_completed`                                     | *Optional[bool]*                                           | :heavy_minus_sign:                                         | a boolean flag for the company's onboarding status         |
| `onboarding_steps`                                         | List[[models.OnboardingStep](../models/onboardingstep.md)] | :heavy_minus_sign:                                         | a list of company onboarding steps                         |