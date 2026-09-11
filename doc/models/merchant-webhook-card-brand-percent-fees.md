
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
from univapayclientsdk.models.merchant_webhook_card_brand_percent_fees import MerchantWebhookCardBrandPercentFees

merchant_webhook_card_brand_percent_fees = MerchantWebhookCardBrandPercentFees(
    visa=3.6,
    mastercard=3.6,
    jcb=3.8
)
```

