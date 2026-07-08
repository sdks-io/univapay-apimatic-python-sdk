
# Subscription Update Schedule Settings

Schedule settings that can be updated on a subscription.

*This model accepts additional fields of type Any.*

## Structure

`SubscriptionUpdateScheduleSettings`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `termination_mode` | [`SubscriptionTerminationMode`](../../doc/models/subscription-termination-mode.md) | Optional | Subscription Termination Mode schema.<br><br>**Default**: `"immediate"` |
| `start_on` | `datetime` | Optional | Subscription start date. Used to change the first actual charge date  for subscriptions that initially only registered a payment method. |
| `retry_interval` | `str` | Optional | ISO-8601 Duration for retry interval if payment fails  (e.g., P3D for 3 days, PT48H for 48 hours). |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import dateutil.parser
import jsonpickle

from univapayclientsdk.models.subscription_termination_mode import SubscriptionTerminationMode
from univapayclientsdk.models.subscription_update_schedule_settings import SubscriptionUpdateScheduleSettings

subscription_update_schedule_settings = SubscriptionUpdateScheduleSettings(
    termination_mode=SubscriptionTerminationMode.IMMEDIATE,
    start_on=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
    retry_interval='retry_interval6',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

