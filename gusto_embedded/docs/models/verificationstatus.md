# VerificationStatus

The verification status of the bank account.

'awaiting_deposits' means the bank account is just created and money is being transferred.
'ready_for_verification' means the micro-deposits are completed and the verification process can begin by using the verify endpoint.
'verified' means the bank account is verified.


## Values

| Name                     | Value                    |
| ------------------------ | ------------------------ |
| `AWAITING_DEPOSITS`      | awaiting_deposits        |
| `READY_FOR_VERIFICATION` | ready_for_verification   |
| `VERIFIED`               | verified                 |