
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
from univapayclientsdk.models.webhook_event import WebhookEvent

webhook_event = WebhookEvent()
```

