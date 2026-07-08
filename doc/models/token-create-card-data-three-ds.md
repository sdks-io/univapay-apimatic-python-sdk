
# Token Create Card Data Three Ds

Token Create Card Data Three Ds schema.

*This model accepts additional fields of type Any.*

## Structure

`TokenCreateCardDataThreeDs`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `enabled` | `bool` | Optional | Enabled value. |
| `redirect_endpoint` | `str` | Optional | Redirect endpoint URL. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from univapayclientsdk.models.token_create_card_data_three_ds import TokenCreateCardDataThreeDs

token_create_card_data_three_ds = TokenCreateCardDataThreeDs(
    enabled=False,
    redirect_endpoint='redirect_endpoint4',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

