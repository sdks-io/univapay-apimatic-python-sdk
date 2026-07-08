
# Webhook Callback Envelope

Common wrapper POSTed to your webhook URL for every event. The `data` field contains the domain object relevant to the event type.

*This model accepts additional fields of type Any.*

## Structure

`WebhookCallbackEnvelope`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `uuid\|str` | Required | Unique ID of this webhook delivery. |
| `event` | [`WebhookTrigger`](../../doc/models/webhook-trigger.md) | Required | Event type that triggers a webhook notification. |
| `created_on` | `datetime` | Required | Timestamp when the event was fired. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import dateutil.parser
import jsonpickle

from univapayclientsdk.models.webhook_callback_envelope import WebhookCallbackEnvelope
from univapayclientsdk.models.webhook_trigger import WebhookTrigger

webhook_callback_envelope = WebhookCallbackEnvelope(
    id='11ef0000-0000-4000-8000-000000000001',
    event=WebhookTrigger.CHARGE_FINISHED,
    created_on=dateutil.parser.parse('2026-04-09T07:35:50.000000Z'),
    additional_properties={
        'data': jsonpickle.decode('{"id":"6efb4e5c-690a-40f3-a4f1-0e19c5f84e98","created_on":"2024-06-26T01:51:30.000000Z"}')
    }
)
```

