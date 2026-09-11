
# Merchant Webhook Security Configuration

Merchant-level fraud and refund safety settings.

*This model accepts additional fields of type Any.*

## Structure

`MerchantWebhookSecurityConfiguration`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `card_charge_cooldown` | `str` | Optional | ISO-8601 duration between card charge attempts. |
| `subscription_cooldown` | `str` | Optional | ISO-8601 duration between subscription charge attempts. |
| `idempotent_card_charge_cooldown` | `str` | Optional | ISO-8601 duration for reusing an idempotent card charge key. |
| `idempotent_subscription_cooldown` | `str` | Optional | ISO-8601 duration for reusing an idempotent subscription key. |
| `restrict_ip_after_failed_charge` | [`RestrictIpAfterFailedChargeConfig`](../../doc/models/restrict-ip-after-failed-charge-config.md) | Optional | IP restriction policy applied after repeated failed charges. |
| `inspect_suspicious_login_after` | `str` | Optional | Look-back period used to review suspicious login activity. |
| `refund_percent_limit` | `float` | Optional | Maximum refund-to-sales percentage allowed before restriction. |
| `limit_charge_by_card_configuration` | [`MerchantWebhookLimitChargeByCardConfiguration`](../../doc/models/merchant-webhook-limit-charge-by-card-configuration.md) | Optional | Per-card velocity limit configuration. |
| `confirmation_required` | `bool` | Optional | Requires confirmation before protected refund actions proceed. |
| `min_refund_threshold` | `int` | Optional | Minimum refund amount, in minor units, subject to confirmation checks. |
| `limit_refund_by_sales` | [`MerchantWebhookLimitRefundBySalesConfiguration`](../../doc/models/merchant-webhook-limit-refund-by-sales-configuration.md) | Optional | Refund-limiting configuration based on sales history. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
from univapayclientsdk.models.merchant_webhook_limit_refund_by_sales_configuration import MerchantWebhookLimitRefundBySalesConfiguration
from univapayclientsdk.models.merchant_webhook_security_configuration import MerchantWebhookSecurityConfiguration
from univapayclientsdk.models.restrict_ip_after_failed_charge_config import RestrictIpAfterFailedChargeConfig

merchant_webhook_security_configuration = MerchantWebhookSecurityConfiguration(
    card_charge_cooldown='PT5M',
    subscription_cooldown='PT10M',
    restrict_ip_after_failed_charge=RestrictIpAfterFailedChargeConfig(
        enabled=True,
        count=5,
        cooldown='PT1H'
    ),
    refund_percent_limit=100,
    confirmation_required=False,
    min_refund_threshold=100,
    limit_refund_by_sales=MerchantWebhookLimitRefundBySalesConfiguration(
        enabled=True,
        period='monthly',
        rolling_window=True
    )
)
```

