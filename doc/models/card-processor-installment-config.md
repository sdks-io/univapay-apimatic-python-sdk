
# Card Processor Installment Config

Card-processor capabilities available for installment payments.

*This model accepts additional fields of type Any.*

## Structure

`CardProcessorInstallmentConfig`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `revolving` | `bool` | Optional | Allows revolving payments through supported processors. |
| `fixed_cycle` | `bool` | Optional | Allows fixed-cycle installment payments through supported processors. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from univapayclientsdk.models.card_processor_installment_config import CardProcessorInstallmentConfig

card_processor_installment_config = CardProcessorInstallmentConfig(
    revolving=True,
    fixed_cycle=True,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

