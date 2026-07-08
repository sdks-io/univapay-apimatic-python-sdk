"""univapay_client_sdk.

This file was automatically generated for Univapay by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

# ruff: noqa: E501
from univapayclientsdk.api_helper import APIHelper


class BaseBankTransferData(object):
    """Implementation of the 'BaseBankTransferData' model.

    Base Bank Transfer Data schema.

    Attributes:
        brand (str): The bank brand identifier (e.g., 'aozora_bank').
        expiration_period (str): ISO 8601 duration format (e.g., 'PT168H').
        expiration_time_shift (str): Time shift applied to the expiration, typically
            pushing it to the end of the day  in a specific timezone (e.g.,
            '23:59:59+09:00').
        additional_properties (Dict[str, Any]): The additional properties for the
            model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "brand": "brand",
        "expiration_period": "expiration_period",
        "expiration_time_shift": "expiration_time_shift",
    }

    _optionals = [
        "brand",
        "expiration_period",
        "expiration_time_shift",
    ]

    def __init__(
        self,
        brand=APIHelper.SKIP,
        expiration_period=APIHelper.SKIP,
        expiration_time_shift=APIHelper.SKIP,
        additional_properties=None):
        """Initialize a BaseBankTransferData instance."""
        # Initialize members of the class
        if brand is not APIHelper.SKIP:
            self.brand = brand
        if expiration_period is not APIHelper.SKIP:
            self.expiration_period = expiration_period
        if expiration_time_shift is not APIHelper.SKIP:
            self.expiration_time_shift = expiration_time_shift

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
        expiration_period =\
            dictionary.get("expiration_period")\
            if dictionary.get("expiration_period")\
                else APIHelper.SKIP
        expiration_time_shift =\
            dictionary.get("expiration_time_shift")\
            if dictionary.get("expiration_time_shift")\
                else APIHelper.SKIP

        additional_properties = APIHelper.get_additional_properties(
            dictionary={k: v for k, v in dictionary.items()
                        if k not in cls._names.values()},
            unboxing_function=lambda value: value)

        # Return an object of this model
        return cls(brand,
                   expiration_period,
                   expiration_time_shift,
                   additional_properties)

    def __repr__(self):
        """Return a unambiguous string representation."""
        _brand=(
            self.brand
            if hasattr(self, "brand")
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
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"brand={_brand!r}, "
            f"expiration_period={_expiration_period!r}, "
            f"expiration_time_shift={_expiration_time_shift!r}, "
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
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"brand={_brand!s}, "
            f"expiration_period={_expiration_period!s}, "
            f"expiration_time_shift={_expiration_time_shift!s}, "
            f"additional_properties={_additional_properties!s}, "
            f")"
        )
