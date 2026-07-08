
# Bank Transfer Ledger List

Paginated list of bank transfer ledger entries.

*This model accepts additional fields of type Any.*

## Structure

`BankTransferLedgerList`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `items` | [`List[BankTransferLedger]`](../../doc/models/bank-transfer-ledger.md) | Optional | List of resources. |
| `has_more` | `bool` | Optional | Whether more results are available. |
| `total_hits` | `int` | Optional | Total number of matching resources. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import dateutil.parser
import jsonpickle

from univapayclientsdk.models.bank_transfer_ledger import BankTransferLedger
from univapayclientsdk.models.bank_transfer_ledger_bank_ledger_type import BankTransferLedgerBankLedgerType
from univapayclientsdk.models.bank_transfer_ledger_list import BankTransferLedgerList
from univapayclientsdk.models.bank_transfer_ledger_mode import BankTransferLedgerMode

bank_transfer_ledger_list = BankTransferLedgerList(
    items=[
        BankTransferLedger(
            bank_ledger_type=BankTransferLedgerBankLedgerType.PAYMENT,
            amount=1000,
            balance=0,
            virtual_bank_account_holder_name='test holder name',
            virtual_bank_account_number='1234567',
            virtual_account_id='test account id',
            transaction_date=dateutil.parser.parse('2024-06-25').date(),
            transaction_timestamp=dateutil.parser.parse('2024-06-25T07:29:16.367347Z'),
            mode=BankTransferLedgerMode.TEST,
            created_on=dateutil.parser.parse('2024-06-25T07:29:16.373181Z'),
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        BankTransferLedger(
            bank_ledger_type=BankTransferLedgerBankLedgerType.DEPOSIT,
            amount=1000,
            balance=1000,
            virtual_bank_account_holder_name='test holder name',
            virtual_bank_account_number='1234567',
            virtual_account_id='test account id',
            transaction_date=dateutil.parser.parse('2024-06-25').date(),
            transaction_timestamp=dateutil.parser.parse('2024-06-25T07:29:16.36731Z'),
            mode=BankTransferLedgerMode.TEST,
            created_on=dateutil.parser.parse('2024-06-25T07:29:16.368093Z'),
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        )
    ],
    has_more=False,
    total_hits=2,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

