"""univapay_client_sdk.

This file was automatically generated for Univapay by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

# ruff: noqa: E501
from univapayclientsdk.api_helper import APIHelper
from univapayclientsdk.models.customs_declaration_webhook_declaration import (
    CustomsDeclarationWebhookDeclaration,
)
from univapayclientsdk.models.customs_declaration_webhook_error import (
    CustomsDeclarationWebhookError,
)
from univapayclientsdk.models.customs_declaration_webhook_result import (
    CustomsDeclarationWebhookResult,
)


class CustomsDeclarationWebhookData(object):
    """Implementation of the 'CustomsDeclarationWebhookData' model.

    Customs declaration payload delivered in `customs_declaration_finished` webhooks.
    Platform-level deliveries may include `platform_id` and `updated_on`.

    Attributes:
        id (uuid|str): Customs declaration identifier.
        charge_id (uuid|str): Charge identifier associated with the declaration.
        merchant_id (uuid|str): Merchant identifier.
        store_id (uuid|str): Store identifier.
        platform_id (uuid|str): Platform identifier, included on platform-level
            deliveries.
        mode (str): Processing mode.
        gateway (str): Gateway that processed the declaration.
        declaration (CustomsDeclarationWebhookDeclaration): WeChat customs
            declaration payload returned by the backend formatter.
        declaration_result (CustomsDeclarationWebhookResult): Result payload returned
            by the customs declaration formatter.
        status (CustomsDeclarationWebhookStatus): Customs declaration status returned
            by the backend.
        error (CustomsDeclarationWebhookError): Error payload returned when customs
            declaration processing fails.
        created_on (datetime): Timestamp when the declaration was created.
        updated_on (datetime): Timestamp when the declaration was last updated,
            included on platform-level deliveries.
        additional_properties (Dict[str, Any]): The additional properties for the
            model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "id": "id",
        "charge_id": "charge_id",
        "merchant_id": "merchant_id",
        "store_id": "store_id",
        "platform_id": "platform_id",
        "mode": "mode",
        "gateway": "gateway",
        "declaration": "declaration",
        "declaration_result": "declaration_result",
        "status": "status",
        "error": "error",
        "created_on": "created_on",
        "updated_on": "updated_on",
    }

    _optionals = [
        "id",
        "charge_id",
        "merchant_id",
        "store_id",
        "platform_id",
        "mode",
        "gateway",
        "declaration",
        "declaration_result",
        "status",
        "error",
        "created_on",
        "updated_on",
    ]

    _nullables = [
        "platform_id",
        "declaration_result",
        "error",
        "updated_on",
    ]

    def __init__(
        self,
        id=APIHelper.SKIP,
        charge_id=APIHelper.SKIP,
        merchant_id=APIHelper.SKIP,
        store_id=APIHelper.SKIP,
        platform_id=APIHelper.SKIP,
        mode=APIHelper.SKIP,
        gateway=APIHelper.SKIP,
        declaration=APIHelper.SKIP,
        declaration_result=APIHelper.SKIP,
        status=APIHelper.SKIP,
        error=APIHelper.SKIP,
        created_on=APIHelper.SKIP,
        updated_on=APIHelper.SKIP,
        additional_properties=None):
        """Initialize a CustomsDeclarationWebhookData instance."""
        # Initialize members of the class
        if id is not APIHelper.SKIP:
            self.id = id
        if charge_id is not APIHelper.SKIP:
            self.charge_id = charge_id
        if merchant_id is not APIHelper.SKIP:
            self.merchant_id = merchant_id
        if store_id is not APIHelper.SKIP:
            self.store_id = store_id
        if platform_id is not APIHelper.SKIP:
            self.platform_id = platform_id
        if mode is not APIHelper.SKIP:
            self.mode = mode
        if gateway is not APIHelper.SKIP:
            self.gateway = gateway
        if declaration is not APIHelper.SKIP:
            self.declaration = declaration
        if declaration_result is not APIHelper.SKIP:
            self.declaration_result = declaration_result
        if status is not APIHelper.SKIP:
            self.status = status
        if error is not APIHelper.SKIP:
            self.error = error
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
        charge_id =\
            dictionary.get("charge_id")\
            if dictionary.get("charge_id")\
                else APIHelper.SKIP
        merchant_id =\
            dictionary.get("merchant_id")\
            if dictionary.get("merchant_id")\
                else APIHelper.SKIP
        store_id =\
            dictionary.get("store_id")\
            if dictionary.get("store_id")\
                else APIHelper.SKIP
        platform_id =\
            dictionary.get("platform_id")\
            if "platform_id" in dictionary.keys()\
                else APIHelper.SKIP
        mode =\
            dictionary.get("mode")\
            if dictionary.get("mode")\
                else APIHelper.SKIP
        gateway =\
            dictionary.get("gateway")\
            if dictionary.get("gateway")\
                else APIHelper.SKIP
        declaration =\
            CustomsDeclarationWebhookDeclaration.from_dictionary(
                dictionary.get("declaration"))\
                if "declaration" in dictionary.keys()\
                else APIHelper.SKIP
        if "declaration_result" in dictionary.keys():
            declaration_result =\
                CustomsDeclarationWebhookResult.from_dictionary(
                dictionary.get("declaration_result"))\
                if dictionary.get("declaration_result") else None
        else:
            declaration_result = APIHelper.SKIP
        status =\
            dictionary.get("status")\
            if dictionary.get("status")\
                else APIHelper.SKIP
        if "error" in dictionary.keys():
            error =\
                CustomsDeclarationWebhookError.from_dictionary(
                dictionary.get("error"))\
                if dictionary.get("error") else None
        else:
            error = APIHelper.SKIP
        created_on = APIHelper.RFC3339DateTime.from_value(
            dictionary.get("created_on")).datetime\
            if dictionary.get("created_on") else APIHelper.SKIP
        if "updated_on" in dictionary.keys():
            updated_on = APIHelper.RFC3339DateTime.from_value(
                dictionary.get("updated_on")).datetime\
                if dictionary.get("updated_on") else None

        else:
            updated_on = APIHelper.SKIP

        additional_properties = APIHelper.get_additional_properties(
            dictionary={k: v for k, v in dictionary.items()
                        if k not in cls._names.values()},
            unboxing_function=lambda value: value)

        # Return an object of this model
        return cls(id,
                   charge_id,
                   merchant_id,
                   store_id,
                   platform_id,
                   mode,
                   gateway,
                   declaration,
                   declaration_result,
                   status,
                   error,
                   created_on,
                   updated_on,
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
        _id=(
            self.id
            if hasattr(self, "id")
            else None
        )
        _charge_id=(
            self.charge_id
            if hasattr(self, "charge_id")
            else None
        )
        _merchant_id=(
            self.merchant_id
            if hasattr(self, "merchant_id")
            else None
        )
        _store_id=(
            self.store_id
            if hasattr(self, "store_id")
            else None
        )
        _platform_id=(
            self.platform_id
            if hasattr(self, "platform_id")
            else None
        )
        _mode=(
            self.mode
            if hasattr(self, "mode")
            else None
        )
        _gateway=(
            self.gateway
            if hasattr(self, "gateway")
            else None
        )
        _declaration=(
            self.declaration
            if hasattr(self, "declaration")
            else None
        )
        _declaration_result=(
            self.declaration_result
            if hasattr(self, "declaration_result")
            else None
        )
        _status=(
            self.status
            if hasattr(self, "status")
            else None
        )
        _error=(
            self.error
            if hasattr(self, "error")
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
            f"charge_id={_charge_id!r}, "
            f"merchant_id={_merchant_id!r}, "
            f"store_id={_store_id!r}, "
            f"platform_id={_platform_id!r}, "
            f"mode={_mode!r}, "
            f"gateway={_gateway!r}, "
            f"declaration={_declaration!r}, "
            f"declaration_result={_declaration_result!r}, "
            f"status={_status!r}, "
            f"error={_error!r}, "
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
        _charge_id=(
            self.charge_id
            if hasattr(self, "charge_id")
            else None
        )
        _merchant_id=(
            self.merchant_id
            if hasattr(self, "merchant_id")
            else None
        )
        _store_id=(
            self.store_id
            if hasattr(self, "store_id")
            else None
        )
        _platform_id=(
            self.platform_id
            if hasattr(self, "platform_id")
            else None
        )
        _mode=(
            self.mode
            if hasattr(self, "mode")
            else None
        )
        _gateway=(
            self.gateway
            if hasattr(self, "gateway")
            else None
        )
        _declaration=(
            self.declaration
            if hasattr(self, "declaration")
            else None
        )
        _declaration_result=(
            self.declaration_result
            if hasattr(self, "declaration_result")
            else None
        )
        _status=(
            self.status
            if hasattr(self, "status")
            else None
        )
        _error=(
            self.error
            if hasattr(self, "error")
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
            f"charge_id={_charge_id!s}, "
            f"merchant_id={_merchant_id!s}, "
            f"store_id={_store_id!s}, "
            f"platform_id={_platform_id!s}, "
            f"mode={_mode!s}, "
            f"gateway={_gateway!s}, "
            f"declaration={_declaration!s}, "
            f"declaration_result={_declaration_result!s}, "
            f"status={_status!s}, "
            f"error={_error!s}, "
            f"created_on={_created_on!s}, "
            f"updated_on={_updated_on!s}, "
            f"additional_properties={_additional_properties!s}, "
            f")"
        )
