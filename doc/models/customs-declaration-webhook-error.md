
# Customs Declaration Webhook Error

Error payload returned when customs declaration processing fails.

*This model accepts additional fields of type Any.*

## Structure

`CustomsDeclarationWebhookError`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `code` | `int` | Optional | Backend customs declaration error code. |
| `message` | `str` | Optional | Human-readable backend error name. |
| `details` | `str` | Optional | Optional backend-provided detail string. |
| `others` | [`List[CustomsDeclarationWebhookOtherError]`](../../doc/models/customs-declaration-webhook-other-error.md) | Optional | Additional nested error records returned by the backend. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
from univapayclientsdk.models.customs_declaration_webhook_error import CustomsDeclarationWebhookError
from univapayclientsdk.models.customs_declaration_webhook_other_error import CustomsDeclarationWebhookOtherError

customs_declaration_webhook_error = CustomsDeclarationWebhookError(
    code=601,
    message='There was a processing error',
    details='Missing customs registration',
    others=[
        CustomsDeclarationWebhookOtherError(
            mtype='related_item',
            item_name='charge'
        )
    ]
)
```

