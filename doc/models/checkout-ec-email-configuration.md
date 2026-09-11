
# Checkout Ec Email Configuration

Email-related EC checkout settings.

*This model accepts additional fields of type Any.*

## Structure

`CheckoutEcEmailConfiguration`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `enabled` | `bool` | Optional | Whether EC email receipts are enabled. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from univapayclientsdk.models.checkout_ec_email_configuration import CheckoutEcEmailConfiguration

checkout_ec_email_configuration = CheckoutEcEmailConfiguration(
    enabled=False,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

