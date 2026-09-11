
# Transaction Token List Item User Data

Transaction Token List Item User Data schema.

*This model accepts additional fields of type Any.*

## Structure

`TransactionTokenListItemUserData`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `cardholder_name` | `str` | Optional | Cardholder name value. |
| `email` | `str` | Optional | Customer email address. |
| `brand` | `str` | Optional | Brand or network name. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
from univapayclientsdk.models.transaction_token_list_item_user_data import TransactionTokenListItemUserData

transaction_token_list_item_user_data = TransactionTokenListItemUserData(
    cardholder_name='TARO YAMADA',
    email='user@example.com',
    brand='visa'
)
```

