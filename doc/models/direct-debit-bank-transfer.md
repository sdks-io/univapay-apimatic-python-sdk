
# Direct Debit Bank Transfer

A single scheduled pull of funds from a registered bank account. The bank account details are copied onto the transfer at registration time, so later edits to the account do not change past transfers.

*This model accepts additional fields of type Any.*

## Structure

`DirectDebitBankTransfer`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Optional | Unique identifier of a direct debit bank transfer (振替ID).<br><br>**Constraints**: *Pattern*: `^[0-9]+$` |
| `legacy_store_id` | `str` | Optional | Identifier of the merchant in the legacy direct debit system.<br><br>**Constraints**: *Pattern*: `^[0-9]+$` |
| `merchant_id` | `uuid\|str` | Optional | The merchant that owns this transfer. |
| `bank_account_id` | `str` | Optional | Unique identifier of a direct debit bank account (銀行口座ID).<br><br>**Constraints**: *Pattern*: `^[0-9]+$` |
| `user_number` | `str` | Optional | The merchant's own membership number for the consumer (会員番号). Alphanumeric.<br><br>**Constraints**: *Pattern*: `^[a-zA-Z0-9]+$` |
| `bank_code` | `str` | Optional | Four-digit code identifying the consumer's bank (銀行コード).<br><br>**Constraints**: *Minimum Length*: `4`, *Maximum Length*: `4`, *Pattern*: `^[0-9]{4}$` |
| `bank_name` | `str` | Optional | Bank name in half-width katakana (銀行名).<br><br>**Constraints**: *Maximum Length*: `15` |
| `branch_code` | `str` | Optional | Three-digit code identifying the bank branch (支店コード).<br><br>**Constraints**: *Minimum Length*: `3`, *Maximum Length*: `3`, *Pattern*: `^[0-9]{3}$` |
| `bank_account_type` | [`DirectDebitBankAccountType`](../../doc/models/direct-debit-bank-account-type.md) | Optional | Deposit account type (預金種類) — `regular` (普通), `current` (当座), `savings` (貯蓄) or `others` (その他). |
| `bank_account_name` | `str` | Optional | Account holder name (口座名義), in half-width katakana. Full-width characters are rejected by the bank.<br><br>**Constraints**: *Maximum Length*: `30`, *Pattern*: `^[A-Z0-9ｱ-ﾝﾞﾟ().\- ]{1,30}$` |
| `bank_account_number` | `str` | Optional | Seven-digit account number (口座番号).<br><br>**Constraints**: *Minimum Length*: `7`, *Maximum Length*: `7`, *Pattern*: `^[0-9]{7}$` |
| `amount` | `int` | Optional | Transfer amount in JPY. Must be a positive, non-zero whole number.<br><br>**Constraints**: `>= 1` |
| `debit_date` | [`DirectDebitDebitDate`](../../doc/models/direct-debit-debit-date.md) | Optional | Monthly debit cycle — funds are pulled on either the 14th or the 27th. |
| `calculated_debit_date` | `date` | Optional | The actual business day on which funds are pulled (計算された振替日), derived from the debit cycle. |
| `lock` | [`DirectDebitBankTransferLock`](../../doc/models/direct-debit-bank-transfer-lock.md) | Optional | Whether the transfer can still be edited. Transfers are `unlocked` until the upload deadline for their debit cycle passes, after which they are `locked` and can no longer be changed or deleted. |
| `status` | [`DirectDebitBankTransferStatus`](../../doc/models/direct-debit-bank-transfer-status.md) | Optional | Transfer state. `awaiting` until the bank reports back, then `successful` or `failed`. Results are reflected days after the debit date, not immediately. |
| `error` | [`DirectDebitBankTransferError`](../../doc/models/direct-debit-bank-transfer-error.md) | Optional | Failure reason, or null while the transfer is awaiting a result or has succeeded. |
| `created_on` | `datetime` | Optional | Timestamp when the resource was created. |
| `updated_on` | `datetime` | Optional | Timestamp when the resource was last updated. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import dateutil.parser
import jsonpickle

from univapayclientsdk.models.direct_debit_bank_account_type import DirectDebitBankAccountType
from univapayclientsdk.models.direct_debit_bank_transfer import DirectDebitBankTransfer
from univapayclientsdk.models.direct_debit_bank_transfer_error import DirectDebitBankTransferError
from univapayclientsdk.models.direct_debit_bank_transfer_lock import DirectDebitBankTransferLock
from univapayclientsdk.models.direct_debit_bank_transfer_status import DirectDebitBankTransferStatus
from univapayclientsdk.models.direct_debit_debit_date import DirectDebitDebitDate

direct_debit_bank_transfer = DirectDebitBankTransfer(
    id='2594976',
    legacy_store_id='1283794',
    merchant_id='01234567-89ab-cdef-0123-456789abcdef',
    bank_account_id='1098116',
    user_number='SD02688328',
    bank_code='0012',
    bank_name='ﾗｸﾃﾝｷﾞﾝｺｳ',
    branch_code='120',
    bank_account_type=DirectDebitBankAccountType.REGULAR,
    bank_account_name='ﾀﾅｶﾕﾐｺ',
    bank_account_number='1234567',
    amount=1000,
    debit_date=DirectDebitDebitDate.FOURTEEN,
    calculated_debit_date=dateutil.parser.parse('2026-03-14').date(),
    lock=DirectDebitBankTransferLock.UNLOCKED,
    status=DirectDebitBankTransferStatus.AWAITING,
    error=DirectDebitBankTransferError.INSUFFICIENT_FUNDS,
    created_on=dateutil.parser.parse('2026-04-09T07:35:50Z'),
    updated_on=dateutil.parser.parse('2026-04-09T07:35:50Z'),
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

