
# Merchant Webhook Configuration

Merchant configuration object as serialized by the backend.

*This model accepts additional fields of type Any.*

## Structure

`MerchantWebhookConfiguration`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `percent_fee` | `float` | Optional | Default percent fee applied when no card-brand override exists. |
| `flat_fees` | [`List[MerchantWebhookMoneyAmount]`](../../doc/models/merchant-webhook-money-amount.md) | Optional | Flat fee overrides by currency. |
| `logo_url` | `str` | Optional | Merchant logo URL. |
| `country` | `str` | Optional | Merchant country code. |
| `language` | `str` | Optional | Merchant default language. |
| `display_time_zone` | `str` | Optional | Merchant display time zone. |
| `min_transfer_payout` | [`MerchantWebhookMoneyAmount`](../../doc/models/merchant-webhook-money-amount.md) | Optional | Monetary amount object serialized by backend config models. |
| `minimum_charge_amounts` | [`List[MerchantWebhookMoneyAmount]`](../../doc/models/merchant-webhook-money-amount.md) | Optional | Minimum allowed charge amounts by currency. |
| `maximum_charge_amounts` | [`List[MerchantWebhookMoneyAmount]`](../../doc/models/merchant-webhook-money-amount.md) | Optional | Maximum allowed charge amounts by currency. |
| `transfer_schedule` | [`MerchantWebhookTransferScheduleConfiguration`](../../doc/models/merchant-webhook-transfer-schedule-configuration.md) | Optional | Transfer schedule configuration inherited by the merchant. |
| `user_transactions_configuration` | [`MerchantWebhookUserTransactionsConfiguration`](../../doc/models/merchant-webhook-user-transactions-configuration.md) | Optional | Merchant transaction notification settings. |
| `recurring_token_configuration` | [`MerchantWebhookRecurringTokenConfiguration`](../../doc/models/merchant-webhook-recurring-token-configuration.md) | Optional | Recurring token configuration inherited by the merchant. |
| `security_configuration` | [`MerchantWebhookSecurityConfiguration`](../../doc/models/merchant-webhook-security-configuration.md) | Optional | Merchant-level fraud and refund safety settings. |
| `checkout_configuration` | [`MerchantWebhookCheckoutConfiguration`](../../doc/models/merchant-webhook-checkout-configuration.md) | Optional | Checkout field collection settings. |
| `installments_configuration` | [`MerchantWebhookInstallmentPlanConfiguration`](../../doc/models/merchant-webhook-installment-plan-configuration.md) | Optional | Installment plan configuration. |
| `subscription_plan_configuration` | [`MerchantWebhookSubscriptionPlanConfiguration`](../../doc/models/merchant-webhook-subscription-plan-configuration.md) | Optional | Subscription plan configuration. |
| `card_brand_percent_fees` | [`MerchantWebhookCardBrandPercentFees`](../../doc/models/merchant-webhook-card-brand-percent-fees.md) | Optional | Per-card-brand percent fee overrides. |
| `subscription_configuration` | [`MerchantWebhookSubscriptionConfiguration`](../../doc/models/merchant-webhook-subscription-configuration.md) | Optional | Subscription feature configuration. |
| `customer_management_configuration` | [`MerchantWebhookCustomerManagementConfiguration`](../../doc/models/merchant-webhook-customer-management-configuration.md) | Optional | Customer-management defaults. |
| `descriptor_provided_configuration` | `bool` | Optional | Whether statement descriptors can be provided by merchants. |
| `card_configuration` | [`MerchantWebhookCardConfiguration`](../../doc/models/merchant-webhook-card-configuration.md) | Optional | Card payment settings. |
| `qr_scan_configuration` | [`MerchantWebhookQrScanConfiguration`](../../doc/models/merchant-webhook-qr-scan-configuration.md) | Optional | QR scan payment settings. |
| `convenience_configuration` | [`MerchantWebhookConvenienceConfiguration`](../../doc/models/merchant-webhook-convenience-configuration.md) | Optional | Convenience-store payment settings. |
| `paidy_configuration` | [`MerchantWebhookPaidyConfiguration`](../../doc/models/merchant-webhook-paidy-configuration.md) | Optional | Paidy payment settings. |
| `qr_merchant_configuration` | [`MerchantWebhookQrMerchantConfiguration`](../../doc/models/merchant-webhook-qr-merchant-configuration.md) | Optional | QR merchant payment settings. |
| `online_configuration` | [`MerchantWebhookOnlineConfiguration`](../../doc/models/merchant-webhook-online-configuration.md) | Optional | Online payment settings. |
| `bank_transfer_configuration` | [`MerchantWebhookBankTransferConfiguration`](../../doc/models/merchant-webhook-bank-transfer-configuration.md) | Optional | Bank transfer payment settings. |
| `platform_credentials_enabled` | `bool` | Optional | Whether platform credentials are enabled. |
| `tagged_platform_credentials_enabled` | `bool` | Optional | Whether tagged platform credentials are enabled. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
from univapayclientsdk.models.card_processor_installment_config import CardProcessorInstallmentConfig
from univapayclientsdk.models.merchant_webhook_bank_transfer_configuration import MerchantWebhookBankTransferConfiguration
from univapayclientsdk.models.merchant_webhook_card_brand_percent_fees import MerchantWebhookCardBrandPercentFees
from univapayclientsdk.models.merchant_webhook_card_configuration import MerchantWebhookCardConfiguration
from univapayclientsdk.models.merchant_webhook_checkout_configuration import MerchantWebhookCheckoutConfiguration
from univapayclientsdk.models.merchant_webhook_checkout_toggle import MerchantWebhookCheckoutToggle
from univapayclientsdk.models.merchant_webhook_configuration import MerchantWebhookConfiguration
from univapayclientsdk.models.merchant_webhook_convenience_configuration import MerchantWebhookConvenienceConfiguration
from univapayclientsdk.models.merchant_webhook_customer_management_configuration import MerchantWebhookCustomerManagementConfiguration
from univapayclientsdk.models.merchant_webhook_installment_plan_configuration import MerchantWebhookInstallmentPlanConfiguration
from univapayclientsdk.models.merchant_webhook_limit_refund_by_sales_configuration import MerchantWebhookLimitRefundBySalesConfiguration
from univapayclientsdk.models.merchant_webhook_money_amount import MerchantWebhookMoneyAmount
from univapayclientsdk.models.merchant_webhook_online_configuration import MerchantWebhookOnlineConfiguration
from univapayclientsdk.models.merchant_webhook_paidy_configuration import MerchantWebhookPaidyConfiguration
from univapayclientsdk.models.merchant_webhook_qr_merchant_configuration import MerchantWebhookQrMerchantConfiguration
from univapayclientsdk.models.merchant_webhook_qr_scan_configuration import MerchantWebhookQrScanConfiguration
from univapayclientsdk.models.merchant_webhook_recurring_cvv_confirmation_config import MerchantWebhookRecurringCvvConfirmationConfig
from univapayclientsdk.models.merchant_webhook_recurring_token_configuration import MerchantWebhookRecurringTokenConfiguration
from univapayclientsdk.models.merchant_webhook_security_configuration import MerchantWebhookSecurityConfiguration
from univapayclientsdk.models.merchant_webhook_subscription_configuration import MerchantWebhookSubscriptionConfiguration
from univapayclientsdk.models.merchant_webhook_subscription_plan_configuration import MerchantWebhookSubscriptionPlanConfiguration
from univapayclientsdk.models.merchant_webhook_transfer_schedule_configuration import MerchantWebhookTransferScheduleConfiguration
from univapayclientsdk.models.merchant_webhook_user_transactions_configuration import MerchantWebhookUserTransactionsConfiguration
from univapayclientsdk.models.restrict_ip_after_failed_charge_config import RestrictIpAfterFailedChargeConfig

