
# Token Response Bank Transfer Data

Token Response Bank Transfer Data schema.

*This model accepts additional fields of type Any.*

## Structure

`TokenResponseBankTransferData`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `brand` | `str` | Optional | The bank brand identifier (e.g., 'aozora_bank'). |
| `expiration_period` | `str` | Optional | ISO 8601 duration format (e.g., 'PT168H'). |
| `expiration_time_shift` | `str` | Optional | Time shift applied to the expiration, typically pushing it to the end of the day  in a specific timezone (e.g., '23:59:59+09:00'). |
| `bank_code` | `str` | Optional | Bank code value. |
| `bank_name` | `str` | Optional | Bank name value. |
| `branch_code` | `str` | Optional | Bank branch code. |
| `branch_name` | `str` | Optional | Bank branch name. |
| `account_number` | `str` | Optional | Bank account number. |
| `account_holder_name` | `str` | Optional | Bank account holder name. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
from univapayclientsdk.models.token_response_bank_transfer_data import TokenResponseBankTransferData

token_response_bank_transfer_data = TokenResponseBankTransferData(
    brand='aozora_bank',
    expiration_period='PT168H',
    expiration_time_shift='23:59:59+09:00',
    bank_code='0310',
    bank_name='GMOあおぞらネット銀行',
    branch_code='123',
    branch_name='Test Branch',
    account_number='1234567',
    account_holder_name='TARO YAMADA'
)
```

