
# Transaction Token Create Request

Request payload for creating a transaction token, which represents a payment method to charge against.

*This model accepts additional fields of type Any.*

## Structure

`TransactionTokenCreateRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `payment_type` | [`TransactionTokenCreateRequestPaymentType`](../../doc/models/transaction-token-create-request-payment-type.md) | Required | Transaction Token Create Request Payment Type schema. |
| `mtype` | [`TransactionTokenCreateRequestType`](../../doc/models/transaction-token-create-request-type.md) | Required | Transaction Token Create Request Type schema. |
| `email` | `str` | Optional | Customer email address. |
| `usage_limit` | `str` | Optional | Usage limit applied to the token. |
| `ip_address` | `str` | Optional | Consumer's IPv4 address. **Required** when `data.brand` is `we_chat_online` and `data.call_method` is `web` or `http_get`. |
| `metadata` | [`TransactionTokenCreateRequestMetadata`](../../doc/models/transaction-token-create-request-metadata.md) | Optional | A free-form dictionary for custom metadata. |
| `data` | [TokenCreateCardData](../../doc/models/token-create-card-data.md) \| [TokenCreateKonbiniData](../../doc/models/token-create-konbini-data.md) \| [TokenCreateOnlineData](../../doc/models/token-create-online-data.md) \| [TokenCreateBankTransferData](../../doc/models/token-create-bank-transfer-data.md) \| [TokenCreatePaidyData](../../doc/models/token-create-paidy-data.md) \| [TokenCreateQrScanData](../../doc/models/token-create-qr-scan-data.md) \| [TokenCreateQrMerchantData](../../doc/models/token-create-qr-merchant-data.md) | Required | Transaction Token Create Request Data schema. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from univapayclientsdk.models.token_create_card_data import TokenCreateCardData
from univapayclientsdk.models.transaction_token_create_request import TransactionTokenCreateRequest
from univapayclientsdk.models.transaction_token_create_request_metadata import TransactionTokenCreateRequestMetadata
from univapayclientsdk.models.transaction_token_create_request_payment_type import TransactionTokenCreateRequestPaymentType
from univapayclientsdk.models.transaction_token_create_request_type import TransactionTokenCreateRequestType

transaction_token_create_request = TransactionTokenCreateRequest(
    payment_type=TransactionTokenCreateRequestPaymentType.CARD,
    mtype=TransactionTokenCreateRequestType.ONE_TIME,
    data=TokenCreateCardData(
        card_number='4242424242424242',
        exp_month='12',
        exp_year='2026',
        cardholder='cardholder4',
        cvv='cvv6',
        line_1='line10',
        line_2='line22',
        state='state6',
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    email='user@example.com',
    usage_limit='daily',
    ip_address='198.51.100.14',
    metadata=TransactionTokenCreateRequestMetadata(
        univapay_reference_id='ref-998877',
        univapay_customer_id='0fd29949-07d5-4a91-8eaf-fbce0897d944',
        univapay_name='univapay-name8',
        univapay_phone_number='univapay-phone-number2',
        additional_properties={
            'exampleAdditionalProperty': 'String8'
        }
    ),
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

