"""univapay_client_sdk.

This file was automatically generated for Univapay by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

# ruff: noqa: E501
from univapayclientsdk.api_helper import APIHelper
from univapayclientsdk.models.issuer_token_payload import (
    IssuerTokenPayload,
)


class IssuerToken(object):
    """Implementation of the 'IssuerToken' model.

    Issuer token or bank transfer instruction payload.

    Attributes:
        payment_type (IssuerTokenPaymentType): The type of payment method for the
            charge.
        issuer_token (str): (Online) The token or payment URL provided by the payment
            provider for the consumer to execute.
        call_method (IssuerTokenCallMethod): (Online) How the client should execute
            the token.  - `sdk` / `app`: Direct use in native app environments/SDKs.
            - `web`: Direct use in special extended browser environments. -
            `http_get` / `http_post`: Execute directly in a new browser window or
            iframe.
        payload (IssuerTokenPayload): Key-value pairs required to complete the
            payment action, or null if not applicable. Used when `call_method` is
            `http_post`. When present, this JSON must be converted by the client to
            match the expected `content_type` (e.g., transformed into an
            `application/x-www-form-urlencoded` string) before sending the POST
            request.
        account_id (str): (Bank Transfer) Unique ID of the bank account issued by the
            connected system.
        branch_code (str): (Bank Transfer) Branch code.
        branch_name (str): (Bank Transfer) Branch name.
        account_holder_name (str): (Bank Transfer) Account holder name.
        account_number (str): (Bank Transfer) Account number.
        additional_properties (Dict[str, Any]): The additional properties for the
            model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "payment_type": "payment_type",
        "issuer_token": "issuer_token",
        "call_method": "call_method",
        "payload": "payload",
        "account_id": "account_id",
        "branch_code": "branch_code",
        "branch_name": "branch_name",
        "account_holder_name": "account_holder_name",
        "account_number": "account_number",
    }

    _optionals = [
        "issuer_token",
        "call_method",
        "payload",
        "account_id",
        "branch_code",
        "branch_name",
        "account_holder_name",
        "account_number",
    ]

    _nullables = [
        "issuer_token",
        "call_method",
        "payload",
        "account_id",
        "branch_code",
        "branch_name",
        "account_holder_name",
        "account_number",
    ]

    def __init__(
        self,
        payment_type=None,
        issuer_token=APIHelper.SKIP,
        call_method=APIHelper.SKIP,
        payload=APIHelper.SKIP,
        account_id=APIHelper.SKIP,
        branch_code=APIHelper.SKIP,
        branch_name=APIHelper.SKIP,
        account_holder_name=APIHelper.SKIP,
        account_number=APIHelper.SKIP,
        additional_properties=None):
        """Initialize a IssuerToken instance."""
        # Initialize members of the class
        self.payment_type = payment_type
        if issuer_token is not APIHelper.SKIP:
            self.issuer_token = issuer_token
        if call_method is not APIHelper.SKIP:
            self.call_method = call_method
        if payload is not APIHelper.SKIP:
            self.payload = payload
        if account_id is not APIHelper.SKIP:
            self.account_id = account_id
        if branch_code is not APIHelper.SKIP:
            self.branch_code = branch_code
        if branch_name is not APIHelper.SKIP:
            self.branch_name = branch_name
        if account_holder_name is not APIHelper.SKIP:
            self.account_holder_name = account_holder_name
        if account_number is not APIHelper.SKIP:
            self.account_number = account_number

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
                else None
        issuer_token =\
            dictionary.get("issuer_token")\
            if "issuer_token" in dictionary.keys()\
                else APIHelper.SKIP
        call_method =\
            dictionary.get("call_method")\
            if "call_method" in dictionary.keys()\
                else APIHelper.SKIP
        if "payload" in dictionary.keys():
            payload =\
                IssuerTokenPayload.from_dictionary(
                dictionary.get("payload"))\
                if dictionary.get("payload") else None
        else:
            payload = APIHelper.SKIP
        account_id =\
            dictionary.get("account_id")\
            if "account_id" in dictionary.keys()\
                else APIHelper.SKIP
        branch_code =\
            dictionary.get("branch_code")\
            if "branch_code" in dictionary.keys()\
                else APIHelper.SKIP
        branch_name =\
            dictionary.get("branch_name")\
            if "branch_name" in dictionary.keys()\
                else APIHelper.SKIP
        account_holder_name =\
            dictionary.get("account_holder_name")\
            if "account_holder_name" in dictionary.keys()\
                else APIHelper.SKIP
        account_number =\
            dictionary.get("account_number")\
            if "account_number" in dictionary.keys()\
                else APIHelper.SKIP

        additional_properties = APIHelper.get_additional_properties(
            dictionary={k: v for k, v in dictionary.items()
                        if k not in cls._names.values()},
            unboxing_function=lambda value: value)

        # Return an object of this model
        return cls(payment_type,
                   issuer_token,
                   call_method,
                   payload,
                   account_id,
                   branch_code,
                   branch_name,
                   account_holder_name,
                   account_number,
                   additional_properties)

    def __repr__(self):
        """Return a unambiguous string representation."""
        _payment_type=self.payment_type
        _issuer_token=(
            self.issuer_token
            if hasattr(self, "issuer_token")
            else None
        )
        _call_method=(
            self.call_method
            if hasattr(self, "call_method")
            else None
        )
        _payload=(
            self.payload
            if hasattr(self, "payload")
            else None
        )
        _account_id=(
            self.account_id
            if hasattr(self, "account_id")
            else None
        )
        _branch_code=(
            self.branch_code
            if hasattr(self, "branch_code")
            else None
        )
        _branch_name=(
            self.branch_name
            if hasattr(self, "branch_name")
            else None
        )
        _account_holder_name=(
            self.account_holder_name
            if hasattr(self, "account_holder_name")
            else None
        )
        _account_number=(
            self.account_number
            if hasattr(self, "account_number")
            else None
        )
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"payment_type={_payment_type!r}, "
            f"issuer_token={_issuer_token!r}, "
            f"call_method={_call_method!r}, "
            f"payload={_payload!r}, "
            f"account_id={_account_id!r}, "
            f"branch_code={_branch_code!r}, "
            f"branch_name={_branch_name!r}, "
            f"account_holder_name={_account_holder_name!r}, "
            f"account_number={_account_number!r}, "
            f"additional_properties={_additional_properties!r}, "
            f")"
        )

    def __str__(self):
        """Return a human-readable string representation."""
        _payment_type=self.payment_type
        _issuer_token=(
            self.issuer_token
            if hasattr(self, "issuer_token")
            else None
        )
        _call_method=(
            self.call_method
            if hasattr(self, "call_method")
            else None
        )
        _payload=(
            self.payload
            if hasattr(self, "payload")
            else None
        )
        _account_id=(
            self.account_id
            if hasattr(self, "account_id")
            else None
        )
        _branch_code=(
            self.branch_code
            if hasattr(self, "branch_code")
            else None
        )
        _branch_name=(
            self.branch_name
            if hasattr(self, "branch_name")
            else None
        )
        _account_holder_name=(
            self.account_holder_name
            if hasattr(self, "account_holder_name")
            else None
        )
        _account_number=(
            self.account_number
            if hasattr(self, "account_number")
            else None
        )
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"payment_type={_payment_type!s}, "
            f"issuer_token={_issuer_token!s}, "
            f"call_method={_call_method!s}, "
            f"payload={_payload!s}, "
            f"account_id={_account_id!s}, "
            f"branch_code={_branch_code!s}, "
            f"branch_name={_branch_name!s}, "
            f"account_holder_name={_account_holder_name!s}, "
            f"account_number={_account_number!s}, "
            f"additional_properties={_additional_properties!s}, "
            f")"
        )
