"""univapay_client_sdk.

This file was automatically generated for Univapay by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

# ruff: noqa: E501

class BaseKonbiniDataConvenienceStore(object):
    """Implementation of the 'BaseKonbiniDataConvenienceStore' enum.

    Base Konbini Data Convenience Store schema.

    Attributes:
        SEVEN_ELEVEN: The enum member of type str.
        FAMILY_MART: The enum member of type str.
        LAWSON: The enum member of type str.
        MINI_STOP: The enum member of type str.
        SEICO_MART: The enum member of type str.
        PAY_EASY: The enum member of type str.
        DAILY_YAMAZAKI: The enum member of type str.
        YAMAZAKI_DAILY_STORE: The enum member of type str.

    """

    _all_values = ["seven_eleven", "family_mart", "lawson", "mini_stop",
        "seico_mart", "pay_easy", "daily_yamazaki", "yamazaki_daily_store"]
    SEVEN_ELEVEN = "seven_eleven"

    FAMILY_MART = "family_mart"

    LAWSON = "lawson"

    MINI_STOP = "mini_stop"

    SEICO_MART = "seico_mart"

    PAY_EASY = "pay_easy"

    DAILY_YAMAZAKI = "daily_yamazaki"

    YAMAZAKI_DAILY_STORE = "yamazaki_daily_store"

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
