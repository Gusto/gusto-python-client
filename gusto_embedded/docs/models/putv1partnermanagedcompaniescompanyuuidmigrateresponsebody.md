# PutV1PartnerManagedCompaniesCompanyUUIDMigrateResponseBody

Example response


## Fields

| Field                                                            | Type                                                             | Required                                                         | Description                                                      |
| ---------------------------------------------------------------- | ---------------------------------------------------------------- | ---------------------------------------------------------------- | ---------------------------------------------------------------- |
| `company_uuid`                                                   | *Optional[str]*                                                  | :heavy_minus_sign:                                               | The company UUID                                                 |
| `migration_status`                                               | [Optional[models.MigrationStatus]](../models/migrationstatus.md) | :heavy_minus_sign:                                               | The migration status. 'success' is the only valid return value.  |