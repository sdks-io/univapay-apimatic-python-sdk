"""univapay_client_sdk.

This file was automatically generated for Univapay by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

# ruff: noqa: E501
from univapayclientsdk.api_helper import APIHelper


class MerchantWebhookUserTransactionsConfiguration(object):
    """Implementation of the 'MerchantWebhookUserTransactionsConfiguration' model.

    Merchant transaction notification settings.

    Attributes:
        enabled (bool): Enables merchant transaction notifications.
        notify_customer (bool): Sends transaction notifications to the customer.
        notify_on_test (bool): Sends notifications for test-mode events.
        notify_on_recurring_token_creation (bool): Sends notifications when a
            recurring token is created.
        notify_on_recurring_token_cvv_failed (bool): Sends notifications when
            recurring-token CVV confirmation fails.
        notify_on_webhook_failure (bool): Sends notifications after repeated webhook
            delivery failures.
        notify_on_webhook_disabled (bool): Sends notifications when webhook delivery
            is disabled.
        notify_user_on_failed_transactions (bool): Sends merchant notifications for
            failed transactions.
        notify_customer_on_failed_transactions (bool): Sends customer notifications
            for failed transactions.
        notify_user_on_convenience_instructions (bool): Sends merchant notifications
            with convenience-store payment instructions.
        notify_on_subscriptions (bool): Sends notifications for subscription
            lifecycle events.
        notify_on_authorizations (bool): Sends notifications for authorization-only
            charges.
        notify_on_cvv_authorizations (bool): Sends notifications for CVV
            authorization events.
        notify_on_cancels (bool): Sends notifications when charges are canceled.
        customer_refer_link_enabled (bool): Includes customer self-service links in
            supported notifications.
        notify_on_convenience_expiry (bool): Sends notifications when convenience
            payments expire.
        notify_on_recurring_token_creation_with_three_ds (bool): Sends notifications
            when recurring tokens are created through 3-D Secure.
        notify_on_chargebacks (bool): Sends notifications for chargeback events.
        additional_properties (Dict[str, Any]): The additional properties for the
            model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "enabled": "enabled",
        "notify_customer": "notify_customer",
        "notify_on_test": "notify_on_test",
        "notify_on_recurring_token_creation": "notify_on_recurring_token_creation",
        "notify_on_recurring_token_cvv_failed": "notify_on_recurring_token_cvv_failed",
        "notify_on_webhook_failure": "notify_on_webhook_failure",
        "notify_on_webhook_disabled": "notify_on_webhook_disabled",
        "notify_user_on_failed_transactions": "notify_user_on_failed_transactions",
        "notify_customer_on_failed_transactions":
            "notify_customer_on_failed_transactions",
        "notify_user_on_convenience_instructions":
            "notify_user_on_convenience_instructions",
        "notify_on_subscriptions": "notify_on_subscriptions",
        "notify_on_authorizations": "notify_on_authorizations",
        "notify_on_cvv_authorizations": "notify_on_cvv_authorizations",
        "notify_on_cancels": "notify_on_cancels",
        "customer_refer_link_enabled": "customer_refer_link_enabled",
        "notify_on_convenience_expiry": "notify_on_convenience_expiry",
        "notify_on_recurring_token_creation_with_three_ds":
            "notify_on_recurring_token_creation_with_three_ds",
        "notify_on_chargebacks": "notify_on_chargebacks",
    }

    _optionals = [
        "enabled",
        "notify_customer",
        "notify_on_test",
        "notify_on_recurring_token_creation",
        "notify_on_recurring_token_cvv_failed",
        "notify_on_webhook_failure",
        "notify_on_webhook_disabled",
        "notify_user_on_failed_transactions",
        "notify_customer_on_failed_transactions",
        "notify_user_on_convenience_instructions",
        "notify_on_subscriptions",
        "notify_on_authorizations",
        "notify_on_cvv_authorizations",
        "notify_on_cancels",
        "customer_refer_link_enabled",
        "notify_on_convenience_expiry",
        "notify_on_recurring_token_creation_with_three_ds",
        "notify_on_chargebacks",
    ]

    _nullables = [
        "enabled",
        "notify_customer",
        "notify_on_test",
        "notify_on_recurring_token_creation",
        "notify_on_recurring_token_cvv_failed",
        "notify_on_webhook_failure",
        "notify_on_webhook_disabled",
        "notify_user_on_failed_transactions",
        "notify_customer_on_failed_transactions",
        "notify_user_on_convenience_instructions",
        "notify_on_subscriptions",
        "notify_on_authorizations",
        "notify_on_cvv_authorizations",
        "notify_on_cancels",
        "customer_refer_link_enabled",
        "notify_on_convenience_expiry",
        "notify_on_recurring_token_creation_with_three_ds",
        "notify_on_chargebacks",
    ]

    def __init__(
        self,
        enabled=APIHelper.SKIP,
        notify_customer=APIHelper.SKIP,
        notify_on_test=APIHelper.SKIP,
        notify_on_recurring_token_creation=APIHelper.SKIP,
        notify_on_recurring_token_cvv_failed=APIHelper.SKIP,
        notify_on_webhook_failure=APIHelper.SKIP,
        notify_on_webhook_disabled=APIHelper.SKIP,
        notify_user_on_failed_transactions=APIHelper.SKIP,
        notify_customer_on_failed_transactions=APIHelper.SKIP,
        notify_user_on_convenience_instructions=APIHelper.SKIP,
        notify_on_subscriptions=APIHelper.SKIP,
        notify_on_authorizations=APIHelper.SKIP,
        notify_on_cvv_authorizations=APIHelper.SKIP,
        notify_on_cancels=APIHelper.SKIP,
        customer_refer_link_enabled=APIHelper.SKIP,
        notify_on_convenience_expiry=APIHelper.SKIP,
        notify_on_recurring_token_creation_with_three_ds=APIHelper.SKIP,
        notify_on_chargebacks=APIHelper.SKIP,
        additional_properties=None):
        """Initialize a MerchantWebhookUserTransactionsConfiguration instance."""
        # Initialize members of the class
        if enabled is not APIHelper.SKIP:
            self.enabled = enabled
        if notify_customer is not APIHelper.SKIP:
            self.notify_customer = notify_customer
        if notify_on_test is not APIHelper.SKIP:
            self.notify_on_test = notify_on_test
        if notify_on_recurring_token_creation is not APIHelper.SKIP:
            self.notify_on_recurring_token_creation =\
                 notify_on_recurring_token_creation
        if notify_on_recurring_token_cvv_failed is not APIHelper.SKIP:
            self.notify_on_recurring_token_cvv_failed =\
                 notify_on_recurring_token_cvv_failed
        if notify_on_webhook_failure is not APIHelper.SKIP:
            self.notify_on_webhook_failure = notify_on_webhook_failure
        if notify_on_webhook_disabled is not APIHelper.SKIP:
            self.notify_on_webhook_disabled = notify_on_webhook_disabled
        if notify_user_on_failed_transactions is not APIHelper.SKIP:
            self.notify_user_on_failed_transactions =\
                 notify_user_on_failed_transactions
        if notify_customer_on_failed_transactions is not APIHelper.SKIP:
            self.notify_customer_on_failed_transactions =\
                 notify_customer_on_failed_transactions
        if notify_user_on_convenience_instructions is not APIHelper.SKIP:
            self.notify_user_on_convenience_instructions =\
                 notify_user_on_convenience_instructions
        if notify_on_subscriptions is not APIHelper.SKIP:
            self.notify_on_subscriptions = notify_on_subscriptions
        if notify_on_authorizations is not APIHelper.SKIP:
            self.notify_on_authorizations = notify_on_authorizations
        if notify_on_cvv_authorizations is not APIHelper.SKIP:
            self.notify_on_cvv_authorizations = notify_on_cvv_authorizations
        if notify_on_cancels is not APIHelper.SKIP:
            self.notify_on_cancels = notify_on_cancels
        if customer_refer_link_enabled is not APIHelper.SKIP:
            self.customer_refer_link_enabled = customer_refer_link_enabled
        if notify_on_convenience_expiry is not APIHelper.SKIP:
            self.notify_on_convenience_expiry = notify_on_convenience_expiry
        if notify_on_recurring_token_creation_with_three_ds is not APIHelper.SKIP:
            self.notify_on_recurring_token_creation_with_three_ds =\
                 notify_on_recurring_token_creation_with_three_ds
        if notify_on_chargebacks is not APIHelper.SKIP:
            self.notify_on_chargebacks = notify_on_chargebacks

        # Add additional model properties to the instance
        if additional_properties is None:
            additional_properties = {}
        self.additional_properties = additional_properties

    @classmethod
    def from_dictionary(cls,
                        dictionary):
        """Create an instance of this model from a dictionary

        Args:
            dictionary (dictionary): A dictionary representation of the object
            as obtained from the deserialization of the server's response. The
            keys MUST match property names in the API description.

        Returns:
            object: An instance of this structure class.

        """
        if not isinstance(dictionary, dict) or dictionary is None:
            return None

        # Extract variables from the dictionary
        enabled =\
            dictionary.get("enabled")\
            if "enabled" in dictionary.keys()\
                else APIHelper.SKIP
        notify_customer =\
            dictionary.get("notify_customer")\
            if "notify_customer" in dictionary.keys()\
                else APIHelper.SKIP
        notify_on_test =\
            dictionary.get("notify_on_test")\
            if "notify_on_test" in dictionary.keys()\
                else APIHelper.SKIP
        notify_on_recurring_token_creation =\
            dictionary.get("notify_on_recurring_token_creation")\
            if "notify_on_recurring_token_creation" in dictionary.keys()\
                else APIHelper.SKIP
        notify_on_recurring_token_cvv_failed =\
            dictionary.get("notify_on_recurring_token_cvv_failed")\
            if "notify_on_recurring_token_cvv_failed" in dictionary.keys()\
                else APIHelper.SKIP
        notify_on_webhook_failure =\
            dictionary.get("notify_on_webhook_failure")\
            if "notify_on_webhook_failure" in dictionary.keys()\
                else APIHelper.SKIP
        notify_on_webhook_disabled =\
            dictionary.get("notify_on_webhook_disabled")\
            if "notify_on_webhook_disabled" in dictionary.keys()\
                else APIHelper.SKIP
        notify_user_on_failed_transactions =\
            dictionary.get("notify_user_on_failed_transactions")\
            if "notify_user_on_failed_transactions" in dictionary.keys()\
                else APIHelper.SKIP
        notify_customer_on_failed_transactions =\
            dictionary.get("notify_customer_on_failed_transactions")\
            if "notify_customer_on_failed_transactions" in dictionary.keys()\
                else APIHelper.SKIP
        notify_user_on_convenience_instructions =\
            dictionary.get("notify_user_on_convenience_instructions")\
            if "notify_user_on_convenience_instructions" in dictionary.keys()\
                else APIHelper.SKIP
        notify_on_subscriptions =\
            dictionary.get("notify_on_subscriptions")\
            if "notify_on_subscriptions" in dictionary.keys()\
                else APIHelper.SKIP
        notify_on_authorizations =\
            dictionary.get("notify_on_authorizations")\
            if "notify_on_authorizations" in dictionary.keys()\
                else APIHelper.SKIP
        notify_on_cvv_authorizations =\
            dictionary.get("notify_on_cvv_authorizations")\
            if "notify_on_cvv_authorizations" in dictionary.keys()\
                else APIHelper.SKIP
        notify_on_cancels =\
            dictionary.get("notify_on_cancels")\
            if "notify_on_cancels" in dictionary.keys()\
                else APIHelper.SKIP
        customer_refer_link_enabled =\
            dictionary.get("customer_refer_link_enabled")\
            if "customer_refer_link_enabled" in dictionary.keys()\
                else APIHelper.SKIP
        notify_on_convenience_expiry =\
            dictionary.get("notify_on_convenience_expiry")\
            if "notify_on_convenience_expiry" in dictionary.keys()\
                else APIHelper.SKIP
        notify_on_recurring_token_creation_with_three_ds =\
            dictionary.get("notify_on_recurring_token_creation_with_three_ds")\
            if "notify_on_recurring_token_creation_with_three_ds" in dictionary.keys()\
                else APIHelper.SKIP
        notify_on_chargebacks =\
            dictionary.get("notify_on_chargebacks")\
            if "notify_on_chargebacks" in dictionary.keys()\
                else APIHelper.SKIP

        additional_properties = APIHelper.get_additional_properties(
            dictionary={k: v for k, v in dictionary.items()
                        if k not in cls._names.values()},
            unboxing_function=lambda value: value)

        # Return an object of this model
        return cls(enabled,
                   notify_customer,
                   notify_on_test,
                   notify_on_recurring_token_creation,
                   notify_on_recurring_token_cvv_failed,
                   notify_on_webhook_failure,
                   notify_on_webhook_disabled,
                   notify_user_on_failed_transactions,
                   notify_customer_on_failed_transactions,
                   notify_user_on_convenience_instructions,
                   notify_on_subscriptions,
                   notify_on_authorizations,
                   notify_on_cvv_authorizations,
                   notify_on_cancels,
                   customer_refer_link_enabled,
                   notify_on_convenience_expiry,
                   notify_on_recurring_token_creation_with_three_ds,
                   notify_on_chargebacks,
                   additional_properties)

    def __repr__(self):
        """Return a unambiguous string representation."""
        _enabled=(
            self.enabled
            if hasattr(self, "enabled")
            else None
        )
        _notify_customer=(
            self.notify_customer
            if hasattr(self, "notify_customer")
            else None
        )
        _notify_on_test=(
            self.notify_on_test
            if hasattr(self, "notify_on_test")
            else None
        )
        _notify_on_recurring_token_creation=(
            self.notify_on_recurring_token_creation
            if hasattr(self, "notify_on_recurring_token_creation")
            else None
        )
        _notify_on_recurring_token_cvv_failed=(
            self.notify_on_recurring_token_cvv_failed
            if hasattr(self, "notify_on_recurring_token_cvv_failed")
            else None
        )
        _notify_on_webhook_failure=(
            self.notify_on_webhook_failure
            if hasattr(self, "notify_on_webhook_failure")
            else None
        )
        _notify_on_webhook_disabled=(
            self.notify_on_webhook_disabled
            if hasattr(self, "notify_on_webhook_disabled")
            else None
        )
        _notify_user_on_failed_transactions=(
            self.notify_user_on_failed_transactions
            if hasattr(self, "notify_user_on_failed_transactions")
            else None
        )
        _notify_customer_on_failed_transactions=(
            self.notify_customer_on_failed_transactions
            if hasattr(self, "notify_customer_on_failed_transactions")
            else None
        )
        _notify_user_on_convenience_instructions=(
            self.notify_user_on_convenience_instructions
            if hasattr(self, "notify_user_on_convenience_instructions")
            else None
        )
        _notify_on_subscriptions=(
            self.notify_on_subscriptions
            if hasattr(self, "notify_on_subscriptions")
            else None
        )
        _notify_on_authorizations=(
            self.notify_on_authorizations
            if hasattr(self, "notify_on_authorizations")
            else None
        )
        _notify_on_cvv_authorizations=(
            self.notify_on_cvv_authorizations
            if hasattr(self, "notify_on_cvv_authorizations")
            else None
        )
        _notify_on_cancels=(
            self.notify_on_cancels
            if hasattr(self, "notify_on_cancels")
            else None
        )
        _customer_refer_link_enabled=(
            self.customer_refer_link_enabled
            if hasattr(self, "customer_refer_link_enabled")
            else None
        )
        _notify_on_convenience_expiry=(
            self.notify_on_convenience_expiry
            if hasattr(self, "notify_on_convenience_expiry")
            else None
        )
        _notify_on_recurring_token_creation_with_three_ds=(
            self.notify_on_recurring_token_creation_with_three_ds
            if hasattr(self, "notify_on_recurring_token_creation_with_three_ds")
            else None
        )
        _notify_on_chargebacks=(
            self.notify_on_chargebacks
            if hasattr(self, "notify_on_chargebacks")
            else None
        )
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"enabled={_enabled!r}, "
            f"notify_customer={_notify_customer!r}, "
            f"notify_on_test={_notify_on_test!r}, "
            f"notify_on_recurring_token_creation={_notify_on_recurring_token_creation!r}, "
            f"notify_on_recurring_token_cvv_failed={_notify_on_recurring_token_cvv_failed!r}, "
            f"notify_on_webhook_failure={_notify_on_webhook_failure!r}, "
            f"notify_on_webhook_disabled={_notify_on_webhook_disabled!r}, "
            f"notify_user_on_failed_transactions={_notify_user_on_failed_transactions!r}, "
            f"notify_customer_on_failed_transactions={_notify_customer_on_failed_transactions!r}, "
            f"notify_user_on_convenience_instructions={_notify_user_on_convenience_instructions!r}, "
            f"notify_on_subscriptions={_notify_on_subscriptions!r}, "
            f"notify_on_authorizations={_notify_on_authorizations!r}, "
            f"notify_on_cvv_authorizations={_notify_on_cvv_authorizations!r}, "
            f"notify_on_cancels={_notify_on_cancels!r}, "
            f"customer_refer_link_enabled={_customer_refer_link_enabled!r}, "
            f"notify_on_convenience_expiry={_notify_on_convenience_expiry!r}, "
            f"notify_on_recurring_token_creation_with_three_ds={_notify_on_recurring_token_creation_with_three_ds!r}, "
            f"notify_on_chargebacks={_notify_on_chargebacks!r}, "
            f"additional_properties={_additional_properties!r}, "
            f")"
        )

    def __str__(self):
        """Return a human-readable string representation."""
        _enabled=(
            self.enabled
            if hasattr(self, "enabled")
            else None
        )
        _notify_customer=(
            self.notify_customer
            if hasattr(self, "notify_customer")
            else None
        )
        _notify_on_test=(
            self.notify_on_test
            if hasattr(self, "notify_on_test")
            else None
        )
        _notify_on_recurring_token_creation=(
            self.notify_on_recurring_token_creation
            if hasattr(self, "notify_on_recurring_token_creation")
            else None
        )
        _notify_on_recurring_token_cvv_failed=(
            self.notify_on_recurring_token_cvv_failed
            if hasattr(self, "notify_on_recurring_token_cvv_failed")
            else None
        )
        _notify_on_webhook_failure=(
            self.notify_on_webhook_failure
            if hasattr(self, "notify_on_webhook_failure")
            else None
        )
        _notify_on_webhook_disabled=(
            self.notify_on_webhook_disabled
            if hasattr(self, "notify_on_webhook_disabled")
            else None
        )
        _notify_user_on_failed_transactions=(
            self.notify_user_on_failed_transactions
            if hasattr(self, "notify_user_on_failed_transactions")
            else None
        )
        _notify_customer_on_failed_transactions=(
            self.notify_customer_on_failed_transactions
            if hasattr(self, "notify_customer_on_failed_transactions")
            else None
        )
        _notify_user_on_convenience_instructions=(
            self.notify_user_on_convenience_instructions
            if hasattr(self, "notify_user_on_convenience_instructions")
            else None
        )
        _notify_on_subscriptions=(
            self.notify_on_subscriptions
            if hasattr(self, "notify_on_subscriptions")
            else None
        )
        _notify_on_authorizations=(
            self.notify_on_authorizations
            if hasattr(self, "notify_on_authorizations")
            else None
        )
        _notify_on_cvv_authorizations=(
            self.notify_on_cvv_authorizations
            if hasattr(self, "notify_on_cvv_authorizations")
            else None
        )
        _notify_on_cancels=(
            self.notify_on_cancels
            if hasattr(self, "notify_on_cancels")
            else None
        )
        _customer_refer_link_enabled=(
            self.customer_refer_link_enabled
            if hasattr(self, "customer_refer_link_enabled")
            else None
        )
        _notify_on_convenience_expiry=(
            self.notify_on_convenience_expiry
            if hasattr(self, "notify_on_convenience_expiry")
            else None
        )
        _notify_on_recurring_token_creation_with_three_ds=(
            self.notify_on_recurring_token_creation_with_three_ds
            if hasattr(self, "notify_on_recurring_token_creation_with_three_ds")
            else None
        )
        _notify_on_chargebacks=(
            self.notify_on_chargebacks
            if hasattr(self, "notify_on_chargebacks")
            else None
        )
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"enabled={_enabled!s}, "
            f"notify_customer={_notify_customer!s}, "
            f"notify_on_test={_notify_on_test!s}, "
            f"notify_on_recurring_token_creation={_notify_on_recurring_token_creation!s}, "
            f"notify_on_recurring_token_cvv_failed={_notify_on_recurring_token_cvv_failed!s}, "
            f"notify_on_webhook_failure={_notify_on_webhook_failure!s}, "
            f"notify_on_webhook_disabled={_notify_on_webhook_disabled!s}, "
            f"notify_user_on_failed_transactions={_notify_user_on_failed_transactions!s}, "
            f"notify_customer_on_failed_transactions={_notify_customer_on_failed_transactions!s}, "
            f"notify_user_on_convenience_instructions={_notify_user_on_convenience_instructions!s}, "
            f"notify_on_subscriptions={_notify_on_subscriptions!s}, "
            f"notify_on_authorizations={_notify_on_authorizations!s}, "
            f"notify_on_cvv_authorizations={_notify_on_cvv_authorizations!s}, "
            f"notify_on_cancels={_notify_on_cancels!s}, "
            f"customer_refer_link_enabled={_customer_refer_link_enabled!s}, "
            f"notify_on_convenience_expiry={_notify_on_convenience_expiry!s}, "
            f"notify_on_recurring_token_creation_with_three_ds={_notify_on_recurring_token_creation_with_three_ds!s}, "
            f"notify_on_chargebacks={_notify_on_chargebacks!s}, "
            f"additional_properties={_additional_properties!s}, "
            f")"
        )
