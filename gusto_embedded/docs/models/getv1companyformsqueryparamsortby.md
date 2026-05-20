# GetV1CompanyFormsQueryParamSortBy

Sort company forms by a given field. Append `:asc` or `:desc` to specify direction (e.g., `name:asc`). Defaults to ascending.

## Example Usage

```python
from gusto_embedded.models import GetV1CompanyFormsQueryParamSortBy

value = GetV1CompanyFormsQueryParamSortBy.NAME
```


## Values

| Name                    | Value                   |
| ----------------------- | ----------------------- |
| `NAME`                  | name                    |
| `YEAR`                  | year                    |
| `QUARTER`               | quarter                 |
| `DRAFT`                 | draft                   |
| `DOCUMENT_CONTENT_TYPE` | document_content_type   |
| `CREATED_AT`            | created_at              |