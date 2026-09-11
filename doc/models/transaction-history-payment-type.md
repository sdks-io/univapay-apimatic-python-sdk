
# Transaction History Payment Type

The payment method used for the underlying charge.

## Enumeration

`TransactionHistoryPaymentType`

## Fields

| Name |
|  --- |
| `CARD` |
| `QR_SCAN` |
| `QR_MERCHANT` |
| `KONBINI` |
| `APPLE_PAY` |
| `PAIDY` |
| `ONLINE` |
| `BANK_TRANSFER` |

## Example

```python
from univapayclientsdk.models.transaction_history_payment_type import TransactionHistoryPaymentType

transaction_history_payment_type = TransactionHistoryPaymentType.APPLE_PAY
```

