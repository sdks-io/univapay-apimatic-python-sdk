
# Token Response Phone Number

Token Response Phone Number schema.

*This model accepts additional fields of type Any.*

## Structure

`TokenResponsePhoneNumber`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `country_code` | `int` | Optional | Returned as an integer in the response. |
| `local_number` | `str` | Optional | Local phone number. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from univapayclientsdk.models.token_response_phone_number import TokenResponsePhoneNumber

token_response_phone_number = TokenResponsePhoneNumber(
    country_code=81,
    local_number='08012341234',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

