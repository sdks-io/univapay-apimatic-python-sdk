
# Merchant

Merchant resource returned by the backend `FullMerchantWithGroupRoles` formatter for merchant-authenticated callers.

*This model accepts additional fields of type Any.*

## Structure

`Merchant`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `uuid\|str` | Optional | Merchant identifier. |
| `verification_data_id` | `uuid\|str` | Optional | Verification data identifier associated with the merchant. |
| `name` | `str` | Optional | Merchant display name. |
| `email` | `str` | Optional | Primary merchant email address. |
| `notification_email` | `str` | Optional | Merchant notification email address. |
| `finance_notification_email` | `str` | Optional | Merchant finance notification email address. |
| `verified` | `bool` | Optional | Whether the merchant has completed verification. |
| `configuration` | [`MerchantWebhookConfiguration`](../../doc/models/merchant-webhook-configuration.md) | Optional | Merchant configuration snapshot serialized by gyron-payments-api. |
| `created_on` | `datetime` | Optional | Timestamp when the merchant was created. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import dateutil.parser
import jsonpickle

from univapayclientsdk.models.merchant import Merchant
from univapayclientsdk.models.merchant_webhook_bank_transfer_configuration import MerchantWebhookBankTransferConfiguration
from univapayclientsdk.models.merchant_webhook_card_configuration import MerchantWebhookCardConfiguration
from univapayclientsdk.models.merchant_webhook_configuration import MerchantWebhookConfiguration
from univapayclientsdk.models.merchant_webhook_money_amount import MerchantWebhookMoneyAmount
from univapayclientsdk.models.merchant_webhook_online_configuration import MerchantWebhookOnlineConfiguration
from univapayclientsdk.models.merchant_webhook_user_transactions_configuration import MerchantWebhookUserTransactionsConfiguration

merchant = Merchant(
    id='11ef0000-0000-4000-8000-000000000020',
    verification_data_id='11ef0000-0000-4000-8000-000000000021',
    name='Example Merchant',
    email='owner@example.com',
    notification_email='alerts@example.com',
    finance_notification_email='finance@example.com',
    verified=True,
    configuration=MerchantWebhookConfiguration(
        percent_fee=3.6,
        country='JP',
        language='ja',
        minimum_charge_amounts=[
            MerchantWebhookMoneyAmount(
                amount=100,
                currency='JPY'
            )
        ],
        maximum_charge_amounts=[
            MerchantWebhookMoneyAmount(
                amount=100000,
                currency='JPY'
            )
        ],
        user_transactions_configuration=MerchantWebhookUserTransactionsConfiguration(
            enabled=True,
            notify_customer=True,
            notify_on_webhook_failure=True
        ),
        card_configuration=MerchantWebhookCardConfiguration(
            enabled=True,
            debit_enabled=True,
            prepaid_enabled=False,
            three_ds_required=True
        ),
        online_configuration=MerchantWebhookOnlineConfiguration(
            enabled=True
        ),
        bank_transfer_configuration=MerchantWebhookBankTransferConfiguration(
            enabled=True,
            match_amount=True,
            expiration='P7D'
        )
    ),
    created_on=dateutil.parser.parse('2026-04-09T07:35:50.000000Z'),
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

