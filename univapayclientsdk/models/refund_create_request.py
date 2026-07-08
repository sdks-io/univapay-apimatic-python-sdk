"""univapay_client_sdk.

This file was automatically generated for Univapay by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

# ruff: noqa: E501
from univapayclientsdk.api_helper import APIHelper
from univapayclientsdk.models.generic_metadata import (
    GenericMetadata,
)


class RefundCreateRequest(object):
    """Implementation of the 'RefundCreateRequest' model.

    Request body for creating a refund against a successful charge. Konbini and bank
    transfer charges cannot be refunded.

    Attributes:
        amount (int): Amount to refund in the smallest currency unit. Must be greater
            than 0 and not exceed the charged amount. Partial refunds are supported
            for most payment methods.
        currency (str): ISO-4217 currency code. Must exactly match the currency of
            the original charge.
        reason (RefundReasonRequest): The reason for the refund (merchant-settable
            values). `duplicate`: A duplicate charge was made. `fraud`: The charge is
            fraudulent. `customer_request`: The customer requested the refund.
        message (str): Optional free-text note about the reason for the refund.
        metadata (GenericMetadata): A free-form dictionary for custom metadata.
        additional_properties (Dict[str, Any]): The additional properties for the
            model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "amount": "amount",
        "currency": "currency",
        "reason": "reason",
        "message": "message",
        "metadata": "metadata",
    }

    _optionals = [
        "reason",
        "message",
        "metadata",
    ]

    def __init__(
        self,
        amount=None,
        currency=None,
        reason=APIHelper.SKIP,
        message=APIHelper.SKIP,
        metadata=APIHelper.SKIP,
        additional_properties=None):
        """Initialize a RefundCreateRequest instance."""
        # Initialize members of the class
        self.amount = amount
        self.currency = currency
        if reason is not APIHelper.SKIP:
            self.reason = reason
        if message is not APIHelper.SKIP:
            self.message = message
        if metadata is not APIHelper.SKIP:
            self.metadata = metadata

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
        amount =\
            dictionary.get("amount")\
            if dictionary.get("amount")\
                else None
        currency =\
            dictionary.get("currency")\
            if dictionary.get("currency")\
                else None
        reason =\
            dictionary.get("reason")\
            if dictionary.get("reason")\
                else APIHelper.SKIP
        message =\
            dictionary.get("message")\
            if dictionary.get("message")\
                else APIHelper.SKIP
        metadata =\
            GenericMetadata.from_dictionary(
                dictionary.get("metadata"))\
                if "metadata" in dictionary.keys()\
                else APIHelper.SKIP

        additional_properties = APIHelper.get_additional_properties(
            dictionary={k: v for k, v in dictionary.items()
                        if k not in cls._names.values()},
            unboxing_function=lambda value: value)

        # Return an object of this model
        return cls(amount,
                   currency,
                   reason,
                   message,
                   metadata,
                   additional_properties)

    def __repr__(self):
        """Return a unambiguous string representation."""
        _amount=self.amount
        _currency=self.currency
        _reason=(
            self.reason
            if hasattr(self, "reason")
            else None
        )
        _message=(
            self.message
            if hasattr(self, "message")
            else None
        )
        _metadata=(
            self.metadata
            if hasattr(self, "metadata")
            else None
        )
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"amount={_amount!r}, "
            f"currency={_currency!r}, "
            f"reason={_reason!r}, "
            f"message={_message!r}, "
            f"metadata={_metadata!r}, "
            f"additional_properties={_additional_properties!r}, "
            f")"
        )

    def __str__(self):
        """Return a human-readable string representation."""
        _amount=self.amount
        _currency=self.currency
        _reason=(
            self.reason
            if hasattr(self, "reason")
            else None
        )
        _message=(
            self.message
            if hasattr(self, "message")
            else None
        )
        _metadata=(
            self.metadata
            if hasattr(self, "metadata")
            else None
        )
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"amount={_amount!s}, "
            f"currency={_currency!s}, "
            f"reason={_reason!s}, "
            f"message={_message!s}, "
            f"metadata={_metadata!s}, "
            f"additional_properties={_additional_properties!s}, "
            f")"
        )
