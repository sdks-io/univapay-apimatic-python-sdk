
# Direct Debit Bank Transfer Create Request

Request payload for scheduling a transfer against an active bank account.

*This model accepts additional fields of type Any.*

## Structure

`DirectDebitBankTransferCreateRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `amount` | `int` | Required | Transfer amount in JPY. Must be a positive, non-zero whole number.<br><br>**Constraints**: `>= 1` |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from univapayclientsdk.models.direct_debit_bank_transfer_create_request import DirectDebitBankTransferCreateRequest

direct_debit_bank_transfer_create_request = DirectDebitBankTransferCreateRequest(
    amount=1000,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

