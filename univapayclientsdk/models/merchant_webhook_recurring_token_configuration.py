"""univapay_client_sdk.

This file was automatically generated for Univapay by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

# ruff: noqa: E501
from univapayclientsdk.api_helper import APIHelper
from univapayclientsdk.models.merchant_webhook_recurring_cvv_confirmation_config import (  # noqa: E501
    MerchantWebhookRecurringCvvConfirmationConfig,
)


class MerchantWebhookRecurringTokenConfiguration(object):
    """Implementation of the 'MerchantWebhookRecurringTokenConfiguration' model.

    Recurring token configuration inherited by the merchant.

    Attributes:
        recurring_type (str): Merchant recurring-token privilege.
        charge_wait_period (str): ISO-8601 duration to wait before first recurring
            charge.
        card_charge_cvv_confirmation (MerchantWebhookRecurringCvvConfirmationConfig):
            CVV confirmation rules for recurring token charges.
        additional_properties (Dict[str, Any]): The additional properties for the
            model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "recurring_type": "recurring_type",
        "charge_wait_period": "charge_wait_period",
        "card_charge_cvv_confirmation": "card_charge_cvv_confirmation",
    }

    _optionals = [
        "recurring_type",
        "charge_wait_period",
        "card_charge_cvv_confirmation",
    ]

    _nullables = [
        "recurring_type",
        "charge_wait_period",
    ]

    def __init__(
        self,
        recurring_type=APIHelper.SKIP,
        charge_wait_period=APIHelper.SKIP,
        card_charge_cvv_confirmation=APIHelper.SKIP,
        additional_properties=None):
        """Initialize a MerchantWebhookRecurringTokenConfiguration instance."""
        # Initialize members of the class
        if recurring_type is not APIHelper.SKIP:
            self.recurring_type = recurring_type
        if charge_wait_period is not APIHelper.SKIP:
            self.charge_wait_period = charge_wait_period
        if card_charge_cvv_confirmation is not APIHelper.SKIP:
            self.card_charge_cvv_confirmation = card_charge_cvv_confirmation

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
        recurring_type =\
            dictionary.get("recurring_type")\
            if "recurring_type" in dictionary.keys()\
                else APIHelper.SKIP
        charge_wait_period =\
            dictionary.get("charge_wait_period")\
            if "charge_wait_period" in dictionary.keys()\
                else APIHelper.SKIP
        card_charge_cvv_confirmation =\
            MerchantWebhookRecurringCvvConfirmationConfig.from_dictionary(
                dictionary.get("card_charge_cvv_confirmation"))\
                if "card_charge_cvv_confirmation" in dictionary.keys()\
                else APIHelper.SKIP

        additional_properties = APIHelper.get_additional_properties(
            dictionary={k: v for k, v in dictionary.items()
                        if k not in cls._names.values()},
            unboxing_function=lambda value: value)

        # Return an object of this model
        return cls(recurring_type,
                   charge_wait_period,
                   card_charge_cvv_confirmation,
                   additional_properties)

    def __repr__(self):
        """Return a unambiguous string representation."""
        _recurring_type=(
            self.recurring_type
            if hasattr(self, "recurring_type")
            else None
        )
        _charge_wait_period=(
            self.charge_wait_period
            if hasattr(self, "charge_wait_period")
            else None
        )
        _card_charge_cvv_confirmation=(
            self.card_charge_cvv_confirmation
            if hasattr(self, "card_charge_cvv_confirmation")
            else None
        )
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"recurring_type={_recurring_type!r}, "
            f"charge_wait_period={_charge_wait_period!r}, "
            f"card_charge_cvv_confirmation={_card_charge_cvv_confirmation!r}, "
            f"additional_properties={_additional_properties!r}, "
            f")"
        )

    def __str__(self):
        """Return a human-readable string representation."""
        _recurring_type=(
            self.recurring_type
            if hasattr(self, "recurring_type")
            else None
        )
        _charge_wait_period=(
            self.charge_wait_period
            if hasattr(self, "charge_wait_period")
            else None
        )
        _card_charge_cvv_confirmation=(
            self.card_charge_cvv_confirmation
            if hasattr(self, "card_charge_cvv_confirmation")
            else None
        )
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"recurring_type={_recurring_type!s}, "
            f"charge_wait_period={_charge_wait_period!s}, "
            f"card_charge_cvv_confirmation={_card_charge_cvv_confirmation!s}, "
            f"additional_properties={_additional_properties!s}, "
            f")"
        )
