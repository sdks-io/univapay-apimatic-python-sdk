
# Subscription Installment Plan

Configuration for credit card company side installments.

*This model accepts additional fields of type Any.*

## Structure

`SubscriptionInstallmentPlan`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `plan_type` | [`InstallmentPlanType`](../../doc/models/installment-plan-type.md) | Optional | Plan type selector. |
| `fixed_cycles` | [`InstallmentFixedCycles`](../../doc/models/installment-fixed-cycles.md) | Optional | Required if plan_type is fixed_cycles. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
from univapayclientsdk.models.subscription_installment_plan import SubscriptionInstallmentPlan

subscription_installment_plan = SubscriptionInstallmentPlan()
```

