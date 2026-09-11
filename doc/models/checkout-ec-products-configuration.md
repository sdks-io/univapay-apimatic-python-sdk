
# Checkout Ec Products Configuration

Product-related EC checkout settings.

*This model accepts additional fields of type Any.*

## Structure

`CheckoutEcProductsConfiguration`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `enabled` | `bool` | Optional | Whether EC product line items are enabled. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from univapayclientsdk.models.checkout_ec_products_configuration import CheckoutEcProductsConfiguration

checkout_ec_products_configuration = CheckoutEcProductsConfiguration(
    enabled=False,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

