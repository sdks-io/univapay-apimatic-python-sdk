
# Checkout Subscription Plan Configuration

Univapay-side subscription plan configuration applied to checkout.

*This model accepts additional fields of type Any.*

## Structure

`CheckoutSubscriptionPlanConfiguration`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `enabled` | `bool` | Optional | Whether subscription plans are enabled. |
| `fixed_cycle` | `bool` | Optional | Whether fixed-cycle subscription plans are allowed. |
| `fixed_cycle_amount` | `bool` | Optional | Whether fixed-cycle-amount subscription plans are allowed. |
| `supported_payment_types` | [`List[CheckoutPaymentType]`](../../doc/models/checkout-payment-type.md) | Optional | Payment types eligible for subscription plans. |
| `min_charge_amount` | [`CheckoutMoneyAmount`](../../doc/models/checkout-money-amount.md) | Optional | Minimum charge amount eligible for subscription plans. `null` when unrestricted. |
| `max_payout_period` | `str` | Optional | ISO-8601 period bounding the maximum payout delay for subscription settlements. `null` when unrestricted. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from univapayclientsdk.models.checkout_payment_type import CheckoutPaymentType
from univapayclientsdk.models.checkout_subscription_plan_configuration import CheckoutSubscriptionPlanConfiguration

checkout_subscription_plan_configuration = CheckoutSubscriptionPlanConfiguration(
    enabled=True,
    fixed_cycle=True,
    fixed_cycle_amount=True,
    supported_payment_types=[
        CheckoutPaymentType.CARD
    ],
    min_charge_amount=None,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

