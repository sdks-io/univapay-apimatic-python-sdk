"""univapay_client_sdk.

This file was automatically generated for Univapay by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

# ruff: noqa: E501
from univapayclientsdk.api_helper import APIHelper
from univapayclientsdk.models.subscription_schedule_settings import (
    SubscriptionScheduleSettings,
)
from univapayclientsdk.models.subscription_simulation_plan_settings import (
    SubscriptionSimulationPlanSettings,
)


class SubscriptionSimulationRequest(object):
    """Implementation of the 'SubscriptionSimulationRequest' model.

    Request payload for simulating a subscription payment schedule without creating a
    live subscription. Specify exactly one of 'period' or 'cyclical_period' to define
    the billing frequency. 'installment_plan' and 'subscription_plan' are mutually
    exclusive — specify at most one to model a limited-cycle schedule.

    Attributes:
        amount (int): Amount to be charged in each cycle. Must be a positive integer.
        currency (str): ISO-4217 currency code.
        payment_type (TransactionTokenPaymentType): Transaction Token Payment Type
            schema.
        initial_amount (int): Optional different amount for the first charge. Must be
            zero or greater.
        period (SubscriptionSimulationPeriod): Billing frequency for the simulated
            schedule. Includes `bimonthly`, which is not offered on
            `SubscriptionPeriod` for live subscription creation.
        cyclical_period (str): ISO-8601 Duration for custom frequency (e.g., P3D,
            P2M). Cannot be used together with 'period' — specify exactly one of the
            two.
        schedule_settings (SubscriptionScheduleSettings): Schedule settings applied
            to a subscription.
        installment_plan (SubscriptionSimulationPlanSettings): Cycle-limiting plan
            configuration used to simulate an installment plan or a Univapay-side
            subscription plan.
        subscription_plan (SubscriptionSimulationPlanSettings): Cycle-limiting plan
            configuration used to simulate an installment plan or a Univapay-side
            subscription plan.
        only_direct_currency (bool): Whether only direct currency processing is
            allowed.
        additional_properties (Dict[str, Any]): The additional properties for the
            model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "amount": "amount",
        "currency": "currency",
        "payment_type": "payment_type",
        "schedule_settings": "schedule_settings",
        "initial_amount": "initial_amount",
        "period": "period",
        "cyclical_period": "cyclical_period",
        "installment_plan": "installment_plan",
        "subscription_plan": "subscription_plan",
        "only_direct_currency": "only_direct_currency",
    }

    _optionals = [
        "initial_amount",
        "period",
        "cyclical_period",
        "installment_plan",
        "subscription_plan",
        "only_direct_currency",
    ]

    def __init__(
        self,
        amount=None,
        currency=None,
        payment_type=None,
        schedule_settings=None,
        initial_amount=APIHelper.SKIP,
        period=APIHelper.SKIP,
        cyclical_period=APIHelper.SKIP,
        installment_plan=APIHelper.SKIP,
        subscription_plan=APIHelper.SKIP,
        only_direct_currency=APIHelper.SKIP,
        additional_properties=None):
        """Initialize a SubscriptionSimulationRequest instance."""
        # Initialize members of the class
        self.amount = amount
        self.currency = currency
        self.payment_type = payment_type
        if initial_amount is not APIHelper.SKIP:
            self.initial_amount = initial_amount
        if period is not APIHelper.SKIP:
            self.period = period
        if cyclical_period is not APIHelper.SKIP:
            self.cyclical_period = cyclical_period
        self.schedule_settings = schedule_settings
        if installment_plan is not APIHelper.SKIP:
            self.installment_plan = installment_plan
        if subscription_plan is not APIHelper.SKIP:
            self.subscription_plan = subscription_plan
        if only_direct_currency is not APIHelper.SKIP:
            self.only_direct_currency = only_direct_currency

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
        amount =\
            dictionary.get("amount")\
            if dictionary.get("amount")\
                else None
        currency =\
            dictionary.get("currency")\
            if dictionary.get("currency")\
                else None
        payment_type =\
            dictionary.get("payment_type")\
            if dictionary.get("payment_type")\
                else None
        schedule_settings =\
            SubscriptionScheduleSettings.from_dictionary(
                dictionary.get("schedule_settings"))\
                if dictionary.get("schedule_settings") else None
        initial_amount =\
            dictionary.get("initial_amount")\
            if dictionary.get("initial_amount")\
                else APIHelper.SKIP
        period =\
            dictionary.get("period")\
            if dictionary.get("period")\
                else APIHelper.SKIP
        cyclical_period =\
            dictionary.get("cyclical_period")\
            if dictionary.get("cyclical_period")\
                else APIHelper.SKIP
        installment_plan =\
            SubscriptionSimulationPlanSettings.from_dictionary(
                dictionary.get("installment_plan"))\
                if "installment_plan" in dictionary.keys()\
                else APIHelper.SKIP
        subscription_plan =\
            SubscriptionSimulationPlanSettings.from_dictionary(
                dictionary.get("subscription_plan"))\
                if "subscription_plan" in dictionary.keys()\
                else APIHelper.SKIP
        only_direct_currency =\
            dictionary.get("only_direct_currency")\
            if "only_direct_currency" in dictionary.keys()\
                else APIHelper.SKIP

        additional_properties = APIHelper.get_additional_properties(
            dictionary={k: v for k, v in dictionary.items()
                        if k not in cls._names.values()},
            unboxing_function=lambda value: value)

        # Return an object of this model
        return cls(amount,
                   currency,
                   payment_type,
                   schedule_settings,
                   initial_amount,
                   period,
                   cyclical_period,
                   installment_plan,
                   subscription_plan,
                   only_direct_currency,
                   additional_properties)

    def __repr__(self):
        """Return a unambiguous string representation."""
        _amount=self.amount
        _currency=self.currency
        _payment_type=self.payment_type
        _initial_amount=(
            self.initial_amount
            if hasattr(self, "initial_amount")
            else None
        )
        _period=(
            self.period
            if hasattr(self, "period")
            else None
        )
        _cyclical_period=(
            self.cyclical_period
            if hasattr(self, "cyclical_period")
            else None
        )
        _schedule_settings=self.schedule_settings
        _installment_plan=(
            self.installment_plan
            if hasattr(self, "installment_plan")
            else None
        )
        _subscription_plan=(
            self.subscription_plan
            if hasattr(self, "subscription_plan")
            else None
        )
        _only_direct_currency=(
            self.only_direct_currency
            if hasattr(self, "only_direct_currency")
            else None
        )
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"amount={_amount!r}, "
            f"currency={_currency!r}, "
            f"payment_type={_payment_type!r}, "
            f"initial_amount={_initial_amount!r}, "
            f"period={_period!r}, "
            f"cyclical_period={_cyclical_period!r}, "
            f"schedule_settings={_schedule_settings!r}, "
            f"installment_plan={_installment_plan!r}, "
            f"subscription_plan={_subscription_plan!r}, "
            f"only_direct_currency={_only_direct_currency!r}, "
            f"additional_properties={_additional_properties!r}, "
            f")"
        )

    def __str__(self):
        """Return a human-readable string representation."""
        _amount=self.amount
        _currency=self.currency
        _payment_type=self.payment_type
        _initial_amount=(
            self.initial_amount
            if hasattr(self, "initial_amount")
            else None
        )
        _period=(
            self.period
            if hasattr(self, "period")
            else None
        )
        _cyclical_period=(
            self.cyclical_period
            if hasattr(self, "cyclical_period")
            else None
        )
        _schedule_settings=self.schedule_settings
        _installment_plan=(
            self.installment_plan
            if hasattr(self, "installment_plan")
            else None
        )
        _subscription_plan=(
            self.subscription_plan
            if hasattr(self, "subscription_plan")
            else None
        )
        _only_direct_currency=(
            self.only_direct_currency
            if hasattr(self, "only_direct_currency")
            else None
        )
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"amount={_amount!s}, "
            f"currency={_currency!s}, "
            f"payment_type={_payment_type!s}, "
            f"initial_amount={_initial_amount!s}, "
            f"period={_period!s}, "
            f"cyclical_period={_cyclical_period!s}, "
            f"schedule_settings={_schedule_settings!s}, "
            f"installment_plan={_installment_plan!s}, "
            f"subscription_plan={_subscription_plan!s}, "
            f"only_direct_currency={_only_direct_currency!s}, "
            f"additional_properties={_additional_properties!s}, "
            f")"
        )
