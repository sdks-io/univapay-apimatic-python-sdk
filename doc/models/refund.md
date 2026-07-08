
# Refund

Represents a refund issued against a charge.

*This model accepts additional fields of type Any.*

## Structure

`Refund`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `uuid\|str` | Optional | Unique identifier. |
| `store_id` | `uuid\|str` | Optional | Store identifier. |
| `charge_id` | `uuid\|str` | Optional | Charge identifier. |
| `status` | [`RefundStatus`](../../doc/models/refund-status.md) | Optional | Current status of the refund. `pending`: The refund has been created and is being processed. `successful`: The refund was processed successfully. `failed`: The refund was rejected by the gateway. `error`: An unexpected error occurred during processing. |
| `amount` | `int` | Optional | Refund amount in the smallest currency unit (e.g., cents for USD, yen for JPY). |
| `currency` | `str` | Optional | ISO-4217 currency code. Must match the charged currency. |
| `amount_formatted` | `float` | Optional | Refund amount formatted for display. |
| `reason` | [`RefundReasonResponse`](../../doc/models/refund-reason-response.md) | Optional | Refund reason returned by the API, or `null` when unset. |
| `message` | `str` | Optional | Optional free-text note about the refund. |
| `error` | [`PaymentError`](../../doc/models/payment-error.md) | Optional | Payment error details, or null if successful. |
| `metadata` | [`GenericMetadata`](../../doc/models/generic-metadata.md) | Optional | A free-form dictionary for custom metadata. |
| `mode` | [`ChargeMode`](../../doc/models/charge-mode.md) | Optional | Charge Mode schema. |
| `created_on` | `datetime` | Optional | Timestamp when the resource was created. |
| `updated_on` | `datetime` | Optional | Timestamp when the resource was last updated. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import dateutil.parser
import jsonpickle

from univapayclientsdk.models.charge_mode import ChargeMode
from univapayclientsdk.models.generic_metadata import GenericMetadata
from univapayclientsdk.models.payment_error import PaymentError
from univapayclientsdk.models.refund import Refund
from univapayclientsdk.models.refund_reason_response import RefundReasonResponse
from univapayclientsdk.models.refund_status import RefundStatus

refund = Refund(
    id='b4d9fea9-c9b3-4e76-a25d-b61f7e4821b6',
    store_id='76cf4a64-02bc-4cb3-9a28-74622e5928a1',
    charge_id='6efb4e5c-690a-40f3-a4f1-0e19c5f84e98',
    status=RefundStatus.PENDING,
    amount=1000,
    currency='JPY',
    amount_formatted=1000,
    reason=RefundReasonResponse.CUSTOMER_REQUEST,
    message='Customer returned item',
    error=PaymentError(
        code=301,
        message='Card number error.',
        detail='The provided card number failed validation.'
    ),
    metadata=GenericMetadata(
        order_id='12345'
    ),
    mode=ChargeMode.LIVE,
    created_on=dateutil.parser.parse('2026-04-09T07:35:50Z'),
    updated_on=dateutil.parser.parse('2026-04-09T07:36:00Z'),
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

