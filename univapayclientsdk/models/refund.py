"""univapay_client_sdk.

This file was automatically generated for Univapay by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

# ruff: noqa: E501
from univapayclientsdk.api_helper import APIHelper
from univapayclientsdk.models.generic_metadata import (
    GenericMetadata,
)
from univapayclientsdk.models.payment_error import (
    PaymentError,
)


class Refund(object):
    """Implementation of the 'Refund' model.

    Represents a refund issued against a charge.

    Attributes:
        id (uuid|str): Unique identifier.
        store_id (uuid|str): Store identifier.
        charge_id (uuid|str): Charge identifier.
        status (RefundStatus): Current status of the refund. `pending`: The refund
            has been created and is being processed. `successful`: The refund was
            processed successfully. `failed`: The refund was rejected by the gateway.
            `error`: An unexpected error occurred during processing.
        amount (int): Refund amount in the smallest currency unit (e.g., cents for
            USD, yen for JPY).
        currency (str): ISO-4217 currency code. Must match the charged currency.
        amount_formatted (float): Refund amount formatted for display.
        reason (RefundReasonResponse): Refund reason returned by the API, or `null`
            when unset.
        message (str): Optional free-text note about the refund.
        error (PaymentError): Payment error details, or null if successful.
        metadata (GenericMetadata): A free-form dictionary for custom metadata.
        mode (ChargeMode): Charge Mode schema.
        created_on (datetime): Timestamp when the resource was created.
        updated_on (datetime): Timestamp when the resource was last updated.
        additional_properties (Dict[str, Any]): The additional properties for the
            model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "id": "id",
        "store_id": "store_id",
        "charge_id": "charge_id",
        "status": "status",
        "amount": "amount",
        "currency": "currency",
        "amount_formatted": "amount_formatted",
        "reason": "reason",
        "message": "message",
        "error": "error",
        "metadata": "metadata",
        "mode": "mode",
        "created_on": "created_on",
        "updated_on": "updated_on",
    }

    _optionals = [
        "id",
        "store_id",
        "charge_id",
        "status",
        "amount",
        "currency",
        "amount_formatted",
        "reason",
        "message",
        "error",
        "metadata",
        "mode",
        "created_on",
        "updated_on",
    ]

    _nullables = [
        "reason",
        "message",
        "error",
    ]

    def __init__(
        self,
        id=APIHelper.SKIP,
        store_id=APIHelper.SKIP,
        charge_id=APIHelper.SKIP,
        status=APIHelper.SKIP,
        amount=APIHelper.SKIP,
        currency=APIHelper.SKIP,
        amount_formatted=APIHelper.SKIP,
        reason=APIHelper.SKIP,
        message=APIHelper.SKIP,
        error=APIHelper.SKIP,
        metadata=APIHelper.SKIP,
        mode=APIHelper.SKIP,
        created_on=APIHelper.SKIP,
        updated_on=APIHelper.SKIP,
        additional_properties=None):
        """Initialize a Refund instance."""
        # Initialize members of the class
        if id is not APIHelper.SKIP:
            self.id = id
        if store_id is not APIHelper.SKIP:
            self.store_id = store_id
        if charge_id is not APIHelper.SKIP:
            self.charge_id = charge_id
        if status is not APIHelper.SKIP:
            self.status = status
        if amount is not APIHelper.SKIP:
            self.amount = amount
        if currency is not APIHelper.SKIP:
            self.currency = currency
        if amount_formatted is not APIHelper.SKIP:
            self.amount_formatted = amount_formatted
        if reason is not APIHelper.SKIP:
            self.reason = reason
        if message is not APIHelper.SKIP:
            self.message = message
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
        store_id =\
            dictionary.get("store_id")\
            if dictionary.get("store_id")\
                else APIHelper.SKIP
        charge_id =\
            dictionary.get("charge_id")\
            if dictionary.get("charge_id")\
                else APIHelper.SKIP
        status =\
            dictionary.get("status")\
            if dictionary.get("status")\
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
        reason =\
            dictionary.get("reason")\
            if "reason" in dictionary.keys()\
                else APIHelper.SKIP
        message =\
            dictionary.get("message")\
            if "message" in dictionary.keys()\
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
        updated_on = APIHelper.RFC3339DateTime.from_value(
            dictionary.get("updated_on")).datetime\
            if dictionary.get("updated_on") else APIHelper.SKIP

        additional_properties = APIHelper.get_additional_properties(
            dictionary={k: v for k, v in dictionary.items()
                        if k not in cls._names.values()},
            unboxing_function=lambda value: value)

        # Return an object of this model
        return cls(id,
                   store_id,
                   charge_id,
                   status,
                   amount,
                   currency,
                   amount_formatted,
                   reason,
                   message,
                   error,
                   metadata,
                   mode,
                   created_on,
                   updated_on,
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
        _charge_id=(
            self.charge_id
            if hasattr(self, "charge_id")
            else None
        )
        _status=(
            self.status
            if hasattr(self, "status")
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
        _updated_on=(
            self.updated_on
            if hasattr(self, "updated_on")
            else None
        )
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"id={_id!r}, "
            f"store_id={_store_id!r}, "
            f"charge_id={_charge_id!r}, "
            f"status={_status!r}, "
            f"amount={_amount!r}, "
            f"currency={_currency!r}, "
            f"amount_formatted={_amount_formatted!r}, "
            f"reason={_reason!r}, "
            f"message={_message!r}, "
            f"error={_error!r}, "
            f"metadata={_metadata!r}, "
            f"mode={_mode!r}, "
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
        _store_id=(
            self.store_id
            if hasattr(self, "store_id")
            else None
        )
        _charge_id=(
            self.charge_id
            if hasattr(self, "charge_id")
            else None
        )
        _status=(
            self.status
            if hasattr(self, "status")
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
        _updated_on=(
            self.updated_on
            if hasattr(self, "updated_on")
            else None
        )
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"id={_id!s}, "
            f"store_id={_store_id!s}, "
            f"charge_id={_charge_id!s}, "
            f"status={_status!s}, "
            f"amount={_amount!s}, "
            f"currency={_currency!s}, "
            f"amount_formatted={_amount_formatted!s}, "
            f"reason={_reason!s}, "
            f"message={_message!s}, "
            f"error={_error!s}, "
            f"metadata={_metadata!s}, "
            f"mode={_mode!s}, "
            f"created_on={_created_on!s}, "
            f"updated_on={_updated_on!s}, "
            f"additional_properties={_additional_properties!s}, "
            f")"
        )
