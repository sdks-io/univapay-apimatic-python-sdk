
# Merchant Webhook Qr Scan Configuration

QR scan payment settings.

*This model accepts additional fields of type Any.*

## Structure

`MerchantWebhookQrScanConfiguration`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `enabled` | `bool` | Optional | Enables QR scan payments. |
| `forbidden_qr_scan_gateways` | `List[str]` | Optional | QR scan gateways disabled for the merchant. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from univapayclientsdk.models.merchant_webhook_qr_scan_configuration import MerchantWebhookQrScanConfiguration

merchant_webhook_qr_scan_configuration = MerchantWebhookQrScanConfiguration(
    enabled=True,
    forbidden_qr_scan_gateways=[
        'wechat'
    ],
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

