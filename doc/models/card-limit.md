
# Card Limit

Per-card spending limit enforced on card payments, evaluated over a rolling duration.

*This model accepts additional fields of type Any.*

## Structure

`CardLimit`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `amount` | `int` | Optional | Maximum amount a single card may charge within `duration`. |
| `currency` | `str` | Optional | ISO-4217 currency code. |
| `amount_formatted` | `float` | Optional | Limit amount formatted for display. |
| `duration` | `str` | Optional | ISO-8601 period over which the limit is evaluated (e.g. P1M). |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from univapayclientsdk.models.card_limit import CardLimit

card_limit = CardLimit(
    amount=100000,
    currency='JPY',
    amount_formatted=100000,
    duration='P1M',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

