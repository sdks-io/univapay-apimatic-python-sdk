"""univapay_client_sdk.

This file was automatically generated for Univapay by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

# ruff: noqa: E501
from univapayclientsdk.api_helper import APIHelper


class CheckoutSupportedBrand(object):
    """Implementation of the 'CheckoutSupportedBrand' model.

    Feature support and capability flags for a single payment-type / brand
    combination the store can accept.

    Attributes:
        payment_type (CheckoutPaymentType): Payment type identifier used throughout
            the checkout configuration.
        brand (str): Brand identifier for `payment_type`. For `card` and `apple_pay`,
            one of the common `CardBrand` values (`visa`, `mastercard`,
            `american_express`, `maestro`, `discover`, `jcb`, `diners_club`,
            `private_label`, `unionpay`) or an `unmapped_<raw value>` fallback. For
            `qr_scan`, a QR-CPM brand (e.g. `pay_pay`, `we_chat`, `qq`, `line_pay`,
            `au_pay`, `alipay_china`). For `qr_merchant`, a QR-MPM brand (e.g.
            `rakuten_pay_merchant`, `alipay_merchant_qr`, `pay_pay_merchant`,
            `d_barai_mpm`, `we_chat_mpm`). For `online`, an online-redirect brand
            (e.g. `alipay_online`, `pay_pay_online`, `we_chat_online`,
            `d_barai_online`, `kakaopay`). For `konbini`, a convenience-store brand
            (e.g. `seven_eleven`, `family_mart`, `lawson`). For `paidy` and
            `bank_transfer`, the payment type's own identifier. The full brand
            catalogue is large and gateway-dependent — treat this as an open string,
            not a fixed set.
        card_brand (str): Legacy alias of `brand`. Present only when `payment_type`
            is `card` or `apple_pay`.
        qr_brand (str): Legacy alias of `brand`. Present only when `payment_type` is
            `qr_merchant`.
        online_brand (str): Legacy alias of `brand`. Present only when `payment_type`
            is `online`.
        dynamic_info (bool): Whether the brand's supported feature set is resolved
            dynamically.
        support_auth_capture (bool): Whether the brand supports separate
            authorization and capture.
        requires_full_name (bool): Whether the brand requires the cardholder's full
            name.
        requires_cvv (bool): Whether the brand requires a CVV.
        countries_allowed (List[str]): ISO 3166-1 alpha-2 country codes allowed for
            this brand. `null` when unrestricted.
        supported_currencies (List[str]): ISO-4217 currency codes supported by this
            brand. `null` when unrestricted.
        cvv_auth (bool): Whether this brand supports CVV-only authorization.
        installment_capable (bool): Whether this brand supports installment plans.
        mcp_capable (bool): Whether this brand supports multi-currency pricing.
        mcp_only (bool): Whether this brand is only available through multi-currency
            pricing.
        additional_properties (Dict[str, Any]): The additional properties for the
            model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "payment_type": "payment_type",
        "brand": "brand",
        "card_brand": "card_brand",
        "qr_brand": "qr_brand",
        "online_brand": "online_brand",
        "dynamic_info": "dynamic_info",
        "support_auth_capture": "support_auth_capture",
        "requires_full_name": "requires_full_name",
        "requires_cvv": "requires_cvv",
        "countries_allowed": "countries_allowed",
        "supported_currencies": "supported_currencies",
        "cvv_auth": "cvv_auth",
        "installment_capable": "installment_capable",
        "mcp_capable": "mcp_capable",
        "mcp_only": "mcp_only",
    }

    _optionals = [
        "payment_type",
        "brand",
        "card_brand",
        "qr_brand",
        "online_brand",
        "dynamic_info",
        "support_auth_capture",
        "requires_full_name",
        "requires_cvv",
        "countries_allowed",
        "supported_currencies",
        "cvv_auth",
        "installment_capable",
        "mcp_capable",
        "mcp_only",
    ]

    _nullables = [
        "countries_allowed",
        "supported_currencies",
    ]

    def __init__(
        self,
        payment_type=APIHelper.SKIP,
        brand=APIHelper.SKIP,
        card_brand=APIHelper.SKIP,
        qr_brand=APIHelper.SKIP,
        online_brand=APIHelper.SKIP,
        dynamic_info=APIHelper.SKIP,
        support_auth_capture=APIHelper.SKIP,
        requires_full_name=APIHelper.SKIP,
        requires_cvv=APIHelper.SKIP,
        countries_allowed=APIHelper.SKIP,
        supported_currencies=APIHelper.SKIP,
        cvv_auth=APIHelper.SKIP,
        installment_capable=APIHelper.SKIP,
        mcp_capable=APIHelper.SKIP,
        mcp_only=APIHelper.SKIP,
        additional_properties=None):
        """Initialize a CheckoutSupportedBrand instance."""
        # Initialize members of the class
        if payment_type is not APIHelper.SKIP:
            self.payment_type = payment_type
        if brand is not APIHelper.SKIP:
            self.brand = brand
        if card_brand is not APIHelper.SKIP:
            self.card_brand = card_brand
        if qr_brand is not APIHelper.SKIP:
            self.qr_brand = qr_brand
        if online_brand is not APIHelper.SKIP:
            self.online_brand = online_brand
        if dynamic_info is not APIHelper.SKIP:
            self.dynamic_info = dynamic_info
        if support_auth_capture is not APIHelper.SKIP:
            self.support_auth_capture = support_auth_capture
        if requires_full_name is not APIHelper.SKIP:
            self.requires_full_name = requires_full_name
        if requires_cvv is not APIHelper.SKIP:
            self.requires_cvv = requires_cvv
        if countries_allowed is not APIHelper.SKIP:
            self.countries_allowed = countries_allowed
        if supported_currencies is not APIHelper.SKIP:
            self.supported_currencies = supported_currencies
        if cvv_auth is not APIHelper.SKIP:
            self.cvv_auth = cvv_auth
        if installment_capable is not APIHelper.SKIP:
            self.installment_capable = installment_capable
        if mcp_capable is not APIHelper.SKIP:
            self.mcp_capable = mcp_capable
        if mcp_only is not APIHelper.SKIP:
            self.mcp_only = mcp_only

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
        payment_type =\
            dictionary.get("payment_type")\
            if dictionary.get("payment_type")\
                else APIHelper.SKIP
        brand =\
            dictionary.get("brand")\
            if dictionary.get("brand")\
                else APIHelper.SKIP
        card_brand =\
            dictionary.get("card_brand")\
            if dictionary.get("card_brand")\
                else APIHelper.SKIP
        qr_brand =\
            dictionary.get("qr_brand")\
            if dictionary.get("qr_brand")\
                else APIHelper.SKIP
        online_brand =\
            dictionary.get("online_brand")\
            if dictionary.get("online_brand")\
                else APIHelper.SKIP
        dynamic_info =\
            dictionary.get("dynamic_info")\
            if "dynamic_info" in dictionary.keys()\
                else APIHelper.SKIP
        support_auth_capture =\
            dictionary.get("support_auth_capture")\
            if "support_auth_capture" in dictionary.keys()\
                else APIHelper.SKIP
        requires_full_name =\
            dictionary.get("requires_full_name")\
            if "requires_full_name" in dictionary.keys()\
                else APIHelper.SKIP
        requires_cvv =\
            dictionary.get("requires_cvv")\
            if "requires_cvv" in dictionary.keys()\
                else APIHelper.SKIP
        countries_allowed =\
            dictionary.get("countries_allowed")\
            if "countries_allowed" in dictionary.keys()\
                else APIHelper.SKIP
        supported_currencies =\
            dictionary.get("supported_currencies")\
            if "supported_currencies" in dictionary.keys()\
                else APIHelper.SKIP
        cvv_auth =\
            dictionary.get("cvv_auth")\
            if "cvv_auth" in dictionary.keys()\
                else APIHelper.SKIP
        installment_capable =\
            dictionary.get("installment_capable")\
            if "installment_capable" in dictionary.keys()\
                else APIHelper.SKIP
        mcp_capable =\
            dictionary.get("mcp_capable")\
            if "mcp_capable" in dictionary.keys()\
                else APIHelper.SKIP
        mcp_only =\
            dictionary.get("mcp_only")\
            if "mcp_only" in dictionary.keys()\
                else APIHelper.SKIP

        additional_properties = APIHelper.get_additional_properties(
            dictionary={k: v for k, v in dictionary.items()
                        if k not in cls._names.values()},
            unboxing_function=lambda value: value)

        # Return an object of this model
        return cls(payment_type,
                   brand,
                   card_brand,
                   qr_brand,
                   online_brand,
                   dynamic_info,
                   support_auth_capture,
                   requires_full_name,
                   requires_cvv,
                   countries_allowed,
                   supported_currencies,
                   cvv_auth,
                   installment_capable,
                   mcp_capable,
                   mcp_only,
                   additional_properties)

    def __repr__(self):
        """Return a unambiguous string representation."""
        _payment_type=(
            self.payment_type
            if hasattr(self, "payment_type")
            else None
        )
        _brand=(
            self.brand
            if hasattr(self, "brand")
            else None
        )
        _card_brand=(
            self.card_brand
            if hasattr(self, "card_brand")
            else None
        )
        _qr_brand=(
            self.qr_brand
            if hasattr(self, "qr_brand")
            else None
        )
        _online_brand=(
            self.online_brand
            if hasattr(self, "online_brand")
            else None
        )
        _dynamic_info=(
            self.dynamic_info
            if hasattr(self, "dynamic_info")
            else None
        )
        _support_auth_capture=(
            self.support_auth_capture
            if hasattr(self, "support_auth_capture")
            else None
        )
        _requires_full_name=(
            self.requires_full_name
            if hasattr(self, "requires_full_name")
            else None
        )
        _requires_cvv=(
            self.requires_cvv
            if hasattr(self, "requires_cvv")
            else None
        )
        _countries_allowed=(
            self.countries_allowed
            if hasattr(self, "countries_allowed")
            else None
        )
        _supported_currencies=(
            self.supported_currencies
            if hasattr(self, "supported_currencies")
            else None
        )
        _cvv_auth=(
            self.cvv_auth
            if hasattr(self, "cvv_auth")
            else None
        )
        _installment_capable=(
            self.installment_capable
            if hasattr(self, "installment_capable")
            else None
        )
        _mcp_capable=(
            self.mcp_capable
            if hasattr(self, "mcp_capable")
            else None
        )
        _mcp_only=(
            self.mcp_only
            if hasattr(self, "mcp_only")
            else None
        )
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"payment_type={_payment_type!r}, "
            f"brand={_brand!r}, "
            f"card_brand={_card_brand!r}, "
            f"qr_brand={_qr_brand!r}, "
            f"online_brand={_online_brand!r}, "
            f"dynamic_info={_dynamic_info!r}, "
            f"support_auth_capture={_support_auth_capture!r}, "
            f"requires_full_name={_requires_full_name!r}, "
            f"requires_cvv={_requires_cvv!r}, "
            f"countries_allowed={_countries_allowed!r}, "
            f"supported_currencies={_supported_currencies!r}, "
            f"cvv_auth={_cvv_auth!r}, "
            f"installment_capable={_installment_capable!r}, "
            f"mcp_capable={_mcp_capable!r}, "
            f"mcp_only={_mcp_only!r}, "
            f"additional_properties={_additional_properties!r}, "
            f")"
        )

    def __str__(self):
        """Return a human-readable string representation."""
        _payment_type=(
            self.payment_type
            if hasattr(self, "payment_type")
            else None
        )
        _brand=(
            self.brand
            if hasattr(self, "brand")
            else None
        )
        _card_brand=(
            self.card_brand
            if hasattr(self, "card_brand")
            else None
        )
        _qr_brand=(
            self.qr_brand
            if hasattr(self, "qr_brand")
            else None
        )
        _online_brand=(
            self.online_brand
            if hasattr(self, "online_brand")
            else None
        )
        _dynamic_info=(
            self.dynamic_info
            if hasattr(self, "dynamic_info")
            else None
        )
        _support_auth_capture=(
            self.support_auth_capture
            if hasattr(self, "support_auth_capture")
            else None
        )
        _requires_full_name=(
            self.requires_full_name
            if hasattr(self, "requires_full_name")
            else None
        )
        _requires_cvv=(
            self.requires_cvv
            if hasattr(self, "requires_cvv")
            else None
        )
        _countries_allowed=(
            self.countries_allowed
            if hasattr(self, "countries_allowed")
            else None
        )
        _supported_currencies=(
            self.supported_currencies
            if hasattr(self, "supported_currencies")
            else None
        )
        _cvv_auth=(
            self.cvv_auth
            if hasattr(self, "cvv_auth")
            else None
        )
        _installment_capable=(
            self.installment_capable
            if hasattr(self, "installment_capable")
            else None
        )
        _mcp_capable=(
            self.mcp_capable
            if hasattr(self, "mcp_capable")
            else None
        )
        _mcp_only=(
            self.mcp_only
            if hasattr(self, "mcp_only")
            else None
        )
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"payment_type={_payment_type!s}, "
            f"brand={_brand!s}, "
            f"card_brand={_card_brand!s}, "
            f"qr_brand={_qr_brand!s}, "
            f"online_brand={_online_brand!s}, "
            f"dynamic_info={_dynamic_info!s}, "
            f"support_auth_capture={_support_auth_capture!s}, "
            f"requires_full_name={_requires_full_name!s}, "
            f"requires_cvv={_requires_cvv!s}, "
            f"countries_allowed={_countries_allowed!s}, "
            f"supported_currencies={_supported_currencies!s}, "
            f"cvv_auth={_cvv_auth!s}, "
            f"installment_capable={_installment_capable!s}, "
            f"mcp_capable={_mcp_capable!s}, "
            f"mcp_only={_mcp_only!s}, "
            f"additional_properties={_additional_properties!s}, "
            f")"
        )
