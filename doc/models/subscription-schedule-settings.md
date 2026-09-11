
# Subscription Schedule Settings

Schedule settings applied to a subscription.

*This model accepts additional fields of type Any.*

## Structure

`SubscriptionScheduleSettings`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `start_on` | `date` | Optional | Date when the recurring schedule starts (YYYY-MM-DD). |
| `zone_id` | `str` | Optional | IANA Timezone ID. |
| `preserve_end_of_month` | `bool` | Optional | If true, subsequent charges will always occur on the last day of the month. |
| `retry_interval` | `str` | Optional | ISO-8601 Duration for retry interval if payment fails (e.g., P5D). |
| `termination_mode` | [`SubscriptionTerminationMode`](../../doc/models/subscription-termination-mode.md) | Optional | Subscription Termination Mode schema.<br><br>**Default**: `"immediate"` |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
from univapayclientsdk.models.subscription_schedule_settings import SubscriptionScheduleSettings

subscription_schedule_settings = SubscriptionScheduleSettings()
```

