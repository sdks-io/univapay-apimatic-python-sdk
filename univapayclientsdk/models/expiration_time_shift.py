"""univapay_client_sdk.

This file was automatically generated for Univapay by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

# ruff: noqa: E501
from univapayclientsdk.api_helper import APIHelper


class ExpirationTimeShift(object):
    """Implementation of the 'ExpirationTimeShift' model.

    Time-of-day override applied when calculating expirations, shared by
    convenience-store and bank-transfer configuration.

    Attributes:
        value (str): ISO-8601 offset time (HH:mm:ssXXX) that overrides the expiration
            cutoff. Omitted entirely when no override is configured.
        enabled (bool): Whether the time-of-day override is applied.
        additional_properties (Dict[str, Any]): The additional properties for the
            model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "value": "value",
        "enabled": "enabled",
    }

    _optionals = [
        "value",
        "enabled",
    ]

    def __init__(
        self,
        value=APIHelper.SKIP,
        enabled=APIHelper.SKIP,
        additional_properties=None):
        """Initialize a ExpirationTimeShift instance."""
        # Initialize members of the class
        if value is not APIHelper.SKIP:
            self.value = value
        if enabled is not APIHelper.SKIP:
            self.enabled = enabled

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
        value =\
            dictionary.get("value")\
            if dictionary.get("value")\
                else APIHelper.SKIP
        enabled =\
            dictionary.get("enabled")\
            if "enabled" in dictionary.keys()\
                else APIHelper.SKIP

        additional_properties = APIHelper.get_additional_properties(
            dictionary={k: v for k, v in dictionary.items()
                        if k not in cls._names.values()},
            unboxing_function=lambda value: value)

        # Return an object of this model
        return cls(value,
                   enabled,
                   additional_properties)

    def __repr__(self):
        """Return a unambiguous string representation."""
        _value=(
            self.value
            if hasattr(self, "value")
            else None
        )
        _enabled=(
            self.enabled
            if hasattr(self, "enabled")
            else None
        )
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"value={_value!r}, "
            f"enabled={_enabled!r}, "
            f"additional_properties={_additional_properties!r}, "
            f")"
        )

    def __str__(self):
        """Return a human-readable string representation."""
        _value=(
            self.value
            if hasattr(self, "value")
            else None
        )
        _enabled=(
            self.enabled
            if hasattr(self, "enabled")
            else None
        )
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"value={_value!s}, "
            f"enabled={_enabled!s}, "
            f"additional_properties={_additional_properties!s}, "
            f")"
        )
