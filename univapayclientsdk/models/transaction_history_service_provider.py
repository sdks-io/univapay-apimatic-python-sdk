"""univapay_client_sdk.

This file was automatically generated for Univapay by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

# ruff: noqa: E501

class TransactionHistoryServiceProvider(object):
    """Implementation of the 'TransactionHistoryServiceProvider' enum.

    The processor or service provider that handled the payment.

    Attributes:
        CREDIT: The enum member of type str.
        CONVENIENCE: The enum member of type str.
        BANK_TRANSFER: The enum member of type str.
        PAIDY: The enum member of type str.
        PAY_PAY: The enum member of type str.
        ALIPAY: The enum member of type str.
        WE_CHAT: The enum member of type str.
        DOCOMO: The enum member of type str.
        MERCARI: The enum member of type str.
        AU: The enum member of type str.
        RAKUTEN: The enum member of type str.
        BARTONG: The enum member of type str.
        JKOPAY: The enum member of type str.
        GINKO_PAY: The enum member of type str.
        AEON_PAY: The enum member of type str.
        EROMNET: The enum member of type str.
        TEST: The enum member of type str.

    """

    CREDIT = "credit"

    CONVENIENCE = "convenience"

    BANK_TRANSFER = "bank_transfer"

    PAIDY = "paidy"

    PAY_PAY = "pay_pay"

    ALIPAY = "alipay"

    WE_CHAT = "we_chat"

    DOCOMO = "docomo"

    MERCARI = "mercari"

    AU = "au"

    RAKUTEN = "rakuten"

    BARTONG = "bartong"

    JKOPAY = "jkopay"

    GINKO_PAY = "ginko_pay"

    AEON_PAY = "aeon_pay"

    EROMNET = "eromnet"

    TEST = "test"

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
