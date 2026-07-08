
# Subscription Payment List

Paginated list of subscription payments.

*This model accepts additional fields of type Any.*

## Structure

`SubscriptionPaymentList`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `items` | [`List[SubscriptionPayment]`](../../doc/models/subscription-payment.md) | Optional | List of resources. |
| `has_more` | `bool` | Optional | Whether more results are available. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import dateutil.parser
import jsonpickle

from univapayclientsdk.models.subscription_payment import SubscriptionPayment
from univapayclientsdk.models.subscription_payment_list import SubscriptionPaymentList

subscription_payment_list = SubscriptionPaymentList(
    items=[
        SubscriptionPayment(
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
        ),
        SubscriptionPayment(
            id='11e89a0a-8cc5-2662-9460-2b14b1a601ba',
            due_date=dateutil.parser.parse('2018-08-07').date(),
            zone_id='Asia/Tokyo',
            amount=1000,
            currency='JPY',
            amount_formatted=1000,
            is_paid=True,
            is_last_payment=False,
            created_on=dateutil.parser.parse('2018-08-07T06:24:33.646223Z'),
            updated_on=dateutil.parser.parse('2018-08-07T06:24:33.887760Z'),
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        )
    ],
    has_more=False,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

