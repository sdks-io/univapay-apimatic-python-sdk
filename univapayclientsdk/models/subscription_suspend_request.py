"""univapay_client_sdk.

This file was automatically generated for Univapay by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

# ruff: noqa: E501
from univapayclientsdk.api_helper import APIHelper
from univapayclientsdk.models.suspend_schedule_settings import (
    SuspendScheduleSettings,
)


class SubscriptionSuspendRequest(object):
    """Implementation of the 'SubscriptionSuspendRequest' model.

    Request body for suspending a subscription. The
    `schedule_settings.termination_mode`  field controls when the suspension takes
    effect.

    Attributes:
        schedule_settings (SuspendScheduleSettings): Schedule-related settings.
        additional_properties (Dict[str, Any]): The additional properties for the
            model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "schedule_settings": "schedule_settings",
    }

    _optionals = [
        "schedule_settings",
    ]

    def __init__(
        self,
        schedule_settings=APIHelper.SKIP,
        additional_properties=None):
        """Initialize a SubscriptionSuspendRequest instance."""
        # Initialize members of the class
        if schedule_settings is not APIHelper.SKIP:
            self.schedule_settings = schedule_settings

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
        schedule_settings =\
            SuspendScheduleSettings.from_dictionary(
                dictionary.get("schedule_settings"))\
                if "schedule_settings" in dictionary.keys()\
                else APIHelper.SKIP

        additional_properties = APIHelper.get_additional_properties(
            dictionary={k: v for k, v in dictionary.items()
                        if k not in cls._names.values()},
            unboxing_function=lambda value: value)

        # Return an object of this model
        return cls(schedule_settings,
                   additional_properties)

    def __repr__(self):
        """Return a unambiguous string representation."""
        _schedule_settings=(
            self.schedule_settings
            if hasattr(self, "schedule_settings")
            else None
        )
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"schedule_settings={_schedule_settings!r}, "
            f"additional_properties={_additional_properties!r}, "
            f")"
        )

    def __str__(self):
        """Return a human-readable string representation."""
        _schedule_settings=(
            self.schedule_settings
            if hasattr(self, "schedule_settings")
            else None
        )
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"schedule_settings={_schedule_settings!s}, "
            f"additional_properties={_additional_properties!s}, "
            f")"
        )
