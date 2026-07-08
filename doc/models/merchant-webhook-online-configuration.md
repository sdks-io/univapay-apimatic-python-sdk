
# Merchant Webhook Online Configuration

Online payment settings.

*This model accepts additional fields of type Any.*

## Structure

`MerchantWebhookOnlineConfiguration`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `enabled` | `bool` | Optional | Enables online redirect and wallet payment flows. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from univapayclientsdk.models.merchant_webhook_online_configuration import MerchantWebhookOnlineConfiguration

merchant_webhook_online_configuration = MerchantWebhookOnlineConfiguration(
    enabled=True,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

