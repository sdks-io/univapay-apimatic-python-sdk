"""univapay_client_sdk.

This file was automatically generated for Univapay by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

# ruff: noqa: E501
from univapayclientsdk.api_helper import APIHelper


class ChargeRedirect(object):
    """Implementation of the 'ChargeRedirect' model.

    Charge Redirect schema.

    Attributes:
        endpoint (str): Endpoint value.
        redirect_id (uuid|str): Redirect identifier.
        additional_properties (Dict[str, Any]): The additional properties for the
            model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "endpoint": "endpoint",
        "redirect_id": "redirect_id",
    }

    _optionals = [
        "endpoint",
        "redirect_id",
    ]

    def __init__(
        self,
        endpoint=APIHelper.SKIP,
        redirect_id=APIHelper.SKIP,
        additional_properties=None):
        """Initialize a ChargeRedirect instance."""
        # Initialize members of the class
        if endpoint is not APIHelper.SKIP:
            self.endpoint = endpoint
        if redirect_id is not APIHelper.SKIP:
            self.redirect_id = redirect_id

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
        redirect_id =\
            dictionary.get("redirect_id")\
            if dictionary.get("redirect_id")\
                else APIHelper.SKIP

        additional_properties = APIHelper.get_additional_properties(
            dictionary={k: v for k, v in dictionary.items()
                        if k not in cls._names.values()},
            unboxing_function=lambda value: value)

        # Return an object of this model
        return cls(endpoint,
                   redirect_id,
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
        _endpoint=(
            self.endpoint
            if hasattr(self, "endpoint")
            else None
        )
        _redirect_id=(
            self.redirect_id
            if hasattr(self, "redirect_id")
            else None
        )
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"endpoint={_endpoint!r}, "
            f"redirect_id={_redirect_id!r}, "
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
        _redirect_id=(
            self.redirect_id
            if hasattr(self, "redirect_id")
            else None
        )
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"endpoint={_endpoint!s}, "
            f"redirect_id={_redirect_id!s}, "
            f"additional_properties={_additional_properties!s}, "
            f")"
        )
