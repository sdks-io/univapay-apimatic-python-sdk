"""univapay_client_sdk.

This file was automatically generated for Univapay by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

# ruff: noqa: E501

class SubscriptionSimulationPeriod(object):
    """Implementation of the 'SubscriptionSimulationPeriod' enum.

    Billing frequency for the simulated schedule. Includes `bimonthly`, which is not
    offered on `SubscriptionPeriod` for live subscription creation.

    Attributes:
        DAILY: The enum member of type str.
        WEEKLY: The enum member of type str.
        BIWEEKLY: The enum member of type str.
        MONTHLY: The enum member of type str.
        BIMONTHLY: The enum member of type str.
        QUARTERLY: The enum member of type str.
        SEMIANNUALLY: The enum member of type str.
        ANNUALLY: The enum member of type str.

    """

    DAILY = "daily"

    WEEKLY = "weekly"

    BIWEEKLY = "biweekly"

    MONTHLY = "monthly"

    BIMONTHLY = "bimonthly"

    QUARTERLY = "quarterly"

    SEMIANNUALLY = "semiannually"

    ANNUALLY = "annually"

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
