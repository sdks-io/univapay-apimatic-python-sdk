"""univapay_client_sdk.

This file was automatically generated for Univapay by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

# ruff: noqa: E501
from univapayclientsdk.api_helper import APIHelper
from univapayclientsdk.models.bank_transfer_status_data import (
    BankTransferStatusData,
)


class BankTransferStatusWebhookCallback(object):
    """Implementation of the 'BankTransferStatusWebhookCallback' model.

    Webhook envelope whose `data` payload is a BankTransferStatusData resource.

    Attributes:
        event (BankTransferEvent): Event type discriminator — always
            `bank_transfer_status_updated` for this callback.
        id (uuid|str): Unique ID of this webhook delivery.
        created_on (datetime): Timestamp when the event was fired.
        data (BankTransferStatusData): Data payload for
            `bank_transfer_status_updated` webhook events. Contains the bank transfer
            extension fields inlined alongside amount and metadata.
        additional_properties (Dict[str, Any]): The additional properties for the
            model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "id": "id",
        "created_on": "created_on",
        "event": "event",
        "data": "data",
    }

    _optionals = [
        "event",
        "data",
    ]

    def __init__(
        self,
        id=None,
        created_on=None,
        event=APIHelper.SKIP,
        data=APIHelper.SKIP,
        additional_properties=None):
        """Initialize a BankTransferStatusWebhookCallback instance."""
        # Initialize members of the class
        if event is not APIHelper.SKIP:
            self.event = event
        self.id = id
        self.created_on =\
             APIHelper.apply_datetime_converter(
            created_on, APIHelper.RFC3339DateTime)\
             if created_on else None
        if data is not APIHelper.SKIP:
            self.data = data

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
                else None
        created_on = APIHelper.RFC3339DateTime.from_value(
            dictionary.get("created_on")).datetime\
            if dictionary.get("created_on") else None
        event =\
            dictionary.get("event")\
            if dictionary.get("event")\
                else APIHelper.SKIP
        data =\
            BankTransferStatusData.from_dictionary(
                dictionary.get("data"))\
                if "data" in dictionary.keys()\
                else APIHelper.SKIP

        additional_properties = APIHelper.get_additional_properties(
            dictionary={k: v for k, v in dictionary.items()
                        if k not in cls._names.values()},
            unboxing_function=lambda value: value)

        # Return an object of this model
        return cls(id,
                   created_on,
                   event,
                   data,
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
            return APIHelper.is_valid_type(
                    value=dictionary.id,
                    type_callable=lambda value:
                        isinstance(
                        value,
                        str,
                )) \
                and APIHelper.is_valid_type(
                    value=dictionary.created_on,
                    type_callable=lambda value:
                        isinstance(
                        value,
                        APIHelper.RFC3339DateTime,
                ))

        if not isinstance(dictionary, dict):
            return False

        return APIHelper.is_valid_type(
                value=dictionary.get("id"),
                type_callable=lambda value:
                    isinstance(
                    value,
                    str,
            )) \
            and APIHelper.is_valid_type(
                value=dictionary.get("created_on"),
                type_callable=lambda value:
                    isinstance(
                    value,
                    str,
            ))

    def __repr__(self):
        """Return a unambiguous string representation."""
        _event=(
            self.event
            if hasattr(self, "event")
            else None
        )
        _id=self.id
        _created_on=self.created_on
        _data=(
            self.data
            if hasattr(self, "data")
            else None
        )
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"event={_event!r}, "
            f"id={_id!r}, "
            f"created_on={_created_on!r}, "
            f"data={_data!r}, "
            f"additional_properties={_additional_properties!r}, "
            f")"
        )

    def __str__(self):
        """Return a human-readable string representation."""
        _event=(
            self.event
            if hasattr(self, "event")
            else None
        )
        _id=self.id
        _created_on=self.created_on
        _data=(
            self.data
            if hasattr(self, "data")
            else None
        )
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"event={_event!s}, "
            f"id={_id!s}, "
            f"created_on={_created_on!s}, "
            f"data={_data!s}, "
            f"additional_properties={_additional_properties!s}, "
            f")"
        )
