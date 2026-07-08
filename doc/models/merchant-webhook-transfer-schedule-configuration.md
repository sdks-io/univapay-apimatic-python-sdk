
# Merchant Webhook Transfer Schedule Configuration

Transfer schedule configuration inherited by the merchant.

*This model accepts additional fields of type Any.*

## Structure

`MerchantWebhookTransferScheduleConfiguration`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `wait_period` | `str` | Optional | ISO-8601 period before charges become payable. |
| `period` | `str` | Optional | Transfer period selected for payouts. |
| `full_period_required` | `bool` | Optional | Whether the first transfer period must be fully completed. |
| `day_of_week` | `str` | Optional | Payout day of week when using weekly schedules. |
| `week_of_month` | `int` | Optional | Week of month used by monthly schedules. |
| `day_of_month` | `int` | Optional | Day of month used by monthly schedules. |
| `weekly_closing_day` | `str` | Optional | Weekly closing day for balance aggregation. |
| `weekly_payout_day` | `str` | Optional | Weekly payout day. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from univapayclientsdk.models.merchant_webhook_transfer_schedule_configuration import MerchantWebhookTransferScheduleConfiguration

merchant_webhook_transfer_schedule_configuration = MerchantWebhookTransferScheduleConfiguration(
    wait_period='P7D',
    period='weekly',
    full_period_required=False,
    day_of_week='day_of_week6',
    week_of_month=124,
    weekly_closing_day='sunday',
    weekly_payout_day='friday',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

