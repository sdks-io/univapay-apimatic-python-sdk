"""univapay_client_sdk.

This file was automatically generated for Univapay by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

# ruff: noqa: E501
from univapayclientsdk.api_helper import APIHelper


class DirectDebitMerchantConfiguration(object):
    """Implementation of the 'DirectDebitMerchantConfiguration' model.

    The merchant's effective direct debit configuration.

    Attributes:
        legacy_id (str): Identifier of the merchant in the legacy direct debit system.
        enabled (bool): Whether direct debit is enabled for this merchant.
        debit_date (DirectDebitDebitDate): Monthly debit cycle — funds are pulled on
            either the 14th or the 27th.
        consignor_code (str): Consignor code (委託者コード) assigned by the collecting bank.
        classifier (str): Transfer classification code (区分) agreed with the
            collecting bank.
        signature (str): Name printed on the consumer's bank statement (印字名), in
            half-width katakana.
        additional_properties (Dict[str, Any]): The additional properties for the
            model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "legacy_id": "legacy_id",
        "enabled": "enabled",
        "debit_date": "debit_date",
        "consignor_code": "consignor_code",
        "classifier": "classifier",
        "signature": "signature",
    }

    _optionals = [
        "legacy_id",
        "enabled",
        "debit_date",
        "consignor_code",
        "classifier",
        "signature",
    ]

    def __init__(
        self,
        legacy_id=APIHelper.SKIP,
        enabled=APIHelper.SKIP,
        debit_date=APIHelper.SKIP,
        consignor_code=APIHelper.SKIP,
        classifier=APIHelper.SKIP,
        signature=APIHelper.SKIP,
        additional_properties=None):
        """Initialize a DirectDebitMerchantConfiguration instance."""
        # Initialize members of the class
        if legacy_id is not APIHelper.SKIP:
            self.legacy_id = legacy_id
        if enabled is not APIHelper.SKIP:
            self.enabled = enabled
        if debit_date is not APIHelper.SKIP:
            self.debit_date = debit_date
        if consignor_code is not APIHelper.SKIP:
            self.consignor_code = consignor_code
        if classifier is not APIHelper.SKIP:
            self.classifier = classifier
        if signature is not APIHelper.SKIP:
            self.signature = signature

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
        legacy_id =\
            dictionary.get("legacy_id")\
            if dictionary.get("legacy_id")\
                else APIHelper.SKIP
        enabled =\
            dictionary.get("enabled")\
            if "enabled" in dictionary.keys()\
                else APIHelper.SKIP
        debit_date =\
            dictionary.get("debit_date")\
            if dictionary.get("debit_date")\
                else APIHelper.SKIP
        consignor_code =\
            dictionary.get("consignor_code")\
            if dictionary.get("consignor_code")\
                else APIHelper.SKIP
        classifier =\
            dictionary.get("classifier")\
            if dictionary.get("classifier")\
                else APIHelper.SKIP
        signature =\
            dictionary.get("signature")\
            if dictionary.get("signature")\
                else APIHelper.SKIP

        additional_properties = APIHelper.get_additional_properties(
            dictionary={k: v for k, v in dictionary.items()
                        if k not in cls._names.values()},
            unboxing_function=lambda value: value)

        # Return an object of this model
        return cls(legacy_id,
                   enabled,
                   debit_date,
                   consignor_code,
                   classifier,
                   signature,
                   additional_properties)

    def __repr__(self):
        """Return a unambiguous string representation."""
        _legacy_id=(
            self.legacy_id
            if hasattr(self, "legacy_id")
            else None
        )
        _enabled=(
            self.enabled
            if hasattr(self, "enabled")
            else None
        )
        _debit_date=(
            self.debit_date
            if hasattr(self, "debit_date")
            else None
        )
        _consignor_code=(
            self.consignor_code
            if hasattr(self, "consignor_code")
            else None
        )
        _classifier=(
            self.classifier
            if hasattr(self, "classifier")
            else None
        )
        _signature=(
            self.signature
            if hasattr(self, "signature")
            else None
        )
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"legacy_id={_legacy_id!r}, "
            f"enabled={_enabled!r}, "
            f"debit_date={_debit_date!r}, "
            f"consignor_code={_consignor_code!r}, "
            f"classifier={_classifier!r}, "
            f"signature={_signature!r}, "
            f"additional_properties={_additional_properties!r}, "
            f")"
        )

    def __str__(self):
        """Return a human-readable string representation."""
        _legacy_id=(
            self.legacy_id
            if hasattr(self, "legacy_id")
            else None
        )
        _enabled=(
            self.enabled
            if hasattr(self, "enabled")
            else None
        )
        _debit_date=(
            self.debit_date
            if hasattr(self, "debit_date")
            else None
        )
        _consignor_code=(
            self.consignor_code
            if hasattr(self, "consignor_code")
            else None
        )
        _classifier=(
            self.classifier
            if hasattr(self, "classifier")
            else None
        )
        _signature=(
            self.signature
            if hasattr(self, "signature")
            else None
        )
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"legacy_id={_legacy_id!s}, "
            f"enabled={_enabled!s}, "
            f"debit_date={_debit_date!s}, "
            f"consignor_code={_consignor_code!s}, "
            f"classifier={_classifier!s}, "
            f"signature={_signature!s}, "
            f"additional_properties={_additional_properties!s}, "
            f")"
        )
