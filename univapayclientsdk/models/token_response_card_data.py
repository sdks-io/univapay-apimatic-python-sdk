"""univapay_client_sdk.

This file was automatically generated for Univapay by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

# ruff: noqa: E501
from univapayclientsdk.api_helper import APIHelper
from univapayclientsdk.models.token_response_card_data_billing import (
    TokenResponseCardDataBilling,
)
from univapayclientsdk.models.token_response_card_data_card import (
    TokenResponseCardDataCard,
)
from univapayclientsdk.models.token_response_card_data_cvv_authorize import (
    TokenResponseCardDataCvvAuthorize,
)
from univapayclientsdk.models.token_response_card_data_cvv_authorize_check import (
    TokenResponseCardDataCvvAuthorizeCheck,
)
from univapayclientsdk.models.token_response_card_data_three_ds import (
    TokenResponseCardDataThreeDs,
)


class TokenResponseCardData(object):
    """Implementation of the 'TokenResponseCardData' model.

    Token Response Card Data schema.

    Attributes:
        card (TokenResponseCardDataCard): Token Response Card Data Card schema.
        billing (TokenResponseCardDataBilling): Token Response Card Data Billing
            schema.
        cvv_authorize (TokenResponseCardDataCvvAuthorize): Token Response Card Data
            Cvv Authorize schema.
        cvv_authorize_check (TokenResponseCardDataCvvAuthorizeCheck): Token Response
            Card Data Cvv Authorize Check schema.
        three_ds (TokenResponseCardDataThreeDs): Token Response Card Data Three Ds
            schema.
        additional_properties (Dict[str, Any]): The additional properties for the
            model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "card": "card",
        "billing": "billing",
        "cvv_authorize": "cvv_authorize",
        "cvv_authorize_check": "cvv_authorize_check",
        "three_ds": "three_ds",
    }

    _optionals = [
        "card",
        "billing",
        "cvv_authorize",
        "cvv_authorize_check",
        "three_ds",
    ]

    def __init__(
        self,
        card=APIHelper.SKIP,
        billing=APIHelper.SKIP,
        cvv_authorize=APIHelper.SKIP,
        cvv_authorize_check=APIHelper.SKIP,
        three_ds=APIHelper.SKIP,
        additional_properties=None):
        """Initialize a TokenResponseCardData instance."""
        # Initialize members of the class
        if card is not APIHelper.SKIP:
            self.card = card
        if billing is not APIHelper.SKIP:
            self.billing = billing
        if cvv_authorize is not APIHelper.SKIP:
            self.cvv_authorize = cvv_authorize
        if cvv_authorize_check is not APIHelper.SKIP:
            self.cvv_authorize_check = cvv_authorize_check
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
        card =\
            TokenResponseCardDataCard.from_dictionary(
                dictionary.get("card"))\
                if "card" in dictionary.keys()\
                else APIHelper.SKIP
        billing =\
            TokenResponseCardDataBilling.from_dictionary(
                dictionary.get("billing"))\
                if "billing" in dictionary.keys()\
                else APIHelper.SKIP
        cvv_authorize =\
            TokenResponseCardDataCvvAuthorize.from_dictionary(
                dictionary.get("cvv_authorize"))\
                if "cvv_authorize" in dictionary.keys()\
                else APIHelper.SKIP
        cvv_authorize_check =\
            TokenResponseCardDataCvvAuthorizeCheck.from_dictionary(
                dictionary.get("cvv_authorize_check"))\
                if "cvv_authorize_check" in dictionary.keys()\
                else APIHelper.SKIP
        three_ds =\
            TokenResponseCardDataThreeDs.from_dictionary(
                dictionary.get("three_ds"))\
                if "three_ds" in dictionary.keys()\
                else APIHelper.SKIP

        additional_properties = APIHelper.get_additional_properties(
            dictionary={k: v for k, v in dictionary.items()
                        if k not in cls._names.values()},
            unboxing_function=lambda value: value)

        # Return an object of this model
        return cls(card,
                   billing,
                   cvv_authorize,
                   cvv_authorize_check,
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
            return True

        if not isinstance(dictionary, dict):
            return False

        return True

    def __repr__(self):
        """Return a unambiguous string representation."""
        _card=(
            self.card
            if hasattr(self, "card")
            else None
        )
        _billing=(
            self.billing
            if hasattr(self, "billing")
            else None
        )
        _cvv_authorize=(
            self.cvv_authorize
            if hasattr(self, "cvv_authorize")
            else None
        )
        _cvv_authorize_check=(
            self.cvv_authorize_check
            if hasattr(self, "cvv_authorize_check")
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
            f"card={_card!r}, "
            f"billing={_billing!r}, "
            f"cvv_authorize={_cvv_authorize!r}, "
            f"cvv_authorize_check={_cvv_authorize_check!r}, "
            f"three_ds={_three_ds!r}, "
            f"additional_properties={_additional_properties!r}, "
            f")"
        )

    def __str__(self):
        """Return a human-readable string representation."""
        _card=(
            self.card
            if hasattr(self, "card")
            else None
        )
        _billing=(
            self.billing
            if hasattr(self, "billing")
            else None
        )
        _cvv_authorize=(
            self.cvv_authorize
            if hasattr(self, "cvv_authorize")
            else None
        )
        _cvv_authorize_check=(
            self.cvv_authorize_check
            if hasattr(self, "cvv_authorize_check")
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
            f"card={_card!s}, "
            f"billing={_billing!s}, "
            f"cvv_authorize={_cvv_authorize!s}, "
            f"cvv_authorize_check={_cvv_authorize_check!s}, "
            f"three_ds={_three_ds!s}, "
            f"additional_properties={_additional_properties!s}, "
            f")"
        )
