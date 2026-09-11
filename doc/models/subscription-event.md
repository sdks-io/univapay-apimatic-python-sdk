
# Subscription Event

Event type discriminator — `subscription_created`, `subscription_payment`, `subscription_completed`, `subscription_failure`, `subscription_canceled`, or `subscription_suspended`.

## Enumeration

`SubscriptionEvent`

## Fields

| Name |
|  --- |
| `SUBSCRIPTION_CREATED` |
| `SUBSCRIPTION_PAYMENT` |
| `SUBSCRIPTION_COMPLETED` |
| `SUBSCRIPTION_FAILURE` |
| `SUBSCRIPTION_CANCELED` |
| `SUBSCRIPTION_SUSPENDED` |

## Example

```python
from univapayclientsdk.models.subscription_event import SubscriptionEvent

subscription_event = SubscriptionEvent.SUBSCRIPTION_CREATED
```

