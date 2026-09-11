
# Checkout Ec Configuration

EC checkout feature toggles for hosted email receipts and product line items.

*This model accepts additional fields of type Any.*

## Structure

`CheckoutEcConfiguration`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `ec_email` | [`CheckoutEcEmailConfiguration`](../../doc/models/checkout-ec-email-configuration.md) | Optional | Email-related EC checkout settings. |
| `ec_products` | [`CheckoutEcProductsConfiguration`](../../doc/models/checkout-ec-products-configuration.md) | Optional | Product-related EC checkout settings. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from univapayclientsdk.models.checkout_ec_configuration import CheckoutEcConfiguration
from univapayclientsdk.models.checkout_ec_email_configuration import CheckoutEcEmailConfiguration
from univapayclientsdk.models.checkout_ec_products_configuration import CheckoutEcProductsConfiguration

checkout_ec_configuration = CheckoutEcConfiguration(
    ec_email=CheckoutEcEmailConfiguration(
        enabled=False,
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    ec_products=CheckoutEcProductsConfiguration(
        enabled=False,
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

