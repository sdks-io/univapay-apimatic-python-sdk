
# Merchant Webhook Card Brand Percent Fees

Per-card-brand percent fee overrides.

*This model accepts additional fields of type Any.*

## Structure

`MerchantWebhookCardBrandPercentFees`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `visa` | `float` | Optional | Percent fee override applied to Visa transactions. |
| `american_express` | `float` | Optional | Percent fee override applied to American Express transactions. |
| `mastercard` | `float` | Optional | Percent fee override applied to Mastercard transactions. |
| `maestro` | `float` | Optional | Percent fee override applied to Maestro transactions. |
| `discover` | `float` | Optional | Percent fee override applied to Discover transactions. |
| `jcb` | `float` | Optional | Percent fee override applied to JCB transactions. |
| `diners_club` | `float` | Optional | Percent fee override applied to Diners Club transactions. |
| `union_pay` | `float` | Optional | Percent fee override applied to UnionPay transactions. |
| `private_label` | `float` | Optional | Percent fee override applied to private-label card transactions. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from univapayclientsdk.models.merchant_webhook_card_brand_percent_fees import MerchantWebhookCardBrandPercentFees

merchant_webhook_card_brand_percent_fees = MerchantWebhookCardBrandPercentFees(
    visa=3.6,
    american_express=255.3,
    mastercard=3.6,
    maestro=249.3,
    discover=29.12,
    jcb=3.8,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

