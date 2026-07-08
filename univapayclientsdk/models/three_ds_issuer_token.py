"""univapay_client_sdk.

This file was automatically generated for Univapay by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

# ruff: noqa: E501
from univapayclientsdk.api_helper import APIHelper
from univapayclientsdk.models.issuer_token_payload import (
    IssuerTokenPayload,
)


class ThreeDsIssuerToken(object):
    """Implementation of the 'ThreeDsIssuerToken' model.

    3-D Secure issuer token payload.

    Attributes:
        payment_type (str): Only 'card' is supported for 3-D Secure issuer tokens.
        issuer_token (str): The 3-D Secure authentication URL to which the client
            must send the request.
        call_method (str): Execution method. Currently, only 'http_post' is supported.
        payload (IssuerTokenPayload): Key-value pairs required to complete the
            payment action, or null if not applicable. Used when `call_method` is
            `http_post`. When present, this JSON must be converted by the client to
            match the expected `content_type` (e.g., transformed into an
            `application/x-www-form-urlencoded` string) before sending the POST
            request.
        content_type (str): The expected content type of the payload required by the
            card issuer's endpoint  (e.g., 'application/x-www-form-urlencoded;
            charset=UTF-8').
        additional_properties (Dict[str, Any]): The additional properties for the
            model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "payment_type": "payment_type",
        "issuer_token": "issuer_token",
        "call_method": "call_method",
        "content_type": "content_type",
        "payload": "payload",
    }

    _optionals = [
        "payload",
    ]

    _nullables = [
        "payload",
    ]

    def __init__(
        self,
        issuer_token=None,
        content_type=None,
        payload=APIHelper.SKIP,
        additional_properties=None):
        """Initialize a ThreeDsIssuerToken instance."""
        # Initialize members of the class
        self.payment_type = "card"
        self.issuer_token = issuer_token
        self.call_method = "http_post"
        if payload is not APIHelper.SKIP:
            self.payload = payload
        self.content_type = content_type

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
        issuer_token =\
            dictionary.get("issuer_token")\
            if dictionary.get("issuer_token")\
                else None
        content_type =\
            dictionary.get("content_type")\
            if dictionary.get("content_type")\
                else None
        if "payload" in dictionary.keys():
            payload =\
                IssuerTokenPayload.from_dictionary(
                dictionary.get("payload"))\
                if dictionary.get("payload") else None
        else:
            payload = APIHelper.SKIP

        additional_properties = APIHelper.get_additional_properties(
            dictionary={k: v for k, v in dictionary.items()
                        if k not in cls._names.values()},
            unboxing_function=lambda value: value)

        # Return an object of this model
        return cls(issuer_token,
                   content_type,
                   payload,
                   additional_properties)

    def __repr__(self):
        """Return a unambiguous string representation."""
        _payment_type=self.payment_type
        _issuer_token=self.issuer_token
        _call_method=self.call_method
        _payload=(
            self.payload
            if hasattr(self, "payload")
            else None
        )
        _content_type=self.content_type
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"payment_type={_payment_type!r}, "
            f"issuer_token={_issuer_token!r}, "
            f"call_method={_call_method!r}, "
            f"payload={_payload!r}, "
            f"content_type={_content_type!r}, "
            f"additional_properties={_additional_properties!r}, "
            f")"
        )

    def __str__(self):
        """Return a human-readable string representation."""
        _payment_type=self.payment_type
        _issuer_token=self.issuer_token
        _call_method=self.call_method
        _payload=(
            self.payload
            if hasattr(self, "payload")
            else None
        )
        _content_type=self.content_type
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"payment_type={_payment_type!s}, "
            f"issuer_token={_issuer_token!s}, "
            f"call_method={_call_method!s}, "
            f"payload={_payload!s}, "
            f"content_type={_content_type!s}, "
            f"additional_properties={_additional_properties!s}, "
            f")"
        )
