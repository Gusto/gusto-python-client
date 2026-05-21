# EmployeeMemberPortalInvitationStatus

Member portal invitation status information. Only included when the include param has the portal_invitations value set.


## Fields

| Field                                                                | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `status`                                                             | [Optional[models.EmployeeStatus]](../models/employeestatus.md)       | :heavy_minus_sign:                                                   | The current status of the member portal invitation.                  |
| `token_expired`                                                      | *OptionalNullable[bool]*                                             | :heavy_minus_sign:                                                   | Whether the invitation token has expired.                            |
| `welcome_email_sent_at`                                              | [date](https://docs.python.org/3/library/datetime.html#date-objects) | :heavy_minus_sign:                                                   | The date and time when the welcome email was sent.                   |
| `last_password_resent_at`                                            | [date](https://docs.python.org/3/library/datetime.html#date-objects) | :heavy_minus_sign:                                                   | The date and time when the password reset was last resent.           |