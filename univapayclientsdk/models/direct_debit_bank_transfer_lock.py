"""univapay_client_sdk.

This file was automatically generated for Univapay by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

# ruff: noqa: E501

class DirectDebitBankTransferLock(object):
    """Implementation of the 'DirectDebitBankTransferLock' enum.

    Whether the transfer can still be edited. Transfers are `unlocked` until the
    upload deadline for their debit cycle passes, after which they are `locked` and
    can no longer be changed or deleted.

    Attributes:
        UNLOCKED: The enum member of type str.
        LOCKED: The enum member of type str.

    """

    UNLOCKED = "unlocked"

    LOCKED = "locked"

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
