
# Refund Update Request

Request body for updating a refund. All fields are optional. Omitted fields are left unchanged.

*This model accepts additional fields of type Any.*

## Structure

`RefundUpdateRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `metadata` | [`GenericMetadata`](../../doc/models/generic-metadata.md) | Optional | A free-form dictionary for custom metadata. |
| `message` | `str` | Optional | Update or clear the refund note. Send `null` to remove. |
| `reason` | [`RefundReasonRequest`](../../doc/models/refund-reason-request.md) | Optional | Merchant-settable refund reason, or `null` to remove it during update. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
from univapayclientsdk.models.generic_metadata import GenericMetadata
from univapayclientsdk.models.refund_update_request import RefundUpdateRequest

refund_update_request = RefundUpdateRequest(
    metadata=GenericMetadata(
        order_id='12345'
    ),
    message='Updated reason note'
)
```

