
# Merchant Webhook Recurring Token Configuration

Recurring token configuration inherited by the merchant.

*This model accepts additional fields of type Any.*

## Structure

`MerchantWebhookRecurringTokenConfiguration`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `recurring_type` | `str` | Optional | Merchant recurring-token privilege. |
| `charge_wait_period` | `str` | Optional | ISO-8601 duration to wait before first recurring charge. |
| `card_charge_cvv_confirmation` | [`MerchantWebhookRecurringCvvConfirmationConfig`](../../doc/models/merchant-webhook-recurring-cvv-confirmation-config.md) | Optional | CVV confirmation rules for recurring token charges. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from univapayclientsdk.models.merchant_webhook_recurring_cvv_confirmation_config import MerchantWebhookRecurringCvvConfirmationConfig
from univapayclientsdk.models.merchant_webhook_recurring_token_configuration import MerchantWebhookRecurringTokenConfiguration

merchant_webhook_recurring_token_configuration = MerchantWebhookRecurringTokenConfiguration(
    recurring_type='infinite',
    charge_wait_period='P7D',
    card_charge_cvv_confirmation=MerchantWebhookRecurringCvvConfirmationConfig(
        enabled=False,
        threshold=[
            None
        ],
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

