"""univapay_client_sdk.

This file was automatically generated for Univapay by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

# ruff: noqa: E501
import dateutil.parser

from univapayclientsdk.api_helper import APIHelper


class SubscriptionUpdateScheduleSettings(object):
    """Implementation of the 'SubscriptionUpdateScheduleSettings' model.

    Schedule settings that can be updated on a subscription.

    Attributes:
        termination_mode (SubscriptionTerminationMode): Subscription Termination Mode
            schema.
        start_on (date): Subscription start date (YYYY-MM-DD). Used to change the
            first actual charge date for subscriptions that initially only registered
            a payment method. Must be in the future; only available before the
            subscription has more than one paid payment.
        preserve_end_of_month (bool): If true, subsequent charges will always occur
            on the last day of the month.
        retry_interval (str): ISO-8601 Duration for retry interval if payment fails
            (e.g., P3D for 3 days, PT48H for 48 hours).
        additional_properties (Dict[str, Any]): The additional properties for the
            model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "termination_mode": "termination_mode",
        "start_on": "start_on",
        "preserve_end_of_month": "preserve_end_of_month",
        "retry_interval": "retry_interval",
    }

    _optionals = [
        "termination_mode",
        "start_on",
        "preserve_end_of_month",
        "retry_interval",
    ]

    def __init__(
        self,
        termination_mode="immediate",
        start_on=APIHelper.SKIP,
        preserve_end_of_month=APIHelper.SKIP,
        retry_interval=APIHelper.SKIP,
        additional_properties=None):
        """Initialize a SubscriptionUpdateScheduleSettings instance."""
        # Initialize members of the class
        self.termination_mode = termination_mode
        if start_on is not APIHelper.SKIP:
            self.start_on = start_on
        if preserve_end_of_month is not APIHelper.SKIP:
            self.preserve_end_of_month = preserve_end_of_month
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
        termination_mode =\
            dictionary.get("termination_mode")\
            if dictionary.get("termination_mode")\
                else "immediate"
        start_on = dateutil.parser.parse(
            dictionary.get("start_on")).date()\
            if dictionary.get("start_on") else APIHelper.SKIP
        preserve_end_of_month =\
            dictionary.get("preserve_end_of_month")\
            if "preserve_end_of_month" in dictionary.keys()\
                else APIHelper.SKIP
        retry_interval =\
            dictionary.get("retry_interval")\
            if dictionary.get("retry_interval")\
                else APIHelper.SKIP

        additional_properties = APIHelper.get_additional_properties(
            dictionary={k: v for k, v in dictionary.items()
                        if k not in cls._names.values()},
            unboxing_function=lambda value: value)

        # Return an object of this model
        return cls(termination_mode,
                   start_on,
                   preserve_end_of_month,
                   retry_interval,
                   additional_properties)

    def __repr__(self):
        """Return a unambiguous string representation."""
        _termination_mode=(
            self.termination_mode
            if hasattr(self, "termination_mode")
            else None
        )
        _start_on=(
            self.start_on
            if hasattr(self, "start_on")
            else None
        )
        _preserve_end_of_month=(
            self.preserve_end_of_month
            if hasattr(self, "preserve_end_of_month")
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
            f"termination_mode={_termination_mode!r}, "
            f"start_on={_start_on!r}, "
            f"preserve_end_of_month={_preserve_end_of_month!r}, "
            f"retry_interval={_retry_interval!r}, "
            f"additional_properties={_additional_properties!r}, "
            f")"
        )

    def __str__(self):
        """Return a human-readable string representation."""
        _termination_mode=(
            self.termination_mode
            if hasattr(self, "termination_mode")
            else None
        )
        _start_on=(
            self.start_on
            if hasattr(self, "start_on")
            else None
        )
        _preserve_end_of_month=(
            self.preserve_end_of_month
            if hasattr(self, "preserve_end_of_month")
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
            f"termination_mode={_termination_mode!s}, "
            f"start_on={_start_on!s}, "
            f"preserve_end_of_month={_preserve_end_of_month!s}, "
            f"retry_interval={_retry_interval!s}, "
            f"additional_properties={_additional_properties!s}, "
            f")"
        )
