
# Merchant Webhook Money Amount

Monetary amount object serialized by backend config models.

*This model accepts additional fields of type Any.*

## Structure

`MerchantWebhookMoneyAmount`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `amount` | `int` | Optional | Amount in minor currency units. |
| `currency` | `str` | Optional | ISO 4217 currency code. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from univapayclientsdk.models.merchant_webhook_money_amount import MerchantWebhookMoneyAmount

merchant_webhook_money_amount = MerchantWebhookMoneyAmount(
    amount=1000,
    currency='JPY',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

