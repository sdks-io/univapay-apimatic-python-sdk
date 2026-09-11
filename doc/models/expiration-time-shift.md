
# Expiration Time Shift

Time-of-day override applied when calculating expirations, shared by convenience-store and bank-transfer configuration.

*This model accepts additional fields of type Any.*

## Structure

`ExpirationTimeShift`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `value` | `str` | Optional | ISO-8601 offset time (HH:mm:ssXXX) that overrides the expiration cutoff. Omitted entirely when no override is configured. |
| `enabled` | `bool` | Optional | Whether the time-of-day override is applied. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from univapayclientsdk.models.expiration_time_shift import ExpirationTimeShift

expiration_time_shift = ExpirationTimeShift(
    value='23:59:59+09:00',
    enabled=False,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

