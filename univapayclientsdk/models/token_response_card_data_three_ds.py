"""univapay_client_sdk.

This file was automatically generated for Univapay by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

# ruff: noqa: E501
from univapayclientsdk.api_helper import APIHelper
from univapayclientsdk.models.payment_error import (
    PaymentError,
)


class TokenResponseCardDataThreeDs(object):
    """Implementation of the 'TokenResponseCardDataThreeDs' model.

    Token Response Card Data Three Ds schema.

    Attributes:
        enabled (bool): Enabled value.
        status (TokenResponseCardDataThreeDsStatus): Token Response Card Data Three
            Ds Status schema.
        redirect_endpoint (str): Redirect endpoint URL.
        redirect_id (uuid|str): Redirect identifier.
        exempted (bool): Indicates if the 3DS check was exempted. When creating
            charge 3DS check will not be required.
        error (PaymentError): Payment error details, or null if successful.
        additional_properties (Dict[str, Any]): The additional properties for the
            model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "enabled": "enabled",
        "status": "status",
        "redirect_endpoint": "redirect_endpoint",
        "redirect_id": "redirect_id",
        "exempted": "exempted",
        "error": "error",
    }

    _optionals = [
        "enabled",
        "status",
        "redirect_endpoint",
        "redirect_id",
        "exempted",
        "error",
    ]

    _nullables = [
        "redirect_endpoint",
        "redirect_id",
        "error",
    ]

    def __init__(
        self,
        enabled=APIHelper.SKIP,
        status=APIHelper.SKIP,
        redirect_endpoint=APIHelper.SKIP,
        redirect_id=APIHelper.SKIP,
        exempted=APIHelper.SKIP,
        error=APIHelper.SKIP,
        additional_properties=None):
        """Initialize a TokenResponseCardDataThreeDs instance."""
        # Initialize members of the class
        if enabled is not APIHelper.SKIP:
            self.enabled = enabled
        if status is not APIHelper.SKIP:
            self.status = status
        if redirect_endpoint is not APIHelper.SKIP:
            self.redirect_endpoint = redirect_endpoint
        if redirect_id is not APIHelper.SKIP:
            self.redirect_id = redirect_id
        if exempted is not APIHelper.SKIP:
            self.exempted = exempted
        if error is not APIHelper.SKIP:
            self.error = error

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
        status =\
            dictionary.get("status")\
            if dictionary.get("status")\
                else APIHelper.SKIP
        redirect_endpoint =\
            dictionary.get("redirect_endpoint")\
            if "redirect_endpoint" in dictionary.keys()\
                else APIHelper.SKIP
        redirect_id =\
            dictionary.get("redirect_id")\
            if "redirect_id" in dictionary.keys()\
                else APIHelper.SKIP
        exempted =\
            dictionary.get("exempted")\
            if "exempted" in dictionary.keys()\
                else APIHelper.SKIP
        if "error" in dictionary.keys():
            error =\
                PaymentError.from_dictionary(
                dictionary.get("error"))\
                if dictionary.get("error") else None
        else:
            error = APIHelper.SKIP

        additional_properties = APIHelper.get_additional_properties(
            dictionary={k: v for k, v in dictionary.items()
                        if k not in cls._names.values()},
            unboxing_function=lambda value: value)

        # Return an object of this model
        return cls(enabled,
                   status,
                   redirect_endpoint,
                   redirect_id,
                   exempted,
                   error,
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
        _enabled=(
            self.enabled
            if hasattr(self, "enabled")
            else None
        )
        _status=(
            self.status
            if hasattr(self, "status")
            else None
        )
        _redirect_endpoint=(
            self.redirect_endpoint
            if hasattr(self, "redirect_endpoint")
            else None
        )
        _redirect_id=(
            self.redirect_id
            if hasattr(self, "redirect_id")
            else None
        )
        _exempted=(
            self.exempted
            if hasattr(self, "exempted")
            else None
        )
        _error=(
            self.error
            if hasattr(self, "error")
            else None
        )
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"enabled={_enabled!r}, "
            f"status={_status!r}, "
            f"redirect_endpoint={_redirect_endpoint!r}, "
            f"redirect_id={_redirect_id!r}, "
            f"exempted={_exempted!r}, "
            f"error={_error!r}, "
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
        _status=(
            self.status
            if hasattr(self, "status")
            else None
        )
        _redirect_endpoint=(
            self.redirect_endpoint
            if hasattr(self, "redirect_endpoint")
            else None
        )
        _redirect_id=(
            self.redirect_id
            if hasattr(self, "redirect_id")
            else None
        )
        _exempted=(
            self.exempted
            if hasattr(self, "exempted")
            else None
        )
        _error=(
            self.error
            if hasattr(self, "error")
            else None
        )
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"enabled={_enabled!s}, "
            f"status={_status!s}, "
            f"redirect_endpoint={_redirect_endpoint!s}, "
            f"redirect_id={_redirect_id!s}, "
            f"exempted={_exempted!s}, "
            f"error={_error!s}, "
            f"additional_properties={_additional_properties!s}, "
            f")"
        )
