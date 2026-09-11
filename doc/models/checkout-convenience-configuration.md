
# Checkout Convenience Configuration

Convenience-store (konbini) payment settings applied to checkout.

*This model accepts additional fields of type Any.*

## Structure

`CheckoutConvenienceConfiguration`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `enabled` | `bool` | Optional | Whether convenience-store payments are enabled. |
| `expiration` | `str` | Optional | ISO-8601 duration before a convenience-store payment expires. |
| `expiration_time_shift` | [`ExpirationTimeShift`](../../doc/models/expiration-time-shift.md) | Optional | Time-of-day override applied when calculating expirations, shared by convenience-store and bank-transfer configuration. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from univapayclientsdk.models.checkout_convenience_configuration import CheckoutConvenienceConfiguration
from univapayclientsdk.models.expiration_time_shift import ExpirationTimeShift

checkout_convenience_configuration = CheckoutConvenienceConfiguration(
    enabled=True,
    expiration='PT720H',
    expiration_time_shift=ExpirationTimeShift(
        value='value4',
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

