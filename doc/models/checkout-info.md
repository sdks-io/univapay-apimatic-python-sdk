
# Checkout Info

Merchant/store checkout configuration: enabled payment methods and their limits, installment/subscription plan settings, convenience-store and bank-transfer settings, widget theme, and per-brand feature support. Returned in full on every call — there is no partial-update or list variant.

*This model accepts additional fields of type Any.*

## Structure

`CheckoutInfo`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `mode` | [`CheckoutMode`](../../doc/models/checkout-mode.md) | Optional | Store processing mode reflected in the checkout configuration: `live` and `test` reflect the credential used to authenticate, while `live_test` is reserved for privileged callers testing against live-mode data. |
| `recurring_token_privilege` | [`CheckoutRecurringTokenPrivilege`](../../doc/models/checkout-recurring-token-privilege.md) | Optional | Level of recurring-charge privilege granted to transaction tokens created under this store: `none` disallows recurring use, `bounded` allows a limited number of recurring charges, and `infinite` allows unlimited recurring charges. |
| `name` | `str` | Optional | Store display name. |
| `card_configuration` | [`CheckoutCardConfiguration`](../../doc/models/checkout-card-configuration.md) | Optional | Card payment settings applied to checkout. |
| `subscription_configuration` | [`CheckoutSubscriptionConfiguration`](../../doc/models/checkout-subscription-configuration.md) | Optional | Univapay-hosted subscription feature toggle. |
| `installments_configuration` | [`CheckoutInstallmentsConfiguration`](../../doc/models/checkout-installments-configuration.md) | Optional | Installment plan configuration applied to checkout. |
| `subscription_plan_configuration` | [`CheckoutSubscriptionPlanConfiguration`](../../doc/models/checkout-subscription-plan-configuration.md) | Optional | Univapay-side subscription plan configuration applied to checkout. |
| `checkout_configuration` | [`CheckoutEcConfiguration`](../../doc/models/checkout-ec-configuration.md) | Optional | EC checkout feature toggles for hosted email receipts and product line items. |
| `qr_scan_configuration` | [`CheckoutQrScanConfiguration`](../../doc/models/checkout-qr-scan-configuration.md) | Optional | QR-scan (CPM) payment settings applied to checkout. |
| `convenience_configuration` | [`CheckoutConvenienceConfiguration`](../../doc/models/checkout-convenience-configuration.md) | Optional | Convenience-store (konbini) payment settings applied to checkout. |
| `paidy_configuration` | [`CheckoutPaidyConfiguration`](../../doc/models/checkout-paidy-configuration.md) | Optional | Paidy payment feature toggle. |
| `paidy_public_key` | `str` | Optional | Public key used to initialize the Paidy widget. `null` when Paidy is not configured for this store. |
| `logo_image` | `str` | Optional | URL of the store's checkout logo image. `null` when no logo is configured. Note: this response field is `logo_image`, but the corresponding store-configuration update field is `logo_url` — the two names do not round-trip automatically. |
| `theme` | [`CheckoutTheme`](../../doc/models/checkout-theme.md) | Optional | Widget theme applied to checkout. |
| `recurring_card_charge_cvv_confirmation` | [`RecurringCvvConfirmation`](../../doc/models/recurring-cvv-confirmation.md) | Optional | CVV re-confirmation policy applied to recurring card charges (subscriptions and tokens with recurring privilege). |
| `online_configuration` | [`CheckoutOnlineConfiguration`](../../doc/models/checkout-online-configuration.md) | Optional | Online redirect/wallet payment feature toggle. |
| `bank_transfer_configuration` | [`CheckoutBankTransferConfiguration`](../../doc/models/checkout-bank-transfer-configuration.md) | Optional | Bank transfer (振込) payment settings applied to checkout. |
| `supported_brands` | [`List[CheckoutSupportedBrand]`](../../doc/models/checkout-supported-brand.md) | Optional | Feature support and capability flags for every payment-type / brand combination the store can accept. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from univapayclientsdk.models.checkout_card_configuration import CheckoutCardConfiguration
from univapayclientsdk.models.checkout_info import CheckoutInfo
from univapayclientsdk.models.checkout_mode import CheckoutMode
from univapayclientsdk.models.checkout_payment_type import CheckoutPaymentType
from univapayclientsdk.models.checkout_recurring_token_privilege import CheckoutRecurringTokenPrivilege
from univapayclientsdk.models.checkout_subscription_configuration import CheckoutSubscriptionConfiguration
from univapayclientsdk.models.checkout_supported_brand import CheckoutSupportedBrand

checkout_info = CheckoutInfo(
    mode=CheckoutMode.TEST,
    recurring_token_privilege=CheckoutRecurringTokenPrivilege.NONE,
    name='Test store',
    card_configuration=CheckoutCardConfiguration(
        enabled=False,
        debit_enabled=False,
        prepaid_enabled=False,
        debit_authorization_enabled=False,
        prepaid_authorization_enabled=False,
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    subscription_configuration=CheckoutSubscriptionConfiguration(
        enabled=False,
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    supported_brands=[
        CheckoutSupportedBrand(
            payment_type=CheckoutPaymentType.CARD,
            brand='visa',
            card_brand='visa',
            qr_brand='qr_brand4',
            online_brand='online_brand2',
            dynamic_info=False,
            support_auth_capture=True,
            requires_full_name=False,
            requires_cvv=True,
            countries_allowed=None,
            supported_currencies=None,
            cvv_auth=False,
            installment_capable=True,
            mcp_capable=False,
            mcp_only=False,
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        CheckoutSupportedBrand(
            payment_type=CheckoutPaymentType.QR_MERCHANT,
            brand='alipay_merchant_qr',
            card_brand='card_brand4',
            qr_brand='alipay_merchant_qr',
            online_brand='online_brand2',
            dynamic_info=False,
            support_auth_capture=False,
            requires_full_name=False,
            requires_cvv=False,
            countries_allowed=None,
            supported_currencies=None,
            cvv_auth=False,
            installment_capable=False,
            mcp_capable=False,
            mcp_only=False,
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        )
    ],
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

