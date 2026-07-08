
# Subscription Next Payment

Next scheduled payment details for a subscription.

*This model accepts additional fields of type Any.*

## Structure

`SubscriptionNextPayment`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `uuid\|str` | Optional | Unique identifier. |
| `due_date` | `date` | Optional | Scheduled due date. |
| `zone_id` | `str` | Optional | IANA timezone identifier. |
| `amount` | `int` | Optional | Amount in the smallest currency unit. |
| `currency` | `str` | Optional | ISO-4217 currency code. |
| `amount_formatted` | `float` | Optional | Amount formatted for display. |
| `is_paid` | `bool` | Optional | Whether the payment has been paid. |
| `is_last_payment` | `bool` | Optional | Whether this is the final payment in the schedule. |
| `created_on` | `datetime` | Optional | Timestamp when the resource was created. |
| `updated_on` | `datetime` | Optional | Timestamp when the resource was last updated. |
| `retry_date` | `date` | Optional | Scheduled retry date. |
| `terminate_with_status` | [`SubscriptionTerminateWithStatus`](../../doc/models/subscription-terminate-with-status.md) | Optional | Schedule a status transition on a payment's due date. Set to `suspended` or `canceled` to schedule termination. Send `null` to cancel a previously scheduled transition. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import dateutil.parser
import jsonpickle

from univapayclientsdk.models.subscription_next_payment import SubscriptionNextPayment

subscription_next_payment = SubscriptionNextPayment(
    id='00002650-0000-0000-0000-000000000000',
    due_date=dateutil.parser.parse('2016-03-13').date(),
    zone_id='zone_id4',
    amount=18,
    currency='currency8',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

