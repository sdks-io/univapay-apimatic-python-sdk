"""univapay_client_sdk.

This file was automatically generated for Univapay by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

# ruff: noqa: E501
from univapayclientsdk.api_helper import APIHelper
from univapayclientsdk.models.generic_metadata import (
    GenericMetadata,
)


class CancelUpdateRequest(object):
    """Implementation of the 'CancelUpdateRequest' model.

    Request body for updating a cancel. Only `metadata` is settable by merchants. All
    fields are optional; omitted fields are left unchanged.

    Attributes:
        metadata (GenericMetadata): A free-form dictionary for custom metadata.
        additional_properties (Dict[str, Any]): The additional properties for the
            model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "metadata": "metadata",
    }

    _optionals = [
        "metadata",
    ]

    def __init__(
        self,
        metadata=APIHelper.SKIP,
        additional_properties=None):
        """Initialize a CancelUpdateRequest instance."""
        # Initialize members of the class
        if metadata is not APIHelper.SKIP:
            self.metadata = metadata

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
        metadata =\
            GenericMetadata.from_dictionary(
                dictionary.get("metadata"))\
                if "metadata" in dictionary.keys()\
                else APIHelper.SKIP

        additional_properties = APIHelper.get_additional_properties(
            dictionary={k: v for k, v in dictionary.items()
                        if k not in cls._names.values()},
            unboxing_function=lambda value: value)

        # Return an object of this model
        return cls(metadata,
                   additional_properties)

    def __repr__(self):
        """Return a unambiguous string representation."""
        _metadata=(
            self.metadata
            if hasattr(self, "metadata")
            else None
        )
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"metadata={_metadata!r}, "
            f"additional_properties={_additional_properties!r}, "
            f")"
        )

    def __str__(self):
        """Return a human-readable string representation."""
        _metadata=(
            self.metadata
            if hasattr(self, "metadata")
            else None
        )
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"metadata={_metadata!s}, "
            f"additional_properties={_additional_properties!s}, "
            f")"
        )
