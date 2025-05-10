# Entries


## Fields

| Field                                                                            | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `uuid`                                                                           | *Optional[str]*                                                                  | :heavy_minus_sign:                                                               | Unique identifier of the entry.                                                  |
| `hours_worked`                                                                   | *Optional[str]*                                                                  | :heavy_minus_sign:                                                               | Hours worked for this pay classification. Represented as a string, e.g. "1.500". |
| `pay_classification`                                                             | [Optional[models.PayClassification]](../models/payclassification.md)             | :heavy_minus_sign:                                                               | Pay classification for the entry.                                                |