"""univapay_client_sdk.

This file was automatically generated for Univapay by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

# ruff: noqa: E501

class ChargeCreateRequestThreeDsMode(object):
    """Implementation of the 'ChargeCreateRequestThreeDsMode' enum.

    3D-Secure authentication type. App Token Secret is required to use 'skip'.

    Attributes:
        NORMAL: The enum member of type str.
        REQUIRE: The enum member of type str.
        FORCE: The enum member of type str.
        SKIP: The enum member of type str.

    """

    NORMAL = "normal"

    REQUIRE = "require"

    FORCE = "force"

    SKIP = "skip"

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
