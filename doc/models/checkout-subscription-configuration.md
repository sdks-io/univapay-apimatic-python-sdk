
# Checkout Subscription Configuration

Univapay-hosted subscription feature toggle.

*This model accepts additional fields of type Any.*

## Structure

`CheckoutSubscriptionConfiguration`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `enabled` | `bool` | Optional | Whether Univapay-hosted subscriptions are enabled. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from univapayclientsdk.models.checkout_subscription_configuration import CheckoutSubscriptionConfiguration

checkout_subscription_configuration = CheckoutSubscriptionConfiguration(
    enabled=True,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

