
# Subscription Update Status

Update the subscription status.  `suspended`: Pause the subscription.  `unpaid`: Resume a suspended subscription.

## Enumeration

`SubscriptionUpdateStatus`

## Fields

| Name |
|  --- |
| `SUSPENDED` |
| `UNPAID` |

## Example

```python
from univapayclientsdk.models.subscription_update_status import SubscriptionUpdateStatus

subscription_update_status = SubscriptionUpdateStatus.SUSPENDED
```

