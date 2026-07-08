"""univapay_client_sdk.

This file was automatically generated for Univapay by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

# ruff: noqa: E501
from univapayclientsdk.api_helper import APIHelper


class Webhook(object):
    """Implementation of the 'Webhook' model.

    Represents a webhook subscription. Webhooks send event notifications to a
    specified URL when triggered by payment events.

    Attributes:
        id (uuid|str): Unique identifier for the webhook.
        store_id (uuid|str): ID of the store this webhook belongs to (null for
            merchant-level webhooks).
        merchant_id (uuid|str): ID of the merchant this webhook belongs to.
        triggers (List[WebhookTrigger]): List of event types that trigger this
            webhook.
        url (str): The endpoint URL that receives webhook POST requests.
        auth_token (str): Optional bearer token included in the `Authorization`
            header of webhook requests. Used to authenticate the webhook receiver.
        active (bool): Whether this webhook is currently active and receiving events.
        is_integration (bool): Admin-only flag. Indicates this webhook is used for
            platform integration purposes. Not settable by merchants.
        created_on (datetime): Timestamp when the webhook was created.
        updated_on (datetime): Timestamp when the webhook was last updated.
        additional_properties (Dict[str, Any]): The additional properties for the
            model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "id": "id",
        "store_id": "store_id",
        "merchant_id": "merchant_id",
        "triggers": "triggers",
        "url": "url",
        "auth_token": "auth_token",
        "active": "active",
        "is_integration": "is_integration",
        "created_on": "created_on",
        "updated_on": "updated_on",
    }

    _optionals = [
        "id",
        "store_id",
        "merchant_id",
        "triggers",
        "url",
        "auth_token",
        "active",
        "is_integration",
        "created_on",
        "updated_on",
    ]

    _nullables = [
        "store_id",
        "merchant_id",
        "auth_token",
    ]

    def __init__(
        self,
        id=APIHelper.SKIP,
        store_id=APIHelper.SKIP,
        merchant_id=APIHelper.SKIP,
        triggers=APIHelper.SKIP,
        url=APIHelper.SKIP,
        auth_token=APIHelper.SKIP,
        active=APIHelper.SKIP,
        is_integration=APIHelper.SKIP,
        created_on=APIHelper.SKIP,
        updated_on=APIHelper.SKIP,
        additional_properties=None):
        """Initialize a Webhook instance."""
        # Initialize members of the class
        if id is not APIHelper.SKIP:
            self.id = id
        if store_id is not APIHelper.SKIP:
            self.store_id = store_id
        if merchant_id is not APIHelper.SKIP:
            self.merchant_id = merchant_id
        if triggers is not APIHelper.SKIP:
            self.triggers = triggers
        if url is not APIHelper.SKIP:
            self.url = url
        if auth_token is not APIHelper.SKIP:
            self.auth_token = auth_token
        if active is not APIHelper.SKIP:
            self.active = active
        if is_integration is not APIHelper.SKIP:
            self.is_integration = is_integration
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
            if "store_id" in dictionary.keys()\
                else APIHelper.SKIP
        merchant_id =\
            dictionary.get("merchant_id")\
            if "merchant_id" in dictionary.keys()\
                else APIHelper.SKIP
        triggers =\
            dictionary.get("triggers")\
            if dictionary.get("triggers")\
                else APIHelper.SKIP
        url =\
            dictionary.get("url")\
            if dictionary.get("url")\
                else APIHelper.SKIP
        auth_token =\
            dictionary.get("auth_token")\
            if "auth_token" in dictionary.keys()\
                else APIHelper.SKIP
        active =\
            dictionary.get("active")\
            if "active" in dictionary.keys()\
                else APIHelper.SKIP
        is_integration =\
            dictionary.get("is_integration")\
            if "is_integration" in dictionary.keys()\
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
                   merchant_id,
                   triggers,
                   url,
                   auth_token,
                   active,
                   is_integration,
                   created_on,
                   updated_on,
                   additional_properties)

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
        _merchant_id=(
            self.merchant_id
            if hasattr(self, "merchant_id")
            else None
        )
        _triggers=(
            self.triggers
            if hasattr(self, "triggers")
            else None
        )
        _url=(
            self.url
            if hasattr(self, "url")
            else None
        )
        _auth_token=(
            self.auth_token
            if hasattr(self, "auth_token")
            else None
        )
        _active=(
            self.active
            if hasattr(self, "active")
            else None
        )
        _is_integration=(
            self.is_integration
            if hasattr(self, "is_integration")
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
            f"merchant_id={_merchant_id!r}, "
            f"triggers={_triggers!r}, "
            f"url={_url!r}, "
            f"auth_token={_auth_token!r}, "
            f"active={_active!r}, "
            f"is_integration={_is_integration!r}, "
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
        _merchant_id=(
            self.merchant_id
            if hasattr(self, "merchant_id")
            else None
        )
        _triggers=(
            self.triggers
            if hasattr(self, "triggers")
            else None
        )
        _url=(
            self.url
            if hasattr(self, "url")
            else None
        )
        _auth_token=(
            self.auth_token
            if hasattr(self, "auth_token")
            else None
        )
        _active=(
            self.active
            if hasattr(self, "active")
            else None
        )
        _is_integration=(
            self.is_integration
            if hasattr(self, "is_integration")
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
            f"merchant_id={_merchant_id!s}, "
            f"triggers={_triggers!s}, "
            f"url={_url!s}, "
            f"auth_token={_auth_token!s}, "
            f"active={_active!s}, "
            f"is_integration={_is_integration!s}, "
            f"created_on={_created_on!s}, "
            f"updated_on={_updated_on!s}, "
            f"additional_properties={_additional_properties!s}, "
            f")"
        )
