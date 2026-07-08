"""univapay_client_sdk.

This file was automatically generated for Univapay by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

# ruff: noqa: E501
import dateutil.parser

from univapayclientsdk.api_helper import APIHelper


class BankTransferLedger(object):
    """Implementation of the 'BankTransferLedger' model.

    Single bank transfer ledger entry associated with a charge.

    Attributes:
        bank_ledger_type (BankTransferLedgerBankLedgerType): Bank Transfer Ledger
            Bank Ledger Type schema.
        amount (int): Amount in the smallest currency unit.
        balance (int): Current balance in the smallest currency unit.
        virtual_bank_account_holder_name (str): Virtual bank account holder name.
        virtual_bank_account_number (str): Virtual bank account number.
        virtual_account_id (str): Virtual account id value.
        transaction_date (date): Transaction date.
        transaction_timestamp (datetime): Transaction timestamp.
        mode (BankTransferLedgerMode): Bank Transfer Ledger Mode schema.
        created_on (datetime): Timestamp when the resource was created.
        additional_properties (Dict[str, Any]): The additional properties for the
            model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "bank_ledger_type": "bank_ledger_type",
        "amount": "amount",
        "balance": "balance",
        "virtual_bank_account_holder_name": "virtual_bank_account_holder_name",
        "virtual_bank_account_number": "virtual_bank_account_number",
        "virtual_account_id": "virtual_account_id",
        "transaction_date": "transaction_date",
        "transaction_timestamp": "transaction_timestamp",
        "mode": "mode",
        "created_on": "created_on",
    }

    _optionals = [
        "bank_ledger_type",
        "amount",
        "balance",
        "virtual_bank_account_holder_name",
        "virtual_bank_account_number",
        "virtual_account_id",
        "transaction_date",
        "transaction_timestamp",
        "mode",
        "created_on",
    ]

    def __init__(
        self,
        bank_ledger_type=APIHelper.SKIP,
        amount=APIHelper.SKIP,
        balance=APIHelper.SKIP,
        virtual_bank_account_holder_name=APIHelper.SKIP,
        virtual_bank_account_number=APIHelper.SKIP,
        virtual_account_id=APIHelper.SKIP,
        transaction_date=APIHelper.SKIP,
        transaction_timestamp=APIHelper.SKIP,
        mode=APIHelper.SKIP,
        created_on=APIHelper.SKIP,
        additional_properties=None):
        """Initialize a BankTransferLedger instance."""
        # Initialize members of the class
        if bank_ledger_type is not APIHelper.SKIP:
            self.bank_ledger_type = bank_ledger_type
        if amount is not APIHelper.SKIP:
            self.amount = amount
        if balance is not APIHelper.SKIP:
            self.balance = balance
        if virtual_bank_account_holder_name is not APIHelper.SKIP:
            self.virtual_bank_account_holder_name = virtual_bank_account_holder_name
        if virtual_bank_account_number is not APIHelper.SKIP:
            self.virtual_bank_account_number = virtual_bank_account_number
        if virtual_account_id is not APIHelper.SKIP:
            self.virtual_account_id = virtual_account_id
        if transaction_date is not APIHelper.SKIP:
            self.transaction_date = transaction_date
        if transaction_timestamp is not APIHelper.SKIP:
            self.transaction_timestamp =\
                 APIHelper.apply_datetime_converter(
                transaction_timestamp, APIHelper.RFC3339DateTime)\
                 if transaction_timestamp else None
        if mode is not APIHelper.SKIP:
            self.mode = mode
        if created_on is not APIHelper.SKIP:
            self.created_on =\
                 APIHelper.apply_datetime_converter(
                created_on, APIHelper.RFC3339DateTime)\
                 if created_on else None

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
        bank_ledger_type =\
            dictionary.get("bank_ledger_type")\
            if dictionary.get("bank_ledger_type")\
                else APIHelper.SKIP
        amount =\
            dictionary.get("amount")\
            if dictionary.get("amount")\
                else APIHelper.SKIP
        balance =\
            dictionary.get("balance")\
            if dictionary.get("balance")\
                else APIHelper.SKIP
        virtual_bank_account_holder_name =\
            dictionary.get("virtual_bank_account_holder_name")\
            if dictionary.get("virtual_bank_account_holder_name")\
                else APIHelper.SKIP
        virtual_bank_account_number =\
            dictionary.get("virtual_bank_account_number")\
            if dictionary.get("virtual_bank_account_number")\
                else APIHelper.SKIP
        virtual_account_id =\
            dictionary.get("virtual_account_id")\
            if dictionary.get("virtual_account_id")\
                else APIHelper.SKIP
        transaction_date = dateutil.parser.parse(
            dictionary.get("transaction_date")).date()\
            if dictionary.get("transaction_date") else APIHelper.SKIP
        transaction_timestamp = APIHelper.RFC3339DateTime.from_value(
            dictionary.get("transaction_timestamp")).datetime\
            if dictionary.get("transaction_timestamp") else APIHelper.SKIP
        mode =\
            dictionary.get("mode")\
            if dictionary.get("mode")\
                else APIHelper.SKIP
        created_on = APIHelper.RFC3339DateTime.from_value(
            dictionary.get("created_on")).datetime\
            if dictionary.get("created_on") else APIHelper.SKIP

        additional_properties = APIHelper.get_additional_properties(
            dictionary={k: v for k, v in dictionary.items()
                        if k not in cls._names.values()},
            unboxing_function=lambda value: value)

        # Return an object of this model
        return cls(bank_ledger_type,
                   amount,
                   balance,
                   virtual_bank_account_holder_name,
                   virtual_bank_account_number,
                   virtual_account_id,
                   transaction_date,
                   transaction_timestamp,
                   mode,
                   created_on,
                   additional_properties)

    def __repr__(self):
        """Return a unambiguous string representation."""
        _bank_ledger_type=(
            self.bank_ledger_type
            if hasattr(self, "bank_ledger_type")
            else None
        )
        _amount=(
            self.amount
            if hasattr(self, "amount")
            else None
        )
        _balance=(
            self.balance
            if hasattr(self, "balance")
            else None
        )
        _virtual_bank_account_holder_name=(
            self.virtual_bank_account_holder_name
            if hasattr(self, "virtual_bank_account_holder_name")
            else None
        )
        _virtual_bank_account_number=(
            self.virtual_bank_account_number
            if hasattr(self, "virtual_bank_account_number")
            else None
        )
        _virtual_account_id=(
            self.virtual_account_id
            if hasattr(self, "virtual_account_id")
            else None
        )
        _transaction_date=(
            self.transaction_date
            if hasattr(self, "transaction_date")
            else None
        )
        _transaction_timestamp=(
            self.transaction_timestamp
            if hasattr(self, "transaction_timestamp")
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
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"bank_ledger_type={_bank_ledger_type!r}, "
            f"amount={_amount!r}, "
            f"balance={_balance!r}, "
            f"virtual_bank_account_holder_name={_virtual_bank_account_holder_name!r}, "
            f"virtual_bank_account_number={_virtual_bank_account_number!r}, "
            f"virtual_account_id={_virtual_account_id!r}, "
            f"transaction_date={_transaction_date!r}, "
            f"transaction_timestamp={_transaction_timestamp!r}, "
            f"mode={_mode!r}, "
            f"created_on={_created_on!r}, "
            f"additional_properties={_additional_properties!r}, "
            f")"
        )

    def __str__(self):
        """Return a human-readable string representation."""
        _bank_ledger_type=(
            self.bank_ledger_type
            if hasattr(self, "bank_ledger_type")
            else None
        )
        _amount=(
            self.amount
            if hasattr(self, "amount")
            else None
        )
        _balance=(
            self.balance
            if hasattr(self, "balance")
            else None
        )
        _virtual_bank_account_holder_name=(
            self.virtual_bank_account_holder_name
            if hasattr(self, "virtual_bank_account_holder_name")
            else None
        )
        _virtual_bank_account_number=(
            self.virtual_bank_account_number
            if hasattr(self, "virtual_bank_account_number")
            else None
        )
        _virtual_account_id=(
            self.virtual_account_id
            if hasattr(self, "virtual_account_id")
            else None
        )
        _transaction_date=(
            self.transaction_date
            if hasattr(self, "transaction_date")
            else None
        )
        _transaction_timestamp=(
            self.transaction_timestamp
            if hasattr(self, "transaction_timestamp")
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
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"bank_ledger_type={_bank_ledger_type!s}, "
            f"amount={_amount!s}, "
            f"balance={_balance!s}, "
            f"virtual_bank_account_holder_name={_virtual_bank_account_holder_name!s}, "
            f"virtual_bank_account_number={_virtual_bank_account_number!s}, "
            f"virtual_account_id={_virtual_account_id!s}, "
            f"transaction_date={_transaction_date!s}, "
            f"transaction_timestamp={_transaction_timestamp!s}, "
            f"mode={_mode!s}, "
            f"created_on={_created_on!s}, "
            f"additional_properties={_additional_properties!s}, "
            f")"
        )
