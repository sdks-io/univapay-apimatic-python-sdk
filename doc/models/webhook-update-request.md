
# Webhook Update Request

Request body for updating a webhook. All fields are optional. Omitted fields are left unchanged.

*This model accepts additional fields of type Any.*

## Structure

`WebhookUpdateRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `triggers` | [`List[WebhookTrigger]`](../../doc/models/webhook-trigger.md) | Optional | Replace the trigger list. Must be non-empty if provided. |
| `url` | `str` | Optional | Update the webhook endpoint URL. |
| `auth_token` | `str` | Optional | Update or clear the auth token. Send `null` to remove. |
| `active` | `bool` | Optional | Enable or disable the webhook. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from univapayclientsdk.models.webhook_trigger import WebhookTrigger
from univapayclientsdk.models.webhook_update_request import WebhookUpdateRequest

webhook_update_request = WebhookUpdateRequest(
    triggers=[
        WebhookTrigger.TOKEN_UPDATED,
        WebhookTrigger.TOKEN_THREE_D_S_UPDATED,
        WebhookTrigger.TOKEN_CVV_AUTH_UPDATED
    ],
    url='url4',
    auth_token='auth_token6',
    active=False,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

