"""univapay_client_sdk.

This file was automatically generated for Univapay by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

# ruff: noqa: E501
from univapayclientsdk.api_helper import APIHelper
from univapayclientsdk.models.base_online_data_brand import (
    BaseOnlineDataBrand,
)
from univapayclientsdk.models.base_online_data_call_method import (
    BaseOnlineDataCallMethod,
)


class TokenCreateOnlineData(object):
    """Implementation of the 'TokenCreateOnlineData' model.

    Token Create Online Data schema.

    Attributes:
        brand (BaseOnlineDataBrand): Base Online Data Brand schema.
        call_method (BaseOnlineDataCallMethod): Base Online Data Call Method schema.
        os_type (BaseOnlineDataOsType): Base Online Data Os Type schema.
        user_identifier (str): Consumer specific identifier required by some gateways
            for fraud prevention.
        user_identifier_source (BaseOnlineDataUserIdentifierSource): The source of
            the user identifier
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
    }

    _optionals = [
        "os_type",
        "user_identifier",
        "user_identifier_source",
    ]

    _nullables = [
        "os_type",
        "user_identifier",
        "user_identifier_source",
    ]

    def __init__(
        self,
        brand=None,
        call_method=None,
        os_type=APIHelper.SKIP,
        user_identifier=APIHelper.SKIP,
        user_identifier_source=APIHelper.SKIP,
        additional_properties=None):
        """Initialize a TokenCreateOnlineData instance."""
        # Initialize members of the class
        self.brand = brand
        self.call_method = call_method
        if os_type is not APIHelper.SKIP:
            self.os_type = os_type
        if user_identifier is not APIHelper.SKIP:
            self.user_identifier = user_identifier
        if user_identifier_source is not APIHelper.SKIP:
            self.user_identifier_source = user_identifier_source

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
                else None
        call_method =\
            dictionary.get("call_method")\
            if dictionary.get("call_method")\
                else None
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
            return APIHelper.is_valid_type(
                    value=dictionary.brand,
                    type_callable=lambda value:
                        BaseOnlineDataBrand.validate(value)) \
                and APIHelper.is_valid_type(
                    value=dictionary.call_method,
                    type_callable=lambda value:
                        BaseOnlineDataCallMethod.validate(value))

        if not isinstance(dictionary, dict):
            return False

        return APIHelper.is_valid_type(
                value=dictionary.get("brand"),
                type_callable=lambda value:
                    BaseOnlineDataBrand.validate(value)) \
            and APIHelper.is_valid_type(
                value=dictionary.get("call_method"),
                type_callable=lambda value:
                    BaseOnlineDataCallMethod.validate(value))

    def __repr__(self):
        """Return a unambiguous string representation."""
        _brand=self.brand
        _call_method=self.call_method
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
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"brand={_brand!r}, "
            f"call_method={_call_method!r}, "
            f"os_type={_os_type!r}, "
            f"user_identifier={_user_identifier!r}, "
            f"user_identifier_source={_user_identifier_source!r}, "
            f"additional_properties={_additional_properties!r}, "
            f")"
        )

    def __str__(self):
        """Return a human-readable string representation."""
        _brand=self.brand
        _call_method=self.call_method
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
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"brand={_brand!s}, "
            f"call_method={_call_method!s}, "
            f"os_type={_os_type!s}, "
            f"user_identifier={_user_identifier!s}, "
            f"user_identifier_source={_user_identifier_source!s}, "
            f"additional_properties={_additional_properties!s}, "
            f")"
        )
