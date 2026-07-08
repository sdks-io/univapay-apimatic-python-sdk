"""univapay_client_sdk.

This file was automatically generated for Univapay by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

# ruff: noqa: E501
from univapayclientsdk.api_helper import APIHelper


class TokenResponseCardDataCard(object):
    """Implementation of the 'TokenResponseCardDataCard' model.

    Token Response Card Data Card schema.

    Attributes:
        cardholder (str): Cardholder name.
        exp_month (int): Card expiration month.
        exp_year (int): Card expiration year.
        card_bin (str): Card bin value.
        last_four (str): Last four value.
        brand (str): Brand or network name.
        card_type (str): Card type value.
        country (str): Country code.
        category (str): Category value.
        issuer (str): Issuer value.
        sub_brand (str): Sub brand value.
        additional_properties (Dict[str, Any]): The additional properties for the
            model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "cardholder": "cardholder",
        "exp_month": "exp_month",
        "exp_year": "exp_year",
        "card_bin": "card_bin",
        "last_four": "last_four",
        "brand": "brand",
        "card_type": "card_type",
        "country": "country",
        "category": "category",
        "issuer": "issuer",
        "sub_brand": "sub_brand",
    }

    _optionals = [
        "cardholder",
        "exp_month",
        "exp_year",
        "card_bin",
        "last_four",
        "brand",
        "card_type",
        "country",
        "category",
        "issuer",
        "sub_brand",
    ]

    _nullables = [
        "category",
        "issuer",
    ]

    def __init__(
        self,
        cardholder=APIHelper.SKIP,
        exp_month=APIHelper.SKIP,
        exp_year=APIHelper.SKIP,
        card_bin=APIHelper.SKIP,
        last_four=APIHelper.SKIP,
        brand=APIHelper.SKIP,
        card_type=APIHelper.SKIP,
        country=APIHelper.SKIP,
        category=APIHelper.SKIP,
        issuer=APIHelper.SKIP,
        sub_brand=APIHelper.SKIP,
        additional_properties=None):
        """Initialize a TokenResponseCardDataCard instance."""
        # Initialize members of the class
        if cardholder is not APIHelper.SKIP:
            self.cardholder = cardholder
        if exp_month is not APIHelper.SKIP:
            self.exp_month = exp_month
        if exp_year is not APIHelper.SKIP:
            self.exp_year = exp_year
        if card_bin is not APIHelper.SKIP:
            self.card_bin = card_bin
        if last_four is not APIHelper.SKIP:
            self.last_four = last_four
        if brand is not APIHelper.SKIP:
            self.brand = brand
        if card_type is not APIHelper.SKIP:
            self.card_type = card_type
        if country is not APIHelper.SKIP:
            self.country = country
        if category is not APIHelper.SKIP:
            self.category = category
        if issuer is not APIHelper.SKIP:
            self.issuer = issuer
        if sub_brand is not APIHelper.SKIP:
            self.sub_brand = sub_brand

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
        cardholder =\
            dictionary.get("cardholder")\
            if dictionary.get("cardholder")\
                else APIHelper.SKIP
        exp_month =\
            dictionary.get("exp_month")\
            if dictionary.get("exp_month")\
                else APIHelper.SKIP
        exp_year =\
            dictionary.get("exp_year")\
            if dictionary.get("exp_year")\
                else APIHelper.SKIP
        card_bin =\
            dictionary.get("card_bin")\
            if dictionary.get("card_bin")\
                else APIHelper.SKIP
        last_four =\
            dictionary.get("last_four")\
            if dictionary.get("last_four")\
                else APIHelper.SKIP
        brand =\
            dictionary.get("brand")\
            if dictionary.get("brand")\
                else APIHelper.SKIP
        card_type =\
            dictionary.get("card_type")\
            if dictionary.get("card_type")\
                else APIHelper.SKIP
        country =\
            dictionary.get("country")\
            if dictionary.get("country")\
                else APIHelper.SKIP
        category =\
            dictionary.get("category")\
            if "category" in dictionary.keys()\
                else APIHelper.SKIP
        issuer =\
            dictionary.get("issuer")\
            if "issuer" in dictionary.keys()\
                else APIHelper.SKIP
        sub_brand =\
            dictionary.get("sub_brand")\
            if dictionary.get("sub_brand")\
                else APIHelper.SKIP

        additional_properties = APIHelper.get_additional_properties(
            dictionary={k: v for k, v in dictionary.items()
                        if k not in cls._names.values()},
            unboxing_function=lambda value: value)

        # Return an object of this model
        return cls(cardholder,
                   exp_month,
                   exp_year,
                   card_bin,
                   last_four,
                   brand,
                   card_type,
                   country,
                   category,
                   issuer,
                   sub_brand,
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
        _cardholder=(
            self.cardholder
            if hasattr(self, "cardholder")
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
        _card_bin=(
            self.card_bin
            if hasattr(self, "card_bin")
            else None
        )
        _last_four=(
            self.last_four
            if hasattr(self, "last_four")
            else None
        )
        _brand=(
            self.brand
            if hasattr(self, "brand")
            else None
        )
        _card_type=(
            self.card_type
            if hasattr(self, "card_type")
            else None
        )
        _country=(
            self.country
            if hasattr(self, "country")
            else None
        )
        _category=(
            self.category
            if hasattr(self, "category")
            else None
        )
        _issuer=(
            self.issuer
            if hasattr(self, "issuer")
            else None
        )
        _sub_brand=(
            self.sub_brand
            if hasattr(self, "sub_brand")
            else None
        )
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"cardholder={_cardholder!r}, "
            f"exp_month={_exp_month!r}, "
            f"exp_year={_exp_year!r}, "
            f"card_bin={_card_bin!r}, "
            f"last_four={_last_four!r}, "
            f"brand={_brand!r}, "
            f"card_type={_card_type!r}, "
            f"country={_country!r}, "
            f"category={_category!r}, "
            f"issuer={_issuer!r}, "
            f"sub_brand={_sub_brand!r}, "
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
        _card_bin=(
            self.card_bin
            if hasattr(self, "card_bin")
            else None
        )
        _last_four=(
            self.last_four
            if hasattr(self, "last_four")
            else None
        )
        _brand=(
            self.brand
            if hasattr(self, "brand")
            else None
        )
        _card_type=(
            self.card_type
            if hasattr(self, "card_type")
            else None
        )
        _country=(
            self.country
            if hasattr(self, "country")
            else None
        )
        _category=(
            self.category
            if hasattr(self, "category")
            else None
        )
        _issuer=(
            self.issuer
            if hasattr(self, "issuer")
            else None
        )
        _sub_brand=(
            self.sub_brand
            if hasattr(self, "sub_brand")
            else None
        )
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"cardholder={_cardholder!s}, "
            f"exp_month={_exp_month!s}, "
            f"exp_year={_exp_year!s}, "
            f"card_bin={_card_bin!s}, "
            f"last_four={_last_four!s}, "
            f"brand={_brand!s}, "
            f"card_type={_card_type!s}, "
            f"country={_country!s}, "
            f"category={_category!s}, "
            f"issuer={_issuer!s}, "
            f"sub_brand={_sub_brand!s}, "
            f"additional_properties={_additional_properties!s}, "
            f")"
        )
