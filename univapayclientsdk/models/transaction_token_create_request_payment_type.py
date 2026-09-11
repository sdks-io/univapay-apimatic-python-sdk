"""univapay_client_sdk.

This file was automatically generated for Univapay by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

# ruff: noqa: E501

class TransactionTokenCreateRequestPaymentType(object):
    """Implementation of the 'TransactionTokenCreateRequestPaymentType' enum.

    Transaction Token Create Request Payment Type schema.

    Attributes:
        CARD: The enum member of type str.
        ONLINE: The enum member of type str.
        KONBINI: The enum member of type str.
        BANK_TRANSFER: The enum member of type str.
        QR_SCAN: The enum member of type str.
        QR_MERCHANT: The enum member of type str.
        PAIDY: The enum member of type str.

    """

    _all_values = ["card", "online", "konbini", "bank_transfer", "qr_scan", "qr_merchant",
        "paidy"]
    CARD = "card"

    ONLINE = "online"

    KONBINI = "konbini"

    BANK_TRANSFER = "bank_transfer"

    QR_SCAN = "qr_scan"

    QR_MERCHANT = "qr_merchant"

    PAIDY = "paidy"

    @classmethod
    def validate(cls, value):
        """Validate value contains in enum

        Args:
            value: the value to be validated

        Returns:
            boolean : if value is valid enum values.

        """
        return value in cls._all_values

    @classmethod
    def from_value(cls, value, default=None):
        """Return the matching enum value for the given input."""
        if value is None:
            return default

        # If numeric and matches directly
        if isinstance(value, int):
            for name, val in cls.__dict__.items():
                if not name.startswith("_") and val == value:
                    return val

        # If string, perform case-insensitive match
        if isinstance(value, str):
            value_lower = value.lower()
            for name, val in cls.__dict__.items():
                if not name.startswith("_") and (
                    name.lower() == value_lower or str(val).lower() == value_lower
                ):
                    return val

        # Fallback to default
        return default
