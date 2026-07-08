
# Merchant Webhook Limit Refund by Sales Configuration

Refund-limiting configuration based on sales history.

*This model accepts additional fields of type Any.*

## Structure

`MerchantWebhookLimitRefundBySalesConfiguration`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `enabled` | `bool` | Optional | Enables sales-based refund limit checks. |
| `period` | `str` | Optional | Sales aggregation period used to evaluate refund limits. |
| `rolling_window` | `bool` | Optional | Uses a rolling window instead of fixed calendar periods. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from univapayclientsdk.models.merchant_webhook_limit_refund_by_sales_configuration import MerchantWebhookLimitRefundBySalesConfiguration

merchant_webhook_limit_refund_by_sales_configuration = MerchantWebhookLimitRefundBySalesConfiguration(
    enabled=True,
    period='monthly',
    rolling_window=True,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

