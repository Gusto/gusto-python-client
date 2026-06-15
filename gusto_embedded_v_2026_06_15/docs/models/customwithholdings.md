# CustomWithholdings

Optional per-payroll one-time custom withholdings for federal and/or state income tax.
When provided, the supplied override takes precedence over any persistent withholding schedule for this run.
This field is in limited release; if your application does not have access, requests including it are silently ignored.



## Fields

| Field                                                                   | Type                                                                    | Required                                                                | Description                                                             |
| ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- |
| `federal`                                                               | [Optional[models.Federal]](../models/federal.md)                        | :heavy_minus_sign:                                                      | Federal one-time custom withholding override.                           |
| `state`                                                                 | List[[models.State](../models/state.md)]                                | :heavy_minus_sign:                                                      | State one-time custom withholding overrides, one entry per state field. |