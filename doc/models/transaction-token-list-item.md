
# Transaction Token List Item

Transaction token entry returned in list responses.

*This model accepts additional fields of type Any.*

## Structure

`TransactionTokenListItem`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `uuid\|str` | Optional | Unique identifier. |
| `store_id` | `uuid\|str` | Optional | Store identifier. |
| `merchant_name` | `str` | Optional | Merchant display name. |
| `store_name` | `str` | Optional | Store display name. |
| `email` | `str` | Optional | Customer email address. |
| `payment_type` | `str` | Optional | Payment method type. |
| `active` | `bool` | Optional | Whether the resource is active. |
| `mode` | `str` | Optional | Processing mode for the resource. |
| `mtype` | `str` | Optional | Type of the resource. |
| `created_on` | `datetime` | Optional | Timestamp when the resource was created. |
| `updated_on` | `datetime` | Optional | Timestamp when the resource was last updated. |
| `user_data` | [`TransactionTokenListItemUserData`](../../doc/models/transaction-token-list-item-user-data.md) | Optional | Transaction Token List Item User Data schema. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import dateutil.parser
import jsonpickle

from univapayclientsdk.models.transaction_token_list_item import TransactionTokenListItem
from univapayclientsdk.models.transaction_token_list_item_user_data import TransactionTokenListItemUserData

transaction_token_list_item = TransactionTokenListItem(
    id='2fe23e45-f95d-4c95-9963-739070096443',
    store_id='79e9504e-96d8-46ed-8d22-2e8b36238605',
    merchant_name='Test Merchant',
    store_name='Tokyo Store',
    email='user@example.com',
    payment_type='card',
    active=True,
    mode='live',
    mtype='one_time',
    created_on=dateutil.parser.parse('2026-04-09T07:35:50Z'),
    updated_on=dateutil.parser.parse('2026-04-09T07:35:50Z'),
    user_data=TransactionTokenListItemUserData(
        cardholder_name='TARO YAMADA',
        email='user@example.com',
        brand='visa'
    ),
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

