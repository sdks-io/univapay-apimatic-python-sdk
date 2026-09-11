
# Checkout Supported Brand

Feature support and capability flags for a single payment-type / brand combination the store can accept.

*This model accepts additional fields of type Any.*

## Structure

`CheckoutSupportedBrand`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `payment_type` | [`CheckoutPaymentType`](../../doc/models/checkout-payment-type.md) | Optional | Payment type identifier used throughout the checkout configuration. |
| `brand` | `str` | Optional | Brand identifier for `payment_type`. For `card` and `apple_pay`, one of the common `CardBrand` values (`visa`, `mastercard`, `american_express`, `maestro`, `discover`, `jcb`, `diners_club`, `private_label`, `unionpay`) or an `unmapped_<raw value>` fallback. For `qr_scan`, a QR-CPM brand (e.g. `pay_pay`, `we_chat`, `qq`, `line_pay`, `au_pay`, `alipay_china`). For `qr_merchant`, a QR-MPM brand (e.g. `rakuten_pay_merchant`, `alipay_merchant_qr`, `pay_pay_merchant`, `d_barai_mpm`, `we_chat_mpm`). For `online`, an online-redirect brand (e.g. `alipay_online`, `pay_pay_online`, `we_chat_online`, `d_barai_online`, `kakaopay`). For `konbini`, a convenience-store brand (e.g. `seven_eleven`, `family_mart`, `lawson`). For `paidy` and `bank_transfer`, the payment type's own identifier. The full brand catalogue is large and gateway-dependent — treat this as an open string, not a fixed set. |
| `card_brand` | `str` | Optional | Legacy alias of `brand`. Present only when `payment_type` is `card` or `apple_pay`. |
| `qr_brand` | `str` | Optional | Legacy alias of `brand`. Present only when `payment_type` is `qr_merchant`. |
| `online_brand` | `str` | Optional | Legacy alias of `brand`. Present only when `payment_type` is `online`. |
| `dynamic_info` | `bool` | Optional | Whether the brand's supported feature set is resolved dynamically. |
| `support_auth_capture` | `bool` | Optional | Whether the brand supports separate authorization and capture. |
| `requires_full_name` | `bool` | Optional | Whether the brand requires the cardholder's full name. |
| `requires_cvv` | `bool` | Optional | Whether the brand requires a CVV. |
| `countries_allowed` | `List[str]` | Optional | ISO 3166-1 alpha-2 country codes allowed for this brand. `null` when unrestricted. |
| `supported_currencies` | `List[str]` | Optional | ISO-4217 currency codes supported by this brand. `null` when unrestricted. |
| `cvv_auth` | `bool` | Optional | Whether this brand supports CVV-only authorization. |
| `installment_capable` | `bool` | Optional | Whether this brand supports installment plans. |
| `mcp_capable` | `bool` | Optional | Whether this brand supports multi-currency pricing. |
| `mcp_only` | `bool` | Optional | Whether this brand is only available through multi-currency pricing. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from univapayclientsdk.models.checkout_payment_type import CheckoutPaymentType
from univapayclientsdk.models.checkout_supported_brand import CheckoutSupportedBrand

checkout_supported_brand = CheckoutSupportedBrand(
    payment_type=CheckoutPaymentType.CARD,
    brand='visa',
    card_brand='visa',
    qr_brand='alipay_merchant_qr',
    online_brand='alipay_online',
    dynamic_info=False,
    support_auth_capture=True,
    requires_full_name=False,
    requires_cvv=True,
    cvv_auth=False,
    installment_capable=True,
    mcp_capable=False,
    mcp_only=False,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

