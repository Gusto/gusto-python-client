# ReverseWireTransactionStatus

Current status of the reverse wire transaction.
- `pending_processing`: The reverse wire has been initiated and is awaiting processing by the banking network.
- `processed`: The reverse wire was successfully settled and funds have been received.
- `rejected`: The reverse wire was rejected by the receiving bank (e.g. invalid account, insufficient funds).
- `failed`: The reverse wire failed during processing due to a system or network error.


## Example Usage

```python
from gusto_embedded_v_2026_06_15.models import ReverseWireTransactionStatus

value = ReverseWireTransactionStatus.PENDING_PROCESSING

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name                 | Value                |
| -------------------- | -------------------- |
| `PENDING_PROCESSING` | pending_processing   |
| `PROCESSED`          | processed            |
| `REJECTED`           | rejected             |
| `FAILED`             | failed               |