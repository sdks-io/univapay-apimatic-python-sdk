
# Checkout Money Amount

Monetary amount used by checkout configuration limits and thresholds.

*This model accepts additional fields of type Any.*

## Structure

`CheckoutMoneyAmount`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `amount` | `int` | Optional | Amount in the smallest unit of the currency. |
| `amount_formatted` | `float` | Optional | Amount formatted for display. |
| `currency` | `str` | Optional | ISO-4217 currency code. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from univapayclientsdk.models.checkout_money_amount import CheckoutMoneyAmount

checkout_money_amount = CheckoutMoneyAmount(
    amount=1000,
    amount_formatted=1000,
    currency='JPY',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

