"""univapay_client_sdk.

This file was automatically generated for Univapay by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

# ruff: noqa: E501
from univapayclientsdk.api_helper import APIHelper


class GenericMetadata(object):
    """Implementation of the 'GenericMetadata' model.

    A free-form dictionary for custom metadata.

    Attributes:
        order_id (str): Example of a custom metadata key.
        univapay_name (str): Consumer name passed to payment processors that require
            it (e.g., konbini, bank transfer).
        univapay_phone_number (str): Consumer phone number passed to payment
            processors that require it.
        additional_properties (Dict[str, str | None | int | float | bool | List[str |
            bool]]): Allowed values for metadata properties. Values may be a string,
            number, boolean, null, or an array of any of the above — but not a nested
            object; the server rejects metadata whose direct property values are JSON
            objects.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "order_id": "order_id",
        "univapay_name": "univapay-name",
        "univapay_phone_number": "univapay-phone-number",
    }

    _optionals = [
        "order_id",
        "univapay_name",
        "univapay_phone_number",
    ]

    def __init__(
        self,
        order_id=APIHelper.SKIP,
        univapay_name=APIHelper.SKIP,
        univapay_phone_number=APIHelper.SKIP,
        additional_properties=None):
        """Initialize a GenericMetadata instance."""
        # Initialize members of the class
        if order_id is not APIHelper.SKIP:
            self.order_id = order_id
        if univapay_name is not APIHelper.SKIP:
            self.univapay_name = univapay_name
        if univapay_phone_number is not APIHelper.SKIP:
            self.univapay_phone_number = univapay_phone_number

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
        from univapayclientsdk.utilities.union_type_lookup import (
            UnionTypeLookUp,
        )

        if not isinstance(dictionary, dict) or dictionary is None:
            return None

        # Extract variables from the dictionary
        order_id =\
            dictionary.get("order_id")\
            if dictionary.get("order_id")\
                else APIHelper.SKIP
        univapay_name =\
            dictionary.get("univapay-name")\
            if dictionary.get("univapay-name")\
                else APIHelper.SKIP
        univapay_phone_number =\
            dictionary.get("univapay-phone-number")\
            if dictionary.get("univapay-phone-number")\
                else APIHelper.SKIP

        additional_properties = APIHelper.get_additional_properties(
            dictionary={k: v for k, v in dictionary.items()
                        if k not in cls._names.values()},
            unboxing_function=lambda value: APIHelper.deserialize_union_type(
                UnionTypeLookUp.get("GenericMetadataValue"), value, False))

        # Return an object of this model
        return cls(order_id,
                   univapay_name,
                   univapay_phone_number,
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
        _order_id=(
            self.order_id
            if hasattr(self, "order_id")
            else None
        )
        _univapay_name=(
            self.univapay_name
            if hasattr(self, "univapay_name")
            else None
        )
        _univapay_phone_number=(
            self.univapay_phone_number
            if hasattr(self, "univapay_phone_number")
            else None
        )
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"order_id={_order_id!r}, "
            f"univapay_name={_univapay_name!r}, "
            f"univapay_phone_number={_univapay_phone_number!r}, "
            f"additional_properties={_additional_properties!r}, "
            f")"
        )

    def __str__(self):
        """Return a human-readable string representation."""
        _order_id=(
            self.order_id
            if hasattr(self, "order_id")
            else None
        )
        _univapay_name=(
            self.univapay_name
            if hasattr(self, "univapay_name")
            else None
        )
        _univapay_phone_number=(
            self.univapay_phone_number
            if hasattr(self, "univapay_phone_number")
            else None
        )
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"order_id={_order_id!s}, "
            f"univapay_name={_univapay_name!s}, "
            f"univapay_phone_number={_univapay_phone_number!s}, "
            f"additional_properties={_additional_properties!s}, "
            f")"
        )
