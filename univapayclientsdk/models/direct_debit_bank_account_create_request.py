"""univapay_client_sdk.

This file was automatically generated for Univapay by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

# ruff: noqa: E501
from univapayclientsdk.api_helper import APIHelper


class DirectDebitBankAccountCreateRequest(object):
    """Implementation of the 'DirectDebitBankAccountCreateRequest' model.

    Request payload for registering a consumer bank account for direct debit.

    Attributes:
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
        additional_properties (Dict[str, Any]): The additional properties for the
            model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "user_number": "user_number",
        "bank_code": "bank_code",
        "bank_name": "bank_name",
        "branch_code": "branch_code",
        "bank_account_type": "bank_account_type",
        "bank_account_name": "bank_account_name",
        "bank_account_number": "bank_account_number",
    }

    def __init__(
        self,
        user_number=None,
        bank_code=None,
        bank_name=None,
        branch_code=None,
        bank_account_type=None,
        bank_account_name=None,
        bank_account_number=None,
        additional_properties=None):
        """Initialize a DirectDebitBankAccountCreateRequest instance."""
        # Initialize members of the class
        self.user_number = user_number
        self.bank_code = bank_code
        self.bank_name = bank_name
        self.branch_code = branch_code
        self.bank_account_type = bank_account_type
        self.bank_account_name = bank_account_name
        self.bank_account_number = bank_account_number

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
        user_number =\
            dictionary.get("user_number")\
            if dictionary.get("user_number")\
                else None
        bank_code =\
            dictionary.get("bank_code")\
            if dictionary.get("bank_code")\
                else None
        bank_name =\
            dictionary.get("bank_name")\
            if dictionary.get("bank_name")\
                else None
        branch_code =\
            dictionary.get("branch_code")\
            if dictionary.get("branch_code")\
                else None
        bank_account_type =\
            dictionary.get("bank_account_type")\
            if dictionary.get("bank_account_type")\
                else None
        bank_account_name =\
            dictionary.get("bank_account_name")\
            if dictionary.get("bank_account_name")\
                else None
        bank_account_number =\
            dictionary.get("bank_account_number")\
            if dictionary.get("bank_account_number")\
                else None

        additional_properties = APIHelper.get_additional_properties(
            dictionary={k: v for k, v in dictionary.items()
                        if k not in cls._names.values()},
            unboxing_function=lambda value: value)

        # Return an object of this model
        return cls(user_number,
                   bank_code,
                   bank_name,
                   branch_code,
                   bank_account_type,
                   bank_account_name,
                   bank_account_number,
                   additional_properties)

    def __repr__(self):
        """Return a unambiguous string representation."""
        _user_number=self.user_number
        _bank_code=self.bank_code
        _bank_name=self.bank_name
        _branch_code=self.branch_code
        _bank_account_type=self.bank_account_type
        _bank_account_name=self.bank_account_name
        _bank_account_number=self.bank_account_number
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"user_number={_user_number!r}, "
            f"bank_code={_bank_code!r}, "
            f"bank_name={_bank_name!r}, "
            f"branch_code={_branch_code!r}, "
            f"bank_account_type={_bank_account_type!r}, "
            f"bank_account_name={_bank_account_name!r}, "
            f"bank_account_number={_bank_account_number!r}, "
            f"additional_properties={_additional_properties!r}, "
            f")"
        )

    def __str__(self):
        """Return a human-readable string representation."""
        _user_number=self.user_number
        _bank_code=self.bank_code
        _bank_name=self.bank_name
        _branch_code=self.branch_code
        _bank_account_type=self.bank_account_type
        _bank_account_name=self.bank_account_name
        _bank_account_number=self.bank_account_number
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"user_number={_user_number!s}, "
            f"bank_code={_bank_code!s}, "
            f"bank_name={_bank_name!s}, "
            f"branch_code={_branch_code!s}, "
            f"bank_account_type={_bank_account_type!s}, "
            f"bank_account_name={_bank_account_name!s}, "
            f"bank_account_number={_bank_account_number!s}, "
            f"additional_properties={_additional_properties!s}, "
            f")"
        )
