"""univapay_client_sdk.

This file was automatically generated for Univapay by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

# ruff: noqa: E501
from univapayclientsdk.api_helper import APIHelper


class ApiErrorDetail(object):
    """Implementation of the 'ApiErrorDetail' model.

    Structured detail entry describing a single API validation or business error.

    Attributes:
        field (str): The field name of the parameter that caused the error
            (lower_snake_case).
        reason (str): Detailed reason for the nested error (UPPER_SNAKE_CASE or
            English description).
        additional_properties (Dict[str, Any]): The additional properties for the
            model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "field": "field",
        "reason": "reason",
    }

    _optionals = [
        "field",
        "reason",
    ]

    def __init__(
        self,
        field=APIHelper.SKIP,
        reason=APIHelper.SKIP,
        additional_properties=None):
        """Initialize a ApiErrorDetail instance."""
        # Initialize members of the class
        if field is not APIHelper.SKIP:
            self.field = field
        if reason is not APIHelper.SKIP:
            self.reason = reason

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
        field =\
            dictionary.get("field")\
            if dictionary.get("field")\
                else APIHelper.SKIP
        reason =\
            dictionary.get("reason")\
            if dictionary.get("reason")\
                else APIHelper.SKIP

        additional_properties = APIHelper.get_additional_properties(
            dictionary={k: v for k, v in dictionary.items()
                        if k not in cls._names.values()},
            unboxing_function=lambda value: value)

        # Return an object of this model
        return cls(field,
                   reason,
                   additional_properties)

    def __repr__(self):
        """Return a unambiguous string representation."""
        _field=(
            self.field
            if hasattr(self, "field")
            else None
        )
        _reason=(
            self.reason
            if hasattr(self, "reason")
            else None
        )
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"field={_field!r}, "
            f"reason={_reason!r}, "
            f"additional_properties={_additional_properties!r}, "
            f")"
        )

    def __str__(self):
        """Return a human-readable string representation."""
        _field=(
            self.field
            if hasattr(self, "field")
            else None
        )
        _reason=(
            self.reason
            if hasattr(self, "reason")
            else None
        )
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"field={_field!s}, "
            f"reason={_reason!s}, "
            f"additional_properties={_additional_properties!s}, "
            f")"
        )
