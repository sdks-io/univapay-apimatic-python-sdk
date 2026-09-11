
# Merchant Webhook Paidy Configuration

Paidy payment settings.

*This model accepts additional fields of type Any.*

## Structure

`MerchantWebhookPaidyConfiguration`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `enabled` | `bool` | Optional | Enables Paidy payments. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
from univapayclientsdk.models.merchant_webhook_paidy_configuration import MerchantWebhookPaidyConfiguration

merchant_webhook_paidy_configuration = MerchantWebhookPaidyConfiguration(
    enabled=False
)
```

