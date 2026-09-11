"""univapay_client_sdk.

This file was automatically generated for Univapay by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

# ruff: noqa: E501
from univapayclientsdk.api_helper import APIHelper
from univapayclientsdk.models.checkout_money_amount import (
    CheckoutMoneyAmount,
)


class CheckoutSubscriptionPlanConfiguration(object):
    """Implementation of the 'CheckoutSubscriptionPlanConfiguration' model.

    Univapay-side subscription plan configuration applied to checkout.

    Attributes:
        enabled (bool): Whether subscription plans are enabled.
        fixed_cycle (bool): Whether fixed-cycle subscription plans are allowed.
        fixed_cycle_amount (bool): Whether fixed-cycle-amount subscription plans are
            allowed.
        supported_payment_types (List[CheckoutPaymentType]): Payment types eligible
            for subscription plans.
        min_charge_amount (CheckoutMoneyAmount): Minimum charge amount eligible for
            subscription plans. `null` when unrestricted.
        max_payout_period (str): ISO-8601 period bounding the maximum payout delay
            for subscription settlements. `null` when unrestricted.
        additional_properties (Dict[str, Any]): The additional properties for the
            model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "enabled": "enabled",
        "fixed_cycle": "fixed_cycle",
        "fixed_cycle_amount": "fixed_cycle_amount",
        "supported_payment_types": "supported_payment_types",
        "min_charge_amount": "min_charge_amount",
        "max_payout_period": "max_payout_period",
    }

    _optionals = [
        "enabled",
        "fixed_cycle",
        "fixed_cycle_amount",
        "supported_payment_types",
        "min_charge_amount",
        "max_payout_period",
    ]

    _nullables = [
        "min_charge_amount",
        "max_payout_period",
    ]

    def __init__(
        self,
        enabled=APIHelper.SKIP,
        fixed_cycle=APIHelper.SKIP,
        fixed_cycle_amount=APIHelper.SKIP,
        supported_payment_types=APIHelper.SKIP,
        min_charge_amount=APIHelper.SKIP,
        max_payout_period=APIHelper.SKIP,
        additional_properties=None):
        """Initialize a CheckoutSubscriptionPlanConfiguration instance."""
        # Initialize members of the class
        if enabled is not APIHelper.SKIP:
            self.enabled = enabled
        if fixed_cycle is not APIHelper.SKIP:
            self.fixed_cycle = fixed_cycle
        if fixed_cycle_amount is not APIHelper.SKIP:
            self.fixed_cycle_amount = fixed_cycle_amount
        if supported_payment_types is not APIHelper.SKIP:
            self.supported_payment_types = supported_payment_types
        if min_charge_amount is not APIHelper.SKIP:
            self.min_charge_amount = min_charge_amount
        if max_payout_period is not APIHelper.SKIP:
            self.max_payout_period = max_payout_period

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
        fixed_cycle =\
            dictionary.get("fixed_cycle")\
            if "fixed_cycle" in dictionary.keys()\
                else APIHelper.SKIP
        fixed_cycle_amount =\
            dictionary.get("fixed_cycle_amount")\
            if "fixed_cycle_amount" in dictionary.keys()\
                else APIHelper.SKIP
        supported_payment_types =\
            dictionary.get("supported_payment_types")\
            if dictionary.get("supported_payment_types")\
                else APIHelper.SKIP
        if "min_charge_amount" in dictionary.keys():
            min_charge_amount =\
                CheckoutMoneyAmount.from_dictionary(
                dictionary.get("min_charge_amount"))\
                if dictionary.get("min_charge_amount") else None
        else:
            min_charge_amount = APIHelper.SKIP
        max_payout_period =\
            dictionary.get("max_payout_period")\
            if "max_payout_period" in dictionary.keys()\
                else APIHelper.SKIP

        additional_properties = APIHelper.get_additional_properties(
            dictionary={k: v for k, v in dictionary.items()
                        if k not in cls._names.values()},
            unboxing_function=lambda value: value)

        # Return an object of this model
        return cls(enabled,
                   fixed_cycle,
                   fixed_cycle_amount,
                   supported_payment_types,
                   min_charge_amount,
                   max_payout_period,
                   additional_properties)

    def __repr__(self):
        """Return a unambiguous string representation."""
        _enabled=(
            self.enabled
            if hasattr(self, "enabled")
            else None
        )
        _fixed_cycle=(
            self.fixed_cycle
            if hasattr(self, "fixed_cycle")
            else None
        )
        _fixed_cycle_amount=(
            self.fixed_cycle_amount
            if hasattr(self, "fixed_cycle_amount")
            else None
        )
        _supported_payment_types=(
            self.supported_payment_types
            if hasattr(self, "supported_payment_types")
            else None
        )
        _min_charge_amount=(
            self.min_charge_amount
            if hasattr(self, "min_charge_amount")
            else None
        )
        _max_payout_period=(
            self.max_payout_period
            if hasattr(self, "max_payout_period")
            else None
        )
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"enabled={_enabled!r}, "
            f"fixed_cycle={_fixed_cycle!r}, "
            f"fixed_cycle_amount={_fixed_cycle_amount!r}, "
            f"supported_payment_types={_supported_payment_types!r}, "
            f"min_charge_amount={_min_charge_amount!r}, "
            f"max_payout_period={_max_payout_period!r}, "
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
        _fixed_cycle=(
            self.fixed_cycle
            if hasattr(self, "fixed_cycle")
            else None
        )
        _fixed_cycle_amount=(
            self.fixed_cycle_amount
            if hasattr(self, "fixed_cycle_amount")
            else None
        )
        _supported_payment_types=(
            self.supported_payment_types
            if hasattr(self, "supported_payment_types")
            else None
        )
        _min_charge_amount=(
            self.min_charge_amount
            if hasattr(self, "min_charge_amount")
            else None
        )
        _max_payout_period=(
            self.max_payout_period
            if hasattr(self, "max_payout_period")
            else None
        )
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"enabled={_enabled!s}, "
            f"fixed_cycle={_fixed_cycle!s}, "
            f"fixed_cycle_amount={_fixed_cycle_amount!s}, "
            f"supported_payment_types={_supported_payment_types!s}, "
            f"min_charge_amount={_min_charge_amount!s}, "
            f"max_payout_period={_max_payout_period!s}, "
            f"additional_properties={_additional_properties!s}, "
            f")"
        )
