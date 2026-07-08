
# Transaction Token

Stored transaction token resource.

*This model accepts additional fields of type Any.*

## Structure

`TransactionToken`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `uuid\|str` | Optional | Unique identifier. |
| `store_id` | `uuid\|str` | Optional | Store identifier. |
| `email` | `str` | Optional | Customer email address. |
| `payment_type` | [`TransactionTokenPaymentType`](../../doc/models/transaction-token-payment-type.md) | Optional | Transaction Token Payment Type schema. |
| `active` | `bool` | Optional | Whether the resource is active. |
| `mode` | [`TransactionTokenMode`](../../doc/models/transaction-token-mode.md) | Optional | Transaction Token Mode schema. |
| `mtype` | [`TransactionTokenType`](../../doc/models/transaction-token-type.md) | Optional | Transaction Token Type schema. |
| `usage_limit` | `str` | Optional | Usage limit applied to the token. |
| `confirmed` | `bool` | Optional | Whether the token has been confirmed. |
| `metadata` | Dict[str, str \| float \| bool] \| None | Optional | Transaction Token Metadata Additional Properties schema. |
| `created_on` | `datetime` | Optional | Timestamp when the resource was created. |
| `updated_on` | `datetime` | Optional | Timestamp when the resource was last updated. |
| `last_used_on` | `datetime` | Optional | Timestamp when the token was last used. |
| `data` | [TokenResponseCardData](../../doc/models/token-response-card-data.md) \| [TokenResponseKonbiniData](../../doc/models/token-response-konbini-data.md) \| [TokenResponseOnlineData](../../doc/models/token-response-online-data.md) \| [TokenResponseBankTransferData](../../doc/models/token-response-bank-transfer-data.md) \| None | Optional | Transaction token data payload. The actual structure depends on `payment_type` — card, konbini, online (QR / 3DS), or bank transfer. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import dateutil.parser
import jsonpickle

from univapayclientsdk.models.transaction_token import TransactionToken
from univapayclientsdk.models.transaction_token_mode import TransactionTokenMode
from univapayclientsdk.models.transaction_token_payment_type import TransactionTokenPaymentType
from univapayclientsdk.models.transaction_token_type import TransactionTokenType

transaction_token = TransactionToken(
    id='6426bbd2-17bd-41bf-883b-1fe970db48ee',
    store_id='fc264608-9a9e-495e-844e-a08129a81af4',
    email='test@univapay.com',
    payment_type=TransactionTokenPaymentType.CARD,
    active=True,
    mode=TransactionTokenMode.LIVE,
    mtype=TransactionTokenType.ONE_TIME,
    usage_limit='example',
    confirmed=True,
    metadata={
        'customer_id': None
    },
    created_on=dateutil.parser.parse('2026-04-09T07:35:50Z'),
    updated_on=dateutil.parser.parse('2026-04-09T07:35:50Z'),
    last_used_on=dateutil.parser.parse('2026-04-09T07:35:50Z'),
    data=None,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

