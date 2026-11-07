# BatchAction

The action to apply to every time sheet in the batch. One batch has only one action.
- `create`: Create new time sheets. Each item takes the same fields as [POST /v1/companies/{company_uuid}/time_tracking/time_sheets](ref:post-companies-company_uuid-time_tracking-time_sheets), plus `external_id`.
- `update`: Update existing time sheets. Each item requires `external_id`, `uuid` and `version`. All other fields are optional, and only the fields you send are changed.


## Example Usage

```python
from gusto_app_integration.models import BatchAction

value = BatchAction.CREATE
```


## Values

| Name     | Value    |
| -------- | -------- |
| `CREATE` | create   |
| `UPDATE` | update   |