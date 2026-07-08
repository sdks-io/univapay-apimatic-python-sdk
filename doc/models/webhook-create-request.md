
# Webhook Create Request

Request body to create a new store-level webhook subscription.

*This model accepts additional fields of type Any.*

## Structure

`WebhookCreateRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `triggers` | [`List[WebhookTrigger]`](../../doc/models/webhook-trigger.md) | Required | List of event types that trigger this webhook. Must be non-empty and contain only events valid for the store level. |
| `url` | `str` | Required | The URL to POST webhook payloads to. |
| `auth_token` | `str` | Optional | Optional bearer token sent in the `Authorization` header of webhook requests. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from univapayclientsdk.models.webhook_create_request import WebhookCreateRequest
from univapayclientsdk.models.webhook_trigger import WebhookTrigger

webhook_create_request = WebhookCreateRequest(
    triggers=[
        WebhookTrigger.CHARGE_FINISHED
    ],
    url='https://example.com/webhooks/payments',
    auth_token='my-secret-token',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

