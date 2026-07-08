
# Merchant Webhook Subscription Plan Configuration

Subscription plan configuration.

*This model accepts additional fields of type Any.*

## Structure

`MerchantWebhookSubscriptionPlanConfiguration`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `enabled` | `bool` | Optional | Enables limited-cycle subscription plans. |
| `fixed_cycle` | `bool` | Optional | Allows plans limited by a fixed number of cycles. |
| `fixed_cycle_amount` | `bool` | Optional | Allows plans limited by a total target amount. |
| `supported_payment_types` | `List[str]` | Optional | Payment types that can use subscription plans. |
| `min_charge_amount` | [`MerchantWebhookMoneyAmount`](../../doc/models/merchant-webhook-money-amount.md) | Optional | Monetary amount object serialized by backend config models. |
| `max_payout_period` | `str` | Optional | Maximum payout delay allowed for subscription plan settlements. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from univapayclientsdk.models.merchant_webhook_money_amount import MerchantWebhookMoneyAmount
from univapayclientsdk.models.merchant_webhook_subscription_plan_configuration import MerchantWebhookSubscriptionPlanConfiguration

merchant_webhook_subscription_plan_configuration = MerchantWebhookSubscriptionPlanConfiguration(
    enabled=True,
    fixed_cycle=True,
    fixed_cycle_amount=True,
    supported_payment_types=[
        'card'
    ],
    min_charge_amount=MerchantWebhookMoneyAmount(
        amount=3000,
        currency='JPY',
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    max_payout_period='P12M',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

