
# Merchant Webhook Convenience Configuration

Convenience-store payment settings.

*This model accepts additional fields of type Any.*

## Structure

`MerchantWebhookConvenienceConfiguration`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `enabled` | `bool` | Optional | Enables convenience-store payments. |
| `expiration` | `str` | Optional | ISO-8601 duration before convenience payment expiry. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
from univapayclientsdk.models.merchant_webhook_convenience_configuration import MerchantWebhookConvenienceConfiguration

merchant_webhook_convenience_configuration = MerchantWebhookConvenienceConfiguration(
    enabled=True,
    expiration='P3D'
)
```

