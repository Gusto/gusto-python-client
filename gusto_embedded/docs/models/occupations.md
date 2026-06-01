# Occupations


## Fields

| Field                                                                 | Type                                                                  | Required                                                              | Description                                                           |
| --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- |
| `code`                                                                | *str*                                                                 | :heavy_check_mark:                                                    | Bureau of Labor Statistics (BLS) occupation code.                     |
| `name`                                                                | *Optional[str]*                                                       | :heavy_minus_sign:                                                    | Occupation name.                                                      |
| `description`                                                         | *Optional[str]*                                                       | :heavy_minus_sign:                                                    | Occupation description.                                               |
| `experience_level`                                                    | [models.ExperienceLevel](../models/experiencelevel.md)                | :heavy_check_mark:                                                    | Experience level for this occupation.                                 |
| `time_percentage`                                                     | *str*                                                                 | :heavy_check_mark:                                                    | Percentage of time spent in this occupation (as decimal string, 0-1). |
| `primary`                                                             | *Optional[bool]*                                                      | :heavy_minus_sign:                                                    | Whether this is the primary occupation.                               |