"""univapay_client_sdk.

This file was automatically generated for Univapay by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

# ruff: noqa: E501
from univapayclientsdk.api_helper import APIHelper
from univapayclientsdk.models.token_response_phone_number import (
    TokenResponsePhoneNumber,
)


class TokenResponseKonbiniData(object):
    """Implementation of the 'TokenResponseKonbiniData' model.

    Token Response Konbini Data schema.

    Attributes:
        customer_name (str): Customer name.
        convenience_store (BaseKonbiniDataConvenienceStore): Base Konbini Data
            Convenience Store schema.
        expiration_period (str): ISO-8601 Duration (e.g., 'P7D'). Default is 30 days.
        expiration_time_shift (str): Time shift applied to the expiration, typically
            pushing it to the end of the day in a specific timezone (e.g.,
            '23:59:59.999999+09:00').
        phone_number (TokenResponsePhoneNumber): Token Response Phone Number schema.
        additional_properties (Dict[str, Any]): The additional properties for the
            model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "customer_name": "customer_name",
        "convenience_store": "convenience_store",
        "expiration_period": "expiration_period",
        "expiration_time_shift": "expiration_time_shift",
        "phone_number": "phone_number",
    }

    _optionals = [
        "customer_name",
        "convenience_store",
        "expiration_period",
        "expiration_time_shift",
        "phone_number",
    ]

    _nullables = [
        "expiration_time_shift",
    ]

    def __init__(
        self,
        customer_name=APIHelper.SKIP,
        convenience_store=APIHelper.SKIP,
        expiration_period=APIHelper.SKIP,
        expiration_time_shift=APIHelper.SKIP,
        phone_number=APIHelper.SKIP,
        additional_properties=None):
        """Initialize a TokenResponseKonbiniData instance."""
        # Initialize members of the class
        if customer_name is not APIHelper.SKIP:
            self.customer_name = customer_name
        if convenience_store is not APIHelper.SKIP:
            self.convenience_store = convenience_store
        if expiration_period is not APIHelper.SKIP:
            self.expiration_period = expiration_period
        if expiration_time_shift is not APIHelper.SKIP:
            self.expiration_time_shift = expiration_time_shift
        if phone_number is not APIHelper.SKIP:
            self.phone_number = phone_number

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
        customer_name =\
            dictionary.get("customer_name")\
            if dictionary.get("customer_name")\
                else APIHelper.SKIP
        convenience_store =\
            dictionary.get("convenience_store")\
            if dictionary.get("convenience_store")\
                else APIHelper.SKIP
        expiration_period =\
            dictionary.get("expiration_period")\
            if dictionary.get("expiration_period")\
                else APIHelper.SKIP
        expiration_time_shift =\
            dictionary.get("expiration_time_shift")\
            if "expiration_time_shift" in dictionary.keys()\
                else APIHelper.SKIP
        phone_number =\
            TokenResponsePhoneNumber.from_dictionary(
                dictionary.get("phone_number"))\
                if "phone_number" in dictionary.keys()\
                else APIHelper.SKIP

        additional_properties = APIHelper.get_additional_properties(
            dictionary={k: v for k, v in dictionary.items()
                        if k not in cls._names.values()},
            unboxing_function=lambda value: value)

        # Return an object of this model
        return cls(customer_name,
                   convenience_store,
                   expiration_period,
                   expiration_time_shift,
                   phone_number,
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
        _customer_name=(
            self.customer_name
            if hasattr(self, "customer_name")
            else None
        )
        _convenience_store=(
            self.convenience_store
            if hasattr(self, "convenience_store")
            else None
        )
        _expiration_period=(
            self.expiration_period
            if hasattr(self, "expiration_period")
            else None
        )
        _expiration_time_shift=(
            self.expiration_time_shift
            if hasattr(self, "expiration_time_shift")
            else None
        )
        _phone_number=(
            self.phone_number
            if hasattr(self, "phone_number")
            else None
        )
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"customer_name={_customer_name!r}, "
            f"convenience_store={_convenience_store!r}, "
            f"expiration_period={_expiration_period!r}, "
            f"expiration_time_shift={_expiration_time_shift!r}, "
            f"phone_number={_phone_number!r}, "
            f"additional_properties={_additional_properties!r}, "
            f")"
        )

    def __str__(self):
        """Return a human-readable string representation."""
        _customer_name=(
            self.customer_name
            if hasattr(self, "customer_name")
            else None
        )
        _convenience_store=(
            self.convenience_store
            if hasattr(self, "convenience_store")
            else None
        )
        _expiration_period=(
            self.expiration_period
            if hasattr(self, "expiration_period")
            else None
        )
        _expiration_time_shift=(
            self.expiration_time_shift
            if hasattr(self, "expiration_time_shift")
            else None
        )
        _phone_number=(
            self.phone_number
            if hasattr(self, "phone_number")
            else None
        )
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"customer_name={_customer_name!s}, "
            f"convenience_store={_convenience_store!s}, "
            f"expiration_period={_expiration_period!s}, "
            f"expiration_time_shift={_expiration_time_shift!s}, "
            f"phone_number={_phone_number!s}, "
            f"additional_properties={_additional_properties!s}, "
            f")"
        )
