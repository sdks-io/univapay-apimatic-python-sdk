
# Token Three Ds Updated Webhook Callback

Webhook envelope for the token_three_d_s_updated event.

*This model accepts additional fields of type Any.*

## Structure

`TokenThreeDsUpdatedWebhookCallback`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `uuid\|str` | Required | Unique ID of this webhook delivery. |
| `event` | `str` | Required, Constant | Event type discriminator — always `token_three_d_s_updated` for this callback.<br><br>**Value**: `"token_three_d_s_updated"` |
| `data` | [`TransactionToken`](../../doc/models/transaction-token.md) | Optional | Stored transaction token resource. |
| `created_on` | `datetime` | Required | Timestamp when the event was fired. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import dateutil.parser
import jsonpickle

from univapayclientsdk.models.token_three_ds_updated_webhook_callback import TokenThreeDsUpdatedWebhookCallback
from univapayclientsdk.models.transaction_token import TransactionToken
from univapayclientsdk.models.transaction_token_mode import TransactionTokenMode
from univapayclientsdk.models.transaction_token_payment_type import TransactionTokenPaymentType
from univapayclientsdk.models.transaction_token_type import TransactionTokenType

token_three_ds_updated_webhook_callback = TokenThreeDsUpdatedWebhookCallback(
    id='11ef0000-0000-4000-8000-000000000001',
    created_on=dateutil.parser.parse('2026-04-09T07:35:50.000000Z'),
    data=TransactionToken(
        id='6426bbd2-17bd-41bf-883b-1fe970db48ee',
        store_id='fc264608-9a9e-495e-844e-a08129a81af4',
        email='test@univapay.com',
        payment_type=TransactionTokenPaymentType.CARD,
        active=True,
        mode=TransactionTokenMode.LIVE,
        mtype=TransactionTokenType.RECURRING,
        confirmed=True,
        metadata={
            'customer_id': None
        },
        created_on=dateutil.parser.parse('2026-04-09T07:35:50.000000Z'),
        updated_on=dateutil.parser.parse('2026-04-09T07:35:50.000000Z'),
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

