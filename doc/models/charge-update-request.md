
# Charge Update Request

Request payload for updating charge metadata.

*This model accepts additional fields of type Any.*

## Structure

`ChargeUpdateRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `metadata` | [`GenericMetadata`](../../doc/models/generic-metadata.md) | Optional | A free-form dictionary for custom metadata. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from univapayclientsdk.models.charge_update_request import ChargeUpdateRequest
from univapayclientsdk.models.generic_metadata import GenericMetadata

charge_update_request = ChargeUpdateRequest(
    metadata=GenericMetadata(
        order_id='12347',
        univapay_name='univapay-name8',
        univapay_phone_number='univapay-phone-number2',
        additional_properties={
            'exampleAdditionalProperty': 'String4'
        }
    ),
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

