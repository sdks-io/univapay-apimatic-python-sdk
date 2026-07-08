"""univapay_client_sdk.

This file was automatically generated for Univapay by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

# ruff: noqa: E501
from univapayclientsdk.api_helper import APIHelper
from univapayclientsdk.models.transaction_token_list_item_user_data import (
    TransactionTokenListItemUserData,
)


class TransactionTokenListItem(object):
    """Implementation of the 'TransactionTokenListItem' model.

    Transaction token entry returned in list responses.

    Attributes:
        id (uuid|str): Unique identifier.
        store_id (uuid|str): Store identifier.
        merchant_name (str): Merchant display name.
        store_name (str): Store display name.
        email (str): Customer email address.
        payment_type (str): Payment method type.
        active (bool): Whether the resource is active.
        mode (str): Processing mode for the resource.
        mtype (str): Type of the resource.
        created_on (datetime): Timestamp when the resource was created.
        updated_on (datetime): Timestamp when the resource was last updated.
        user_data (TransactionTokenListItemUserData): Transaction Token List Item
            User Data schema.
        additional_properties (Dict[str, Any]): The additional properties for the
            model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "id": "id",
        "store_id": "store_id",
        "merchant_name": "merchant_name",
        "store_name": "store_name",
        "email": "email",
        "payment_type": "payment_type",
        "active": "active",
        "mode": "mode",
        "mtype": "type",
        "created_on": "created_on",
        "updated_on": "updated_on",
        "user_data": "user_data",
    }

    _optionals = [
        "id",
        "store_id",
        "merchant_name",
        "store_name",
        "email",
        "payment_type",
        "active",
        "mode",
        "mtype",
        "created_on",
        "updated_on",
        "user_data",
    ]

    def __init__(
        self,
        id=APIHelper.SKIP,
        store_id=APIHelper.SKIP,
        merchant_name=APIHelper.SKIP,
        store_name=APIHelper.SKIP,
        email=APIHelper.SKIP,
        payment_type=APIHelper.SKIP,
        active=APIHelper.SKIP,
        mode=APIHelper.SKIP,
        mtype=APIHelper.SKIP,
        created_on=APIHelper.SKIP,
        updated_on=APIHelper.SKIP,
        user_data=APIHelper.SKIP,
        additional_properties=None):
        """Initialize a TransactionTokenListItem instance."""
        # Initialize members of the class
        if id is not APIHelper.SKIP:
            self.id = id
        if store_id is not APIHelper.SKIP:
            self.store_id = store_id
        if merchant_name is not APIHelper.SKIP:
            self.merchant_name = merchant_name
        if store_name is not APIHelper.SKIP:
            self.store_name = store_name
        if email is not APIHelper.SKIP:
            self.email = email
        if payment_type is not APIHelper.SKIP:
            self.payment_type = payment_type
        if active is not APIHelper.SKIP:
            self.active = active
        if mode is not APIHelper.SKIP:
            self.mode = mode
        if mtype is not APIHelper.SKIP:
            self.mtype = mtype
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
        if user_data is not APIHelper.SKIP:
            self.user_data = user_data

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
            if dictionary.get("store_id")\
                else APIHelper.SKIP
        merchant_name =\
            dictionary.get("merchant_name")\
            if dictionary.get("merchant_name")\
                else APIHelper.SKIP
        store_name =\
            dictionary.get("store_name")\
            if dictionary.get("store_name")\
                else APIHelper.SKIP
        email =\
            dictionary.get("email")\
            if dictionary.get("email")\
                else APIHelper.SKIP
        payment_type =\
            dictionary.get("payment_type")\
            if dictionary.get("payment_type")\
                else APIHelper.SKIP
        active =\
            dictionary.get("active")\
            if "active" in dictionary.keys()\
                else APIHelper.SKIP
        mode =\
            dictionary.get("mode")\
            if dictionary.get("mode")\
                else APIHelper.SKIP
        mtype =\
            dictionary.get("type")\
            if dictionary.get("type")\
                else APIHelper.SKIP
        created_on = APIHelper.RFC3339DateTime.from_value(
            dictionary.get("created_on")).datetime\
            if dictionary.get("created_on") else APIHelper.SKIP
        updated_on = APIHelper.RFC3339DateTime.from_value(
            dictionary.get("updated_on")).datetime\
            if dictionary.get("updated_on") else APIHelper.SKIP
        user_data =\
            TransactionTokenListItemUserData.from_dictionary(
                dictionary.get("user_data"))\
                if "user_data" in dictionary.keys()\
                else APIHelper.SKIP

        additional_properties = APIHelper.get_additional_properties(
            dictionary={k: v for k, v in dictionary.items()
                        if k not in cls._names.values()},
            unboxing_function=lambda value: value)

        # Return an object of this model
        return cls(id,
                   store_id,
                   merchant_name,
                   store_name,
                   email,
                   payment_type,
                   active,
                   mode,
                   mtype,
                   created_on,
                   updated_on,
                   user_data,
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
        _merchant_name=(
            self.merchant_name
            if hasattr(self, "merchant_name")
            else None
        )
        _store_name=(
            self.store_name
            if hasattr(self, "store_name")
            else None
        )
        _email=(
            self.email
            if hasattr(self, "email")
            else None
        )
        _payment_type=(
            self.payment_type
            if hasattr(self, "payment_type")
            else None
        )
        _active=(
            self.active
            if hasattr(self, "active")
            else None
        )
        _mode=(
            self.mode
            if hasattr(self, "mode")
            else None
        )
        _mtype=(
            self.mtype
            if hasattr(self, "mtype")
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
        _user_data=(
            self.user_data
            if hasattr(self, "user_data")
            else None
        )
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"id={_id!r}, "
            f"store_id={_store_id!r}, "
            f"merchant_name={_merchant_name!r}, "
            f"store_name={_store_name!r}, "
            f"email={_email!r}, "
            f"payment_type={_payment_type!r}, "
            f"active={_active!r}, "
            f"mode={_mode!r}, "
            f"mtype={_mtype!r}, "
            f"created_on={_created_on!r}, "
            f"updated_on={_updated_on!r}, "
            f"user_data={_user_data!r}, "
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
        _merchant_name=(
            self.merchant_name
            if hasattr(self, "merchant_name")
            else None
        )
        _store_name=(
            self.store_name
            if hasattr(self, "store_name")
            else None
        )
        _email=(
            self.email
            if hasattr(self, "email")
            else None
        )
        _payment_type=(
            self.payment_type
            if hasattr(self, "payment_type")
            else None
        )
        _active=(
            self.active
            if hasattr(self, "active")
            else None
        )
        _mode=(
            self.mode
            if hasattr(self, "mode")
            else None
        )
        _mtype=(
            self.mtype
            if hasattr(self, "mtype")
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
        _user_data=(
            self.user_data
            if hasattr(self, "user_data")
            else None
        )
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"id={_id!s}, "
            f"store_id={_store_id!s}, "
            f"merchant_name={_merchant_name!s}, "
            f"store_name={_store_name!s}, "
            f"email={_email!s}, "
            f"payment_type={_payment_type!s}, "
            f"active={_active!s}, "
            f"mode={_mode!s}, "
            f"mtype={_mtype!s}, "
            f"created_on={_created_on!s}, "
            f"updated_on={_updated_on!s}, "
            f"user_data={_user_data!s}, "
            f"additional_properties={_additional_properties!s}, "
            f")"
        )
