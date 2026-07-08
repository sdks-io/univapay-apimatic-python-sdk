
# Subscription Payment

Represents a single scheduled or historical payment for a subscription.

*This model accepts additional fields of type Any.*

## Structure

`SubscriptionPayment`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `uuid\|str` | Optional | Unique identifier. |
| `due_date` | `date` | Optional | Scheduled due date. |
| `zone_id` | `str` | Optional | IANA Timezone ID. |
| `amount` | `int` | Optional | Amount in the smallest currency unit. |
| `currency` | `str` | Optional | ISO-4217 currency code. |
| `amount_formatted` | `float` | Optional | Amount formatted for display. |
| `is_paid` | `bool` | Optional | Indicates whether this specific payment cycle has been successfully charged. |
| `is_last_payment` | `bool` | Optional | Indicates if this is the final payment in a limited-cycle subscription. |
| `created_on` | `datetime` | Optional | Timestamp when the resource was created. |
| `updated_on` | `datetime` | Optional | Timestamp when the resource was last updated. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import dateutil.parser
import jsonpickle

from univapayclientsdk.models.subscription_payment import SubscriptionPayment

subscription_payment = SubscriptionPayment(
    id='11e89a0a-8cee-d660-b984-3fcaaed46e7c',
    due_date=dateutil.parser.parse('2018-08-21').date(),
    zone_id='Asia/Tokyo',
    amount=10000,
    currency='JPY',
    amount_formatted=10000,
    is_paid=False,
    is_last_payment=False,
    created_on=dateutil.parser.parse('2018-08-07T06:24:33.961256Z'),
    updated_on=dateutil.parser.parse('2018-08-07T06:24:33.961256Z'),
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

