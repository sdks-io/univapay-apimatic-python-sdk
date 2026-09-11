"""univapay_client_sdk.

This file was automatically generated for Univapay by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

# ruff: noqa: E501

class ChargeCreateRequestThreeDsMode(object):
    """Implementation of the 'ChargeCreateRequestThreeDsMode' enum.

    3D-Secure authentication type. App Token Secret is required to use 'skip'.
    `if_available` enforces 3DS only if credentials are available for the recurring
    token and it has not already completed 3DS. `provided` is set automatically by
    the server when external MPI authentication data (`authentication_value`, `eci`,
    etc.) is submitted on the request and cannot be set manually. When omitted, the
    store's default 3DS policy applies — do not assume 'normal'.

    Attributes:
        NORMAL: The enum member of type str.
        REQUIRE: The enum member of type str.
        FORCE: The enum member of type str.
        SKIP: The enum member of type str.
        IF_AVAILABLE: The enum member of type str.
        PROVIDED: The enum member of type str.

    """

    NORMAL = "normal"

    REQUIRE = "require"

    FORCE = "force"

    SKIP = "skip"

    IF_AVAILABLE = "if_available"

    PROVIDED = "provided"

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
