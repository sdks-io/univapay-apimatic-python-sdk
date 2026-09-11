"""univapay_client_sdk.

This file was automatically generated for Univapay by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

# ruff: noqa: E501
from univapayclientsdk.api_helper import APIHelper


class TokenResponseQrScanData(object):
    """Implementation of the 'TokenResponseQrScanData' model.

    Token Response Qr Scan Data schema.

    Attributes:
        brand (str): QR-CPM brand detected from the scanned code (e.g. `pay_pay`,
            `we_chat`, `qq`, `line_pay`, `au_pay`, `alipay_china`). This is an open
            value set — new brands may appear without notice. Returned as `null` when
            the scanned code could not be parsed into a known brand.
        additional_properties (Dict[str, Any]): The additional properties for the
            model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "brand": "brand",
    }

    _nullables = [
        "brand",
    ]

    def __init__(
        self,
        brand=None,
        additional_properties=None):
        """Initialize a TokenResponseQrScanData instance."""
        # Initialize members of the class
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
        brand =\
            dictionary.get("brand")\
            if dictionary.get("brand")\
                else None

        additional_properties = APIHelper.get_additional_properties(
            dictionary={k: v for k, v in dictionary.items()
                        if k not in cls._names.values()},
            unboxing_function=lambda value: value)

        # Return an object of this model
        return cls(brand,
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
                    value=dictionary.brand,
                    type_callable=lambda value:
                        isinstance(
                        value,
                        str,
                ),
                    is_value_nullable=True)

        if not isinstance(dictionary, dict):
            return False

        return APIHelper.is_valid_type(
                value=dictionary.get("brand"),
                type_callable=lambda value:
                    isinstance(
                    value,
                    str,
            ),
                is_value_nullable=True)

    def __repr__(self):
        """Return a unambiguous string representation."""
        _brand=self.brand
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"brand={_brand!r}, "
            f"additional_properties={_additional_properties!r}, "
            f")"
        )

    def __str__(self):
        """Return a human-readable string representation."""
        _brand=self.brand
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"brand={_brand!s}, "
            f"additional_properties={_additional_properties!s}, "
            f")"
        )
