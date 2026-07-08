
# Store

Store resource returned by the backend `FullStore` formatter. It combines core store identity with the resolved configuration snapshot used for runtime policy evaluation.

*This model accepts additional fields of type Any.*

## Structure

`Store`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `uuid\|str` | Optional | Store identifier. |
| `name` | `str` | Optional | Store display name. |
| `created_on` | `datetime` | Optional | Timestamp when the store was created. |
| `configuration` | [`MerchantWebhookConfiguration`](../../doc/models/merchant-webhook-configuration.md) | Optional | Store-scoped configuration snapshot serialized by gyron-payments-api. It uses the same flattened serializer as merchant configuration, but omits `transfer_schedule`. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import dateutil.parser
import jsonpickle

from univapayclientsdk.models.merchant_webhook_bank_transfer_configuration import MerchantWebhookBankTransferConfiguration
from univapayclientsdk.models.merchant_webhook_card_configuration import MerchantWebhookCardConfiguration
from univapayclientsdk.models.merchant_webhook_configuration import MerchantWebhookConfiguration
from univapayclientsdk.models.merchant_webhook_money_amount import MerchantWebhookMoneyAmount
from univapayclientsdk.models.merchant_webhook_online_configuration import MerchantWebhookOnlineConfiguration
from univapayclientsdk.models.merchant_webhook_user_transactions_configuration import MerchantWebhookUserTransactionsConfiguration
from univapayclientsdk.models.store import Store

store = Store(
    id='11ef0000-0000-4000-8000-000000000022',
    name='Tokyo Store',
    created_on=dateutil.parser.parse('2026-04-09T07:35:50.000000Z'),
    configuration=MerchantWebhookConfiguration(
        percent_fee=3.6,
        flat_fees=[
            None
        ],
        logo_url='logo_url4',
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
        ),
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

