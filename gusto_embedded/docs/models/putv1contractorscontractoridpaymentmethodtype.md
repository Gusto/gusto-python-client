# PutV1ContractorsContractorIDPaymentMethodType

The payment method type. If type is Direct Deposit, the contractor is required to have a bank account. See [Bank account endpoint](./post-v1-contractors-contractor_uuid-bank_accounts).

## Example Usage

```python
from gusto_embedded.models import PutV1ContractorsContractorIDPaymentMethodType

value = PutV1ContractorsContractorIDPaymentMethodType.DIRECT_DEPOSIT
```


## Values

| Name             | Value            |
| ---------------- | ---------------- |
| `DIRECT_DEPOSIT` | Direct Deposit   |
| `CHECK`          | Check            |