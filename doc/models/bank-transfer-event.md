
# Bank Transfer Event

Event type discriminator — always `bank_transfer_status_updated` for this callback.

## Enumeration

`BankTransferEvent`

## Fields

| Name |
|  --- |
| `BANK_TRANSFER_STATUS_UPDATED` |

## Example

```python
from univapayclientsdk.models.bank_transfer_event import BankTransferEvent

bank_transfer_event = BankTransferEvent.BANK_TRANSFER_STATUS_UPDATED
```

