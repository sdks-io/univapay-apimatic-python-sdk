
# Charge Finished Webhook Callback

Webhook envelope for the charge_finished event.

*This model accepts additional fields of type Any.*

## Structure

`ChargeFinishedWebhookCallback`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `uuid\|str` | Required | Unique ID of this webhook delivery. |
| `event` | `str` | Required, Constant | Event type discriminator — always `charge_finished` for this callback.<br><br>**Value**: `"charge_finished"` |
| `data` | [`Charge`](../../doc/models/charge.md) | Optional | Charge resource returned by the payments API. |
| `created_on` | `datetime` | Required | Timestamp when the event was fired. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import dateutil.parser
import jsonpickle

from univapayclientsdk.models.charge import Charge
from univapayclientsdk.models.charge_finished_webhook_callback import ChargeFinishedWebhookCallback
from univapayclientsdk.models.charge_mode import ChargeMode
from univapayclientsdk.models.charge_status import ChargeStatus
from univapayclientsdk.models.charge_transaction_token_type import ChargeTransactionTokenType

charge_finished_webhook_callback = ChargeFinishedWebhookCallback(
    id='11ef0000-0000-4000-8000-000000000001',
    created_on=dateutil.parser.parse('2026-04-09T07:35:50.000000Z'),
    data=Charge(
        id='6efb4e5c-690a-40f3-a4f1-0e19c5f84e98',
        store_id='11edf541-c42d-653c-8c3d-dfe0a55f95c0',
        transaction_token_id='11ef32a7-3a71-8662-803f-1bc27702eeec',
        transaction_token_type=ChargeTransactionTokenType.RECURRING,
        subscription_id='11ef335e-9aa5-c54a-8313-7f9847da313a',
        requested_amount=1250,
        requested_currency='USD',
        requested_amount_formatted=12.5,
        charged_amount=1250,
        charged_currency='USD',
        charged_amount_formatted=12.5,
        only_direct_currency=False,
        status=ChargeStatus.SUCCESSFUL,
        error=None,
        mode=ChargeMode.TEST,
        created_on=dateutil.parser.parse('2024-06-26T01:51:30.000000Z'),
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

