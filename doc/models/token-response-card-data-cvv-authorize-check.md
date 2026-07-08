
# Token Response Card Data Cvv Authorize Check

Token Response Card Data Cvv Authorize Check schema.

*This model accepts additional fields of type Any.*

## Structure

`TokenResponseCardDataCvvAuthorizeCheck`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `status` | `str` | Optional | Current status of the resource. |
| `charge_id` | `uuid\|str` | Optional | Charge identifier. |
| `date` | `datetime` | Optional | Date value. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import dateutil.parser
import jsonpickle

from univapayclientsdk.models.token_response_card_data_cvv_authorize_check import TokenResponseCardDataCvvAuthorizeCheck

token_response_card_data_cvv_authorize_check = TokenResponseCardDataCvvAuthorizeCheck(
    status='successful',
    charge_id=None,
    date=dateutil.parser.parse('2026-04-09T07:35:50Z'),
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

