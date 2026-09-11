
# Checkout Installments Configuration

Installment plan configuration applied to checkout.

*This model accepts additional fields of type Any.*

## Structure

`CheckoutInstallmentsConfiguration`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `enabled` | `bool` | Optional | Whether installment plans are enabled. |
| `card_processor` | [`CheckoutInstallmentCardProcessor`](../../doc/models/checkout-installment-card-processor.md) | Optional | Card-processor capabilities available for installment payments. |
| `supported_payment_types` | [`List[CheckoutPaymentType]`](../../doc/models/checkout-payment-type.md) | Optional | Payment types eligible for installment plans. |
| `min_charge_amount` | [`CheckoutMoneyAmount`](../../doc/models/checkout-money-amount.md) | Optional | Minimum charge amount eligible for installment plans. `null` when unrestricted. |
| `max_payout_period` | `str` | Optional | ISO-8601 period bounding the maximum payout delay for installment settlements. `null` when unrestricted. |
| `only_with_processor` | `bool` | Optional | Whether installment plans are restricted to processor-backed flows. Always `true` — retained for backwards compatibility. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from univapayclientsdk.models.checkout_installment_card_processor import CheckoutInstallmentCardProcessor
from univapayclientsdk.models.checkout_installments_configuration import CheckoutInstallmentsConfiguration
from univapayclientsdk.models.checkout_payment_type import CheckoutPaymentType

checkout_installments_configuration = CheckoutInstallmentsConfiguration(
    enabled=True,
    card_processor=CheckoutInstallmentCardProcessor(
        revolving=False,
        fixed_cycle=False,
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    supported_payment_types=[
        CheckoutPaymentType.CARD
    ],
    min_charge_amount=None,
    max_payout_period='max_payout_period0',
    only_with_processor=True,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

