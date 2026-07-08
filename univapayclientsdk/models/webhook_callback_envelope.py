"""univapay_client_sdk.

This file was automatically generated for Univapay by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

# ruff: noqa: E501
from univapayclientsdk.api_helper import APIHelper


class WebhookCallbackEnvelope(object):
    """Implementation of the 'WebhookCallbackEnvelope' model.

    Common wrapper POSTed to your webhook URL for every event. The `data` field
    contains the domain object relevant to the event type.

    Attributes:
        id (uuid|str): Unique ID of this webhook delivery.
        event (WebhookTrigger): Event type that triggers a webhook notification.
        created_on (datetime): Timestamp when the event was fired.
        additional_properties (Dict[str, Any]): The additional properties for the
            model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "id": "id",
        "event": "event",
        "created_on": "created_on",
    }

    def __init__(
        self,
        id=None,
        event=None,
        created_on=None,
        additional_properties=None):
        """Initialize a WebhookCallbackEnvelope instance."""
        # Initialize members of the class
        self.id = id
        self.event = event
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

        additional_properties = APIHelper.get_additional_properties(
            dictionary={k: v for k, v in dictionary.items()
                        if k not in cls._names.values()},
            unboxing_function=lambda value: value)

        # Return an object of this model
        return cls(id,
                   event,
                   created_on,
                   additional_properties)

    def __repr__(self):
        """Return a unambiguous string representation."""
        _id=self.id
        _event=self.event
        _created_on=self.created_on
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"id={_id!r}, "
            f"event={_event!r}, "
            f"created_on={_created_on!r}, "
            f"additional_properties={_additional_properties!r}, "
            f")"
        )

    def __str__(self):
        """Return a human-readable string representation."""
        _id=self.id
        _event=self.event
        _created_on=self.created_on
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"id={_id!s}, "
            f"event={_event!s}, "
            f"created_on={_created_on!s}, "
            f"additional_properties={_additional_properties!s}, "
            f")"
        )
