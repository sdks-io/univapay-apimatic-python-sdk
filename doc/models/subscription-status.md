
# Subscription Status

Subscription Status schema.

## Enumeration

`SubscriptionStatus`

## Fields

| Name |
|  --- |
| `UNVERIFIED` |
| `UNCONFIRMED` |
| `CANCELED` |
| `UNPAID` |
| `CURRENT` |
| `SUSPENDED` |
| `COMPLETED` |

## Example

```python
from univapayclientsdk.models.subscription_status import SubscriptionStatus

subscription_status = SubscriptionStatus.SUSPENDED
```

