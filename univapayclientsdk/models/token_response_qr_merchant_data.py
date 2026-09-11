"""univapay_client_sdk.

This file was automatically generated for Univapay by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

# ruff: noqa: E501
from univapayclientsdk.api_helper import APIHelper


class TokenResponseQrMerchantData(object):
    """Implementation of the 'TokenResponseQrMerchantData' model.

    Token Response Qr Merchant Data schema.

    Attributes:
        qr_image_url (str): QR code payload to be rendered by the consumer (content
            varies by brand — may be a URL or an opaque code). Some brands return an
            image URL; others (e.g. convenience-store QR brands) return an opaque
            numeric code with no URL structure. Populated asynchronously shortly
            after token/charge creation — `null` until then.
        brand (str): The QR-MPM brand this code was generated for.
        additional_properties (Dict[str, Any]): The additional properties for the
            model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "qr_image_url": "qr_image_url",
        "brand": "brand",
    }

    _optionals = [
        "brand",
    ]

    _nullables = [
        "qr_image_url",
        "brand",
    ]

    def __init__(
        self,
        qr_image_url=None,
        brand=APIHelper.SKIP,
        additional_properties=None):
        """Initialize a TokenResponseQrMerchantData instance."""
        # Initialize members of the class
        self.qr_image_url = qr_image_url
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
        qr_image_url =\
            dictionary.get("qr_image_url")\
            if dictionary.get("qr_image_url")\
                else None
        brand =\
            dictionary.get("brand")\
            if "brand" in dictionary.keys()\
                else APIHelper.SKIP

        additional_properties = APIHelper.get_additional_properties(
            dictionary={k: v for k, v in dictionary.items()
                        if k not in cls._names.values()},
            unboxing_function=lambda value: value)

        # Return an object of this model
        return cls(qr_image_url,
                   brand,
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
                    value=dictionary.qr_image_url,
                    type_callable=lambda value:
                        isinstance(
                        value,
                        str,
                ),
                    is_value_nullable=True)

        if not isinstance(dictionary, dict):
            return False

        return APIHelper.is_valid_type(
                value=dictionary.get("qr_image_url"),
                type_callable=lambda value:
                    isinstance(
                    value,
                    str,
            ),
                is_value_nullable=True)

    def __repr__(self):
        """Return a unambiguous string representation."""
        _qr_image_url=self.qr_image_url
        _brand=(
            self.brand
            if hasattr(self, "brand")
            else None
        )
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"qr_image_url={_qr_image_url!r}, "
            f"brand={_brand!r}, "
            f"additional_properties={_additional_properties!r}, "
            f")"
        )

    def __str__(self):
        """Return a human-readable string representation."""
        _qr_image_url=self.qr_image_url
        _brand=(
            self.brand
            if hasattr(self, "brand")
            else None
        )
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"qr_image_url={_qr_image_url!s}, "
            f"brand={_brand!s}, "
            f"additional_properties={_additional_properties!s}, "
            f")"
        )
