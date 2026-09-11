"""univapay_client_sdk.

This file was automatically generated for Univapay by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

# ruff: noqa: E501
from univapayclientsdk.api_helper import APIHelper


class EnableTokenThreeDsRequest(object):
    """Implementation of the 'EnableTokenThreeDsRequest' model.

    Request payload for enabling 3DS on a recurring token. Both the body and
    `redirect_endpoint` are optional.

    Attributes:
        redirect_endpoint (str): URL to redirect the customer to after 3DS
            authentication.
        additional_properties (Dict[str, Any]): The additional properties for the
            model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "redirect_endpoint": "redirect_endpoint",
    }

    _optionals = [
        "redirect_endpoint",
    ]

    def __init__(
        self,
        redirect_endpoint=APIHelper.SKIP,
        additional_properties=None):
        """Initialize a EnableTokenThreeDsRequest instance."""
        # Initialize members of the class
        if redirect_endpoint is not APIHelper.SKIP:
            self.redirect_endpoint = redirect_endpoint

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

        additional_properties = APIHelper.get_additional_properties(
            dictionary={k: v for k, v in dictionary.items()
                        if k not in cls._names.values()},
            unboxing_function=lambda value: value)

        # Return an object of this model
        return cls(redirect_endpoint,
                   additional_properties)

    def __repr__(self):
        """Return a unambiguous string representation."""
        _redirect_endpoint=(
            self.redirect_endpoint
            if hasattr(self, "redirect_endpoint")
            else None
        )
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"redirect_endpoint={_redirect_endpoint!r}, "
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
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"redirect_endpoint={_redirect_endpoint!s}, "
            f"additional_properties={_additional_properties!s}, "
            f")"
        )
