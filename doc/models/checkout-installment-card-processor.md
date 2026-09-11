
# Checkout Installment Card Processor

Card-processor capabilities available for installment payments.

*This model accepts additional fields of type Any.*

## Structure

`CheckoutInstallmentCardProcessor`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `revolving` | `bool` | Optional | Whether revolving installment payments are allowed. |
| `fixed_cycle` | `bool` | Optional | Whether fixed-cycle installment payments are allowed. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from univapayclientsdk.models.checkout_installment_card_processor import CheckoutInstallmentCardProcessor

checkout_installment_card_processor = CheckoutInstallmentCardProcessor(
    revolving=True,
    fixed_cycle=True,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

