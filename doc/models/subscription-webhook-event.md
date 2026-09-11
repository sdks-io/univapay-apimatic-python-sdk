
# Subscription Webhook Event

Webhook envelope for subscription lifecycle events. Fired as `subscription_created` when a subscription is created and its first payment initiated, `subscription_payment` when a scheduled payment processes successfully, `subscription_completed` when all scheduled payments complete, `subscription_failure` when a scheduled payment fails, `subscription_canceled` when a subscription is cancelled before all payments complete, and `subscription_suspended` when a subscription is paused. The `data` field contains the full Subscription object at the time of the event.

*This model accepts additional fields of type Any.*

## Structure

`SubscriptionWebhookEvent`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `uuid\|str` | Required | Unique ID of this webhook delivery. |
| `event` | [`SubscriptionEvent`](../../doc/models/subscription-event.md) | Required | Event type discriminator — `subscription_created`, `subscription_payment`, `subscription_completed`, `subscription_failure`, `subscription_canceled`, or `subscription_suspended`. |
| `data` | [`Subscription`](../../doc/models/subscription.md) | Optional | The Subscription object represents a recurring payment schedule. |
| `created_on` | `datetime` | Required | Timestamp when the event was fired. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import dateutil.parser

from univapayclientsdk.models.charge_mode import ChargeMode
from univapayclientsdk.models.generic_metadata import GenericMetadata
from univapayclientsdk.models.subscription import Subscription
from univapayclientsdk.models.subscription_event import SubscriptionEvent
from univapayclientsdk.models.subscription_period import SubscriptionPeriod
from univapayclientsdk.models.subscription_schedule_settings import SubscriptionScheduleSettings
from univapayclientsdk.models.subscription_status import SubscriptionStatus
from univapayclientsdk.models.subscription_termination_mode import SubscriptionTerminationMode
from univapayclientsdk.models.subscription_webhook_event import SubscriptionWebhookEvent

subscription_webhook_event = SubscriptionWebhookEvent(
    id='11ef0000-0000-4000-8000-000000000001',
    event=SubscriptionEvent.SUBSCRIPTION_CREATED,
    created_on=dateutil.parser.parse('2026-04-09T07:35:50.000000Z'),
    data=Subscription(
        id='11ef335e-9aa5-c54a-8313-7f9847da313a',
        store_id='11edf541-c42d-653c-8c3d-dfe0a55f95c0',
        transaction_token_id='11ef32a7-3a71-8662-803f-1bc27702eeec',
        amount=1250,
        currency='USD',
        amount_formatted=12.5,
        schedule_settings=SubscriptionScheduleSettings(
            start_on=dateutil.parser.parse('2024-07-01').date(),
            zone_id='Asia/Tokyo',
            preserve_end_of_month=False,
            retry_interval='P7D',
            termination_mode=SubscriptionTerminationMode.ON_NEXT_PAYMENT
        ),
        only_direct_currency=False,
        first_charge_authorization_only=False,
        status=SubscriptionStatus.CURRENT,
        metadata=GenericMetadata(
            order_id='12345'
        ),
        mode=ChargeMode.TEST,
        created_on=dateutil.parser.parse('2024-06-26T01:51:28.627023Z'),
        period=SubscriptionPeriod.MONTHLY
    )
)
```

