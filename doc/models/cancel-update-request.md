
# Cancel Update Request

Request body for updating a cancel. Only `metadata` is settable by merchants. All fields are optional; omitted fields are left unchanged.

*This model accepts additional fields of type Any.*

## Structure

`CancelUpdateRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `metadata` | [`GenericMetadata`](../../doc/models/generic-metadata.md) | Optional | A free-form dictionary for custom metadata. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
from univapayclientsdk.models.cancel_update_request import CancelUpdateRequest
from univapayclientsdk.models.generic_metadata import GenericMetadata

cancel_update_request = CancelUpdateRequest(
    metadata=GenericMetadata(
        order_id='12345'
    )
)
```

