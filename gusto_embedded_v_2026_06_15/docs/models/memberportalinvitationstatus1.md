# MemberPortalInvitationStatus1

Current status of the member portal invitation.
- `pending`: The invitation record has been created but the invitation email has not yet been delivered.
- `sent`: The invitation email has been delivered to the member.
- `verified`: The member has been verified by the member portal partner.
- `complete`: The member has fully completed their member portal registration.
- `cancelled`: The invitation has been cancelled, either via `DELETE` on this endpoint or because it was superseded.


## Example Usage

```python
from gusto_embedded_v_2026_06_15.models import MemberPortalInvitationStatus1

value = MemberPortalInvitationStatus1.PENDING

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name        | Value       |
| ----------- | ----------- |
| `PENDING`   | pending     |
| `SENT`      | sent        |
| `VERIFIED`  | verified    |
| `COMPLETE`  | complete    |
| `CANCELLED` | cancelled   |