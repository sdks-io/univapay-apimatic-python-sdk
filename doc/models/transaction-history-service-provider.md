
# Transaction History Service Provider

The processor or service provider that handled the payment.

## Enumeration

`TransactionHistoryServiceProvider`

## Fields

| Name |
|  --- |
| `CREDIT` |
| `CONVENIENCE` |
| `BANK_TRANSFER` |
| `PAIDY` |
| `PAY_PAY` |
| `ALIPAY` |
| `WE_CHAT` |
| `DOCOMO` |
| `MERCARI` |
| `AU` |
| `RAKUTEN` |
| `BARTONG` |
| `JKOPAY` |
| `GINKO_PAY` |
| `AEON_PAY` |
| `EROMNET` |
| `TEST` |

## Example

```python
from univapayclientsdk.models.transaction_history_service_provider import TransactionHistoryServiceProvider

transaction_history_service_provider = TransactionHistoryServiceProvider.CONVENIENCE
```

