"""univapay_client_sdk.

This file was automatically generated for Univapay by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

# ruff: noqa: E501
from univapayclientsdk.api_helper import APIHelper


class TransactionHistoryRefund(object):
    """Implementation of the 'TransactionHistoryRefund' model.

    A single refund issued against the charge this row describes.

    Attributes:
        refund_id (uuid|str): Unique identifier of the refund.
        amount (int): Refunded amount, in the currency's minor unit.
        currency (str): ISO-4217 currency code.
        amount_formatted (float): Refunded amount, formatted per the currency's
            display scale.
        status (TransactionHistoryRefundStatus): Status of a single refund entry.
        reason (TransactionHistoryRefundReason): Reason code for a refund.
        additional_properties (Dict[str, Any]): The additional properties for the
            model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "refund_id": "refund_id",
        "amount": "amount",
        "currency": "currency",
        "amount_formatted": "amount_formatted",
        "status": "status",
        "reason": "reason",
    }

    _optionals = [
        "refund_id",
        "amount",
        "currency",
        "amount_formatted",
        "status",
        "reason",
    ]

    def __init__(
        self,
        refund_id=APIHelper.SKIP,
        amount=APIHelper.SKIP,
        currency=APIHelper.SKIP,
        amount_formatted=APIHelper.SKIP,
        status=APIHelper.SKIP,
        reason=APIHelper.SKIP,
        additional_properties=None):
        """Initialize a TransactionHistoryRefund instance."""
        # Initialize members of the class
        if refund_id is not APIHelper.SKIP:
            self.refund_id = refund_id
        if amount is not APIHelper.SKIP:
            self.amount = amount
        if currency is not APIHelper.SKIP:
            self.currency = currency
        if amount_formatted is not APIHelper.SKIP:
            self.amount_formatted = amount_formatted
        if status is not APIHelper.SKIP:
            self.status = status
        if reason is not APIHelper.SKIP:
            self.reason = reason

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
        refund_id =\
            dictionary.get("refund_id")\
            if dictionary.get("refund_id")\
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
        status =\
            dictionary.get("status")\
            if dictionary.get("status")\
                else APIHelper.SKIP
        reason =\
            dictionary.get("reason")\
            if dictionary.get("reason")\
                else APIHelper.SKIP

        additional_properties = APIHelper.get_additional_properties(
            dictionary={k: v for k, v in dictionary.items()
                        if k not in cls._names.values()},
            unboxing_function=lambda value: value)

        # Return an object of this model
        return cls(refund_id,
                   amount,
                   currency,
                   amount_formatted,
                   status,
                   reason,
                   additional_properties)

    def __repr__(self):
        """Return a unambiguous string representation."""
        _refund_id=(
            self.refund_id
            if hasattr(self, "refund_id")
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
        _status=(
            self.status
            if hasattr(self, "status")
            else None
        )
        _reason=(
            self.reason
            if hasattr(self, "reason")
            else None
        )
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"refund_id={_refund_id!r}, "
            f"amount={_amount!r}, "
            f"currency={_currency!r}, "
            f"amount_formatted={_amount_formatted!r}, "
            f"status={_status!r}, "
            f"reason={_reason!r}, "
            f"additional_properties={_additional_properties!r}, "
            f")"
        )

    def __str__(self):
        """Return a human-readable string representation."""
        _refund_id=(
            self.refund_id
            if hasattr(self, "refund_id")
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
        _status=(
            self.status
            if hasattr(self, "status")
            else None
        )
        _reason=(
            self.reason
            if hasattr(self, "reason")
            else None
        )
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"refund_id={_refund_id!s}, "
            f"amount={_amount!s}, "
            f"currency={_currency!s}, "
            f"amount_formatted={_amount_formatted!s}, "
            f"status={_status!s}, "
            f"reason={_reason!s}, "
            f"additional_properties={_additional_properties!s}, "
            f")"
        )
