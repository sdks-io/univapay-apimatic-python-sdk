
# Webhook Event

Represents a single delivery attempt of a webhook event, including the payload sent and the delivery outcome.

*This model accepts additional fields of type Any.*

## Structure

`WebhookEvent`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `uuid\|str` | Optional | Unique identifier for the webhook event. |
| `webhook_id` | `uuid\|str` | Optional | ID of the parent webhook. |
| `event` | [`WebhookTrigger`](../../doc/models/webhook-trigger.md) | Optional | Event type that triggers a webhook notification. |
| `data` | `Any` | Optional | Domain object payload for webhook deliveries. The actual structure depends on the event type — see each webhook callback schema for the specific payload shape. |
| `successful` | `bool` | Optional | Whether the webhook delivery was acknowledged (HTTP 2xx). |
| `fired_on` | `datetime` | Optional | Timestamp when the webhook was dispatched. |
| `error_message` | `str` | Optional | Error message if delivery failed. |
| `created_on` | `datetime` | Optional | Timestamp when the event was created. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from univapayclientsdk.models.webhook_event import WebhookEvent
from univapayclientsdk.models.webhook_trigger import WebhookTrigger

webhook_event = WebhookEvent(
    id='00000188-0000-0000-0000-000000000000',
    webhook_id='000023ae-0000-0000-0000-000000000000',
    event=WebhookTrigger.TOKEN_CREATED,
    data=jsonpickle.decode('{"key1":"val1","key2":"val2"}'),
    successful=False,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

