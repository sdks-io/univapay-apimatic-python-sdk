
# Charge Capture Request

Request payload for capturing an authorized charge.

*This model accepts additional fields of type Any.*

## Structure

`ChargeCaptureRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `amount` | `int` | Required | The amount to capture. Must be less than or equal to the authorized amount. |
| `currency` | `str` | Required | ISO-4217 currency code. Must exactly match the currency used during authorization. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from univapayclientsdk.models.charge_capture_request import ChargeCaptureRequest

charge_capture_request = ChargeCaptureRequest(
    amount=1000,
    currency='JPY',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

