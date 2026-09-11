
# Transaction History Refund Status

Status of a single refund entry.

## Enumeration

`TransactionHistoryRefundStatus`

## Fields

| Name |
|  --- |
| `PENDING` |
| `SUCCESSFUL` |
| `FAILED` |
| `ERROR` |

## Example

```python
from univapayclientsdk.models.transaction_history_refund_status import TransactionHistoryRefundStatus

transaction_history_refund_status = TransactionHistoryRefundStatus.FAILED
```

