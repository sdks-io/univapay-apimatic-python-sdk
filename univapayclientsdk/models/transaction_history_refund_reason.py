"""univapay_client_sdk.

This file was automatically generated for Univapay by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

# ruff: noqa: E501

class TransactionHistoryRefundReason(object):
    """Implementation of the 'TransactionHistoryRefundReason' enum.

    Reason code for a refund.

    Attributes:
        DUPLICATE: The enum member of type str.
        FRAUD: The enum member of type str.
        CUSTOMER_REQUEST: The enum member of type str.
        SYSTEM_FAILURE: The enum member of type str.
        CHARGEBACK: The enum member of type str.
        CHARGEBACK_FEE_EXEMPT: The enum member of type str.
        CHARGEBACK_REVERSE: The enum member of type str.

    """

    DUPLICATE = "duplicate"

    FRAUD = "fraud"

    CUSTOMER_REQUEST = "customer_request"

    SYSTEM_FAILURE = "system_failure"

    CHARGEBACK = "chargeback"

    CHARGEBACK_FEE_EXEMPT = "chargeback_fee_exempt"

    CHARGEBACK_REVERSE = "chargeback_reverse"

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
