"""univapay_client_sdk.

This file was automatically generated for Univapay by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

# ruff: noqa: E501
from univapayclientsdk.api_helper import APIHelper
from univapayclientsdk.models.charge_redirect import (
    ChargeRedirect,
)
from univapayclientsdk.models.charge_three_ds import (
    ChargeThreeDs,
)
from univapayclientsdk.models.generic_metadata import (
    GenericMetadata,
)
from univapayclientsdk.models.payment_error import (
    PaymentError,
)


class Charge(object):
    """Implementation of the 'Charge' model.

    Charge resource returned by the payments API.

    Attributes:
        id (uuid|str): Unique identifier.
        store_id (uuid|str): Store identifier.
        transaction_token_id (uuid|str): Transaction token identifier.
        transaction_token_type (ChargeTransactionTokenType): Charge Transaction Token
            Type schema.
        subscription_id (uuid|str): Subscription identifier.
        merchant_transaction_id (str): Merchant-defined transaction identifier.
        requested_amount (int): Requested amount in the smallest currency unit.
        requested_currency (str): Requested ISO-4217 currency code.
        requested_amount_formatted (float): Requested amount formatted for display.
        charged_amount (int): Charged amount in the smallest currency unit.
        charged_currency (str): Charged ISO-4217 currency code.
        charged_amount_formatted (float): Charged amount formatted for display.
        fee_amount (int): Fee amount in the smallest currency unit.
        fee_currency (str): Fee ISO-4217 currency code.
        fee_amount_formatted (float): Fee amount formatted for display.
        only_direct_currency (bool): Whether only direct currency processing is
            allowed.
        capture_at (datetime): Timestamp when capture should occur.
        descriptor (str): Billing descriptor.
        descriptor_phone_number (str): Billing descriptor phone number.
        status (ChargeStatus): Charge Status schema.
        error (PaymentError): Payment error details, or null if successful.
        metadata (GenericMetadata): A free-form dictionary for custom metadata.
        mode (ChargeMode): Charge Mode schema.
        created_on (datetime): Timestamp when the resource was created.
        merchant_name (str): Merchant display name.
        store_name (str): Store display name.
        redirect (ChargeRedirect): Charge Redirect schema.
        three_ds (ChargeThreeDs): Charge Three Ds schema.
        additional_properties (Dict[str, Any]): The additional properties for the
            model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "id": "id",
        "store_id": "store_id",
        "transaction_token_id": "transaction_token_id",
        "transaction_token_type": "transaction_token_type",
        "subscription_id": "subscription_id",
        "merchant_transaction_id": "merchant_transaction_id",
        "requested_amount": "requested_amount",
        "requested_currency": "requested_currency",
        "requested_amount_formatted": "requested_amount_formatted",
        "charged_amount": "charged_amount",
        "charged_currency": "charged_currency",
        "charged_amount_formatted": "charged_amount_formatted",
        "fee_amount": "fee_amount",
        "fee_currency": "fee_currency",
        "fee_amount_formatted": "fee_amount_formatted",
        "only_direct_currency": "only_direct_currency",
        "capture_at": "capture_at",
        "descriptor": "descriptor",
        "descriptor_phone_number": "descriptor_phone_number",
        "status": "status",
        "error": "error",
        "metadata": "metadata",
        "mode": "mode",
        "created_on": "created_on",
        "merchant_name": "merchant_name",
        "store_name": "store_name",
        "redirect": "redirect",
        "three_ds": "three_ds",
    }

    _optionals = [
        "id",
        "store_id",
        "transaction_token_id",
        "transaction_token_type",
        "subscription_id",
        "merchant_transaction_id",
        "requested_amount",
        "requested_currency",
        "requested_amount_formatted",
        "charged_amount",
        "charged_currency",
        "charged_amount_formatted",
        "fee_amount",
        "fee_currency",
        "fee_amount_formatted",
        "only_direct_currency",
        "capture_at",
        "descriptor",
        "descriptor_phone_number",
        "status",
        "error",
        "metadata",
        "mode",
        "created_on",
        "merchant_name",
        "store_name",
        "redirect",
        "three_ds",
    ]

    _nullables = [
        "subscription_id",
        "merchant_transaction_id",
        "charged_amount",
        "charged_currency",
        "charged_amount_formatted",
        "fee_amount",
        "fee_currency",
        "fee_amount_formatted",
        "capture_at",
        "descriptor",
        "descriptor_phone_number",
        "error",
    ]

    def __init__(
        self,
        id=APIHelper.SKIP,
        store_id=APIHelper.SKIP,
        transaction_token_id=APIHelper.SKIP,
        transaction_token_type=APIHelper.SKIP,
        subscription_id=APIHelper.SKIP,
        merchant_transaction_id=APIHelper.SKIP,
        requested_amount=APIHelper.SKIP,
        requested_currency=APIHelper.SKIP,
        requested_amount_formatted=APIHelper.SKIP,
        charged_amount=APIHelper.SKIP,
        charged_currency=APIHelper.SKIP,
        charged_amount_formatted=APIHelper.SKIP,
        fee_amount=APIHelper.SKIP,
        fee_currency=APIHelper.SKIP,
        fee_amount_formatted=APIHelper.SKIP,
        only_direct_currency=APIHelper.SKIP,
        capture_at=APIHelper.SKIP,
        descriptor=APIHelper.SKIP,
        descriptor_phone_number=APIHelper.SKIP,
        status=APIHelper.SKIP,
        error=APIHelper.SKIP,
        metadata=APIHelper.SKIP,
        mode=APIHelper.SKIP,
        created_on=APIHelper.SKIP,
        merchant_name=APIHelper.SKIP,
        store_name=APIHelper.SKIP,
        redirect=APIHelper.SKIP,
        three_ds=APIHelper.SKIP,
        additional_properties=None):
        """Initialize a Charge instance."""
        # Initialize members of the class
        if id is not APIHelper.SKIP:
            self.id = id
        if store_id is not APIHelper.SKIP:
            self.store_id = store_id
        if transaction_token_id is not APIHelper.SKIP:
            self.transaction_token_id = transaction_token_id
        if transaction_token_type is not APIHelper.SKIP:
            self.transaction_token_type = transaction_token_type
        if subscription_id is not APIHelper.SKIP:
            self.subscription_id = subscription_id
        if merchant_transaction_id is not APIHelper.SKIP:
            self.merchant_transaction_id = merchant_transaction_id
        if requested_amount is not APIHelper.SKIP:
            self.requested_amount = requested_amount
        if requested_currency is not APIHelper.SKIP:
            self.requested_currency = requested_currency
        if requested_amount_formatted is not APIHelper.SKIP:
            self.requested_amount_formatted = requested_amount_formatted
        if charged_amount is not APIHelper.SKIP:
            self.charged_amount = charged_amount
        if charged_currency is not APIHelper.SKIP:
            self.charged_currency = charged_currency
        if charged_amount_formatted is not APIHelper.SKIP:
            self.charged_amount_formatted = charged_amount_formatted
        if fee_amount is not APIHelper.SKIP:
            self.fee_amount = fee_amount
        if fee_currency is not APIHelper.SKIP:
            self.fee_currency = fee_currency
        if fee_amount_formatted is not APIHelper.SKIP:
            self.fee_amount_formatted = fee_amount_formatted
        if only_direct_currency is not APIHelper.SKIP:
            self.only_direct_currency = only_direct_currency
        if capture_at is not APIHelper.SKIP:
            self.capture_at =\
                 APIHelper.apply_datetime_converter(
                capture_at, APIHelper.RFC3339DateTime)\
                 if capture_at else None
        if descriptor is not APIHelper.SKIP:
            self.descriptor = descriptor
        if descriptor_phone_number is not APIHelper.SKIP:
            self.descriptor_phone_number = descriptor_phone_number
        if status is not APIHelper.SKIP:
            self.status = status
        if error is not APIHelper.SKIP:
            self.error = error
        if metadata is not APIHelper.SKIP:
            self.metadata = metadata
        if mode is not APIHelper.SKIP:
            self.mode = mode
        if created_on is not APIHelper.SKIP:
            self.created_on =\
                 APIHelper.apply_datetime_converter(
                created_on, APIHelper.RFC3339DateTime)\
                 if created_on else None
        if merchant_name is not APIHelper.SKIP:
            self.merchant_name = merchant_name
        if store_name is not APIHelper.SKIP:
            self.store_name = store_name
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
        id =\
            dictionary.get("id")\
            if dictionary.get("id")\
                else APIHelper.SKIP
        store_id =\
            dictionary.get("store_id")\
            if dictionary.get("store_id")\
                else APIHelper.SKIP
        transaction_token_id =\
            dictionary.get("transaction_token_id")\
            if dictionary.get("transaction_token_id")\
                else APIHelper.SKIP
        transaction_token_type =\
            dictionary.get("transaction_token_type")\
            if dictionary.get("transaction_token_type")\
                else APIHelper.SKIP
        subscription_id =\
            dictionary.get("subscription_id")\
            if "subscription_id" in dictionary.keys()\
                else APIHelper.SKIP
        merchant_transaction_id =\
            dictionary.get("merchant_transaction_id")\
            if "merchant_transaction_id" in dictionary.keys()\
                else APIHelper.SKIP
        requested_amount =\
            dictionary.get("requested_amount")\
            if dictionary.get("requested_amount")\
                else APIHelper.SKIP
        requested_currency =\
            dictionary.get("requested_currency")\
            if dictionary.get("requested_currency")\
                else APIHelper.SKIP
        requested_amount_formatted =\
            dictionary.get("requested_amount_formatted")\
            if dictionary.get("requested_amount_formatted")\
                else APIHelper.SKIP
        charged_amount =\
            dictionary.get("charged_amount")\
            if "charged_amount" in dictionary.keys()\
                else APIHelper.SKIP
        charged_currency =\
            dictionary.get("charged_currency")\
            if "charged_currency" in dictionary.keys()\
                else APIHelper.SKIP
        charged_amount_formatted =\
            dictionary.get("charged_amount_formatted")\
            if "charged_amount_formatted" in dictionary.keys()\
                else APIHelper.SKIP
        fee_amount =\
            dictionary.get("fee_amount")\
            if "fee_amount" in dictionary.keys()\
                else APIHelper.SKIP
        fee_currency =\
            dictionary.get("fee_currency")\
            if "fee_currency" in dictionary.keys()\
                else APIHelper.SKIP
        fee_amount_formatted =\
            dictionary.get("fee_amount_formatted")\
            if "fee_amount_formatted" in dictionary.keys()\
                else APIHelper.SKIP
        only_direct_currency =\
            dictionary.get("only_direct_currency")\
            if "only_direct_currency" in dictionary.keys()\
                else APIHelper.SKIP
        if "capture_at" in dictionary.keys():
            capture_at = APIHelper.RFC3339DateTime.from_value(
                dictionary.get("capture_at")).datetime\
                if dictionary.get("capture_at") else None

        else:
            capture_at = APIHelper.SKIP
        descriptor =\
            dictionary.get("descriptor")\
            if "descriptor" in dictionary.keys()\
                else APIHelper.SKIP
        descriptor_phone_number =\
            dictionary.get("descriptor_phone_number")\
            if "descriptor_phone_number" in dictionary.keys()\
                else APIHelper.SKIP
        status =\
            dictionary.get("status")\
            if dictionary.get("status")\
                else APIHelper.SKIP
        if "error" in dictionary.keys():
            error =\
                PaymentError.from_dictionary(
                dictionary.get("error"))\
                if dictionary.get("error") else None
        else:
            error = APIHelper.SKIP
        metadata =\
            GenericMetadata.from_dictionary(
                dictionary.get("metadata"))\
                if "metadata" in dictionary.keys()\
                else APIHelper.SKIP
        mode =\
            dictionary.get("mode")\
            if dictionary.get("mode")\
                else APIHelper.SKIP
        created_on = APIHelper.RFC3339DateTime.from_value(
            dictionary.get("created_on")).datetime\
            if dictionary.get("created_on") else APIHelper.SKIP
        merchant_name =\
            dictionary.get("merchant_name")\
            if dictionary.get("merchant_name")\
                else APIHelper.SKIP
        store_name =\
            dictionary.get("store_name")\
            if dictionary.get("store_name")\
                else APIHelper.SKIP
        redirect =\
            ChargeRedirect.from_dictionary(
                dictionary.get("redirect"))\
                if "redirect" in dictionary.keys()\
                else APIHelper.SKIP
        three_ds =\
            ChargeThreeDs.from_dictionary(
                dictionary.get("three_ds"))\
                if "three_ds" in dictionary.keys()\
                else APIHelper.SKIP

        additional_properties = APIHelper.get_additional_properties(
            dictionary={k: v for k, v in dictionary.items()
                        if k not in cls._names.values()},
            unboxing_function=lambda value: value)

        # Return an object of this model
        return cls(id,
                   store_id,
                   transaction_token_id,
                   transaction_token_type,
                   subscription_id,
                   merchant_transaction_id,
                   requested_amount,
                   requested_currency,
                   requested_amount_formatted,
                   charged_amount,
                   charged_currency,
                   charged_amount_formatted,
                   fee_amount,
                   fee_currency,
                   fee_amount_formatted,
                   only_direct_currency,
                   capture_at,
                   descriptor,
                   descriptor_phone_number,
                   status,
                   error,
                   metadata,
                   mode,
                   created_on,
                   merchant_name,
                   store_name,
                   redirect,
                   three_ds,
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
        if isinstance(dictionary, cls):
            return True

        if not isinstance(dictionary, dict):
            return False

        return True

    def __repr__(self):
        """Return a unambiguous string representation."""
        _id=(
            self.id
            if hasattr(self, "id")
            else None
        )
        _store_id=(
            self.store_id
            if hasattr(self, "store_id")
            else None
        )
        _transaction_token_id=(
            self.transaction_token_id
            if hasattr(self, "transaction_token_id")
            else None
        )
        _transaction_token_type=(
            self.transaction_token_type
            if hasattr(self, "transaction_token_type")
            else None
        )
        _subscription_id=(
            self.subscription_id
            if hasattr(self, "subscription_id")
            else None
        )
        _merchant_transaction_id=(
            self.merchant_transaction_id
            if hasattr(self, "merchant_transaction_id")
            else None
        )
        _requested_amount=(
            self.requested_amount
            if hasattr(self, "requested_amount")
            else None
        )
        _requested_currency=(
            self.requested_currency
            if hasattr(self, "requested_currency")
            else None
        )
        _requested_amount_formatted=(
            self.requested_amount_formatted
            if hasattr(self, "requested_amount_formatted")
            else None
        )
        _charged_amount=(
            self.charged_amount
            if hasattr(self, "charged_amount")
            else None
        )
        _charged_currency=(
            self.charged_currency
            if hasattr(self, "charged_currency")
            else None
        )
        _charged_amount_formatted=(
            self.charged_amount_formatted
            if hasattr(self, "charged_amount_formatted")
            else None
        )
        _fee_amount=(
            self.fee_amount
            if hasattr(self, "fee_amount")
            else None
        )
        _fee_currency=(
            self.fee_currency
            if hasattr(self, "fee_currency")
            else None
        )
        _fee_amount_formatted=(
            self.fee_amount_formatted
            if hasattr(self, "fee_amount_formatted")
            else None
        )
        _only_direct_currency=(
            self.only_direct_currency
            if hasattr(self, "only_direct_currency")
            else None
        )
        _capture_at=(
            self.capture_at
            if hasattr(self, "capture_at")
            else None
        )
        _descriptor=(
            self.descriptor
            if hasattr(self, "descriptor")
            else None
        )
        _descriptor_phone_number=(
            self.descriptor_phone_number
            if hasattr(self, "descriptor_phone_number")
            else None
        )
        _status=(
            self.status
            if hasattr(self, "status")
            else None
        )
        _error=(
            self.error
            if hasattr(self, "error")
            else None
        )
        _metadata=(
            self.metadata
            if hasattr(self, "metadata")
            else None
        )
        _mode=(
            self.mode
            if hasattr(self, "mode")
            else None
        )
        _created_on=(
            self.created_on
            if hasattr(self, "created_on")
            else None
        )
        _merchant_name=(
            self.merchant_name
            if hasattr(self, "merchant_name")
            else None
        )
        _store_name=(
            self.store_name
            if hasattr(self, "store_name")
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
            f"id={_id!r}, "
            f"store_id={_store_id!r}, "
            f"transaction_token_id={_transaction_token_id!r}, "
            f"transaction_token_type={_transaction_token_type!r}, "
            f"subscription_id={_subscription_id!r}, "
            f"merchant_transaction_id={_merchant_transaction_id!r}, "
            f"requested_amount={_requested_amount!r}, "
            f"requested_currency={_requested_currency!r}, "
            f"requested_amount_formatted={_requested_amount_formatted!r}, "
            f"charged_amount={_charged_amount!r}, "
            f"charged_currency={_charged_currency!r}, "
            f"charged_amount_formatted={_charged_amount_formatted!r}, "
            f"fee_amount={_fee_amount!r}, "
            f"fee_currency={_fee_currency!r}, "
            f"fee_amount_formatted={_fee_amount_formatted!r}, "
            f"only_direct_currency={_only_direct_currency!r}, "
            f"capture_at={_capture_at!r}, "
            f"descriptor={_descriptor!r}, "
            f"descriptor_phone_number={_descriptor_phone_number!r}, "
            f"status={_status!r}, "
            f"error={_error!r}, "
            f"metadata={_metadata!r}, "
            f"mode={_mode!r}, "
            f"created_on={_created_on!r}, "
            f"merchant_name={_merchant_name!r}, "
            f"store_name={_store_name!r}, "
            f"redirect={_redirect!r}, "
            f"three_ds={_three_ds!r}, "
            f"additional_properties={_additional_properties!r}, "
            f")"
        )

    def __str__(self):
        """Return a human-readable string representation."""
        _id=(
            self.id
            if hasattr(self, "id")
            else None
        )
        _store_id=(
            self.store_id
            if hasattr(self, "store_id")
            else None
        )
        _transaction_token_id=(
            self.transaction_token_id
            if hasattr(self, "transaction_token_id")
            else None
        )
        _transaction_token_type=(
            self.transaction_token_type
            if hasattr(self, "transaction_token_type")
            else None
        )
        _subscription_id=(
            self.subscription_id
            if hasattr(self, "subscription_id")
            else None
        )
        _merchant_transaction_id=(
            self.merchant_transaction_id
            if hasattr(self, "merchant_transaction_id")
            else None
        )
        _requested_amount=(
            self.requested_amount
            if hasattr(self, "requested_amount")
            else None
        )
        _requested_currency=(
            self.requested_currency
            if hasattr(self, "requested_currency")
            else None
        )
        _requested_amount_formatted=(
            self.requested_amount_formatted
            if hasattr(self, "requested_amount_formatted")
            else None
        )
        _charged_amount=(
            self.charged_amount
            if hasattr(self, "charged_amount")
            else None
        )
        _charged_currency=(
            self.charged_currency
            if hasattr(self, "charged_currency")
            else None
        )
        _charged_amount_formatted=(
            self.charged_amount_formatted
            if hasattr(self, "charged_amount_formatted")
            else None
        )
        _fee_amount=(
            self.fee_amount
            if hasattr(self, "fee_amount")
            else None
        )
        _fee_currency=(
            self.fee_currency
            if hasattr(self, "fee_currency")
            else None
        )
        _fee_amount_formatted=(
            self.fee_amount_formatted
            if hasattr(self, "fee_amount_formatted")
            else None
        )
        _only_direct_currency=(
            self.only_direct_currency
            if hasattr(self, "only_direct_currency")
            else None
        )
        _capture_at=(
            self.capture_at
            if hasattr(self, "capture_at")
            else None
        )
        _descriptor=(
            self.descriptor
            if hasattr(self, "descriptor")
            else None
        )
        _descriptor_phone_number=(
            self.descriptor_phone_number
            if hasattr(self, "descriptor_phone_number")
            else None
        )
        _status=(
            self.status
            if hasattr(self, "status")
            else None
        )
        _error=(
            self.error
            if hasattr(self, "error")
            else None
        )
        _metadata=(
            self.metadata
            if hasattr(self, "metadata")
            else None
        )
        _mode=(
            self.mode
            if hasattr(self, "mode")
            else None
        )
        _created_on=(
            self.created_on
            if hasattr(self, "created_on")
            else None
        )
        _merchant_name=(
            self.merchant_name
            if hasattr(self, "merchant_name")
            else None
        )
        _store_name=(
            self.store_name
            if hasattr(self, "store_name")
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
            f"id={_id!s}, "
            f"store_id={_store_id!s}, "
            f"transaction_token_id={_transaction_token_id!s}, "
            f"transaction_token_type={_transaction_token_type!s}, "
            f"subscription_id={_subscription_id!s}, "
            f"merchant_transaction_id={_merchant_transaction_id!s}, "
            f"requested_amount={_requested_amount!s}, "
            f"requested_currency={_requested_currency!s}, "
            f"requested_amount_formatted={_requested_amount_formatted!s}, "
            f"charged_amount={_charged_amount!s}, "
            f"charged_currency={_charged_currency!s}, "
            f"charged_amount_formatted={_charged_amount_formatted!s}, "
            f"fee_amount={_fee_amount!s}, "
            f"fee_currency={_fee_currency!s}, "
            f"fee_amount_formatted={_fee_amount_formatted!s}, "
            f"only_direct_currency={_only_direct_currency!s}, "
            f"capture_at={_capture_at!s}, "
            f"descriptor={_descriptor!s}, "
            f"descriptor_phone_number={_descriptor_phone_number!s}, "
            f"status={_status!s}, "
            f"error={_error!s}, "
            f"metadata={_metadata!s}, "
            f"mode={_mode!s}, "
            f"created_on={_created_on!s}, "
            f"merchant_name={_merchant_name!s}, "
            f"store_name={_store_name!s}, "
            f"redirect={_redirect!s}, "
            f"three_ds={_three_ds!s}, "
            f"additional_properties={_additional_properties!s}, "
            f")"
        )
