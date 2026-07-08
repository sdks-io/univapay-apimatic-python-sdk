
# Subscription User Data

Customer-facing payment method summary data.

*This model accepts additional fields of type Any.*

## Structure

`SubscriptionUserData`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `mtype` | `str` | Optional | Type of the resource. |
| `cardholder_name` | `str` | Optional | Cardholder name value. |
| `email` | `str` | Optional | Customer email address. |
| `brand` | `str` | Optional | Brand or network name. |
| `gateway` | `str` | Optional | Gateway identifier. |
| `service_provider` | `str` | Optional | Service provider identifier. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from univapayclientsdk.models.subscription_user_data import SubscriptionUserData

subscription_user_data = SubscriptionUserData(
    mtype='type2',
    cardholder_name='cardholder_name6',
    email='email8',
    brand='brand2',
    gateway='gateway8',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

