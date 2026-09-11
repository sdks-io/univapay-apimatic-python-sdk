"""univapay_client_sdk.

This file was automatically generated for Univapay by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

# ruff: noqa: E501

class DirectDebitRegistrationOrigin(object):
    """Implementation of the 'DirectDebitRegistrationOrigin' enum.

    Where the bank account was registered from — `merchant_console` for the merchant
    dashboard, `anywhere` otherwise.

    Attributes:
        ANYWHERE: The enum member of type str.
        MERCHANT_CONSOLE: The enum member of type str.

    """

    ANYWHERE = "anywhere"

    MERCHANT_CONSOLE = "merchant_console"

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
