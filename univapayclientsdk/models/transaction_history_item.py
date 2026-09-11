"""univapay_client_sdk.

This file was automatically generated for Univapay by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

# ruff: noqa: E501
from univapayclientsdk.api_helper import APIHelper
from univapayclientsdk.models.generic_metadata import (
    GenericMetadata,
)
from univapayclientsdk.models.transaction_history_user_data import (
    TransactionHistoryUserData,
)


class TransactionHistoryItem(object):
    """Implementation of the 'TransactionHistoryItem' model.

    A single charge or refund row in the merchant's transaction history.

    Attributes:
        store_id (uuid|str): Store identifier.
        resource_id (uuid|str): ID of the underlying resource — a charge ID for
            charge rows, a refund ID for refund rows.
        charge_id (uuid|str): ID of the originating charge. `null` for charge rows;
            set for refund rows.
        amount (int): Amount, in the currency's minor unit.
        currency (str): ISO-4217 currency code.
        amount_formatted (float): Amount, formatted per the currency's display scale.
        mtype (TransactionHistoryType): Whether this row represents a charge or a
            refund.
        status (TransactionHistoryStatus): Status of the underlying resource. Charge
            rows use the full set of values; refund rows only ever report `pending`,
            `successful`, `failed`, or `error`.
        metadata (GenericMetadata): A free-form dictionary for custom metadata.
        created_on (datetime): Timestamp when the underlying resource was created.
        mode (TransactionHistoryMode): Environment mode: `live` and `test` reflect
            the credential used to authenticate, while `live_test` is reserved for
            privileged callers testing against live-mode data.
        merchant_name (str): Merchant display name.
        store_name (str): Store display name.
        payment_type (TransactionHistoryPaymentType): The payment method used for the
            underlying charge.
        user_data (TransactionHistoryUserData): Payment-type-specific details for
            this row. This is a single flat object covering every payment type — the
            fields actually populated depend on `payment_type` (documented per field
            below). Fields not applicable to a given payment type are omitted.
        bank_transfer_payment_status (BankTransferPaymentStatus): Bank transfer
            payment status, or `null` when not applicable.
        bank_transfer_latest_deposit_date (datetime): Timestamp of the most recent
            deposit matched against a bank transfer charge. `null` when not
            applicable.
        mcp_token_id (uuid|str): ID of the multi-currency-pricing token used, when
            applicable. `null` when not applicable.
        charge_type (TransactionHistoryChargeType): Charge type, or `null` when not
            applicable.
        additional_properties (Dict[str, Any]): The additional properties for the
            model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "store_id": "store_id",
        "resource_id": "resource_id",
        "charge_id": "charge_id",
        "amount": "amount",
        "currency": "currency",
        "amount_formatted": "amount_formatted",
        "mtype": "type",
        "status": "status",
        "metadata": "metadata",
        "created_on": "created_on",
        "mode": "mode",
        "merchant_name": "merchant_name",
        "store_name": "store_name",
        "payment_type": "payment_type",
        "user_data": "user_data",
        "bank_transfer_payment_status": "bank_transfer_payment_status",
        "bank_transfer_latest_deposit_date": "bank_transfer_latest_deposit_date",
        "mcp_token_id": "mcp_token_id",
        "charge_type": "charge_type",
    }

    _optionals = [
        "store_id",
        "resource_id",
        "charge_id",
        "amount",
        "currency",
        "amount_formatted",
        "mtype",
        "status",
        "metadata",
        "created_on",
        "mode",
        "merchant_name",
        "store_name",
        "payment_type",
        "user_data",
        "bank_transfer_payment_status",
        "bank_transfer_latest_deposit_date",
        "mcp_token_id",
        "charge_type",
    ]

    _nullables = [
        "charge_id",
        "bank_transfer_payment_status",
        "bank_transfer_latest_deposit_date",
        "mcp_token_id",
        "charge_type",
    ]

    def __init__(
        self,
        store_id=APIHelper.SKIP,
        resource_id=APIHelper.SKIP,
        charge_id=APIHelper.SKIP,
        amount=APIHelper.SKIP,
        currency=APIHelper.SKIP,
        amount_formatted=APIHelper.SKIP,
        mtype=APIHelper.SKIP,
        status=APIHelper.SKIP,
        metadata=APIHelper.SKIP,
        created_on=APIHelper.SKIP,
        mode=APIHelper.SKIP,
        merchant_name=APIHelper.SKIP,
        store_name=APIHelper.SKIP,
        payment_type=APIHelper.SKIP,
        user_data=APIHelper.SKIP,
        bank_transfer_payment_status=APIHelper.SKIP,
        bank_transfer_latest_deposit_date=APIHelper.SKIP,
        mcp_token_id=APIHelper.SKIP,
        charge_type=APIHelper.SKIP,
        additional_properties=None):
        """Initialize a TransactionHistoryItem instance."""
        # Initialize members of the class
        if store_id is not APIHelper.SKIP:
            self.store_id = store_id
        if resource_id is not APIHelper.SKIP:
            self.resource_id = resource_id
        if charge_id is not APIHelper.SKIP:
            self.charge_id = charge_id
        if amount is not APIHelper.SKIP:
            self.amount = amount
        if currency is not APIHelper.SKIP:
            self.currency = currency
        if amount_formatted is not APIHelper.SKIP:
            self.amount_formatted = amount_formatted
        if mtype is not APIHelper.SKIP:
            self.mtype = mtype
        if status is not APIHelper.SKIP:
            self.status = status
        if metadata is not APIHelper.SKIP:
            self.metadata = metadata
        if created_on is not APIHelper.SKIP:
            self.created_on =\
                 APIHelper.apply_datetime_converter(
                created_on, APIHelper.RFC3339DateTime)\
                 if created_on else None
        if mode is not APIHelper.SKIP:
            self.mode = mode
        if merchant_name is not APIHelper.SKIP:
            self.merchant_name = merchant_name
        if store_name is not APIHelper.SKIP:
            self.store_name = store_name
        if payment_type is not APIHelper.SKIP:
            self.payment_type = payment_type
        if user_data is not APIHelper.SKIP:
            self.user_data = user_data
        if bank_transfer_payment_status is not APIHelper.SKIP:
            self.bank_transfer_payment_status = bank_transfer_payment_status
        if bank_transfer_latest_deposit_date is not APIHelper.SKIP:
            self.bank_transfer_latest_deposit_date =\
                 APIHelper.apply_datetime_converter(
                bank_transfer_latest_deposit_date, APIHelper.RFC3339DateTime)\
                 if bank_transfer_latest_deposit_date else None
        if mcp_token_id is not APIHelper.SKIP:
            self.mcp_token_id = mcp_token_id
        if charge_type is not APIHelper.SKIP:
            self.charge_type = charge_type

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
        store_id =\
            dictionary.get("store_id")\
            if dictionary.get("store_id")\
                else APIHelper.SKIP
        resource_id =\
            dictionary.get("resource_id")\
            if dictionary.get("resource_id")\
                else APIHelper.SKIP
        charge_id =\
            dictionary.get("charge_id")\
            if "charge_id" in dictionary.keys()\
                else APIHelper.SKIP
        amount =\
            dictionary.get("amount")\
            if dictionary.get("amount")\
                else APIHelper.SKIP
        currency =\
            dictionary.get("currency")\
            if dictionary.get("currency")\
                else APIHelper.SKIP
        amount_formatted =\
            dictionary.get("amount_formatted")\
            if dictionary.get("amount_formatted")\
                else APIHelper.SKIP
        mtype =\
            dictionary.get("type")\
            if dictionary.get("type")\
                else APIHelper.SKIP
        status =\
            dictionary.get("status")\
            if dictionary.get("status")\
                else APIHelper.SKIP
        metadata =\
            GenericMetadata.from_dictionary(
                dictionary.get("metadata"))\
                if "metadata" in dictionary.keys()\
                else APIHelper.SKIP
        created_on = APIHelper.RFC3339DateTime.from_value(
            dictionary.get("created_on")).datetime\
            if dictionary.get("created_on") else APIHelper.SKIP
        mode =\
            dictionary.get("mode")\
            if dictionary.get("mode")\
                else APIHelper.SKIP
        merchant_name =\
            dictionary.get("merchant_name")\
            if dictionary.get("merchant_name")\
                else APIHelper.SKIP
        store_name =\
            dictionary.get("store_name")\
            if dictionary.get("store_name")\
                else APIHelper.SKIP
        payment_type =\
            dictionary.get("payment_type")\
            if dictionary.get("payment_type")\
                else APIHelper.SKIP
        user_data =\
            TransactionHistoryUserData.from_dictionary(
                dictionary.get("user_data"))\
                if "user_data" in dictionary.keys()\
                else APIHelper.SKIP
        bank_transfer_payment_status =\
            dictionary.get("bank_transfer_payment_status")\
            if "bank_transfer_payment_status" in dictionary.keys()\
                else APIHelper.SKIP
        if "bank_transfer_latest_deposit_date" in dictionary.keys():
            bank_transfer_latest_deposit_date = APIHelper.RFC3339DateTime.from_value(
                dictionary.get("bank_transfer_latest_deposit_date")).datetime\
                if dictionary.get("bank_transfer_latest_deposit_date") else None

        else:
            bank_transfer_latest_deposit_date = APIHelper.SKIP
        mcp_token_id =\
            dictionary.get("mcp_token_id")\
            if "mcp_token_id" in dictionary.keys()\
                else APIHelper.SKIP
        charge_type =\
            dictionary.get("charge_type")\
            if "charge_type" in dictionary.keys()\
                else APIHelper.SKIP

        additional_properties = APIHelper.get_additional_properties(
            dictionary={k: v for k, v in dictionary.items()
                        if k not in cls._names.values()},
            unboxing_function=lambda value: value)

        # Return an object of this model
        return cls(store_id,
                   resource_id,
                   charge_id,
                   amount,
                   currency,
                   amount_formatted,
                   mtype,
                   status,
                   metadata,
                   created_on,
                   mode,
                   merchant_name,
                   store_name,
                   payment_type,
                   user_data,
                   bank_transfer_payment_status,
                   bank_transfer_latest_deposit_date,
                   mcp_token_id,
                   charge_type,
                   additional_properties)

    def __repr__(self):
        """Return a unambiguous string representation."""
        _store_id=(
            self.store_id
            if hasattr(self, "store_id")
            else None
        )
        _resource_id=(
            self.resource_id
            if hasattr(self, "resource_id")
            else None
        )
        _charge_id=(
            self.charge_id
            if hasattr(self, "charge_id")
            else None
        )
        _amount=(
            self.amount
            if hasattr(self, "amount")
            else None
        )
        _currency=(
            self.currency
            if hasattr(self, "currency")
            else None
        )
        _amount_formatted=(
            self.amount_formatted
            if hasattr(self, "amount_formatted")
            else None
        )
        _mtype=(
            self.mtype
            if hasattr(self, "mtype")
            else None
        )
        _status=(
            self.status
            if hasattr(self, "status")
            else None
        )
        _metadata=(
            self.metadata
            if hasattr(self, "metadata")
            else None
        )
        _created_on=(
            self.created_on
            if hasattr(self, "created_on")
            else None
        )
        _mode=(
            self.mode
            if hasattr(self, "mode")
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
        _payment_type=(
            self.payment_type
            if hasattr(self, "payment_type")
            else None
        )
        _user_data=(
            self.user_data
            if hasattr(self, "user_data")
            else None
        )
        _bank_transfer_payment_status=(
            self.bank_transfer_payment_status
            if hasattr(self, "bank_transfer_payment_status")
            else None
        )
        _bank_transfer_latest_deposit_date=(
            self.bank_transfer_latest_deposit_date
            if hasattr(self, "bank_transfer_latest_deposit_date")
            else None
        )
        _mcp_token_id=(
            self.mcp_token_id
            if hasattr(self, "mcp_token_id")
            else None
        )
        _charge_type=(
            self.charge_type
            if hasattr(self, "charge_type")
            else None
        )
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"store_id={_store_id!r}, "
            f"resource_id={_resource_id!r}, "
            f"charge_id={_charge_id!r}, "
            f"amount={_amount!r}, "
            f"currency={_currency!r}, "
            f"amount_formatted={_amount_formatted!r}, "
            f"mtype={_mtype!r}, "
            f"status={_status!r}, "
            f"metadata={_metadata!r}, "
            f"created_on={_created_on!r}, "
            f"mode={_mode!r}, "
            f"merchant_name={_merchant_name!r}, "
            f"store_name={_store_name!r}, "
            f"payment_type={_payment_type!r}, "
            f"user_data={_user_data!r}, "
            f"bank_transfer_payment_status={_bank_transfer_payment_status!r}, "
            f"bank_transfer_latest_deposit_date={_bank_transfer_latest_deposit_date!r}, "
            f"mcp_token_id={_mcp_token_id!r}, "
            f"charge_type={_charge_type!r}, "
            f"additional_properties={_additional_properties!r}, "
            f")"
        )

    def __str__(self):
        """Return a human-readable string representation."""
        _store_id=(
            self.store_id
            if hasattr(self, "store_id")
            else None
        )
        _resource_id=(
            self.resource_id
            if hasattr(self, "resource_id")
            else None
        )
        _charge_id=(
            self.charge_id
            if hasattr(self, "charge_id")
            else None
        )
        _amount=(
            self.amount
            if hasattr(self, "amount")
            else None
        )
        _currency=(
            self.currency
            if hasattr(self, "currency")
            else None
        )
        _amount_formatted=(
            self.amount_formatted
            if hasattr(self, "amount_formatted")
            else None
        )
        _mtype=(
            self.mtype
            if hasattr(self, "mtype")
            else None
        )
        _status=(
            self.status
            if hasattr(self, "status")
            else None
        )
        _metadata=(
            self.metadata
            if hasattr(self, "metadata")
            else None
        )
        _created_on=(
            self.created_on
            if hasattr(self, "created_on")
            else None
        )
        _mode=(
            self.mode
            if hasattr(self, "mode")
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
        _payment_type=(
            self.payment_type
            if hasattr(self, "payment_type")
            else None
        )
        _user_data=(
            self.user_data
            if hasattr(self, "user_data")
            else None
        )
        _bank_transfer_payment_status=(
            self.bank_transfer_payment_status
            if hasattr(self, "bank_transfer_payment_status")
            else None
        )
        _bank_transfer_latest_deposit_date=(
            self.bank_transfer_latest_deposit_date
            if hasattr(self, "bank_transfer_latest_deposit_date")
            else None
        )
        _mcp_token_id=(
            self.mcp_token_id
            if hasattr(self, "mcp_token_id")
            else None
        )
        _charge_type=(
            self.charge_type
            if hasattr(self, "charge_type")
            else None
        )
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"store_id={_store_id!s}, "
            f"resource_id={_resource_id!s}, "
            f"charge_id={_charge_id!s}, "
            f"amount={_amount!s}, "
            f"currency={_currency!s}, "
            f"amount_formatted={_amount_formatted!s}, "
            f"mtype={_mtype!s}, "
            f"status={_status!s}, "
            f"metadata={_metadata!s}, "
            f"created_on={_created_on!s}, "
            f"mode={_mode!s}, "
            f"merchant_name={_merchant_name!s}, "
            f"store_name={_store_name!s}, "
            f"payment_type={_payment_type!s}, "
            f"user_data={_user_data!s}, "
            f"bank_transfer_payment_status={_bank_transfer_payment_status!s}, "
            f"bank_transfer_latest_deposit_date={_bank_transfer_latest_deposit_date!s}, "
            f"mcp_token_id={_mcp_token_id!s}, "
            f"charge_type={_charge_type!s}, "
            f"additional_properties={_additional_properties!s}, "
            f")"
        )
