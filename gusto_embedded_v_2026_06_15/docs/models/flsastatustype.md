# FlsaStatusType

The FLSA status for this compensation. Salaried ('Exempt') employees are paid a fixed salary every pay period. Salaried with overtime ('Salaried Nonexempt') employees are paid a fixed salary every pay period, and receive overtime pay when applicable. Hourly ('Nonexempt') employees are paid for the hours they work, and receive overtime pay when applicable. Commissioned employees ('Commission Only Exempt') earn wages based only on commission. Commissioned with overtime ('Commission Only Nonexempt') earn wages based on commission, and receive overtime pay when applicable. Owners ('Owner') are employees that own at least twenty percent of the company. 

## Example Usage

```python
from gusto_embedded_v_2026_06_15.models import FlsaStatusType

value = FlsaStatusType.EXEMPT

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name                        | Value                       |
| --------------------------- | --------------------------- |
| `EXEMPT`                    | Exempt                      |
| `SALARIED_NONEXEMPT`        | Salaried Nonexempt          |
| `NONEXEMPT`                 | Nonexempt                   |
| `OWNER`                     | Owner                       |
| `COMMISSION_ONLY_EXEMPT`    | Commission Only Exempt      |
| `COMMISSION_ONLY_NONEXEMPT` | Commission Only Nonexempt   |