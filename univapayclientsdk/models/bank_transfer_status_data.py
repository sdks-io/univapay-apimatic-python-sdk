"""univapay_client_sdk.

This file was automatically generated for Univapay by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

# ruff: noqa: E501
from univapayclientsdk.api_helper import APIHelper
from univapayclientsdk.models.generic_metadata import (
    GenericMetadata,
)


class BankTransferStatusData(object):
    """Implementation of the 'BankTransferStatusData' model.

    Data payload for `bank_transfer_status_updated` webhook events. Contains the bank
    transfer extension fields inlined alongside amount and metadata.

    Attributes:
        id (uuid|str): Bank transfer charge extension ID.
        charge_id (uuid|str): ID of the associated charge.
        payment_status (BankTransferPaymentStatus): Payment status of a bank transfer
            charge.
        latest_deposit_date (datetime): Date of the most recent deposit.
        created_on (datetime): When the bank transfer extension record was created.
        latest_deposit_amount (int): Amount of the most recent deposit in minor
            currency units.
        balance (int): Current outstanding balance in minor currency units.
        currency (str): ISO 4217 currency code.
        amount (int): Total charge amount in minor currency units.
        amount_difference (int): Difference between paid and expected amount
            (positive = over, negative = under).
        token_metadata (GenericMetadata): A free-form dictionary for custom metadata.
        charge_metadata (GenericMetadata): A free-form dictionary for custom metadata.
        additional_properties (Dict[str, Any]): The additional properties for the
            model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "id": "id",
        "charge_id": "charge_id",
        "payment_status": "payment_status",
        "latest_deposit_date": "latest_deposit_date",
        "created_on": "created_on",
        "latest_deposit_amount": "latest_deposit_amount",
        "balance": "balance",
        "currency": "currency",
        "amount": "amount",
        "amount_difference": "amount_difference",
        "token_metadata": "token_metadata",
        "charge_metadata": "charge_metadata",
    }

    _optionals = [
        "id",
        "charge_id",
        "payment_status",
        "latest_deposit_date",
        "created_on",
        "latest_deposit_amount",
        "balance",
        "currency",
        "amount",
        "amount_difference",
        "token_metadata",
        "charge_metadata",
    ]

    _nullables = [
        "id",
        "latest_deposit_date",
        "created_on",
        "latest_deposit_amount",
        "balance",
        "amount_difference",
    ]

    def __init__(
        self,
        id=APIHelper.SKIP,
        charge_id=APIHelper.SKIP,
        payment_status=APIHelper.SKIP,
        latest_deposit_date=APIHelper.SKIP,
        created_on=APIHelper.SKIP,
        latest_deposit_amount=APIHelper.SKIP,
        balance=APIHelper.SKIP,
        currency=APIHelper.SKIP,
        amount=APIHelper.SKIP,
        amount_difference=APIHelper.SKIP,
        token_metadata=APIHelper.SKIP,
        charge_metadata=APIHelper.SKIP,
        additional_properties=None):
        """Initialize a BankTransferStatusData instance."""
        # Initialize members of the class
        if id is not APIHelper.SKIP:
            self.id = id
        if charge_id is not APIHelper.SKIP:
            self.charge_id = charge_id
        if payment_status is not APIHelper.SKIP:
            self.payment_status = payment_status
        if latest_deposit_date is not APIHelper.SKIP:
            self.latest_deposit_date =\
                 APIHelper.apply_datetime_converter(
                latest_deposit_date, APIHelper.RFC3339DateTime)\
                 if latest_deposit_date else None
        if created_on is not APIHelper.SKIP:
            self.created_on =\
                 APIHelper.apply_datetime_converter(
                created_on, APIHelper.RFC3339DateTime)\
                 if created_on else None
        if latest_deposit_amount is not APIHelper.SKIP:
            self.latest_deposit_amount = latest_deposit_amount
        if balance is not APIHelper.SKIP:
            self.balance = balance
        if currency is not APIHelper.SKIP:
            self.currency = currency
        if amount is not APIHelper.SKIP:
            self.amount = amount
        if amount_difference is not APIHelper.SKIP:
            self.amount_difference = amount_difference
        if token_metadata is not APIHelper.SKIP:
            self.token_metadata = token_metadata
        if charge_metadata is not APIHelper.SKIP:
            self.charge_metadata = charge_metadata

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
            if "id" in dictionary.keys()\
                else APIHelper.SKIP
        charge_id =\
            dictionary.get("charge_id")\
            if dictionary.get("charge_id")\
                else APIHelper.SKIP
        payment_status =\
            dictionary.get("payment_status")\
            if dictionary.get("payment_status")\
                else APIHelper.SKIP
        if "latest_deposit_date" in dictionary.keys():
            latest_deposit_date = APIHelper.RFC3339DateTime.from_value(
                dictionary.get("latest_deposit_date")).datetime\
                if dictionary.get("latest_deposit_date") else None

        else:
            latest_deposit_date = APIHelper.SKIP
        if "created_on" in dictionary.keys():
            created_on = APIHelper.RFC3339DateTime.from_value(
                dictionary.get("created_on")).datetime\
                if dictionary.get("created_on") else None

        else:
            created_on = APIHelper.SKIP
        latest_deposit_amount =\
            dictionary.get("latest_deposit_amount")\
            if "latest_deposit_amount" in dictionary.keys()\
                else APIHelper.SKIP
        balance =\
            dictionary.get("balance")\
            if "balance" in dictionary.keys()\
                else APIHelper.SKIP
        currency =\
            dictionary.get("currency")\
            if dictionary.get("currency")\
                else APIHelper.SKIP
        amount =\
            dictionary.get("amount")\
            if dictionary.get("amount")\
                else APIHelper.SKIP
        amount_difference =\
            dictionary.get("amount_difference")\
            if "amount_difference" in dictionary.keys()\
                else APIHelper.SKIP
        token_metadata =\
            GenericMetadata.from_dictionary(
                dictionary.get("token_metadata"))\
                if "token_metadata" in dictionary.keys()\
                else APIHelper.SKIP
        charge_metadata =\
            GenericMetadata.from_dictionary(
                dictionary.get("charge_metadata"))\
                if "charge_metadata" in dictionary.keys()\
                else APIHelper.SKIP

        additional_properties = APIHelper.get_additional_properties(
            dictionary={k: v for k, v in dictionary.items()
                        if k not in cls._names.values()},
            unboxing_function=lambda value: value)

        # Return an object of this model
        return cls(id,
                   charge_id,
                   payment_status,
                   latest_deposit_date,
                   created_on,
                   latest_deposit_amount,
                   balance,
                   currency,
                   amount,
                   amount_difference,
                   token_metadata,
                   charge_metadata,
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
        _charge_id=(
            self.charge_id
            if hasattr(self, "charge_id")
            else None
        )
        _payment_status=(
            self.payment_status
            if hasattr(self, "payment_status")
            else None
        )
        _latest_deposit_date=(
            self.latest_deposit_date
            if hasattr(self, "latest_deposit_date")
            else None
        )
        _created_on=(
            self.created_on
            if hasattr(self, "created_on")
            else None
        )
        _latest_deposit_amount=(
            self.latest_deposit_amount
            if hasattr(self, "latest_deposit_amount")
            else None
        )
        _balance=(
            self.balance
            if hasattr(self, "balance")
            else None
        )
        _currency=(
            self.currency
            if hasattr(self, "currency")
            else None
        )
        _amount=(
            self.amount
            if hasattr(self, "amount")
            else None
        )
        _amount_difference=(
            self.amount_difference
            if hasattr(self, "amount_difference")
            else None
        )
        _token_metadata=(
            self.token_metadata
            if hasattr(self, "token_metadata")
            else None
        )
        _charge_metadata=(
            self.charge_metadata
            if hasattr(self, "charge_metadata")
            else None
        )
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"id={_id!r}, "
            f"charge_id={_charge_id!r}, "
            f"payment_status={_payment_status!r}, "
            f"latest_deposit_date={_latest_deposit_date!r}, "
            f"created_on={_created_on!r}, "
            f"latest_deposit_amount={_latest_deposit_amount!r}, "
            f"balance={_balance!r}, "
            f"currency={_currency!r}, "
            f"amount={_amount!r}, "
            f"amount_difference={_amount_difference!r}, "
            f"token_metadata={_token_metadata!r}, "
            f"charge_metadata={_charge_metadata!r}, "
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
        _charge_id=(
            self.charge_id
            if hasattr(self, "charge_id")
            else None
        )
        _payment_status=(
            self.payment_status
            if hasattr(self, "payment_status")
            else None
        )
        _latest_deposit_date=(
            self.latest_deposit_date
            if hasattr(self, "latest_deposit_date")
            else None
        )
        _created_on=(
            self.created_on
            if hasattr(self, "created_on")
            else None
        )
        _latest_deposit_amount=(
            self.latest_deposit_amount
            if hasattr(self, "latest_deposit_amount")
            else None
        )
        _balance=(
            self.balance
            if hasattr(self, "balance")
            else None
        )
        _currency=(
            self.currency
            if hasattr(self, "currency")
            else None
        )
        _amount=(
            self.amount
            if hasattr(self, "amount")
            else None
        )
        _amount_difference=(
            self.amount_difference
            if hasattr(self, "amount_difference")
            else None
        )
        _token_metadata=(
            self.token_metadata
            if hasattr(self, "token_metadata")
            else None
        )
        _charge_metadata=(
            self.charge_metadata
            if hasattr(self, "charge_metadata")
            else None
        )
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"id={_id!s}, "
            f"charge_id={_charge_id!s}, "
            f"payment_status={_payment_status!s}, "
            f"latest_deposit_date={_latest_deposit_date!s}, "
            f"created_on={_created_on!s}, "
            f"latest_deposit_amount={_latest_deposit_amount!s}, "
            f"balance={_balance!s}, "
            f"currency={_currency!s}, "
            f"amount={_amount!s}, "
            f"amount_difference={_amount_difference!s}, "
            f"token_metadata={_token_metadata!s}, "
            f"charge_metadata={_charge_metadata!s}, "
            f"additional_properties={_additional_properties!s}, "
            f")"
        )
