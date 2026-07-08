"""univapay_client_sdk.

This file was automatically generated for Univapay by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

# ruff: noqa: E501
from univapayclientsdk.api_helper import APIHelper


class TransactionTokenListItemUserData(object):
    """Implementation of the 'TransactionTokenListItemUserData' model.

    Transaction Token List Item User Data schema.

    Attributes:
        cardholder_name (str): Cardholder name value.
        email (str): Customer email address.
        brand (str): Brand or network name.
        additional_properties (Dict[str, Any]): The additional properties for the
            model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "cardholder_name": "cardholder_name",
        "email": "email",
        "brand": "brand",
    }

    _optionals = [
        "cardholder_name",
        "email",
        "brand",
    ]

    def __init__(
        self,
        cardholder_name=APIHelper.SKIP,
        email=APIHelper.SKIP,
        brand=APIHelper.SKIP,
        additional_properties=None):
        """Initialize a TransactionTokenListItemUserData instance."""
        # Initialize members of the class
        if cardholder_name is not APIHelper.SKIP:
            self.cardholder_name = cardholder_name
        if email is not APIHelper.SKIP:
            self.email = email
        if brand is not APIHelper.SKIP:
            self.brand = brand

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
        cardholder_name =\
            dictionary.get("cardholder_name")\
            if dictionary.get("cardholder_name")\
                else APIHelper.SKIP
        email =\
            dictionary.get("email")\
            if dictionary.get("email")\
                else APIHelper.SKIP
        brand =\
            dictionary.get("brand")\
            if dictionary.get("brand")\
                else APIHelper.SKIP

        additional_properties = APIHelper.get_additional_properties(
            dictionary={k: v for k, v in dictionary.items()
                        if k not in cls._names.values()},
            unboxing_function=lambda value: value)

        # Return an object of this model
        return cls(cardholder_name,
                   email,
                   brand,
                   additional_properties)

    def __repr__(self):
        """Return a unambiguous string representation."""
        _cardholder_name=(
            self.cardholder_name
            if hasattr(self, "cardholder_name")
            else None
        )
        _email=(
            self.email
            if hasattr(self, "email")
            else None
        )
        _brand=(
            self.brand
            if hasattr(self, "brand")
            else None
        )
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"cardholder_name={_cardholder_name!r}, "
            f"email={_email!r}, "
            f"brand={_brand!r}, "
            f"additional_properties={_additional_properties!r}, "
            f")"
        )

    def __str__(self):
        """Return a human-readable string representation."""
        _cardholder_name=(
            self.cardholder_name
            if hasattr(self, "cardholder_name")
            else None
        )
        _email=(
            self.email
            if hasattr(self, "email")
            else None
        )
        _brand=(
            self.brand
            if hasattr(self, "brand")
            else None
        )
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"cardholder_name={_cardholder_name!s}, "
            f"email={_email!s}, "
            f"brand={_brand!s}, "
            f"additional_properties={_additional_properties!s}, "
            f")"
        )
