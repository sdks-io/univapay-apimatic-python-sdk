
# Bank Transfer Status Webhook Callback Extension

Bank-transfer-specific webhook payload extension.

*This model accepts additional fields of type Any.*

## Structure

`BankTransferStatusWebhookCallbackExtension`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `data` | [`BankTransferStatusData`](../../doc/models/bank-transfer-status-data.md) | Optional | Data payload for `bank_transfer_status_updated` webhook events. Contains the bank transfer extension fields inlined alongside amount and metadata. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import dateutil.parser
import jsonpickle

from univapayclientsdk.models.bank_transfer_payment_status import BankTransferPaymentStatus
from univapayclientsdk.models.bank_transfer_status_data import BankTransferStatusData
from univapayclientsdk.models.bank_transfer_status_webhook_callback_extension import BankTransferStatusWebhookCallbackExtension
from univapayclientsdk.models.generic_metadata import GenericMetadata

bank_transfer_status_webhook_callback_extension = BankTransferStatusWebhookCallbackExtension(
    data=BankTransferStatusData(
        id='11ef0000-0000-4000-8000-000000000002',
        charge_id='11ef0000-0000-4000-8000-000000000001',
        payment_status=BankTransferPaymentStatus.EXACT,
        latest_deposit_date=dateutil.parser.parse('2026-04-09T07:35:50.000000Z'),
        created_on=dateutil.parser.parse('2026-04-09T07:35:50.000000Z'),
        latest_deposit_amount=1000,
        balance=0,
        currency='JPY',
        amount=1000,
        amount_difference=0,
        token_metadata=GenericMetadata(
            order_id='12345'
        ),
        charge_metadata=GenericMetadata(
            order_id='order_12345'
        ),
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

