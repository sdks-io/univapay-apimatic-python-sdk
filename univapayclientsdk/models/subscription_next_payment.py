"""univapay_client_sdk.

This file was automatically generated for Univapay by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

# ruff: noqa: E501
import dateutil.parser

from univapayclientsdk.api_helper import APIHelper


class SubscriptionNextPayment(object):
    """Implementation of the 'SubscriptionNextPayment' model.

    Next scheduled payment details for a subscription.

    Attributes:
        id (uuid|str): Unique identifier.
        due_date (date): Scheduled due date.
        zone_id (str): IANA timezone identifier.
        amount (int): Amount in the smallest currency unit.
        currency (str): ISO-4217 currency code.
        amount_formatted (float): Amount formatted for display.
        is_paid (bool): Whether the payment has been paid.
        is_last_payment (bool): Whether this is the final payment in the schedule.
        created_on (datetime): Timestamp when the resource was created.
        updated_on (datetime): Timestamp when the resource was last updated.
        retry_date (date): Scheduled retry date.
        terminate_with_status (SubscriptionTerminateWithStatus): Schedule a status
            transition on a payment's due date. Set to `suspended` or `canceled` to
            schedule termination. Send `null` to cancel a previously scheduled
            transition.
        additional_properties (Dict[str, Any]): The additional properties for the
            model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "id": "id",
        "due_date": "due_date",
        "zone_id": "zone_id",
        "amount": "amount",
        "currency": "currency",
        "amount_formatted": "amount_formatted",
        "is_paid": "is_paid",
        "is_last_payment": "is_last_payment",
        "created_on": "created_on",
        "updated_on": "updated_on",
        "retry_date": "retry_date",
        "terminate_with_status": "terminate_with_status",
    }

    _optionals = [
        "id",
        "due_date",
        "zone_id",
        "amount",
        "currency",
        "amount_formatted",
        "is_paid",
        "is_last_payment",
        "created_on",
        "updated_on",
        "retry_date",
        "terminate_with_status",
    ]

    _nullables = [
        "retry_date",
        "terminate_with_status",
    ]

    def __init__(
        self,
        id=APIHelper.SKIP,
        due_date=APIHelper.SKIP,
        zone_id=APIHelper.SKIP,
        amount=APIHelper.SKIP,
        currency=APIHelper.SKIP,
        amount_formatted=APIHelper.SKIP,
        is_paid=APIHelper.SKIP,
        is_last_payment=APIHelper.SKIP,
        created_on=APIHelper.SKIP,
        updated_on=APIHelper.SKIP,
        retry_date=APIHelper.SKIP,
        terminate_with_status=APIHelper.SKIP,
        additional_properties=None):
        """Initialize a SubscriptionNextPayment instance."""
        # Initialize members of the class
        if id is not APIHelper.SKIP:
            self.id = id
        if due_date is not APIHelper.SKIP:
            self.due_date = due_date
        if zone_id is not APIHelper.SKIP:
            self.zone_id = zone_id
        if amount is not APIHelper.SKIP:
            self.amount = amount
        if currency is not APIHelper.SKIP:
            self.currency = currency
        if amount_formatted is not APIHelper.SKIP:
            self.amount_formatted = amount_formatted
        if is_paid is not APIHelper.SKIP:
            self.is_paid = is_paid
        if is_last_payment is not APIHelper.SKIP:
            self.is_last_payment = is_last_payment
        if created_on is not APIHelper.SKIP:
            self.created_on =\
                 APIHelper.apply_datetime_converter(
                created_on, APIHelper.RFC3339DateTime)\
                 if created_on else None
        if updated_on is not APIHelper.SKIP:
            self.updated_on =\
                 APIHelper.apply_datetime_converter(
                updated_on, APIHelper.RFC3339DateTime)\
                 if updated_on else None
        if retry_date is not APIHelper.SKIP:
            self.retry_date = retry_date
        if terminate_with_status is not APIHelper.SKIP:
            self.terminate_with_status = terminate_with_status

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
        amount_formatted =\
            dictionary.get("amount_formatted")\
            if dictionary.get("amount_formatted")\
                else APIHelper.SKIP
        is_paid =\
            dictionary.get("is_paid")\
            if "is_paid" in dictionary.keys()\
                else APIHelper.SKIP
        is_last_payment =\
            dictionary.get("is_last_payment")\
            if "is_last_payment" in dictionary.keys()\
                else APIHelper.SKIP
        created_on = APIHelper.RFC3339DateTime.from_value(
            dictionary.get("created_on")).datetime\
            if dictionary.get("created_on") else APIHelper.SKIP
        updated_on = APIHelper.RFC3339DateTime.from_value(
            dictionary.get("updated_on")).datetime\
            if dictionary.get("updated_on") else APIHelper.SKIP
        if "retry_date" in dictionary.keys():
            retry_date = dateutil.parser.parse(
                dictionary.get("retry_date")).date()\
                if dictionary.get("retry_date") else None

        else:
            retry_date = APIHelper.SKIP
        terminate_with_status =\
            dictionary.get("terminate_with_status")\
            if "terminate_with_status" in dictionary.keys()\
                else APIHelper.SKIP

        additional_properties = APIHelper.get_additional_properties(
            dictionary={k: v for k, v in dictionary.items()
                        if k not in cls._names.values()},
            unboxing_function=lambda value: value)

        # Return an object of this model
        return cls(id,
                   due_date,
                   zone_id,
                   amount,
                   currency,
                   amount_formatted,
                   is_paid,
                   is_last_payment,
                   created_on,
                   updated_on,
                   retry_date,
                   terminate_with_status,
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
        _amount_formatted=(
            self.amount_formatted
            if hasattr(self, "amount_formatted")
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
        _created_on=(
            self.created_on
            if hasattr(self, "created_on")
            else None
        )
        _updated_on=(
            self.updated_on
            if hasattr(self, "updated_on")
            else None
        )
        _retry_date=(
            self.retry_date
            if hasattr(self, "retry_date")
            else None
        )
        _terminate_with_status=(
            self.terminate_with_status
            if hasattr(self, "terminate_with_status")
            else None
        )
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"id={_id!r}, "
            f"due_date={_due_date!r}, "
            f"zone_id={_zone_id!r}, "
            f"amount={_amount!r}, "
            f"currency={_currency!r}, "
            f"amount_formatted={_amount_formatted!r}, "
            f"is_paid={_is_paid!r}, "
            f"is_last_payment={_is_last_payment!r}, "
            f"created_on={_created_on!r}, "
            f"updated_on={_updated_on!r}, "
            f"retry_date={_retry_date!r}, "
            f"terminate_with_status={_terminate_with_status!r}, "
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
        _amount_formatted=(
            self.amount_formatted
            if hasattr(self, "amount_formatted")
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
        _created_on=(
            self.created_on
            if hasattr(self, "created_on")
            else None
        )
        _updated_on=(
            self.updated_on
            if hasattr(self, "updated_on")
            else None
        )
        _retry_date=(
            self.retry_date
            if hasattr(self, "retry_date")
            else None
        )
        _terminate_with_status=(
            self.terminate_with_status
            if hasattr(self, "terminate_with_status")
            else None
        )
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"id={_id!s}, "
            f"due_date={_due_date!s}, "
            f"zone_id={_zone_id!s}, "
            f"amount={_amount!s}, "
            f"currency={_currency!s}, "
            f"amount_formatted={_amount_formatted!s}, "
            f"is_paid={_is_paid!s}, "
            f"is_last_payment={_is_last_payment!s}, "
            f"created_on={_created_on!s}, "
            f"updated_on={_updated_on!s}, "
            f"retry_date={_retry_date!s}, "
            f"terminate_with_status={_terminate_with_status!s}, "
            f"additional_properties={_additional_properties!s}, "
            f")"
        )
