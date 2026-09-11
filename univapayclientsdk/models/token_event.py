"""univapay_client_sdk.

This file was automatically generated for Univapay by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

# ruff: noqa: E501

class TokenEvent(object):
    """Implementation of the 'TokenEvent' enum.

    Event type discriminator — `token_created`, `token_updated`,
    `token_three_d_s_updated`, `token_cvv_auth_updated`,
    `token_cvv_auth_check_updated`, `token_replaced`, or `recurring_token_deleted`.

    Attributes:
        TOKEN_CREATED: The enum member of type str.
        TOKEN_UPDATED: The enum member of type str.
        TOKEN_THREE_D_S_UPDATED: The enum member of type str.
        TOKEN_CVV_AUTH_UPDATED: The enum member of type str.
        TOKEN_CVV_AUTH_CHECK_UPDATED: The enum member of type str.
        TOKEN_REPLACED: The enum member of type str.
        RECURRING_TOKEN_DELETED: The enum member of type str.

    """

    _all_values = ["token_created", "token_updated", "token_three_d_s_updated",
        "token_cvv_auth_updated", "token_cvv_auth_check_updated", "token_replaced",
        "recurring_token_deleted"]
    TOKEN_CREATED = "token_created"

    TOKEN_UPDATED = "token_updated"

    TOKEN_THREE_D_S_UPDATED = "token_three_d_s_updated"

    TOKEN_CVV_AUTH_UPDATED = "token_cvv_auth_updated"

    TOKEN_CVV_AUTH_CHECK_UPDATED = "token_cvv_auth_check_updated"

    TOKEN_REPLACED = "token_replaced"

    RECURRING_TOKEN_DELETED = "recurring_token_deleted"

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
