"""univapay_client_sdk.

This file was automatically generated for Univapay by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

# ruff: noqa: E501

class SubscriptionThreeDsMode(object):
    """Implementation of the 'SubscriptionThreeDsMode' enum.

    3-D Secure authentication mode applied to the subscription's payments.
    `if_available` enforces 3DS only if credentials are available for the recurring
    token and it has not already completed 3DS. `provided` indicates externally
    supplied MPI authentication data was used.

    Attributes:
        NORMAL: The enum member of type str.
        REQUIRE: The enum member of type str.
        FORCE: The enum member of type str.
        SKIP: The enum member of type str.
        IF_AVAILABLE: The enum member of type str.
        PROVIDED: The enum member of type str.

    """

    _all_values = ["normal", "require", "force", "skip", "if_available", "provided"]
    NORMAL = "normal"

    REQUIRE = "require"

    FORCE = "force"

    SKIP = "skip"

    IF_AVAILABLE = "if_available"

    PROVIDED = "provided"

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
