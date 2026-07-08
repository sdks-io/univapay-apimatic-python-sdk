
# Cancel Create Request

Request body to create a cancel for a charge. Only `metadata` is accepted; all other fields are determined server-side. The charge must be in a cancellable state.

*This model accepts additional fields of type Any.*

## Structure

`CancelCreateRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `metadata` | [`GenericMetadata`](../../doc/models/generic-metadata.md) | Optional | A free-form dictionary for custom metadata. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from univapayclientsdk.models.cancel_create_request import CancelCreateRequest
from univapayclientsdk.models.generic_metadata import GenericMetadata

cancel_create_request = CancelCreateRequest(
    metadata=GenericMetadata(
        order_id='ORD-987',
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

