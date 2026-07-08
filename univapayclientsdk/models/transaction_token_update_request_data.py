"""univapay_client_sdk.

This file was automatically generated for Univapay by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

# ruff: noqa: E501
from univapayclientsdk.api_helper import APIHelper
from univapayclientsdk.models.transaction_token_update_request_data_phone_number import (  # noqa: E501
    TransactionTokenUpdateRequestDataPhoneNumber,
)


class TransactionTokenUpdateRequestData(object):
    """Implementation of the 'TransactionTokenUpdateRequestData' model.

    Transaction Token Update Request Data schema.

    Attributes:
        cvv (str): Update if RECURRING_USAGE_REQUIRES_CVV error occurs.
        cardholder (str): Cardholder name.
        card_number (str): Card number.
        exp_month (int): Card expiration month.
        exp_year (int): Card expiration year.
        line_1 (str): Primary street address line.
        line_2 (str): Secondary street address line.
        state (str): State or prefecture.
        city (str): City or locality.
        country (str): Country code.
        zip (str): Postal code.
        phone_number (TransactionTokenUpdateRequestDataPhoneNumber): Transaction
            Token Update Request Data Phone Number schema.
        additional_properties (Dict[str, Any]): The additional properties for the
            model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "cvv": "cvv",
        "cardholder": "cardholder",
        "card_number": "card_number",
        "exp_month": "exp_month",
        "exp_year": "exp_year",
        "line_1": "line1",
        "line_2": "line2",
        "state": "state",
        "city": "city",
        "country": "country",
        "zip": "zip",
        "phone_number": "phone_number",
    }

    _optionals = [
        "cvv",
        "cardholder",
        "card_number",
        "exp_month",
        "exp_year",
        "line_1",
        "line_2",
        "state",
        "city",
        "country",
        "zip",
        "phone_number",
    ]

    def __init__(
        self,
        cvv=APIHelper.SKIP,
        cardholder=APIHelper.SKIP,
        card_number=APIHelper.SKIP,
        exp_month=APIHelper.SKIP,
        exp_year=APIHelper.SKIP,
        line_1=APIHelper.SKIP,
        line_2=APIHelper.SKIP,
        state=APIHelper.SKIP,
        city=APIHelper.SKIP,
        country=APIHelper.SKIP,
        zip=APIHelper.SKIP,
        phone_number=APIHelper.SKIP,
        additional_properties=None):
        """Initialize a TransactionTokenUpdateRequestData instance."""
        # Initialize members of the class
        if cvv is not APIHelper.SKIP:
            self.cvv = cvv
        if cardholder is not APIHelper.SKIP:
            self.cardholder = cardholder
        if card_number is not APIHelper.SKIP:
            self.card_number = card_number
        if exp_month is not APIHelper.SKIP:
            self.exp_month = exp_month
        if exp_year is not APIHelper.SKIP:
            self.exp_year = exp_year
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
        cvv =\
            dictionary.get("cvv")\
            if dictionary.get("cvv")\
                else APIHelper.SKIP
        cardholder =\
            dictionary.get("cardholder")\
            if dictionary.get("cardholder")\
                else APIHelper.SKIP
        card_number =\
            dictionary.get("card_number")\
            if dictionary.get("card_number")\
                else APIHelper.SKIP
        exp_month =\
            dictionary.get("exp_month")\
            if dictionary.get("exp_month")\
                else APIHelper.SKIP
        exp_year =\
            dictionary.get("exp_year")\
            if dictionary.get("exp_year")\
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
            TransactionTokenUpdateRequestDataPhoneNumber.from_dictionary(
                dictionary.get("phone_number"))\
                if "phone_number" in dictionary.keys()\
                else APIHelper.SKIP

        additional_properties = APIHelper.get_additional_properties(
            dictionary={k: v for k, v in dictionary.items()
                        if k not in cls._names.values()},
            unboxing_function=lambda value: value)

        # Return an object of this model
        return cls(cvv,
                   cardholder,
                   card_number,
                   exp_month,
                   exp_year,
                   line_1,
                   line_2,
                   state,
                   city,
                   country,
                   zip,
                   phone_number,
                   additional_properties)

    def __repr__(self):
        """Return a unambiguous string representation."""
        _cvv=(
            self.cvv
            if hasattr(self, "cvv")
            else None
        )
        _cardholder=(
            self.cardholder
            if hasattr(self, "cardholder")
            else None
        )
        _card_number=(
            self.card_number
            if hasattr(self, "card_number")
            else None
        )
        _exp_month=(
            self.exp_month
            if hasattr(self, "exp_month")
            else None
        )
        _exp_year=(
            self.exp_year
            if hasattr(self, "exp_year")
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
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"cvv={_cvv!r}, "
            f"cardholder={_cardholder!r}, "
            f"card_number={_card_number!r}, "
            f"exp_month={_exp_month!r}, "
            f"exp_year={_exp_year!r}, "
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
        _cvv=(
            self.cvv
            if hasattr(self, "cvv")
            else None
        )
        _cardholder=(
            self.cardholder
            if hasattr(self, "cardholder")
            else None
        )
        _card_number=(
            self.card_number
            if hasattr(self, "card_number")
            else None
        )
        _exp_month=(
            self.exp_month
            if hasattr(self, "exp_month")
            else None
        )
        _exp_year=(
            self.exp_year
            if hasattr(self, "exp_year")
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
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"cvv={_cvv!s}, "
            f"cardholder={_cardholder!s}, "
            f"card_number={_card_number!s}, "
            f"exp_month={_exp_month!s}, "
            f"exp_year={_exp_year!s}, "
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
