"""univapay_client_sdk.

This file was automatically generated for Univapay by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

# ruff: noqa: E501
from univapayclientsdk.api_helper import APIHelper
from univapayclientsdk.models.token_response_phone_number import (
    TokenResponsePhoneNumber,
)


class TokenResponseCardDataBilling(object):
    """Implementation of the 'TokenResponseCardDataBilling' model.

    Token Response Card Data Billing schema.

    Attributes:
        line_1 (str): Primary street address line.
        line_2 (str): Secondary street address line.
        state (str): State or prefecture.
        city (str): City or locality.
        country (str): Country code.
        zip (str): Postal code.
        phone_number (TokenResponsePhoneNumber): Token Response Phone Number schema.
        additional_properties (Dict[str, Any]): The additional properties for the
            model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "line_1": "line1",
        "line_2": "line2",
        "state": "state",
        "city": "city",
        "country": "country",
        "zip": "zip",
        "phone_number": "phone_number",
    }

    _optionals = [
        "line_1",
        "line_2",
        "state",
        "city",
        "country",
        "zip",
        "phone_number",
    ]

    _nullables = [
        "line_1",
        "line_2",
        "state",
        "city",
        "country",
        "zip",
    ]

    def __init__(
        self,
        line_1=APIHelper.SKIP,
        line_2=APIHelper.SKIP,
        state=APIHelper.SKIP,
        city=APIHelper.SKIP,
        country=APIHelper.SKIP,
        zip=APIHelper.SKIP,
        phone_number=APIHelper.SKIP,
        additional_properties=None):
        """Initialize a TokenResponseCardDataBilling instance."""
        # Initialize members of the class
        if line_1 is not APIHelper.SKIP:
            self.line_1 = line_1
        if line_2 is not APIHelper.SKIP:
            self.line_2 = line_2
        if state is not APIHelper.SKIP:
            self.state = state
        if city is not APIHelper.SKIP:
            self.city = city
        if country is not APIHelper.SKIP:
            self.country = country
        if zip is not APIHelper.SKIP:
            self.zip = zip
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
        line_1 =\
            dictionary.get("line1")\
            if "line1" in dictionary.keys()\
                else APIHelper.SKIP
        line_2 =\
            dictionary.get("line2")\
            if "line2" in dictionary.keys()\
                else APIHelper.SKIP
        state =\
            dictionary.get("state")\
            if "state" in dictionary.keys()\
                else APIHelper.SKIP
        city =\
            dictionary.get("city")\
            if "city" in dictionary.keys()\
                else APIHelper.SKIP
        country =\
            dictionary.get("country")\
            if "country" in dictionary.keys()\
                else APIHelper.SKIP
        zip =\
            dictionary.get("zip")\
            if "zip" in dictionary.keys()\
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
        return cls(line_1,
                   line_2,
                   state,
                   city,
                   country,
                   zip,
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
        _line_1=(
            self.line_1
            if hasattr(self, "line_1")
            else None
        )
        _line_2=(
            self.line_2
            if hasattr(self, "line_2")
            else None
        )
        _state=(
            self.state
            if hasattr(self, "state")
            else None
        )
        _city=(
            self.city
            if hasattr(self, "city")
            else None
        )
        _country=(
            self.country
            if hasattr(self, "country")
            else None
        )
        _zip=(
            self.zip
            if hasattr(self, "zip")
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
            f"line_1={_line_1!r}, "
            f"line_2={_line_2!r}, "
            f"state={_state!r}, "
            f"city={_city!r}, "
            f"country={_country!r}, "
            f"zip={_zip!r}, "
            f"phone_number={_phone_number!r}, "
            f"additional_properties={_additional_properties!r}, "
            f")"
        )

    def __str__(self):
        """Return a human-readable string representation."""
        _line_1=(
            self.line_1
            if hasattr(self, "line_1")
            else None
        )
        _line_2=(
            self.line_2
            if hasattr(self, "line_2")
            else None
        )
        _state=(
            self.state
            if hasattr(self, "state")
            else None
        )
        _city=(
            self.city
            if hasattr(self, "city")
            else None
        )
        _country=(
            self.country
            if hasattr(self, "country")
            else None
        )
        _zip=(
            self.zip
            if hasattr(self, "zip")
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
            f"line_1={_line_1!s}, "
            f"line_2={_line_2!s}, "
            f"state={_state!s}, "
            f"city={_city!s}, "
            f"country={_country!s}, "
            f"zip={_zip!s}, "
            f"phone_number={_phone_number!s}, "
            f"additional_properties={_additional_properties!s}, "
            f")"
        )
