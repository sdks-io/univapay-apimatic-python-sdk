
# Token Response Card Data Card

Token Response Card Data Card schema.

*This model accepts additional fields of type Any.*

## Structure

`TokenResponseCardDataCard`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `cardholder` | `str` | Optional | Cardholder name. |
| `exp_month` | `int` | Optional | Card expiration month. |
| `exp_year` | `int` | Optional | Card expiration year. |
| `card_bin` | `str` | Optional | Card bin value. |
| `last_four` | `str` | Optional | Last four value. |
| `brand` | `str` | Optional | Brand or network name. |
| `card_type` | `str` | Optional | Card type value. |
| `country` | `str` | Optional | Country code. |
| `category` | `str` | Optional | Category value. |
| `issuer` | `str` | Optional | Issuer value. |
| `sub_brand` | `str` | Optional | Sub brand value. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
from univapayclientsdk.models.token_response_card_data_card import TokenResponseCardDataCard

token_response_card_data_card = TokenResponseCardDataCard(
    cardholder='TARO YAMADA',
    exp_month=12,
    exp_year=2026,
    card_bin='424242',
    last_four='4242',
    brand='visa',
    card_type='credit',
    country='JP',
    category='standard',
    issuer=None,
    sub_brand='none'
)
```

