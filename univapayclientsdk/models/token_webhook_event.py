"""univapay_client_sdk.

This file was automatically generated for Univapay by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

# ruff: noqa: E501
from univapayclientsdk.api_helper import APIHelper
from univapayclientsdk.models.token_event import (
    TokenEvent,
)


class TokenWebhookEvent(object):
    """Implementation of the 'TokenWebhookEvent' model.

    Webhook envelope for transaction token lifecycle events. Fired as `token_created`
    when a token is created, `token_updated` on metadata changes,
    `token_three_d_s_updated` on 3-D Secure data changes, `token_cvv_auth_updated` on
    CVV authorization changes, `token_cvv_auth_check_updated` on CVV auth check
    changes, `token_replaced` when a token is replaced by a new one (e.g., after a
    card update), and `recurring_token_deleted` when a recurring token is deleted.
    The `data` field contains the full TransactionToken object at the time of the
    event.

    Attributes:
        id (uuid|str): Unique ID of this webhook delivery.
        event (TokenEvent): Event type discriminator — `token_created`,
            `token_updated`, `token_three_d_s_updated`, `token_cvv_auth_updated`,
            `token_cvv_auth_check_updated`, `token_replaced`, or
            `recurring_token_deleted`.
        data (CardTransactionToken | KonbiniTransactionToken | OnlineTransactionToken
            | BankTransferTransactionToken | PaidyTransactionToken |
            QrScanTransactionToken | QrMerchantTransactionToken | None): Stored
            transaction token resource. `payment_type` discriminates which variant
            applies — and therefore the concrete shape of `data` — per the mapping
            above.
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
        """Initialize a TokenWebhookEvent instance."""
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
        from univapayclientsdk.utilities.union_type_lookup import (
            UnionTypeLookUp,
        )

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
        data = APIHelper.deserialize_union_type(
            UnionTypeLookUp.get("TransactionToken2"),
            dictionary.get("data"),
            False)\
            if dictionary.get("data") is not None\
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
                        TokenEvent.validate(value)) \
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
                    TokenEvent.validate(value)) \
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
