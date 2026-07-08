
# Merchant Webhook Customer Management Configuration

Customer-management defaults.

*This model accepts additional fields of type Any.*

## Structure

`MerchantWebhookCustomerManagementConfiguration`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `enabled` | `bool` | Optional | Enables customer-management features. |
| `default_roles` | `List[str]` | Optional | Roles applied to newly created customers. |
| `default_mode` | `str` | Optional | Default processing mode assigned to new customer records. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from univapayclientsdk.models.merchant_webhook_customer_management_configuration import MerchantWebhookCustomerManagementConfiguration

merchant_webhook_customer_management_configuration = MerchantWebhookCustomerManagementConfiguration(
    enabled=True,
    default_roles=[
        'end_user'
    ],
    default_mode='live',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

