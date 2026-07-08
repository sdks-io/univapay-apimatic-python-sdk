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


class Cancel(object):
    """Implementation of the 'Cancel' model.

    Represents a cancellation request for a charge.

    Attributes:
        id (uuid|str): Unique identifier for the cancel.
        charge_id (uuid|str): ID of the charge this cancel is associated with.
        store_id (uuid|str): ID of the store.
        status (CancelStatus): Current status of the cancel operation.
        error (PaymentError): Payment error details, or null if successful.
        metadata (GenericMetadata): A free-form dictionary for custom metadata.
        mode (ChargeMode): Charge Mode schema.
        created_on (datetime): Timestamp when the cancel was created.
        updated_on (datetime): Timestamp when the cancel was last updated.
        additional_properties (Dict[str, Any]): The additional properties for the
            model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "id": "id",
        "charge_id": "charge_id",
        "store_id": "store_id",
        "status": "status",
        "error": "error",
        "metadata": "metadata",
        "mode": "mode",
        "created_on": "created_on",
        "updated_on": "updated_on",
    }

    _optionals = [
        "id",
        "charge_id",
        "store_id",
        "status",
        "error",
        "metadata",
        "mode",
        "created_on",
        "updated_on",
    ]

    _nullables = [
        "error",
    ]

    def __init__(
        self,
        id=APIHelper.SKIP,
        charge_id=APIHelper.SKIP,
        store_id=APIHelper.SKIP,
        status=APIHelper.SKIP,
        error=APIHelper.SKIP,
        metadata=APIHelper.SKIP,
        mode=APIHelper.SKIP,
        created_on=APIHelper.SKIP,
        updated_on=APIHelper.SKIP,
        additional_properties=None):
        """Initialize a Cancel instance."""
        # Initialize members of the class
        if id is not APIHelper.SKIP:
            self.id = id
        if charge_id is not APIHelper.SKIP:
            self.charge_id = charge_id
        if store_id is not APIHelper.SKIP:
            self.store_id = store_id
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
        charge_id =\
            dictionary.get("charge_id")\
            if dictionary.get("charge_id")\
                else APIHelper.SKIP
        store_id =\
            dictionary.get("store_id")\
            if dictionary.get("store_id")\
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
        updated_on = APIHelper.RFC3339DateTime.from_value(
            dictionary.get("updated_on")).datetime\
            if dictionary.get("updated_on") else APIHelper.SKIP

        additional_properties = APIHelper.get_additional_properties(
            dictionary={k: v for k, v in dictionary.items()
                        if k not in cls._names.values()},
            unboxing_function=lambda value: value)

        # Return an object of this model
        return cls(id,
                   charge_id,
                   store_id,
                   status,
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
        _charge_id=(
            self.charge_id
            if hasattr(self, "charge_id")
            else None
        )
        _store_id=(
            self.store_id
            if hasattr(self, "store_id")
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
        _updated_on=(
            self.updated_on
            if hasattr(self, "updated_on")
            else None
        )
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"id={_id!r}, "
            f"charge_id={_charge_id!r}, "
            f"store_id={_store_id!r}, "
            f"status={_status!r}, "
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
        _charge_id=(
            self.charge_id
            if hasattr(self, "charge_id")
            else None
        )
        _store_id=(
            self.store_id
            if hasattr(self, "store_id")
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
        _updated_on=(
            self.updated_on
            if hasattr(self, "updated_on")
            else None
        )
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"id={_id!s}, "
            f"charge_id={_charge_id!s}, "
            f"store_id={_store_id!s}, "
            f"status={_status!s}, "
            f"error={_error!s}, "
            f"metadata={_metadata!s}, "
            f"mode={_mode!s}, "
            f"created_on={_created_on!s}, "
            f"updated_on={_updated_on!s}, "
            f"additional_properties={_additional_properties!s}, "
            f")"
        )
