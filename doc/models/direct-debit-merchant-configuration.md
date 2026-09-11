
# Direct Debit Merchant Configuration

The merchant's effective direct debit configuration.

*This model accepts additional fields of type Any.*

## Structure

`DirectDebitMerchantConfiguration`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `legacy_id` | `str` | Optional | Identifier of the merchant in the legacy direct debit system.<br><br>**Constraints**: *Pattern*: `^[0-9]+$` |
| `enabled` | `bool` | Optional | Whether direct debit is enabled for this merchant. |
| `debit_date` | [`DirectDebitDebitDate`](../../doc/models/direct-debit-debit-date.md) | Optional | Monthly debit cycle — funds are pulled on either the 14th or the 27th. |
| `consignor_code` | `str` | Optional | Consignor code (委託者コード) assigned by the collecting bank.<br><br>**Constraints**: *Minimum Length*: `6`, *Maximum Length*: `6`, *Pattern*: `^[0-9]{6}$` |
| `classifier` | `str` | Optional | Transfer classification code (区分) agreed with the collecting bank.<br><br>**Constraints**: *Minimum Length*: `2`, *Maximum Length*: `2`, *Pattern*: `^[0-9]{2}$` |
| `signature` | `str` | Optional | Name printed on the consumer's bank statement (印字名), in half-width katakana. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from univapayclientsdk.models.direct_debit_debit_date import DirectDebitDebitDate
from univapayclientsdk.models.direct_debit_merchant_configuration import DirectDebitMerchantConfiguration

direct_debit_merchant_configuration = DirectDebitMerchantConfiguration(
    legacy_id='1283794',
    enabled=True,
    debit_date=DirectDebitDebitDate.FOURTEEN,
    consignor_code='135456',
    classifier='99',
    signature='モモサン',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

