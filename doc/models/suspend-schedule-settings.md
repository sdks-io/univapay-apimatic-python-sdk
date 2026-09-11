
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
from univapayclientsdk.models.suspend_schedule_settings import SuspendScheduleSettings

suspend_schedule_settings = SuspendScheduleSettings()
```

