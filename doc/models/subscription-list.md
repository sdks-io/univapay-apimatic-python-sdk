
# Subscription List

Paginated list of subscriptions.

*This model accepts additional fields of type Any.*

## Structure

`SubscriptionList`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `items` | [`List[SubscriptionListItem]`](../../doc/models/subscription-list-item.md) | Optional | List of resources. |
| `has_more` | `bool` | Optional | Whether more results are available. |
| `total_hits` | `int` | Optional | Total number of matching resources. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import dateutil.parser
import jsonpickle

from univapayclientsdk.models.subscription_list import SubscriptionList
from univapayclientsdk.models.subscription_list_item import SubscriptionListItem
from univapayclientsdk.models.subscription_status import SubscriptionStatus
from univapayclientsdk.models.subscription_user_data import SubscriptionUserData

subscription_list = SubscriptionList(
    items=[
        SubscriptionListItem(
            id='11ef3410-aaaa-4bcd-8e1f-1a2b3c4d5e60',
            store_id='11edf541-c42d-653c-8c3d-dfe0a55f95c0',
            transaction_token_id='11ef3413-dddd-4ef0-b142-4d5e6f809193',
            amount=1250,
            currency='USD',
            amount_formatted=12.5,
            status=SubscriptionStatus.CURRENT,
            merchant_name='管理画面ガイド',
            store_name='管理画面ガイド_TEST店舗',
            payment_type='card',
            next_payment_date=dateutil.parser.parse('2024-07-26').date(),
            user_data=SubscriptionUserData(
                mtype='charge',
                cardholder_name='taro yamada',
                email='taro@test.com',
                brand='visa'
            ),
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        SubscriptionListItem(
            id='11ef3411-bbbb-4cde-9f20-2b3c4d5e6f71',
            store_id='22af6520-d53e-764d-9d4e-ef01b66fa6d1',
            transaction_token_id='11ef3414-eeee-4f01-c253-5e6f80919204',
            amount=3000,
            currency='JPY',
            amount_formatted=3000,
            status=SubscriptionStatus.CURRENT,
            merchant_name='管理画面ガイド',
            store_name='管理画面ガイド_Online店舗',
            payment_type='card',
            next_payment_date=dateutil.parser.parse('2024-08-10').date(),
            user_data=SubscriptionUserData(
                mtype='charge',
                cardholder_name='hanako suzuki',
                email='hanako@test.com',
                brand='mastercard'
            ),
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        )
    ],
    has_more=False,
    total_hits=2,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

