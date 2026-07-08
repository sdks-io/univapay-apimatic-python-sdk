"""univapay_client_sdk.

This file was automatically generated for Univapay by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

# ruff: noqa: E501
from univapayclientsdk.api_helper import APIHelper


class MerchantWebhookCardConfiguration(object):
    """Implementation of the 'MerchantWebhookCardConfiguration' model.

    Card payment settings.

    Attributes:
        enabled (bool): Enables card payments.
        debit_enabled (bool): Allows debit cards for payment flows.
        prepaid_enabled (bool): Allows prepaid cards for payment flows.
        debit_authorization_enabled (bool): Allows authorization-only flows for debit
            cards.
        prepaid_authorization_enabled (bool): Allows authorization-only flows for
            prepaid cards.
        forbidden_card_brands (List[str]): Card brands rejected by merchant policy.
        allowed_countries_by_ip (List[str]): Source IP country codes allowed for card
            payments.
        foreign_cards_allowed (bool): Allows cards issued outside the primary
            operating country.
        fail_on_new_email (bool): Rejects card charges from previously unseen
            customer email addresses.
        card_limit (int): Maximum number of cards allowed per customer context.
        allow_empty_cvv (bool): Allows card flows without providing a CVV.
        only_direct_currency (bool): Limits card processing to direct-settlement
            currencies only.
        three_ds_required (bool): Requires 3-D Secure for eligible card flows.
        three_ds_address_required (bool): Requires billing address data when running
            3-D Secure.
        three_ds_skip_enabled (bool): Allows privileged callers to request 3-D Secure
            skip mode.
        allow_direct_token_creation (bool): Allows direct card token creation without
            hosted capture flows.
        three_ds_phone_number_required (bool): Requires a phone number when running
            3-D Secure.
        additional_properties (Dict[str, Any]): The additional properties for the
            model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "enabled": "enabled",
        "debit_enabled": "debit_enabled",
        "prepaid_enabled": "prepaid_enabled",
        "debit_authorization_enabled": "debit_authorization_enabled",
        "prepaid_authorization_enabled": "prepaid_authorization_enabled",
        "forbidden_card_brands": "forbidden_card_brands",
        "allowed_countries_by_ip": "allowed_countries_by_ip",
        "foreign_cards_allowed": "foreign_cards_allowed",
        "fail_on_new_email": "fail_on_new_email",
        "card_limit": "card_limit",
        "allow_empty_cvv": "allow_empty_cvv",
        "only_direct_currency": "only_direct_currency",
        "three_ds_required": "three_ds_required",
        "three_ds_address_required": "three_ds_address_required",
        "three_ds_skip_enabled": "three_ds_skip_enabled",
        "allow_direct_token_creation": "allow_direct_token_creation",
        "three_ds_phone_number_required": "three_ds_phone_number_required",
    }

    _optionals = [
        "enabled",
        "debit_enabled",
        "prepaid_enabled",
        "debit_authorization_enabled",
        "prepaid_authorization_enabled",
        "forbidden_card_brands",
        "allowed_countries_by_ip",
        "foreign_cards_allowed",
        "fail_on_new_email",
        "card_limit",
        "allow_empty_cvv",
        "only_direct_currency",
        "three_ds_required",
        "three_ds_address_required",
        "three_ds_skip_enabled",
        "allow_direct_token_creation",
        "three_ds_phone_number_required",
    ]

    _nullables = [
        "enabled",
        "debit_enabled",
        "prepaid_enabled",
        "debit_authorization_enabled",
        "prepaid_authorization_enabled",
        "forbidden_card_brands",
        "allowed_countries_by_ip",
        "foreign_cards_allowed",
        "fail_on_new_email",
        "card_limit",
        "allow_empty_cvv",
        "only_direct_currency",
        "three_ds_required",
        "three_ds_address_required",
        "three_ds_skip_enabled",
        "allow_direct_token_creation",
        "three_ds_phone_number_required",
    ]

    def __init__(
        self,
        enabled=APIHelper.SKIP,
        debit_enabled=APIHelper.SKIP,
        prepaid_enabled=APIHelper.SKIP,
        debit_authorization_enabled=APIHelper.SKIP,
        prepaid_authorization_enabled=APIHelper.SKIP,
        forbidden_card_brands=APIHelper.SKIP,
        allowed_countries_by_ip=APIHelper.SKIP,
        foreign_cards_allowed=APIHelper.SKIP,
        fail_on_new_email=APIHelper.SKIP,
        card_limit=APIHelper.SKIP,
        allow_empty_cvv=APIHelper.SKIP,
        only_direct_currency=APIHelper.SKIP,
        three_ds_required=APIHelper.SKIP,
        three_ds_address_required=APIHelper.SKIP,
        three_ds_skip_enabled=APIHelper.SKIP,
        allow_direct_token_creation=APIHelper.SKIP,
        three_ds_phone_number_required=APIHelper.SKIP,
        additional_properties=None):
        """Initialize a MerchantWebhookCardConfiguration instance."""
        # Initialize members of the class
        if enabled is not APIHelper.SKIP:
            self.enabled = enabled
        if debit_enabled is not APIHelper.SKIP:
            self.debit_enabled = debit_enabled
        if prepaid_enabled is not APIHelper.SKIP:
            self.prepaid_enabled = prepaid_enabled
        if debit_authorization_enabled is not APIHelper.SKIP:
            self.debit_authorization_enabled = debit_authorization_enabled
        if prepaid_authorization_enabled is not APIHelper.SKIP:
            self.prepaid_authorization_enabled = prepaid_authorization_enabled
        if forbidden_card_brands is not APIHelper.SKIP:
            self.forbidden_card_brands = forbidden_card_brands
        if allowed_countries_by_ip is not APIHelper.SKIP:
            self.allowed_countries_by_ip = allowed_countries_by_ip
        if foreign_cards_allowed is not APIHelper.SKIP:
            self.foreign_cards_allowed = foreign_cards_allowed
        if fail_on_new_email is not APIHelper.SKIP:
            self.fail_on_new_email = fail_on_new_email
        if card_limit is not APIHelper.SKIP:
            self.card_limit = card_limit
        if allow_empty_cvv is not APIHelper.SKIP:
            self.allow_empty_cvv = allow_empty_cvv
        if only_direct_currency is not APIHelper.SKIP:
            self.only_direct_currency = only_direct_currency
        if three_ds_required is not APIHelper.SKIP:
            self.three_ds_required = three_ds_required
        if three_ds_address_required is not APIHelper.SKIP:
            self.three_ds_address_required = three_ds_address_required
        if three_ds_skip_enabled is not APIHelper.SKIP:
            self.three_ds_skip_enabled = three_ds_skip_enabled
        if allow_direct_token_creation is not APIHelper.SKIP:
            self.allow_direct_token_creation = allow_direct_token_creation
        if three_ds_phone_number_required is not APIHelper.SKIP:
            self.three_ds_phone_number_required = three_ds_phone_number_required

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
        enabled =\
            dictionary.get("enabled")\
            if "enabled" in dictionary.keys()\
                else APIHelper.SKIP
        debit_enabled =\
            dictionary.get("debit_enabled")\
            if "debit_enabled" in dictionary.keys()\
                else APIHelper.SKIP
        prepaid_enabled =\
            dictionary.get("prepaid_enabled")\
            if "prepaid_enabled" in dictionary.keys()\
                else APIHelper.SKIP
        debit_authorization_enabled =\
            dictionary.get("debit_authorization_enabled")\
            if "debit_authorization_enabled" in dictionary.keys()\
                else APIHelper.SKIP
        prepaid_authorization_enabled =\
            dictionary.get("prepaid_authorization_enabled")\
            if "prepaid_authorization_enabled" in dictionary.keys()\
                else APIHelper.SKIP
        forbidden_card_brands =\
            dictionary.get("forbidden_card_brands")\
            if "forbidden_card_brands" in dictionary.keys()\
                else APIHelper.SKIP
        allowed_countries_by_ip =\
            dictionary.get("allowed_countries_by_ip")\
            if "allowed_countries_by_ip" in dictionary.keys()\
                else APIHelper.SKIP
        foreign_cards_allowed =\
            dictionary.get("foreign_cards_allowed")\
            if "foreign_cards_allowed" in dictionary.keys()\
                else APIHelper.SKIP
        fail_on_new_email =\
            dictionary.get("fail_on_new_email")\
            if "fail_on_new_email" in dictionary.keys()\
                else APIHelper.SKIP
        card_limit =\
            dictionary.get("card_limit")\
            if "card_limit" in dictionary.keys()\
                else APIHelper.SKIP
        allow_empty_cvv =\
            dictionary.get("allow_empty_cvv")\
            if "allow_empty_cvv" in dictionary.keys()\
                else APIHelper.SKIP
        only_direct_currency =\
            dictionary.get("only_direct_currency")\
            if "only_direct_currency" in dictionary.keys()\
                else APIHelper.SKIP
        three_ds_required =\
            dictionary.get("three_ds_required")\
            if "three_ds_required" in dictionary.keys()\
                else APIHelper.SKIP
        three_ds_address_required =\
            dictionary.get("three_ds_address_required")\
            if "three_ds_address_required" in dictionary.keys()\
                else APIHelper.SKIP
        three_ds_skip_enabled =\
            dictionary.get("three_ds_skip_enabled")\
            if "three_ds_skip_enabled" in dictionary.keys()\
                else APIHelper.SKIP
        allow_direct_token_creation =\
            dictionary.get("allow_direct_token_creation")\
            if "allow_direct_token_creation" in dictionary.keys()\
                else APIHelper.SKIP
        three_ds_phone_number_required =\
            dictionary.get("three_ds_phone_number_required")\
            if "three_ds_phone_number_required" in dictionary.keys()\
                else APIHelper.SKIP

        additional_properties = APIHelper.get_additional_properties(
            dictionary={k: v for k, v in dictionary.items()
                        if k not in cls._names.values()},
            unboxing_function=lambda value: value)

        # Return an object of this model
        return cls(enabled,
                   debit_enabled,
                   prepaid_enabled,
                   debit_authorization_enabled,
                   prepaid_authorization_enabled,
                   forbidden_card_brands,
                   allowed_countries_by_ip,
                   foreign_cards_allowed,
                   fail_on_new_email,
                   card_limit,
                   allow_empty_cvv,
                   only_direct_currency,
                   three_ds_required,
                   three_ds_address_required,
                   three_ds_skip_enabled,
                   allow_direct_token_creation,
                   three_ds_phone_number_required,
                   additional_properties)

    def __repr__(self):
        """Return a unambiguous string representation."""
        _enabled=(
            self.enabled
            if hasattr(self, "enabled")
            else None
        )
        _debit_enabled=(
            self.debit_enabled
            if hasattr(self, "debit_enabled")
            else None
        )
        _prepaid_enabled=(
            self.prepaid_enabled
            if hasattr(self, "prepaid_enabled")
            else None
        )
        _debit_authorization_enabled=(
            self.debit_authorization_enabled
            if hasattr(self, "debit_authorization_enabled")
            else None
        )
        _prepaid_authorization_enabled=(
            self.prepaid_authorization_enabled
            if hasattr(self, "prepaid_authorization_enabled")
            else None
        )
        _forbidden_card_brands=(
            self.forbidden_card_brands
            if hasattr(self, "forbidden_card_brands")
            else None
        )
        _allowed_countries_by_ip=(
            self.allowed_countries_by_ip
            if hasattr(self, "allowed_countries_by_ip")
            else None
        )
        _foreign_cards_allowed=(
            self.foreign_cards_allowed
            if hasattr(self, "foreign_cards_allowed")
            else None
        )
        _fail_on_new_email=(
            self.fail_on_new_email
            if hasattr(self, "fail_on_new_email")
            else None
        )
        _card_limit=(
            self.card_limit
            if hasattr(self, "card_limit")
            else None
        )
        _allow_empty_cvv=(
            self.allow_empty_cvv
            if hasattr(self, "allow_empty_cvv")
            else None
        )
        _only_direct_currency=(
            self.only_direct_currency
            if hasattr(self, "only_direct_currency")
            else None
        )
        _three_ds_required=(
            self.three_ds_required
            if hasattr(self, "three_ds_required")
            else None
        )
        _three_ds_address_required=(
            self.three_ds_address_required
            if hasattr(self, "three_ds_address_required")
            else None
        )
        _three_ds_skip_enabled=(
            self.three_ds_skip_enabled
            if hasattr(self, "three_ds_skip_enabled")
            else None
        )
        _allow_direct_token_creation=(
            self.allow_direct_token_creation
            if hasattr(self, "allow_direct_token_creation")
            else None
        )
        _three_ds_phone_number_required=(
            self.three_ds_phone_number_required
            if hasattr(self, "three_ds_phone_number_required")
            else None
        )
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"enabled={_enabled!r}, "
            f"debit_enabled={_debit_enabled!r}, "
            f"prepaid_enabled={_prepaid_enabled!r}, "
            f"debit_authorization_enabled={_debit_authorization_enabled!r}, "
            f"prepaid_authorization_enabled={_prepaid_authorization_enabled!r}, "
            f"forbidden_card_brands={_forbidden_card_brands!r}, "
            f"allowed_countries_by_ip={_allowed_countries_by_ip!r}, "
            f"foreign_cards_allowed={_foreign_cards_allowed!r}, "
            f"fail_on_new_email={_fail_on_new_email!r}, "
            f"card_limit={_card_limit!r}, "
            f"allow_empty_cvv={_allow_empty_cvv!r}, "
            f"only_direct_currency={_only_direct_currency!r}, "
            f"three_ds_required={_three_ds_required!r}, "
            f"three_ds_address_required={_three_ds_address_required!r}, "
            f"three_ds_skip_enabled={_three_ds_skip_enabled!r}, "
            f"allow_direct_token_creation={_allow_direct_token_creation!r}, "
            f"three_ds_phone_number_required={_three_ds_phone_number_required!r}, "
            f"additional_properties={_additional_properties!r}, "
            f")"
        )

    def __str__(self):
        """Return a human-readable string representation."""
        _enabled=(
            self.enabled
            if hasattr(self, "enabled")
            else None
        )
        _debit_enabled=(
            self.debit_enabled
            if hasattr(self, "debit_enabled")
            else None
        )
        _prepaid_enabled=(
            self.prepaid_enabled
            if hasattr(self, "prepaid_enabled")
            else None
        )
        _debit_authorization_enabled=(
            self.debit_authorization_enabled
            if hasattr(self, "debit_authorization_enabled")
            else None
        )
        _prepaid_authorization_enabled=(
            self.prepaid_authorization_enabled
            if hasattr(self, "prepaid_authorization_enabled")
            else None
        )
        _forbidden_card_brands=(
            self.forbidden_card_brands
            if hasattr(self, "forbidden_card_brands")
            else None
        )
        _allowed_countries_by_ip=(
            self.allowed_countries_by_ip
            if hasattr(self, "allowed_countries_by_ip")
            else None
        )
        _foreign_cards_allowed=(
            self.foreign_cards_allowed
            if hasattr(self, "foreign_cards_allowed")
            else None
        )
        _fail_on_new_email=(
            self.fail_on_new_email
            if hasattr(self, "fail_on_new_email")
            else None
        )
        _card_limit=(
            self.card_limit
            if hasattr(self, "card_limit")
            else None
        )
        _allow_empty_cvv=(
            self.allow_empty_cvv
            if hasattr(self, "allow_empty_cvv")
            else None
        )
        _only_direct_currency=(
            self.only_direct_currency
            if hasattr(self, "only_direct_currency")
            else None
        )
        _three_ds_required=(
            self.three_ds_required
            if hasattr(self, "three_ds_required")
            else None
        )
        _three_ds_address_required=(
            self.three_ds_address_required
            if hasattr(self, "three_ds_address_required")
            else None
        )
        _three_ds_skip_enabled=(
            self.three_ds_skip_enabled
            if hasattr(self, "three_ds_skip_enabled")
            else None
        )
        _allow_direct_token_creation=(
            self.allow_direct_token_creation
            if hasattr(self, "allow_direct_token_creation")
            else None
        )
        _three_ds_phone_number_required=(
            self.three_ds_phone_number_required
            if hasattr(self, "three_ds_phone_number_required")
            else None
        )
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"enabled={_enabled!s}, "
            f"debit_enabled={_debit_enabled!s}, "
            f"prepaid_enabled={_prepaid_enabled!s}, "
            f"debit_authorization_enabled={_debit_authorization_enabled!s}, "
            f"prepaid_authorization_enabled={_prepaid_authorization_enabled!s}, "
            f"forbidden_card_brands={_forbidden_card_brands!s}, "
            f"allowed_countries_by_ip={_allowed_countries_by_ip!s}, "
            f"foreign_cards_allowed={_foreign_cards_allowed!s}, "
            f"fail_on_new_email={_fail_on_new_email!s}, "
            f"card_limit={_card_limit!s}, "
            f"allow_empty_cvv={_allow_empty_cvv!s}, "
            f"only_direct_currency={_only_direct_currency!s}, "
            f"three_ds_required={_three_ds_required!s}, "
            f"three_ds_address_required={_three_ds_address_required!s}, "
            f"three_ds_skip_enabled={_three_ds_skip_enabled!s}, "
            f"allow_direct_token_creation={_allow_direct_token_creation!s}, "
            f"three_ds_phone_number_required={_three_ds_phone_number_required!s}, "
            f"additional_properties={_additional_properties!s}, "
            f")"
        )
