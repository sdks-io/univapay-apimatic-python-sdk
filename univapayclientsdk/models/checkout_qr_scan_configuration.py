"""univapay_client_sdk.

This file was automatically generated for Univapay by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

# ruff: noqa: E501
from univapayclientsdk.api_helper import APIHelper


class CheckoutQrScanConfiguration(object):
    """Implementation of the 'CheckoutQrScanConfiguration' model.

    QR-scan (CPM) payment settings applied to checkout.

    Attributes:
        enabled (bool): Whether QR-scan payments are enabled.
        forbidden_qr_scan_gateways (List[str]): QR-scan gateways disabled for the
            merchant. Common values include `alipay`, `alipay_plus`, `pay_pay`,
            `we_chat`, `univapay`, and `test`. `null` when no gateway is forbidden.
        additional_properties (Dict[str, Any]): The additional properties for the
            model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "enabled": "enabled",
        "forbidden_qr_scan_gateways": "forbidden_qr_scan_gateways",
    }

    _optionals = [
        "enabled",
        "forbidden_qr_scan_gateways",
    ]

    _nullables = [
        "forbidden_qr_scan_gateways",
    ]

    def __init__(
        self,
        enabled=APIHelper.SKIP,
        forbidden_qr_scan_gateways=APIHelper.SKIP,
        additional_properties=None):
        """Initialize a CheckoutQrScanConfiguration instance."""
        # Initialize members of the class
        if enabled is not APIHelper.SKIP:
            self.enabled = enabled
        if forbidden_qr_scan_gateways is not APIHelper.SKIP:
            self.forbidden_qr_scan_gateways = forbidden_qr_scan_gateways

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
        enabled =\
            dictionary.get("enabled")\
            if "enabled" in dictionary.keys()\
                else APIHelper.SKIP
        forbidden_qr_scan_gateways =\
            dictionary.get("forbidden_qr_scan_gateways")\
            if "forbidden_qr_scan_gateways" in dictionary.keys()\
                else APIHelper.SKIP

        additional_properties = APIHelper.get_additional_properties(
            dictionary={k: v for k, v in dictionary.items()
                        if k not in cls._names.values()},
            unboxing_function=lambda value: value)

        # Return an object of this model
        return cls(enabled,
                   forbidden_qr_scan_gateways,
                   additional_properties)

    def __repr__(self):
        """Return a unambiguous string representation."""
        _enabled=(
            self.enabled
            if hasattr(self, "enabled")
            else None
        )
        _forbidden_qr_scan_gateways=(
            self.forbidden_qr_scan_gateways
            if hasattr(self, "forbidden_qr_scan_gateways")
            else None
        )
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"enabled={_enabled!r}, "
            f"forbidden_qr_scan_gateways={_forbidden_qr_scan_gateways!r}, "
            f"additional_properties={_additional_properties!r}, "
            f")"
        )

    def __str__(self):
        """Return a human-readable string representation."""
        _enabled=(
            self.enabled
            if hasattr(self, "enabled")
            else None
        )
        _forbidden_qr_scan_gateways=(
            self.forbidden_qr_scan_gateways
            if hasattr(self, "forbidden_qr_scan_gateways")
            else None
        )
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"enabled={_enabled!s}, "
            f"forbidden_qr_scan_gateways={_forbidden_qr_scan_gateways!s}, "
            f"additional_properties={_additional_properties!s}, "
            f")"
        )
