"""univapay_client_sdk.

This file was automatically generated for Univapay by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

# ruff: noqa: E501
from univapayclientsdk.api_helper import APIHelper
from univapayclientsdk.models.merchant_webhook_bank_transfer_configuration import (
    MerchantWebhookBankTransferConfiguration,
)
from univapayclientsdk.models.merchant_webhook_card_brand_percent_fees import (
    MerchantWebhookCardBrandPercentFees,
)
from univapayclientsdk.models.merchant_webhook_card_configuration import (
    MerchantWebhookCardConfiguration,
)
from univapayclientsdk.models.merchant_webhook_checkout_configuration import (
    MerchantWebhookCheckoutConfiguration,
)
from univapayclientsdk.models.merchant_webhook_convenience_configuration import (
    MerchantWebhookConvenienceConfiguration,
)
from univapayclientsdk.models.merchant_webhook_customer_management_configuration import (  # noqa: E501
    MerchantWebhookCustomerManagementConfiguration,
)
from univapayclientsdk.models.merchant_webhook_installment_plan_configuration import (
    MerchantWebhookInstallmentPlanConfiguration,
)
from univapayclientsdk.models.merchant_webhook_money_amount import (
    MerchantWebhookMoneyAmount,
)
from univapayclientsdk.models.merchant_webhook_online_configuration import (
    MerchantWebhookOnlineConfiguration,
)
from univapayclientsdk.models.merchant_webhook_paidy_configuration import (
    MerchantWebhookPaidyConfiguration,
)
from univapayclientsdk.models.merchant_webhook_qr_merchant_configuration import (
    MerchantWebhookQrMerchantConfiguration,
)
from univapayclientsdk.models.merchant_webhook_qr_scan_configuration import (
    MerchantWebhookQrScanConfiguration,
)
from univapayclientsdk.models.merchant_webhook_recurring_token_configuration import (
    MerchantWebhookRecurringTokenConfiguration,
)
from univapayclientsdk.models.merchant_webhook_security_configuration import (
    MerchantWebhookSecurityConfiguration,
)
from univapayclientsdk.models.merchant_webhook_subscription_configuration import (
    MerchantWebhookSubscriptionConfiguration,
)
from univapayclientsdk.models.merchant_webhook_subscription_plan_configuration import (
    MerchantWebhookSubscriptionPlanConfiguration,
)
from univapayclientsdk.models.merchant_webhook_transfer_schedule_configuration import (
    MerchantWebhookTransferScheduleConfiguration,
)
from univapayclientsdk.models.merchant_webhook_user_transactions_configuration import (
    MerchantWebhookUserTransactionsConfiguration,
)


class MerchantWebhookConfiguration(object):
    """Implementation of the 'MerchantWebhookConfiguration' model.

    Merchant configuration object as serialized by the backend.

    Attributes:
        percent_fee (float): Default percent fee applied when no card-brand override
            exists.
        flat_fees (List[MerchantWebhookMoneyAmount]): Flat fee overrides by currency.
        logo_url (str): Merchant logo URL.
        country (str): Merchant country code.
        language (str): Merchant default language.
        display_time_zone (str): Merchant display time zone.
        min_transfer_payout (MerchantWebhookMoneyAmount): Monetary amount object
            serialized by backend config models.
        minimum_charge_amounts (List[MerchantWebhookMoneyAmount]): Minimum allowed
            charge amounts by currency.
        maximum_charge_amounts (List[MerchantWebhookMoneyAmount]): Maximum allowed
            charge amounts by currency.
        transfer_schedule (MerchantWebhookTransferScheduleConfiguration): Transfer
            schedule configuration inherited by the merchant.
        user_transactions_configuration
            (MerchantWebhookUserTransactionsConfiguration): Merchant transaction
            notification settings.
        recurring_token_configuration (MerchantWebhookRecurringTokenConfiguration):
            Recurring token configuration inherited by the merchant.
        security_configuration (MerchantWebhookSecurityConfiguration): Merchant-level
            fraud and refund safety settings.
        checkout_configuration (MerchantWebhookCheckoutConfiguration): Checkout field
            collection settings.
        installments_configuration (MerchantWebhookInstallmentPlanConfiguration):
            Installment plan configuration.
        subscription_plan_configuration
            (MerchantWebhookSubscriptionPlanConfiguration): Subscription plan
            configuration.
        card_brand_percent_fees (MerchantWebhookCardBrandPercentFees): Per-card-brand
            percent fee overrides.
        subscription_configuration (MerchantWebhookSubscriptionConfiguration):
            Subscription feature configuration.
        customer_management_configuration
            (MerchantWebhookCustomerManagementConfiguration): Customer-management
            defaults.
        descriptor_provided_configuration (bool): Whether statement descriptors can
            be provided by merchants.
        card_configuration (MerchantWebhookCardConfiguration): Card payment settings.
        qr_scan_configuration (MerchantWebhookQrScanConfiguration): QR scan payment
            settings.
        convenience_configuration (MerchantWebhookConvenienceConfiguration):
            Convenience-store payment settings.
        paidy_configuration (MerchantWebhookPaidyConfiguration): Paidy payment
            settings.
        qr_merchant_configuration (MerchantWebhookQrMerchantConfiguration): QR
            merchant payment settings.
        online_configuration (MerchantWebhookOnlineConfiguration): Online payment
            settings.
        bank_transfer_configuration (MerchantWebhookBankTransferConfiguration): Bank
            transfer payment settings.
        platform_credentials_enabled (bool): Whether platform credentials are enabled.
        tagged_platform_credentials_enabled (bool): Whether tagged platform
            credentials are enabled.
        additional_properties (Dict[str, Any]): The additional properties for the
            model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "percent_fee": "percent_fee",
        "flat_fees": "flat_fees",
        "logo_url": "logo_url",
        "country": "country",
        "language": "language",
        "display_time_zone": "display_time_zone",
        "min_transfer_payout": "min_transfer_payout",
        "minimum_charge_amounts": "minimum_charge_amounts",
        "maximum_charge_amounts": "maximum_charge_amounts",
        "transfer_schedule": "transfer_schedule",
        "user_transactions_configuration": "user_transactions_configuration",
        "recurring_token_configuration": "recurring_token_configuration",
        "security_configuration": "security_configuration",
        "checkout_configuration": "checkout_configuration",
        "installments_configuration": "installments_configuration",
        "subscription_plan_configuration": "subscription_plan_configuration",
        "card_brand_percent_fees": "card_brand_percent_fees",
        "subscription_configuration": "subscription_configuration",
        "customer_management_configuration": "customer_management_configuration",
        "descriptor_provided_configuration": "descriptor_provided_configuration",
        "card_configuration": "card_configuration",
        "qr_scan_configuration": "qr_scan_configuration",
        "convenience_configuration": "convenience_configuration",
        "paidy_configuration": "paidy_configuration",
        "qr_merchant_configuration": "qr_merchant_configuration",
        "online_configuration": "online_configuration",
        "bank_transfer_configuration": "bank_transfer_configuration",
        "platform_credentials_enabled": "platform_credentials_enabled",
        "tagged_platform_credentials_enabled": "tagged_platform_credentials_enabled",
    }

    _optionals = [
        "percent_fee",
        "flat_fees",
        "logo_url",
        "country",
        "language",
        "display_time_zone",
        "min_transfer_payout",
        "minimum_charge_amounts",
        "maximum_charge_amounts",
        "transfer_schedule",
        "user_transactions_configuration",
        "recurring_token_configuration",
        "security_configuration",
        "checkout_configuration",
        "installments_configuration",
        "subscription_plan_configuration",
        "card_brand_percent_fees",
        "subscription_configuration",
        "customer_management_configuration",
        "descriptor_provided_configuration",
        "card_configuration",
        "qr_scan_configuration",
        "convenience_configuration",
        "paidy_configuration",
        "qr_merchant_configuration",
        "online_configuration",
        "bank_transfer_configuration",
        "platform_credentials_enabled",
        "tagged_platform_credentials_enabled",
    ]

    _nullables = [
        "percent_fee",
        "logo_url",
        "country",
        "language",
        "display_time_zone",
        "descriptor_provided_configuration",
        "platform_credentials_enabled",
        "tagged_platform_credentials_enabled",
    ]

    def __init__(
        self,
        percent_fee=APIHelper.SKIP,
        flat_fees=APIHelper.SKIP,
        logo_url=APIHelper.SKIP,
        country=APIHelper.SKIP,
        language=APIHelper.SKIP,
        display_time_zone=APIHelper.SKIP,
        min_transfer_payout=APIHelper.SKIP,
        minimum_charge_amounts=APIHelper.SKIP,
        maximum_charge_amounts=APIHelper.SKIP,
        transfer_schedule=APIHelper.SKIP,
        user_transactions_configuration=APIHelper.SKIP,
        recurring_token_configuration=APIHelper.SKIP,
        security_configuration=APIHelper.SKIP,
        checkout_configuration=APIHelper.SKIP,
        installments_configuration=APIHelper.SKIP,
        subscription_plan_configuration=APIHelper.SKIP,
        card_brand_percent_fees=APIHelper.SKIP,
        subscription_configuration=APIHelper.SKIP,
        customer_management_configuration=APIHelper.SKIP,
        descriptor_provided_configuration=APIHelper.SKIP,
        card_configuration=APIHelper.SKIP,
        qr_scan_configuration=APIHelper.SKIP,
        convenience_configuration=APIHelper.SKIP,
        paidy_configuration=APIHelper.SKIP,
        qr_merchant_configuration=APIHelper.SKIP,
        online_configuration=APIHelper.SKIP,
        bank_transfer_configuration=APIHelper.SKIP,
        platform_credentials_enabled=APIHelper.SKIP,
        tagged_platform_credentials_enabled=APIHelper.SKIP,
        additional_properties=None):
        """Initialize a MerchantWebhookConfiguration instance."""
        # Initialize members of the class
        if percent_fee is not APIHelper.SKIP:
            self.percent_fee = percent_fee
        if flat_fees is not APIHelper.SKIP:
            self.flat_fees = flat_fees
        if logo_url is not APIHelper.SKIP:
            self.logo_url = logo_url
        if country is not APIHelper.SKIP:
            self.country = country
        if language is not APIHelper.SKIP:
            self.language = language
        if display_time_zone is not APIHelper.SKIP:
            self.display_time_zone = display_time_zone
        if min_transfer_payout is not APIHelper.SKIP:
            self.min_transfer_payout = min_transfer_payout
        if minimum_charge_amounts is not APIHelper.SKIP:
            self.minimum_charge_amounts = minimum_charge_amounts
        if maximum_charge_amounts is not APIHelper.SKIP:
            self.maximum_charge_amounts = maximum_charge_amounts
        if transfer_schedule is not APIHelper.SKIP:
            self.transfer_schedule = transfer_schedule
        if user_transactions_configuration is not APIHelper.SKIP:
            self.user_transactions_configuration = user_transactions_configuration
        if recurring_token_configuration is not APIHelper.SKIP:
            self.recurring_token_configuration = recurring_token_configuration
        if security_configuration is not APIHelper.SKIP:
            self.security_configuration = security_configuration
        if checkout_configuration is not APIHelper.SKIP:
            self.checkout_configuration = checkout_configuration
        if installments_configuration is not APIHelper.SKIP:
            self.installments_configuration = installments_configuration
        if subscription_plan_configuration is not APIHelper.SKIP:
            self.subscription_plan_configuration = subscription_plan_configuration
        if card_brand_percent_fees is not APIHelper.SKIP:
            self.card_brand_percent_fees = card_brand_percent_fees
        if subscription_configuration is not APIHelper.SKIP:
            self.subscription_configuration = subscription_configuration
        if customer_management_configuration is not APIHelper.SKIP:
            self.customer_management_configuration =\
                 customer_management_configuration
        if descriptor_provided_configuration is not APIHelper.SKIP:
            self.descriptor_provided_configuration =\
                 descriptor_provided_configuration
        if card_configuration is not APIHelper.SKIP:
            self.card_configuration = card_configuration
        if qr_scan_configuration is not APIHelper.SKIP:
            self.qr_scan_configuration = qr_scan_configuration
        if convenience_configuration is not APIHelper.SKIP:
            self.convenience_configuration = convenience_configuration
        if paidy_configuration is not APIHelper.SKIP:
            self.paidy_configuration = paidy_configuration
        if qr_merchant_configuration is not APIHelper.SKIP:
            self.qr_merchant_configuration = qr_merchant_configuration
        if online_configuration is not APIHelper.SKIP:
            self.online_configuration = online_configuration
        if bank_transfer_configuration is not APIHelper.SKIP:
            self.bank_transfer_configuration = bank_transfer_configuration
        if platform_credentials_enabled is not APIHelper.SKIP:
            self.platform_credentials_enabled = platform_credentials_enabled
        if tagged_platform_credentials_enabled is not APIHelper.SKIP:
            self.tagged_platform_credentials_enabled =\
                 tagged_platform_credentials_enabled

        # Add additional model properties to the instance
        if additional_properties is None:
            additional_properties = {}
        self.additional_properties = additional_properties

    @classmethod
    def from_dictionary(cls,
                        dictionary):
        """Create an instance of this model from a dictionary

        Args:
            dictionary (dictionary): A dictionary representation of the object
            as obtained from the deserialization of the server's response. The
            keys MUST match property names in the API description.

        Returns:
            object: An instance of this structure class.

        """
        if not isinstance(dictionary, dict) or dictionary is None:
            return None

        # Extract variables from the dictionary
        percent_fee =\
            dictionary.get("percent_fee")\
            if "percent_fee" in dictionary.keys()\
                else APIHelper.SKIP
        flat_fees = None
        if dictionary.get("flat_fees") is not None:
            flat_fees = [
                MerchantWebhookMoneyAmount.from_dictionary(x)
                    for x in dictionary.get("flat_fees")
            ]
        else:
            flat_fees = APIHelper.SKIP
        logo_url =\
            dictionary.get("logo_url")\
            if "logo_url" in dictionary.keys()\
                else APIHelper.SKIP
        country =\
            dictionary.get("country")\
            if "country" in dictionary.keys()\
                else APIHelper.SKIP
        language =\
            dictionary.get("language")\
            if "language" in dictionary.keys()\
                else APIHelper.SKIP
        display_time_zone =\
            dictionary.get("display_time_zone")\
            if "display_time_zone" in dictionary.keys()\
                else APIHelper.SKIP
        min_transfer_payout =\
            MerchantWebhookMoneyAmount.from_dictionary(
                dictionary.get("min_transfer_payout"))\
                if "min_transfer_payout" in dictionary.keys()\
                else APIHelper.SKIP
        minimum_charge_amounts = None
        if dictionary.get("minimum_charge_amounts") is not None:
            minimum_charge_amounts = [
                MerchantWebhookMoneyAmount.from_dictionary(x)
                    for x in dictionary.get("minimum_charge_amounts")
            ]
        else:
            minimum_charge_amounts = APIHelper.SKIP
        maximum_charge_amounts = None
        if dictionary.get("maximum_charge_amounts") is not None:
            maximum_charge_amounts = [
                MerchantWebhookMoneyAmount.from_dictionary(x)
                    for x in dictionary.get("maximum_charge_amounts")
            ]
        else:
            maximum_charge_amounts = APIHelper.SKIP
        transfer_schedule =\
            MerchantWebhookTransferScheduleConfiguration.from_dictionary(
                dictionary.get("transfer_schedule"))\
                if "transfer_schedule" in dictionary.keys()\
                else APIHelper.SKIP
        user_transactions_configuration =\
            MerchantWebhookUserTransactionsConfiguration.from_dictionary(
                dictionary.get("user_transactions_configuration"))\
                if "user_transactions_configuration" in dictionary.keys()\
                else APIHelper.SKIP
        recurring_token_configuration =\
            MerchantWebhookRecurringTokenConfiguration.from_dictionary(
                dictionary.get("recurring_token_configuration"))\
                if "recurring_token_configuration" in dictionary.keys()\
                else APIHelper.SKIP
        security_configuration =\
            MerchantWebhookSecurityConfiguration.from_dictionary(
                dictionary.get("security_configuration"))\
                if "security_configuration" in dictionary.keys()\
                else APIHelper.SKIP
        checkout_configuration =\
            MerchantWebhookCheckoutConfiguration.from_dictionary(
                dictionary.get("checkout_configuration"))\
                if "checkout_configuration" in dictionary.keys()\
                else APIHelper.SKIP
        installments_configuration =\
            MerchantWebhookInstallmentPlanConfiguration.from_dictionary(
                dictionary.get("installments_configuration"))\
                if "installments_configuration" in dictionary.keys()\
                else APIHelper.SKIP
        subscription_plan_configuration =\
            MerchantWebhookSubscriptionPlanConfiguration.from_dictionary(
                dictionary.get("subscription_plan_configuration"))\
                if "subscription_plan_configuration" in dictionary.keys()\
                else APIHelper.SKIP
        card_brand_percent_fees =\
            MerchantWebhookCardBrandPercentFees.from_dictionary(
                dictionary.get("card_brand_percent_fees"))\
                if "card_brand_percent_fees" in dictionary.keys()\
                else APIHelper.SKIP
        subscription_configuration =\
            MerchantWebhookSubscriptionConfiguration.from_dictionary(
                dictionary.get("subscription_configuration"))\
                if "subscription_configuration" in dictionary.keys()\
                else APIHelper.SKIP
        customer_management_configuration =\
            MerchantWebhookCustomerManagementConfiguration.from_dictionary(
                dictionary.get("customer_management_configuration"))\
                if "customer_management_configuration" in dictionary.keys()\
                else APIHelper.SKIP
        descriptor_provided_configuration =\
            dictionary.get("descriptor_provided_configuration")\
            if "descriptor_provided_configuration" in dictionary.keys()\
                else APIHelper.SKIP
        card_configuration =\
            MerchantWebhookCardConfiguration.from_dictionary(
                dictionary.get("card_configuration"))\
                if "card_configuration" in dictionary.keys()\
                else APIHelper.SKIP
        qr_scan_configuration =\
            MerchantWebhookQrScanConfiguration.from_dictionary(
                dictionary.get("qr_scan_configuration"))\
                if "qr_scan_configuration" in dictionary.keys()\
                else APIHelper.SKIP
        convenience_configuration =\
            MerchantWebhookConvenienceConfiguration.from_dictionary(
                dictionary.get("convenience_configuration"))\
                if "convenience_configuration" in dictionary.keys()\
                else APIHelper.SKIP
        paidy_configuration =\
            MerchantWebhookPaidyConfiguration.from_dictionary(
                dictionary.get("paidy_configuration"))\
                if "paidy_configuration" in dictionary.keys()\
                else APIHelper.SKIP
        qr_merchant_configuration =\
            MerchantWebhookQrMerchantConfiguration.from_dictionary(
                dictionary.get("qr_merchant_configuration"))\
                if "qr_merchant_configuration" in dictionary.keys()\
                else APIHelper.SKIP
        online_configuration =\
            MerchantWebhookOnlineConfiguration.from_dictionary(
                dictionary.get("online_configuration"))\
                if "online_configuration" in dictionary.keys()\
                else APIHelper.SKIP
        bank_transfer_configuration =\
            MerchantWebhookBankTransferConfiguration.from_dictionary(
                dictionary.get("bank_transfer_configuration"))\
                if "bank_transfer_configuration" in dictionary.keys()\
                else APIHelper.SKIP
        platform_credentials_enabled =\
            dictionary.get("platform_credentials_enabled")\
            if "platform_credentials_enabled" in dictionary.keys()\
                else APIHelper.SKIP
        tagged_platform_credentials_enabled =\
            dictionary.get("tagged_platform_credentials_enabled")\
            if "tagged_platform_credentials_enabled" in dictionary.keys()\
                else APIHelper.SKIP

        additional_properties = APIHelper.get_additional_properties(
            dictionary={k: v for k, v in dictionary.items()
                        if k not in cls._names.values()},
            unboxing_function=lambda value: value)

        # Return an object of this model
        return cls(percent_fee,
                   flat_fees,
                   logo_url,
                   country,
                   language,
                   display_time_zone,
                   min_transfer_payout,
                   minimum_charge_amounts,
                   maximum_charge_amounts,
                   transfer_schedule,
                   user_transactions_configuration,
                   recurring_token_configuration,
                   security_configuration,
                   checkout_configuration,
                   installments_configuration,
                   subscription_plan_configuration,
                   card_brand_percent_fees,
                   subscription_configuration,
                   customer_management_configuration,
                   descriptor_provided_configuration,
                   card_configuration,
                   qr_scan_configuration,
                   convenience_configuration,
                   paidy_configuration,
                   qr_merchant_configuration,
                   online_configuration,
                   bank_transfer_configuration,
                   platform_credentials_enabled,
                   tagged_platform_credentials_enabled,
                   additional_properties)

    def __repr__(self):
        """Return a unambiguous string representation."""
        _percent_fee=(
            self.percent_fee
            if hasattr(self, "percent_fee")
            else None
        )
        _flat_fees=(
            self.flat_fees
            if hasattr(self, "flat_fees")
            else None
        )
        _logo_url=(
            self.logo_url
            if hasattr(self, "logo_url")
            else None
        )
        _country=(
            self.country
            if hasattr(self, "country")
            else None
        )
        _language=(
            self.language
            if hasattr(self, "language")
            else None
        )
        _display_time_zone=(
            self.display_time_zone
            if hasattr(self, "display_time_zone")
            else None
        )
        _min_transfer_payout=(
            self.min_transfer_payout
            if hasattr(self, "min_transfer_payout")
            else None
        )
        _minimum_charge_amounts=(
            self.minimum_charge_amounts
            if hasattr(self, "minimum_charge_amounts")
            else None
        )
        _maximum_charge_amounts=(
            self.maximum_charge_amounts
            if hasattr(self, "maximum_charge_amounts")
            else None
        )
        _transfer_schedule=(
            self.transfer_schedule
            if hasattr(self, "transfer_schedule")
            else None
        )
        _user_transactions_configuration=(
            self.user_transactions_configuration
            if hasattr(self, "user_transactions_configuration")
            else None
        )
        _recurring_token_configuration=(
            self.recurring_token_configuration
            if hasattr(self, "recurring_token_configuration")
            else None
        )
        _security_configuration=(
            self.security_configuration
            if hasattr(self, "security_configuration")
            else None
        )
        _checkout_configuration=(
            self.checkout_configuration
            if hasattr(self, "checkout_configuration")
            else None
        )
        _installments_configuration=(
            self.installments_configuration
            if hasattr(self, "installments_configuration")
            else None
        )
        _subscription_plan_configuration=(
            self.subscription_plan_configuration
            if hasattr(self, "subscription_plan_configuration")
            else None
        )
        _card_brand_percent_fees=(
            self.card_brand_percent_fees
            if hasattr(self, "card_brand_percent_fees")
            else None
        )
        _subscription_configuration=(
            self.subscription_configuration
            if hasattr(self, "subscription_configuration")
            else None
        )
        _customer_management_configuration=(
            self.customer_management_configuration
            if hasattr(self, "customer_management_configuration")
            else None
        )
        _descriptor_provided_configuration=(
            self.descriptor_provided_configuration
            if hasattr(self, "descriptor_provided_configuration")
            else None
        )
        _card_configuration=(
            self.card_configuration
            if hasattr(self, "card_configuration")
            else None
        )
        _qr_scan_configuration=(
            self.qr_scan_configuration
            if hasattr(self, "qr_scan_configuration")
            else None
        )
        _convenience_configuration=(
            self.convenience_configuration
            if hasattr(self, "convenience_configuration")
            else None
        )
        _paidy_configuration=(
            self.paidy_configuration
            if hasattr(self, "paidy_configuration")
            else None
        )
        _qr_merchant_configuration=(
            self.qr_merchant_configuration
            if hasattr(self, "qr_merchant_configuration")
            else None
        )
        _online_configuration=(
            self.online_configuration
            if hasattr(self, "online_configuration")
            else None
        )
        _bank_transfer_configuration=(
            self.bank_transfer_configuration
            if hasattr(self, "bank_transfer_configuration")
            else None
        )
        _platform_credentials_enabled=(
            self.platform_credentials_enabled
            if hasattr(self, "platform_credentials_enabled")
            else None
        )
        _tagged_platform_credentials_enabled=(
            self.tagged_platform_credentials_enabled
            if hasattr(self, "tagged_platform_credentials_enabled")
            else None
        )
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"percent_fee={_percent_fee!r}, "
            f"flat_fees={_flat_fees!r}, "
            f"logo_url={_logo_url!r}, "
            f"country={_country!r}, "
            f"language={_language!r}, "
            f"display_time_zone={_display_time_zone!r}, "
            f"min_transfer_payout={_min_transfer_payout!r}, "
            f"minimum_charge_amounts={_minimum_charge_amounts!r}, "
            f"maximum_charge_amounts={_maximum_charge_amounts!r}, "
            f"transfer_schedule={_transfer_schedule!r}, "
            f"user_transactions_configuration={_user_transactions_configuration!r}, "
            f"recurring_token_configuration={_recurring_token_configuration!r}, "
            f"security_configuration={_security_configuration!r}, "
            f"checkout_configuration={_checkout_configuration!r}, "
            f"installments_configuration={_installments_configuration!r}, "
            f"subscription_plan_configuration={_subscription_plan_configuration!r}, "
            f"card_brand_percent_fees={_card_brand_percent_fees!r}, "
            f"subscription_configuration={_subscription_configuration!r}, "
            f"customer_management_configuration={_customer_management_configuration!r}, "
            f"descriptor_provided_configuration={_descriptor_provided_configuration!r}, "
            f"card_configuration={_card_configuration!r}, "
            f"qr_scan_configuration={_qr_scan_configuration!r}, "
            f"convenience_configuration={_convenience_configuration!r}, "
            f"paidy_configuration={_paidy_configuration!r}, "
            f"qr_merchant_configuration={_qr_merchant_configuration!r}, "
            f"online_configuration={_online_configuration!r}, "
            f"bank_transfer_configuration={_bank_transfer_configuration!r}, "
            f"platform_credentials_enabled={_platform_credentials_enabled!r}, "
            f"tagged_platform_credentials_enabled={_tagged_platform_credentials_enabled!r}, "
            f"additional_properties={_additional_properties!r}, "
            f")"
        )

    def __str__(self):
        """Return a human-readable string representation."""
        _percent_fee=(
            self.percent_fee
            if hasattr(self, "percent_fee")
            else None
        )
        _flat_fees=(
            self.flat_fees
            if hasattr(self, "flat_fees")
            else None
        )
        _logo_url=(
            self.logo_url
            if hasattr(self, "logo_url")
            else None
        )
        _country=(
            self.country
            if hasattr(self, "country")
            else None
        )
        _language=(
            self.language
            if hasattr(self, "language")
            else None
        )
        _display_time_zone=(
            self.display_time_zone
            if hasattr(self, "display_time_zone")
            else None
        )
        _min_transfer_payout=(
            self.min_transfer_payout
            if hasattr(self, "min_transfer_payout")
            else None
        )
        _minimum_charge_amounts=(
            self.minimum_charge_amounts
            if hasattr(self, "minimum_charge_amounts")
            else None
        )
        _maximum_charge_amounts=(
            self.maximum_charge_amounts
            if hasattr(self, "maximum_charge_amounts")
            else None
        )
        _transfer_schedule=(
            self.transfer_schedule
            if hasattr(self, "transfer_schedule")
            else None
        )
        _user_transactions_configuration=(
            self.user_transactions_configuration
            if hasattr(self, "user_transactions_configuration")
            else None
        )
        _recurring_token_configuration=(
            self.recurring_token_configuration
            if hasattr(self, "recurring_token_configuration")
            else None
        )
        _security_configuration=(
            self.security_configuration
            if hasattr(self, "security_configuration")
            else None
        )
        _checkout_configuration=(
            self.checkout_configuration
            if hasattr(self, "checkout_configuration")
            else None
        )
        _installments_configuration=(
            self.installments_configuration
            if hasattr(self, "installments_configuration")
            else None
        )
        _subscription_plan_configuration=(
            self.subscription_plan_configuration
            if hasattr(self, "subscription_plan_configuration")
            else None
        )
        _card_brand_percent_fees=(
            self.card_brand_percent_fees
            if hasattr(self, "card_brand_percent_fees")
            else None
        )
        _subscription_configuration=(
            self.subscription_configuration
            if hasattr(self, "subscription_configuration")
            else None
        )
        _customer_management_configuration=(
            self.customer_management_configuration
            if hasattr(self, "customer_management_configuration")
            else None
        )
        _descriptor_provided_configuration=(
            self.descriptor_provided_configuration
            if hasattr(self, "descriptor_provided_configuration")
            else None
        )
        _card_configuration=(
            self.card_configuration
            if hasattr(self, "card_configuration")
            else None
        )
        _qr_scan_configuration=(
            self.qr_scan_configuration
            if hasattr(self, "qr_scan_configuration")
            else None
        )
        _convenience_configuration=(
            self.convenience_configuration
            if hasattr(self, "convenience_configuration")
            else None
        )
        _paidy_configuration=(
            self.paidy_configuration
            if hasattr(self, "paidy_configuration")
            else None
        )
        _qr_merchant_configuration=(
            self.qr_merchant_configuration
            if hasattr(self, "qr_merchant_configuration")
            else None
        )
        _online_configuration=(
            self.online_configuration
            if hasattr(self, "online_configuration")
            else None
        )
        _bank_transfer_configuration=(
            self.bank_transfer_configuration
            if hasattr(self, "bank_transfer_configuration")
            else None
        )
        _platform_credentials_enabled=(
            self.platform_credentials_enabled
            if hasattr(self, "platform_credentials_enabled")
            else None
        )
        _tagged_platform_credentials_enabled=(
            self.tagged_platform_credentials_enabled
            if hasattr(self, "tagged_platform_credentials_enabled")
            else None
        )
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"percent_fee={_percent_fee!s}, "
            f"flat_fees={_flat_fees!s}, "
            f"logo_url={_logo_url!s}, "
            f"country={_country!s}, "
            f"language={_language!s}, "
            f"display_time_zone={_display_time_zone!s}, "
            f"min_transfer_payout={_min_transfer_payout!s}, "
            f"minimum_charge_amounts={_minimum_charge_amounts!s}, "
            f"maximum_charge_amounts={_maximum_charge_amounts!s}, "
            f"transfer_schedule={_transfer_schedule!s}, "
            f"user_transactions_configuration={_user_transactions_configuration!s}, "
            f"recurring_token_configuration={_recurring_token_configuration!s}, "
            f"security_configuration={_security_configuration!s}, "
            f"checkout_configuration={_checkout_configuration!s}, "
            f"installments_configuration={_installments_configuration!s}, "
            f"subscription_plan_configuration={_subscription_plan_configuration!s}, "
            f"card_brand_percent_fees={_card_brand_percent_fees!s}, "
            f"subscription_configuration={_subscription_configuration!s}, "
            f"customer_management_configuration={_customer_management_configuration!s}, "
            f"descriptor_provided_configuration={_descriptor_provided_configuration!s}, "
            f"card_configuration={_card_configuration!s}, "
            f"qr_scan_configuration={_qr_scan_configuration!s}, "
            f"convenience_configuration={_convenience_configuration!s}, "
            f"paidy_configuration={_paidy_configuration!s}, "
            f"qr_merchant_configuration={_qr_merchant_configuration!s}, "
            f"online_configuration={_online_configuration!s}, "
            f"bank_transfer_configuration={_bank_transfer_configuration!s}, "
            f"platform_credentials_enabled={_platform_credentials_enabled!s}, "
            f"tagged_platform_credentials_enabled={_tagged_platform_credentials_enabled!s}, "
            f"additional_properties={_additional_properties!s}, "
            f")"
        )
