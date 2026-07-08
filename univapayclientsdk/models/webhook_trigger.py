"""univapay_client_sdk.

This file was automatically generated for Univapay by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

# ruff: noqa: E501

class WebhookTrigger(object):
    """Implementation of the 'WebhookTrigger' enum.

    Event type that triggers a webhook notification.

    Attributes:
        TOKEN_CREATED: The enum member of type str.
        TOKEN_UPDATED: The enum member of type str.
        TOKEN_THREE_D_S_UPDATED: The enum member of type str.
        TOKEN_CVV_AUTH_UPDATED: The enum member of type str.
        TOKEN_CVV_AUTH_CHECK_UPDATED: The enum member of type str.
        TOKEN_REPLACED: The enum member of type str.
        CHARGE_UPDATED: The enum member of type str.
        CHARGE_FINISHED: The enum member of type str.
        REFUND_FINISHED: The enum member of type str.
        CANCEL_FINISHED: The enum member of type str.
        CUSTOMS_DECLARATION_FINISHED: The enum member of type str.
        RECURRING_TOKEN_DELETED: The enum member of type str.
        BANK_TRANSFER_STATUS_UPDATED: The enum member of type str.
        SUBSCRIPTION_CREATED: The enum member of type str.
        SUBSCRIPTION_PAYMENT: The enum member of type str.
        SUBSCRIPTION_COMPLETED: The enum member of type str.
        SUBSCRIPTION_FAILURE: The enum member of type str.
        SUBSCRIPTION_CANCELED: The enum member of type str.
        SUBSCRIPTION_SUSPENDED: The enum member of type str.

    """

    TOKEN_CREATED = "token_created"

    TOKEN_UPDATED = "token_updated"

    TOKEN_THREE_D_S_UPDATED = "token_three_d_s_updated"

    TOKEN_CVV_AUTH_UPDATED = "token_cvv_auth_updated"

    TOKEN_CVV_AUTH_CHECK_UPDATED = "token_cvv_auth_check_updated"

    TOKEN_REPLACED = "token_replaced"

    CHARGE_UPDATED = "charge_updated"

    CHARGE_FINISHED = "charge_finished"

    REFUND_FINISHED = "refund_finished"

    CANCEL_FINISHED = "cancel_finished"

    CUSTOMS_DECLARATION_FINISHED = "customs_declaration_finished"

    RECURRING_TOKEN_DELETED = "recurring_token_deleted"

    BANK_TRANSFER_STATUS_UPDATED = "bank_transfer_status_updated"

    SUBSCRIPTION_CREATED = "subscription_created"

    SUBSCRIPTION_PAYMENT = "subscription_payment"

    SUBSCRIPTION_COMPLETED = "subscription_completed"

    SUBSCRIPTION_FAILURE = "subscription_failure"

    SUBSCRIPTION_CANCELED = "subscription_canceled"

    SUBSCRIPTION_SUSPENDED = "subscription_suspended"

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
