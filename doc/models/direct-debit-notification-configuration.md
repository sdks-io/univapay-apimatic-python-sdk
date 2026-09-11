
# Direct Debit Notification Configuration

Which direct debit email notifications the merchant has opted into.

*This model accepts additional fields of type Any.*

## Structure

`DirectDebitNotificationConfiguration`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `notify_deadline_mailing` | `bool` | Optional | Notify when the deadline for the bank to receive the signed mandate approaches (郵送期限の通知). |
| `notify_deadline_debit` | `bool` | Optional | Notify when the transfer registration cutoff approaches (締切日の通知). |
| `notify_debit_update` | `bool` | Optional | Notify when transfer results are reflected (振替結果の通知). |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from univapayclientsdk.models.direct_debit_notification_configuration import DirectDebitNotificationConfiguration

direct_debit_notification_configuration = DirectDebitNotificationConfiguration(
    notify_deadline_mailing=True,
    notify_deadline_debit=True,
    notify_debit_update=False,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

