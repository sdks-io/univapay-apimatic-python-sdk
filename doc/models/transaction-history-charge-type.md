
# Transaction History Charge Type

Whether the underlying charge was a normal charge or a CVV authorization.

## Enumeration

`TransactionHistoryChargeType`

## Fields

| Name |
|  --- |
| `NORMAL` |
| `CVV_AUTH` |

## Example

```python
from univapayclientsdk.models.transaction_history_charge_type import TransactionHistoryChargeType

transaction_history_charge_type = TransactionHistoryChargeType.NORMAL
```

