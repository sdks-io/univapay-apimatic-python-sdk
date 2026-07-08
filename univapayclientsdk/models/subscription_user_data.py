"""univapay_client_sdk.

This file was automatically generated for Univapay by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

# ruff: noqa: E501
from univapayclientsdk.api_helper import APIHelper


class SubscriptionUserData(object):
    """Implementation of the 'SubscriptionUserData' model.

    Customer-facing payment method summary data.

    Attributes:
        mtype (str): Type of the resource.
        cardholder_name (str): Cardholder name value.
        email (str): Customer email address.
        brand (str): Brand or network name.
        gateway (str): Gateway identifier.
        service_provider (str): Service provider identifier.
        additional_properties (Dict[str, Any]): The additional properties for the
            model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "mtype": "type",
        "cardholder_name": "cardholder_name",
        "email": "email",
        "brand": "brand",
        "gateway": "gateway",
        "service_provider": "service_provider",
    }

    _optionals = [
        "mtype",
        "cardholder_name",
        "email",
        "brand",
        "gateway",
        "service_provider",
    ]

    _nullables = [
        "cardholder_name",
        "email",
        "brand",
        "gateway",
        "service_provider",
    ]

    def __init__(
        self,
        mtype=APIHelper.SKIP,
        cardholder_name=APIHelper.SKIP,
        email=APIHelper.SKIP,
        brand=APIHelper.SKIP,
        gateway=APIHelper.SKIP,
        service_provider=APIHelper.SKIP,
        additional_properties=None):
        """Initialize a SubscriptionUserData instance."""
        # Initialize members of the class
        if mtype is not APIHelper.SKIP:
            self.mtype = mtype
        if cardholder_name is not APIHelper.SKIP:
            self.cardholder_name = cardholder_name
        if email is not APIHelper.SKIP:
            self.email = email
        if brand is not APIHelper.SKIP:
            self.brand = brand
        if gateway is not APIHelper.SKIP:
            self.gateway = gateway
        if service_provider is not APIHelper.SKIP:
            self.service_provider = service_provider

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
        mtype =\
            dictionary.get("type")\
            if dictionary.get("type")\
                else APIHelper.SKIP
        cardholder_name =\
            dictionary.get("cardholder_name")\
            if "cardholder_name" in dictionary.keys()\
                else APIHelper.SKIP
        email =\
            dictionary.get("email")\
            if "email" in dictionary.keys()\
                else APIHelper.SKIP
        brand =\
            dictionary.get("brand")\
            if "brand" in dictionary.keys()\
                else APIHelper.SKIP
        gateway =\
            dictionary.get("gateway")\
            if "gateway" in dictionary.keys()\
                else APIHelper.SKIP
        service_provider =\
            dictionary.get("service_provider")\
            if "service_provider" in dictionary.keys()\
                else APIHelper.SKIP

        additional_properties = APIHelper.get_additional_properties(
            dictionary={k: v for k, v in dictionary.items()
                        if k not in cls._names.values()},
            unboxing_function=lambda value: value)

        # Return an object of this model
        return cls(mtype,
                   cardholder_name,
                   email,
                   brand,
                   gateway,
                   service_provider,
                   additional_properties)

    def __repr__(self):
        """Return a unambiguous string representation."""
        _mtype=(
            self.mtype
            if hasattr(self, "mtype")
            else None
        )
        _cardholder_name=(
            self.cardholder_name
            if hasattr(self, "cardholder_name")
            else None
        )
        _email=(
            self.email
            if hasattr(self, "email")
            else None
        )
        _brand=(
            self.brand
            if hasattr(self, "brand")
            else None
        )
        _gateway=(
            self.gateway
            if hasattr(self, "gateway")
            else None
        )
        _service_provider=(
            self.service_provider
            if hasattr(self, "service_provider")
            else None
        )
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"mtype={_mtype!r}, "
            f"cardholder_name={_cardholder_name!r}, "
            f"email={_email!r}, "
            f"brand={_brand!r}, "
            f"gateway={_gateway!r}, "
            f"service_provider={_service_provider!r}, "
            f"additional_properties={_additional_properties!r}, "
            f")"
        )

    def __str__(self):
        """Return a human-readable string representation."""
        _mtype=(
            self.mtype
            if hasattr(self, "mtype")
            else None
        )
        _cardholder_name=(
            self.cardholder_name
            if hasattr(self, "cardholder_name")
            else None
        )
        _email=(
            self.email
            if hasattr(self, "email")
            else None
        )
        _brand=(
            self.brand
            if hasattr(self, "brand")
            else None
        )
        _gateway=(
            self.gateway
            if hasattr(self, "gateway")
            else None
        )
        _service_provider=(
            self.service_provider
            if hasattr(self, "service_provider")
            else None
        )
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"mtype={_mtype!s}, "
            f"cardholder_name={_cardholder_name!s}, "
            f"email={_email!s}, "
            f"brand={_brand!s}, "
            f"gateway={_gateway!s}, "
            f"service_provider={_service_provider!s}, "
            f"additional_properties={_additional_properties!s}, "
            f")"
        )
