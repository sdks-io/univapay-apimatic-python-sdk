"""univapay_client_sdk.

This file was automatically generated for Univapay by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

# ruff: noqa: E501

class SubscriptionPeriod(object):
    """Implementation of the 'SubscriptionPeriod' enum.

    Subscription Period schema.

    Attributes:
        DAILY: The enum member of type str.
        WEEKLY: The enum member of type str.
        BIWEEKLY: The enum member of type str.
        MONTHLY: The enum member of type str.
        QUARTERLY: The enum member of type str.
        SEMIANNUALLY: The enum member of type str.
        ANNUALLY: The enum member of type str.

    """

    _all_values = ["daily", "weekly", "biweekly", "monthly", "quarterly",
        "semiannually", "annually"]
    DAILY = "daily"

    WEEKLY = "weekly"

    BIWEEKLY = "biweekly"

    MONTHLY = "monthly"

    QUARTERLY = "quarterly"

    SEMIANNUALLY = "semiannually"

    ANNUALLY = "annually"

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
