"""univapay_client_sdk.

This file was automatically generated for Univapay by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

# ruff: noqa: E501
from univapayclientsdk.api_helper import APIHelper


class CustomsDeclarationWebhookResult(object):
    """Implementation of the 'CustomsDeclarationWebhookResult' model.

    Result payload returned by the customs declaration formatter.

    Attributes:
        approving_authority (str): Customs authority that approved the declaration.
        trade_id (str): Gateway trade identifier.
        transaction_id (str): Gateway transaction identifier for customs.
        charge_transaction_id (str): Gateway charge transaction identifier linked to
            the declaration.
        additional_properties (Dict[str, Any]): The additional properties for the
            model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "approving_authority": "approving_authority",
        "trade_id": "trade_id",
        "transaction_id": "transaction_id",
        "charge_transaction_id": "charge_transaction_id",
    }

    _optionals = [
        "approving_authority",
        "trade_id",
        "transaction_id",
        "charge_transaction_id",
    ]

    _nullables = [
        "approving_authority",
        "trade_id",
        "transaction_id",
        "charge_transaction_id",
    ]

    def __init__(
        self,
        approving_authority=APIHelper.SKIP,
        trade_id=APIHelper.SKIP,
        transaction_id=APIHelper.SKIP,
        charge_transaction_id=APIHelper.SKIP,
        additional_properties=None):
        """Initialize a CustomsDeclarationWebhookResult instance."""
        # Initialize members of the class
        if approving_authority is not APIHelper.SKIP:
            self.approving_authority = approving_authority
        if trade_id is not APIHelper.SKIP:
            self.trade_id = trade_id
        if transaction_id is not APIHelper.SKIP:
            self.transaction_id = transaction_id
        if charge_transaction_id is not APIHelper.SKIP:
            self.charge_transaction_id = charge_transaction_id

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
        approving_authority =\
            dictionary.get("approving_authority")\
            if "approving_authority" in dictionary.keys()\
                else APIHelper.SKIP
        trade_id =\
            dictionary.get("trade_id")\
            if "trade_id" in dictionary.keys()\
                else APIHelper.SKIP
        transaction_id =\
            dictionary.get("transaction_id")\
            if "transaction_id" in dictionary.keys()\
                else APIHelper.SKIP
        charge_transaction_id =\
            dictionary.get("charge_transaction_id")\
            if "charge_transaction_id" in dictionary.keys()\
                else APIHelper.SKIP

        additional_properties = APIHelper.get_additional_properties(
            dictionary={k: v for k, v in dictionary.items()
                        if k not in cls._names.values()},
            unboxing_function=lambda value: value)

        # Return an object of this model
        return cls(approving_authority,
                   trade_id,
                   transaction_id,
                   charge_transaction_id,
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
        _approving_authority=(
            self.approving_authority
            if hasattr(self, "approving_authority")
            else None
        )
        _trade_id=(
            self.trade_id
            if hasattr(self, "trade_id")
            else None
        )
        _transaction_id=(
            self.transaction_id
            if hasattr(self, "transaction_id")
            else None
        )
        _charge_transaction_id=(
            self.charge_transaction_id
            if hasattr(self, "charge_transaction_id")
            else None
        )
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"approving_authority={_approving_authority!r}, "
            f"trade_id={_trade_id!r}, "
            f"transaction_id={_transaction_id!r}, "
            f"charge_transaction_id={_charge_transaction_id!r}, "
            f"additional_properties={_additional_properties!r}, "
            f")"
        )

    def __str__(self):
        """Return a human-readable string representation."""
        _approving_authority=(
            self.approving_authority
            if hasattr(self, "approving_authority")
            else None
        )
        _trade_id=(
            self.trade_id
            if hasattr(self, "trade_id")
            else None
        )
        _transaction_id=(
            self.transaction_id
            if hasattr(self, "transaction_id")
            else None
        )
        _charge_transaction_id=(
            self.charge_transaction_id
            if hasattr(self, "charge_transaction_id")
            else None
        )
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"approving_authority={_approving_authority!s}, "
            f"trade_id={_trade_id!s}, "
            f"transaction_id={_transaction_id!s}, "
            f"charge_transaction_id={_charge_transaction_id!s}, "
            f"additional_properties={_additional_properties!s}, "
            f")"
        )
