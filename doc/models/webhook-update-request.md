
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
from univapayclientsdk.models.webhook_update_request import WebhookUpdateRequest

webhook_update_request = WebhookUpdateRequest(
    active=False
)
```

