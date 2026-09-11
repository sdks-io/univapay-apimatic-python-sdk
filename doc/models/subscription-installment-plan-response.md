
# Subscription Installment Plan Response

Installment plan applied to the subscription, as returned by the API. Covers both card-network installment plans (`revolving`, `fixed_cycles`) and legacy fixed-amount installment plans (`fixed_cycle_amount`).

*This model accepts additional fields of type Any.*

## Structure

`SubscriptionInstallmentPlanResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `plan_type` | [`CombinedPlanType`](../../doc/models/combined-plan-type.md) | Optional | Plan type selector. |
| `fixed_cycles` | [`CombinedInstallmentFixedCycles`](../../doc/models/combined-installment-fixed-cycles.md) | Optional | Number of installment cycles. Present when plan_type is fixed_cycles. |
| `fixed_cycles_amount` | `int` | Optional | Total target amount for the fixed_cycle_amount plan type, in the smallest currency unit. Present when plan_type is fixed_cycle_amount. Note the plural `fixed_cycles_amount` key differs from `subscription_plan`'s singular `fixed_cycle_amount`. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
from univapayclientsdk.models.subscription_installment_plan_response import SubscriptionInstallmentPlanResponse

subscription_installment_plan_response = SubscriptionInstallmentPlanResponse()
```

