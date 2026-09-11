"""univapay_client_sdk.

This file was automatically generated for Univapay by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

# ruff: noqa: E501

class SubscriptionEvent(object):
    """Implementation of the 'SubscriptionEvent' enum.

    Event type discriminator — `subscription_created`, `subscription_payment`,
    `subscription_completed`, `subscription_failure`, `subscription_canceled`, or
    `subscription_suspended`.

    Attributes:
        SUBSCRIPTION_CREATED: The enum member of type str.
        SUBSCRIPTION_PAYMENT: The enum member of type str.
        SUBSCRIPTION_COMPLETED: The enum member of type str.
        SUBSCRIPTION_FAILURE: The enum member of type str.
        SUBSCRIPTION_CANCELED: The enum member of type str.
        SUBSCRIPTION_SUSPENDED: The enum member of type str.

    """

    _all_values = ["subscription_created", "subscription_payment", "subscription_completed",
        "subscription_failure", "subscription_canceled", "subscription_suspended"]
    SUBSCRIPTION_CREATED = "subscription_created"

    SUBSCRIPTION_PAYMENT = "subscription_payment"

    SUBSCRIPTION_COMPLETED = "subscription_completed"

    SUBSCRIPTION_FAILURE = "subscription_failure"

    SUBSCRIPTION_CANCELED = "subscription_canceled"

    SUBSCRIPTION_SUSPENDED = "subscription_suspended"

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
