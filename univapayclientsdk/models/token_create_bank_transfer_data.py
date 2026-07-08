"""univapay_client_sdk.

This file was automatically generated for Univapay by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

# ruff: noqa: E501
from univapayclientsdk.api_helper import APIHelper


class TokenCreateBankTransferData(object):
    """Implementation of the 'TokenCreateBankTransferData' model.

    Token Create Bank Transfer Data schema.

    Attributes:
        brand (str): The bank brand identifier (e.g., 'aozora_bank').
        expiration_period (str): ISO 8601 duration format (e.g., 'PT168H').
        expiration_time_shift (str): Time shift applied to the expiration, typically
            pushing it to the end of the day  in a specific timezone (e.g.,
            '23:59:59+09:00').
        name (str): The name of the customer initiating the transfer.
        additional_properties (Dict[str, Any]): The additional properties for the
            model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "brand": "brand",
        "expiration_period": "expiration_period",
        "expiration_time_shift": "expiration_time_shift",
        "name": "name",
    }

    _optionals = [
        "expiration_period",
        "expiration_time_shift",
        "name",
    ]

    def __init__(
        self,
        brand=None,
        expiration_period=APIHelper.SKIP,
        expiration_time_shift=APIHelper.SKIP,
        name=APIHelper.SKIP,
        additional_properties=None):
        """Initialize a TokenCreateBankTransferData instance."""
        # Initialize members of the class
        self.brand = brand
        if expiration_period is not APIHelper.SKIP:
            self.expiration_period = expiration_period
        if expiration_time_shift is not APIHelper.SKIP:
            self.expiration_time_shift = expiration_time_shift
        if name is not APIHelper.SKIP:
            self.name = name

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
        expiration_period =\
            dictionary.get("expiration_period")\
            if dictionary.get("expiration_period")\
                else APIHelper.SKIP
        expiration_time_shift =\
            dictionary.get("expiration_time_shift")\
            if dictionary.get("expiration_time_shift")\
                else APIHelper.SKIP
        name =\
            dictionary.get("name")\
            if dictionary.get("name")\
                else APIHelper.SKIP

        additional_properties = APIHelper.get_additional_properties(
            dictionary={k: v for k, v in dictionary.items()
                        if k not in cls._names.values()},
            unboxing_function=lambda value: value)

        # Return an object of this model
        return cls(brand,
                   expiration_period,
                   expiration_time_shift,
                   name,
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
                        isinstance(
                        value,
                        str,
                ))

        if not isinstance(dictionary, dict):
            return False

        return APIHelper.is_valid_type(
                value=dictionary.get("brand"),
                type_callable=lambda value:
                    isinstance(
                    value,
                    str,
            ))

    def __repr__(self):
        """Return a unambiguous string representation."""
        _brand=self.brand
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
        _name=(
            self.name
            if hasattr(self, "name")
            else None
        )
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"brand={_brand!r}, "
            f"expiration_period={_expiration_period!r}, "
            f"expiration_time_shift={_expiration_time_shift!r}, "
            f"name={_name!r}, "
            f"additional_properties={_additional_properties!r}, "
            f")"
        )

    def __str__(self):
        """Return a human-readable string representation."""
        _brand=self.brand
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
        _name=(
            self.name
            if hasattr(self, "name")
            else None
        )
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"brand={_brand!s}, "
            f"expiration_period={_expiration_period!s}, "
            f"expiration_time_shift={_expiration_time_shift!s}, "
            f"name={_name!s}, "
            f"additional_properties={_additional_properties!s}, "
            f")"
        )
