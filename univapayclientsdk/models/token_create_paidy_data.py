"""univapay_client_sdk.

This file was automatically generated for Univapay by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

# ruff: noqa: E501
from univapayclientsdk.api_helper import APIHelper
from univapayclientsdk.models.token_create_paidy_data_shipping_address import (
    TokenCreatePaidyDataShippingAddress,
)


class TokenCreatePaidyData(object):
    """Implementation of the 'TokenCreatePaidyData' model.

    Token Create Paidy Data schema.

    Attributes:
        paidy_token (str): One-time token issued by the Paidy SDK/widget on the
            client side.
        shipping_address (TokenCreatePaidyDataShippingAddress): Shipping address for
            a Paidy token. `zip` is required; the server additionally requires at
            least one of `line1`, `line2`, `city`, or `state` to be present (not
            enforceable at the schema level).
        phone_number (str): Consumer phone number in Japanese format (e.g.,
            '08012341234').
        additional_properties (Dict[str, Any]): The additional properties for the
            model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "paidy_token": "paidy_token",
        "shipping_address": "shipping_address",
        "phone_number": "phone_number",
    }

    _optionals = [
        "phone_number",
    ]

    def __init__(
        self,
        paidy_token=None,
        shipping_address=None,
        phone_number=APIHelper.SKIP,
        additional_properties=None):
        """Initialize a TokenCreatePaidyData instance."""
        # Initialize members of the class
        self.paidy_token = paidy_token
        self.shipping_address = shipping_address
        if phone_number is not APIHelper.SKIP:
            self.phone_number = phone_number

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
        shipping_address =\
            TokenCreatePaidyDataShippingAddress.from_dictionary(
                dictionary.get("shipping_address"))\
                if dictionary.get("shipping_address") else None
        phone_number =\
            dictionary.get("phone_number")\
            if dictionary.get("phone_number")\
                else APIHelper.SKIP

        additional_properties = APIHelper.get_additional_properties(
            dictionary={k: v for k, v in dictionary.items()
                        if k not in cls._names.values()},
            unboxing_function=lambda value: value)

        # Return an object of this model
        return cls(paidy_token,
                   shipping_address,
                   phone_number,
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
                )) \
                and APIHelper.is_valid_type(
                    value=dictionary.shipping_address,
                    type_callable=lambda value:
                        TokenCreatePaidyDataShippingAddress.validate(value),
                    is_model_dict=True)

        if not isinstance(dictionary, dict):
            return False

        return APIHelper.is_valid_type(
                value=dictionary.get("paidy_token"),
                type_callable=lambda value:
                    isinstance(
                    value,
                    str,
            )) \
            and APIHelper.is_valid_type(
                value=dictionary.get("shipping_address"),
                type_callable=lambda value:
                    TokenCreatePaidyDataShippingAddress.validate(value),
                is_model_dict=True)

    def __repr__(self):
        """Return a unambiguous string representation."""
        _paidy_token=self.paidy_token
        _shipping_address=self.shipping_address
        _phone_number=(
            self.phone_number
            if hasattr(self, "phone_number")
            else None
        )
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"paidy_token={_paidy_token!r}, "
            f"shipping_address={_shipping_address!r}, "
            f"phone_number={_phone_number!r}, "
            f"additional_properties={_additional_properties!r}, "
            f")"
        )

    def __str__(self):
        """Return a human-readable string representation."""
        _paidy_token=self.paidy_token
        _shipping_address=self.shipping_address
        _phone_number=(
            self.phone_number
            if hasattr(self, "phone_number")
            else None
        )
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"paidy_token={_paidy_token!s}, "
            f"shipping_address={_shipping_address!s}, "
            f"phone_number={_phone_number!s}, "
            f"additional_properties={_additional_properties!s}, "
            f")"
        )
