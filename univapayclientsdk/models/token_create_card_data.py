"""univapay_client_sdk.

This file was automatically generated for Univapay by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

# ruff: noqa: E501
from univapayclientsdk.api_helper import APIHelper
from univapayclientsdk.models.token_create_card_data_cvv_authorize import (
    TokenCreateCardDataCvvAuthorize,
)
from univapayclientsdk.models.token_create_card_data_three_ds import (
    TokenCreateCardDataThreeDs,
)
from univapayclientsdk.models.token_create_phone_number import (
    TokenCreatePhoneNumber,
)


class TokenCreateCardData(object):
    """Implementation of the 'TokenCreateCardData' model.

    Token Create Card Data schema.

    Attributes:
        cardholder (str): Cardholder name.
        card_number (str): Card number.
        exp_month (str): Card expiration month.
        exp_year (str): Card expiration year.
        cvv (str): Card security code.
        line_1 (str): Primary street address line.
        line_2 (str): Secondary street address line.
        state (str): State or prefecture.
        city (str): City or locality.
        country (str): Country code.
        zip (str): Postal code.
        phone_number (TokenCreatePhoneNumber): Token Create Phone Number schema.
        cvv_authorize (TokenCreateCardDataCvvAuthorize): Token Create Card Data Cvv
            Authorize schema.
        three_ds (TokenCreateCardDataThreeDs): Token Create Card Data Three Ds schema.
        additional_properties (Dict[str, Any]): The additional properties for the
            model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "card_number": "card_number",
        "exp_month": "exp_month",
        "exp_year": "exp_year",
        "cardholder": "cardholder",
        "cvv": "cvv",
        "line_1": "line1",
        "line_2": "line2",
        "state": "state",
        "city": "city",
        "country": "country",
        "zip": "zip",
        "phone_number": "phone_number",
        "cvv_authorize": "cvv_authorize",
        "three_ds": "three_ds",
    }

    _optionals = [
        "cardholder",
        "cvv",
        "line_1",
        "line_2",
        "state",
        "city",
        "country",
        "zip",
        "phone_number",
        "cvv_authorize",
        "three_ds",
    ]

    _nullables = [
        "cvv",
    ]

    def __init__(
        self,
        card_number=None,
        exp_month=None,
        exp_year=None,
        cardholder=APIHelper.SKIP,
        cvv=APIHelper.SKIP,
        line_1=APIHelper.SKIP,
        line_2=APIHelper.SKIP,
        state=APIHelper.SKIP,
        city=APIHelper.SKIP,
        country=APIHelper.SKIP,
        zip=APIHelper.SKIP,
        phone_number=APIHelper.SKIP,
        cvv_authorize=APIHelper.SKIP,
        three_ds=APIHelper.SKIP,
        additional_properties=None):
        """Initialize a TokenCreateCardData instance."""
        # Initialize members of the class
        if cardholder is not APIHelper.SKIP:
            self.cardholder = cardholder
        self.card_number = card_number
        self.exp_month = exp_month
        self.exp_year = exp_year
        if cvv is not APIHelper.SKIP:
            self.cvv = cvv
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
        if cvv_authorize is not APIHelper.SKIP:
            self.cvv_authorize = cvv_authorize
        if three_ds is not APIHelper.SKIP:
            self.three_ds = three_ds

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
        card_number =\
            dictionary.get("card_number")\
            if dictionary.get("card_number")\
                else None
        exp_month =\
            dictionary.get("exp_month")\
            if dictionary.get("exp_month")\
                else None
        exp_year =\
            dictionary.get("exp_year")\
            if dictionary.get("exp_year")\
                else None
        cardholder =\
            dictionary.get("cardholder")\
            if dictionary.get("cardholder")\
                else APIHelper.SKIP
        cvv =\
            dictionary.get("cvv")\
            if "cvv" in dictionary.keys()\
                else APIHelper.SKIP
        line_1 =\
            dictionary.get("line1")\
            if dictionary.get("line1")\
                else APIHelper.SKIP
        line_2 =\
            dictionary.get("line2")\
            if dictionary.get("line2")\
                else APIHelper.SKIP
        state =\
            dictionary.get("state")\
            if dictionary.get("state")\
                else APIHelper.SKIP
        city =\
            dictionary.get("city")\
            if dictionary.get("city")\
                else APIHelper.SKIP
        country =\
            dictionary.get("country")\
            if dictionary.get("country")\
                else APIHelper.SKIP
        zip =\
            dictionary.get("zip")\
            if dictionary.get("zip")\
                else APIHelper.SKIP
        phone_number =\
            TokenCreatePhoneNumber.from_dictionary(
                dictionary.get("phone_number"))\
                if "phone_number" in dictionary.keys()\
                else APIHelper.SKIP
        cvv_authorize =\
            TokenCreateCardDataCvvAuthorize.from_dictionary(
                dictionary.get("cvv_authorize"))\
                if "cvv_authorize" in dictionary.keys()\
                else APIHelper.SKIP
        three_ds =\
            TokenCreateCardDataThreeDs.from_dictionary(
                dictionary.get("three_ds"))\
                if "three_ds" in dictionary.keys()\
                else APIHelper.SKIP

        additional_properties = APIHelper.get_additional_properties(
            dictionary={k: v for k, v in dictionary.items()
                        if k not in cls._names.values()},
            unboxing_function=lambda value: value)

        # Return an object of this model
        return cls(card_number,
                   exp_month,
                   exp_year,
                   cardholder,
                   cvv,
                   line_1,
                   line_2,
                   state,
                   city,
                   country,
                   zip,
                   phone_number,
                   cvv_authorize,
                   three_ds,
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
                    value=dictionary.card_number,
                    type_callable=lambda value:
                        isinstance(
                        value,
                        str,
                )) \
                and APIHelper.is_valid_type(
                    value=dictionary.exp_month,
                    type_callable=lambda value:
                        isinstance(
                        value,
                        str,
                )) \
                and APIHelper.is_valid_type(
                    value=dictionary.exp_year,
                    type_callable=lambda value:
                        isinstance(
                        value,
                        str,
                ))

        if not isinstance(dictionary, dict):
            return False

        return APIHelper.is_valid_type(
                value=dictionary.get("card_number"),
                type_callable=lambda value:
                    isinstance(
                    value,
                    str,
            )) \
            and APIHelper.is_valid_type(
                value=dictionary.get("exp_month"),
                type_callable=lambda value:
                    isinstance(
                    value,
                    str,
            )) \
            and APIHelper.is_valid_type(
                value=dictionary.get("exp_year"),
                type_callable=lambda value:
                    isinstance(
                    value,
                    str,
            ))

    def __repr__(self):
        """Return a unambiguous string representation."""
        _cardholder=(
            self.cardholder
            if hasattr(self, "cardholder")
            else None
        )
        _card_number=self.card_number
        _exp_month=self.exp_month
        _exp_year=self.exp_year
        _cvv=(
            self.cvv
            if hasattr(self, "cvv")
            else None
        )
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
        _cvv_authorize=(
            self.cvv_authorize
            if hasattr(self, "cvv_authorize")
            else None
        )
        _three_ds=(
            self.three_ds
            if hasattr(self, "three_ds")
            else None
        )
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"cardholder={_cardholder!r}, "
            f"card_number={_card_number!r}, "
            f"exp_month={_exp_month!r}, "
            f"exp_year={_exp_year!r}, "
            f"cvv={_cvv!r}, "
            f"line_1={_line_1!r}, "
            f"line_2={_line_2!r}, "
            f"state={_state!r}, "
            f"city={_city!r}, "
            f"country={_country!r}, "
            f"zip={_zip!r}, "
            f"phone_number={_phone_number!r}, "
            f"cvv_authorize={_cvv_authorize!r}, "
            f"three_ds={_three_ds!r}, "
            f"additional_properties={_additional_properties!r}, "
            f")"
        )

    def __str__(self):
        """Return a human-readable string representation."""
        _cardholder=(
            self.cardholder
            if hasattr(self, "cardholder")
            else None
        )
        _card_number=self.card_number
        _exp_month=self.exp_month
        _exp_year=self.exp_year
        _cvv=(
            self.cvv
            if hasattr(self, "cvv")
            else None
        )
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
        _cvv_authorize=(
            self.cvv_authorize
            if hasattr(self, "cvv_authorize")
            else None
        )
        _three_ds=(
            self.three_ds
            if hasattr(self, "three_ds")
            else None
        )
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"cardholder={_cardholder!s}, "
            f"card_number={_card_number!s}, "
            f"exp_month={_exp_month!s}, "
            f"exp_year={_exp_year!s}, "
            f"cvv={_cvv!s}, "
            f"line_1={_line_1!s}, "
            f"line_2={_line_2!s}, "
            f"state={_state!s}, "
            f"city={_city!s}, "
            f"country={_country!s}, "
            f"zip={_zip!s}, "
            f"phone_number={_phone_number!s}, "
            f"cvv_authorize={_cvv_authorize!s}, "
            f"three_ds={_three_ds!s}, "
            f"additional_properties={_additional_properties!s}, "
            f")"
        )
