
# Checkout Bank Transfer Configuration

Bank transfer (振込) payment settings applied to checkout.

*This model accepts additional fields of type Any.*

## Structure

`CheckoutBankTransferConfiguration`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `enabled` | `bool` | Optional | Whether bank transfer payments are enabled. |
| `match_amount` | [`CheckoutBankTransferMatchAmount`](../../doc/models/checkout-bank-transfer-match-amount.md) | Optional | Deposit-matching policy applied to bank transfer payments. |
| `expiration` | `str` | Optional | ISO-8601 duration before a bank transfer payment expires. |
| `expiration_time_shift` | [`ExpirationTimeShift`](../../doc/models/expiration-time-shift.md) | Optional | Time-of-day override applied when calculating expirations, shared by convenience-store and bank-transfer configuration. |
| `virtual_bank_accounts_threshold` | `int` | Optional | Number of unused virtual bank accounts that triggers provisioning of additional accounts.<br><br>**Constraints**: `>= 0` |
| `virtual_bank_accounts_fetch_count` | `int` | Optional | Number of virtual bank accounts provisioned per replenishment.<br><br>**Constraints**: `>= 1` |
| `default_extension_period` | `str` | Optional | ISO-8601 duration by which a payment deadline is extended by default. |
| `maximum_extension_period` | `str` | Optional | ISO-8601 duration for the maximum allowed extension. |
| `automatic_extension_enabled` | `bool` | Optional | Whether payment deadlines are extended automatically. |
| `charge_request_notification_enabled` | `bool` | Optional | Whether a notification is sent when a bank transfer charge is requested. |
| `charge_request_canceled_notification_enabled` | `bool` | Optional | Whether a notification is sent when a requested bank transfer charge is canceled. |
| `charge_expired_notification_enabled` | `bool` | Optional | Whether a notification is sent when a bank transfer charge expires. |
| `deposit_received_notification_enabled` | `bool` | Optional | Whether a notification is sent when a deposit is received. |
| `deposit_insufficient_notification_enabled` | `bool` | Optional | Whether a notification is sent when a deposit is insufficient. |
| `deposit_exceeded_notification_enabled` | `bool` | Optional | Whether a notification is sent when a deposit exceeds the requested amount. |
| `extension_notification_enabled` | `bool` | Optional | Whether a notification is sent when a payment deadline is extended. |
| `remind_notification_period` | `str` | Optional | ISO-8601 duration before expiration at which a reminder notification is sent. |
| `remind_notification_enabled` | `bool` | Optional | Whether reminder notifications are sent before a payment deadline. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from univapayclientsdk.models.checkout_bank_transfer_configuration import CheckoutBankTransferConfiguration
from univapayclientsdk.models.checkout_bank_transfer_match_amount import CheckoutBankTransferMatchAmount
from univapayclientsdk.models.expiration_time_shift import ExpirationTimeShift

checkout_bank_transfer_configuration = CheckoutBankTransferConfiguration(
    enabled=True,
    match_amount=CheckoutBankTransferMatchAmount.DISABLED,
    expiration='PT72H',
    expiration_time_shift=ExpirationTimeShift(
        value='value4',
        enabled=False,
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    virtual_bank_accounts_threshold=5,
    virtual_bank_accounts_fetch_count=10,
    default_extension_period='PT168H',
    maximum_extension_period='PT168H',
    automatic_extension_enabled=False,
    charge_request_notification_enabled=False,
    charge_request_canceled_notification_enabled=False,
    charge_expired_notification_enabled=False,
    deposit_received_notification_enabled=False,
    deposit_insufficient_notification_enabled=False,
    deposit_exceeded_notification_enabled=False,
    extension_notification_enabled=False,
    remind_notification_period='PT168H',
    remind_notification_enabled=False,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

