"""univapay_client_sdk.

This file was automatically generated for Univapay by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

# ruff: noqa: E501
from univapayclientsdk.api_helper import APIHelper
from univapayclientsdk.models.checkout_theme_colors import (
    CheckoutThemeColors,
)


class CheckoutTheme(object):
    """Implementation of the 'CheckoutTheme' model.

    Widget theme applied to checkout.

    Attributes:
        colors (CheckoutThemeColors): Hex colors applied to the checkout widget.
            Always resolves to the platform defaults shown here when not customized —
            never `null`.
        additional_properties (Dict[str, Any]): The additional properties for the
            model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "colors": "colors",
    }

    _optionals = [
        "colors",
    ]

    def __init__(
        self,
        colors=APIHelper.SKIP,
        additional_properties=None):
        """Initialize a CheckoutTheme instance."""
        # Initialize members of the class
        if colors is not APIHelper.SKIP:
            self.colors = colors

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
        colors =\
            CheckoutThemeColors.from_dictionary(
                dictionary.get("colors"))\
                if "colors" in dictionary.keys()\
                else APIHelper.SKIP

        additional_properties = APIHelper.get_additional_properties(
            dictionary={k: v for k, v in dictionary.items()
                        if k not in cls._names.values()},
            unboxing_function=lambda value: value)

        # Return an object of this model
        return cls(colors,
                   additional_properties)

    def __repr__(self):
        """Return a unambiguous string representation."""
        _colors=(
            self.colors
            if hasattr(self, "colors")
            else None
        )
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"colors={_colors!r}, "
            f"additional_properties={_additional_properties!r}, "
            f")"
        )

    def __str__(self):
        """Return a human-readable string representation."""
        _colors=(
            self.colors
            if hasattr(self, "colors")
            else None
        )
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"colors={_colors!s}, "
            f"additional_properties={_additional_properties!s}, "
            f")"
        )
