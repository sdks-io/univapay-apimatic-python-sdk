"""univapay_client_sdk.

This file was automatically generated for Univapay by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

# ruff: noqa: E501
from univapayclientsdk.api_helper import APIHelper
from univapayclientsdk.models.refund import (
    Refund,
)


class RefundWebhookCallbackExtension(object):
    """Implementation of the 'RefundWebhookCallbackExtension' model.

    Refund-specific webhook payload extension.

    Attributes:
        data (Refund): Represents a refund issued against a charge.
        additional_properties (Dict[str, Any]): The additional properties for the
            model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "data": "data",
    }

    _optionals = [
        "data",
    ]

    def __init__(
        self,
        data=APIHelper.SKIP,
        additional_properties=None):
        """Initialize a RefundWebhookCallbackExtension instance."""
        # Initialize members of the class
        if data is not APIHelper.SKIP:
            self.data = data

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
        data =\
            Refund.from_dictionary(
                dictionary.get("data"))\
                if "data" in dictionary.keys()\
                else APIHelper.SKIP

        additional_properties = APIHelper.get_additional_properties(
            dictionary={k: v for k, v in dictionary.items()
                        if k not in cls._names.values()},
            unboxing_function=lambda value: value)

        # Return an object of this model
        return cls(data,
                   additional_properties)

    def __repr__(self):
        """Return a unambiguous string representation."""
        _data=(
            self.data
            if hasattr(self, "data")
            else None
        )
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"data={_data!r}, "
            f"additional_properties={_additional_properties!r}, "
            f")"
        )

    def __str__(self):
        """Return a human-readable string representation."""
        _data=(
            self.data
            if hasattr(self, "data")
            else None
        )
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"data={_data!s}, "
            f"additional_properties={_additional_properties!s}, "
            f")"
        )
