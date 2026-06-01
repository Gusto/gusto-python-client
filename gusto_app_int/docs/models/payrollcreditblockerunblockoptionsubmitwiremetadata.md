# PayrollCreditBlockerUnblockOptionSubmitWireMetadata


## Fields

| Field                                                                | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `wire_in_amount`                                                     | *str*                                                                | :heavy_check_mark:                                                   | The amount to be wired in (decimal string)                           |
| `wire_in_deadline`                                                   | [date](https://docs.python.org/3/library/datetime.html#date-objects) | :heavy_check_mark:                                                   | Deadline for the wire transfer to be received                        |
| `wire_in_request_uuid`                                               | *str*                                                                | :heavy_check_mark:                                                   | UUID of the wire in request                                          |