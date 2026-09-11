
# Customs Declaration Webhook Other Error

Nested customs-processing error entry returned in `others`.

*This model accepts additional fields of type Any.*

## Structure

`CustomsDeclarationWebhookOtherError`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `mtype` | `str` | Optional | Backend other-error type. |
| `credentials_id` | `uuid\|str` | Optional | Gateway credentials involved in the error when applicable. |
| `message` | `List[str]` | Optional | Additional reason values for `not_selected_reasons`. |
| `item_name` | `str` | Optional | Related item name for `related_item`. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
from univapayclientsdk.models.customs_declaration_webhook_other_error import CustomsDeclarationWebhookOtherError

customs_declaration_webhook_other_error = CustomsDeclarationWebhookOtherError(
    mtype='related_item',
    item_name='charge'
)
```

