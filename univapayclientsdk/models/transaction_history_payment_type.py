"""univapay_client_sdk.

This file was automatically generated for Univapay by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

# ruff: noqa: E501

class TransactionHistoryPaymentType(object):
    """Implementation of the 'TransactionHistoryPaymentType' enum.

    The payment method used for the underlying charge.

    Attributes:
        CARD: The enum member of type str.
        QR_SCAN: The enum member of type str.
        QR_MERCHANT: The enum member of type str.
        KONBINI: The enum member of type str.
        APPLE_PAY: The enum member of type str.
        PAIDY: The enum member of type str.
        ONLINE: The enum member of type str.
        BANK_TRANSFER: The enum member of type str.

    """

    CARD = "card"

    QR_SCAN = "qr_scan"

    QR_MERCHANT = "qr_merchant"

    KONBINI = "konbini"

    APPLE_PAY = "apple_pay"

    PAIDY = "paidy"

    ONLINE = "online"

    BANK_TRANSFER = "bank_transfer"

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
