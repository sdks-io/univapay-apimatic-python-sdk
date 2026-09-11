"""univapay_client_sdk.

This file was automatically generated for Univapay by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

# ruff: noqa: E501

class TransactionHistoryStatus(object):
    """Implementation of the 'TransactionHistoryStatus' enum.

    Status of the underlying resource. Charge rows use the full set of values; refund
    rows only ever report `pending`, `successful`, `failed`, or `error`.

    Attributes:
        PENDING: The enum member of type str.
        AUTHORIZED: The enum member of type str.
        SUCCESSFUL: The enum member of type str.
        FAILED: The enum member of type str.
        ERROR: The enum member of type str.
        CANCELED: The enum member of type str.
        AWAITING: The enum member of type str.

    """

    PENDING = "pending"

    AUTHORIZED = "authorized"

    SUCCESSFUL = "successful"

    FAILED = "failed"

    ERROR = "error"

    CANCELED = "canceled"

    AWAITING = "awaiting"

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
