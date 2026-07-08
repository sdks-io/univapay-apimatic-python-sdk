"""univapay_client_sdk.

This file was automatically generated for Univapay by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

# ruff: noqa: E501
from univapayclientsdk.api_helper import APIHelper


class MerchantWebhookLimitChargeByCardConfiguration(object):
    """Implementation of the 'MerchantWebhookLimitChargeByCardConfiguration' model.

    Per-card velocity limit configuration.

    Attributes:
        quantity_of_charges (int): Maximum number of charges allowed in the time
            window.
        duration_window (str): ISO-8601 duration for the rolling window.
        additional_properties (Dict[str, Any]): The additional properties for the
            model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "quantity_of_charges": "quantity_of_charges",
        "duration_window": "duration_window",
    }

    _optionals = [
        "quantity_of_charges",
        "duration_window",
    ]

    def __init__(
        self,
        quantity_of_charges=APIHelper.SKIP,
        duration_window=APIHelper.SKIP,
        additional_properties=None):
        """Initialize a MerchantWebhookLimitChargeByCardConfiguration instance."""
        # Initialize members of the class
        if quantity_of_charges is not APIHelper.SKIP:
            self.quantity_of_charges = quantity_of_charges
        if duration_window is not APIHelper.SKIP:
            self.duration_window = duration_window

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
        quantity_of_charges =\
            dictionary.get("quantity_of_charges")\
            if dictionary.get("quantity_of_charges")\
                else APIHelper.SKIP
        duration_window =\
            dictionary.get("duration_window")\
            if dictionary.get("duration_window")\
                else APIHelper.SKIP

        additional_properties = APIHelper.get_additional_properties(
            dictionary={k: v for k, v in dictionary.items()
                        if k not in cls._names.values()},
            unboxing_function=lambda value: value)

        # Return an object of this model
        return cls(quantity_of_charges,
                   duration_window,
                   additional_properties)

    def __repr__(self):
        """Return a unambiguous string representation."""
        _quantity_of_charges=(
            self.quantity_of_charges
            if hasattr(self, "quantity_of_charges")
            else None
        )
        _duration_window=(
            self.duration_window
            if hasattr(self, "duration_window")
            else None
        )
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"quantity_of_charges={_quantity_of_charges!r}, "
            f"duration_window={_duration_window!r}, "
            f"additional_properties={_additional_properties!r}, "
            f")"
        )

    def __str__(self):
        """Return a human-readable string representation."""
        _quantity_of_charges=(
            self.quantity_of_charges
            if hasattr(self, "quantity_of_charges")
            else None
        )
        _duration_window=(
            self.duration_window
            if hasattr(self, "duration_window")
            else None
        )
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"quantity_of_charges={_quantity_of_charges!s}, "
            f"duration_window={_duration_window!s}, "
            f"additional_properties={_additional_properties!s}, "
            f")"
        )
