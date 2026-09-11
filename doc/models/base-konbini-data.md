
# Base Konbini Data

Base Konbini Data schema.

*This model accepts additional fields of type Any.*

## Structure

`BaseKonbiniData`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `customer_name` | `str` | Optional | Customer name. |
| `convenience_store` | [`BaseKonbiniDataConvenienceStore`](../../doc/models/base-konbini-data-convenience-store.md) | Optional | Base Konbini Data Convenience Store schema. |
| `expiration_period` | `str` | Optional | ISO-8601 Duration (e.g., 'P7D'). Default is 30 days. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
from univapayclientsdk.models.base_konbini_data import BaseKonbiniData
from univapayclientsdk.models.base_konbini_data_convenience_store import BaseKonbiniDataConvenienceStore

base_konbini_data = BaseKonbiniData(
    customer_name='Taro Yamada',
    convenience_store=BaseKonbiniDataConvenienceStore.SEVEN_ELEVEN,
    expiration_period='P7D'
)
```

