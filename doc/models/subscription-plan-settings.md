
# Subscription Plan Settings

Configuration for limited-cycle subscriptions (Univapay side).

*This model accepts additional fields of type Any.*

## Structure

`SubscriptionPlanSettings`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `plan_type` | [`PlanSettingsType`](../../doc/models/plan-settings-type.md) | Optional | Plan type selector. |
| `fixed_cycles` | `int` | Optional | Number of cycles for fixed_cycles plan. |
| `fixed_cycle_amount` | `int` | Optional | Total target amount for fixed_cycle_amount plan. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
from univapayclientsdk.models.subscription_plan_settings import SubscriptionPlanSettings

subscription_plan_settings = SubscriptionPlanSettings()
```

