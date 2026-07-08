"""univapay_client_sdk.

This file was automatically generated for Univapay by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

# ruff: noqa: E501
from univapayclientsdk.api_helper import APIHelper
from univapayclientsdk.models.generic_metadata import (
    GenericMetadata,
)
from univapayclientsdk.models.transaction_token_update_request_data import (
    TransactionTokenUpdateRequestData,
)


class TransactionTokenUpdateRequest(object):
    """Implementation of the 'TransactionTokenUpdateRequest' model.

    Request payload for updating a transaction token.

    Attributes:
        email (str): Customer email address.
        metadata (GenericMetadata): A free-form dictionary for custom metadata.
        data (TransactionTokenUpdateRequestData): Transaction Token Update Request
            Data schema.
        additional_properties (Dict[str, Any]): The additional properties for the
            model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "email": "email",
        "metadata": "metadata",
        "data": "data",
    }

    _optionals = [
        "email",
        "metadata",
        "data",
    ]

    def __init__(
        self,
        email=APIHelper.SKIP,
        metadata=APIHelper.SKIP,
        data=APIHelper.SKIP,
        additional_properties=None):
        """Initialize a TransactionTokenUpdateRequest instance."""
        # Initialize members of the class
        if email is not APIHelper.SKIP:
            self.email = email
        if metadata is not APIHelper.SKIP:
            self.metadata = metadata
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
        email =\
            dictionary.get("email")\
            if dictionary.get("email")\
                else APIHelper.SKIP
        metadata =\
            GenericMetadata.from_dictionary(
                dictionary.get("metadata"))\
                if "metadata" in dictionary.keys()\
                else APIHelper.SKIP
        data =\
            TransactionTokenUpdateRequestData.from_dictionary(
                dictionary.get("data"))\
                if "data" in dictionary.keys()\
                else APIHelper.SKIP

        additional_properties = APIHelper.get_additional_properties(
            dictionary={k: v for k, v in dictionary.items()
                        if k not in cls._names.values()},
            unboxing_function=lambda value: value)

        # Return an object of this model
        return cls(email,
                   metadata,
                   data,
                   additional_properties)

    def __repr__(self):
        """Return a unambiguous string representation."""
        _email=(
            self.email
            if hasattr(self, "email")
            else None
        )
        _metadata=(
            self.metadata
            if hasattr(self, "metadata")
            else None
        )
        _data=(
            self.data
            if hasattr(self, "data")
            else None
        )
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"email={_email!r}, "
            f"metadata={_metadata!r}, "
            f"data={_data!r}, "
            f"additional_properties={_additional_properties!r}, "
            f")"
        )

    def __str__(self):
        """Return a human-readable string representation."""
        _email=(
            self.email
            if hasattr(self, "email")
            else None
        )
        _metadata=(
            self.metadata
            if hasattr(self, "metadata")
            else None
        )
        _data=(
            self.data
            if hasattr(self, "data")
            else None
        )
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"email={_email!s}, "
            f"metadata={_metadata!s}, "
            f"data={_data!s}, "
            f"additional_properties={_additional_properties!s}, "
            f")"
        )
