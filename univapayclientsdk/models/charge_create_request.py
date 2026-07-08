"""univapay_client_sdk.

This file was automatically generated for Univapay by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

# ruff: noqa: E501
from univapayclientsdk.api_helper import APIHelper
from univapayclientsdk.models.charge_create_request_client_metadata import (
    ChargeCreateRequestClientMetadata,
)
from univapayclientsdk.models.charge_create_request_redirect import (
    ChargeCreateRequestRedirect,
)
from univapayclientsdk.models.charge_create_request_three_ds import (
    ChargeCreateRequestThreeDs,
)
from univapayclientsdk.models.generic_metadata import (
    GenericMetadata,
)


class ChargeCreateRequest(object):
    """Implementation of the 'ChargeCreateRequest' model.

    Request payload for creating a charge.

    Attributes:
        transaction_token_id (uuid|str): Transaction token identifier.
        amount (int): The charge amount.
        currency (str): ISO-4217 currency code.
        capture (bool): If false, creates an Authorization only (Hold).
        capture_at (datetime): Auto-capture date for cards, or payment deadline for
            Konbini/Bank. Note: Time specification is ignored for 7-Eleven,
            Seicomart, and PayEasy.
        merchant_transaction_id (str): Unique transaction ID for the merchant.
            Required/used by specific brands like we_chat, we_chat_mpm, and
            we_chat_online.
        metadata (GenericMetadata): A free-form dictionary for custom metadata.
        client_metadata (ChargeCreateRequestClientMetadata): Charge Create Request
            Client Metadata schema.
        redirect (ChargeCreateRequestRedirect): Charge Create Request Redirect schema.
        three_ds (ChargeCreateRequestThreeDs): Charge Create Request Three Ds schema.
        additional_properties (Dict[str, Any]): The additional properties for the
            model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "transaction_token_id": "transaction_token_id",
        "amount": "amount",
        "currency": "currency",
        "capture": "capture",
        "capture_at": "capture_at",
        "merchant_transaction_id": "merchant_transaction_id",
        "metadata": "metadata",
        "client_metadata": "client_metadata",
        "redirect": "redirect",
        "three_ds": "three_ds",
    }

    _optionals = [
        "capture",
        "capture_at",
        "merchant_transaction_id",
        "metadata",
        "client_metadata",
        "redirect",
        "three_ds",
    ]

    def __init__(
        self,
        transaction_token_id=None,
        amount=None,
        currency="JPY",
        capture=True,
        capture_at=APIHelper.SKIP,
        merchant_transaction_id=APIHelper.SKIP,
        metadata=APIHelper.SKIP,
        client_metadata=APIHelper.SKIP,
        redirect=APIHelper.SKIP,
        three_ds=APIHelper.SKIP,
        additional_properties=None):
        """Initialize a ChargeCreateRequest instance."""
        # Initialize members of the class
        self.transaction_token_id = transaction_token_id
        self.amount = amount
        self.currency = currency
        self.capture = capture
        if capture_at is not APIHelper.SKIP:
            self.capture_at =\
                 APIHelper.apply_datetime_converter(
                capture_at, APIHelper.RFC3339DateTime)\
                 if capture_at else None
        if merchant_transaction_id is not APIHelper.SKIP:
            self.merchant_transaction_id = merchant_transaction_id
        if metadata is not APIHelper.SKIP:
            self.metadata = metadata
        if client_metadata is not APIHelper.SKIP:
            self.client_metadata = client_metadata
        if redirect is not APIHelper.SKIP:
            self.redirect = redirect
        if three_ds is not APIHelper.SKIP:
            self.three_ds = three_ds

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
        transaction_token_id =\
            dictionary.get("transaction_token_id")\
            if dictionary.get("transaction_token_id")\
                else None
        amount =\
            dictionary.get("amount")\
            if dictionary.get("amount")\
                else None
        currency =\
            dictionary.get("currency")\
            if dictionary.get("currency")\
                else "JPY"
        capture =\
            dictionary.get("capture")\
            if dictionary.get("capture")\
                else True
        capture_at = APIHelper.RFC3339DateTime.from_value(
            dictionary.get("capture_at")).datetime\
            if dictionary.get("capture_at") else APIHelper.SKIP
        merchant_transaction_id =\
            dictionary.get("merchant_transaction_id")\
            if dictionary.get("merchant_transaction_id")\
                else APIHelper.SKIP
        metadata =\
            GenericMetadata.from_dictionary(
                dictionary.get("metadata"))\
                if "metadata" in dictionary.keys()\
                else APIHelper.SKIP
        client_metadata =\
            ChargeCreateRequestClientMetadata.from_dictionary(
                dictionary.get("client_metadata"))\
                if "client_metadata" in dictionary.keys()\
                else APIHelper.SKIP
        redirect =\
            ChargeCreateRequestRedirect.from_dictionary(
                dictionary.get("redirect"))\
                if "redirect" in dictionary.keys()\
                else APIHelper.SKIP
        three_ds =\
            ChargeCreateRequestThreeDs.from_dictionary(
                dictionary.get("three_ds"))\
                if "three_ds" in dictionary.keys()\
                else APIHelper.SKIP

        additional_properties = APIHelper.get_additional_properties(
            dictionary={k: v for k, v in dictionary.items()
                        if k not in cls._names.values()},
            unboxing_function=lambda value: value)

        # Return an object of this model
        return cls(transaction_token_id,
                   amount,
                   currency,
                   capture,
                   capture_at,
                   merchant_transaction_id,
                   metadata,
                   client_metadata,
                   redirect,
                   three_ds,
                   additional_properties)

    def __repr__(self):
        """Return a unambiguous string representation."""
        _transaction_token_id=self.transaction_token_id
        _amount=self.amount
        _currency=self.currency
        _capture=(
            self.capture
            if hasattr(self, "capture")
            else None
        )
        _capture_at=(
            self.capture_at
            if hasattr(self, "capture_at")
            else None
        )
        _merchant_transaction_id=(
            self.merchant_transaction_id
            if hasattr(self, "merchant_transaction_id")
            else None
        )
        _metadata=(
            self.metadata
            if hasattr(self, "metadata")
            else None
        )
        _client_metadata=(
            self.client_metadata
            if hasattr(self, "client_metadata")
            else None
        )
        _redirect=(
            self.redirect
            if hasattr(self, "redirect")
            else None
        )
        _three_ds=(
            self.three_ds
            if hasattr(self, "three_ds")
            else None
        )
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"transaction_token_id={_transaction_token_id!r}, "
            f"amount={_amount!r}, "
            f"currency={_currency!r}, "
            f"capture={_capture!r}, "
            f"capture_at={_capture_at!r}, "
            f"merchant_transaction_id={_merchant_transaction_id!r}, "
            f"metadata={_metadata!r}, "
            f"client_metadata={_client_metadata!r}, "
            f"redirect={_redirect!r}, "
            f"three_ds={_three_ds!r}, "
            f"additional_properties={_additional_properties!r}, "
            f")"
        )

    def __str__(self):
        """Return a human-readable string representation."""
        _transaction_token_id=self.transaction_token_id
        _amount=self.amount
        _currency=self.currency
        _capture=(
            self.capture
            if hasattr(self, "capture")
            else None
        )
        _capture_at=(
            self.capture_at
            if hasattr(self, "capture_at")
            else None
        )
        _merchant_transaction_id=(
            self.merchant_transaction_id
            if hasattr(self, "merchant_transaction_id")
            else None
        )
        _metadata=(
            self.metadata
            if hasattr(self, "metadata")
            else None
        )
        _client_metadata=(
            self.client_metadata
            if hasattr(self, "client_metadata")
            else None
        )
        _redirect=(
            self.redirect
            if hasattr(self, "redirect")
            else None
        )
        _three_ds=(
            self.three_ds
            if hasattr(self, "three_ds")
            else None
        )
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"transaction_token_id={_transaction_token_id!s}, "
            f"amount={_amount!s}, "
            f"currency={_currency!s}, "
            f"capture={_capture!s}, "
            f"capture_at={_capture_at!s}, "
            f"merchant_transaction_id={_merchant_transaction_id!s}, "
            f"metadata={_metadata!s}, "
            f"client_metadata={_client_metadata!s}, "
            f"redirect={_redirect!s}, "
            f"three_ds={_three_ds!s}, "
            f"additional_properties={_additional_properties!s}, "
            f")"
        )
