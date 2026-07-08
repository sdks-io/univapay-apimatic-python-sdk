"""univapay_client_sdk.

This file was automatically generated for Univapay by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

# ruff: noqa: E501
from univapayclientsdk.api_helper import APIHelper


class SuspendScheduleSettings(object):
    """Implementation of the 'SuspendScheduleSettings' model.

    Schedule-related settings.

    Attributes:
        termination_mode (SubscriptionTerminationMode): Subscription Termination Mode
            schema.
        additional_properties (Dict[str, Any]): The additional properties for the
            model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "termination_mode": "termination_mode",
    }

    _optionals = [
        "termination_mode",
    ]

    def __init__(
        self,
        termination_mode="immediate",
        additional_properties=None):
        """Initialize a SuspendScheduleSettings instance."""
        # Initialize members of the class
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
        termination_mode =\
            dictionary.get("termination_mode")\
            if dictionary.get("termination_mode")\
                else "immediate"

        additional_properties = APIHelper.get_additional_properties(
            dictionary={k: v for k, v in dictionary.items()
                        if k not in cls._names.values()},
            unboxing_function=lambda value: value)

        # Return an object of this model
        return cls(termination_mode,
                   additional_properties)

    def __repr__(self):
        """Return a unambiguous string representation."""
        _termination_mode=(
            self.termination_mode
            if hasattr(self, "termination_mode")
            else None
        )
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"termination_mode={_termination_mode!r}, "
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
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"termination_mode={_termination_mode!s}, "
            f"additional_properties={_additional_properties!s}, "
            f")"
        )
