
# Checkout Online Configuration

Online redirect/wallet payment feature toggle.

*This model accepts additional fields of type Any.*

## Structure

`CheckoutOnlineConfiguration`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `enabled` | `bool` | Optional | Whether online redirect/wallet payments are enabled. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from univapayclientsdk.models.checkout_online_configuration import CheckoutOnlineConfiguration

checkout_online_configuration = CheckoutOnlineConfiguration(
    enabled=True,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

