"""univapay_client_sdk.

This file was automatically generated for Univapay by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

# ruff: noqa: E501

class RefundReasonResponse(object):
    """Implementation of the 'RefundReasonResponse' enum.

    The reason for the refund as returned by the API. Includes operational reasons
    that merchants cannot set but may still observe on fetched refunds. `duplicate`:
    A duplicate charge was made. `fraud`: The charge is fraudulent.
    `customer_request`: The customer requested the refund. `system_failure`: An
    internal system failure triggered the refund. `chargeback`: A chargeback was
    raised. `chargeback_fee_exempt`: A fee-exempt chargeback. `chargeback_reverse`: A
    chargeback reversal.

    Attributes:
        DUPLICATE: The enum member of type str.
        FRAUD: The enum member of type str.
        CUSTOMER_REQUEST: The enum member of type str.
        SYSTEM_FAILURE: The enum member of type str.
        CHARGEBACK: The enum member of type str.
        CHARGEBACK_FEE_EXEMPT: The enum member of type str.
        CHARGEBACK_REVERSE: The enum member of type str.

    """

    _all_values = ["duplicate", "fraud", "customer_request", "system_failure",
        "chargeback", "chargeback_fee_exempt", "chargeback_reverse"]
    DUPLICATE = "duplicate"

    FRAUD = "fraud"

    CUSTOMER_REQUEST = "customer_request"

    SYSTEM_FAILURE = "system_failure"

    CHARGEBACK = "chargeback"

    CHARGEBACK_FEE_EXEMPT = "chargeback_fee_exempt"

    CHARGEBACK_REVERSE = "chargeback_reverse"

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
