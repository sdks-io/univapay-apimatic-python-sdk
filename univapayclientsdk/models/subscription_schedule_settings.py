"""univapay_client_sdk.

This file was automatically generated for Univapay by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

# ruff: noqa: E501
import dateutil.parser

from univapayclientsdk.api_helper import APIHelper


class SubscriptionScheduleSettings(object):
    """Implementation of the 'SubscriptionScheduleSettings' model.

    Schedule settings applied to a subscription.

    Attributes:
        start_on (date): Date when the recurring schedule starts (YYYY-MM-DD).
        zone_id (str): IANA Timezone ID.
        preserve_end_of_month (bool): If true, subsequent charges will always occur
            on the last day of the month.
        retry_interval (str): ISO-8601 Duration for retry interval if payment fails
            (e.g., P5D).
        termination_mode (SubscriptionTerminationMode): Subscription Termination Mode
            schema.
        additional_properties (Dict[str, Any]): The additional properties for the
            model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "start_on": "start_on",
        "zone_id": "zone_id",
        "preserve_end_of_month": "preserve_end_of_month",
        "retry_interval": "retry_interval",
        "termination_mode": "termination_mode",
    }

    _optionals = [
        "start_on",
        "zone_id",
        "preserve_end_of_month",
        "retry_interval",
        "termination_mode",
    ]

    def __init__(
        self,
        start_on=APIHelper.SKIP,
        zone_id=APIHelper.SKIP,
        preserve_end_of_month=APIHelper.SKIP,
        retry_interval=APIHelper.SKIP,
        termination_mode="immediate",
        additional_properties=None):
        """Initialize a SubscriptionScheduleSettings instance."""
        # Initialize members of the class
        if start_on is not APIHelper.SKIP:
            self.start_on = start_on
        if zone_id is not APIHelper.SKIP:
            self.zone_id = zone_id
        if preserve_end_of_month is not APIHelper.SKIP:
            self.preserve_end_of_month = preserve_end_of_month
        if retry_interval is not APIHelper.SKIP:
            self.retry_interval = retry_interval
        self.termination_mode = termination_mode

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
        start_on = dateutil.parser.parse(
            dictionary.get("start_on")).date()\
            if dictionary.get("start_on") else APIHelper.SKIP
        zone_id =\
            dictionary.get("zone_id")\
            if dictionary.get("zone_id")\
                else APIHelper.SKIP
        preserve_end_of_month =\
            dictionary.get("preserve_end_of_month")\
            if "preserve_end_of_month" in dictionary.keys()\
                else APIHelper.SKIP
        retry_interval =\
            dictionary.get("retry_interval")\
            if dictionary.get("retry_interval")\
                else APIHelper.SKIP
        termination_mode =\
            dictionary.get("termination_mode")\
            if dictionary.get("termination_mode")\
                else "immediate"

        additional_properties = APIHelper.get_additional_properties(
            dictionary={k: v for k, v in dictionary.items()
                        if k not in cls._names.values()},
            unboxing_function=lambda value: value)

        # Return an object of this model
        return cls(start_on,
                   zone_id,
                   preserve_end_of_month,
                   retry_interval,
                   termination_mode,
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
        _start_on=(
            self.start_on
            if hasattr(self, "start_on")
            else None
        )
        _zone_id=(
            self.zone_id
            if hasattr(self, "zone_id")
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
        _termination_mode=(
            self.termination_mode
            if hasattr(self, "termination_mode")
            else None
        )
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"start_on={_start_on!r}, "
            f"zone_id={_zone_id!r}, "
            f"preserve_end_of_month={_preserve_end_of_month!r}, "
            f"retry_interval={_retry_interval!r}, "
            f"termination_mode={_termination_mode!r}, "
            f"additional_properties={_additional_properties!r}, "
            f")"
        )

    def __str__(self):
        """Return a human-readable string representation."""
        _start_on=(
            self.start_on
            if hasattr(self, "start_on")
            else None
        )
        _zone_id=(
            self.zone_id
            if hasattr(self, "zone_id")
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
        _termination_mode=(
            self.termination_mode
            if hasattr(self, "termination_mode")
            else None
        )
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"start_on={_start_on!s}, "
            f"zone_id={_zone_id!s}, "
            f"preserve_end_of_month={_preserve_end_of_month!s}, "
            f"retry_interval={_retry_interval!s}, "
            f"termination_mode={_termination_mode!s}, "
            f"additional_properties={_additional_properties!s}, "
            f")"
        )
