"""univapay_client_sdk.

This file was automatically generated for Univapay by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

# ruff: noqa: E501
from univapayclientsdk.api_helper import APIHelper
from univapayclientsdk.models.token_response_paidy_data_shipping_address import (
    TokenResponsePaidyDataShippingAddress,
)


class TokenResponsePaidyData(object):
    """Implementation of the 'TokenResponsePaidyData' model.

    Token Response Paidy Data schema.

    Attributes:
        paidy_token (str): One-time token issued by the Paidy SDK/widget on the
            client side.
        phone_number (str): Consumer phone number in Japanese format.
        shipping_address (TokenResponsePaidyDataShippingAddress): Shipping address
            returned for a Paidy token.
        additional_properties (Dict[str, Any]): The additional properties for the
            model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "paidy_token": "paidy_token",
        "phone_number": "phone_number",
        "shipping_address": "shipping_address",
    }

    _optionals = [
        "phone_number",
        "shipping_address",
    ]

    _nullables = [
        "phone_number",
    ]

    def __init__(
        self,
        paidy_token=None,
        phone_number=APIHelper.SKIP,
        shipping_address=APIHelper.SKIP,
        additional_properties=None):
        """Initialize a TokenResponsePaidyData instance."""
        # Initialize members of the class
        self.paidy_token = paidy_token
        if phone_number is not APIHelper.SKIP:
            self.phone_number = phone_number
        if shipping_address is not APIHelper.SKIP:
            self.shipping_address = shipping_address

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
        paidy_token =\
            dictionary.get("paidy_token")\
            if dictionary.get("paidy_token")\
                else None
        phone_number =\
            dictionary.get("phone_number")\
            if "phone_number" in dictionary.keys()\
                else APIHelper.SKIP
        shipping_address =\
            TokenResponsePaidyDataShippingAddress.from_dictionary(
                dictionary.get("shipping_address"))\
                if "shipping_address" in dictionary.keys()\
                else APIHelper.SKIP

        additional_properties = APIHelper.get_additional_properties(
            dictionary={k: v for k, v in dictionary.items()
                        if k not in cls._names.values()},
            unboxing_function=lambda value: value)

        # Return an object of this model
        return cls(paidy_token,
                   phone_number,
                   shipping_address,
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
            return APIHelper.is_valid_type(
                    value=dictionary.paidy_token,
                    type_callable=lambda value:
                        isinstance(
                        value,
                        str,
                ))

        if not isinstance(dictionary, dict):
            return False

        return APIHelper.is_valid_type(
                value=dictionary.get("paidy_token"),
                type_callable=lambda value:
                    isinstance(
                    value,
                    str,
            ))

    def __repr__(self):
        """Return a unambiguous string representation."""
        _paidy_token=self.paidy_token
        _phone_number=(
            self.phone_number
            if hasattr(self, "phone_number")
            else None
        )
        _shipping_address=(
            self.shipping_address
            if hasattr(self, "shipping_address")
            else None
        )
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"paidy_token={_paidy_token!r}, "
            f"phone_number={_phone_number!r}, "
            f"shipping_address={_shipping_address!r}, "
            f"additional_properties={_additional_properties!r}, "
            f")"
        )

    def __str__(self):
        """Return a human-readable string representation."""
        _paidy_token=self.paidy_token
        _phone_number=(
            self.phone_number
            if hasattr(self, "phone_number")
            else None
        )
        _shipping_address=(
            self.shipping_address
            if hasattr(self, "shipping_address")
            else None
        )
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"paidy_token={_paidy_token!s}, "
            f"phone_number={_phone_number!s}, "
            f"shipping_address={_shipping_address!s}, "
            f"additional_properties={_additional_properties!s}, "
            f")"
        )
