"""univapay_client_sdk.

This file was automatically generated for Univapay by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

# ruff: noqa: E501
import dateutil.parser

from univapayclientsdk.api_helper import APIHelper


class SubscriptionSimulationPayment(object):
    """Implementation of the 'SubscriptionSimulationPayment' model.

    A single scheduled payment produced by the subscription plan simulation.

    Attributes:
        due_date (date): Scheduled due date for this simulated payment (YYYY-MM-DD).
        zone_id (str): IANA timezone identifier used to resolve the due date.
        amount (int): Amount to be charged on this cycle, in the smallest currency
            unit.
        currency (str): ISO-4217 currency code.
        is_paid (bool): Always `false` for simulated payments — no real payment has
            been made.
        is_last_payment (bool): Whether this is the final payment in the simulated
            schedule.
        successful_payment_date (date): Always `null` for simulated payments —
            populated only once a real payment settles.
        terminate_with_status (TerminateWithStatus): The status the subscription
            would transition to on this payment's due date, if a termination is
            scheduled. `null` when no termination applies.
        retry_interval (str): ISO-8601 Duration for the retry interval applied if
            this payment fails (e.g., P5D). `null` if no retry interval is configured.
        additional_properties (Dict[str, Any]): The additional properties for the
            model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "due_date": "due_date",
        "zone_id": "zone_id",
        "amount": "amount",
        "currency": "currency",
        "is_paid": "is_paid",
        "is_last_payment": "is_last_payment",
        "successful_payment_date": "successful_payment_date",
        "terminate_with_status": "terminate_with_status",
        "retry_interval": "retry_interval",
    }

    _optionals = [
        "due_date",
        "zone_id",
        "amount",
        "currency",
        "is_paid",
        "is_last_payment",
        "successful_payment_date",
        "terminate_with_status",
        "retry_interval",
    ]

    _nullables = [
        "successful_payment_date",
        "terminate_with_status",
        "retry_interval",
    ]

    def __init__(
        self,
        due_date=APIHelper.SKIP,
        zone_id=APIHelper.SKIP,
        amount=APIHelper.SKIP,
        currency=APIHelper.SKIP,
        is_paid=APIHelper.SKIP,
        is_last_payment=APIHelper.SKIP,
        successful_payment_date=APIHelper.SKIP,
        terminate_with_status=APIHelper.SKIP,
        retry_interval=APIHelper.SKIP,
        additional_properties=None):
        """Initialize a SubscriptionSimulationPayment instance."""
        # Initialize members of the class
        if due_date is not APIHelper.SKIP:
            self.due_date = due_date
        if zone_id is not APIHelper.SKIP:
            self.zone_id = zone_id
        if amount is not APIHelper.SKIP:
            self.amount = amount
        if currency is not APIHelper.SKIP:
            self.currency = currency
        if is_paid is not APIHelper.SKIP:
            self.is_paid = is_paid
        if is_last_payment is not APIHelper.SKIP:
            self.is_last_payment = is_last_payment
        if successful_payment_date is not APIHelper.SKIP:
            self.successful_payment_date = successful_payment_date
        if terminate_with_status is not APIHelper.SKIP:
            self.terminate_with_status = terminate_with_status
        if retry_interval is not APIHelper.SKIP:
            self.retry_interval = retry_interval

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
        due_date = dateutil.parser.parse(
            dictionary.get("due_date")).date()\
            if dictionary.get("due_date") else APIHelper.SKIP
        zone_id =\
            dictionary.get("zone_id")\
            if dictionary.get("zone_id")\
                else APIHelper.SKIP
        amount =\
            dictionary.get("amount")\
            if dictionary.get("amount")\
                else APIHelper.SKIP
        currency =\
            dictionary.get("currency")\
            if dictionary.get("currency")\
                else APIHelper.SKIP
        is_paid =\
            dictionary.get("is_paid")\
            if "is_paid" in dictionary.keys()\
                else APIHelper.SKIP
        is_last_payment =\
            dictionary.get("is_last_payment")\
            if "is_last_payment" in dictionary.keys()\
                else APIHelper.SKIP
        if "successful_payment_date" in dictionary.keys():
            successful_payment_date = dateutil.parser.parse(
                dictionary.get("successful_payment_date")).date()\
                if dictionary.get("successful_payment_date") else None

        else:
            successful_payment_date = APIHelper.SKIP
        terminate_with_status =\
            dictionary.get("terminate_with_status")\
            if "terminate_with_status" in dictionary.keys()\
                else APIHelper.SKIP
        retry_interval =\
            dictionary.get("retry_interval")\
            if "retry_interval" in dictionary.keys()\
                else APIHelper.SKIP

        additional_properties = APIHelper.get_additional_properties(
            dictionary={k: v for k, v in dictionary.items()
                        if k not in cls._names.values()},
            unboxing_function=lambda value: value)

        # Return an object of this model
        return cls(due_date,
                   zone_id,
                   amount,
                   currency,
                   is_paid,
                   is_last_payment,
                   successful_payment_date,
                   terminate_with_status,
                   retry_interval,
                   additional_properties)

    def __repr__(self):
        """Return a unambiguous string representation."""
        _due_date=(
            self.due_date
            if hasattr(self, "due_date")
            else None
        )
        _zone_id=(
            self.zone_id
            if hasattr(self, "zone_id")
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
        _is_paid=(
            self.is_paid
            if hasattr(self, "is_paid")
            else None
        )
        _is_last_payment=(
            self.is_last_payment
            if hasattr(self, "is_last_payment")
            else None
        )
        _successful_payment_date=(
            self.successful_payment_date
            if hasattr(self, "successful_payment_date")
            else None
        )
        _terminate_with_status=(
            self.terminate_with_status
            if hasattr(self, "terminate_with_status")
            else None
        )
        _retry_interval=(
            self.retry_interval
            if hasattr(self, "retry_interval")
            else None
        )
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"due_date={_due_date!r}, "
            f"zone_id={_zone_id!r}, "
            f"amount={_amount!r}, "
            f"currency={_currency!r}, "
            f"is_paid={_is_paid!r}, "
            f"is_last_payment={_is_last_payment!r}, "
            f"successful_payment_date={_successful_payment_date!r}, "
            f"terminate_with_status={_terminate_with_status!r}, "
            f"retry_interval={_retry_interval!r}, "
            f"additional_properties={_additional_properties!r}, "
            f")"
        )

    def __str__(self):
        """Return a human-readable string representation."""
        _due_date=(
            self.due_date
            if hasattr(self, "due_date")
            else None
        )
        _zone_id=(
            self.zone_id
            if hasattr(self, "zone_id")
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
        _is_paid=(
            self.is_paid
            if hasattr(self, "is_paid")
            else None
        )
        _is_last_payment=(
            self.is_last_payment
            if hasattr(self, "is_last_payment")
            else None
        )
        _successful_payment_date=(
            self.successful_payment_date
            if hasattr(self, "successful_payment_date")
            else None
        )
        _terminate_with_status=(
            self.terminate_with_status
            if hasattr(self, "terminate_with_status")
            else None
        )
        _retry_interval=(
            self.retry_interval
            if hasattr(self, "retry_interval")
            else None
        )
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"due_date={_due_date!s}, "
            f"zone_id={_zone_id!s}, "
            f"amount={_amount!s}, "
            f"currency={_currency!s}, "
            f"is_paid={_is_paid!s}, "
            f"is_last_payment={_is_last_payment!s}, "
            f"successful_payment_date={_successful_payment_date!s}, "
            f"terminate_with_status={_terminate_with_status!s}, "
            f"retry_interval={_retry_interval!s}, "
            f"additional_properties={_additional_properties!s}, "
            f")"
        )
