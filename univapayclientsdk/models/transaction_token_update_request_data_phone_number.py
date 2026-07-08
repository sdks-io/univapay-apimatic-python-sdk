"""univapay_client_sdk.

This file was automatically generated for Univapay by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

# ruff: noqa: E501
from univapayclientsdk.api_helper import APIHelper


class TransactionTokenUpdateRequestDataPhoneNumber(object):
    """Implementation of the 'TransactionTokenUpdateRequestDataPhoneNumber' model.

    Transaction Token Update Request Data Phone Number schema.

    Attributes:
        country_code (str): Telephone country code.
        local_number (str): Local phone number.
        additional_properties (Dict[str, Any]): The additional properties for the
            model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "country_code": "country_code",
        "local_number": "local_number",
    }

    _optionals = [
        "country_code",
        "local_number",
    ]

    def __init__(
        self,
        country_code=APIHelper.SKIP,
        local_number=APIHelper.SKIP,
        additional_properties=None):
        """Initialize a TransactionTokenUpdateRequestDataPhoneNumber instance."""
        # Initialize members of the class
        if country_code is not APIHelper.SKIP:
            self.country_code = country_code
        if local_number is not APIHelper.SKIP:
            self.local_number = local_number

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
        country_code =\
            dictionary.get("country_code")\
            if dictionary.get("country_code")\
                else APIHelper.SKIP
        local_number =\
            dictionary.get("local_number")\
            if dictionary.get("local_number")\
                else APIHelper.SKIP

        additional_properties = APIHelper.get_additional_properties(
            dictionary={k: v for k, v in dictionary.items()
                        if k not in cls._names.values()},
            unboxing_function=lambda value: value)

        # Return an object of this model
        return cls(country_code,
                   local_number,
                   additional_properties)

    def __repr__(self):
        """Return a unambiguous string representation."""
        _country_code=(
            self.country_code
            if hasattr(self, "country_code")
            else None
        )
        _local_number=(
            self.local_number
            if hasattr(self, "local_number")
            else None
        )
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"country_code={_country_code!r}, "
            f"local_number={_local_number!r}, "
            f"additional_properties={_additional_properties!r}, "
            f")"
        )

    def __str__(self):
        """Return a human-readable string representation."""
        _country_code=(
            self.country_code
            if hasattr(self, "country_code")
            else None
        )
        _local_number=(
            self.local_number
            if hasattr(self, "local_number")
            else None
        )
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"country_code={_country_code!s}, "
            f"local_number={_local_number!s}, "
            f"additional_properties={_additional_properties!s}, "
            f")"
        )
