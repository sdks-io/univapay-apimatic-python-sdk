
# Transaction Token Update Request

Request payload for updating a transaction token.

*This model accepts additional fields of type Any.*

## Structure

`TransactionTokenUpdateRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `email` | `str` | Optional | Customer email address. |
| `metadata` | [`GenericMetadata`](../../doc/models/generic-metadata.md) | Optional | A free-form dictionary for custom metadata. |
| `data` | [`TransactionTokenUpdateRequestData`](../../doc/models/transaction-token-update-request-data.md) | Optional | Transaction Token Update Request Data schema. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from univapayclientsdk.models.generic_metadata import GenericMetadata
from univapayclientsdk.models.transaction_token_update_request import TransactionTokenUpdateRequest
from univapayclientsdk.models.transaction_token_update_request_data import TransactionTokenUpdateRequestData

transaction_token_update_request = TransactionTokenUpdateRequest(
    email='new_email@test.com',
    metadata=GenericMetadata(
        order_id='12345',
        univapay_name='univapay-name8',
        univapay_phone_number='univapay-phone-number2',
        additional_properties={
            'exampleAdditionalProperty': 'String4'
        }
    ),
    data=TransactionTokenUpdateRequestData(
        cvv='123',
        cardholder='TARO YAMADA',
        card_number='card_number6',
        exp_month=12,
        exp_year=2028,
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

