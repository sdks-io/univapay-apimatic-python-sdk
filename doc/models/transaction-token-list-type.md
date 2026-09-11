
# Transaction Token List Type

Filterable token types for token listings. `one_time` tokens cannot be filtered on and are excluded from this enum.

## Enumeration

`TransactionTokenListType`

## Fields

| Name |
|  --- |
| `SUBSCRIPTION` |
| `RECURRING` |

## Example

```python
from univapayclientsdk.models.transaction_token_list_type import TransactionTokenListType

transaction_token_list_type = TransactionTokenListType.SUBSCRIPTION
```

