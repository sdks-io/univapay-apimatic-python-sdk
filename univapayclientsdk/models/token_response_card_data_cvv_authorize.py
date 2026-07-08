"""univapay_client_sdk.

This file was automatically generated for Univapay by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

# ruff: noqa: E501
from univapayclientsdk.api_helper import APIHelper


class TokenResponseCardDataCvvAuthorize(object):
    """Implementation of the 'TokenResponseCardDataCvvAuthorize' model.

    Token Response Card Data Cvv Authorize schema.

    Attributes:
        enabled (bool): Enabled value.
        status (str): Current status of the resource.
        charge_id (uuid|str): Charge identifier.
        credentials_id (uuid|str): Credentials identifier.
        currency (str): ISO-4217 currency code.
        additional_properties (Dict[str, Any]): The additional properties for the
            model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "enabled": "enabled",
        "status": "status",
        "charge_id": "charge_id",
        "credentials_id": "credentials_id",
        "currency": "currency",
    }

    _optionals = [
        "enabled",
        "status",
        "charge_id",
        "credentials_id",
        "currency",
    ]

    _nullables = [
        "status",
        "charge_id",
        "credentials_id",
        "currency",
    ]

    def __init__(
        self,
        enabled=APIHelper.SKIP,
        status=APIHelper.SKIP,
        charge_id=APIHelper.SKIP,
        credentials_id=APIHelper.SKIP,
        currency=APIHelper.SKIP,
        additional_properties=None):
        """Initialize a TokenResponseCardDataCvvAuthorize instance."""
        # Initialize members of the class
        if enabled is not APIHelper.SKIP:
            self.enabled = enabled
        if status is not APIHelper.SKIP:
            self.status = status
        if charge_id is not APIHelper.SKIP:
            self.charge_id = charge_id
        if credentials_id is not APIHelper.SKIP:
            self.credentials_id = credentials_id
        if currency is not APIHelper.SKIP:
            self.currency = currency

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
            if "status" in dictionary.keys()\
                else APIHelper.SKIP
        charge_id =\
            dictionary.get("charge_id")\
            if "charge_id" in dictionary.keys()\
                else APIHelper.SKIP
        credentials_id =\
            dictionary.get("credentials_id")\
            if "credentials_id" in dictionary.keys()\
                else APIHelper.SKIP
        currency =\
            dictionary.get("currency")\
            if "currency" in dictionary.keys()\
                else APIHelper.SKIP

        additional_properties = APIHelper.get_additional_properties(
            dictionary={k: v for k, v in dictionary.items()
                        if k not in cls._names.values()},
            unboxing_function=lambda value: value)

        # Return an object of this model
        return cls(enabled,
                   status,
                   charge_id,
                   credentials_id,
                   currency,
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
        _charge_id=(
            self.charge_id
            if hasattr(self, "charge_id")
            else None
        )
        _credentials_id=(
            self.credentials_id
            if hasattr(self, "credentials_id")
            else None
        )
        _currency=(
            self.currency
            if hasattr(self, "currency")
            else None
        )
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"enabled={_enabled!r}, "
            f"status={_status!r}, "
            f"charge_id={_charge_id!r}, "
            f"credentials_id={_credentials_id!r}, "
            f"currency={_currency!r}, "
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
        _charge_id=(
            self.charge_id
            if hasattr(self, "charge_id")
            else None
        )
        _credentials_id=(
            self.credentials_id
            if hasattr(self, "credentials_id")
            else None
        )
        _currency=(
            self.currency
            if hasattr(self, "currency")
            else None
        )
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"enabled={_enabled!s}, "
            f"status={_status!s}, "
            f"charge_id={_charge_id!s}, "
            f"credentials_id={_credentials_id!s}, "
            f"currency={_currency!s}, "
            f"additional_properties={_additional_properties!s}, "
            f")"
        )
