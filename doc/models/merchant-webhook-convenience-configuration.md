
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
import jsonpickle

from univapayclientsdk.models.merchant_webhook_convenience_configuration import MerchantWebhookConvenienceConfiguration

merchant_webhook_convenience_configuration = MerchantWebhookConvenienceConfiguration(
    enabled=True,
    expiration='P3D',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

