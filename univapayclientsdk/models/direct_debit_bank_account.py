"""univapay_client_sdk.

This file was automatically generated for Univapay by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

# ruff: noqa: E501
from univapayclientsdk.api_helper import APIHelper


class DirectDebitBankAccount(object):
    """Implementation of the 'DirectDebitBankAccount' model.

    A consumer bank account registered for direct debit.

    Attributes:
        id (str): Unique identifier of a direct debit bank account (銀行口座ID).
        legacy_store_id (str): Identifier of the merchant in the legacy direct debit
            system.
        merchant_id (uuid|str): The merchant that owns this bank account.
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
        registration_origin (DirectDebitRegistrationOrigin): Where the bank account
            was registered from — `merchant_console` for the merchant dashboard,
            `anywhere` otherwise.
        status (DirectDebitBankAccountStatus): Bank account state (有効・無効・登録失敗). Only
            an `active` account can have transfers registered against it.
            `registration_failed` means the bank rejected the account details.
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
        "user_number": "user_number",
        "bank_code": "bank_code",
        "bank_name": "bank_name",
        "branch_code": "branch_code",
        "bank_account_type": "bank_account_type",
        "bank_account_name": "bank_account_name",
        "bank_account_number": "bank_account_number",
        "registration_origin": "registration_origin",
        "status": "status",
        "created_on": "created_on",
        "updated_on": "updated_on",
    }

    _optionals = [
        "id",
        "legacy_store_id",
        "merchant_id",
        "user_number",
        "bank_code",
        "bank_name",
        "branch_code",
        "bank_account_type",
        "bank_account_name",
        "bank_account_number",
        "registration_origin",
        "status",
        "created_on",
        "updated_on",
    ]

    def __init__(
        self,
        id=APIHelper.SKIP,
        legacy_store_id=APIHelper.SKIP,
        merchant_id=APIHelper.SKIP,
        user_number=APIHelper.SKIP,
        bank_code=APIHelper.SKIP,
        bank_name=APIHelper.SKIP,
        branch_code=APIHelper.SKIP,
        bank_account_type=APIHelper.SKIP,
        bank_account_name=APIHelper.SKIP,
        bank_account_number=APIHelper.SKIP,
        registration_origin=APIHelper.SKIP,
        status=APIHelper.SKIP,
        created_on=APIHelper.SKIP,
        updated_on=APIHelper.SKIP,
        additional_properties=None):
        """Initialize a DirectDebitBankAccount instance."""
        # Initialize members of the class
        if id is not APIHelper.SKIP:
            self.id = id
        if legacy_store_id is not APIHelper.SKIP:
            self.legacy_store_id = legacy_store_id
        if merchant_id is not APIHelper.SKIP:
            self.merchant_id = merchant_id
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
        if registration_origin is not APIHelper.SKIP:
            self.registration_origin = registration_origin
        if status is not APIHelper.SKIP:
            self.status = status
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
        registration_origin =\
            dictionary.get("registration_origin")\
            if dictionary.get("registration_origin")\
                else APIHelper.SKIP
        status =\
            dictionary.get("status")\
            if dictionary.get("status")\
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
                   user_number,
                   bank_code,
                   bank_name,
                   branch_code,
                   bank_account_type,
                   bank_account_name,
                   bank_account_number,
                   registration_origin,
                   status,
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
        _registration_origin=(
            self.registration_origin
            if hasattr(self, "registration_origin")
            else None
        )
        _status=(
            self.status
            if hasattr(self, "status")
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
            f"user_number={_user_number!r}, "
            f"bank_code={_bank_code!r}, "
            f"bank_name={_bank_name!r}, "
            f"branch_code={_branch_code!r}, "
            f"bank_account_type={_bank_account_type!r}, "
            f"bank_account_name={_bank_account_name!r}, "
            f"bank_account_number={_bank_account_number!r}, "
            f"registration_origin={_registration_origin!r}, "
            f"status={_status!r}, "
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
        _registration_origin=(
            self.registration_origin
            if hasattr(self, "registration_origin")
            else None
        )
        _status=(
            self.status
            if hasattr(self, "status")
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
            f"user_number={_user_number!s}, "
            f"bank_code={_bank_code!s}, "
            f"bank_name={_bank_name!s}, "
            f"branch_code={_branch_code!s}, "
            f"bank_account_type={_bank_account_type!s}, "
            f"bank_account_name={_bank_account_name!s}, "
            f"bank_account_number={_bank_account_number!s}, "
            f"registration_origin={_registration_origin!s}, "
            f"status={_status!s}, "
            f"created_on={_created_on!s}, "
            f"updated_on={_updated_on!s}, "
            f"additional_properties={_additional_properties!s}, "
            f")"
        )
