"""univapay_client_sdk.

This file was automatically generated for Univapay by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

# ruff: noqa: E501
from univapayclientsdk.api_helper import APIHelper


class TransactionTokenCreateRequestMetadata(object):
    """Implementation of the 'TransactionTokenCreateRequestMetadata' model.

    A free-form dictionary for custom metadata.

    Attributes:
        univapay_reference_id (str): Any arbitrary value (Free format).
        univapay_customer_id (uuid|str): Customer ID.
        univapay_name (str): Consumer name passed to payment processors that require
            it (e.g., konbini, bank transfer).
        univapay_phone_number (str): Consumer phone number passed to payment
            processors that require it.
        additional_properties (Dict[str, str | bool | float]): Transaction Token
            Create Metadata Props schema.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "univapay_reference_id": "univapay-reference-id",
        "univapay_customer_id": "univapay-customer-id",
        "univapay_name": "univapay-name",
        "univapay_phone_number": "univapay-phone-number",
    }

    _optionals = [
        "univapay_reference_id",
        "univapay_customer_id",
        "univapay_name",
        "univapay_phone_number",
    ]

    def __init__(
        self,
        univapay_reference_id=APIHelper.SKIP,
        univapay_customer_id=APIHelper.SKIP,
        univapay_name=APIHelper.SKIP,
        univapay_phone_number=APIHelper.SKIP,
        additional_properties=None):
        """Initialize a TransactionTokenCreateRequestMetadata instance."""
        # Initialize members of the class
        if univapay_reference_id is not APIHelper.SKIP:
            self.univapay_reference_id = univapay_reference_id
        if univapay_customer_id is not APIHelper.SKIP:
            self.univapay_customer_id = univapay_customer_id
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
        univapay_reference_id =\
            dictionary.get("univapay-reference-id")\
            if dictionary.get("univapay-reference-id")\
                else APIHelper.SKIP
        univapay_customer_id =\
            dictionary.get("univapay-customer-id")\
            if dictionary.get("univapay-customer-id")\
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
                UnionTypeLookUp.get("TransactionTokenCreateMetadataProps"), value, False))

        # Return an object of this model
        return cls(univapay_reference_id,
                   univapay_customer_id,
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
        _univapay_reference_id=(
            self.univapay_reference_id
            if hasattr(self, "univapay_reference_id")
            else None
        )
        _univapay_customer_id=(
            self.univapay_customer_id
            if hasattr(self, "univapay_customer_id")
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
            f"univapay_reference_id={_univapay_reference_id!r}, "
            f"univapay_customer_id={_univapay_customer_id!r}, "
            f"univapay_name={_univapay_name!r}, "
            f"univapay_phone_number={_univapay_phone_number!r}, "
            f"additional_properties={_additional_properties!r}, "
            f")"
        )

    def __str__(self):
        """Return a human-readable string representation."""
        _univapay_reference_id=(
            self.univapay_reference_id
            if hasattr(self, "univapay_reference_id")
            else None
        )
        _univapay_customer_id=(
            self.univapay_customer_id
            if hasattr(self, "univapay_customer_id")
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
            f"univapay_reference_id={_univapay_reference_id!s}, "
            f"univapay_customer_id={_univapay_customer_id!s}, "
            f"univapay_name={_univapay_name!s}, "
            f"univapay_phone_number={_univapay_phone_number!s}, "
            f"additional_properties={_additional_properties!s}, "
            f")"
        )
