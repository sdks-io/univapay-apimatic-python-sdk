"""univapay_client_sdk.

This file was automatically generated for Univapay by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

# ruff: noqa: E501

class BaseOnlineDataCallMethod(object):
    """Implementation of the 'BaseOnlineDataCallMethod' enum.

    Base Online Data Call Method schema.

    Attributes:
        HTTP_GET: The enum member of type str.
        HTTP_POST: The enum member of type str.
        HTTP_GET_MOBILE: The enum member of type str.
        SDK: The enum member of type str.
        WEB: The enum member of type str.
        APP: The enum member of type str.

    """

    _all_values = ["http_get", "http_post", "http_get_mobile", "sdk", "web",
        "app"]
    HTTP_GET = "http_get"

    HTTP_POST = "http_post"

    HTTP_GET_MOBILE = "http_get_mobile"

    SDK = "sdk"

    WEB = "web"

    APP = "app"

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
