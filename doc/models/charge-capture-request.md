
# Charge Capture Request

Request payload for capturing an authorized charge. Both fields are optional; omit the entire body to capture the full outstanding amount.

*This model accepts additional fields of type Any.*

## Structure

`ChargeCaptureRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `amount` | `int` | Optional | The amount to capture. Must be less than or equal to the authorized amount. If omitted, the full outstanding authorized amount is captured. |
| `currency` | `str` | Optional | ISO-4217 currency code. Must exactly match the currency used during authorization. If omitted, defaults to the currency originally requested on the charge. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
from univapayclientsdk.models.charge_capture_request import ChargeCaptureRequest

charge_capture_request = ChargeCaptureRequest(
    amount=1000,
    currency='JPY'
)
```

