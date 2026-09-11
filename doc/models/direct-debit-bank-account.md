
# Direct Debit Bank Account

A consumer bank account registered for direct debit.

*This model accepts additional fields of type Any.*

## Structure

`DirectDebitBankAccount`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Optional | Unique identifier of a direct debit bank account (銀行口座ID).<br><br>**Constraints**: *Pattern*: `^[0-9]+$` |
| `legacy_store_id` | `str` | Optional | Identifier of the merchant in the legacy direct debit system.<br><br>**Constraints**: *Pattern*: `^[0-9]+$` |
| `merchant_id` | `uuid\|str` | Optional | The merchant that owns this bank account. |
| `user_number` | `str` | Optional | The merchant's own membership number for the consumer (会員番号). Alphanumeric.<br><br>**Constraints**: *Pattern*: `^[a-zA-Z0-9]+$` |
| `bank_code` | `str` | Optional | Four-digit code identifying the consumer's bank (銀行コード).<br><br>**Constraints**: *Minimum Length*: `4`, *Maximum Length*: `4`, *Pattern*: `^[0-9]{4}$` |
| `bank_name` | `str` | Optional | Bank name in half-width katakana (銀行名).<br><br>**Constraints**: *Maximum Length*: `15` |
| `branch_code` | `str` | Optional | Three-digit code identifying the bank branch (支店コード).<br><br>**Constraints**: *Minimum Length*: `3`, *Maximum Length*: `3`, *Pattern*: `^[0-9]{3}$` |
| `bank_account_type` | [`DirectDebitBankAccountType`](../../doc/models/direct-debit-bank-account-type.md) | Optional | Deposit account type (預金種類) — `regular` (普通), `current` (当座), `savings` (貯蓄) or `others` (その他). |
| `bank_account_name` | `str` | Optional | Account holder name (口座名義), in half-width katakana. Full-width characters are rejected by the bank.<br><br>**Constraints**: *Maximum Length*: `30`, *Pattern*: `^[A-Z0-9ｱ-ﾝﾞﾟ().\- ]{1,30}$` |
| `bank_account_number` | `str` | Optional | Seven-digit account number (口座番号).<br><br>**Constraints**: *Minimum Length*: `7`, *Maximum Length*: `7`, *Pattern*: `^[0-9]{7}$` |
| `registration_origin` | [`DirectDebitRegistrationOrigin`](../../doc/models/direct-debit-registration-origin.md) | Optional | Where the bank account was registered from — `merchant_console` for the merchant dashboard, `anywhere` otherwise. |
| `status` | [`DirectDebitBankAccountStatus`](../../doc/models/direct-debit-bank-account-status.md) | Optional | Bank account state (有効・無効・登録失敗). Only an `active` account can have transfers registered against it. `registration_failed` means the bank rejected the account details. |
| `created_on` | `datetime` | Optional | Timestamp when the resource was created. |
| `updated_on` | `datetime` | Optional | Timestamp when the resource was last updated. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import dateutil.parser
import jsonpickle

from univapayclientsdk.models.direct_debit_bank_account import DirectDebitBankAccount
from univapayclientsdk.models.direct_debit_bank_account_status import DirectDebitBankAccountStatus
from univapayclientsdk.models.direct_debit_bank_account_type import DirectDebitBankAccountType
from univapayclientsdk.models.direct_debit_registration_origin import DirectDebitRegistrationOrigin

direct_debit_bank_account = DirectDebitBankAccount(
    id='1098116',
    legacy_store_id='1283794',
    merchant_id='01234567-89ab-cdef-0123-456789abcdef',
    user_number='SD02688328',
    bank_code='0012',
    bank_name='ﾗｸﾃﾝｷﾞﾝｺｳ',
    branch_code='120',
    bank_account_type=DirectDebitBankAccountType.REGULAR,
    bank_account_name='ﾀﾅｶﾕﾐｺ',
    bank_account_number='1234567',
    registration_origin=DirectDebitRegistrationOrigin.MERCHANT_CONSOLE,
    status=DirectDebitBankAccountStatus.ACTIVE,
    created_on=dateutil.parser.parse('2026-04-09T07:35:50Z'),
    updated_on=dateutil.parser.parse('2026-04-09T07:35:50Z'),
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

