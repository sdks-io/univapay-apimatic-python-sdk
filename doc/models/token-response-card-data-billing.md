
# Token Response Card Data Billing

Token Response Card Data Billing schema.

*This model accepts additional fields of type Any.*

## Structure

`TokenResponseCardDataBilling`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `line_1` | `str` | Optional | Primary street address line. |
| `line_2` | `str` | Optional | Secondary street address line. |
| `state` | `str` | Optional | State or prefecture. |
| `city` | `str` | Optional | City or locality. |
| `country` | `str` | Optional | Country code. |
| `zip` | `str` | Optional | Postal code. |
| `phone_number` | [`TokenResponsePhoneNumber`](../../doc/models/token-response-phone-number.md) | Optional | Token Response Phone Number schema. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
from univapayclientsdk.models.token_response_card_data_billing import TokenResponseCardDataBilling
from univapayclientsdk.models.token_response_phone_number import TokenResponsePhoneNumber

token_response_card_data_billing = TokenResponseCardDataBilling(
    line_1='1-1-1',
    line_2='Shibakoen',
    state='Tokyo',
    city='Minato',
    country='JP',
    zip='105-0011',
    phone_number=TokenResponsePhoneNumber(
        country_code=81,
        local_number='08012341234'
    )
)
```

