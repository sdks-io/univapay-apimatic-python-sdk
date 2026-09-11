
# Recurring Cvv Confirmation

CVV re-confirmation policy applied to recurring card charges (subscriptions and tokens with recurring privilege).

*This model accepts additional fields of type Any.*

## Structure

`RecurringCvvConfirmation`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `enabled` | `bool` | Optional | Whether CVV re-confirmation is required for recurring card charges. Resolves to `false` when not configured. |
| `threshold` | [`List[CheckoutMoneyAmount]`](../../doc/models/checkout-money-amount.md) | Optional | Amount thresholds above which CVV re-confirmation is required. `null` when no threshold is configured. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from univapayclientsdk.models.recurring_cvv_confirmation import RecurringCvvConfirmation

recurring_cvv_confirmation = RecurringCvvConfirmation(
    enabled=False,
    threshold=[
        None
    ],
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

