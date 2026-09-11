
# Token Create Phone Number

Token Create Phone Number schema.

*This model accepts additional fields of type Any.*

## Structure

`TokenCreatePhoneNumber`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `country_code` | `str` | Required | Country code as string (e.g., '1' or '81'). |
| `local_number` | `str` | Required | Local phone number.<br><br>**Constraints**: *Maximum Length*: `15` |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
from univapayclientsdk.models.token_create_phone_number import TokenCreatePhoneNumber

token_create_phone_number = TokenCreatePhoneNumber(
    country_code='81',
    local_number='08012341234'
)
```

