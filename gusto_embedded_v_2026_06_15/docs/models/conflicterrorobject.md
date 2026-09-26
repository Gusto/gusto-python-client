# ConflictErrorObject

Conflict
  
This may happen when the resource version provided does not match the current version — retrieve the latest version and retry — or when the request conflicts with another in-progress operation on the same resource. See the [Errors Categories](https://docs.gusto.com/embedded-payroll/docs/error-categories) guide for more details.


## Fields

| Field                                                                            | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `errors`                                                                         | List[[models.ConflictErrorObjectErrors](../models/conflicterrorobjecterrors.md)] | :heavy_check_mark:                                                               | N/A                                                                              |