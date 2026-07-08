
# Merchant Webhook Recurring Cvv Confirmation Config

CVV confirmation rules for recurring token charges.

*This model accepts additional fields of type Any.*

## Structure

`MerchantWebhookRecurringCvvConfirmationConfig`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `enabled` | `bool` | Optional | Enables recurring-charge CVV confirmation checks. |
| `threshold` | [`List[MerchantWebhookMoneyAmount]`](../../doc/models/merchant-webhook-money-amount.md) | Optional | Amount thresholds that trigger CVV confirmation. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from univapayclientsdk.models.merchant_webhook_recurring_cvv_confirmation_config import MerchantWebhookRecurringCvvConfirmationConfig

merchant_webhook_recurring_cvv_confirmation_config = MerchantWebhookRecurringCvvConfirmationConfig(
    enabled=False,
    threshold=[
        None
    ],
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

