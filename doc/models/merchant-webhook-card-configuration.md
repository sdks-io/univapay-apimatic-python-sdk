
# Merchant Webhook Card Configuration

Card payment settings.

*This model accepts additional fields of type Any.*

## Structure

`MerchantWebhookCardConfiguration`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `enabled` | `bool` | Optional | Enables card payments. |
| `debit_enabled` | `bool` | Optional | Allows debit cards for payment flows. |
| `prepaid_enabled` | `bool` | Optional | Allows prepaid cards for payment flows. |
| `debit_authorization_enabled` | `bool` | Optional | Allows authorization-only flows for debit cards. |
| `prepaid_authorization_enabled` | `bool` | Optional | Allows authorization-only flows for prepaid cards. |
| `forbidden_card_brands` | `List[str]` | Optional | Card brands rejected by merchant policy. |
| `allowed_countries_by_ip` | `List[str]` | Optional | Source IP country codes allowed for card payments. |
| `foreign_cards_allowed` | `bool` | Optional | Allows cards issued outside the primary operating country. |
| `fail_on_new_email` | `bool` | Optional | Rejects card charges from previously unseen customer email addresses. |
| `card_limit` | `int` | Optional | Maximum number of cards allowed per customer context. |
| `allow_empty_cvv` | `bool` | Optional | Allows card flows without providing a CVV. |
| `only_direct_currency` | `bool` | Optional | Limits card processing to direct-settlement currencies only. |
| `three_ds_required` | `bool` | Optional | Requires 3-D Secure for eligible card flows. |
| `three_ds_address_required` | `bool` | Optional | Requires billing address data when running 3-D Secure. |
| `three_ds_skip_enabled` | `bool` | Optional | Allows privileged callers to request 3-D Secure skip mode. |
| `allow_direct_token_creation` | `bool` | Optional | Allows direct card token creation without hosted capture flows. |
| `three_ds_phone_number_required` | `bool` | Optional | Requires a phone number when running 3-D Secure. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from univapayclientsdk.models.merchant_webhook_card_configuration import MerchantWebhookCardConfiguration

merchant_webhook_card_configuration = MerchantWebhookCardConfiguration(
    enabled=True,
    debit_enabled=True,
    prepaid_enabled=False,
    debit_authorization_enabled=False,
    prepaid_authorization_enabled=False,
    foreign_cards_allowed=False,
    three_ds_required=True,
    allow_direct_token_creation=False,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

