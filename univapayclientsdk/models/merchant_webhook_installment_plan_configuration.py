"""univapay_client_sdk.

This file was automatically generated for Univapay by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

# ruff: noqa: E501
from univapayclientsdk.api_helper import APIHelper
from univapayclientsdk.models.card_processor_installment_config import (
    CardProcessorInstallmentConfig,
)
from univapayclientsdk.models.merchant_webhook_money_amount import (
    MerchantWebhookMoneyAmount,
)


class MerchantWebhookInstallmentPlanConfiguration(object):
    """Implementation of the 'MerchantWebhookInstallmentPlanConfiguration' model.

    Installment plan configuration.

    Attributes:
        enabled (bool): Enables installment plan features for eligible payments.
        card_processor (CardProcessorInstallmentConfig): Card-processor capabilities
            available for installment payments.
        supported_payment_types (List[str]): Payment types that can use installment
            plans.
        min_charge_amount (MerchantWebhookMoneyAmount): Monetary amount object
            serialized by backend config models.
        max_payout_period (str): Maximum payout delay allowed for installment
            settlements.
        only_with_processor (bool): Restricts installment use to processor-backed
            flows.
        additional_properties (Dict[str, Any]): The additional properties for the
            model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "enabled": "enabled",
        "card_processor": "card_processor",
        "supported_payment_types": "supported_payment_types",
        "min_charge_amount": "min_charge_amount",
        "max_payout_period": "max_payout_period",
        "only_with_processor": "only_with_processor",
    }

    _optionals = [
        "enabled",
        "card_processor",
        "supported_payment_types",
        "min_charge_amount",
        "max_payout_period",
        "only_with_processor",
    ]

    _nullables = [
        "enabled",
        "supported_payment_types",
        "max_payout_period",
        "only_with_processor",
    ]

    def __init__(
        self,
        enabled=APIHelper.SKIP,
        card_processor=APIHelper.SKIP,
        supported_payment_types=APIHelper.SKIP,
        min_charge_amount=APIHelper.SKIP,
        max_payout_period=APIHelper.SKIP,
        only_with_processor=APIHelper.SKIP,
        additional_properties=None):
        """Initialize a MerchantWebhookInstallmentPlanConfiguration instance."""
        # Initialize members of the class
        if enabled is not APIHelper.SKIP:
            self.enabled = enabled
        if card_processor is not APIHelper.SKIP:
            self.card_processor = card_processor
        if supported_payment_types is not APIHelper.SKIP:
            self.supported_payment_types = supported_payment_types
        if min_charge_amount is not APIHelper.SKIP:
            self.min_charge_amount = min_charge_amount
        if max_payout_period is not APIHelper.SKIP:
            self.max_payout_period = max_payout_period
        if only_with_processor is not APIHelper.SKIP:
            self.only_with_processor = only_with_processor

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
        enabled =\
            dictionary.get("enabled")\
            if "enabled" in dictionary.keys()\
                else APIHelper.SKIP
        card_processor =\
            CardProcessorInstallmentConfig.from_dictionary(
                dictionary.get("card_processor"))\
                if "card_processor" in dictionary.keys()\
                else APIHelper.SKIP
        supported_payment_types =\
            dictionary.get("supported_payment_types")\
            if "supported_payment_types" in dictionary.keys()\
                else APIHelper.SKIP
        min_charge_amount =\
            MerchantWebhookMoneyAmount.from_dictionary(
                dictionary.get("min_charge_amount"))\
                if "min_charge_amount" in dictionary.keys()\
                else APIHelper.SKIP
        max_payout_period =\
            dictionary.get("max_payout_period")\
            if "max_payout_period" in dictionary.keys()\
                else APIHelper.SKIP
        only_with_processor =\
            dictionary.get("only_with_processor")\
            if "only_with_processor" in dictionary.keys()\
                else APIHelper.SKIP

        additional_properties = APIHelper.get_additional_properties(
            dictionary={k: v for k, v in dictionary.items()
                        if k not in cls._names.values()},
            unboxing_function=lambda value: value)

        # Return an object of this model
        return cls(enabled,
                   card_processor,
                   supported_payment_types,
                   min_charge_amount,
                   max_payout_period,
                   only_with_processor,
                   additional_properties)

    def __repr__(self):
        """Return a unambiguous string representation."""
        _enabled=(
            self.enabled
            if hasattr(self, "enabled")
            else None
        )
        _card_processor=(
            self.card_processor
            if hasattr(self, "card_processor")
            else None
        )
        _supported_payment_types=(
            self.supported_payment_types
            if hasattr(self, "supported_payment_types")
            else None
        )
        _min_charge_amount=(
            self.min_charge_amount
            if hasattr(self, "min_charge_amount")
            else None
        )
        _max_payout_period=(
            self.max_payout_period
            if hasattr(self, "max_payout_period")
            else None
        )
        _only_with_processor=(
            self.only_with_processor
            if hasattr(self, "only_with_processor")
            else None
        )
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"enabled={_enabled!r}, "
            f"card_processor={_card_processor!r}, "
            f"supported_payment_types={_supported_payment_types!r}, "
            f"min_charge_amount={_min_charge_amount!r}, "
            f"max_payout_period={_max_payout_period!r}, "
            f"only_with_processor={_only_with_processor!r}, "
            f"additional_properties={_additional_properties!r}, "
            f")"
        )

    def __str__(self):
        """Return a human-readable string representation."""
        _enabled=(
            self.enabled
            if hasattr(self, "enabled")
            else None
        )
        _card_processor=(
            self.card_processor
            if hasattr(self, "card_processor")
            else None
        )
        _supported_payment_types=(
            self.supported_payment_types
            if hasattr(self, "supported_payment_types")
            else None
        )
        _min_charge_amount=(
            self.min_charge_amount
            if hasattr(self, "min_charge_amount")
            else None
        )
        _max_payout_period=(
            self.max_payout_period
            if hasattr(self, "max_payout_period")
            else None
        )
        _only_with_processor=(
            self.only_with_processor
            if hasattr(self, "only_with_processor")
            else None
        )
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"enabled={_enabled!s}, "
            f"card_processor={_card_processor!s}, "
            f"supported_payment_types={_supported_payment_types!s}, "
            f"min_charge_amount={_min_charge_amount!s}, "
            f"max_payout_period={_max_payout_period!s}, "
            f"only_with_processor={_only_with_processor!s}, "
            f"additional_properties={_additional_properties!s}, "
            f")"
        )
