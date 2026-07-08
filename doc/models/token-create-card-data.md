
# Token Create Card Data

Token Create Card Data schema.

*This model accepts additional fields of type Any.*

## Structure

`TokenCreateCardData`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `cardholder` | `str` | Optional | Cardholder name. |
| `card_number` | `str` | Required | Card number. |
| `exp_month` | `str` | Required | Card expiration month. |
| `exp_year` | `str` | Required | Card expiration year. |
| `cvv` | `str` | Optional | Card security code. |
| `line_1` | `str` | Optional | Primary street address line. |
| `line_2` | `str` | Optional | Secondary street address line. |
| `state` | `str` | Optional | State or prefecture. |
| `city` | `str` | Optional | City or locality. |
| `country` | `str` | Optional | Country code. |
| `zip` | `str` | Optional | Postal code. |
| `phone_number` | [`TokenCreatePhoneNumber`](../../doc/models/token-create-phone-number.md) | Optional | Token Create Phone Number schema. |
| `cvv_authorize` | [`TokenCreateCardDataCvvAuthorize`](../../doc/models/token-create-card-data-cvv-authorize.md) | Optional | Token Create Card Data Cvv Authorize schema. |
| `three_ds` | [`TokenCreateCardDataThreeDs`](../../doc/models/token-create-card-data-three-ds.md) | Optional | Token Create Card Data Three Ds schema. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from univapayclientsdk.models.token_create_card_data import TokenCreateCardData

token_create_card_data = TokenCreateCardData(
    card_number='4242424242424242',
    exp_month='12',
    exp_year='2026',
    cardholder='cardholder6',
    cvv='cvv8',
    line_1='line12',
    line_2='line24',
    state='state4',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

