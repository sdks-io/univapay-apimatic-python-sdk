
# Merchant Webhook Limit Charge by Card Configuration

Per-card velocity limit configuration.

*This model accepts additional fields of type Any.*

## Structure

`MerchantWebhookLimitChargeByCardConfiguration`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `quantity_of_charges` | `int` | Optional | Maximum number of charges allowed in the time window. |
| `duration_window` | `str` | Optional | ISO-8601 duration for the rolling window. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from univapayclientsdk.models.merchant_webhook_limit_charge_by_card_configuration import MerchantWebhookLimitChargeByCardConfiguration

merchant_webhook_limit_charge_by_card_configuration = MerchantWebhookLimitChargeByCardConfiguration(
    quantity_of_charges=5,
    duration_window='PT24H',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

