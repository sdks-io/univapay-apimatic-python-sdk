"""univapay_client_sdk.

This file was automatically generated for Univapay by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

# ruff: noqa: E501
from univapayclientsdk.api_helper import APIHelper


class TokenCreateQrScanData(object):
    """Implementation of the 'TokenCreateQrScanData' model.

    Token Create Qr Scan Data schema.

    Attributes:
        scanned_qr (str): The QR/barcode payload scanned from the customer's payment
            app (Customer-Presented Mode). Only valid when `type` is `one_time` — the
            server rejects `subscription`/`recurring` token types for this payment
            type.
        additional_properties (Dict[str, Any]): The additional properties for the
            model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "scanned_qr": "scanned_qr",
    }

    def __init__(
        self,
        scanned_qr=None,
        additional_properties=None):
        """Initialize a TokenCreateQrScanData instance."""
        # Initialize members of the class
        self.scanned_qr = scanned_qr

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
        scanned_qr =\
            dictionary.get("scanned_qr")\
            if dictionary.get("scanned_qr")\
                else None

        additional_properties = APIHelper.get_additional_properties(
            dictionary={k: v for k, v in dictionary.items()
                        if k not in cls._names.values()},
            unboxing_function=lambda value: value)

        # Return an object of this model
        return cls(scanned_qr,
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
                    value=dictionary.scanned_qr,
                    type_callable=lambda value:
                        isinstance(
                        value,
                        str,
                ))

        if not isinstance(dictionary, dict):
            return False

        return APIHelper.is_valid_type(
                value=dictionary.get("scanned_qr"),
                type_callable=lambda value:
                    isinstance(
                    value,
                    str,
            ))

    def __repr__(self):
        """Return a unambiguous string representation."""
        _scanned_qr=self.scanned_qr
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"scanned_qr={_scanned_qr!r}, "
            f"additional_properties={_additional_properties!r}, "
            f")"
        )

    def __str__(self):
        """Return a human-readable string representation."""
        _scanned_qr=self.scanned_qr
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"scanned_qr={_scanned_qr!s}, "
            f"additional_properties={_additional_properties!s}, "
            f")"
        )
