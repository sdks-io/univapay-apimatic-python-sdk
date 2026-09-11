
# Merchant Webhook Qr Merchant Configuration

QR merchant payment settings.

*This model accepts additional fields of type Any.*

## Structure

`MerchantWebhookQrMerchantConfiguration`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `enabled` | `bool` | Optional | Enables QR merchant payment flows. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
from univapayclientsdk.models.merchant_webhook_qr_merchant_configuration import MerchantWebhookQrMerchantConfiguration

merchant_webhook_qr_merchant_configuration = MerchantWebhookQrMerchantConfiguration(
    enabled=False
)
```

