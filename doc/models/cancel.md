
# Cancel

Represents a cancellation request for a charge.

*This model accepts additional fields of type Any.*

## Structure

`Cancel`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `uuid\|str` | Optional | Unique identifier for the cancel. |
| `charge_id` | `uuid\|str` | Optional | ID of the charge this cancel is associated with. |
| `store_id` | `uuid\|str` | Optional | ID of the store. |
| `status` | [`CancelStatus`](../../doc/models/cancel-status.md) | Optional | Current status of the cancel operation. |
| `error` | [`PaymentError`](../../doc/models/payment-error.md) | Optional | Payment error details, or null if successful. |
| `metadata` | [`GenericMetadata`](../../doc/models/generic-metadata.md) | Optional | A free-form dictionary for custom metadata. |
| `mode` | [`ChargeMode`](../../doc/models/charge-mode.md) | Optional | Charge Mode schema. |
| `created_on` | `datetime` | Optional | Timestamp when the cancel was created. |
| `updated_on` | `datetime` | Optional | Timestamp when the cancel was last updated. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import dateutil.parser
import jsonpickle

from univapayclientsdk.models.cancel import Cancel
from univapayclientsdk.models.cancel_status import CancelStatus
from univapayclientsdk.models.charge_mode import ChargeMode
from univapayclientsdk.models.generic_metadata import GenericMetadata
from univapayclientsdk.models.payment_error import PaymentError

cancel = Cancel(
    id='a1b2c3d4-e5f6-7890-abcd-ef1234567890',
    charge_id='6efb4e5c-690a-40f3-a4f1-0e19c5f84e98',
    store_id='76cf4a64-02bc-4cb3-9a28-74622e5928a1',
    status=CancelStatus.PENDING,
    error=PaymentError(
        code=301,
        message='Card number error.',
        detail='The provided card number failed validation.',
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    metadata=GenericMetadata(
        order_id='12345',
        univapay_name='univapay-name8',
        univapay_phone_number='univapay-phone-number2',
        additional_properties={
            'exampleAdditionalProperty': 'String4'
        }
    ),
    mode=ChargeMode.LIVE,
    created_on=dateutil.parser.parse('2026-04-09T07:35:50Z'),
    updated_on=dateutil.parser.parse('2026-04-09T07:36:00Z'),
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

