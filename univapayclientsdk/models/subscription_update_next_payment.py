"""univapay_client_sdk.

This file was automatically generated for Univapay by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

# ruff: noqa: E501
import dateutil.parser

from univapayclientsdk.api_helper import APIHelper


class SubscriptionUpdateNextPayment(object):
    """Implementation of the 'SubscriptionUpdateNextPayment' model.

    Fields that can be updated on the next scheduled payment.

    Attributes:
        due_date (date): Next payment date (YYYY-MM-DD).  Note: Only available for
            merchants permitted to edit next payment dates.
        amount (int): Next payment amount. Not available for limited-cycle
            subscriptions.  Only available for permitted merchants.  This does not
            change subsequent cycle amounts.
        terminate_with_status (SubscriptionTerminateWithStatus): Schedule a status
            transition on a payment's due date. Set to `suspended` or `canceled` to
            schedule termination. Send `null` to cancel a previously scheduled
            transition.
        additional_properties (Dict[str, Any]): The additional properties for the
            model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "due_date": "due_date",
        "amount": "amount",
        "terminate_with_status": "terminate_with_status",
    }

    _optionals = [
        "due_date",
        "amount",
        "terminate_with_status",
    ]

    _nullables = [
        "terminate_with_status",
    ]

    def __init__(
        self,
        due_date=APIHelper.SKIP,
        amount=APIHelper.SKIP,
        terminate_with_status=APIHelper.SKIP,
        additional_properties=None):
        """Initialize a SubscriptionUpdateNextPayment instance."""
        # Initialize members of the class
        if due_date is not APIHelper.SKIP:
            self.due_date = due_date
        if amount is not APIHelper.SKIP:
            self.amount = amount
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
        due_date = dateutil.parser.parse(
            dictionary.get("due_date")).date()\
            if dictionary.get("due_date") else APIHelper.SKIP
        amount =\
            dictionary.get("amount")\
            if dictionary.get("amount")\
                else APIHelper.SKIP
        terminate_with_status =\
            dictionary.get("terminate_with_status")\
            if "terminate_with_status" in dictionary.keys()\
                else APIHelper.SKIP

        additional_properties = APIHelper.get_additional_properties(
            dictionary={k: v for k, v in dictionary.items()
                        if k not in cls._names.values()},
            unboxing_function=lambda value: value)

        # Return an object of this model
        return cls(due_date,
                   amount,
                   terminate_with_status,
                   additional_properties)

    def __repr__(self):
        """Return a unambiguous string representation."""
        _due_date=(
            self.due_date
            if hasattr(self, "due_date")
            else None
        )
        _amount=(
            self.amount
            if hasattr(self, "amount")
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
            f"due_date={_due_date!r}, "
            f"amount={_amount!r}, "
            f"terminate_with_status={_terminate_with_status!r}, "
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
        _amount=(
            self.amount
            if hasattr(self, "amount")
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
            f"due_date={_due_date!s}, "
            f"amount={_amount!s}, "
            f"terminate_with_status={_terminate_with_status!s}, "
            f"additional_properties={_additional_properties!s}, "
            f")"
        )
