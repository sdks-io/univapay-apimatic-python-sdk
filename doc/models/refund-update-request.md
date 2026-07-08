
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
import jsonpickle

from univapayclientsdk.models.generic_metadata import GenericMetadata
from univapayclientsdk.models.refund_reason_request import RefundReasonRequest
from univapayclientsdk.models.refund_update_request import RefundUpdateRequest

refund_update_request = RefundUpdateRequest(
    metadata=GenericMetadata(
        order_id='12345',
        univapay_name='univapay-name8',
        univapay_phone_number='univapay-phone-number2',
        additional_properties={
            'exampleAdditionalProperty': 'String4'
        }
    ),
    message='Updated reason note',
    reason=RefundReasonRequest.DUPLICATE,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

