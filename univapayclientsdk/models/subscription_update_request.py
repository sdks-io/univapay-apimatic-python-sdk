"""univapay_client_sdk.

This file was automatically generated for Univapay by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

# ruff: noqa: E501
from univapayclientsdk.api_helper import APIHelper
from univapayclientsdk.models.generic_metadata import (
    GenericMetadata,
)
from univapayclientsdk.models.subscription_update_next_payment import (
    SubscriptionUpdateNextPayment,
)
from univapayclientsdk.models.subscription_update_schedule_settings import (
    SubscriptionUpdateScheduleSettings,
)


class SubscriptionUpdateRequest(object):
    """Implementation of the 'SubscriptionUpdateRequest' model.

    Request payload for updating a subscription.

    Attributes:
        transaction_token_id (uuid|str): Transaction token ID used for the
            subscription.  Can be changed to update the payment method (e.g., when a
            card expires).  Allowed only when the status is `unconfirmed`, `unpaid`,
            `current`, or `suspended`.
        amount (int): The recurring charge amount (applied to the cycle after the
            next one).  Not available for limited-cycle subscriptions.  To change the
            immediate next payment amount, update `next_payment.amount` instead.
        metadata (GenericMetadata): A free-form dictionary for custom metadata.
        status (SubscriptionUpdateStatus): Update the subscription status.
            `suspended`: Pause the subscription.  `unpaid`: Resume a suspended
            subscription.
        schedule_settings (SubscriptionUpdateScheduleSettings): Schedule settings
            that can be updated on a subscription.
        next_payment (SubscriptionUpdateNextPayment): Fields that can be updated on
            the next scheduled payment.
        additional_properties (Dict[str, Any]): The additional properties for the
            model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "transaction_token_id": "transaction_token_id",
        "amount": "amount",
        "metadata": "metadata",
        "status": "status",
        "schedule_settings": "schedule_settings",
        "next_payment": "next_payment",
    }

    _optionals = [
        "transaction_token_id",
        "amount",
        "metadata",
        "status",
        "schedule_settings",
        "next_payment",
    ]

    def __init__(
        self,
        transaction_token_id=APIHelper.SKIP,
        amount=APIHelper.SKIP,
        metadata=APIHelper.SKIP,
        status=APIHelper.SKIP,
        schedule_settings=APIHelper.SKIP,
        next_payment=APIHelper.SKIP,
        additional_properties=None):
        """Initialize a SubscriptionUpdateRequest instance."""
        # Initialize members of the class
        if transaction_token_id is not APIHelper.SKIP:
            self.transaction_token_id = transaction_token_id
        if amount is not APIHelper.SKIP:
            self.amount = amount
        if metadata is not APIHelper.SKIP:
            self.metadata = metadata
        if status is not APIHelper.SKIP:
            self.status = status
        if schedule_settings is not APIHelper.SKIP:
            self.schedule_settings = schedule_settings
        if next_payment is not APIHelper.SKIP:
            self.next_payment = next_payment

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
        transaction_token_id =\
            dictionary.get("transaction_token_id")\
            if dictionary.get("transaction_token_id")\
                else APIHelper.SKIP
        amount =\
            dictionary.get("amount")\
            if dictionary.get("amount")\
                else APIHelper.SKIP
        metadata =\
            GenericMetadata.from_dictionary(
                dictionary.get("metadata"))\
                if "metadata" in dictionary.keys()\
                else APIHelper.SKIP
        status =\
            dictionary.get("status")\
            if dictionary.get("status")\
                else APIHelper.SKIP
        schedule_settings =\
            SubscriptionUpdateScheduleSettings.from_dictionary(
                dictionary.get("schedule_settings"))\
                if "schedule_settings" in dictionary.keys()\
                else APIHelper.SKIP
        next_payment =\
            SubscriptionUpdateNextPayment.from_dictionary(
                dictionary.get("next_payment"))\
                if "next_payment" in dictionary.keys()\
                else APIHelper.SKIP

        additional_properties = APIHelper.get_additional_properties(
            dictionary={k: v for k, v in dictionary.items()
                        if k not in cls._names.values()},
            unboxing_function=lambda value: value)

        # Return an object of this model
        return cls(transaction_token_id,
                   amount,
                   metadata,
                   status,
                   schedule_settings,
                   next_payment,
                   additional_properties)

    def __repr__(self):
        """Return a unambiguous string representation."""
        _transaction_token_id=(
            self.transaction_token_id
            if hasattr(self, "transaction_token_id")
            else None
        )
        _amount=(
            self.amount
            if hasattr(self, "amount")
            else None
        )
        _metadata=(
            self.metadata
            if hasattr(self, "metadata")
            else None
        )
        _status=(
            self.status
            if hasattr(self, "status")
            else None
        )
        _schedule_settings=(
            self.schedule_settings
            if hasattr(self, "schedule_settings")
            else None
        )
        _next_payment=(
            self.next_payment
            if hasattr(self, "next_payment")
            else None
        )
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"transaction_token_id={_transaction_token_id!r}, "
            f"amount={_amount!r}, "
            f"metadata={_metadata!r}, "
            f"status={_status!r}, "
            f"schedule_settings={_schedule_settings!r}, "
            f"next_payment={_next_payment!r}, "
            f"additional_properties={_additional_properties!r}, "
            f")"
        )

    def __str__(self):
        """Return a human-readable string representation."""
        _transaction_token_id=(
            self.transaction_token_id
            if hasattr(self, "transaction_token_id")
            else None
        )
        _amount=(
            self.amount
            if hasattr(self, "amount")
            else None
        )
        _metadata=(
            self.metadata
            if hasattr(self, "metadata")
            else None
        )
        _status=(
            self.status
            if hasattr(self, "status")
            else None
        )
        _schedule_settings=(
            self.schedule_settings
            if hasattr(self, "schedule_settings")
            else None
        )
        _next_payment=(
            self.next_payment
            if hasattr(self, "next_payment")
            else None
        )
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"transaction_token_id={_transaction_token_id!s}, "
            f"amount={_amount!s}, "
            f"metadata={_metadata!s}, "
            f"status={_status!s}, "
            f"schedule_settings={_schedule_settings!s}, "
            f"next_payment={_next_payment!s}, "
            f"additional_properties={_additional_properties!s}, "
            f")"
        )
