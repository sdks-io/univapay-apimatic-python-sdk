
# Subscription Suspend Request

Request body for suspending a subscription. The `schedule_settings.termination_mode`  field controls when the suspension takes effect.

*This model accepts additional fields of type Any.*

## Structure

`SubscriptionSuspendRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `schedule_settings` | [`SuspendScheduleSettings`](../../doc/models/suspend-schedule-settings.md) | Optional | Schedule-related settings. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from univapayclientsdk.models.subscription_suspend_request import SubscriptionSuspendRequest
from univapayclientsdk.models.subscription_termination_mode import SubscriptionTerminationMode
from univapayclientsdk.models.suspend_schedule_settings import SuspendScheduleSettings

subscription_suspend_request = SubscriptionSuspendRequest(
    schedule_settings=SuspendScheduleSettings(
        termination_mode=SubscriptionTerminationMode.ON_NEXT_PAYMENT,
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

