"""univapay_client_sdk.

This file was automatically generated for Univapay by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

# ruff: noqa: E501
from univapayclientsdk.api_helper import APIHelper


class TokenCreatePhoneNumber(object):
    """Implementation of the 'TokenCreatePhoneNumber' model.

    Token Create Phone Number schema.

    Attributes:
        country_code (str): Country code as string (e.g., '1' or '81').
        local_number (str): Local phone number.
        additional_properties (Dict[str, Any]): The additional properties for the
            model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "country_code": "country_code",
        "local_number": "local_number",
    }

    def __init__(
        self,
        country_code=None,
        local_number=None,
        additional_properties=None):
        """Initialize a TokenCreatePhoneNumber instance."""
        # Initialize members of the class
        self.country_code = country_code
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
                else None
        local_number =\
            dictionary.get("local_number")\
            if dictionary.get("local_number")\
                else None

        additional_properties = APIHelper.get_additional_properties(
            dictionary={k: v for k, v in dictionary.items()
                        if k not in cls._names.values()},
            unboxing_function=lambda value: value)

        # Return an object of this model
        return cls(country_code,
                   local_number,
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
                    value=dictionary.country_code,
                    type_callable=lambda value:
                        isinstance(
                        value,
                        str,
                )) \
                and APIHelper.is_valid_type(
                    value=dictionary.local_number,
                    type_callable=lambda value:
                        isinstance(
                        value,
                        str,
                ))

        if not isinstance(dictionary, dict):
            return False

        return APIHelper.is_valid_type(
                value=dictionary.get("country_code"),
                type_callable=lambda value:
                    isinstance(
                    value,
                    str,
            )) \
            and APIHelper.is_valid_type(
                value=dictionary.get("local_number"),
                type_callable=lambda value:
                    isinstance(
                    value,
                    str,
            ))

    def __repr__(self):
        """Return a unambiguous string representation."""
        _country_code=self.country_code
        _local_number=self.local_number
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
        _country_code=self.country_code
        _local_number=self.local_number
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"country_code={_country_code!s}, "
            f"local_number={_local_number!s}, "
            f"additional_properties={_additional_properties!s}, "
            f")"
        )
