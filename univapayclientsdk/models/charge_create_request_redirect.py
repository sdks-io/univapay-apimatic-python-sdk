"""univapay_client_sdk.

This file was automatically generated for Univapay by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

# ruff: noqa: E501
from univapayclientsdk.api_helper import APIHelper


class ChargeCreateRequestRedirect(object):
    """Implementation of the 'ChargeCreateRequestRedirect' model.

    Charge Create Request Redirect schema.

    Attributes:
        endpoint (str): URL to redirect the customer to after payment completion.
        additional_properties (Dict[str, Any]): The additional properties for the
            model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "endpoint": "endpoint",
    }

    _optionals = [
        "endpoint",
    ]

    def __init__(
        self,
        endpoint=APIHelper.SKIP,
        additional_properties=None):
        """Initialize a ChargeCreateRequestRedirect instance."""
        # Initialize members of the class
        if endpoint is not APIHelper.SKIP:
            self.endpoint = endpoint

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
        endpoint =\
            dictionary.get("endpoint")\
            if dictionary.get("endpoint")\
                else APIHelper.SKIP

        additional_properties = APIHelper.get_additional_properties(
            dictionary={k: v for k, v in dictionary.items()
                        if k not in cls._names.values()},
            unboxing_function=lambda value: value)

        # Return an object of this model
        return cls(endpoint,
                   additional_properties)

    def __repr__(self):
        """Return a unambiguous string representation."""
        _endpoint=(
            self.endpoint
            if hasattr(self, "endpoint")
            else None
        )
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"endpoint={_endpoint!r}, "
            f"additional_properties={_additional_properties!r}, "
            f")"
        )

    def __str__(self):
        """Return a human-readable string representation."""
        _endpoint=(
            self.endpoint
            if hasattr(self, "endpoint")
            else None
        )
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"endpoint={_endpoint!s}, "
            f"additional_properties={_additional_properties!s}, "
            f")"
        )
