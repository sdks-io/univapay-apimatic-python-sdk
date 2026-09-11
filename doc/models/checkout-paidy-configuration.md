
# Checkout Paidy Configuration

Paidy payment feature toggle.

*This model accepts additional fields of type Any.*

## Structure

`CheckoutPaidyConfiguration`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `enabled` | `bool` | Optional | Whether Paidy payments are enabled. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from univapayclientsdk.models.checkout_paidy_configuration import CheckoutPaidyConfiguration

checkout_paidy_configuration = CheckoutPaidyConfiguration(
    enabled=True,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

