
# Webhook Event List

Paginated list of webhook events.

*This model accepts additional fields of type Any.*

## Structure

`WebhookEventList`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `items` | [`List[WebhookEvent]`](../../doc/models/webhook-event.md) | Optional | List of resources. |
| `has_more` | `bool` | Optional | Whether more results are available. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import dateutil.parser
import jsonpickle

from univapayclientsdk.models.webhook_event import WebhookEvent
from univapayclientsdk.models.webhook_event_list import WebhookEventList
from univapayclientsdk.models.webhook_trigger import WebhookTrigger

webhook_event_list = WebhookEventList(
    items=[
        WebhookEvent(
            id='e1f2a3b4-c5d6-7890-efab-123456789cde',
            webhook_id='d3e4f5a6-b7c8-9012-def0-123456789abc',
            event=WebhookTrigger.CHARGE_FINISHED,
            data=jsonpickle.decode('{"key1":"val1","key2":"val2"}'),
            successful=True,
            fired_on=dateutil.parser.parse('2026-04-09T07:36:00.000000Z'),
            error_message=None,
            created_on=dateutil.parser.parse('2026-04-09T07:35:50.000000Z'),
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        WebhookEvent(
            id='f2a3b4c5-d6e7-8901-fabc-23456789cdef',
            webhook_id='d3e4f5a6-b7c8-9012-def0-123456789abc',
            event=WebhookTrigger.REFUND_FINISHED,
            data=jsonpickle.decode('{"key1":"val1","key2":"val2"}'),
            successful=True,
            fired_on=dateutil.parser.parse('2026-04-10T11:00:05.000000Z'),
            error_message=None,
            created_on=dateutil.parser.parse('2026-04-10T11:00:00.000000Z'),
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

