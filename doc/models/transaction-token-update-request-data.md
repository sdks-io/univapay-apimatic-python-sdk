
# Transaction Token Update Request Data

Transaction Token Update Request Data schema.

*This model accepts additional fields of type Any.*

## Structure

`TransactionTokenUpdateRequestData`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `cvv` | `str` | Optional | Update if RECURRING_USAGE_REQUIRES_CVV error occurs. |
| `cardholder` | `str` | Optional | Cardholder name. |
| `card_number` | `str` | Optional | Card number. |
| `exp_month` | `int` | Optional | Card expiration month. |
| `exp_year` | `int` | Optional | Card expiration year. |
| `line_1` | `str` | Optional | Primary street address line. |
| `line_2` | `str` | Optional | Secondary street address line. |
| `state` | `str` | Optional | State or prefecture. |
| `city` | `str` | Optional | City or locality. |
| `country` | `str` | Optional | Country code. |
| `zip` | `str` | Optional | Postal code. |
| `phone_number` | [`TransactionTokenUpdateRequestDataPhoneNumber`](../../doc/models/transaction-token-update-request-data-phone-number.md) | Optional | Transaction Token Update Request Data Phone Number schema. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
from univapayclientsdk.models.transaction_token_update_request_data import TransactionTokenUpdateRequestData
from univapayclientsdk.models.transaction_token_update_request_data_phone_number import TransactionTokenUpdateRequestDataPhoneNumber

transaction_token_update_request_data = TransactionTokenUpdateRequestData(
    cvv='123',
    cardholder='TARO YAMADA',
    card_number='4242424242424242',
    exp_month=12,
    exp_year=2026,
    line_1='1-1-1',
    line_2='Shibakoen',
    state='Tokyo',
    city='Minato',
    country='JP',
    zip='105-0011',
    phone_number=TransactionTokenUpdateRequestDataPhoneNumber(
        country_code='81',
        local_number='08012341234'
    )
)
```

