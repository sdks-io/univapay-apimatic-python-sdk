"""univapay_client_sdk.

This file was automatically generated for Univapay by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

# ruff: noqa: E501

class DirectDebitBankAccountType(object):
    """Implementation of the 'DirectDebitBankAccountType' enum.

    Deposit account type (預金種類) — `regular` (普通), `current` (当座), `savings` (貯蓄) or
    `others` (その他).

    Attributes:
        REGULAR: The enum member of type str.
        CURRENT: The enum member of type str.
        SAVINGS: The enum member of type str.
        OTHERS: The enum member of type str.

    """

    REGULAR = "regular"

    CURRENT = "current"

    SAVINGS = "savings"

    OTHERS = "others"

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
