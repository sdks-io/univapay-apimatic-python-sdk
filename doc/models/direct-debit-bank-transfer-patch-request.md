
# Direct Debit Bank Transfer Patch Request

Request payload for changing a transfer's amount. Only permitted while the transfer is unlocked.

*This model accepts additional fields of type Any.*

## Structure

`DirectDebitBankTransferPatchRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `amount` | `int` | Required | Transfer amount in JPY. Must be a positive, non-zero whole number.<br><br>**Constraints**: `>= 1` |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from univapayclientsdk.models.direct_debit_bank_transfer_patch_request import DirectDebitBankTransferPatchRequest

direct_debit_bank_transfer_patch_request = DirectDebitBankTransferPatchRequest(
    amount=1000,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

