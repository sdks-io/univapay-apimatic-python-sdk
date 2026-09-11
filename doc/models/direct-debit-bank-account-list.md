
# Direct Debit Bank Account List

Paginated list of direct debit bank accounts.

*This model accepts additional fields of type Any.*

## Structure

`DirectDebitBankAccountList`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `items` | [`List[DirectDebitBankAccount]`](../../doc/models/direct-debit-bank-account.md) | Optional | List of resources. |
| `has_more` | `bool` | Optional | Whether more results are available. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import dateutil.parser
import jsonpickle

from univapayclientsdk.models.direct_debit_bank_account import DirectDebitBankAccount
from univapayclientsdk.models.direct_debit_bank_account_list import DirectDebitBankAccountList
from univapayclientsdk.models.direct_debit_bank_account_status import DirectDebitBankAccountStatus
from univapayclientsdk.models.direct_debit_bank_account_type import DirectDebitBankAccountType
from univapayclientsdk.models.direct_debit_registration_origin import DirectDebitRegistrationOrigin

direct_debit_bank_account_list = DirectDebitBankAccountList(
    items=[
        DirectDebitBankAccount(
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
            created_on=dateutil.parser.parse('2026-04-09T07:35:50.000Z'),
            updated_on=dateutil.parser.parse('2026-04-09T07:35:50.000Z'),
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        DirectDebitBankAccount(
            id='1098117',
            legacy_store_id='1283794',
            merchant_id='01234567-89ab-cdef-0123-456789abcdef',
            user_number='SD02688329',
            bank_code='0009',
            bank_name='ﾐﾂｲｽﾐﾄﾓ',
            branch_code='221',
            bank_account_type=DirectDebitBankAccountType.CURRENT,
            bank_account_name='ｽｽﾞｷﾀﾛｳ',
            bank_account_number='7654321',
            registration_origin=DirectDebitRegistrationOrigin.ANYWHERE,
            status=DirectDebitBankAccountStatus.INACTIVE,
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

