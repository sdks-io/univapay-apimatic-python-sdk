"""univapay_client_sdk.

This file was automatically generated for Univapay by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

# ruff: noqa: E501
from univapayclientsdk.api_helper import APIHelper
from univapayclientsdk.models.merchant_webhook_configuration import (
    MerchantWebhookConfiguration,
)


class Store(object):
    """Implementation of the 'Store' model.

    Store resource returned by the backend `FullStore` formatter. It combines core
    store identity with the resolved configuration snapshot used for runtime policy
    evaluation.

    Attributes:
        id (uuid|str): Store identifier.
        name (str): Store display name.
        created_on (datetime): Timestamp when the store was created.
        configuration (MerchantWebhookConfiguration): Store-scoped configuration
            snapshot as serialized by the backend. It uses the same flattened
            serializer as merchant configuration, but omits `transfer_schedule`.
        additional_properties (Dict[str, Any]): The additional properties for the
            model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "id": "id",
        "name": "name",
        "created_on": "created_on",
        "configuration": "configuration",
    }

    _optionals = [
        "id",
        "name",
        "created_on",
        "configuration",
    ]

    def __init__(
        self,
        id=APIHelper.SKIP,
        name=APIHelper.SKIP,
        created_on=APIHelper.SKIP,
        configuration=APIHelper.SKIP,
        additional_properties=None):
        """Initialize a Store instance."""
        # Initialize members of the class
        if id is not APIHelper.SKIP:
            self.id = id
        if name is not APIHelper.SKIP:
            self.name = name
        if created_on is not APIHelper.SKIP:
            self.created_on =\
                 APIHelper.apply_datetime_converter(
                created_on, APIHelper.RFC3339DateTime)\
                 if created_on else None
        if configuration is not APIHelper.SKIP:
            self.configuration = configuration

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
        name =\
            dictionary.get("name")\
            if dictionary.get("name")\
                else APIHelper.SKIP
        created_on = APIHelper.RFC3339DateTime.from_value(
            dictionary.get("created_on")).datetime\
            if dictionary.get("created_on") else APIHelper.SKIP
        configuration =\
            MerchantWebhookConfiguration.from_dictionary(
                dictionary.get("configuration"))\
                if "configuration" in dictionary.keys()\
                else APIHelper.SKIP

        additional_properties = APIHelper.get_additional_properties(
            dictionary={k: v for k, v in dictionary.items()
                        if k not in cls._names.values()},
            unboxing_function=lambda value: value)

        # Return an object of this model
        return cls(id,
                   name,
                   created_on,
                   configuration,
                   additional_properties)

    def __repr__(self):
        """Return a unambiguous string representation."""
        _id=(
            self.id
            if hasattr(self, "id")
            else None
        )
        _name=(
            self.name
            if hasattr(self, "name")
            else None
        )
        _created_on=(
            self.created_on
            if hasattr(self, "created_on")
            else None
        )
        _configuration=(
            self.configuration
            if hasattr(self, "configuration")
            else None
        )
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"id={_id!r}, "
            f"name={_name!r}, "
            f"created_on={_created_on!r}, "
            f"configuration={_configuration!r}, "
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
        _name=(
            self.name
            if hasattr(self, "name")
            else None
        )
        _created_on=(
            self.created_on
            if hasattr(self, "created_on")
            else None
        )
        _configuration=(
            self.configuration
            if hasattr(self, "configuration")
            else None
        )
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"id={_id!s}, "
            f"name={_name!s}, "
            f"created_on={_created_on!s}, "
            f"configuration={_configuration!s}, "
            f"additional_properties={_additional_properties!s}, "
            f")"
        )
