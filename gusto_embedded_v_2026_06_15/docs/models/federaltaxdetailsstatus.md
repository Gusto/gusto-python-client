# FederalTaxDetailsStatus

The status of EIN verification:
- `pending`: The EIN verification process has not completed (or the company does not yet have an EIN).
- `verified`: The EIN has been successfully verified as a valid EIN with the IRS.
- `failed`: The company's EIN did not pass verification. Common issues are being entered incorrectly or not matching the company's legal name.

## Example Usage

```python
from gusto_embedded_v_2026_06_15.models import FederalTaxDetailsStatus

value = FederalTaxDetailsStatus.PENDING

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name       | Value      |
| ---------- | ---------- |
| `PENDING`  | pending    |
| `VERIFIED` | verified   |
| `FAILED`   | failed     |