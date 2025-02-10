# CompensationsModel

The available company-wide compensation rates for the company.


## Fields

| Field                                                              | Type                                                               | Required                                                           | Description                                                        |
| ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ |
| `hourly`                                                           | List[[models.Hourly](../models/hourly.md)]                         | :heavy_minus_sign:                                                 | The available hourly compensation rates for the company.           |
| `fixed`                                                            | List[[models.Fixed](../models/fixed.md)]                           | :heavy_minus_sign:                                                 | The available fixed compensation rates for the company.            |
| `paid_time_off`                                                    | List[[models.CompanyPaidTimeOff](../models/companypaidtimeoff.md)] | :heavy_minus_sign:                                                 | The available types of paid time off for the company.              |