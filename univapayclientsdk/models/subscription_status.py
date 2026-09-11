"""univapay_client_sdk.

This file was automatically generated for Univapay by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

# ruff: noqa: E501

class SubscriptionStatus(object):
    """Implementation of the 'SubscriptionStatus' enum.

    Subscription Status schema.

    Attributes:
        UNVERIFIED: The enum member of type str.
        UNCONFIRMED: The enum member of type str.
        CANCELED: The enum member of type str.
        UNPAID: The enum member of type str.
        CURRENT: The enum member of type str.
        SUSPENDED: The enum member of type str.
        COMPLETED: The enum member of type str.

    """

    _all_values = ["unverified", "unconfirmed", "canceled", "unpaid", "current", "suspended",
        "completed"]
    UNVERIFIED = "unverified"

    UNCONFIRMED = "unconfirmed"

    CANCELED = "canceled"

    UNPAID = "unpaid"

    CURRENT = "current"

    SUSPENDED = "suspended"

    COMPLETED = "completed"

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
