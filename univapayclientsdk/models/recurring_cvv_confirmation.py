"""univapay_client_sdk.

This file was automatically generated for Univapay by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

# ruff: noqa: E501
from univapayclientsdk.api_helper import APIHelper
from univapayclientsdk.models.checkout_money_amount import (
    CheckoutMoneyAmount,
)


class RecurringCvvConfirmation(object):
    """Implementation of the 'RecurringCvvConfirmation' model.

    CVV re-confirmation policy applied to recurring card charges (subscriptions and
    tokens with recurring privilege).

    Attributes:
        enabled (bool): Whether CVV re-confirmation is required for recurring card
            charges. Resolves to `false` when not configured.
        threshold (List[CheckoutMoneyAmount]): Amount thresholds above which CVV
            re-confirmation is required. `null` when no threshold is configured.
        additional_properties (Dict[str, Any]): The additional properties for the
            model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "enabled": "enabled",
        "threshold": "threshold",
    }

    _optionals = [
        "enabled",
        "threshold",
    ]

    _nullables = [
        "threshold",
    ]

    def __init__(
        self,
        enabled=APIHelper.SKIP,
        threshold=APIHelper.SKIP,
        additional_properties=None):
        """Initialize a RecurringCvvConfirmation instance."""
        # Initialize members of the class
        if enabled is not APIHelper.SKIP:
            self.enabled = enabled
        if threshold is not APIHelper.SKIP:
            self.threshold = threshold

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
        if "threshold" in dictionary.keys():
            threshold = [
                CheckoutMoneyAmount.from_dictionary(x)
                for x in dictionary.get("threshold")
            ] if dictionary.get("threshold") else None
        else:
            threshold = APIHelper.SKIP

        additional_properties = APIHelper.get_additional_properties(
            dictionary={k: v for k, v in dictionary.items()
                        if k not in cls._names.values()},
            unboxing_function=lambda value: value)

        # Return an object of this model
        return cls(enabled,
                   threshold,
                   additional_properties)

    def __repr__(self):
        """Return a unambiguous string representation."""
        _enabled=(
            self.enabled
            if hasattr(self, "enabled")
            else None
        )
        _threshold=(
            self.threshold
            if hasattr(self, "threshold")
            else None
        )
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"enabled={_enabled!r}, "
            f"threshold={_threshold!r}, "
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
        _threshold=(
            self.threshold
            if hasattr(self, "threshold")
            else None
        )
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"enabled={_enabled!s}, "
            f"threshold={_threshold!s}, "
            f"additional_properties={_additional_properties!s}, "
            f")"
        )
