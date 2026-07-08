
# Token Response Card Data Cvv Authorize

Token Response Card Data Cvv Authorize schema.

*This model accepts additional fields of type Any.*

## Structure

`TokenResponseCardDataCvvAuthorize`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `enabled` | `bool` | Optional | Enabled value. |
| `status` | `str` | Optional | Current status of the resource. |
| `charge_id` | `uuid\|str` | Optional | Charge identifier. |
| `credentials_id` | `uuid\|str` | Optional | Credentials identifier. |
| `currency` | `str` | Optional | ISO-4217 currency code. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from univapayclientsdk.models.token_response_card_data_cvv_authorize import TokenResponseCardDataCvvAuthorize

token_response_card_data_cvv_authorize = TokenResponseCardDataCvvAuthorize(
    enabled=True,
    status='successful',
    charge_id=None,
    credentials_id=None,
    currency='JPY',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

