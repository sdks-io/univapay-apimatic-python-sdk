
# Qr Merchant Transaction Token

Stored transaction token resource for a `qr_merchant` (QR Merchant-Presented Mode) payment type.

*This model accepts additional fields of type Any.*

## Structure

`QrMerchantTransactionToken`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `uuid\|str` | Optional | Unique identifier. |
| `store_id` | `uuid\|str` | Optional | Store identifier. |
| `email` | `str` | Optional | Customer email address. |
| `active` | `bool` | Optional | Whether the resource is active. |
| `mode` | [`TransactionTokenMode`](../../doc/models/transaction-token-mode.md) | Optional | Transaction Token Mode schema. |
| `mtype` | [`TransactionTokenType`](../../doc/models/transaction-token-type.md) | Optional | Transaction Token Type schema. |
| `usage_limit` | `str` | Optional | Usage limit applied to the token. |
| `confirmed` | `bool` | Optional | Whether the token has been confirmed. |
| `metadata` | Dict[str, str \| None \| int \| float \| bool \| List[str \| None \| int \| float \| bool]] | Optional | Alias of GenericMetadataValue, retained because this schema name is part of the published SDK surface. Do not narrow it — see GenericMetadataValue for the contract. |
| `created_on` | `datetime` | Optional | Timestamp when the resource was created. |
| `updated_on` | `datetime` | Optional | Timestamp when the resource was last updated. |
| `last_used_on` | `datetime` | Optional | Timestamp when the token was last used. |
| `payment_type` | `str` | Required, Constant | Payment method type. Always `qr_merchant` for this variant.<br><br>**Value**: `"qr_merchant"` |
| `data` | [`TokenResponseQrMerchantData`](../../doc/models/token-response-qr-merchant-data.md) | Required | Token Response Qr Merchant Data schema. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import dateutil.parser
import jsonpickle

from univapayclientsdk.models.qr_merchant_transaction_token import QrMerchantTransactionToken
from univapayclientsdk.models.token_response_qr_merchant_data import TokenResponseQrMerchantData
from univapayclientsdk.models.transaction_token_mode import TransactionTokenMode
from univapayclientsdk.models.transaction_token_type import TransactionTokenType

qr_merchant_transaction_token = QrMerchantTransactionToken(
    data=TokenResponseQrMerchantData(
        qr_image_url='71001234567890202604141200450',
        brand='pay_pay_merchant',
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    id='6426bbd2-17bd-41bf-883b-1fe970db48ee',
    store_id='fc264608-9a9e-495e-844e-a08129a81af4',
    email='test@univapay.com',
    active=True,
    mode=TransactionTokenMode.LIVE,
    mtype=TransactionTokenType.ONE_TIME,
    usage_limit='example',
    confirmed=True,
    metadata={
        'customer_id': 'cust_12345'
    },
    created_on=dateutil.parser.parse('2026-04-09T07:35:50Z'),
    updated_on=dateutil.parser.parse('2026-04-09T07:35:50Z'),
    last_used_on=dateutil.parser.parse('2026-04-09T07:35:50Z'),
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

