
# Subscription Created Webhook Callback

Webhook envelope for the subscription_created event.

*This model accepts additional fields of type Any.*

## Structure

`SubscriptionCreatedWebhookCallback`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `uuid\|str` | Required | Unique ID of this webhook delivery. |
| `event` | `str` | Required, Constant | Event type discriminator — always `subscription_created` for this callback.<br><br>**Value**: `"subscription_created"` |
| `data` | [`Subscription`](../../doc/models/subscription.md) | Optional | The Subscription object represents a recurring payment schedule. |
| `created_on` | `datetime` | Required | Timestamp when the event was fired. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import dateutil.parser
import jsonpickle

from univapayclientsdk.models.charge_mode import ChargeMode
from univapayclientsdk.models.generic_metadata import GenericMetadata
from univapayclientsdk.models.subscription import Subscription
from univapayclientsdk.models.subscription_created_webhook_callback import SubscriptionCreatedWebhookCallback
from univapayclientsdk.models.subscription_period import SubscriptionPeriod
from univapayclientsdk.models.subscription_schedule_settings import SubscriptionScheduleSettings
from univapayclientsdk.models.subscription_status import SubscriptionStatus
from univapayclientsdk.models.subscription_termination_mode import SubscriptionTerminationMode

subscription_created_webhook_callback = SubscriptionCreatedWebhookCallback(
    id='11ef0000-0000-4000-8000-000000000001',
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
        period=SubscriptionPeriod.MONTHLY,
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

