"""univapay_client_sdk.

This file was automatically generated for Univapay by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

# ruff: noqa: E501
from univapayclientsdk.api_helper import APIHelper


class RestrictIpAfterFailedChargeConfig(object):
    """Implementation of the 'RestrictIpAfterFailedChargeConfig' model.

    IP restriction policy applied after repeated failed charges.

    Attributes:
        enabled (bool): Enables temporary IP restrictions after repeated failures.
        count (int): Number of failed charges allowed before restriction starts.
        cooldown (str): ISO-8601 duration that the IP restriction remains active.
        additional_properties (Dict[str, Any]): The additional properties for the
            model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "enabled": "enabled",
        "count": "count",
        "cooldown": "cooldown",
    }

    _optionals = [
        "enabled",
        "count",
        "cooldown",
    ]

    _nullables = [
        "enabled",
        "count",
        "cooldown",
    ]

    def __init__(
        self,
        enabled=APIHelper.SKIP,
        count=APIHelper.SKIP,
        cooldown=APIHelper.SKIP,
        additional_properties=None):
        """Initialize a RestrictIpAfterFailedChargeConfig instance."""
        # Initialize members of the class
        if enabled is not APIHelper.SKIP:
            self.enabled = enabled
        if count is not APIHelper.SKIP:
            self.count = count
        if cooldown is not APIHelper.SKIP:
            self.cooldown = cooldown

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
        enabled =\
            dictionary.get("enabled")\
            if "enabled" in dictionary.keys()\
                else APIHelper.SKIP
        count =\
            dictionary.get("count")\
            if "count" in dictionary.keys()\
                else APIHelper.SKIP
        cooldown =\
            dictionary.get("cooldown")\
            if "cooldown" in dictionary.keys()\
                else APIHelper.SKIP

        additional_properties = APIHelper.get_additional_properties(
            dictionary={k: v for k, v in dictionary.items()
                        if k not in cls._names.values()},
            unboxing_function=lambda value: value)

        # Return an object of this model
        return cls(enabled,
                   count,
                   cooldown,
                   additional_properties)

    def __repr__(self):
        """Return a unambiguous string representation."""
        _enabled=(
            self.enabled
            if hasattr(self, "enabled")
            else None
        )
        _count=(
            self.count
            if hasattr(self, "count")
            else None
        )
        _cooldown=(
            self.cooldown
            if hasattr(self, "cooldown")
            else None
        )
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"enabled={_enabled!r}, "
            f"count={_count!r}, "
            f"cooldown={_cooldown!r}, "
            f"additional_properties={_additional_properties!r}, "
            f")"
        )

    def __str__(self):
        """Return a human-readable string representation."""
        _enabled=(
            self.enabled
            if hasattr(self, "enabled")
            else None
        )
        _count=(
            self.count
            if hasattr(self, "count")
            else None
        )
        _cooldown=(
            self.cooldown
            if hasattr(self, "cooldown")
            else None
        )
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"enabled={_enabled!s}, "
            f"count={_count!s}, "
            f"cooldown={_cooldown!s}, "
            f"additional_properties={_additional_properties!s}, "
            f")"
        )
