"""univapay_client_sdk.

This file was automatically generated for Univapay by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

# ruff: noqa: E501

class BaseOnlineDataBrand(object):
    """Implementation of the 'BaseOnlineDataBrand' enum.

    Base Online Data Brand schema.

    Attributes:
        ALIPAY_ONLINE: The enum member of type str.
        ALIPAY_PLUS_ONLINE: The enum member of type str.
        PAY_PAY_ONLINE: The enum member of type str.
        WE_CHAT_ONLINE: The enum member of type str.
        D_BARAI_ONLINE: The enum member of type str.

    """

    _all_values = ["alipay_online", "alipay_plus_online", "pay_pay_online",
        "we_chat_online", "d_barai_online"]
    ALIPAY_ONLINE = "alipay_online"

    ALIPAY_PLUS_ONLINE = "alipay_plus_online"

    PAY_PAY_ONLINE = "pay_pay_online"

    WE_CHAT_ONLINE = "we_chat_online"

    D_BARAI_ONLINE = "d_barai_online"

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
