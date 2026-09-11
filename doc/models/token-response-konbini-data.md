
# Token Response Konbini Data

Token Response Konbini Data schema.

*This model accepts additional fields of type Any.*

## Structure

`TokenResponseKonbiniData`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `customer_name` | `str` | Optional | Customer name. |
| `convenience_store` | [`BaseKonbiniDataConvenienceStore`](../../doc/models/base-konbini-data-convenience-store.md) | Optional | Base Konbini Data Convenience Store schema. |
| `expiration_period` | `str` | Optional | ISO-8601 Duration (e.g., 'P7D'). Default is 30 days. |
| `expiration_time_shift` | `str` | Optional | Time shift applied to the expiration, typically pushing it to the end of the day in a specific timezone (e.g., '23:59:59.999999+09:00'). |
| `phone_number` | [`TokenResponsePhoneNumber`](../../doc/models/token-response-phone-number.md) | Optional | Token Response Phone Number schema. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
from univapayclientsdk.models.base_konbini_data_convenience_store import BaseKonbiniDataConvenienceStore
from univapayclientsdk.models.token_response_konbini_data import TokenResponseKonbiniData
from univapayclientsdk.models.token_response_phone_number import TokenResponsePhoneNumber

token_response_konbini_data = TokenResponseKonbiniData(
    customer_name='Taro Yamada',
    convenience_store=BaseKonbiniDataConvenienceStore.SEVEN_ELEVEN,
    expiration_period='P7D',
    expiration_time_shift=None,
    phone_number=TokenResponsePhoneNumber(
        country_code=81,
        local_number='08012341234'
    )
)
```

