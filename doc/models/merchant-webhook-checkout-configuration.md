
# Merchant Webhook Checkout Configuration

Checkout field collection settings.

*This model accepts additional fields of type Any.*

## Structure

`MerchantWebhookCheckoutConfiguration`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `ec_email` | [`MerchantWebhookCheckoutToggle`](../../doc/models/merchant-webhook-checkout-toggle.md) | Optional | Checkout feature toggle. |
| `ec_products` | [`MerchantWebhookCheckoutToggle`](../../doc/models/merchant-webhook-checkout-toggle.md) | Optional | Checkout feature toggle. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from univapayclientsdk.models.merchant_webhook_checkout_configuration import MerchantWebhookCheckoutConfiguration
from univapayclientsdk.models.merchant_webhook_checkout_toggle import MerchantWebhookCheckoutToggle

merchant_webhook_checkout_configuration = MerchantWebhookCheckoutConfiguration(
    ec_email=MerchantWebhookCheckoutToggle(
        enabled=True,
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    ec_products=MerchantWebhookCheckoutToggle(
        enabled=True,
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

