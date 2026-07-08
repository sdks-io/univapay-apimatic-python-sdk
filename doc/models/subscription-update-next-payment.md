
# Subscription Update Next Payment

Fields that can be updated on the next scheduled payment.

*This model accepts additional fields of type Any.*

## Structure

`SubscriptionUpdateNextPayment`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `due_date` | `date` | Optional | Next payment date (YYYY-MM-DD).  Note: Only available for merchants permitted to edit next payment dates. |
| `amount` | `int` | Optional | Next payment amount. Not available for limited-cycle subscriptions.  Only available for permitted merchants.  This does not change subsequent cycle amounts. |
| `terminate_with_status` | [`SubscriptionTerminateWithStatus`](../../doc/models/subscription-terminate-with-status.md) | Optional | Schedule a status transition on a payment's due date. Set to `suspended` or `canceled` to schedule termination. Send `null` to cancel a previously scheduled transition. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import dateutil.parser
import jsonpickle

from univapayclientsdk.models.subscription_terminate_with_status import SubscriptionTerminateWithStatus
from univapayclientsdk.models.subscription_update_next_payment import SubscriptionUpdateNextPayment

subscription_update_next_payment = SubscriptionUpdateNextPayment(
    due_date=dateutil.parser.parse('2016-03-13').date(),
    amount=32,
    terminate_with_status=SubscriptionTerminateWithStatus.SUSPENDED,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

