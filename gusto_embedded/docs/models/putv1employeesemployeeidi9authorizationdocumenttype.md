# PutV1EmployeesEmployeeIDI9AuthorizationDocumentType

The type of document an employee holds, based on their authorization status.

  * This is unused for authorization status `citizen` or `noncitizen`.
  * If the authorization status is `permanent_resident`, this must be `uscis_alien_registration_number`.
  * If the authorization status is `alien`, this is required and may be any of the valid values.



## Values

| Name                              | Value                             |
| --------------------------------- | --------------------------------- |
| `USCIS_ALIEN_REGISTRATION_NUMBER` | uscis_alien_registration_number   |
| `FORM_I94`                        | form_i94                          |
| `FOREIGN_PASSPORT`                | foreign_passport                  |