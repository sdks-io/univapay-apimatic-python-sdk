
# Base Bank Transfer Data

Base Bank Transfer Data schema.

*This model accepts additional fields of type Any.*

## Structure

`BaseBankTransferData`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `brand` | `str` | Optional | The bank brand identifier (e.g., 'aozora_bank'). |
| `expiration_period` | `str` | Optional | ISO 8601 duration format (e.g., 'PT168H'). |
| `expiration_time_shift` | `str` | Optional | Time shift applied to the expiration, typically pushing it to the end of the day  in a specific timezone (e.g., '23:59:59+09:00'). |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from univapayclientsdk.models.base_bank_transfer_data import BaseBankTransferData

base_bank_transfer_data = BaseBankTransferData(
    brand='aozora_bank',
    expiration_period='PT168H',
    expiration_time_shift='23:59:59+09:00',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

