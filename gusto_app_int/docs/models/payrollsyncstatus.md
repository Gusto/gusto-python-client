# PayrollSyncStatus

The current status of the payroll sync. READ-ONLY.

## State Transitions
```
pending ──────► in_progress ──────► success
                            ├─────► failure
                            └─────► partial_success
```

### Valid Transitions
- `pending` → `in_progress`: Automatic when processing begins
- `in_progress` → `success`: All time sheet data synced successfully
- `in_progress` → `failure`: Sync failed entirely
- `in_progress` → `partial_success`: Some members failed to sync


## Example Usage

```python
from gusto_app_integration.models import PayrollSyncStatus

value = PayrollSyncStatus.PENDING
```


## Values

| Name              | Value             |
| ----------------- | ----------------- |
| `PENDING`         | pending           |
| `IN_PROGRESS`     | in_progress       |
| `SUCCESS`         | success           |
| `FAILURE`         | failure           |
| `PARTIAL_SUCCESS` | partial_success   |