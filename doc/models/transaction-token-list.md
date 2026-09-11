
# Transaction Token List

Paginated list of transaction tokens.

*This model accepts additional fields of type Any.*

## Structure

`TransactionTokenList`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `items` | [`List[TransactionTokenListItem]`](../../doc/models/transaction-token-list-item.md) | Optional | List of resources. |
| `has_more` | `bool` | Optional | Whether more results are available. |
| `total_hits` | `int` | Optional | Total number of matching resources. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import dateutil.parser
import jsonpickle

from univapayclientsdk.models.transaction_token_list import TransactionTokenList
from univapayclientsdk.models.transaction_token_list_item import TransactionTokenListItem
from univapayclientsdk.models.transaction_token_list_item_user_data import TransactionTokenListItemUserData

transaction_token_list = TransactionTokenList(
    items=[
        TransactionTokenListItem(
            id='2fe23e45-f95d-4c95-9963-739070096443',
            store_id='79e9504e-96d8-46ed-8d22-2e8b36238605',
            merchant_name='Test Merchant',
            store_name='Tokyo Store',
            email='taro@example.com',
            payment_type='card',
            active=True,
            mode='live',
            mtype='recurring',
            created_on=dateutil.parser.parse('2026-04-09T07:35:50Z'),
            updated_on=dateutil.parser.parse('2026-04-09T07:35:50Z'),
            user_data=TransactionTokenListItemUserData(
                cardholder_name='TARO YAMADA',
                email='taro@example.com',
                brand='brand0',
                additional_properties={
                    'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                }
            ),
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        TransactionTokenListItem(
            id='3af34f56-a06e-4d06-aa74-84a181107554',
            store_id='8bfa615f-a7e9-47fe-9e33-3f9c47349716',
            merchant_name='Test Merchant',
            store_name='Osaka Store',
            email='hanako@example.com',
            payment_type='card',
            active=True,
            mode='live',
            mtype='one_time',
            created_on=dateutil.parser.parse('2026-04-10T10:20:11Z'),
            updated_on=dateutil.parser.parse('2026-04-10T10:20:11Z'),
            user_data=TransactionTokenListItemUserData(
                cardholder_name='HANAKO SUZUKI',
                email='hanako@example.com',
                brand='brand0',
                additional_properties={
                    'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                }
            ),
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        )
    ],
    has_more=False,
    total_hits=2,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

