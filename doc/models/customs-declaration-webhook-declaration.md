
# Customs Declaration Webhook Declaration

WeChat customs declaration payload returned by the backend formatter.

*This model accepts additional fields of type Any.*

## Structure

`CustomsDeclarationWebhookDeclaration`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `customs` | `str` | Optional | WeChat customs authority code. |
| `merchant_customs_no` | `str` | Optional | Merchant customs registration number. |
| `certificate_id` | `str` | Optional | Customer certificate or passport identifier. |
| `certificate_name` | `str` | Optional | Customer name as provided to customs. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
from univapayclientsdk.models.customs_declaration_webhook_declaration import CustomsDeclarationWebhookDeclaration

customs_declaration_webhook_declaration = CustomsDeclarationWebhookDeclaration(
    customs='TOKYO',
    merchant_customs_no='1234567890',
    certificate_id='AB1234567',
    certificate_name='TARO YAMADA'
)
```

