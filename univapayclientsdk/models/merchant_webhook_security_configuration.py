"""univapay_client_sdk.

This file was automatically generated for Univapay by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

# ruff: noqa: E501
from univapayclientsdk.api_helper import APIHelper
from univapayclientsdk.models.merchant_webhook_limit_charge_by_card_configuration import (  # noqa: E501
    MerchantWebhookLimitChargeByCardConfiguration,
)
from univapayclientsdk.models.merchant_webhook_limit_refund_by_sales_configuration import (  # noqa: E501
    MerchantWebhookLimitRefundBySalesConfiguration,
)
from univapayclientsdk.models.restrict_ip_after_failed_charge_config import (
    RestrictIpAfterFailedChargeConfig,
)


class MerchantWebhookSecurityConfiguration(object):
    """Implementation of the 'MerchantWebhookSecurityConfiguration' model.

    Merchant-level fraud and refund safety settings.

    Attributes:
        card_charge_cooldown (str): ISO-8601 duration between card charge attempts.
        subscription_cooldown (str): ISO-8601 duration between subscription charge
            attempts.
        idempotent_card_charge_cooldown (str): ISO-8601 duration for reusing an
            idempotent card charge key.
        idempotent_subscription_cooldown (str): ISO-8601 duration for reusing an
            idempotent subscription key.
        restrict_ip_after_failed_charge (RestrictIpAfterFailedChargeConfig): IP
            restriction policy applied after repeated failed charges.
        inspect_suspicious_login_after (str): Look-back period used to review
            suspicious login activity.
        refund_percent_limit (float): Maximum refund-to-sales percentage allowed
            before restriction.
        limit_charge_by_card_configuration
            (MerchantWebhookLimitChargeByCardConfiguration): Per-card velocity limit
            configuration.
        confirmation_required (bool): Requires confirmation before protected refund
            actions proceed.
        min_refund_threshold (int): Minimum refund amount, in minor units, subject to
            confirmation checks.
        limit_refund_by_sales (MerchantWebhookLimitRefundBySalesConfiguration):
            Refund-limiting configuration based on sales history.
        additional_properties (Dict[str, Any]): The additional properties for the
            model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "card_charge_cooldown": "card_charge_cooldown",
        "subscription_cooldown": "subscription_cooldown",
        "idempotent_card_charge_cooldown": "idempotent_card_charge_cooldown",
        "idempotent_subscription_cooldown": "idempotent_subscription_cooldown",
        "restrict_ip_after_failed_charge": "restrict_ip_after_failed_charge",
        "inspect_suspicious_login_after": "inspect_suspicious_login_after",
        "refund_percent_limit": "refund_percent_limit",
        "limit_charge_by_card_configuration": "limit_charge_by_card_configuration",
        "confirmation_required": "confirmation_required",
        "min_refund_threshold": "min_refund_threshold",
        "limit_refund_by_sales": "limit_refund_by_sales",
    }

    _optionals = [
        "card_charge_cooldown",
        "subscription_cooldown",
        "idempotent_card_charge_cooldown",
        "idempotent_subscription_cooldown",
        "restrict_ip_after_failed_charge",
        "inspect_suspicious_login_after",
        "refund_percent_limit",
        "limit_charge_by_card_configuration",
        "confirmation_required",
        "min_refund_threshold",
        "limit_refund_by_sales",
    ]

    _nullables = [
        "card_charge_cooldown",
        "subscription_cooldown",
        "idempotent_card_charge_cooldown",
        "idempotent_subscription_cooldown",
        "inspect_suspicious_login_after",
        "refund_percent_limit",
        "confirmation_required",
        "min_refund_threshold",
    ]

    def __init__(
        self,
        card_charge_cooldown=APIHelper.SKIP,
        subscription_cooldown=APIHelper.SKIP,
        idempotent_card_charge_cooldown=APIHelper.SKIP,
        idempotent_subscription_cooldown=APIHelper.SKIP,
        restrict_ip_after_failed_charge=APIHelper.SKIP,
        inspect_suspicious_login_after=APIHelper.SKIP,
        refund_percent_limit=APIHelper.SKIP,
        limit_charge_by_card_configuration=APIHelper.SKIP,
        confirmation_required=APIHelper.SKIP,
        min_refund_threshold=APIHelper.SKIP,
        limit_refund_by_sales=APIHelper.SKIP,
        additional_properties=None):
        """Initialize a MerchantWebhookSecurityConfiguration instance."""
        # Initialize members of the class
        if card_charge_cooldown is not APIHelper.SKIP:
            self.card_charge_cooldown = card_charge_cooldown
        if subscription_cooldown is not APIHelper.SKIP:
            self.subscription_cooldown = subscription_cooldown
        if idempotent_card_charge_cooldown is not APIHelper.SKIP:
            self.idempotent_card_charge_cooldown = idempotent_card_charge_cooldown
        if idempotent_subscription_cooldown is not APIHelper.SKIP:
            self.idempotent_subscription_cooldown = idempotent_subscription_cooldown
        if restrict_ip_after_failed_charge is not APIHelper.SKIP:
            self.restrict_ip_after_failed_charge = restrict_ip_after_failed_charge
        if inspect_suspicious_login_after is not APIHelper.SKIP:
            self.inspect_suspicious_login_after = inspect_suspicious_login_after
        if refund_percent_limit is not APIHelper.SKIP:
            self.refund_percent_limit = refund_percent_limit
        if limit_charge_by_card_configuration is not APIHelper.SKIP:
            self.limit_charge_by_card_configuration =\
                 limit_charge_by_card_configuration
        if confirmation_required is not APIHelper.SKIP:
            self.confirmation_required = confirmation_required
        if min_refund_threshold is not APIHelper.SKIP:
            self.min_refund_threshold = min_refund_threshold
        if limit_refund_by_sales is not APIHelper.SKIP:
            self.limit_refund_by_sales = limit_refund_by_sales

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
        card_charge_cooldown =\
            dictionary.get("card_charge_cooldown")\
            if "card_charge_cooldown" in dictionary.keys()\
                else APIHelper.SKIP
        subscription_cooldown =\
            dictionary.get("subscription_cooldown")\
            if "subscription_cooldown" in dictionary.keys()\
                else APIHelper.SKIP
        idempotent_card_charge_cooldown =\
            dictionary.get("idempotent_card_charge_cooldown")\
            if "idempotent_card_charge_cooldown" in dictionary.keys()\
                else APIHelper.SKIP
        idempotent_subscription_cooldown =\
            dictionary.get("idempotent_subscription_cooldown")\
            if "idempotent_subscription_cooldown" in dictionary.keys()\
                else APIHelper.SKIP
        restrict_ip_after_failed_charge =\
            RestrictIpAfterFailedChargeConfig.from_dictionary(
                dictionary.get("restrict_ip_after_failed_charge"))\
                if "restrict_ip_after_failed_charge" in dictionary.keys()\
                else APIHelper.SKIP
        inspect_suspicious_login_after =\
            dictionary.get("inspect_suspicious_login_after")\
            if "inspect_suspicious_login_after" in dictionary.keys()\
                else APIHelper.SKIP
        refund_percent_limit =\
            dictionary.get("refund_percent_limit")\
            if "refund_percent_limit" in dictionary.keys()\
                else APIHelper.SKIP
        limit_charge_by_card_configuration =\
            MerchantWebhookLimitChargeByCardConfiguration.from_dictionary(
                dictionary.get("limit_charge_by_card_configuration"))\
                if "limit_charge_by_card_configuration" in dictionary.keys()\
                else APIHelper.SKIP
        confirmation_required =\
            dictionary.get("confirmation_required")\
            if "confirmation_required" in dictionary.keys()\
                else APIHelper.SKIP
        min_refund_threshold =\
            dictionary.get("min_refund_threshold")\
            if "min_refund_threshold" in dictionary.keys()\
                else APIHelper.SKIP
        limit_refund_by_sales =\
            MerchantWebhookLimitRefundBySalesConfiguration.from_dictionary(
                dictionary.get("limit_refund_by_sales"))\
                if "limit_refund_by_sales" in dictionary.keys()\
                else APIHelper.SKIP

        additional_properties = APIHelper.get_additional_properties(
            dictionary={k: v for k, v in dictionary.items()
                        if k not in cls._names.values()},
            unboxing_function=lambda value: value)

        # Return an object of this model
        return cls(card_charge_cooldown,
                   subscription_cooldown,
                   idempotent_card_charge_cooldown,
                   idempotent_subscription_cooldown,
                   restrict_ip_after_failed_charge,
                   inspect_suspicious_login_after,
                   refund_percent_limit,
                   limit_charge_by_card_configuration,
                   confirmation_required,
                   min_refund_threshold,
                   limit_refund_by_sales,
                   additional_properties)

    def __repr__(self):
        """Return a unambiguous string representation."""
        _card_charge_cooldown=(
            self.card_charge_cooldown
            if hasattr(self, "card_charge_cooldown")
            else None
        )
        _subscription_cooldown=(
            self.subscription_cooldown
            if hasattr(self, "subscription_cooldown")
            else None
        )
        _idempotent_card_charge_cooldown=(
            self.idempotent_card_charge_cooldown
            if hasattr(self, "idempotent_card_charge_cooldown")
            else None
        )
        _idempotent_subscription_cooldown=(
            self.idempotent_subscription_cooldown
            if hasattr(self, "idempotent_subscription_cooldown")
            else None
        )
        _restrict_ip_after_failed_charge=(
            self.restrict_ip_after_failed_charge
            if hasattr(self, "restrict_ip_after_failed_charge")
            else None
        )
        _inspect_suspicious_login_after=(
            self.inspect_suspicious_login_after
            if hasattr(self, "inspect_suspicious_login_after")
            else None
        )
        _refund_percent_limit=(
            self.refund_percent_limit
            if hasattr(self, "refund_percent_limit")
            else None
        )
        _limit_charge_by_card_configuration=(
            self.limit_charge_by_card_configuration
            if hasattr(self, "limit_charge_by_card_configuration")
            else None
        )
        _confirmation_required=(
            self.confirmation_required
            if hasattr(self, "confirmation_required")
            else None
        )
        _min_refund_threshold=(
            self.min_refund_threshold
            if hasattr(self, "min_refund_threshold")
            else None
        )
        _limit_refund_by_sales=(
            self.limit_refund_by_sales
            if hasattr(self, "limit_refund_by_sales")
            else None
        )
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"card_charge_cooldown={_card_charge_cooldown!r}, "
            f"subscription_cooldown={_subscription_cooldown!r}, "
            f"idempotent_card_charge_cooldown={_idempotent_card_charge_cooldown!r}, "
            f"idempotent_subscription_cooldown={_idempotent_subscription_cooldown!r}, "
            f"restrict_ip_after_failed_charge={_restrict_ip_after_failed_charge!r}, "
            f"inspect_suspicious_login_after={_inspect_suspicious_login_after!r}, "
            f"refund_percent_limit={_refund_percent_limit!r}, "
            f"limit_charge_by_card_configuration={_limit_charge_by_card_configuration!r}, "
            f"confirmation_required={_confirmation_required!r}, "
            f"min_refund_threshold={_min_refund_threshold!r}, "
            f"limit_refund_by_sales={_limit_refund_by_sales!r}, "
            f"additional_properties={_additional_properties!r}, "
            f")"
        )

    def __str__(self):
        """Return a human-readable string representation."""
        _card_charge_cooldown=(
            self.card_charge_cooldown
            if hasattr(self, "card_charge_cooldown")
            else None
        )
        _subscription_cooldown=(
            self.subscription_cooldown
            if hasattr(self, "subscription_cooldown")
            else None
        )
        _idempotent_card_charge_cooldown=(
            self.idempotent_card_charge_cooldown
            if hasattr(self, "idempotent_card_charge_cooldown")
            else None
        )
        _idempotent_subscription_cooldown=(
            self.idempotent_subscription_cooldown
            if hasattr(self, "idempotent_subscription_cooldown")
            else None
        )
        _restrict_ip_after_failed_charge=(
            self.restrict_ip_after_failed_charge
            if hasattr(self, "restrict_ip_after_failed_charge")
            else None
        )
        _inspect_suspicious_login_after=(
            self.inspect_suspicious_login_after
            if hasattr(self, "inspect_suspicious_login_after")
            else None
        )
        _refund_percent_limit=(
            self.refund_percent_limit
            if hasattr(self, "refund_percent_limit")
            else None
        )
        _limit_charge_by_card_configuration=(
            self.limit_charge_by_card_configuration
            if hasattr(self, "limit_charge_by_card_configuration")
            else None
        )
        _confirmation_required=(
            self.confirmation_required
            if hasattr(self, "confirmation_required")
            else None
        )
        _min_refund_threshold=(
            self.min_refund_threshold
            if hasattr(self, "min_refund_threshold")
            else None
        )
        _limit_refund_by_sales=(
            self.limit_refund_by_sales
            if hasattr(self, "limit_refund_by_sales")
            else None
        )
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"card_charge_cooldown={_card_charge_cooldown!s}, "
            f"subscription_cooldown={_subscription_cooldown!s}, "
            f"idempotent_card_charge_cooldown={_idempotent_card_charge_cooldown!s}, "
            f"idempotent_subscription_cooldown={_idempotent_subscription_cooldown!s}, "
            f"restrict_ip_after_failed_charge={_restrict_ip_after_failed_charge!s}, "
            f"inspect_suspicious_login_after={_inspect_suspicious_login_after!s}, "
            f"refund_percent_limit={_refund_percent_limit!s}, "
            f"limit_charge_by_card_configuration={_limit_charge_by_card_configuration!s}, "
            f"confirmation_required={_confirmation_required!s}, "
            f"min_refund_threshold={_min_refund_threshold!s}, "
            f"limit_refund_by_sales={_limit_refund_by_sales!s}, "
            f"additional_properties={_additional_properties!s}, "
            f")"
        )
