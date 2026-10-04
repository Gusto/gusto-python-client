# EarningTypeCategory

The earning type category. Only present when the company has access to
categorized custom bonus earning types.


## Example Usage

```python
from gusto_embedded_v_2026_06_15.models import EarningTypeCategory

value = EarningTypeCategory.CASH_TIPS

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name                      | Value                     |
| ------------------------- | ------------------------- |
| `CASH_TIPS`               | CashTips                  |
| `COMMISSION`              | Commission                |
| `DISCRETIONARY_BONUS`     | DiscretionaryBonus        |
| `BENEFIT_CONTRIBUTIONS`   | BenefitContributions      |
| `MINIMUM_WAGE_ADJUSTMENT` | MinimumWageAdjustment     |
| `MINISTER_HOUSING`        | MinisterHousing           |
| `NON_DISCRETIONARY_BONUS` | NonDiscretionaryBonus     |
| `ON_CALL_PAY`             | OnCallPay                 |
| `OWNERS_DRAW`             | OwnersDraw                |
| `PAYCHECK_TIPS`           | PaycheckTips              |
| `CORRECTION_PAYMENT`      | CorrectionPayment         |
| `SERVICE_CHARGES`         | ServiceCharges            |
| `SEVERANCE_PAY`           | SeverancePay              |
| `OTHER`                   | Other                     |
| `NON_TAXABLE_DISABILITY`  | NonTaxableDisability      |
| `OTHER_REGULAR_INCOME`    | OtherRegularIncome        |
| `OTHER_NON_TAXABLE`       | OtherNonTaxable           |