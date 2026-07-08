"""univapay_client_sdk.

This file was automatically generated for Univapay by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

# ruff: noqa: E501
from univapayclientsdk.api_helper import APIHelper
from univapayclientsdk.models.transaction_token import (
    TransactionToken,
)


class TokenCvvAuthUpdatedWebhookCallback(object):
    """Implementation of the 'TokenCvvAuthUpdatedWebhookCallback' model.

    Webhook envelope for the token_cvv_auth_updated event.

    Attributes:
        id (uuid|str): Unique ID of this webhook delivery.
        event (str): Event type discriminator — always `token_cvv_auth_updated` for
            this callback.
        data (TransactionToken): Stored transaction token resource.
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
        created_on=None,
        data=APIHelper.SKIP,
        additional_properties=None):
        """Initialize a TokenCvvAuthUpdatedWebhookCallback instance."""
        # Initialize members of the class
        self.id = id
        self.event = "token_cvv_auth_updated"
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
        created_on = APIHelper.RFC3339DateTime.from_value(
            dictionary.get("created_on")).datetime\
            if dictionary.get("created_on") else None
        data =\
            TransactionToken.from_dictionary(
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
                value=dictionary.get("event"),
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
