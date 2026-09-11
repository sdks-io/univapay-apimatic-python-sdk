
# Checkout Card Configuration

Card payment settings applied to checkout.

*This model accepts additional fields of type Any.*

## Structure

`CheckoutCardConfiguration`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `enabled` | `bool` | Optional | Whether card payments are enabled. |
| `debit_enabled` | `bool` | Optional | Whether debit cards are allowed. |
| `prepaid_enabled` | `bool` | Optional | Whether prepaid cards are allowed. |
| `debit_authorization_enabled` | `bool` | Optional | Whether authorization-only flows are allowed for debit cards. |
| `prepaid_authorization_enabled` | `bool` | Optional | Whether authorization-only flows are allowed for prepaid cards. |
| `only_direct_currency` | `bool` | Optional | Whether card processing is restricted to direct-settlement currencies. |
| `forbidden_card_brands` | `List[str]` | Optional | Card brands rejected by merchant policy. Common values include `visa`, `mastercard`, `american_express`, `maestro`, `discover`, `jcb`, `diners_club`, `private_label`, and `unionpay`; gateway-specific brands the platform cannot map appear as `unmapped_<raw value>`. `null` when no brand is forbidden. |
| `allowed_countries_by_ip` | `List[str]` | Optional | ISO 3166-1 alpha-2 country codes allowed to originate card payments by IP geolocation. `null` when unrestricted. |
| `foreign_cards_allowed` | `bool` | Optional | Whether cards issued outside the primary operating country are allowed. |
| `fail_on_new_email` | `bool` | Optional | Whether to reject card charges from previously unseen customer email addresses. `null` when not configured. |
| `card_limit` | [`CardLimit`](../../doc/models/card-limit.md) | Optional | Per-card spending limit. `null` when no limit is configured. |
| `allow_empty_cvv` | `bool` | Optional | Whether card flows may proceed without a CVV. `null` when not configured. |
| `allow_direct_token_creation` | `bool` | Optional | Whether direct card token creation is allowed without a hosted capture flow. |
| `three_ds_required` | `bool` | Optional | Whether 3-D Secure is required for eligible card flows. |
| `three_ds_address_required` | `bool` | Optional | Whether billing address data is required when running 3-D Secure. |
| `three_ds_skip_enabled` | `bool` | Optional | Whether privileged callers may request a 3-D Secure skip. |
| `three_ds_phone_number_required` | `bool` | Optional | Whether a phone number is required when running 3-D Secure. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from univapayclientsdk.models.checkout_card_configuration import CheckoutCardConfiguration

checkout_card_configuration = CheckoutCardConfiguration(
    enabled=True,
    debit_enabled=True,
    prepaid_enabled=True,
    debit_authorization_enabled=False,
    prepaid_authorization_enabled=False,
    only_direct_currency=False,
    foreign_cards_allowed=True,
    allow_direct_token_creation=True,
    three_ds_required=False,
    three_ds_address_required=False,
    three_ds_skip_enabled=False,
    three_ds_phone_number_required=True,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

