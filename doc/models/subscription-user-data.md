
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
from univapayclientsdk.models.subscription_user_data import SubscriptionUserData

subscription_user_data = SubscriptionUserData()
```

