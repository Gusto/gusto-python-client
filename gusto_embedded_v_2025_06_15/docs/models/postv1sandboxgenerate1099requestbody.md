# PostV1SandboxGenerate1099RequestBody


## Fields

| Field                                                                                        | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `contractor_id`                                                                              | *str*                                                                                        | :heavy_check_mark:                                                                           | The contractor UUID.                                                                         |
| `year`                                                                                       | *Optional[int]*                                                                              | :heavy_minus_sign:                                                                           | Must be equal to or more recent than 2015. If not specified, defaults to the previous year.<br/> |