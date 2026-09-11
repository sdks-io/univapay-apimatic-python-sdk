
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
| `configuration` | [`MerchantWebhookConfiguration`](../../doc/models/merchant-webhook-configuration.md) | Optional | Store-scoped configuration snapshot as serialized by the backend. It uses the same flattened serializer as merchant configuration, but omits `transfer_schedule`. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import dateutil.parser

from univapayclientsdk.models.card_processor_installment_config import CardProcessorInstallmentConfig
from univapayclientsdk.models.merchant_webhook_bank_transfer_configuration import MerchantWebhookBankTransferConfiguration
from univapayclientsdk.models.merchant_webhook_card_brand_percent_fees import MerchantWebhookCardBrandPercentFees
from univapayclientsdk.models.merchant_webhook_card_configuration import MerchantWebhookCardConfiguration
from univapayclientsdk.models.merchant_webhook_configuration import MerchantWebhookConfiguration
from univapayclientsdk.models.merchant_webhook_convenience_configuration import MerchantWebhookConvenienceConfiguration
from univapayclientsdk.models.merchant_webhook_installment_plan_configuration import MerchantWebhookInstallmentPlanConfiguration
from univapayclientsdk.models.merchant_webhook_limit_refund_by_sales_configuration import MerchantWebhookLimitRefundBySalesConfiguration
from univapayclientsdk.models.merchant_webhook_money_amount import MerchantWebhookMoneyAmount
from univapayclientsdk.models.merchant_webhook_online_configuration import MerchantWebhookOnlineConfiguration
from univapayclientsdk.models.merchant_webhook_paidy_configuration import MerchantWebhookPaidyConfiguration
from univapayclientsdk.models.merchant_webhook_qr_scan_configuration import MerchantWebhookQrScanConfiguration
from univapayclientsdk.models.merchant_webhook_recurring_cvv_confirmation_config import MerchantWebhookRecurringCvvConfirmationConfig
from univapayclientsdk.models.merchant_webhook_recurring_token_configuration import MerchantWebhookRecurringTokenConfiguration
from univapayclientsdk.models.merchant_webhook_security_configuration import MerchantWebhookSecurityConfiguration
from univapayclientsdk.models.merchant_webhook_user_transactions_configuration import MerchantWebhookUserTransactionsConfiguration
from univapayclientsdk.models.restrict_ip_after_failed_charge_config import RestrictIpAfterFailedChargeConfig
from univapayclientsdk.models.store import Store

store = Store(
    id='11ef0000-0000-4000-8000-000000000022',
    name='Tokyo Store',
    created_on=dateutil.parser.parse('2026-04-09T07:35:50.000000Z'),
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
        recurring_token_configuration=MerchantWebhookRecurringTokenConfiguration(
            recurring_type='infinite',
            charge_wait_period='P7D',
            card_charge_cvv_confirmation=MerchantWebhookRecurringCvvConfirmationConfig(
                enabled=False
            )
        ),
        security_configuration=MerchantWebhookSecurityConfiguration(
            card_charge_cooldown='PT5M',
            subscription_cooldown='PT10M',
            restrict_ip_after_failed_charge=RestrictIpAfterFailedChargeConfig(
                enabled=True,
                count=5,
                cooldown='PT1H'
            ),
            refund_percent_limit=100,
            confirmation_required=False,
            min_refund_threshold=100,
            limit_refund_by_sales=MerchantWebhookLimitRefundBySalesConfiguration(
                enabled=True,
                period='monthly',
                rolling_window=True
            )
        ),
        installments_configuration=MerchantWebhookInstallmentPlanConfiguration(
            enabled=True,
            card_processor=CardProcessorInstallmentConfig(
                revolving=True,
                fixed_cycle=True
            ),
            supported_payment_types=[
                'card'
            ],
            min_charge_amount=MerchantWebhookMoneyAmount(
                amount=3000,
                currency='JPY'
            ),
            max_payout_period='P12M',
            only_with_processor=True
        ),
        card_brand_percent_fees=MerchantWebhookCardBrandPercentFees(
            visa=3.6,
            mastercard=3.6,
            jcb=3.8
        ),
        card_configuration=MerchantWebhookCardConfiguration(
            enabled=True,
            debit_enabled=True,
            prepaid_enabled=False,
            three_ds_required=True
        ),
        qr_scan_configuration=MerchantWebhookQrScanConfiguration(
            enabled=True,
            forbidden_qr_scan_gateways=[
                'wechat'
            ]
        ),
        convenience_configuration=MerchantWebhookConvenienceConfiguration(
            enabled=True,
            expiration='P3D'
        ),
        paidy_configuration=MerchantWebhookPaidyConfiguration(
            enabled=False
        ),
        online_configuration=MerchantWebhookOnlineConfiguration(
            enabled=True
        ),
        bank_transfer_configuration=MerchantWebhookBankTransferConfiguration(
            enabled=True,
            match_amount=True,
            expiration='P7D'
        )
    )
)
```

