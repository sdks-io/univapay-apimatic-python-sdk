"""univapay_client_sdk.

This file was automatically generated for Univapay by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

# ruff: noqa: E501
from univapayclientsdk.api_helper import APIHelper


class WebhookCreateRequest(object):
    """Implementation of the 'WebhookCreateRequest' model.

    Request body to create a new store-level webhook subscription.

    Attributes:
        triggers (List[WebhookTrigger]): List of event types that trigger this
            webhook. Must be non-empty and contain only events valid for the store
            level.
        url (str): The URL to POST webhook payloads to.
        auth_token (str): Optional bearer token sent in the `Authorization` header of
            webhook requests.
        additional_properties (Dict[str, Any]): The additional properties for the
            model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "triggers": "triggers",
        "url": "url",
        "auth_token": "auth_token",
    }

    _optionals = [
        "auth_token",
    ]

    _nullables = [
        "auth_token",
    ]

    def __init__(
        self,
        triggers=None,
        url=None,
        auth_token=APIHelper.SKIP,
        additional_properties=None):
        """Initialize a WebhookCreateRequest instance."""
        # Initialize members of the class
        self.triggers = triggers
        self.url = url
        if auth_token is not APIHelper.SKIP:
            self.auth_token = auth_token

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
                else None
        url =\
            dictionary.get("url")\
            if dictionary.get("url")\
                else None
        auth_token =\
            dictionary.get("auth_token")\
            if "auth_token" in dictionary.keys()\
                else APIHelper.SKIP

        additional_properties = APIHelper.get_additional_properties(
            dictionary={k: v for k, v in dictionary.items()
                        if k not in cls._names.values()},
            unboxing_function=lambda value: value)

        # Return an object of this model
        return cls(triggers,
                   url,
                   auth_token,
                   additional_properties)

    def __repr__(self):
        """Return a unambiguous string representation."""
        _triggers=self.triggers
        _url=self.url
        _auth_token=(
            self.auth_token
            if hasattr(self, "auth_token")
            else None
        )
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"triggers={_triggers!r}, "
            f"url={_url!r}, "
            f"auth_token={_auth_token!r}, "
            f"additional_properties={_additional_properties!r}, "
            f")"
        )

    def __str__(self):
        """Return a human-readable string representation."""
        _triggers=self.triggers
        _url=self.url
        _auth_token=(
            self.auth_token
            if hasattr(self, "auth_token")
            else None
        )
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"triggers={_triggers!s}, "
            f"url={_url!s}, "
            f"auth_token={_auth_token!s}, "
            f"additional_properties={_additional_properties!s}, "
            f")"
        )
