"""univapay_client_sdk.

This file was automatically generated for Univapay by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

# ruff: noqa: E501
from univapayclientsdk.api_helper import APIHelper
from univapayclientsdk.models.charge import (
    Charge,
)
from univapayclientsdk.models.charge_event import (
    ChargeEvent,
)


class ChargeWebhookEvent(object):
    """Implementation of the 'ChargeWebhookEvent' model.

    Webhook envelope for charge lifecycle events. Fired as `charge_updated` whenever
    a charge transitions to a new status (e.g., `pending` → `awaiting`), and as
    `charge_finished` when a charge reaches a terminal status (`successful`,
    `failed`, `error`). The `data` field contains the full Charge object at the time
    of the event.

    Attributes:
        id (uuid|str): Unique ID of this webhook delivery.
        event (ChargeEvent): Event type discriminator — `charge_updated` or
            `charge_finished`.
        data (Charge): Charge resource returned by the payments API.
        created_on (datetime): Timestamp when the event was fired.
        additional_properties (Dict[str, Any]): The additional properties for the
            model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "id": "id",
        "event": "event",
        "created_on": "created_on",
        "data": "data",
    }

    _optionals = [
        "data",
    ]

    def __init__(
        self,
        id=None,
        event=None,
        created_on=None,
        data=APIHelper.SKIP,
        additional_properties=None):
        """Initialize a ChargeWebhookEvent instance."""
        # Initialize members of the class
        self.id = id
        self.event = event
        if data is not APIHelper.SKIP:
            self.data = data
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
        id =\
            dictionary.get("id")\
            if dictionary.get("id")\
                else None
        event =\
            dictionary.get("event")\
            if dictionary.get("event")\
                else None
        created_on = APIHelper.RFC3339DateTime.from_value(
            dictionary.get("created_on")).datetime\
            if dictionary.get("created_on") else None
        data =\
            Charge.from_dictionary(
                dictionary.get("data"))\
                if "data" in dictionary.keys()\
                else APIHelper.SKIP

        additional_properties = APIHelper.get_additional_properties(
            dictionary={k: v for k, v in dictionary.items()
                        if k not in cls._names.values()},
            unboxing_function=lambda value: value)

        # Return an object of this model
        return cls(id,
                   event,
                   created_on,
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
                    value=dictionary.event,
                    type_callable=lambda value:
                        ChargeEvent.validate(value)) \
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
                value=dictionary.get("event"),
                type_callable=lambda value:
                    ChargeEvent.validate(value)) \
            and APIHelper.is_valid_type(
                value=dictionary.get("created_on"),
                type_callable=lambda value:
                    isinstance(
                    value,
                    str,
            ))

    def __repr__(self):
        """Return a unambiguous string representation."""
        _id=self.id
        _event=self.event
        _data=(
            self.data
            if hasattr(self, "data")
            else None
        )
        _created_on=self.created_on
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"id={_id!r}, "
            f"event={_event!r}, "
            f"data={_data!r}, "
            f"created_on={_created_on!r}, "
            f"additional_properties={_additional_properties!r}, "
            f")"
        )

    def __str__(self):
        """Return a human-readable string representation."""
        _id=self.id
        _event=self.event
        _data=(
            self.data
            if hasattr(self, "data")
            else None
        )
        _created_on=self.created_on
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"id={_id!s}, "
            f"event={_event!s}, "
            f"data={_data!s}, "
            f"created_on={_created_on!s}, "
            f"additional_properties={_additional_properties!s}, "
            f")"
        )
