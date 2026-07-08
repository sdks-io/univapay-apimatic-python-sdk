"""univapay_client_sdk.

This file was automatically generated for Univapay by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

# ruff: noqa: E501
from univapayclientsdk.api_helper import APIHelper
from univapayclientsdk.models.cancel import (
    Cancel,
)


class CancelList(object):
    """Implementation of the 'CancelList' model.

    Paginated list of cancels.

    Attributes:
        items (List[Cancel]): List of resources.
        has_more (bool): Whether more results are available.
        additional_properties (Dict[str, Any]): The additional properties for the
            model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "items": "items",
        "has_more": "has_more",
    }

    _optionals = [
        "items",
        "has_more",
    ]

    def __init__(
        self,
        items=APIHelper.SKIP,
        has_more=APIHelper.SKIP,
        additional_properties=None):
        """Initialize a CancelList instance."""
        # Initialize members of the class
        if items is not APIHelper.SKIP:
            self.items = items
        if has_more is not APIHelper.SKIP:
            self.has_more = has_more

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
        items = None
        if dictionary.get("items") is not None:
            items = [
                Cancel.from_dictionary(x)
                    for x in dictionary.get("items")
            ]
        else:
            items = APIHelper.SKIP
        has_more =\
            dictionary.get("has_more")\
            if "has_more" in dictionary.keys()\
                else APIHelper.SKIP

        additional_properties = APIHelper.get_additional_properties(
            dictionary={k: v for k, v in dictionary.items()
                        if k not in cls._names.values()},
            unboxing_function=lambda value: value)

        # Return an object of this model
        return cls(items,
                   has_more,
                   additional_properties)

    def __repr__(self):
        """Return a unambiguous string representation."""
        _items=(
            self.items
            if hasattr(self, "items")
            else None
        )
        _has_more=(
            self.has_more
            if hasattr(self, "has_more")
            else None
        )
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"items={_items!r}, "
            f"has_more={_has_more!r}, "
            f"additional_properties={_additional_properties!r}, "
            f")"
        )

    def __str__(self):
        """Return a human-readable string representation."""
        _items=(
            self.items
            if hasattr(self, "items")
            else None
        )
        _has_more=(
            self.has_more
            if hasattr(self, "has_more")
            else None
        )
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"items={_items!s}, "
            f"has_more={_has_more!s}, "
            f"additional_properties={_additional_properties!s}, "
            f")"
        )
