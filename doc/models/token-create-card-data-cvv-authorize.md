
# Token Create Card Data Cvv Authorize

Token Create Card Data Cvv Authorize schema.

*This model accepts additional fields of type Any.*

## Structure

`TokenCreateCardDataCvvAuthorize`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `enabled` | `bool` | Optional | Enabled value.<br><br>**Default**: `False` |
| `currency` | `str` | Optional | ISO-4217 currency code. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from univapayclientsdk.models.token_create_card_data_cvv_authorize import TokenCreateCardDataCvvAuthorize

token_create_card_data_cvv_authorize = TokenCreateCardDataCvvAuthorize(
    enabled=False,
    currency='JPY',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

