"""univapay_client_sdk.

This file was automatically generated for Univapay by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

# ruff: noqa: E501
from univapayclientsdk.api_helper import APIHelper
from univapayclientsdk.models.merchant_webhook_configuration import (
    MerchantWebhookConfiguration,
)


class Merchant(object):
    """Implementation of the 'Merchant' model.

    Merchant resource returned by the backend `FullMerchantWithGroupRoles` formatter
    for merchant-authenticated callers.

    Attributes:
        id (uuid|str): Merchant identifier.
        verification_data_id (uuid|str): Verification data identifier associated with
            the merchant.
        name (str): Merchant display name.
        email (str): Primary merchant email address.
        notification_email (str): Merchant notification email address.
        finance_notification_email (str): Merchant finance notification email address.
        verified (bool): Whether the merchant has completed verification.
        configuration (MerchantWebhookConfiguration): Merchant configuration snapshot
            as serialized by the backend.
        created_on (datetime): Timestamp when the merchant was created.
        additional_properties (Dict[str, Any]): The additional properties for the
            model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "id": "id",
        "verification_data_id": "verification_data_id",
        "name": "name",
        "email": "email",
        "notification_email": "notification_email",
        "finance_notification_email": "finance_notification_email",
        "verified": "verified",
        "configuration": "configuration",
        "created_on": "created_on",
    }

    _optionals = [
        "id",
        "verification_data_id",
        "name",
        "email",
        "notification_email",
        "finance_notification_email",
        "verified",
        "configuration",
        "created_on",
    ]

    _nullables = [
        "verification_data_id",
        "notification_email",
        "finance_notification_email",
    ]

    def __init__(
        self,
        id=APIHelper.SKIP,
        verification_data_id=APIHelper.SKIP,
        name=APIHelper.SKIP,
        email=APIHelper.SKIP,
        notification_email=APIHelper.SKIP,
        finance_notification_email=APIHelper.SKIP,
        verified=APIHelper.SKIP,
        configuration=APIHelper.SKIP,
        created_on=APIHelper.SKIP,
        additional_properties=None):
        """Initialize a Merchant instance."""
        # Initialize members of the class
        if id is not APIHelper.SKIP:
            self.id = id
        if verification_data_id is not APIHelper.SKIP:
            self.verification_data_id = verification_data_id
        if name is not APIHelper.SKIP:
            self.name = name
        if email is not APIHelper.SKIP:
            self.email = email
        if notification_email is not APIHelper.SKIP:
            self.notification_email = notification_email
        if finance_notification_email is not APIHelper.SKIP:
            self.finance_notification_email = finance_notification_email
        if verified is not APIHelper.SKIP:
            self.verified = verified
        if configuration is not APIHelper.SKIP:
            self.configuration = configuration
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
        verification_data_id =\
            dictionary.get("verification_data_id")\
            if "verification_data_id" in dictionary.keys()\
                else APIHelper.SKIP
        name =\
            dictionary.get("name")\
            if dictionary.get("name")\
                else APIHelper.SKIP
        email =\
            dictionary.get("email")\
            if dictionary.get("email")\
                else APIHelper.SKIP
        notification_email =\
            dictionary.get("notification_email")\
            if "notification_email" in dictionary.keys()\
                else APIHelper.SKIP
        finance_notification_email =\
            dictionary.get("finance_notification_email")\
            if "finance_notification_email" in dictionary.keys()\
                else APIHelper.SKIP
        verified =\
            dictionary.get("verified")\
            if "verified" in dictionary.keys()\
                else APIHelper.SKIP
        configuration =\
            MerchantWebhookConfiguration.from_dictionary(
                dictionary.get("configuration"))\
                if "configuration" in dictionary.keys()\
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
                   verification_data_id,
                   name,
                   email,
                   notification_email,
                   finance_notification_email,
                   verified,
                   configuration,
                   created_on,
                   additional_properties)

    def __repr__(self):
        """Return a unambiguous string representation."""
        _id=(
            self.id
            if hasattr(self, "id")
            else None
        )
        _verification_data_id=(
            self.verification_data_id
            if hasattr(self, "verification_data_id")
            else None
        )
        _name=(
            self.name
            if hasattr(self, "name")
            else None
        )
        _email=(
            self.email
            if hasattr(self, "email")
            else None
        )
        _notification_email=(
            self.notification_email
            if hasattr(self, "notification_email")
            else None
        )
        _finance_notification_email=(
            self.finance_notification_email
            if hasattr(self, "finance_notification_email")
            else None
        )
        _verified=(
            self.verified
            if hasattr(self, "verified")
            else None
        )
        _configuration=(
            self.configuration
            if hasattr(self, "configuration")
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
            f"verification_data_id={_verification_data_id!r}, "
            f"name={_name!r}, "
            f"email={_email!r}, "
            f"notification_email={_notification_email!r}, "
            f"finance_notification_email={_finance_notification_email!r}, "
            f"verified={_verified!r}, "
            f"configuration={_configuration!r}, "
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
        _verification_data_id=(
            self.verification_data_id
            if hasattr(self, "verification_data_id")
            else None
        )
        _name=(
            self.name
            if hasattr(self, "name")
            else None
        )
        _email=(
            self.email
            if hasattr(self, "email")
            else None
        )
        _notification_email=(
            self.notification_email
            if hasattr(self, "notification_email")
            else None
        )
        _finance_notification_email=(
            self.finance_notification_email
            if hasattr(self, "finance_notification_email")
            else None
        )
        _verified=(
            self.verified
            if hasattr(self, "verified")
            else None
        )
        _configuration=(
            self.configuration
            if hasattr(self, "configuration")
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
            f"verification_data_id={_verification_data_id!s}, "
            f"name={_name!s}, "
            f"email={_email!s}, "
            f"notification_email={_notification_email!s}, "
            f"finance_notification_email={_finance_notification_email!s}, "
            f"verified={_verified!s}, "
            f"configuration={_configuration!s}, "
            f"created_on={_created_on!s}, "
            f"additional_properties={_additional_properties!s}, "
            f")"
        )
