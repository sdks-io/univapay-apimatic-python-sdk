
# Merchant Webhook Subscription Configuration

Subscription feature configuration.

*This model accepts additional fields of type Any.*

## Structure

`MerchantWebhookSubscriptionConfiguration`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `enabled` | `bool` | Optional | Enables subscription payments. |
| `failed_charges_to_cancel` | `int` | Optional | Number of failed charges allowed before cancellation. |
| `suspend_on_cancel` | `bool` | Optional | Suspends the subscription when its latest charge is canceled. |
| `allow_merchant_amount_patch` | `bool` | Optional | Allows merchants to update scheduled subscription amounts. |
| `allow_merchant_due_date_patch` | `bool` | Optional | Allows merchants to update scheduled subscription due dates. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
from univapayclientsdk.models.merchant_webhook_subscription_configuration import MerchantWebhookSubscriptionConfiguration

merchant_webhook_subscription_configuration = MerchantWebhookSubscriptionConfiguration(
    enabled=True,
    failed_charges_to_cancel=3,
    suspend_on_cancel=True,
    allow_merchant_amount_patch=False,
    allow_merchant_due_date_patch=False
)
```

