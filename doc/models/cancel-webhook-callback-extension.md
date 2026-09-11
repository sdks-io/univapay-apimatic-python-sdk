
# Cancel Webhook Callback Extension

Cancel-specific webhook payload extension.

*This model accepts additional fields of type Any.*

## Structure

`CancelWebhookCallbackExtension`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `data` | [`Cancel`](../../doc/models/cancel.md) | Optional | Represents a cancellation request for a charge. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import dateutil.parser

from univapayclientsdk.models.cancel import Cancel
from univapayclientsdk.models.cancel_status import CancelStatus
from univapayclientsdk.models.cancel_webhook_callback_extension import CancelWebhookCallbackExtension
from univapayclientsdk.models.charge_mode import ChargeMode
from univapayclientsdk.models.generic_metadata import GenericMetadata

cancel_webhook_callback_extension = CancelWebhookCallbackExtension(
    data=Cancel(
        id='a1b2c3d4-e5f6-7890-abcd-ef1234567890',
        charge_id='6efb4e5c-690a-40f3-a4f1-0e19c5f84e98',
        store_id='76cf4a64-02bc-4cb3-9a28-74622e5928a1',
        status=CancelStatus.SUCCESSFUL,
        error=None,
        metadata=GenericMetadata(
            order_id='order_12345'
        ),
        mode=ChargeMode.LIVE,
        created_on=dateutil.parser.parse('2026-04-09T07:35:50.000000Z'),
        updated_on=dateutil.parser.parse('2026-04-09T07:36:00.000000Z')
    )
)
```

