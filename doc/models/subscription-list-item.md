
# Subscription List Item

Subscription entry returned in list responses.

*This model accepts additional fields of type Any.*

## Structure

`SubscriptionListItem`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `uuid\|str` | Optional | Unique identifier. |
| `store_id` | `uuid\|str` | Optional | Store identifier. |
| `transaction_token_id` | `uuid\|str` | Optional | Transaction token identifier. |
| `amount` | `int` | Optional | Amount in the smallest currency unit. |
| `currency` | `str` | Optional | ISO-4217 currency code. |
| `amount_formatted` | `float` | Optional | Amount formatted for display. |
| `initial_amount` | `int` | Optional | Initial amount in the smallest currency unit. |
| `initial_amount_formatted` | `float` | Optional | Initial amount formatted for display. |
| `subsequent_cycles_start` | `datetime` | Optional | Timestamp when recurring cycles begin. |
| `schedule_settings` | [`SubscriptionScheduleSettings`](../../doc/models/subscription-schedule-settings.md) | Optional | Schedule settings applied to a subscription. |
| `only_direct_currency` | `bool` | Optional | Whether only direct currency processing is allowed. |
| `first_charge_capture_after` | `str` | Optional | ISO-8601 Duration (e.g., P3D). |
| `first_charge_authorization_only` | `bool` | Optional | Whether the first charge is authorization-only. |
| `status` | [`SubscriptionStatus`](../../doc/models/subscription-status.md) | Optional | Subscription Status schema. |
| `metadata` | [`GenericMetadata`](../../doc/models/generic-metadata.md) | Optional | A free-form dictionary for custom metadata. |
| `mode` | [`ChargeMode`](../../doc/models/charge-mode.md) | Optional | Charge Mode schema. |
| `created_on` | `datetime` | Optional | Timestamp when the resource was created. |
| `period` | [`SubscriptionPeriod`](../../doc/models/subscription-period.md) | Optional | Subscription Period schema. |
| `next_payment` | [`SubscriptionNextPayment`](../../doc/models/subscription-next-payment.md) | Optional | Next scheduled payment details for a subscription. |
| `merchant_name` | `str` | Optional | Merchant display name. |
| `store_name` | `str` | Optional | Store display name. |
| `payment_type` | `str` | Optional | Payment method type. |
| `next_payment_date` | `date` | Optional | Next payment date value. |
| `user_data` | [`SubscriptionUserData`](../../doc/models/subscription-user-data.md) | Optional | Customer-facing payment method summary data. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import dateutil.parser
import jsonpickle

from univapayclientsdk.models.subscription_list_item import SubscriptionListItem
from univapayclientsdk.models.subscription_status import SubscriptionStatus
from univapayclientsdk.models.subscription_user_data import SubscriptionUserData

subscription_list_item = SubscriptionListItem(
    id='11ef335e-9aa5-c54a-8313-7f9847da313a',
    store_id='11edf541-c42d-653c-8c3d-dfe0a55f95c0',
    transaction_token_id='11ef32a7-3a71-8662-803f-1bc27702eeec',
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
        email='test@test.com',
        brand='visa'
    ),
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

