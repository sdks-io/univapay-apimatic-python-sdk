
# Token Response Card Data Three Ds

Token Response Card Data Three Ds schema.

*This model accepts additional fields of type Any.*

## Structure

`TokenResponseCardDataThreeDs`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `enabled` | `bool` | Optional | Enabled value. |
| `status` | [`TokenResponseCardDataThreeDsStatus`](../../doc/models/token-response-card-data-three-ds-status.md) | Optional | Token Response Card Data Three Ds Status schema. |
| `redirect_endpoint` | `str` | Optional | Redirect endpoint URL. |
| `redirect_id` | `uuid\|str` | Optional | Redirect identifier. |
| `exempted` | `bool` | Optional | Indicates if the 3DS check was exempted. When creating charge 3DS check will not be required. |
| `error` | [`PaymentError`](../../doc/models/payment-error.md) | Optional | Payment error details, or null if successful. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from univapayclientsdk.models.token_response_card_data_three_ds import TokenResponseCardDataThreeDs
from univapayclientsdk.models.token_response_card_data_three_ds_status import TokenResponseCardDataThreeDsStatus

token_response_card_data_three_ds = TokenResponseCardDataThreeDs(
    enabled=True,
    status=TokenResponseCardDataThreeDsStatus.SUCCESSFUL,
    redirect_endpoint=None,
    redirect_id=None,
    exempted=False,
    error=None,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

