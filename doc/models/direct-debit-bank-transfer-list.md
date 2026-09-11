
# Direct Debit Bank Transfer List

Paginated list of direct debit bank transfers.

*This model accepts additional fields of type Any.*

## Structure

`DirectDebitBankTransferList`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `items` | [`List[DirectDebitBankTransfer]`](../../doc/models/direct-debit-bank-transfer.md) | Optional | List of resources. |
| `has_more` | `bool` | Optional | Whether more results are available. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import dateutil.parser
import jsonpickle

from univapayclientsdk.models.direct_debit_bank_account_type import DirectDebitBankAccountType
from univapayclientsdk.models.direct_debit_bank_transfer import DirectDebitBankTransfer
from univapayclientsdk.models.direct_debit_bank_transfer_error import DirectDebitBankTransferError
from univapayclientsdk.models.direct_debit_bank_transfer_list import DirectDebitBankTransferList
from univapayclientsdk.models.direct_debit_bank_transfer_lock import DirectDebitBankTransferLock
from univapayclientsdk.models.direct_debit_bank_transfer_status import DirectDebitBankTransferStatus
from univapayclientsdk.models.direct_debit_debit_date import DirectDebitDebitDate

direct_debit_bank_transfer_list = DirectDebitBankTransferList(
    items=[
        DirectDebitBankTransfer(
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
            error=None,
            created_on=dateutil.parser.parse('2026-04-09T07:35:50.000Z'),
            updated_on=dateutil.parser.parse('2026-04-09T07:35:50.000Z'),
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        DirectDebitBankTransfer(
            id='2594977',
            legacy_store_id='1283794',
            merchant_id='01234567-89ab-cdef-0123-456789abcdef',
            bank_account_id='1098117',
            user_number='SD02688329',
            bank_code='0009',
            bank_name='ﾐﾂｲｽﾐﾄﾓ',
            branch_code='221',
            bank_account_type=DirectDebitBankAccountType.CURRENT,
            bank_account_name='ｽｽﾞｷﾀﾛｳ',
            bank_account_number='7654321',
            amount=1850,
            debit_date=DirectDebitDebitDate.TWENTY_SEVEN,
            calculated_debit_date=dateutil.parser.parse('2026-03-27').date(),
            lock=DirectDebitBankTransferLock.LOCKED,
            status=DirectDebitBankTransferStatus.FAILED,
            error=DirectDebitBankTransferError.INSUFFICIENT_FUNDS,
            created_on=dateutil.parser.parse('2026-04-10T09:12:04.000Z'),
            updated_on=dateutil.parser.parse('2026-04-12T11:03:41.000Z'),
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        )
    ],
    has_more=False,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

