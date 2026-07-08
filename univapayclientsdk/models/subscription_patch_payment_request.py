"""univapay_client_sdk.

This file was automatically generated for Univapay by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

# ruff: noqa: E501
import dateutil.parser

from univapayclientsdk.api_helper import APIHelper


class SubscriptionPatchPaymentRequest(object):
    """Implementation of the 'SubscriptionPatchPaymentRequest' model.

    Request body for updating a scheduled payment. All fields are optional. Omitted
    fields are left unchanged.

    Attributes:
        due_date (date): New due date for this payment (YYYY-MM-DD).  Only available
            to merchants with permission to edit payment dates.
        is_paid (bool): Mark this payment as paid. Setting to `true` will trigger
            scheduling  of the next payment in the cycle.
        terminate_with_status (SubscriptionTerminateWithStatus): Schedule a status
            transition on a payment's due date. Set to `suspended` or `canceled` to
            schedule termination. Send `null` to cancel a previously scheduled
            transition.
        retry_interval (str): ISO-8601 Duration override for the retry interval on a
            scheduled payment (for example `P3D`). Send `null` to clear.
        additional_properties (Dict[str, Any]): The additional properties for the
            model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "due_date": "due_date",
        "is_paid": "is_paid",
        "terminate_with_status": "terminate_with_status",
        "retry_interval": "retry_interval",
    }

    _optionals = [
        "due_date",
        "is_paid",
        "terminate_with_status",
        "retry_interval",
    ]

    _nullables = [
        "terminate_with_status",
        "retry_interval",
    ]

    def __init__(
        self,
        due_date=APIHelper.SKIP,
        is_paid=APIHelper.SKIP,
        terminate_with_status=APIHelper.SKIP,
        retry_interval=APIHelper.SKIP,
        additional_properties=None):
        """Initialize a SubscriptionPatchPaymentRequest instance."""
        # Initialize members of the class
        if due_date is not APIHelper.SKIP:
            self.due_date = due_date
        if is_paid is not APIHelper.SKIP:
            self.is_paid = is_paid
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
        is_paid =\
            dictionary.get("is_paid")\
            if "is_paid" in dictionary.keys()\
                else APIHelper.SKIP
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
                   is_paid,
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
        _is_paid=(
            self.is_paid
            if hasattr(self, "is_paid")
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
            f"is_paid={_is_paid!r}, "
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
        _is_paid=(
            self.is_paid
            if hasattr(self, "is_paid")
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
            f"is_paid={_is_paid!s}, "
            f"terminate_with_status={_terminate_with_status!s}, "
            f"retry_interval={_retry_interval!s}, "
            f"additional_properties={_additional_properties!s}, "
            f")"
        )
