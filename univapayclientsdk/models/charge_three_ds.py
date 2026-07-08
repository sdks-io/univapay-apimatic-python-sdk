"""univapay_client_sdk.

This file was automatically generated for Univapay by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

# ruff: noqa: E501
from univapayclientsdk.api_helper import APIHelper


class ChargeThreeDs(object):
    """Implementation of the 'ChargeThreeDs' model.

    Charge Three Ds schema.

    Attributes:
        redirect_endpoint (str): Redirect endpoint URL.
        mode (str): Processing mode for the resource.
        additional_properties (Dict[str, Any]): The additional properties for the
            model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "redirect_endpoint": "redirect_endpoint",
        "mode": "mode",
    }

    _optionals = [
        "redirect_endpoint",
        "mode",
    ]

    def __init__(
        self,
        redirect_endpoint=APIHelper.SKIP,
        mode=APIHelper.SKIP,
        additional_properties=None):
        """Initialize a ChargeThreeDs instance."""
        # Initialize members of the class
        if redirect_endpoint is not APIHelper.SKIP:
            self.redirect_endpoint = redirect_endpoint
        if mode is not APIHelper.SKIP:
            self.mode = mode

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
        redirect_endpoint =\
            dictionary.get("redirect_endpoint")\
            if dictionary.get("redirect_endpoint")\
                else APIHelper.SKIP
        mode =\
            dictionary.get("mode")\
            if dictionary.get("mode")\
                else APIHelper.SKIP

        additional_properties = APIHelper.get_additional_properties(
            dictionary={k: v for k, v in dictionary.items()
                        if k not in cls._names.values()},
            unboxing_function=lambda value: value)

        # Return an object of this model
        return cls(redirect_endpoint,
                   mode,
                   additional_properties)

    @classmethod
    def validate(cls, dictionary):
        """Validate dictionary against class required properties

        Args:
            dictionary (dictionary): A dictionary representation of the object
            as obtained from the deserialization of the server's response. The
            keys MUST match property names in the API description.

        Returns:
            boolean : if dictionary is valid contains required properties.

        """
        if isinstance(dictionary, cls):
            return True

        if not isinstance(dictionary, dict):
            return False

        return True

    def __repr__(self):
        """Return a unambiguous string representation."""
        _redirect_endpoint=(
            self.redirect_endpoint
            if hasattr(self, "redirect_endpoint")
            else None
        )
        _mode=(
            self.mode
            if hasattr(self, "mode")
            else None
        )
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"redirect_endpoint={_redirect_endpoint!r}, "
            f"mode={_mode!r}, "
            f"additional_properties={_additional_properties!r}, "
            f")"
        )

    def __str__(self):
        """Return a human-readable string representation."""
        _redirect_endpoint=(
            self.redirect_endpoint
            if hasattr(self, "redirect_endpoint")
            else None
        )
        _mode=(
            self.mode
            if hasattr(self, "mode")
            else None
        )
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"redirect_endpoint={_redirect_endpoint!s}, "
            f"mode={_mode!s}, "
            f"additional_properties={_additional_properties!s}, "
            f")"
        )
