"""univapay_client_sdk.

This file was automatically generated for Univapay by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

# ruff: noqa: E501
from univapayclientsdk.api_helper import APIHelper
from univapayclientsdk.models.customs_declaration_webhook_other_error import (
    CustomsDeclarationWebhookOtherError,
)


class CustomsDeclarationWebhookError(object):
    """Implementation of the 'CustomsDeclarationWebhookError' model.

    Error payload returned when customs declaration processing fails.

    Attributes:
        code (int): Backend customs declaration error code.
        message (str): Human-readable backend error name.
        details (str): Optional backend-provided detail string.
        others (List[CustomsDeclarationWebhookOtherError]): Additional nested error
            records returned by the backend.
        additional_properties (Dict[str, Any]): The additional properties for the
            model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "code": "code",
        "message": "message",
        "details": "details",
        "others": "others",
    }

    _optionals = [
        "code",
        "message",
        "details",
        "others",
    ]

    _nullables = [
        "details",
        "others",
    ]

    def __init__(
        self,
        code=APIHelper.SKIP,
        message=APIHelper.SKIP,
        details=APIHelper.SKIP,
        others=APIHelper.SKIP,
        additional_properties=None):
        """Initialize a CustomsDeclarationWebhookError instance."""
        # Initialize members of the class
        if code is not APIHelper.SKIP:
            self.code = code
        if message is not APIHelper.SKIP:
            self.message = message
        if details is not APIHelper.SKIP:
            self.details = details
        if others is not APIHelper.SKIP:
            self.others = others

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
        code =\
            dictionary.get("code")\
            if dictionary.get("code")\
                else APIHelper.SKIP
        message =\
            dictionary.get("message")\
            if dictionary.get("message")\
                else APIHelper.SKIP
        details =\
            dictionary.get("details")\
            if "details" in dictionary.keys()\
                else APIHelper.SKIP
        if "others" in dictionary.keys():
            others = [
                CustomsDeclarationWebhookOtherError.from_dictionary(x)
                for x in dictionary.get("others")
            ] if dictionary.get("others") else None
        else:
            others = APIHelper.SKIP

        additional_properties = APIHelper.get_additional_properties(
            dictionary={k: v for k, v in dictionary.items()
                        if k not in cls._names.values()},
            unboxing_function=lambda value: value)

        # Return an object of this model
        return cls(code,
                   message,
                   details,
                   others,
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
        _code=(
            self.code
            if hasattr(self, "code")
            else None
        )
        _message=(
            self.message
            if hasattr(self, "message")
            else None
        )
        _details=(
            self.details
            if hasattr(self, "details")
            else None
        )
        _others=(
            self.others
            if hasattr(self, "others")
            else None
        )
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"code={_code!r}, "
            f"message={_message!r}, "
            f"details={_details!r}, "
            f"others={_others!r}, "
            f"additional_properties={_additional_properties!r}, "
            f")"
        )

    def __str__(self):
        """Return a human-readable string representation."""
        _code=(
            self.code
            if hasattr(self, "code")
            else None
        )
        _message=(
            self.message
            if hasattr(self, "message")
            else None
        )
        _details=(
            self.details
            if hasattr(self, "details")
            else None
        )
        _others=(
            self.others
            if hasattr(self, "others")
            else None
        )
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"code={_code!s}, "
            f"message={_message!s}, "
            f"details={_details!s}, "
            f"others={_others!s}, "
            f"additional_properties={_additional_properties!s}, "
            f")"
        )
