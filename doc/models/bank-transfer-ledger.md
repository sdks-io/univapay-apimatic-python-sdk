
# Bank Transfer Ledger

Single bank transfer ledger entry associated with a charge.

*This model accepts additional fields of type Any.*

## Structure

`BankTransferLedger`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `bank_ledger_type` | [`BankTransferLedgerBankLedgerType`](../../doc/models/bank-transfer-ledger-bank-ledger-type.md) | Optional | Bank Transfer Ledger Bank Ledger Type schema. |
| `amount` | `int` | Optional | Amount in the smallest currency unit. |
| `balance` | `int` | Optional | Current balance in the smallest currency unit. |
| `virtual_bank_account_holder_name` | `str` | Optional | Virtual bank account holder name. |
| `virtual_bank_account_number` | `str` | Optional | Virtual bank account number. |
| `virtual_account_id` | `str` | Optional | Virtual account id value. |
| `transaction_date` | `date` | Optional | Transaction date. |
| `transaction_timestamp` | `datetime` | Optional | Transaction timestamp. |
| `mode` | [`BankTransferLedgerMode`](../../doc/models/bank-transfer-ledger-mode.md) | Optional | Bank Transfer Ledger Mode schema. |
| `created_on` | `datetime` | Optional | Timestamp when the resource was created. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import dateutil.parser
import jsonpickle

from univapayclientsdk.models.bank_transfer_ledger import BankTransferLedger
from univapayclientsdk.models.bank_transfer_ledger_bank_ledger_type import BankTransferLedgerBankLedgerType
from univapayclientsdk.models.bank_transfer_ledger_mode import BankTransferLedgerMode

bank_transfer_ledger = BankTransferLedger(
    bank_ledger_type=BankTransferLedgerBankLedgerType.DEPOSIT,
    amount=1000,
    balance=1000,
    virtual_bank_account_holder_name='TARO YAMADA',
    virtual_bank_account_number='1234567',
    virtual_account_id='va_12345',
    transaction_date=dateutil.parser.parse('2026-04-09').date(),
    transaction_timestamp=dateutil.parser.parse('2026-04-09T07:35:50Z'),
    mode=BankTransferLedgerMode.LIVE,
    created_on=dateutil.parser.parse('2026-04-09T07:35:50Z'),
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

