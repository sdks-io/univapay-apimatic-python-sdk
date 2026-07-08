"""univapay_client_sdk.

This file was automatically generated for Univapay by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

# ruff: noqa: E501
from univapayclientsdk.api_helper import APIHelper
from univapayclientsdk.exceptions.api_exception import (
    ApiException,
)
from univapayclientsdk.models.api_error_detail import (
    ApiErrorDetail,
)


class ApiErrorException(ApiException):
    def __init__(self, reason, response):
        """Initialize ApiErrorException object.

        Args:
            reason (string): The reason (or error message) for the Exception
                to be raised.
            response (HttpResponse): The HttpResponse of the API call.

        """
        super(ApiErrorException, self).__init__(reason, response)
        dictionary = APIHelper.json_deserialize(self.response.text)
        if isinstance(dictionary, dict):
            self.unbox(dictionary)

    def unbox(self, dictionary):
        """Populate the properties of this object by extracting them from a dictionary.

        Args:
            dictionary (dictionary): A dictionary representation of the object as
            obtained from the deserialization of the server's response. The keys
            MUST match property names in the API description.

        """
        self.code =\
            dictionary.get("code")\
            if dictionary.get("code")\
                else None
        self.errors = None
        if dictionary.get("errors") is not None:
            self.errors = [
                ApiErrorDetail.from_dictionary(x)
                    for x in dictionary.get("errors")
            ]
        else:
            self.errors = None


    def __str__(self):
        """Return a human-readable string representation."""
        _status=self.status
        _code=self.code
        _errors=(
            self.errors
            if hasattr(self, "errors")
            else None
        )
        _base_str = super().__str__()
        _base_str = _base_str[_base_str.find("(") + 1:-1]
        return (
            f"{self.__class__.__name__}("
            f"base_str={_base_str!s}, "
            f"status={_status!s}, "
            f"code={_code!s}, "
            f"errors={_errors!s}, "
            f")"
        )
