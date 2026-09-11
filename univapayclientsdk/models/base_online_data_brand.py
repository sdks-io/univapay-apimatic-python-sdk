"""univapay_client_sdk.

This file was automatically generated for Univapay by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

# ruff: noqa: E501

class BaseOnlineDataBrand(object):
    """Implementation of the 'BaseOnlineDataBrand' enum.

    Base Online Data Brand schema. `alipay_china`, `alipay_hk`, `gcash`, `dana`,
    `truemoney`, `kakaopay`, `tng`, `rabbit_line_pay`, `bpi`, `boost`, `tinaba`,
    `naver_pay`, `toss_pay`, `maya`, `grab_sg`, `kredivo_id`, `k_plus`, and
    `kaspi_kz` are Alipay+ regional wallets routed through the `alipay_plus_online`
    gateway family.

    Attributes:
        ALIPAY_ONLINE: The enum member of type str.
        ALIPAY_PLUS_ONLINE: The enum member of type str.
        PAY_PAY_ONLINE: The enum member of type str.
        WE_CHAT_ONLINE: The enum member of type str.
        D_BARAI_ONLINE: The enum member of type str.
        ALIPAY_CHINA: The enum member of type str.
        ALIPAY_HK: The enum member of type str.
        GCASH: The enum member of type str.
        DANA: The enum member of type str.
        TRUEMONEY: The enum member of type str.
        KAKAOPAY: The enum member of type str.
        TNG: The enum member of type str.
        RABBIT_LINE_PAY: The enum member of type str.
        BPI: The enum member of type str.
        BOOST: The enum member of type str.
        TINABA: The enum member of type str.
        NAVER_PAY: The enum member of type str.
        TOSS_PAY: The enum member of type str.
        MAYA: The enum member of type str.
        GRAB_SG: The enum member of type str.
        KREDIVO_ID: The enum member of type str.
        K_PLUS: The enum member of type str.
        KASPI_KZ: The enum member of type str.

    """

    _all_values = ["alipay_online", "alipay_plus_online", "pay_pay_online", "we_chat_online",
        "d_barai_online", "alipay_china", "alipay_hk", "gcash", "dana", "truemoney",
        "kakaopay", "tng", "rabbit_line_pay", "bpi", "boost", "tinaba", "naver_pay",
        "toss_pay", "maya", "grab_sg", "kredivo_id", "k_plus", "kaspi_kz"]
    ALIPAY_ONLINE = "alipay_online"

    ALIPAY_PLUS_ONLINE = "alipay_plus_online"

    PAY_PAY_ONLINE = "pay_pay_online"

    WE_CHAT_ONLINE = "we_chat_online"

    D_BARAI_ONLINE = "d_barai_online"

    ALIPAY_CHINA = "alipay_china"

    ALIPAY_HK = "alipay_hk"

    GCASH = "gcash"

    DANA = "dana"

    TRUEMONEY = "truemoney"

    KAKAOPAY = "kakaopay"

    TNG = "tng"

    RABBIT_LINE_PAY = "rabbit_line_pay"

    BPI = "bpi"

    BOOST = "boost"

    TINABA = "tinaba"

    NAVER_PAY = "naver_pay"

    TOSS_PAY = "toss_pay"

    MAYA = "maya"

    GRAB_SG = "grab_sg"

    KREDIVO_ID = "kredivo_id"

    K_PLUS = "k_plus"

    KASPI_KZ = "kaspi_kz"

    @classmethod
    def validate(cls, value):
        """Validate value contains in enum

        Args:
            value: the value to be validated

        Returns:
            boolean : if value is valid enum values.

        """
        return value in cls._all_values

    @classmethod
    def from_value(cls, value, default=None):
        """Return the matching enum value for the given input."""
        if value is None:
            return default

        # If numeric and matches directly
        if isinstance(value, int):
            for name, val in cls.__dict__.items():
                if not name.startswith("_") and val == value:
                    return val

        # If string, perform case-insensitive match
        if isinstance(value, str):
            value_lower = value.lower()
            for name, val in cls.__dict__.items():
                if not name.startswith("_") and (
                    name.lower() == value_lower or str(val).lower() == value_lower
                ):
                    return val

        # Fallback to default
        return default
