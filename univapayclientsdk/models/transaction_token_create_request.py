"""univapay_client_sdk.

This file was automatically generated for Univapay by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

# ruff: noqa: E501
from univapayclientsdk.api_helper import APIHelper
from univapayclientsdk.models.transaction_token_create_request_metadata import (
    TransactionTokenCreateRequestMetadata,
)
from univapayclientsdk.models.transaction_token_create_request_payment_type import (
    TransactionTokenCreateRequestPaymentType,
)
from univapayclientsdk.models.transaction_token_create_request_type import (
    TransactionTokenCreateRequestType,
)


class TransactionTokenCreateRequest(object):
    """Implementation of the 'TransactionTokenCreateRequest' model.

    Request payload for creating a transaction token, which represents a payment
    method to charge against.

    Attributes:
        payment_type (TransactionTokenCreateRequestPaymentType): Transaction Token
            Create Request Payment Type schema.
        mtype (TransactionTokenCreateRequestType): Transaction Token Create Request
            Type schema.
        email (str): Customer email address.
        usage_limit (str): Usage limit applied to the token.
        ip_address (str): Consumer's IPv4 address. **Required** when `data.brand` is
            `we_chat_online` and `data.call_method` is `web` or `http_get`.
        metadata (TransactionTokenCreateRequestMetadata): A free-form dictionary for
            custom metadata.
        data (TokenCreateCardData | TokenCreateKonbiniData | TokenCreateOnlineData |
            TokenCreateBankTransferData | TokenCreatePaidyData |
            TokenCreateQrScanData | TokenCreateQrMerchantData): Transaction Token
            Create Request Data schema.
        additional_properties (Dict[str, Any]): The additional properties for the
            model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "payment_type": "payment_type",
        "mtype": "type",
        "data": "data",
        "email": "email",
        "usage_limit": "usage_limit",
        "ip_address": "ip_address",
        "metadata": "metadata",
    }

    _optionals = [
        "email",
        "usage_limit",
        "ip_address",
        "metadata",
    ]

    def __init__(
        self,
        payment_type=None,
        mtype=None,
        data=None,
        email=APIHelper.SKIP,
        usage_limit=APIHelper.SKIP,
        ip_address=APIHelper.SKIP,
        metadata=APIHelper.SKIP,
        additional_properties=None):
        """Initialize a TransactionTokenCreateRequest instance."""
        # Initialize members of the class
        self.payment_type = payment_type
        self.mtype = mtype
        if email is not APIHelper.SKIP:
            self.email = email
        if usage_limit is not APIHelper.SKIP:
            self.usage_limit = usage_limit
        if ip_address is not APIHelper.SKIP:
            self.ip_address = ip_address
        if metadata is not APIHelper.SKIP:
            self.metadata = metadata
        self.data = data

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
        from univapayclientsdk.utilities.union_type_lookup import (
            UnionTypeLookUp,
        )

        if not isinstance(dictionary, dict) or dictionary is None:
            return None

        # Extract variables from the dictionary
        payment_type =\
            dictionary.get("payment_type")\
            if dictionary.get("payment_type")\
                else None
        mtype =\
            dictionary.get("type")\
            if dictionary.get("type")\
                else None
        data = APIHelper.deserialize_union_type(
            UnionTypeLookUp.get("TransactionTokenCreateRequestData"),
            dictionary.get("data"),
            False)\
            if dictionary.get("data") is not None\
            else None
        email =\
            dictionary.get("email")\
            if dictionary.get("email")\
                else APIHelper.SKIP
        usage_limit =\
            dictionary.get("usage_limit")\
            if dictionary.get("usage_limit")\
                else APIHelper.SKIP
        ip_address =\
            dictionary.get("ip_address")\
            if dictionary.get("ip_address")\
                else APIHelper.SKIP
        metadata =\
            TransactionTokenCreateRequestMetadata.from_dictionary(
                dictionary.get("metadata"))\
                if "metadata" in dictionary.keys()\
                else APIHelper.SKIP

        additional_properties = APIHelper.get_additional_properties(
            dictionary={k: v for k, v in dictionary.items()
                        if k not in cls._names.values()},
            unboxing_function=lambda value: value)

        # Return an object of this model
        return cls(payment_type,
                   mtype,
                   data,
                   email,
                   usage_limit,
                   ip_address,
                   metadata,
                   additional_properties)

    @classmethod
    def validate(cls, dictionary):
        """Validate dictionary against class required properties

        Args:
            dictionary (dictionary): A dictionary representation of the object
            as obtained from the deserialization of the server's response. The
            keys MUST match property names in the API description.

        Returns:
            boolean : if dictionary is valid contains required properties.

        """
        from univapayclientsdk.utilities.union_type_lookup import (
            UnionTypeLookUp,
        )

        if isinstance(dictionary, cls):
            return APIHelper.is_valid_type(
                    value=dictionary.payment_type,
                    type_callable=lambda value:
                        TransactionTokenCreateRequestPaymentType.validate(value)) \
                and APIHelper.is_valid_type(
                    value=dictionary.mtype,
                    type_callable=lambda value:
                        TransactionTokenCreateRequestType.validate(value)) \
                and (UnionTypeLookUp.get("TransactionTokenCreateRequestData")
                .validate(dictionary.data).is_valid)

        if not isinstance(dictionary, dict):
            return False

        return APIHelper.is_valid_type(
                value=dictionary.get("payment_type"),
                type_callable=lambda value:
                    TransactionTokenCreateRequestPaymentType.validate(value)) \
            and APIHelper.is_valid_type(
                value=dictionary.get("type"),
                type_callable=lambda value:
                    TransactionTokenCreateRequestType.validate(value)) \
            and (UnionTypeLookUp.get("TransactionTokenCreateRequestData")
            .validate(dictionary.get("data")).is_valid)

    def __repr__(self):
        """Return a unambiguous string representation."""
        _payment_type=self.payment_type
        _mtype=self.mtype
        _email=(
            self.email
            if hasattr(self, "email")
            else None
        )
        _usage_limit=(
            self.usage_limit
            if hasattr(self, "usage_limit")
            else None
        )
        _ip_address=(
            self.ip_address
            if hasattr(self, "ip_address")
            else None
        )
        _metadata=(
            self.metadata
            if hasattr(self, "metadata")
            else None
        )
        _data=self.data
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"payment_type={_payment_type!r}, "
            f"mtype={_mtype!r}, "
            f"email={_email!r}, "
            f"usage_limit={_usage_limit!r}, "
            f"ip_address={_ip_address!r}, "
            f"metadata={_metadata!r}, "
            f"data={_data!r}, "
            f"additional_properties={_additional_properties!r}, "
            f")"
        )

    def __str__(self):
        """Return a human-readable string representation."""
        _payment_type=self.payment_type
        _mtype=self.mtype
        _email=(
            self.email
            if hasattr(self, "email")
            else None
        )
        _usage_limit=(
            self.usage_limit
            if hasattr(self, "usage_limit")
            else None
        )
        _ip_address=(
            self.ip_address
            if hasattr(self, "ip_address")
            else None
        )
        _metadata=(
            self.metadata
            if hasattr(self, "metadata")
            else None
        )
        _data=self.data
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"payment_type={_payment_type!s}, "
            f"mtype={_mtype!s}, "
            f"email={_email!s}, "
            f"usage_limit={_usage_limit!s}, "
            f"ip_address={_ip_address!s}, "
            f"metadata={_metadata!s}, "
            f"data={_data!s}, "
            f"additional_properties={_additional_properties!s}, "
            f")"
        )
