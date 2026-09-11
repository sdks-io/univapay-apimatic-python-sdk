
# Token Create Card Data Cvv Authorize

Token Create Card Data Cvv Authorize schema.

*This model accepts additional fields of type Any.*

## Structure

`TokenCreateCardDataCvvAuthorize`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `enabled` | `bool` | Optional | Enabled value.<br><br>**Default**: `False` |
| `currency` | `str` | Optional | ISO-4217 currency code. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
from univapayclientsdk.models.token_create_card_data_cvv_authorize import TokenCreateCardDataCvvAuthorize

token_create_card_data_cvv_authorize = TokenCreateCardDataCvvAuthorize(
    enabled=False,
    currency='JPY'
)
```

