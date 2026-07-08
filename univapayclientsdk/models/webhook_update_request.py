"""univapay_client_sdk.

This file was automatically generated for Univapay by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

# ruff: noqa: E501
from univapayclientsdk.api_helper import APIHelper


class WebhookUpdateRequest(object):
    """Implementation of the 'WebhookUpdateRequest' model.

    Request body for updating a webhook. All fields are optional. Omitted fields are
    left unchanged.

    Attributes:
        triggers (List[WebhookTrigger]): Replace the trigger list. Must be non-empty
            if provided.
        url (str): Update the webhook endpoint URL.
        auth_token (str): Update or clear the auth token. Send `null` to remove.
        active (bool): Enable or disable the webhook.
        additional_properties (Dict[str, Any]): The additional properties for the
            model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "triggers": "triggers",
        "url": "url",
        "auth_token": "auth_token",
        "active": "active",
    }

    _optionals = [
        "triggers",
        "url",
        "auth_token",
        "active",
    ]

    _nullables = [
        "auth_token",
    ]

    def __init__(
        self,
        triggers=APIHelper.SKIP,
        url=APIHelper.SKIP,
        auth_token=APIHelper.SKIP,
        active=APIHelper.SKIP,
        additional_properties=None):
        """Initialize a WebhookUpdateRequest instance."""
        # Initialize members of the class
        if triggers is not APIHelper.SKIP:
            self.triggers = triggers
        if url is not APIHelper.SKIP:
            self.url = url
        if auth_token is not APIHelper.SKIP:
            self.auth_token = auth_token
        if active is not APIHelper.SKIP:
            self.active = active

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

        additional_properties = APIHelper.get_additional_properties(
            dictionary={k: v for k, v in dictionary.items()
                        if k not in cls._names.values()},
            unboxing_function=lambda value: value)

        # Return an object of this model
        return cls(triggers,
                   url,
                   auth_token,
                   active,
                   additional_properties)

    def __repr__(self):
        """Return a unambiguous string representation."""
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
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"triggers={_triggers!r}, "
            f"url={_url!r}, "
            f"auth_token={_auth_token!r}, "
            f"active={_active!r}, "
            f"additional_properties={_additional_properties!r}, "
            f")"
        )

    def __str__(self):
        """Return a human-readable string representation."""
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
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"triggers={_triggers!s}, "
            f"url={_url!s}, "
            f"auth_token={_auth_token!s}, "
            f"active={_active!s}, "
            f"additional_properties={_additional_properties!s}, "
            f")"
        )
