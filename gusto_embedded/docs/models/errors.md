# Errors


## Fields

| Field                                                                          | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `error_key`                                                                    | *Optional[str]*                                                                | :heavy_minus_sign:                                                             | The key identifying the error source.                                          |
| `category`                                                                     | *Optional[str]*                                                                | :heavy_minus_sign:                                                             | The error category.                                                            |
| `message`                                                                      | *OptionalNullable[str]*                                                        | :heavy_minus_sign:                                                             | Human-readable error message.                                                  |
| `errors`                                                                       | List[[models.PeopleBatchResultsErrors](../models/peoplebatchresultserrors.md)] | :heavy_minus_sign:                                                             | Nested errors for sub-operations.                                              |