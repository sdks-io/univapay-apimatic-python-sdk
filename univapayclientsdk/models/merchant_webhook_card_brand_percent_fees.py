"""univapay_client_sdk.

This file was automatically generated for Univapay by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

# ruff: noqa: E501
from univapayclientsdk.api_helper import APIHelper


class MerchantWebhookCardBrandPercentFees(object):
    """Implementation of the 'MerchantWebhookCardBrandPercentFees' model.

    Per-card-brand percent fee overrides.

    Attributes:
        visa (float): Percent fee override applied to Visa transactions.
        american_express (float): Percent fee override applied to American Express
            transactions.
        mastercard (float): Percent fee override applied to Mastercard transactions.
        maestro (float): Percent fee override applied to Maestro transactions.
        discover (float): Percent fee override applied to Discover transactions.
        jcb (float): Percent fee override applied to JCB transactions.
        diners_club (float): Percent fee override applied to Diners Club transactions.
        union_pay (float): Percent fee override applied to UnionPay transactions.
        private_label (float): Percent fee override applied to private-label card
            transactions.
        additional_properties (Dict[str, Any]): The additional properties for the
            model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "visa": "visa",
        "american_express": "american_express",
        "mastercard": "mastercard",
        "maestro": "maestro",
        "discover": "discover",
        "jcb": "jcb",
        "diners_club": "diners_club",
        "union_pay": "union_pay",
        "private_label": "private_label",
    }

    _optionals = [
        "visa",
        "american_express",
        "mastercard",
        "maestro",
        "discover",
        "jcb",
        "diners_club",
        "union_pay",
        "private_label",
    ]

    _nullables = [
        "visa",
        "american_express",
        "mastercard",
        "maestro",
        "discover",
        "jcb",
        "diners_club",
        "union_pay",
        "private_label",
    ]

    def __init__(
        self,
        visa=APIHelper.SKIP,
        american_express=APIHelper.SKIP,
        mastercard=APIHelper.SKIP,
        maestro=APIHelper.SKIP,
        discover=APIHelper.SKIP,
        jcb=APIHelper.SKIP,
        diners_club=APIHelper.SKIP,
        union_pay=APIHelper.SKIP,
        private_label=APIHelper.SKIP,
        additional_properties=None):
        """Initialize a MerchantWebhookCardBrandPercentFees instance."""
        # Initialize members of the class
        if visa is not APIHelper.SKIP:
            self.visa = visa
        if american_express is not APIHelper.SKIP:
            self.american_express = american_express
        if mastercard is not APIHelper.SKIP:
            self.mastercard = mastercard
        if maestro is not APIHelper.SKIP:
            self.maestro = maestro
        if discover is not APIHelper.SKIP:
            self.discover = discover
        if jcb is not APIHelper.SKIP:
            self.jcb = jcb
        if diners_club is not APIHelper.SKIP:
            self.diners_club = diners_club
        if union_pay is not APIHelper.SKIP:
            self.union_pay = union_pay
        if private_label is not APIHelper.SKIP:
            self.private_label = private_label

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
        visa =\
            dictionary.get("visa")\
            if "visa" in dictionary.keys()\
                else APIHelper.SKIP
        american_express =\
            dictionary.get("american_express")\
            if "american_express" in dictionary.keys()\
                else APIHelper.SKIP
        mastercard =\
            dictionary.get("mastercard")\
            if "mastercard" in dictionary.keys()\
                else APIHelper.SKIP
        maestro =\
            dictionary.get("maestro")\
            if "maestro" in dictionary.keys()\
                else APIHelper.SKIP
        discover =\
            dictionary.get("discover")\
            if "discover" in dictionary.keys()\
                else APIHelper.SKIP
        jcb =\
            dictionary.get("jcb")\
            if "jcb" in dictionary.keys()\
                else APIHelper.SKIP
        diners_club =\
            dictionary.get("diners_club")\
            if "diners_club" in dictionary.keys()\
                else APIHelper.SKIP
        union_pay =\
            dictionary.get("union_pay")\
            if "union_pay" in dictionary.keys()\
                else APIHelper.SKIP
        private_label =\
            dictionary.get("private_label")\
            if "private_label" in dictionary.keys()\
                else APIHelper.SKIP

        additional_properties = APIHelper.get_additional_properties(
            dictionary={k: v for k, v in dictionary.items()
                        if k not in cls._names.values()},
            unboxing_function=lambda value: value)

        # Return an object of this model
        return cls(visa,
                   american_express,
                   mastercard,
                   maestro,
                   discover,
                   jcb,
                   diners_club,
                   union_pay,
                   private_label,
                   additional_properties)

    def __repr__(self):
        """Return a unambiguous string representation."""
        _visa=(
            self.visa
            if hasattr(self, "visa")
            else None
        )
        _american_express=(
            self.american_express
            if hasattr(self, "american_express")
            else None
        )
        _mastercard=(
            self.mastercard
            if hasattr(self, "mastercard")
            else None
        )
        _maestro=(
            self.maestro
            if hasattr(self, "maestro")
            else None
        )
        _discover=(
            self.discover
            if hasattr(self, "discover")
            else None
        )
        _jcb=(
            self.jcb
            if hasattr(self, "jcb")
            else None
        )
        _diners_club=(
            self.diners_club
            if hasattr(self, "diners_club")
            else None
        )
        _union_pay=(
            self.union_pay
            if hasattr(self, "union_pay")
            else None
        )
        _private_label=(
            self.private_label
            if hasattr(self, "private_label")
            else None
        )
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"visa={_visa!r}, "
            f"american_express={_american_express!r}, "
            f"mastercard={_mastercard!r}, "
            f"maestro={_maestro!r}, "
            f"discover={_discover!r}, "
            f"jcb={_jcb!r}, "
            f"diners_club={_diners_club!r}, "
            f"union_pay={_union_pay!r}, "
            f"private_label={_private_label!r}, "
            f"additional_properties={_additional_properties!r}, "
            f")"
        )

    def __str__(self):
        """Return a human-readable string representation."""
        _visa=(
            self.visa
            if hasattr(self, "visa")
            else None
        )
        _american_express=(
            self.american_express
            if hasattr(self, "american_express")
            else None
        )
        _mastercard=(
            self.mastercard
            if hasattr(self, "mastercard")
            else None
        )
        _maestro=(
            self.maestro
            if hasattr(self, "maestro")
            else None
        )
        _discover=(
            self.discover
            if hasattr(self, "discover")
            else None
        )
        _jcb=(
            self.jcb
            if hasattr(self, "jcb")
            else None
        )
        _diners_club=(
            self.diners_club
            if hasattr(self, "diners_club")
            else None
        )
        _union_pay=(
            self.union_pay
            if hasattr(self, "union_pay")
            else None
        )
        _private_label=(
            self.private_label
            if hasattr(self, "private_label")
            else None
        )
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"visa={_visa!s}, "
            f"american_express={_american_express!s}, "
            f"mastercard={_mastercard!s}, "
            f"maestro={_maestro!s}, "
            f"discover={_discover!s}, "
            f"jcb={_jcb!s}, "
            f"diners_club={_diners_club!s}, "
            f"union_pay={_union_pay!s}, "
            f"private_label={_private_label!s}, "
            f"additional_properties={_additional_properties!s}, "
            f")"
        )
