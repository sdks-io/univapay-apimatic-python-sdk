"""univapay_client_sdk.

This file was automatically generated for Univapay by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

# ruff: noqa: E501

class CheckoutMode(object):
    """Implementation of the 'CheckoutMode' enum.

    Store processing mode reflected in the checkout configuration: `live` and `test`
    reflect the credential used to authenticate, while `live_test` is reserved for
    privileged callers testing against live-mode data.

    Attributes:
        LIVE: The enum member of type str.
        TEST: The enum member of type str.
        LIVE_TEST: The enum member of type str.

    """

    LIVE = "live"

    TEST = "test"

    LIVE_TEST = "live_test"

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
