"""univapay_client_sdk.

This file was automatically generated for Univapay by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

# ruff: noqa: E501
from univapayclientsdk.api_helper import APIHelper
from univapayclientsdk.models.checkout_bank_transfer_configuration import (
    CheckoutBankTransferConfiguration,
)
from univapayclientsdk.models.checkout_card_configuration import (
    CheckoutCardConfiguration,
)
from univapayclientsdk.models.checkout_convenience_configuration import (
    CheckoutConvenienceConfiguration,
)
from univapayclientsdk.models.checkout_ec_configuration import (
    CheckoutEcConfiguration,
)
from univapayclientsdk.models.checkout_installments_configuration import (
    CheckoutInstallmentsConfiguration,
)
from univapayclientsdk.models.checkout_online_configuration import (
    CheckoutOnlineConfiguration,
)
from univapayclientsdk.models.checkout_paidy_configuration import (
    CheckoutPaidyConfiguration,
)
from univapayclientsdk.models.checkout_qr_scan_configuration import (
    CheckoutQrScanConfiguration,
)
from univapayclientsdk.models.checkout_subscription_configuration import (
    CheckoutSubscriptionConfiguration,
)
from univapayclientsdk.models.checkout_subscription_plan_configuration import (
    CheckoutSubscriptionPlanConfiguration,
)
from univapayclientsdk.models.checkout_supported_brand import (
    CheckoutSupportedBrand,
)
from univapayclientsdk.models.checkout_theme import (
    CheckoutTheme,
)
from univapayclientsdk.models.recurring_cvv_confirmation import (
    RecurringCvvConfirmation,
)


class CheckoutInfo(object):
    """Implementation of the 'CheckoutInfo' model.

    Merchant/store checkout configuration: enabled payment methods and their limits,
    installment/subscription plan settings, convenience-store and bank-transfer
    settings, widget theme, and per-brand feature support. Returned in full on every
    call — there is no partial-update or list variant.

    Attributes:
        mode (CheckoutMode): Store processing mode reflected in the checkout
            configuration: `live` and `test` reflect the credential used to
            authenticate, while `live_test` is reserved for privileged callers
            testing against live-mode data.
        recurring_token_privilege (CheckoutRecurringTokenPrivilege): Level of
            recurring-charge privilege granted to transaction tokens created under
            this store: `none` disallows recurring use, `bounded` allows a limited
            number of recurring charges, and `infinite` allows unlimited recurring
            charges.
        name (str): Store display name.
        card_configuration (CheckoutCardConfiguration): Card payment settings applied
            to checkout.
        subscription_configuration (CheckoutSubscriptionConfiguration):
            Univapay-hosted subscription feature toggle.
        installments_configuration (CheckoutInstallmentsConfiguration): Installment
            plan configuration applied to checkout.
        subscription_plan_configuration (CheckoutSubscriptionPlanConfiguration):
            Univapay-side subscription plan configuration applied to checkout.
        checkout_configuration (CheckoutEcConfiguration): EC checkout feature toggles
            for hosted email receipts and product line items.
        qr_scan_configuration (CheckoutQrScanConfiguration): QR-scan (CPM) payment
            settings applied to checkout.
        convenience_configuration (CheckoutConvenienceConfiguration):
            Convenience-store (konbini) payment settings applied to checkout.
        paidy_configuration (CheckoutPaidyConfiguration): Paidy payment feature
            toggle.
        paidy_public_key (str): Public key used to initialize the Paidy widget.
            `null` when Paidy is not configured for this store.
        logo_image (str): URL of the store's checkout logo image. `null` when no logo
            is configured. Note: this response field is `logo_image`, but the
            corresponding store-configuration update field is `logo_url` — the two
            names do not round-trip automatically.
        theme (CheckoutTheme): Widget theme applied to checkout.
        recurring_card_charge_cvv_confirmation (RecurringCvvConfirmation): CVV
            re-confirmation policy applied to recurring card charges (subscriptions
            and tokens with recurring privilege).
        online_configuration (CheckoutOnlineConfiguration): Online redirect/wallet
            payment feature toggle.
        bank_transfer_configuration (CheckoutBankTransferConfiguration): Bank
            transfer (振込) payment settings applied to checkout.
        supported_brands (List[CheckoutSupportedBrand]): Feature support and
            capability flags for every payment-type / brand combination the store can
            accept.
        additional_properties (Dict[str, Any]): The additional properties for the
            model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "mode": "mode",
        "recurring_token_privilege": "recurring_token_privilege",
        "name": "name",
        "card_configuration": "card_configuration",
        "subscription_configuration": "subscription_configuration",
        "installments_configuration": "installments_configuration",
        "subscription_plan_configuration": "subscription_plan_configuration",
        "checkout_configuration": "checkout_configuration",
        "qr_scan_configuration": "qr_scan_configuration",
        "convenience_configuration": "convenience_configuration",
        "paidy_configuration": "paidy_configuration",
        "paidy_public_key": "paidy_public_key",
        "logo_image": "logo_image",
        "theme": "theme",
        "recurring_card_charge_cvv_confirmation":
            "recurring_card_charge_cvv_confirmation",
        "online_configuration": "online_configuration",
        "bank_transfer_configuration": "bank_transfer_configuration",
        "supported_brands": "supported_brands",
    }

    _optionals = [
        "mode",
        "recurring_token_privilege",
        "name",
        "card_configuration",
        "subscription_configuration",
        "installments_configuration",
        "subscription_plan_configuration",
        "checkout_configuration",
        "qr_scan_configuration",
        "convenience_configuration",
        "paidy_configuration",
        "paidy_public_key",
        "logo_image",
        "theme",
        "recurring_card_charge_cvv_confirmation",
        "online_configuration",
        "bank_transfer_configuration",
        "supported_brands",
    ]

    _nullables = [
        "paidy_public_key",
        "logo_image",
    ]

    def __init__(
        self,
        mode=APIHelper.SKIP,
        recurring_token_privilege=APIHelper.SKIP,
        name=APIHelper.SKIP,
        card_configuration=APIHelper.SKIP,
        subscription_configuration=APIHelper.SKIP,
        installments_configuration=APIHelper.SKIP,
        subscription_plan_configuration=APIHelper.SKIP,
        checkout_configuration=APIHelper.SKIP,
        qr_scan_configuration=APIHelper.SKIP,
        convenience_configuration=APIHelper.SKIP,
        paidy_configuration=APIHelper.SKIP,
        paidy_public_key=APIHelper.SKIP,
        logo_image=APIHelper.SKIP,
        theme=APIHelper.SKIP,
        recurring_card_charge_cvv_confirmation=APIHelper.SKIP,
        online_configuration=APIHelper.SKIP,
        bank_transfer_configuration=APIHelper.SKIP,
        supported_brands=APIHelper.SKIP,
        additional_properties=None):
        """Initialize a CheckoutInfo instance."""
        # Initialize members of the class
        if mode is not APIHelper.SKIP:
            self.mode = mode
        if recurring_token_privilege is not APIHelper.SKIP:
            self.recurring_token_privilege = recurring_token_privilege
        if name is not APIHelper.SKIP:
            self.name = name
        if card_configuration is not APIHelper.SKIP:
            self.card_configuration = card_configuration
        if subscription_configuration is not APIHelper.SKIP:
            self.subscription_configuration = subscription_configuration
        if installments_configuration is not APIHelper.SKIP:
            self.installments_configuration = installments_configuration
        if subscription_plan_configuration is not APIHelper.SKIP:
            self.subscription_plan_configuration = subscription_plan_configuration
        if checkout_configuration is not APIHelper.SKIP:
            self.checkout_configuration = checkout_configuration
        if qr_scan_configuration is not APIHelper.SKIP:
            self.qr_scan_configuration = qr_scan_configuration
        if convenience_configuration is not APIHelper.SKIP:
            self.convenience_configuration = convenience_configuration
        if paidy_configuration is not APIHelper.SKIP:
            self.paidy_configuration = paidy_configuration
        if paidy_public_key is not APIHelper.SKIP:
            self.paidy_public_key = paidy_public_key
        if logo_image is not APIHelper.SKIP:
            self.logo_image = logo_image
        if theme is not APIHelper.SKIP:
            self.theme = theme
        if recurring_card_charge_cvv_confirmation is not APIHelper.SKIP:
            self.recurring_card_charge_cvv_confirmation =\
                 recurring_card_charge_cvv_confirmation
        if online_configuration is not APIHelper.SKIP:
            self.online_configuration = online_configuration
        if bank_transfer_configuration is not APIHelper.SKIP:
            self.bank_transfer_configuration = bank_transfer_configuration
        if supported_brands is not APIHelper.SKIP:
            self.supported_brands = supported_brands

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
        mode =\
            dictionary.get("mode")\
            if dictionary.get("mode")\
                else APIHelper.SKIP
        recurring_token_privilege =\
            dictionary.get("recurring_token_privilege")\
            if dictionary.get("recurring_token_privilege")\
                else APIHelper.SKIP
        name =\
            dictionary.get("name")\
            if dictionary.get("name")\
                else APIHelper.SKIP
        card_configuration =\
            CheckoutCardConfiguration.from_dictionary(
                dictionary.get("card_configuration"))\
                if "card_configuration" in dictionary.keys()\
                else APIHelper.SKIP
        subscription_configuration =\
            CheckoutSubscriptionConfiguration.from_dictionary(
                dictionary.get("subscription_configuration"))\
                if "subscription_configuration" in dictionary.keys()\
                else APIHelper.SKIP
        installments_configuration =\
            CheckoutInstallmentsConfiguration.from_dictionary(
                dictionary.get("installments_configuration"))\
                if "installments_configuration" in dictionary.keys()\
                else APIHelper.SKIP
        subscription_plan_configuration =\
            CheckoutSubscriptionPlanConfiguration.from_dictionary(
                dictionary.get("subscription_plan_configuration"))\
                if "subscription_plan_configuration" in dictionary.keys()\
                else APIHelper.SKIP
        checkout_configuration =\
            CheckoutEcConfiguration.from_dictionary(
                dictionary.get("checkout_configuration"))\
                if "checkout_configuration" in dictionary.keys()\
                else APIHelper.SKIP
        qr_scan_configuration =\
            CheckoutQrScanConfiguration.from_dictionary(
                dictionary.get("qr_scan_configuration"))\
                if "qr_scan_configuration" in dictionary.keys()\
                else APIHelper.SKIP
        convenience_configuration =\
            CheckoutConvenienceConfiguration.from_dictionary(
                dictionary.get("convenience_configuration"))\
                if "convenience_configuration" in dictionary.keys()\
                else APIHelper.SKIP
        paidy_configuration =\
            CheckoutPaidyConfiguration.from_dictionary(
                dictionary.get("paidy_configuration"))\
                if "paidy_configuration" in dictionary.keys()\
                else APIHelper.SKIP
        paidy_public_key =\
            dictionary.get("paidy_public_key")\
            if "paidy_public_key" in dictionary.keys()\
                else APIHelper.SKIP
        logo_image =\
            dictionary.get("logo_image")\
            if "logo_image" in dictionary.keys()\
                else APIHelper.SKIP
        theme =\
            CheckoutTheme.from_dictionary(
                dictionary.get("theme"))\
                if "theme" in dictionary.keys()\
                else APIHelper.SKIP
        recurring_card_charge_cvv_confirmation =\
            RecurringCvvConfirmation.from_dictionary(
                dictionary.get("recurring_card_charge_cvv_confirmation"))\
                if "recurring_card_charge_cvv_confirmation" in dictionary.keys()\
                else APIHelper.SKIP
        online_configuration =\
            CheckoutOnlineConfiguration.from_dictionary(
                dictionary.get("online_configuration"))\
                if "online_configuration" in dictionary.keys()\
                else APIHelper.SKIP
        bank_transfer_configuration =\
            CheckoutBankTransferConfiguration.from_dictionary(
                dictionary.get("bank_transfer_configuration"))\
                if "bank_transfer_configuration" in dictionary.keys()\
                else APIHelper.SKIP
        supported_brands = None
        if dictionary.get("supported_brands") is not None:
            supported_brands = [
                CheckoutSupportedBrand.from_dictionary(x)
                    for x in dictionary.get("supported_brands")
            ]
        else:
            supported_brands = APIHelper.SKIP

        additional_properties = APIHelper.get_additional_properties(
            dictionary={k: v for k, v in dictionary.items()
                        if k not in cls._names.values()},
            unboxing_function=lambda value: value)

        # Return an object of this model
        return cls(mode,
                   recurring_token_privilege,
                   name,
                   card_configuration,
                   subscription_configuration,
                   installments_configuration,
                   subscription_plan_configuration,
                   checkout_configuration,
                   qr_scan_configuration,
                   convenience_configuration,
                   paidy_configuration,
                   paidy_public_key,
                   logo_image,
                   theme,
                   recurring_card_charge_cvv_confirmation,
                   online_configuration,
                   bank_transfer_configuration,
                   supported_brands,
                   additional_properties)

    def __repr__(self):
        """Return a unambiguous string representation."""
        _mode=(
            self.mode
            if hasattr(self, "mode")
            else None
        )
        _recurring_token_privilege=(
            self.recurring_token_privilege
            if hasattr(self, "recurring_token_privilege")
            else None
        )
        _name=(
            self.name
            if hasattr(self, "name")
            else None
        )
        _card_configuration=(
            self.card_configuration
            if hasattr(self, "card_configuration")
            else None
        )
        _subscription_configuration=(
            self.subscription_configuration
            if hasattr(self, "subscription_configuration")
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
        _checkout_configuration=(
            self.checkout_configuration
            if hasattr(self, "checkout_configuration")
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
        _paidy_public_key=(
            self.paidy_public_key
            if hasattr(self, "paidy_public_key")
            else None
        )
        _logo_image=(
            self.logo_image
            if hasattr(self, "logo_image")
            else None
        )
        _theme=(
            self.theme
            if hasattr(self, "theme")
            else None
        )
        _recurring_card_charge_cvv_confirmation=(
            self.recurring_card_charge_cvv_confirmation
            if hasattr(self, "recurring_card_charge_cvv_confirmation")
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
        _supported_brands=(
            self.supported_brands
            if hasattr(self, "supported_brands")
            else None
        )
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"mode={_mode!r}, "
            f"recurring_token_privilege={_recurring_token_privilege!r}, "
            f"name={_name!r}, "
            f"card_configuration={_card_configuration!r}, "
            f"subscription_configuration={_subscription_configuration!r}, "
            f"installments_configuration={_installments_configuration!r}, "
            f"subscription_plan_configuration={_subscription_plan_configuration!r}, "
            f"checkout_configuration={_checkout_configuration!r}, "
            f"qr_scan_configuration={_qr_scan_configuration!r}, "
            f"convenience_configuration={_convenience_configuration!r}, "
            f"paidy_configuration={_paidy_configuration!r}, "
            f"paidy_public_key={_paidy_public_key!r}, "
            f"logo_image={_logo_image!r}, "
            f"theme={_theme!r}, "
            f"recurring_card_charge_cvv_confirmation={_recurring_card_charge_cvv_confirmation!r}, "
            f"online_configuration={_online_configuration!r}, "
            f"bank_transfer_configuration={_bank_transfer_configuration!r}, "
            f"supported_brands={_supported_brands!r}, "
            f"additional_properties={_additional_properties!r}, "
            f")"
        )

    def __str__(self):
        """Return a human-readable string representation."""
        _mode=(
            self.mode
            if hasattr(self, "mode")
            else None
        )
        _recurring_token_privilege=(
            self.recurring_token_privilege
            if hasattr(self, "recurring_token_privilege")
            else None
        )
        _name=(
            self.name
            if hasattr(self, "name")
            else None
        )
        _card_configuration=(
            self.card_configuration
            if hasattr(self, "card_configuration")
            else None
        )
        _subscription_configuration=(
            self.subscription_configuration
            if hasattr(self, "subscription_configuration")
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
        _checkout_configuration=(
            self.checkout_configuration
            if hasattr(self, "checkout_configuration")
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
        _paidy_public_key=(
            self.paidy_public_key
            if hasattr(self, "paidy_public_key")
            else None
        )
        _logo_image=(
            self.logo_image
            if hasattr(self, "logo_image")
            else None
        )
        _theme=(
            self.theme
            if hasattr(self, "theme")
            else None
        )
        _recurring_card_charge_cvv_confirmation=(
            self.recurring_card_charge_cvv_confirmation
            if hasattr(self, "recurring_card_charge_cvv_confirmation")
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
        _supported_brands=(
            self.supported_brands
            if hasattr(self, "supported_brands")
            else None
        )
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"mode={_mode!s}, "
            f"recurring_token_privilege={_recurring_token_privilege!s}, "
            f"name={_name!s}, "
            f"card_configuration={_card_configuration!s}, "
            f"subscription_configuration={_subscription_configuration!s}, "
            f"installments_configuration={_installments_configuration!s}, "
            f"subscription_plan_configuration={_subscription_plan_configuration!s}, "
            f"checkout_configuration={_checkout_configuration!s}, "
            f"qr_scan_configuration={_qr_scan_configuration!s}, "
            f"convenience_configuration={_convenience_configuration!s}, "
            f"paidy_configuration={_paidy_configuration!s}, "
            f"paidy_public_key={_paidy_public_key!s}, "
            f"logo_image={_logo_image!s}, "
            f"theme={_theme!s}, "
            f"recurring_card_charge_cvv_confirmation={_recurring_card_charge_cvv_confirmation!s}, "
            f"online_configuration={_online_configuration!s}, "
            f"bank_transfer_configuration={_bank_transfer_configuration!s}, "
            f"supported_brands={_supported_brands!s}, "
            f"additional_properties={_additional_properties!s}, "
            f")"
        )
