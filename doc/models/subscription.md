
# Subscription

The Subscription object represents a recurring payment schedule.

*This model accepts additional fields of type Any.*

## Structure

`Subscription`

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
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import dateutil.parser
import jsonpickle

from univapayclientsdk.models.charge_mode import ChargeMode
from univapayclientsdk.models.generic_metadata import GenericMetadata
from univapayclientsdk.models.subscription import Subscription
from univapayclientsdk.models.subscription_next_payment import SubscriptionNextPayment
from univapayclientsdk.models.subscription_period import SubscriptionPeriod
from univapayclientsdk.models.subscription_schedule_settings import SubscriptionScheduleSettings
from univapayclientsdk.models.subscription_status import SubscriptionStatus

subscription = Subscription(
    id='11ef335e-9aa5-c54a-8313-7f9847da313a',
    store_id='11edf541-c42d-653c-8c3d-dfe0a55f95c0',
    transaction_token_id='11ef32a7-3a71-8662-803f-1bc27702eeec',
    amount=1250,
    currency='USD',
    amount_formatted=12.5,
    schedule_settings=SubscriptionScheduleSettings(),
    only_direct_currency=False,
    first_charge_authorization_only=False,
    status=SubscriptionStatus.CURRENT,
    metadata=GenericMetadata(
        order_id='12345'
    ),
    mode=ChargeMode.LIVE,
    created_on=dateutil.parser.parse('2024-06-26T01:51:28.627023Z'),
    period=SubscriptionPeriod.MONTHLY,
    next_payment=SubscriptionNextPayment(),
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

