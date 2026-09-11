
# Customs Declaration Patch Request

Request body for updating a customs declaration. Backend patch handling keeps the original `customs`, `certificate_id`, and `certificate_name` values and only accepts a new `merchant_customs_no`.

*This model accepts additional fields of type Any.*

## Structure

`CustomsDeclarationPatchRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `merchant_customs_no` | `str` | Required | Updated merchant customs registration number. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
from univapayclientsdk.models.customs_declaration_patch_request import CustomsDeclarationPatchRequest

customs_declaration_patch_request = CustomsDeclarationPatchRequest(
    merchant_customs_no='1234567891'
)
```

