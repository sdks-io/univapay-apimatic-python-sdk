
# Subscription Simulation Plan Settings

Cycle-limiting plan configuration used to simulate an installment plan or a Univapay-side subscription plan.

*This model accepts additional fields of type Any.*

## Structure

`SubscriptionSimulationPlanSettings`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `plan_type` | [`SimulationPlanSettingsType`](../../doc/models/simulation-plan-settings-type.md) | Optional | Plan type selector. |
| `fixed_cycles` | `int` | Optional | Number of cycles for the fixed_cycles plan. Must be greater than 1. |
| `fixed_cycle_amount` | `int` | Optional | Total target amount for the fixed_cycle_amount plan. Must not exceed the requested amount. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
from univapayclientsdk.models.subscription_simulation_plan_settings import SubscriptionSimulationPlanSettings

subscription_simulation_plan_settings = SubscriptionSimulationPlanSettings()
```

