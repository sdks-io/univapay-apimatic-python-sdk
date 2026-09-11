
# Merchant Webhook Checkout Toggle

Checkout feature toggle.

*This model accepts additional fields of type Any.*

## Structure

`MerchantWebhookCheckoutToggle`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `enabled` | `bool` | Optional | Enables this checkout field in hosted payment flows. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
from univapayclientsdk.models.merchant_webhook_checkout_toggle import MerchantWebhookCheckoutToggle

merchant_webhook_checkout_toggle = MerchantWebhookCheckoutToggle(
    enabled=True
)
```

