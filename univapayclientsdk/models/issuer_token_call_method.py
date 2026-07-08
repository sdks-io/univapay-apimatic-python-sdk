"""univapay_client_sdk.

This file was automatically generated for Univapay by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

# ruff: noqa: E501

class IssuerTokenCallMethod(object):
    """Implementation of the 'IssuerTokenCallMethod' enum.

    (Online) How the client should execute the token.  - `sdk` / `app`: Direct use in
    native app environments/SDKs. - `web`: Direct use in special extended browser
    environments. - `http_get` / `http_post`: Execute directly in a new browser
    window or iframe.

    Attributes:
        HTTP_GET: The enum member of type str.
        HTTP_POST: The enum member of type str.
        SDK: The enum member of type str.
        WEB: The enum member of type str.
        APP: The enum member of type str.

    """

    HTTP_GET = "http_get"

    HTTP_POST = "http_post"

    SDK = "sdk"

    WEB = "web"

    APP = "app"

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
