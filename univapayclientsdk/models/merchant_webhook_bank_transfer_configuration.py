"""univapay_client_sdk.

This file was automatically generated for Univapay by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

# ruff: noqa: E501
from univapayclientsdk.api_helper import APIHelper


class MerchantWebhookBankTransferConfiguration(object):
    """Implementation of the 'MerchantWebhookBankTransferConfiguration' model.

    Bank transfer payment settings.

    Attributes:
        enabled (bool): Enables bank transfer payments.
        match_amount (bool): Requires the received deposit amount to exactly match
            the charge amount.
        expiration (str): ISO-8601 duration before the charge expires.
        virtual_bank_accounts_threshold (int): Threshold for provisioning additional
            virtual bank accounts.
        virtual_bank_accounts_fetch_count (int): Number of virtual bank accounts
            fetched per replenishment batch.
        default_extension_period (str): Default ISO-8601 extension period applied to
            eligible charges.
        maximum_extension_period (str): Maximum ISO-8601 extension period allowed for
            a charge.
        automatic_extension_enabled (bool): Automatically extends eligible bank
            transfer charges.
        charge_request_notification_enabled (bool): Sends notifications when a bank
            transfer charge is created.
        charge_request_canceled_notification_enabled (bool): Sends notifications when
            a bank transfer charge is canceled.
        charge_expired_notification_enabled (bool): Sends notifications when a bank
            transfer charge expires.
        deposit_received_notification_enabled (bool): Sends notifications when a
            deposit is received.
        deposit_insufficient_notification_enabled (bool): Sends notifications when a
            deposit is below the expected amount.
        deposit_exceeded_notification_enabled (bool): Sends notifications when a
            deposit exceeds the expected amount.
        extension_notification_enabled (bool): Sends notifications when a bank
            transfer charge is extended.
        remind_notification_period (str): ISO-8601 lead time for payment reminder
            notifications.
        remind_notification_enabled (bool): Sends reminder notifications before bank
            transfer expiry.
        additional_properties (Dict[str, Any]): The additional properties for the
            model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "enabled": "enabled",
        "match_amount": "match_amount",
        "expiration": "expiration",
        "virtual_bank_accounts_threshold": "virtual_bank_accounts_threshold",
        "virtual_bank_accounts_fetch_count": "virtual_bank_accounts_fetch_count",
        "default_extension_period": "default_extension_period",
        "maximum_extension_period": "maximum_extension_period",
        "automatic_extension_enabled": "automatic_extension_enabled",
        "charge_request_notification_enabled": "charge_request_notification_enabled",
        "charge_request_canceled_notification_enabled":
            "charge_request_canceled_notification_enabled",
        "charge_expired_notification_enabled": "charge_expired_notification_enabled",
        "deposit_received_notification_enabled":
            "deposit_received_notification_enabled",
        "deposit_insufficient_notification_enabled":
            "deposit_insufficient_notification_enabled",
        "deposit_exceeded_notification_enabled":
            "deposit_exceeded_notification_enabled",
        "extension_notification_enabled": "extension_notification_enabled",
        "remind_notification_period": "remind_notification_period",
        "remind_notification_enabled": "remind_notification_enabled",
    }

    _optionals = [
        "enabled",
        "match_amount",
        "expiration",
        "virtual_bank_accounts_threshold",
        "virtual_bank_accounts_fetch_count",
        "default_extension_period",
        "maximum_extension_period",
        "automatic_extension_enabled",
        "charge_request_notification_enabled",
        "charge_request_canceled_notification_enabled",
        "charge_expired_notification_enabled",
        "deposit_received_notification_enabled",
        "deposit_insufficient_notification_enabled",
        "deposit_exceeded_notification_enabled",
        "extension_notification_enabled",
        "remind_notification_period",
        "remind_notification_enabled",
    ]

    _nullables = [
        "enabled",
        "match_amount",
        "expiration",
        "virtual_bank_accounts_threshold",
        "virtual_bank_accounts_fetch_count",
        "default_extension_period",
        "maximum_extension_period",
        "automatic_extension_enabled",
        "charge_request_notification_enabled",
        "charge_request_canceled_notification_enabled",
        "charge_expired_notification_enabled",
        "deposit_received_notification_enabled",
        "deposit_insufficient_notification_enabled",
        "deposit_exceeded_notification_enabled",
        "extension_notification_enabled",
        "remind_notification_period",
        "remind_notification_enabled",
    ]

    def __init__(
        self,
        enabled=APIHelper.SKIP,
        match_amount=APIHelper.SKIP,
        expiration=APIHelper.SKIP,
        virtual_bank_accounts_threshold=APIHelper.SKIP,
        virtual_bank_accounts_fetch_count=APIHelper.SKIP,
        default_extension_period=APIHelper.SKIP,
        maximum_extension_period=APIHelper.SKIP,
        automatic_extension_enabled=APIHelper.SKIP,
        charge_request_notification_enabled=APIHelper.SKIP,
        charge_request_canceled_notification_enabled=APIHelper.SKIP,
        charge_expired_notification_enabled=APIHelper.SKIP,
        deposit_received_notification_enabled=APIHelper.SKIP,
        deposit_insufficient_notification_enabled=APIHelper.SKIP,
        deposit_exceeded_notification_enabled=APIHelper.SKIP,
        extension_notification_enabled=APIHelper.SKIP,
        remind_notification_period=APIHelper.SKIP,
        remind_notification_enabled=APIHelper.SKIP,
        additional_properties=None):
        """Initialize a MerchantWebhookBankTransferConfiguration instance."""
        # Initialize members of the class
        if enabled is not APIHelper.SKIP:
            self.enabled = enabled
        if match_amount is not APIHelper.SKIP:
            self.match_amount = match_amount
        if expiration is not APIHelper.SKIP:
            self.expiration = expiration
        if virtual_bank_accounts_threshold is not APIHelper.SKIP:
            self.virtual_bank_accounts_threshold = virtual_bank_accounts_threshold
        if virtual_bank_accounts_fetch_count is not APIHelper.SKIP:
            self.virtual_bank_accounts_fetch_count =\
                 virtual_bank_accounts_fetch_count
        if default_extension_period is not APIHelper.SKIP:
            self.default_extension_period = default_extension_period
        if maximum_extension_period is not APIHelper.SKIP:
            self.maximum_extension_period = maximum_extension_period
        if automatic_extension_enabled is not APIHelper.SKIP:
            self.automatic_extension_enabled = automatic_extension_enabled
        if charge_request_notification_enabled is not APIHelper.SKIP:
            self.charge_request_notification_enabled =\
                 charge_request_notification_enabled
        if charge_request_canceled_notification_enabled is not APIHelper.SKIP:
            self.charge_request_canceled_notification_enabled =\
                 charge_request_canceled_notification_enabled
        if charge_expired_notification_enabled is not APIHelper.SKIP:
            self.charge_expired_notification_enabled =\
                 charge_expired_notification_enabled
        if deposit_received_notification_enabled is not APIHelper.SKIP:
            self.deposit_received_notification_enabled =\
                 deposit_received_notification_enabled
        if deposit_insufficient_notification_enabled is not APIHelper.SKIP:
            self.deposit_insufficient_notification_enabled =\
                 deposit_insufficient_notification_enabled
        if deposit_exceeded_notification_enabled is not APIHelper.SKIP:
            self.deposit_exceeded_notification_enabled =\
                 deposit_exceeded_notification_enabled
        if extension_notification_enabled is not APIHelper.SKIP:
            self.extension_notification_enabled = extension_notification_enabled
        if remind_notification_period is not APIHelper.SKIP:
            self.remind_notification_period = remind_notification_period
        if remind_notification_enabled is not APIHelper.SKIP:
            self.remind_notification_enabled = remind_notification_enabled

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
        enabled =\
            dictionary.get("enabled")\
            if "enabled" in dictionary.keys()\
                else APIHelper.SKIP
        match_amount =\
            dictionary.get("match_amount")\
            if "match_amount" in dictionary.keys()\
                else APIHelper.SKIP
        expiration =\
            dictionary.get("expiration")\
            if "expiration" in dictionary.keys()\
                else APIHelper.SKIP
        virtual_bank_accounts_threshold =\
            dictionary.get("virtual_bank_accounts_threshold")\
            if "virtual_bank_accounts_threshold" in dictionary.keys()\
                else APIHelper.SKIP
        virtual_bank_accounts_fetch_count =\
            dictionary.get("virtual_bank_accounts_fetch_count")\
            if "virtual_bank_accounts_fetch_count" in dictionary.keys()\
                else APIHelper.SKIP
        default_extension_period =\
            dictionary.get("default_extension_period")\
            if "default_extension_period" in dictionary.keys()\
                else APIHelper.SKIP
        maximum_extension_period =\
            dictionary.get("maximum_extension_period")\
            if "maximum_extension_period" in dictionary.keys()\
                else APIHelper.SKIP
        automatic_extension_enabled =\
            dictionary.get("automatic_extension_enabled")\
            if "automatic_extension_enabled" in dictionary.keys()\
                else APIHelper.SKIP
        charge_request_notification_enabled =\
            dictionary.get("charge_request_notification_enabled")\
            if "charge_request_notification_enabled" in dictionary.keys()\
                else APIHelper.SKIP
        charge_request_canceled_notification_enabled =\
            dictionary.get("charge_request_canceled_notification_enabled")\
            if "charge_request_canceled_notification_enabled" in dictionary.keys()\
                else APIHelper.SKIP
        charge_expired_notification_enabled =\
            dictionary.get("charge_expired_notification_enabled")\
            if "charge_expired_notification_enabled" in dictionary.keys()\
                else APIHelper.SKIP
        deposit_received_notification_enabled =\
            dictionary.get("deposit_received_notification_enabled")\
            if "deposit_received_notification_enabled" in dictionary.keys()\
                else APIHelper.SKIP
        deposit_insufficient_notification_enabled =\
            dictionary.get("deposit_insufficient_notification_enabled")\
            if "deposit_insufficient_notification_enabled" in dictionary.keys()\
                else APIHelper.SKIP
        deposit_exceeded_notification_enabled =\
            dictionary.get("deposit_exceeded_notification_enabled")\
            if "deposit_exceeded_notification_enabled" in dictionary.keys()\
                else APIHelper.SKIP
        extension_notification_enabled =\
            dictionary.get("extension_notification_enabled")\
            if "extension_notification_enabled" in dictionary.keys()\
                else APIHelper.SKIP
        remind_notification_period =\
            dictionary.get("remind_notification_period")\
            if "remind_notification_period" in dictionary.keys()\
                else APIHelper.SKIP
        remind_notification_enabled =\
            dictionary.get("remind_notification_enabled")\
            if "remind_notification_enabled" in dictionary.keys()\
                else APIHelper.SKIP

        additional_properties = APIHelper.get_additional_properties(
            dictionary={k: v for k, v in dictionary.items()
                        if k not in cls._names.values()},
            unboxing_function=lambda value: value)

        # Return an object of this model
        return cls(enabled,
                   match_amount,
                   expiration,
                   virtual_bank_accounts_threshold,
                   virtual_bank_accounts_fetch_count,
                   default_extension_period,
                   maximum_extension_period,
                   automatic_extension_enabled,
                   charge_request_notification_enabled,
                   charge_request_canceled_notification_enabled,
                   charge_expired_notification_enabled,
                   deposit_received_notification_enabled,
                   deposit_insufficient_notification_enabled,
                   deposit_exceeded_notification_enabled,
                   extension_notification_enabled,
                   remind_notification_period,
                   remind_notification_enabled,
                   additional_properties)

    def __repr__(self):
        """Return a unambiguous string representation."""
        _enabled=(
            self.enabled
            if hasattr(self, "enabled")
            else None
        )
        _match_amount=(
            self.match_amount
            if hasattr(self, "match_amount")
            else None
        )
        _expiration=(
            self.expiration
            if hasattr(self, "expiration")
            else None
        )
        _virtual_bank_accounts_threshold=(
            self.virtual_bank_accounts_threshold
            if hasattr(self, "virtual_bank_accounts_threshold")
            else None
        )
        _virtual_bank_accounts_fetch_count=(
            self.virtual_bank_accounts_fetch_count
            if hasattr(self, "virtual_bank_accounts_fetch_count")
            else None
        )
        _default_extension_period=(
            self.default_extension_period
            if hasattr(self, "default_extension_period")
            else None
        )
        _maximum_extension_period=(
            self.maximum_extension_period
            if hasattr(self, "maximum_extension_period")
            else None
        )
        _automatic_extension_enabled=(
            self.automatic_extension_enabled
            if hasattr(self, "automatic_extension_enabled")
            else None
        )
        _charge_request_notification_enabled=(
            self.charge_request_notification_enabled
            if hasattr(self, "charge_request_notification_enabled")
            else None
        )
        _charge_request_canceled_notification_enabled=(
            self.charge_request_canceled_notification_enabled
            if hasattr(self, "charge_request_canceled_notification_enabled")
            else None
        )
        _charge_expired_notification_enabled=(
            self.charge_expired_notification_enabled
            if hasattr(self, "charge_expired_notification_enabled")
            else None
        )
        _deposit_received_notification_enabled=(
            self.deposit_received_notification_enabled
            if hasattr(self, "deposit_received_notification_enabled")
            else None
        )
        _deposit_insufficient_notification_enabled=(
            self.deposit_insufficient_notification_enabled
            if hasattr(self, "deposit_insufficient_notification_enabled")
            else None
        )
        _deposit_exceeded_notification_enabled=(
            self.deposit_exceeded_notification_enabled
            if hasattr(self, "deposit_exceeded_notification_enabled")
            else None
        )
        _extension_notification_enabled=(
            self.extension_notification_enabled
            if hasattr(self, "extension_notification_enabled")
            else None
        )
        _remind_notification_period=(
            self.remind_notification_period
            if hasattr(self, "remind_notification_period")
            else None
        )
        _remind_notification_enabled=(
            self.remind_notification_enabled
            if hasattr(self, "remind_notification_enabled")
            else None
        )
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"enabled={_enabled!r}, "
            f"match_amount={_match_amount!r}, "
            f"expiration={_expiration!r}, "
            f"virtual_bank_accounts_threshold={_virtual_bank_accounts_threshold!r}, "
            f"virtual_bank_accounts_fetch_count={_virtual_bank_accounts_fetch_count!r}, "
            f"default_extension_period={_default_extension_period!r}, "
            f"maximum_extension_period={_maximum_extension_period!r}, "
            f"automatic_extension_enabled={_automatic_extension_enabled!r}, "
            f"charge_request_notification_enabled={_charge_request_notification_enabled!r}, "
            f"charge_request_canceled_notification_enabled={_charge_request_canceled_notification_enabled!r}, "
            f"charge_expired_notification_enabled={_charge_expired_notification_enabled!r}, "
            f"deposit_received_notification_enabled={_deposit_received_notification_enabled!r}, "
            f"deposit_insufficient_notification_enabled={_deposit_insufficient_notification_enabled!r}, "
            f"deposit_exceeded_notification_enabled={_deposit_exceeded_notification_enabled!r}, "
            f"extension_notification_enabled={_extension_notification_enabled!r}, "
            f"remind_notification_period={_remind_notification_period!r}, "
            f"remind_notification_enabled={_remind_notification_enabled!r}, "
            f"additional_properties={_additional_properties!r}, "
            f")"
        )

    def __str__(self):
        """Return a human-readable string representation."""
        _enabled=(
            self.enabled
            if hasattr(self, "enabled")
            else None
        )
        _match_amount=(
            self.match_amount
            if hasattr(self, "match_amount")
            else None
        )
        _expiration=(
            self.expiration
            if hasattr(self, "expiration")
            else None
        )
        _virtual_bank_accounts_threshold=(
            self.virtual_bank_accounts_threshold
            if hasattr(self, "virtual_bank_accounts_threshold")
            else None
        )
        _virtual_bank_accounts_fetch_count=(
            self.virtual_bank_accounts_fetch_count
            if hasattr(self, "virtual_bank_accounts_fetch_count")
            else None
        )
        _default_extension_period=(
            self.default_extension_period
            if hasattr(self, "default_extension_period")
            else None
        )
        _maximum_extension_period=(
            self.maximum_extension_period
            if hasattr(self, "maximum_extension_period")
            else None
        )
        _automatic_extension_enabled=(
            self.automatic_extension_enabled
            if hasattr(self, "automatic_extension_enabled")
            else None
        )
        _charge_request_notification_enabled=(
            self.charge_request_notification_enabled
            if hasattr(self, "charge_request_notification_enabled")
            else None
        )
        _charge_request_canceled_notification_enabled=(
            self.charge_request_canceled_notification_enabled
            if hasattr(self, "charge_request_canceled_notification_enabled")
            else None
        )
        _charge_expired_notification_enabled=(
            self.charge_expired_notification_enabled
            if hasattr(self, "charge_expired_notification_enabled")
            else None
        )
        _deposit_received_notification_enabled=(
            self.deposit_received_notification_enabled
            if hasattr(self, "deposit_received_notification_enabled")
            else None
        )
        _deposit_insufficient_notification_enabled=(
            self.deposit_insufficient_notification_enabled
            if hasattr(self, "deposit_insufficient_notification_enabled")
            else None
        )
        _deposit_exceeded_notification_enabled=(
            self.deposit_exceeded_notification_enabled
            if hasattr(self, "deposit_exceeded_notification_enabled")
            else None
        )
        _extension_notification_enabled=(
            self.extension_notification_enabled
            if hasattr(self, "extension_notification_enabled")
            else None
        )
        _remind_notification_period=(
            self.remind_notification_period
            if hasattr(self, "remind_notification_period")
            else None
        )
        _remind_notification_enabled=(
            self.remind_notification_enabled
            if hasattr(self, "remind_notification_enabled")
            else None
        )
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"enabled={_enabled!s}, "
            f"match_amount={_match_amount!s}, "
            f"expiration={_expiration!s}, "
            f"virtual_bank_accounts_threshold={_virtual_bank_accounts_threshold!s}, "
            f"virtual_bank_accounts_fetch_count={_virtual_bank_accounts_fetch_count!s}, "
            f"default_extension_period={_default_extension_period!s}, "
            f"maximum_extension_period={_maximum_extension_period!s}, "
            f"automatic_extension_enabled={_automatic_extension_enabled!s}, "
            f"charge_request_notification_enabled={_charge_request_notification_enabled!s}, "
            f"charge_request_canceled_notification_enabled={_charge_request_canceled_notification_enabled!s}, "
            f"charge_expired_notification_enabled={_charge_expired_notification_enabled!s}, "
            f"deposit_received_notification_enabled={_deposit_received_notification_enabled!s}, "
            f"deposit_insufficient_notification_enabled={_deposit_insufficient_notification_enabled!s}, "
            f"deposit_exceeded_notification_enabled={_deposit_exceeded_notification_enabled!s}, "
            f"extension_notification_enabled={_extension_notification_enabled!s}, "
            f"remind_notification_period={_remind_notification_period!s}, "
            f"remind_notification_enabled={_remind_notification_enabled!s}, "
            f"additional_properties={_additional_properties!s}, "
            f")"
        )