merchant_webhook_configuration = MerchantWebhookConfiguration(
    percent_fee=3.6,
    flat_fees=[
        MerchantWebhookMoneyAmount(
            amount=100,
            currency='JPY'
        )
    ],
    country='JP',
    language='ja',
    display_time_zone='Asia/Tokyo',
    min_transfer_payout=MerchantWebhookMoneyAmount(
        amount=5000,
        currency='JPY'
    ),
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
    transfer_schedule=MerchantWebhookTransferScheduleConfiguration(
        wait_period='P7D',
        period='weekly',
        full_period_required=False,
        weekly_closing_day='sunday',
        weekly_payout_day='friday'
    ),
    user_transactions_configuration=MerchantWebhookUserTransactionsConfiguration(
        enabled=True,
        notify_customer=True,
        notify_on_webhook_failure=True,
        notify_on_webhook_disabled=True,
        notify_on_subscriptions=True
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
    checkout_configuration=MerchantWebhookCheckoutConfiguration(
        ec_email=MerchantWebhookCheckoutToggle(
            enabled=True
        ),
        ec_products=MerchantWebhookCheckoutToggle(
            enabled=True
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
    subscription_plan_configuration=MerchantWebhookSubscriptionPlanConfiguration(
        enabled=True,
        fixed_cycle=True,
        fixed_cycle_amount=True,
        supported_payment_types=[
            'card'
        ],
        min_charge_amount=MerchantWebhookMoneyAmount(
            amount=3000,
            currency='JPY'
        ),
        max_payout_period='P12M'
    ),
    card_brand_percent_fees=MerchantWebhookCardBrandPercentFees(
        visa=3.6,
        mastercard=3.6,
        jcb=3.8
    ),
    subscription_configuration=MerchantWebhookSubscriptionConfiguration(
        enabled=True,
        failed_charges_to_cancel=3,
        suspend_on_cancel=True,
        allow_merchant_amount_patch=False,
        allow_merchant_due_date_patch=False
    ),
    customer_management_configuration=MerchantWebhookCustomerManagementConfiguration(
        enabled=True,
        default_roles=[
            'end_user'
        ],
        default_mode='live'
    ),
    descriptor_provided_configuration=False,
    card_configuration=MerchantWebhookCardConfiguration(
        enabled=True,
        debit_enabled=True,
        prepaid_enabled=False,
        foreign_cards_allowed=False,
        three_ds_required=True,
        allow_direct_token_creation=False
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
    qr_merchant_configuration=MerchantWebhookQrMerchantConfiguration(
        enabled=False
    ),
    online_configuration=MerchantWebhookOnlineConfiguration(
        enabled=True
    ),
    bank_transfer_configuration=MerchantWebhookBankTransferConfiguration(
        enabled=True,
        match_amount=True,
        expiration='P7D',
        virtual_bank_accounts_threshold=50,
        virtual_bank_accounts_fetch_count=25,
        default_extension_period='P3D',
        maximum_extension_period='P30D',
        automatic_extension_enabled=True,
        charge_request_notification_enabled=True,
        deposit_received_notification_enabled=True,
        remind_notification_period='P2D',
        remind_notification_enabled=True
    ),
    platform_credentials_enabled=True,
    tagged_platform_credentials_enabled=False
)
```

