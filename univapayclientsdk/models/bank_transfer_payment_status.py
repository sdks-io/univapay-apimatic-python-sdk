"""univapay_client_sdk.

This file was automatically generated for Univapay by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

# ruff: noqa: E501

class BankTransferPaymentStatus(object):
    """Implementation of the 'BankTransferPaymentStatus' enum.

    Payment status of a bank transfer charge.

    Attributes:
        UNPAID: The enum member of type str.
        INSUFFICIENT: The enum member of type str.
        EXACT: The enum member of type str.
        EXCEEDED: The enum member of type str.

    """

    _all_values = ["unpaid", "insufficient", "exact", "exceeded"]
    UNPAID = "unpaid"

    INSUFFICIENT = "insufficient"

    EXACT = "exact"

    EXCEEDED = "exceeded"

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
