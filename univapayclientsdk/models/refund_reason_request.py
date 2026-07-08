"""univapay_client_sdk.

This file was automatically generated for Univapay by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

# ruff: noqa: E501

class RefundReasonRequest(object):
    """Implementation of the 'RefundReasonRequest' enum.

    The reason for the refund (merchant-settable values). `duplicate`: A duplicate
    charge was made. `fraud`: The charge is fraudulent. `customer_request`: The
    customer requested the refund.

    Attributes:
        DUPLICATE: The enum member of type str.
        FRAUD: The enum member of type str.
        CUSTOMER_REQUEST: The enum member of type str.

    """

    DUPLICATE = "duplicate"

    FRAUD = "fraud"

    CUSTOMER_REQUEST = "customer_request"

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
