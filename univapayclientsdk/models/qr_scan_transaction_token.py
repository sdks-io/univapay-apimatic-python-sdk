"""univapay_client_sdk.

This file was automatically generated for Univapay by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

# ruff: noqa: E501
from univapayclientsdk.api_helper import APIHelper
from univapayclientsdk.models.token_response_qr_scan_data import (
    TokenResponseQrScanData,
)


class QrScanTransactionToken(object):
    """Implementation of the 'QrScanTransactionToken' model.

    Stored transaction token resource for a `qr_scan` (QR Customer-Presented Mode)
    payment type.

    Attributes:
        id (uuid|str): Unique identifier.
        store_id (uuid|str): Store identifier.
        email (str): Customer email address.
        active (bool): Whether the resource is active.
        mode (TransactionTokenMode): Transaction Token Mode schema.
        mtype (TransactionTokenType): Transaction Token Type schema.
        usage_limit (str): Usage limit applied to the token.
        confirmed (bool): Whether the token has been confirmed.
        metadata (Dict[str, str | None | int | float | bool | List[str | None | int |
            float | bool]]): Arbitrary key-value metadata.
        created_on (datetime): Timestamp when the resource was created.
        updated_on (datetime): Timestamp when the resource was last updated.
        last_used_on (datetime): Timestamp when the token was last used.
        payment_type (str): Payment method type. Always `qr_scan` for this variant.
        data (TokenResponseQrScanData): Token Response Qr Scan Data schema.
        additional_properties (Dict[str, Any]): The additional properties for the
            model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "payment_type": "payment_type",
        "data": "data",
        "id": "id",
        "store_id": "store_id",
        "email": "email",
        "active": "active",
        "mode": "mode",
        "mtype": "type",
        "usage_limit": "usage_limit",
        "confirmed": "confirmed",
        "metadata": "metadata",
        "created_on": "created_on",
        "updated_on": "updated_on",
        "last_used_on": "last_used_on",
    }

    _optionals = [
        "id",
        "store_id",
        "email",
        "active",
        "mode",
        "mtype",
        "usage_limit",
        "confirmed",
        "metadata",
        "created_on",
        "updated_on",
        "last_used_on",
    ]

    _nullables = [
        "email",
        "usage_limit",
        "confirmed",
        "last_used_on",
    ]

    def __init__(
        self,
        data=None,
        id=APIHelper.SKIP,
        store_id=APIHelper.SKIP,
        email=APIHelper.SKIP,
        active=APIHelper.SKIP,
        mode=APIHelper.SKIP,
        mtype=APIHelper.SKIP,
        usage_limit=APIHelper.SKIP,
        confirmed=APIHelper.SKIP,
        metadata=APIHelper.SKIP,
        created_on=APIHelper.SKIP,
        updated_on=APIHelper.SKIP,
        last_used_on=APIHelper.SKIP,
        additional_properties=None):
        """Initialize a QrScanTransactionToken instance."""
        # Initialize members of the class
        if id is not APIHelper.SKIP:
            self.id = id
        if store_id is not APIHelper.SKIP:
            self.store_id = store_id
        if email is not APIHelper.SKIP:
            self.email = email
        if active is not APIHelper.SKIP:
            self.active = active
        if mode is not APIHelper.SKIP:
            self.mode = mode
        if mtype is not APIHelper.SKIP:
            self.mtype = mtype
        if usage_limit is not APIHelper.SKIP:
            self.usage_limit = usage_limit
        if confirmed is not APIHelper.SKIP:
            self.confirmed = confirmed
        if metadata is not APIHelper.SKIP:
            self.metadata = metadata
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
        if last_used_on is not APIHelper.SKIP:
            self.last_used_on =\
                 APIHelper.apply_datetime_converter(
                last_used_on, APIHelper.RFC3339DateTime)\
                 if last_used_on else None
        self.payment_type = "qr_scan"
        self.data = data

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
        data =\
            TokenResponseQrScanData.from_dictionary(
                dictionary.get("data"))\
                if dictionary.get("data") else None
        id =\
            dictionary.get("id")\
            if dictionary.get("id")\
                else APIHelper.SKIP
        store_id =\
            dictionary.get("store_id")\
            if dictionary.get("store_id")\
                else APIHelper.SKIP
        email =\
            dictionary.get("email")\
            if "email" in dictionary.keys()\
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
        usage_limit =\
            dictionary.get("usage_limit")\
            if "usage_limit" in dictionary.keys()\
                else APIHelper.SKIP
        confirmed =\
            dictionary.get("confirmed")\
            if "confirmed" in dictionary.keys()\
                else APIHelper.SKIP
        metadata = APIHelper.deserialize_union_type(
            UnionTypeLookUp.get("TransactionTokenMetadataAdditionalProperties"),
            dictionary.get("metadata"),
            False)\
            if dictionary.get("metadata") is not None\
            else APIHelper.SKIP
        created_on = APIHelper.RFC3339DateTime.from_value(
            dictionary.get("created_on")).datetime\
            if dictionary.get("created_on") else APIHelper.SKIP
        updated_on = APIHelper.RFC3339DateTime.from_value(
            dictionary.get("updated_on")).datetime\
            if dictionary.get("updated_on") else APIHelper.SKIP
        if "last_used_on" in dictionary.keys():
            last_used_on = APIHelper.RFC3339DateTime.from_value(
                dictionary.get("last_used_on")).datetime\
                if dictionary.get("last_used_on") else None

        else:
            last_used_on = APIHelper.SKIP

        additional_properties = APIHelper.get_additional_properties(
            dictionary={k: v for k, v in dictionary.items()
                        if k not in cls._names.values()},
            unboxing_function=lambda value: value)

        # Return an object of this model
        return cls(data,
                   id,
                   store_id,
                   email,
                   active,
                   mode,
                   mtype,
                   usage_limit,
                   confirmed,
                   metadata,
                   created_on,
                   updated_on,
                   last_used_on,
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
                    value=dictionary.payment_type,
                    type_callable=lambda value:
                        isinstance(
                        value,
                        str,
                )) \
                and APIHelper.is_valid_type(
                    value=dictionary.data,
                    type_callable=lambda value:
                        TokenResponseQrScanData.validate(value),
                    is_model_dict=True)

        if not isinstance(dictionary, dict):
            return False

        return APIHelper.is_valid_type(
                value=dictionary.get("payment_type"),
                type_callable=lambda value:
                    isinstance(
                    value,
                    str,
            )) \
            and APIHelper.is_valid_type(
                value=dictionary.get("data"),
                type_callable=lambda value:
                    TokenResponseQrScanData.validate(value),
                is_model_dict=True)

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
        _email=(
            self.email
            if hasattr(self, "email")
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
        _usage_limit=(
            self.usage_limit
            if hasattr(self, "usage_limit")
            else None
        )
        _confirmed=(
            self.confirmed
            if hasattr(self, "confirmed")
            else None
        )
        _metadata=(
            self.metadata
            if hasattr(self, "metadata")
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
        _last_used_on=(
            self.last_used_on
            if hasattr(self, "last_used_on")
            else None
        )
        _payment_type=self.payment_type
        _data=self.data
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"id={_id!r}, "
            f"store_id={_store_id!r}, "
            f"email={_email!r}, "
            f"active={_active!r}, "
            f"mode={_mode!r}, "
            f"mtype={_mtype!r}, "
            f"usage_limit={_usage_limit!r}, "
            f"confirmed={_confirmed!r}, "
            f"metadata={_metadata!r}, "
            f"created_on={_created_on!r}, "
            f"updated_on={_updated_on!r}, "
            f"last_used_on={_last_used_on!r}, "
            f"payment_type={_payment_type!r}, "
            f"data={_data!r}, "
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
        _email=(
            self.email
            if hasattr(self, "email")
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
        _usage_limit=(
            self.usage_limit
            if hasattr(self, "usage_limit")
            else None
        )
        _confirmed=(
            self.confirmed
            if hasattr(self, "confirmed")
            else None
        )
        _metadata=(
            self.metadata
            if hasattr(self, "metadata")
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
        _last_used_on=(
            self.last_used_on
            if hasattr(self, "last_used_on")
            else None
        )
        _payment_type=self.payment_type
        _data=self.data
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"id={_id!s}, "
            f"store_id={_store_id!s}, "
            f"email={_email!s}, "
            f"active={_active!s}, "
            f"mode={_mode!s}, "
            f"mtype={_mtype!s}, "
            f"usage_limit={_usage_limit!s}, "
            f"confirmed={_confirmed!s}, "
            f"metadata={_metadata!s}, "
            f"created_on={_created_on!s}, "
            f"updated_on={_updated_on!s}, "
            f"last_used_on={_last_used_on!s}, "
            f"payment_type={_payment_type!s}, "
            f"data={_data!s}, "
            f"additional_properties={_additional_properties!s}, "
            f")"
        )
