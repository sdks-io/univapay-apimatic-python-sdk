
# Merchant Webhook User Transactions Configuration

Merchant transaction notification settings.

*This model accepts additional fields of type Any.*

## Structure

`MerchantWebhookUserTransactionsConfiguration`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `enabled` | `bool` | Optional | Enables merchant transaction notifications. |
| `notify_customer` | `bool` | Optional | Sends transaction notifications to the customer. |
| `notify_on_test` | `bool` | Optional | Sends notifications for test-mode events. |
| `notify_on_recurring_token_creation` | `bool` | Optional | Sends notifications when a recurring token is created. |
| `notify_on_recurring_token_cvv_failed` | `bool` | Optional | Sends notifications when recurring-token CVV confirmation fails. |
| `notify_on_webhook_failure` | `bool` | Optional | Sends notifications after repeated webhook delivery failures. |
| `notify_on_webhook_disabled` | `bool` | Optional | Sends notifications when webhook delivery is disabled. |
| `notify_user_on_failed_transactions` | `bool` | Optional | Sends merchant notifications for failed transactions. |
| `notify_customer_on_failed_transactions` | `bool` | Optional | Sends customer notifications for failed transactions. |
| `notify_user_on_convenience_instructions` | `bool` | Optional | Sends merchant notifications with convenience-store payment instructions. |
| `notify_on_subscriptions` | `bool` | Optional | Sends notifications for subscription lifecycle events. |
| `notify_on_authorizations` | `bool` | Optional | Sends notifications for authorization-only charges. |
| `notify_on_cvv_authorizations` | `bool` | Optional | Sends notifications for CVV authorization events. |
| `notify_on_cancels` | `bool` | Optional | Sends notifications when charges are canceled. |
| `customer_refer_link_enabled` | `bool` | Optional | Includes customer self-service links in supported notifications. |
| `notify_on_convenience_expiry` | `bool` | Optional | Sends notifications when convenience payments expire. |
| `notify_on_recurring_token_creation_with_three_ds` | `bool` | Optional | Sends notifications when recurring tokens are created through 3-D Secure. |
| `notify_on_chargebacks` | `bool` | Optional | Sends notifications for chargeback events. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from univapayclientsdk.models.merchant_webhook_user_transactions_configuration import MerchantWebhookUserTransactionsConfiguration

merchant_webhook_user_transactions_configuration = MerchantWebhookUserTransactionsConfiguration(
    enabled=True,
    notify_customer=True,
    notify_on_test=False,
    notify_on_recurring_token_creation=False,
    notify_on_recurring_token_cvv_failed=False,
    notify_on_webhook_failure=True,
    notify_on_webhook_disabled=True,
    notify_on_subscriptions=True,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

