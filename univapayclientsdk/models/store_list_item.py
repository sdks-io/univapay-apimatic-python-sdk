"""univapay_client_sdk.

This file was automatically generated for Univapay by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

# ruff: noqa: E501
from univapayclientsdk.api_helper import APIHelper


class StoreListItem(object):
    """Implementation of the 'StoreListItem' model.

    Store row returned by store list queries.

    Attributes:
        id (uuid|str): Store identifier.
        name (str): Store display name.
        merchant_name (str): Merchant display name associated with the store row.
        created_on (datetime): Timestamp when the store was created.
        additional_properties (Dict[str, Any]): The additional properties for the
            model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "id": "id",
        "name": "name",
        "merchant_name": "merchant_name",
        "created_on": "created_on",
    }

    _optionals = [
        "id",
        "name",
        "merchant_name",
        "created_on",
    ]

    def __init__(
        self,
        id=APIHelper.SKIP,
        name=APIHelper.SKIP,
        merchant_name=APIHelper.SKIP,
        created_on=APIHelper.SKIP,
        additional_properties=None):
        """Initialize a StoreListItem instance."""
        # Initialize members of the class
        if id is not APIHelper.SKIP:
            self.id = id
        if name is not APIHelper.SKIP:
            self.name = name
        if merchant_name is not APIHelper.SKIP:
            self.merchant_name = merchant_name
        if created_on is not APIHelper.SKIP:
            self.created_on =\
                 APIHelper.apply_datetime_converter(
                created_on, APIHelper.RFC3339DateTime)\
                 if created_on else None

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
        id =\
            dictionary.get("id")\
            if dictionary.get("id")\
                else APIHelper.SKIP
        name =\
            dictionary.get("name")\
            if dictionary.get("name")\
                else APIHelper.SKIP
        merchant_name =\
            dictionary.get("merchant_name")\
            if dictionary.get("merchant_name")\
                else APIHelper.SKIP
        created_on = APIHelper.RFC3339DateTime.from_value(
            dictionary.get("created_on")).datetime\
            if dictionary.get("created_on") else APIHelper.SKIP

        additional_properties = APIHelper.get_additional_properties(
            dictionary={k: v for k, v in dictionary.items()
                        if k not in cls._names.values()},
            unboxing_function=lambda value: value)

        # Return an object of this model
        return cls(id,
                   name,
                   merchant_name,
                   created_on,
                   additional_properties)

    def __repr__(self):
        """Return a unambiguous string representation."""
        _id=(
            self.id
            if hasattr(self, "id")
            else None
        )
        _name=(
            self.name
            if hasattr(self, "name")
            else None
        )
        _merchant_name=(
            self.merchant_name
            if hasattr(self, "merchant_name")
            else None
        )
        _created_on=(
            self.created_on
            if hasattr(self, "created_on")
            else None
        )
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"id={_id!r}, "
            f"name={_name!r}, "
            f"merchant_name={_merchant_name!r}, "
            f"created_on={_created_on!r}, "
            f"additional_properties={_additional_properties!r}, "
            f")"
        )

    def __str__(self):
        """Return a human-readable string representation."""
        _id=(
            self.id
            if hasattr(self, "id")
            else None
        )
        _name=(
            self.name
            if hasattr(self, "name")
            else None
        )
        _merchant_name=(
            self.merchant_name
            if hasattr(self, "merchant_name")
            else None
        )
        _created_on=(
            self.created_on
            if hasattr(self, "created_on")
            else None
        )
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"id={_id!s}, "
            f"name={_name!s}, "
            f"merchant_name={_merchant_name!s}, "
            f"created_on={_created_on!s}, "
            f"additional_properties={_additional_properties!s}, "
            f")"
        )
