
# Transaction History Status

Status of the underlying resource. Charge rows use the full set of values; refund rows only ever report `pending`, `successful`, `failed`, or `error`.

## Enumeration

`TransactionHistoryStatus`

## Fields

| Name |
|  --- |
| `PENDING` |
| `AUTHORIZED` |
| `SUCCESSFUL` |
| `FAILED` |
| `ERROR` |
| `CANCELED` |
| `AWAITING` |

## Example

```python
from univapayclientsdk.models.transaction_history_status import TransactionHistoryStatus

transaction_history_status = TransactionHistoryStatus.AWAITING
```

