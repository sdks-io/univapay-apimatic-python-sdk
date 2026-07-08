"""univapay_client_sdk.

This file was automatically generated for Univapay by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

# ruff: noqa: E501
from univapayclientsdk.api_helper import APIHelper


class TokenResponseOnlineData(object):
    """Implementation of the 'TokenResponseOnlineData' model.

    Token Response Online Data schema.

    Attributes:
        brand (BaseOnlineDataBrand): Base Online Data Brand schema.
        call_method (BaseOnlineDataCallMethod): Base Online Data Call Method schema.
        os_type (BaseOnlineDataOsType): Base Online Data Os Type schema.
        user_identifier (str): Consumer specific identifier required by some gateways
            for fraud prevention.
        user_identifier_source (BaseOnlineDataUserIdentifierSource): The source of
            the user identifier
        issuer_token (str): Token provided by the issuer (if applicable).
        issuer_token_payload (str): Additional payload from the issuer.
        additional_properties (Dict[str, Any]): The additional properties for the
            model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "brand": "brand",
        "call_method": "call_method",
        "os_type": "os_type",
        "user_identifier": "user_identifier",
        "user_identifier_source": "user_identifier_source",
        "issuer_token": "issuer_token",
        "issuer_token_payload": "issuer_token_payload",
    }

    _optionals = [
        "brand",
        "call_method",
        "os_type",
        "user_identifier",
        "user_identifier_source",
        "issuer_token",
        "issuer_token_payload",
    ]

    _nullables = [
        "os_type",
        "user_identifier",
        "user_identifier_source",
        "issuer_token",
        "issuer_token_payload",
    ]

    def __init__(
        self,
        brand=APIHelper.SKIP,
        call_method=APIHelper.SKIP,
        os_type=APIHelper.SKIP,
        user_identifier=APIHelper.SKIP,
        user_identifier_source=APIHelper.SKIP,
        issuer_token=APIHelper.SKIP,
        issuer_token_payload=APIHelper.SKIP,
        additional_properties=None):
        """Initialize a TokenResponseOnlineData instance."""
        # Initialize members of the class
        if brand is not APIHelper.SKIP:
            self.brand = brand
        if call_method is not APIHelper.SKIP:
            self.call_method = call_method
        if os_type is not APIHelper.SKIP:
            self.os_type = os_type
        if user_identifier is not APIHelper.SKIP:
            self.user_identifier = user_identifier
        if user_identifier_source is not APIHelper.SKIP:
            self.user_identifier_source = user_identifier_source
        if issuer_token is not APIHelper.SKIP:
            self.issuer_token = issuer_token
        if issuer_token_payload is not APIHelper.SKIP:
            self.issuer_token_payload = issuer_token_payload

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
        brand =\
            dictionary.get("brand")\
            if dictionary.get("brand")\
                else APIHelper.SKIP
        call_method =\
            dictionary.get("call_method")\
            if dictionary.get("call_method")\
                else APIHelper.SKIP
        os_type =\
            dictionary.get("os_type")\
            if "os_type" in dictionary.keys()\
                else APIHelper.SKIP
        user_identifier =\
            dictionary.get("user_identifier")\
            if "user_identifier" in dictionary.keys()\
                else APIHelper.SKIP
        user_identifier_source =\
            dictionary.get("user_identifier_source")\
            if "user_identifier_source" in dictionary.keys()\
                else APIHelper.SKIP
        issuer_token =\
            dictionary.get("issuer_token")\
            if "issuer_token" in dictionary.keys()\
                else APIHelper.SKIP
        issuer_token_payload =\
            dictionary.get("issuer_token_payload")\
            if "issuer_token_payload" in dictionary.keys()\
                else APIHelper.SKIP

        additional_properties = APIHelper.get_additional_properties(
            dictionary={k: v for k, v in dictionary.items()
                        if k not in cls._names.values()},
            unboxing_function=lambda value: value)

        # Return an object of this model
        return cls(brand,
                   call_method,
                   os_type,
                   user_identifier,
                   user_identifier_source,
                   issuer_token,
                   issuer_token_payload,
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
        _brand=(
            self.brand
            if hasattr(self, "brand")
            else None
        )
        _call_method=(
            self.call_method
            if hasattr(self, "call_method")
            else None
        )
        _os_type=(
            self.os_type
            if hasattr(self, "os_type")
            else None
        )
        _user_identifier=(
            self.user_identifier
            if hasattr(self, "user_identifier")
            else None
        )
        _user_identifier_source=(
            self.user_identifier_source
            if hasattr(self, "user_identifier_source")
            else None
        )
        _issuer_token=(
            self.issuer_token
            if hasattr(self, "issuer_token")
            else None
        )
        _issuer_token_payload=(
            self.issuer_token_payload
            if hasattr(self, "issuer_token_payload")
            else None
        )
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"brand={_brand!r}, "
            f"call_method={_call_method!r}, "
            f"os_type={_os_type!r}, "
            f"user_identifier={_user_identifier!r}, "
            f"user_identifier_source={_user_identifier_source!r}, "
            f"issuer_token={_issuer_token!r}, "
            f"issuer_token_payload={_issuer_token_payload!r}, "
            f"additional_properties={_additional_properties!r}, "
            f")"
        )

    def __str__(self):
        """Return a human-readable string representation."""
        _brand=(
            self.brand
            if hasattr(self, "brand")
            else None
        )
        _call_method=(
            self.call_method
            if hasattr(self, "call_method")
            else None
        )
        _os_type=(
            self.os_type
            if hasattr(self, "os_type")
            else None
        )
        _user_identifier=(
            self.user_identifier
            if hasattr(self, "user_identifier")
            else None
        )
        _user_identifier_source=(
            self.user_identifier_source
            if hasattr(self, "user_identifier_source")
            else None
        )
        _issuer_token=(
            self.issuer_token
            if hasattr(self, "issuer_token")
            else None
        )
        _issuer_token_payload=(
            self.issuer_token_payload
            if hasattr(self, "issuer_token_payload")
            else None
        )
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"brand={_brand!s}, "
            f"call_method={_call_method!s}, "
            f"os_type={_os_type!s}, "
            f"user_identifier={_user_identifier!s}, "
            f"user_identifier_source={_user_identifier_source!s}, "
            f"issuer_token={_issuer_token!s}, "
            f"issuer_token_payload={_issuer_token_payload!s}, "
            f"additional_properties={_additional_properties!s}, "
            f")"
        )
