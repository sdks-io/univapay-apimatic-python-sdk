
# Customs Declaration Create Request

Request body for creating a customs declaration. Backend currently accepts this shape only for WeChat Online and WeChat MPM charges.

*This model accepts additional fields of type Any.*

## Structure

`CustomsDeclarationCreateRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `customs` | `str` | Required | WeChat customs authority code used for the declaration. |
| `merchant_customs_no` | `str` | Required | Merchant customs registration number. |
| `certificate_id` | `str` | Required | Customer certificate or passport identifier used by customs. |
| `certificate_name` | `str` | Required | Customer name exactly as shown on the certificate. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
from univapayclientsdk.models.customs_declaration_create_request import CustomsDeclarationCreateRequest

customs_declaration_create_request = CustomsDeclarationCreateRequest(
    customs='TOKYO',
    merchant_customs_no='1234567890',
    certificate_id='AB1234567',
    certificate_name='TARO YAMADA'
)
```

