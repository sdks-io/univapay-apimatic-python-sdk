
# Merchant Webhook Installment Plan Configuration

Installment plan configuration.

*This model accepts additional fields of type Any.*

## Structure

`MerchantWebhookInstallmentPlanConfiguration`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `enabled` | `bool` | Optional | Enables installment plan features for eligible payments. |
| `card_processor` | [`CardProcessorInstallmentConfig`](../../doc/models/card-processor-installment-config.md) | Optional | Card-processor capabilities available for installment payments. |
| `supported_payment_types` | `List[str]` | Optional | Payment types that can use installment plans. |
| `min_charge_amount` | [`MerchantWebhookMoneyAmount`](../../doc/models/merchant-webhook-money-amount.md) | Optional | Monetary amount object serialized by backend config models. |
| `max_payout_period` | `str` | Optional | Maximum payout delay allowed for installment settlements. |
| `only_with_processor` | `bool` | Optional | Restricts installment use to processor-backed flows. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from univapayclientsdk.models.card_processor_installment_config import CardProcessorInstallmentConfig
from univapayclientsdk.models.merchant_webhook_installment_plan_configuration import MerchantWebhookInstallmentPlanConfiguration
from univapayclientsdk.models.merchant_webhook_money_amount import MerchantWebhookMoneyAmount

merchant_webhook_installment_plan_configuration = MerchantWebhookInstallmentPlanConfiguration(
    enabled=True,
    card_processor=CardProcessorInstallmentConfig(
        revolving=True,
        fixed_cycle=True,
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    supported_payment_types=[
        'card'
    ],
    min_charge_amount=MerchantWebhookMoneyAmount(
        amount=3000,
        currency='JPY',
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    max_payout_period='P12M',
    only_with_processor=True,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

