
# Token Create Konbini Data

Token Create Konbini Data schema.

*This model accepts additional fields of type Any.*

## Structure

`TokenCreateKonbiniData`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `customer_name` | `str` | Required | Customer name. |
| `convenience_store` | [`BaseKonbiniDataConvenienceStore`](../../doc/models/base-konbini-data-convenience-store.md) | Required | Base Konbini Data Convenience Store schema. |
| `expiration_period` | `str` | Optional | ISO-8601 Duration (e.g., 'P7D'). Default is 30 days. |
| `phone_number` | [`TokenCreatePhoneNumber`](../../doc/models/token-create-phone-number.md) | Required | Token Create Phone Number schema. |
| `expiration_time_shift` | `str` | Optional | Expiration time shift value. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from univapayclientsdk.models.base_konbini_data_convenience_store import BaseKonbiniDataConvenienceStore
from univapayclientsdk.models.token_create_konbini_data import TokenCreateKonbiniData
from univapayclientsdk.models.token_create_phone_number import TokenCreatePhoneNumber

token_create_konbini_data = TokenCreateKonbiniData(
    customer_name='Taro Yamada',
    convenience_store=BaseKonbiniDataConvenienceStore.SEVEN_ELEVEN,
    phone_number=TokenCreatePhoneNumber(
        country_code='81',
        local_number='08012341234',
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    expiration_period='P7D',
    expiration_time_shift='23:59:59+09:00',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

