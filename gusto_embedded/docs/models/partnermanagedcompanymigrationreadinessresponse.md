# PartnerManagedCompanyMigrationReadinessResponse


## Fields

| Field                                             | Type                                              | Required                                          | Description                                       |
| ------------------------------------------------- | ------------------------------------------------- | ------------------------------------------------- | ------------------------------------------------- |
| `ready_to_migrate`                                | *Optional[bool]*                                  | :heavy_minus_sign:                                | Indicates if the company is ready to be migrated. |
| `company_uuid`                                    | *Optional[str]*                                   | :heavy_minus_sign:                                | The company UUID                                  |
| `errors`                                          | List[[models.Errors](../models/errors.md)]        | :heavy_minus_sign:                                | N/A                                               |
| `warnings`                                        | List[[models.Warnings](../models/warnings.md)]    | :heavy_minus_sign:                                | N/A                                               |