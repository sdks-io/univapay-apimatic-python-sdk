"""univapay_client_sdk.

This file was automatically generated for Univapay by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

# ruff: noqa: E501
import dateutil.parser

from univapayclientsdk.api_helper import APIHelper


class DirectDebitBankTransfer(object):
    """Implementation of the 'DirectDebitBankTransfer' model.

    A single scheduled pull of funds from a registered bank account. The bank account
    details are copied onto the transfer at registration time, so later edits to the
    account do not change past transfers.

    Attributes:
        id (str): Unique identifier of a direct debit bank transfer (振替ID).
        legacy_store_id (str): Identifier of the merchant in the legacy direct debit
            system.
        merchant_id (uuid|str): The merchant that owns this transfer.
        bank_account_id (str): Unique identifier of a direct debit bank account
            (銀行口座ID).
        user_number (str): The merchant's own membership number for the consumer
            (会員番号). Alphanumeric.
        bank_code (str): Four-digit code identifying the consumer's bank (銀行コード).
        bank_name (str): Bank name in half-width katakana (銀行名).
        branch_code (str): Three-digit code identifying the bank branch (支店コード).
        bank_account_type (DirectDebitBankAccountType): Deposit account type (預金種類) —
            `regular` (普通), `current` (当座), `savings` (貯蓄) or `others` (その他).
        bank_account_name (str): Account holder name (口座名義), in half-width katakana.
            Full-width characters are rejected by the bank.
        bank_account_number (str): Seven-digit account number (口座番号).
        amount (int): Transfer amount in JPY. Must be a positive, non-zero whole
            number.
        debit_date (DirectDebitDebitDate): Monthly debit cycle — funds are pulled on
            either the 14th or the 27th.
        calculated_debit_date (date): The actual business day on which funds are
            pulled (計算された振替日), derived from the debit cycle.
        lock (DirectDebitBankTransferLock): Whether the transfer can still be edited.
            Transfers are `unlocked` until the upload deadline for their debit cycle
            passes, after which they are `locked` and can no longer be changed or
            deleted.
        status (DirectDebitBankTransferStatus): Transfer state. `awaiting` until the
            bank reports back, then `successful` or `failed`. Results are reflected
            days after the debit date, not immediately.
        error (DirectDebitBankTransferError): Failure reason, or null while the
            transfer is awaiting a result or has succeeded.
        created_on (datetime): Timestamp when the resource was created.
        updated_on (datetime): Timestamp when the resource was last updated.
        additional_properties (Dict[str, Any]): The additional properties for the
            model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "id": "id",
        "legacy_store_id": "legacy_store_id",
        "merchant_id": "merchant_id",
        "bank_account_id": "bank_account_id",
        "user_number": "user_number",
        "bank_code": "bank_code",
        "bank_name": "bank_name",
        "branch_code": "branch_code",
        "bank_account_type": "bank_account_type",
        "bank_account_name": "bank_account_name",
        "bank_account_number": "bank_account_number",
        "amount": "amount",
        "debit_date": "debit_date",
        "calculated_debit_date": "calculated_debit_date",
        "lock": "lock",
        "status": "status",
        "error": "error",
        "created_on": "created_on",
        "updated_on": "updated_on",
    }

    _optionals = [
        "id",
        "legacy_store_id",
        "merchant_id",
        "bank_account_id",
        "user_number",
        "bank_code",
        "bank_name",
        "branch_code",
        "bank_account_type",
        "bank_account_name",
        "bank_account_number",
        "amount",
        "debit_date",
        "calculated_debit_date",
        "lock",
        "status",
        "error",
        "created_on",
        "updated_on",
    ]

    _nullables = [
        "error",
    ]

    def __init__(
        self,
        id=APIHelper.SKIP,
        legacy_store_id=APIHelper.SKIP,
        merchant_id=APIHelper.SKIP,
        bank_account_id=APIHelper.SKIP,
        user_number=APIHelper.SKIP,
        bank_code=APIHelper.SKIP,
        bank_name=APIHelper.SKIP,
        branch_code=APIHelper.SKIP,
        bank_account_type=APIHelper.SKIP,
        bank_account_name=APIHelper.SKIP,
        bank_account_number=APIHelper.SKIP,
        amount=APIHelper.SKIP,
        debit_date=APIHelper.SKIP,
        calculated_debit_date=APIHelper.SKIP,
        lock=APIHelper.SKIP,
        status=APIHelper.SKIP,
        error=APIHelper.SKIP,
        created_on=APIHelper.SKIP,
        updated_on=APIHelper.SKIP,
        additional_properties=None):
        """Initialize a DirectDebitBankTransfer instance."""
        # Initialize members of the class
        if id is not APIHelper.SKIP:
            self.id = id
        if legacy_store_id is not APIHelper.SKIP:
            self.legacy_store_id = legacy_store_id
        if merchant_id is not APIHelper.SKIP:
            self.merchant_id = merchant_id
        if bank_account_id is not APIHelper.SKIP:
            self.bank_account_id = bank_account_id
        if user_number is not APIHelper.SKIP:
            self.user_number = user_number
        if bank_code is not APIHelper.SKIP:
            self.bank_code = bank_code
        if bank_name is not APIHelper.SKIP:
            self.bank_name = bank_name
        if branch_code is not APIHelper.SKIP:
            self.branch_code = branch_code
        if bank_account_type is not APIHelper.SKIP:
            self.bank_account_type = bank_account_type
        if bank_account_name is not APIHelper.SKIP:
            self.bank_account_name = bank_account_name
        if bank_account_number is not APIHelper.SKIP:
            self.bank_account_number = bank_account_number
        if amount is not APIHelper.SKIP:
            self.amount = amount
        if debit_date is not APIHelper.SKIP:
            self.debit_date = debit_date
        if calculated_debit_date is not APIHelper.SKIP:
            self.calculated_debit_date = calculated_debit_date
        if lock is not APIHelper.SKIP:
            self.lock = lock
        if status is not APIHelper.SKIP:
            self.status = status
        if error is not APIHelper.SKIP:
            self.error = error
        if created_on is not APIHelper.SKIP:
            self.created_on =\
                 APIHelper.apply_datetime_converter(
                created_on, APIHelper.RFC3339DateTime)\
                 if created_on else None
        if updated_on is not APIHelper.SKIP:
            self.updated_on =\
                 APIHelper.apply_datetime_converter(
                updated_on, APIHelper.RFC3339DateTime)\
                 if updated_on else None

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
        legacy_store_id =\
            dictionary.get("legacy_store_id")\
            if dictionary.get("legacy_store_id")\
                else APIHelper.SKIP
        merchant_id =\
            dictionary.get("merchant_id")\
            if dictionary.get("merchant_id")\
                else APIHelper.SKIP
        bank_account_id =\
            dictionary.get("bank_account_id")\
            if dictionary.get("bank_account_id")\
                else APIHelper.SKIP
        user_number =\
            dictionary.get("user_number")\
            if dictionary.get("user_number")\
                else APIHelper.SKIP
        bank_code =\
            dictionary.get("bank_code")\
            if dictionary.get("bank_code")\
                else APIHelper.SKIP
        bank_name =\
            dictionary.get("bank_name")\
            if dictionary.get("bank_name")\
                else APIHelper.SKIP
        branch_code =\
            dictionary.get("branch_code")\
            if dictionary.get("branch_code")\
                else APIHelper.SKIP
        bank_account_type =\
            dictionary.get("bank_account_type")\
            if dictionary.get("bank_account_type")\
                else APIHelper.SKIP
        bank_account_name =\
            dictionary.get("bank_account_name")\
            if dictionary.get("bank_account_name")\
                else APIHelper.SKIP
        bank_account_number =\
            dictionary.get("bank_account_number")\
            if dictionary.get("bank_account_number")\
                else APIHelper.SKIP
        amount =\
            dictionary.get("amount")\
            if dictionary.get("amount")\
                else APIHelper.SKIP
        debit_date =\
            dictionary.get("debit_date")\
            if dictionary.get("debit_date")\
                else APIHelper.SKIP
        calculated_debit_date = dateutil.parser.parse(
            dictionary.get("calculated_debit_date")).date()\
            if dictionary.get("calculated_debit_date") else APIHelper.SKIP
        lock =\
            dictionary.get("lock")\
            if dictionary.get("lock")\
                else APIHelper.SKIP
        status =\
            dictionary.get("status")\
            if dictionary.get("status")\
                else APIHelper.SKIP
        error =\
            dictionary.get("error")\
            if "error" in dictionary.keys()\
                else APIHelper.SKIP
        created_on = APIHelper.RFC3339DateTime.from_value(
            dictionary.get("created_on")).datetime\
            if dictionary.get("created_on") else APIHelper.SKIP
        updated_on = APIHelper.RFC3339DateTime.from_value(
            dictionary.get("updated_on")).datetime\
            if dictionary.get("updated_on") else APIHelper.SKIP

        additional_properties = APIHelper.get_additional_properties(
            dictionary={k: v for k, v in dictionary.items()
                        if k not in cls._names.values()},
            unboxing_function=lambda value: value)

        # Return an object of this model
        return cls(id,
                   legacy_store_id,
                   merchant_id,
                   bank_account_id,
                   user_number,
                   bank_code,
                   bank_name,
                   branch_code,
                   bank_account_type,
                   bank_account_name,
                   bank_account_number,
                   amount,
                   debit_date,
                   calculated_debit_date,
                   lock,
                   status,
                   error,
                   created_on,
                   updated_on,
                   additional_properties)

    def __repr__(self):
        """Return a unambiguous string representation."""
        _id=(
            self.id
            if hasattr(self, "id")
            else None
        )
        _legacy_store_id=(
            self.legacy_store_id
            if hasattr(self, "legacy_store_id")
            else None
        )
        _merchant_id=(
            self.merchant_id
            if hasattr(self, "merchant_id")
            else None
        )
        _bank_account_id=(
            self.bank_account_id
            if hasattr(self, "bank_account_id")
            else None
        )
        _user_number=(
            self.user_number
            if hasattr(self, "user_number")
            else None
        )
        _bank_code=(
            self.bank_code
            if hasattr(self, "bank_code")
            else None
        )
        _bank_name=(
            self.bank_name
            if hasattr(self, "bank_name")
            else None
        )
        _branch_code=(
            self.branch_code
            if hasattr(self, "branch_code")
            else None
        )
        _bank_account_type=(
            self.bank_account_type
            if hasattr(self, "bank_account_type")
            else None
        )
        _bank_account_name=(
            self.bank_account_name
            if hasattr(self, "bank_account_name")
            else None
        )
        _bank_account_number=(
            self.bank_account_number
            if hasattr(self, "bank_account_number")
            else None
        )
        _amount=(
            self.amount
            if hasattr(self, "amount")
            else None
        )
        _debit_date=(
            self.debit_date
            if hasattr(self, "debit_date")
            else None
        )
        _calculated_debit_date=(
            self.calculated_debit_date
            if hasattr(self, "calculated_debit_date")
            else None
        )
        _lock=(
            self.lock
            if hasattr(self, "lock")
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
        _created_on=(
            self.created_on
            if hasattr(self, "created_on")
            else None
        )
        _updated_on=(
            self.updated_on
            if hasattr(self, "updated_on")
            else None
        )
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"id={_id!r}, "
            f"legacy_store_id={_legacy_store_id!r}, "
            f"merchant_id={_merchant_id!r}, "
            f"bank_account_id={_bank_account_id!r}, "
            f"user_number={_user_number!r}, "
            f"bank_code={_bank_code!r}, "
            f"bank_name={_bank_name!r}, "
            f"branch_code={_branch_code!r}, "
            f"bank_account_type={_bank_account_type!r}, "
            f"bank_account_name={_bank_account_name!r}, "
            f"bank_account_number={_bank_account_number!r}, "
            f"amount={_amount!r}, "
            f"debit_date={_debit_date!r}, "
            f"calculated_debit_date={_calculated_debit_date!r}, "
            f"lock={_lock!r}, "
            f"status={_status!r}, "
            f"error={_error!r}, "
            f"created_on={_created_on!r}, "
            f"updated_on={_updated_on!r}, "
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
        _legacy_store_id=(
            self.legacy_store_id
            if hasattr(self, "legacy_store_id")
            else None
        )
        _merchant_id=(
            self.merchant_id
            if hasattr(self, "merchant_id")
            else None
        )
        _bank_account_id=(
            self.bank_account_id
            if hasattr(self, "bank_account_id")
            else None
        )
        _user_number=(
            self.user_number
            if hasattr(self, "user_number")
            else None
        )
        _bank_code=(
            self.bank_code
            if hasattr(self, "bank_code")
            else None
        )
        _bank_name=(
            self.bank_name
            if hasattr(self, "bank_name")
            else None
        )
        _branch_code=(
            self.branch_code
            if hasattr(self, "branch_code")
            else None
        )
        _bank_account_type=(
            self.bank_account_type
            if hasattr(self, "bank_account_type")
            else None
        )
        _bank_account_name=(
            self.bank_account_name
            if hasattr(self, "bank_account_name")
            else None
        )
        _bank_account_number=(
            self.bank_account_number
            if hasattr(self, "bank_account_number")
            else None
        )
        _amount=(
            self.amount
            if hasattr(self, "amount")
            else None
        )
        _debit_date=(
            self.debit_date
            if hasattr(self, "debit_date")
            else None
        )
        _calculated_debit_date=(
            self.calculated_debit_date
            if hasattr(self, "calculated_debit_date")
            else None
        )
        _lock=(
            self.lock
            if hasattr(self, "lock")
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
        _created_on=(
            self.created_on
            if hasattr(self, "created_on")
            else None
        )
        _updated_on=(
            self.updated_on
            if hasattr(self, "updated_on")
            else None
        )
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"id={_id!s}, "
            f"legacy_store_id={_legacy_store_id!s}, "
            f"merchant_id={_merchant_id!s}, "
            f"bank_account_id={_bank_account_id!s}, "
            f"user_number={_user_number!s}, "
            f"bank_code={_bank_code!s}, "
            f"bank_name={_bank_name!s}, "
            f"branch_code={_branch_code!s}, "
            f"bank_account_type={_bank_account_type!s}, "
            f"bank_account_name={_bank_account_name!s}, "
            f"bank_account_number={_bank_account_number!s}, "
            f"amount={_amount!s}, "
            f"debit_date={_debit_date!s}, "
            f"calculated_debit_date={_calculated_debit_date!s}, "
            f"lock={_lock!s}, "
            f"status={_status!s}, "
            f"error={_error!s}, "
            f"created_on={_created_on!s}, "
            f"updated_on={_updated_on!s}, "
            f"additional_properties={_additional_properties!s}, "
            f")"
        )
