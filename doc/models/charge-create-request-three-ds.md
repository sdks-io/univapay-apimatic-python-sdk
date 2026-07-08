
# Charge Create Request Three Ds

Charge Create Request Three Ds schema.

*This model accepts additional fields of type Any.*

## Structure

`ChargeCreateRequestThreeDs`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `redirect_endpoint` | `str` | Optional | URL to redirect the customer to after 3DS authentication. |
| `mode` | [`ChargeCreateRequestThreeDsMode`](../../doc/models/charge-create-request-three-ds-mode.md) | Optional | 3D-Secure authentication type. App Token Secret is required to use 'skip'.<br><br>**Default**: `"normal"` |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from univapayclientsdk.models.charge_create_request_three_ds import ChargeCreateRequestThreeDs
from univapayclientsdk.models.charge_create_request_three_ds_mode import ChargeCreateRequestThreeDsMode

charge_create_request_three_ds = ChargeCreateRequestThreeDs(
    redirect_endpoint='redirect_endpoint6',
    mode=ChargeCreateRequestThreeDsMode.NORMAL,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

