"""univapay_client_sdk.

This file was automatically generated for Univapay by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

# ruff: noqa: E501
from univapayclientsdk.api_helper import APIHelper
from univapayclientsdk.models.generic_metadata import (
    GenericMetadata,
)
from univapayclientsdk.models.subscription_next_payment import (
    SubscriptionNextPayment,
)
from univapayclientsdk.models.subscription_schedule_settings import (
    SubscriptionScheduleSettings,
)


class Subscription(object):
    """Implementation of the 'Subscription' model.

    The Subscription object represents a recurring payment schedule.

    Attributes:
        id (uuid|str): Unique identifier.
        store_id (uuid|str): Store identifier.
        transaction_token_id (uuid|str): Transaction token identifier.
        amount (int): Amount in the smallest currency unit.
        currency (str): ISO-4217 currency code.
        amount_formatted (float): Amount formatted for display.
        initial_amount (int): Initial amount in the smallest currency unit.
        initial_amount_formatted (float): Initial amount formatted for display.
        subsequent_cycles_start (datetime): Timestamp when recurring cycles begin.
        schedule_settings (SubscriptionScheduleSettings): Schedule settings applied
            to a subscription.
        only_direct_currency (bool): Whether only direct currency processing is
            allowed.
        first_charge_capture_after (str): ISO-8601 Duration (e.g., P3D).
        first_charge_authorization_only (bool): Whether the first charge is
            authorization-only.
        status (SubscriptionStatus): Subscription Status schema.
        metadata (GenericMetadata): A free-form dictionary for custom metadata.
        mode (ChargeMode): Charge Mode schema.
        created_on (datetime): Timestamp when the resource was created.
        period (SubscriptionPeriod): Subscription Period schema.
        next_payment (SubscriptionNextPayment): Next scheduled payment details for a
            subscription.
        additional_properties (Dict[str, Any]): The additional properties for the
            model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "id": "id",
        "store_id": "store_id",
        "transaction_token_id": "transaction_token_id",
        "amount": "amount",
        "currency": "currency",
        "amount_formatted": "amount_formatted",
        "initial_amount": "initial_amount",
        "initial_amount_formatted": "initial_amount_formatted",
        "subsequent_cycles_start": "subsequent_cycles_start",
        "schedule_settings": "schedule_settings",
        "only_direct_currency": "only_direct_currency",
        "first_charge_capture_after": "first_charge_capture_after",
        "first_charge_authorization_only": "first_charge_authorization_only",
        "status": "status",
        "metadata": "metadata",
        "mode": "mode",
        "created_on": "created_on",
        "period": "period",
        "next_payment": "next_payment",
    }

    _optionals = [
        "id",
        "store_id",
        "transaction_token_id",
        "amount",
        "currency",
        "amount_formatted",
        "initial_amount",
        "initial_amount_formatted",
        "subsequent_cycles_start",
        "schedule_settings",
        "only_direct_currency",
        "first_charge_capture_after",
        "first_charge_authorization_only",
        "status",
        "metadata",
        "mode",
        "created_on",
        "period",
        "next_payment",
    ]

    _nullables = [
        "initial_amount",
        "initial_amount_formatted",
        "subsequent_cycles_start",
        "first_charge_capture_after",
    ]

    def __init__(
        self,
        id=APIHelper.SKIP,
        store_id=APIHelper.SKIP,
        transaction_token_id=APIHelper.SKIP,
        amount=APIHelper.SKIP,
        currency=APIHelper.SKIP,
        amount_formatted=APIHelper.SKIP,
        initial_amount=APIHelper.SKIP,
        initial_amount_formatted=APIHelper.SKIP,
        subsequent_cycles_start=APIHelper.SKIP,
        schedule_settings=APIHelper.SKIP,
        only_direct_currency=APIHelper.SKIP,
        first_charge_capture_after=APIHelper.SKIP,
        first_charge_authorization_only=APIHelper.SKIP,
        status=APIHelper.SKIP,
        metadata=APIHelper.SKIP,
        mode=APIHelper.SKIP,
        created_on=APIHelper.SKIP,
        period=APIHelper.SKIP,
        next_payment=APIHelper.SKIP,
        additional_properties=None):
        """Initialize a Subscription instance."""
        # Initialize members of the class
        if id is not APIHelper.SKIP:
            self.id = id
        if store_id is not APIHelper.SKIP:
            self.store_id = store_id
        if transaction_token_id is not APIHelper.SKIP:
            self.transaction_token_id = transaction_token_id
        if amount is not APIHelper.SKIP:
            self.amount = amount
        if currency is not APIHelper.SKIP:
            self.currency = currency
        if amount_formatted is not APIHelper.SKIP:
            self.amount_formatted = amount_formatted
        if initial_amount is not APIHelper.SKIP:
            self.initial_amount = initial_amount
        if initial_amount_formatted is not APIHelper.SKIP:
            self.initial_amount_formatted = initial_amount_formatted
        if subsequent_cycles_start is not APIHelper.SKIP:
            self.subsequent_cycles_start =\
                 APIHelper.apply_datetime_converter(
                subsequent_cycles_start, APIHelper.RFC3339DateTime)\
                 if subsequent_cycles_start else None
        if schedule_settings is not APIHelper.SKIP:
            self.schedule_settings = schedule_settings
        if only_direct_currency is not APIHelper.SKIP:
            self.only_direct_currency = only_direct_currency
        if first_charge_capture_after is not APIHelper.SKIP:
            self.first_charge_capture_after = first_charge_capture_after
        if first_charge_authorization_only is not APIHelper.SKIP:
            self.first_charge_authorization_only = first_charge_authorization_only
        if status is not APIHelper.SKIP:
            self.status = status
        if metadata is not APIHelper.SKIP:
            self.metadata = metadata
        if mode is not APIHelper.SKIP:
            self.mode = mode
        if created_on is not APIHelper.SKIP:
            self.created_on =\
                 APIHelper.apply_datetime_converter(
                created_on, APIHelper.RFC3339DateTime)\
                 if created_on else None
        if period is not APIHelper.SKIP:
            self.period = period
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
        id =\
            dictionary.get("id")\
            if dictionary.get("id")\
                else APIHelper.SKIP
        store_id =\
            dictionary.get("store_id")\
            if dictionary.get("store_id")\
                else APIHelper.SKIP
        transaction_token_id =\
            dictionary.get("transaction_token_id")\
            if dictionary.get("transaction_token_id")\
                else APIHelper.SKIP
        amount =\
            dictionary.get("amount")\
            if dictionary.get("amount")\
                else APIHelper.SKIP
        currency =\
            dictionary.get("currency")\
            if dictionary.get("currency")\
                else APIHelper.SKIP
        amount_formatted =\
            dictionary.get("amount_formatted")\
            if dictionary.get("amount_formatted")\
                else APIHelper.SKIP
        initial_amount =\
            dictionary.get("initial_amount")\
            if "initial_amount" in dictionary.keys()\
                else APIHelper.SKIP
        initial_amount_formatted =\
            dictionary.get("initial_amount_formatted")\
            if "initial_amount_formatted" in dictionary.keys()\
                else APIHelper.SKIP
        if "subsequent_cycles_start" in dictionary.keys():
            subsequent_cycles_start = APIHelper.RFC3339DateTime.from_value(
                dictionary.get("subsequent_cycles_start")).datetime\
                if dictionary.get("subsequent_cycles_start") else None

        else:
            subsequent_cycles_start = APIHelper.SKIP
        schedule_settings =\
            SubscriptionScheduleSettings.from_dictionary(
                dictionary.get("schedule_settings"))\
                if "schedule_settings" in dictionary.keys()\
                else APIHelper.SKIP
        only_direct_currency =\
            dictionary.get("only_direct_currency")\
            if "only_direct_currency" in dictionary.keys()\
                else APIHelper.SKIP
        first_charge_capture_after =\
            dictionary.get("first_charge_capture_after")\
            if "first_charge_capture_after" in dictionary.keys()\
                else APIHelper.SKIP
        first_charge_authorization_only =\
            dictionary.get("first_charge_authorization_only")\
            if "first_charge_authorization_only" in dictionary.keys()\
                else APIHelper.SKIP
        status =\
            dictionary.get("status")\
            if dictionary.get("status")\
                else APIHelper.SKIP
        metadata =\
            GenericMetadata.from_dictionary(
                dictionary.get("metadata"))\
                if "metadata" in dictionary.keys()\
                else APIHelper.SKIP
        mode =\
            dictionary.get("mode")\
            if dictionary.get("mode")\
                else APIHelper.SKIP
        created_on = APIHelper.RFC3339DateTime.from_value(
            dictionary.get("created_on")).datetime\
            if dictionary.get("created_on") else APIHelper.SKIP
        period =\
            dictionary.get("period")\
            if dictionary.get("period")\
                else APIHelper.SKIP
        next_payment =\
            SubscriptionNextPayment.from_dictionary(
                dictionary.get("next_payment"))\
                if "next_payment" in dictionary.keys()\
                else APIHelper.SKIP

        additional_properties = APIHelper.get_additional_properties(
            dictionary={k: v for k, v in dictionary.items()
                        if k not in cls._names.values()},
            unboxing_function=lambda value: value)

        # Return an object of this model
        return cls(id,
                   store_id,
                   transaction_token_id,
                   amount,
                   currency,
                   amount_formatted,
                   initial_amount,
                   initial_amount_formatted,
                   subsequent_cycles_start,
                   schedule_settings,
                   only_direct_currency,
                   first_charge_capture_after,
                   first_charge_authorization_only,
                   status,
                   metadata,
                   mode,
                   created_on,
                   period,
                   next_payment,
                   additional_properties)

    @classmethod
    def validate(cls, dictionary):
        """Validate dictionary against class required properties

        Args:
            dictionary (dictionary): A dictionary representation of the object
            as obtained from the deserialization of the server's response. The
            keys MUST match property names in the API description.

        Returns:
            boolean : if dictionary is valid contains required properties.

        """
        if isinstance(dictionary, cls):
            return True

        if not isinstance(dictionary, dict):
            return False

        return True

    def __repr__(self):
        """Return a unambiguous string representation."""
        _id=(
            self.id
            if hasattr(self, "id")
            else None
        )
        _store_id=(
            self.store_id
            if hasattr(self, "store_id")
            else None
        )
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
        _currency=(
            self.currency
            if hasattr(self, "currency")
            else None
        )
        _amount_formatted=(
            self.amount_formatted
            if hasattr(self, "amount_formatted")
            else None
        )
        _initial_amount=(
            self.initial_amount
            if hasattr(self, "initial_amount")
            else None
        )
        _initial_amount_formatted=(
            self.initial_amount_formatted
            if hasattr(self, "initial_amount_formatted")
            else None
        )
        _subsequent_cycles_start=(
            self.subsequent_cycles_start
            if hasattr(self, "subsequent_cycles_start")
            else None
        )
        _schedule_settings=(
            self.schedule_settings
            if hasattr(self, "schedule_settings")
            else None
        )
        _only_direct_currency=(
            self.only_direct_currency
            if hasattr(self, "only_direct_currency")
            else None
        )
        _first_charge_capture_after=(
            self.first_charge_capture_after
            if hasattr(self, "first_charge_capture_after")
            else None
        )
        _first_charge_authorization_only=(
            self.first_charge_authorization_only
            if hasattr(self, "first_charge_authorization_only")
            else None
        )
        _status=(
            self.status
            if hasattr(self, "status")
            else None
        )
        _metadata=(
            self.metadata
            if hasattr(self, "metadata")
            else None
        )
        _mode=(
            self.mode
            if hasattr(self, "mode")
            else None
        )
        _created_on=(
            self.created_on
            if hasattr(self, "created_on")
            else None
        )
        _period=(
            self.period
            if hasattr(self, "period")
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
            f"id={_id!r}, "
            f"store_id={_store_id!r}, "
            f"transaction_token_id={_transaction_token_id!r}, "
            f"amount={_amount!r}, "
            f"currency={_currency!r}, "
            f"amount_formatted={_amount_formatted!r}, "
            f"initial_amount={_initial_amount!r}, "
            f"initial_amount_formatted={_initial_amount_formatted!r}, "
            f"subsequent_cycles_start={_subsequent_cycles_start!r}, "
            f"schedule_settings={_schedule_settings!r}, "
            f"only_direct_currency={_only_direct_currency!r}, "
            f"first_charge_capture_after={_first_charge_capture_after!r}, "
            f"first_charge_authorization_only={_first_charge_authorization_only!r}, "
            f"status={_status!r}, "
            f"metadata={_metadata!r}, "
            f"mode={_mode!r}, "
            f"created_on={_created_on!r}, "
            f"period={_period!r}, "
            f"next_payment={_next_payment!r}, "
            f"additional_properties={_additional_properties!r}, "
            f")"
        )

    def __str__(self):
        """Return a human-readable string representation."""
        _id=(
            self.id
            if hasattr(self, "id")
            else None
        )
        _store_id=(
            self.store_id
            if hasattr(self, "store_id")
            else None
        )
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
        _currency=(
            self.currency
            if hasattr(self, "currency")
            else None
        )
        _amount_formatted=(
            self.amount_formatted
            if hasattr(self, "amount_formatted")
            else None
        )
        _initial_amount=(
            self.initial_amount
            if hasattr(self, "initial_amount")
            else None
        )
        _initial_amount_formatted=(
            self.initial_amount_formatted
            if hasattr(self, "initial_amount_formatted")
            else None
        )
        _subsequent_cycles_start=(
            self.subsequent_cycles_start
            if hasattr(self, "subsequent_cycles_start")
            else None
        )
        _schedule_settings=(
            self.schedule_settings
            if hasattr(self, "schedule_settings")
            else None
        )
        _only_direct_currency=(
            self.only_direct_currency
            if hasattr(self, "only_direct_currency")
            else None
        )
        _first_charge_capture_after=(
            self.first_charge_capture_after
            if hasattr(self, "first_charge_capture_after")
            else None
        )
        _first_charge_authorization_only=(
            self.first_charge_authorization_only
            if hasattr(self, "first_charge_authorization_only")
            else None
        )
        _status=(
            self.status
            if hasattr(self, "status")
            else None
        )
        _metadata=(
            self.metadata
            if hasattr(self, "metadata")
            else None
        )
        _mode=(
            self.mode
            if hasattr(self, "mode")
            else None
        )
        _created_on=(
            self.created_on
            if hasattr(self, "created_on")
            else None
        )
        _period=(
            self.period
            if hasattr(self, "period")
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
            f"id={_id!s}, "
            f"store_id={_store_id!s}, "
            f"transaction_token_id={_transaction_token_id!s}, "
            f"amount={_amount!s}, "
            f"currency={_currency!s}, "
            f"amount_formatted={_amount_formatted!s}, "
            f"initial_amount={_initial_amount!s}, "
            f"initial_amount_formatted={_initial_amount_formatted!s}, "
            f"subsequent_cycles_start={_subsequent_cycles_start!s}, "
            f"schedule_settings={_schedule_settings!s}, "
            f"only_direct_currency={_only_direct_currency!s}, "
            f"first_charge_capture_after={_first_charge_capture_after!s}, "
            f"first_charge_authorization_only={_first_charge_authorization_only!s}, "
            f"status={_status!s}, "
            f"metadata={_metadata!s}, "
            f"mode={_mode!s}, "
            f"created_on={_created_on!s}, "
            f"period={_period!s}, "
            f"next_payment={_next_payment!s}, "
            f"additional_properties={_additional_properties!s}, "
            f")"
        )
