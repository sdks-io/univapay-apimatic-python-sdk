
# Token Create Bank Transfer Data

Token Create Bank Transfer Data schema.

*This model accepts additional fields of type Any.*

## Structure

`TokenCreateBankTransferData`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `brand` | `str` | Required | The bank brand identifier (e.g., 'aozora_bank'). |
| `expiration_period` | `str` | Optional | ISO 8601 duration format (e.g., 'PT168H'). |
| `expiration_time_shift` | `str` | Optional | Time shift applied to the expiration, typically pushing it to the end of the day  in a specific timezone (e.g., '23:59:59+09:00'). |
| `name` | `str` | Optional | The name of the customer initiating the transfer. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from univapayclientsdk.models.token_create_bank_transfer_data import TokenCreateBankTransferData

token_create_bank_transfer_data = TokenCreateBankTransferData(
    brand='aozora_bank',
    expiration_period='PT168H',
    expiration_time_shift='23:59:59+09:00',
    name='Taro Yamada',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

