"""univapay_client_sdk.

This file was automatically generated for Univapay by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

# ruff: noqa: E501
from univapayclientsdk.api_helper import APIHelper


class CustomsDeclarationWebhookOtherError(object):
    """Implementation of the 'CustomsDeclarationWebhookOtherError' model.

    Nested customs-processing error entry returned in `others`.

    Attributes:
        mtype (str): Backend other-error type.
        credentials_id (uuid|str): Gateway credentials involved in the error when
            applicable.
        message (List[str]): Additional reason values for `not_selected_reasons`.
        item_name (str): Related item name for `related_item`.
        additional_properties (Dict[str, Any]): The additional properties for the
            model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "mtype": "type",
        "credentials_id": "credentials_id",
        "message": "message",
        "item_name": "item_name",
    }

    _optionals = [
        "mtype",
        "credentials_id",
        "message",
        "item_name",
    ]

    _nullables = [
        "credentials_id",
        "message",
        "item_name",
    ]

    def __init__(
        self,
        mtype=APIHelper.SKIP,
        credentials_id=APIHelper.SKIP,
        message=APIHelper.SKIP,
        item_name=APIHelper.SKIP,
        additional_properties=None):
        """Initialize a CustomsDeclarationWebhookOtherError instance."""
        # Initialize members of the class
        if mtype is not APIHelper.SKIP:
            self.mtype = mtype
        if credentials_id is not APIHelper.SKIP:
            self.credentials_id = credentials_id
        if message is not APIHelper.SKIP:
            self.message = message
        if item_name is not APIHelper.SKIP:
            self.item_name = item_name

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
        mtype =\
            dictionary.get("type")\
            if dictionary.get("type")\
                else APIHelper.SKIP
        credentials_id =\
            dictionary.get("credentials_id")\
            if "credentials_id" in dictionary.keys()\
                else APIHelper.SKIP
        message =\
            dictionary.get("message")\
            if "message" in dictionary.keys()\
                else APIHelper.SKIP
        item_name =\
            dictionary.get("item_name")\
            if "item_name" in dictionary.keys()\
                else APIHelper.SKIP

        additional_properties = APIHelper.get_additional_properties(
            dictionary={k: v for k, v in dictionary.items()
                        if k not in cls._names.values()},
            unboxing_function=lambda value: value)

        # Return an object of this model
        return cls(mtype,
                   credentials_id,
                   message,
                   item_name,
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
            return True

        if not isinstance(dictionary, dict):
            return False

        return True

    def __repr__(self):
        """Return a unambiguous string representation."""
        _mtype=(
            self.mtype
            if hasattr(self, "mtype")
            else None
        )
        _credentials_id=(
            self.credentials_id
            if hasattr(self, "credentials_id")
            else None
        )
        _message=(
            self.message
            if hasattr(self, "message")
            else None
        )
        _item_name=(
            self.item_name
            if hasattr(self, "item_name")
            else None
        )
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"mtype={_mtype!r}, "
            f"credentials_id={_credentials_id!r}, "
            f"message={_message!r}, "
            f"item_name={_item_name!r}, "
            f"additional_properties={_additional_properties!r}, "
            f")"
        )

    def __str__(self):
        """Return a human-readable string representation."""
        _mtype=(
            self.mtype
            if hasattr(self, "mtype")
            else None
        )
        _credentials_id=(
            self.credentials_id
            if hasattr(self, "credentials_id")
            else None
        )
        _message=(
            self.message
            if hasattr(self, "message")
            else None
        )
        _item_name=(
            self.item_name
            if hasattr(self, "item_name")
            else None
        )
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"mtype={_mtype!s}, "
            f"credentials_id={_credentials_id!s}, "
            f"message={_message!s}, "
            f"item_name={_item_name!s}, "
            f"additional_properties={_additional_properties!s}, "
            f")"
        )
