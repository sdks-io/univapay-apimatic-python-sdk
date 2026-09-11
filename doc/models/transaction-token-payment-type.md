
# Transaction Token Payment Type

Transaction Token Payment Type schema.

## Enumeration

`TransactionTokenPaymentType`

## Fields

| Name |
|  --- |
| `CARD` |
| `PAIDY` |
| `ONLINE` |
| `KONBINI` |
| `BANK_TRANSFER` |
| `QR_SCAN` |
| `QR_MERCHANT` |

## Example

```python
from univapayclientsdk.models.transaction_token_payment_type import TransactionTokenPaymentType

transaction_token_payment_type = TransactionTokenPaymentType.BANK_TRANSFER
```

