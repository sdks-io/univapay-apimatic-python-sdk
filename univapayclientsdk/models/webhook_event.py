"""univapay_client_sdk.

This file was automatically generated for Univapay by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

# ruff: noqa: E501
from univapayclientsdk.api_helper import APIHelper


class WebhookEvent(object):
    """Implementation of the 'WebhookEvent' model.

    Represents a single delivery attempt of a webhook event, including the payload
    sent and the delivery outcome.

    Attributes:
        id (uuid|str): Unique identifier for the webhook event.
        webhook_id (uuid|str): ID of the parent webhook.
        event (WebhookTrigger): Event type that triggers a webhook notification.
        data (Any): Domain object payload for webhook deliveries. The actual
            structure depends on the event type — see each webhook callback schema
            for the specific payload shape.
        successful (bool): Whether the webhook delivery was acknowledged (HTTP 2xx).
        fired_on (datetime): Timestamp when the webhook was dispatched.
        error_message (str): Error message if delivery failed.
        created_on (datetime): Timestamp when the event was created.
        additional_properties (Dict[str, Any]): The additional properties for the
            model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "id": "id",
        "webhook_id": "webhook_id",
        "event": "event",
        "data": "data",
        "successful": "successful",
        "fired_on": "fired_on",
        "error_message": "error_message",
        "created_on": "created_on",
    }

    _optionals = [
        "id",
        "webhook_id",
        "event",
        "data",
        "successful",
        "fired_on",
        "error_message",
        "created_on",
    ]

    _nullables = [
        "error_message",
    ]

    def __init__(
        self,
        id=APIHelper.SKIP,
        webhook_id=APIHelper.SKIP,
        event=APIHelper.SKIP,
        data=APIHelper.SKIP,
        successful=APIHelper.SKIP,
        fired_on=APIHelper.SKIP,
        error_message=APIHelper.SKIP,
        created_on=APIHelper.SKIP,
        additional_properties=None):
        """Initialize a WebhookEvent instance."""
        # Initialize members of the class
        if id is not APIHelper.SKIP:
            self.id = id
        if webhook_id is not APIHelper.SKIP:
            self.webhook_id = webhook_id
        if event is not APIHelper.SKIP:
            self.event = event
        if data is not APIHelper.SKIP:
            self.data = data
        if successful is not APIHelper.SKIP:
            self.successful = successful
        if fired_on is not APIHelper.SKIP:
            self.fired_on =\
                 APIHelper.apply_datetime_converter(
                fired_on, APIHelper.RFC3339DateTime)\
                 if fired_on else None
        if error_message is not APIHelper.SKIP:
            self.error_message = error_message
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
        id =\
            dictionary.get("id")\
            if dictionary.get("id")\
                else APIHelper.SKIP
        webhook_id =\
            dictionary.get("webhook_id")\
            if dictionary.get("webhook_id")\
                else APIHelper.SKIP
        event =\
            dictionary.get("event")\
            if dictionary.get("event")\
                else APIHelper.SKIP
        data =\
            dictionary.get("data")\
            if dictionary.get("data")\
                else APIHelper.SKIP
        successful =\
            dictionary.get("successful")\
            if "successful" in dictionary.keys()\
                else APIHelper.SKIP
        fired_on = APIHelper.RFC3339DateTime.from_value(
            dictionary.get("fired_on")).datetime\
            if dictionary.get("fired_on") else APIHelper.SKIP
        error_message =\
            dictionary.get("error_message")\
            if "error_message" in dictionary.keys()\
                else APIHelper.SKIP
        created_on = APIHelper.RFC3339DateTime.from_value(
            dictionary.get("created_on")).datetime\
            if dictionary.get("created_on") else APIHelper.SKIP

        additional_properties = APIHelper.get_additional_properties(
            dictionary={k: v for k, v in dictionary.items()
                        if k not in cls._names.values()},
            unboxing_function=lambda value: value)

        # Return an object of this model
        return cls(id,
                   webhook_id,
                   event,
                   data,
                   successful,
                   fired_on,
                   error_message,
                   created_on,
                   additional_properties)

    def __repr__(self):
        """Return a unambiguous string representation."""
        _id=(
            self.id
            if hasattr(self, "id")
            else None
        )
        _webhook_id=(
            self.webhook_id
            if hasattr(self, "webhook_id")
            else None
        )
        _event=(
            self.event
            if hasattr(self, "event")
            else None
        )
        _data=(
            self.data
            if hasattr(self, "data")
            else None
        )
        _successful=(
            self.successful
            if hasattr(self, "successful")
            else None
        )
        _fired_on=(
            self.fired_on
            if hasattr(self, "fired_on")
            else None
        )
        _error_message=(
            self.error_message
            if hasattr(self, "error_message")
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
            f"id={_id!r}, "
            f"webhook_id={_webhook_id!r}, "
            f"event={_event!r}, "
            f"data={_data!r}, "
            f"successful={_successful!r}, "
            f"fired_on={_fired_on!r}, "
            f"error_message={_error_message!r}, "
            f"created_on={_created_on!r}, "
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
        _webhook_id=(
            self.webhook_id
            if hasattr(self, "webhook_id")
            else None
        )
        _event=(
            self.event
            if hasattr(self, "event")
            else None
        )
        _data=(
            self.data
            if hasattr(self, "data")
            else None
        )
        _successful=(
            self.successful
            if hasattr(self, "successful")
            else None
        )
        _fired_on=(
            self.fired_on
            if hasattr(self, "fired_on")
            else None
        )
        _error_message=(
            self.error_message
            if hasattr(self, "error_message")
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
            f"id={_id!s}, "
            f"webhook_id={_webhook_id!s}, "
            f"event={_event!s}, "
            f"data={_data!s}, "
            f"successful={_successful!s}, "
            f"fired_on={_fired_on!s}, "
            f"error_message={_error_message!s}, "
            f"created_on={_created_on!s}, "
            f"additional_properties={_additional_properties!s}, "
            f")"
        )
