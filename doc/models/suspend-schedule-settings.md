
# Suspend Schedule Settings

Schedule-related settings.

*This model accepts additional fields of type Any.*

## Structure

`SuspendScheduleSettings`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `termination_mode` | [`SubscriptionTerminationMode`](../../doc/models/subscription-termination-mode.md) | Optional | Subscription Termination Mode schema.<br><br>**Default**: `"immediate"` |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from univapayclientsdk.models.subscription_termination_mode import SubscriptionTerminationMode
from univapayclientsdk.models.suspend_schedule_settings import SuspendScheduleSettings

suspend_schedule_settings = SuspendScheduleSettings(
    termination_mode=SubscriptionTerminationMode.IMMEDIATE,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

