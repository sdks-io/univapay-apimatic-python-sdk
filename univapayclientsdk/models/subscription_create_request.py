"""univapay_client_sdk.

This file was automatically generated for Univapay by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

# ruff: noqa: E501
from univapayclientsdk.api_helper import APIHelper
from univapayclientsdk.models.charge_create_request_three_ds import (
    ChargeCreateRequestThreeDs,
)
from univapayclientsdk.models.generic_metadata import (
    GenericMetadata,
)
from univapayclientsdk.models.subscription_installment_plan import (
    SubscriptionInstallmentPlan,
)
from univapayclientsdk.models.subscription_plan_settings import (
    SubscriptionPlanSettings,
)
from univapayclientsdk.models.subscription_schedule_settings import (
    SubscriptionScheduleSettings,
)


class SubscriptionCreateRequest(object):
    """Implementation of the 'SubscriptionCreateRequest' model.

    Request payload for creating a subscription.

    Attributes:
        transaction_token_id (uuid|str): Transaction token ID authorized for
            recurring payments.
        amount (int): Amount to be charged in each cycle.
        currency (str): ISO-4217 currency code.
        initial_amount (int): Optional different amount for the first charge.
        period (SubscriptionPeriod): Subscription Period schema.
        cyclical_period (str): ISO-8601 Duration for custom frequency (e.g., P3D,
            P2M).  Cannot be used if 'period' is specified.
        schedule_settings (SubscriptionScheduleSettings): Schedule settings applied
            to a subscription.
        installment_plan (SubscriptionInstallmentPlan): Configuration for credit card
            company side installments.
        subscription_plan (SubscriptionPlanSettings): Configuration for limited-cycle
            subscriptions (Univapay side).
        first_charge_authorization_only (bool): If true, the first charge will only
            be an authorization (Hold).
        first_charge_capture_after (str): ISO-8601 Duration for auto-capture if
            authorization only is true.  Allowed days: P1D to P6D.
        metadata (GenericMetadata): A free-form dictionary for custom metadata.
        three_ds (ChargeCreateRequestThreeDs): Charge Create Request Three Ds schema.
            Either supply `mode` (and optionally `redirect_endpoint`) to have
            Univapay run 3DS, or supply all six external-MPI fields
            (`authentication_value` through `transaction_status`) when 3DS
            authentication was already completed outside of Univapay — in that case
            `mode` is set to `provided` automatically and must not be sent.
        additional_properties (Dict[str, Any]): The additional properties for the
            model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "transaction_token_id": "transaction_token_id",
        "amount": "amount",
        "currency": "currency",
        "initial_amount": "initial_amount",
        "period": "period",
        "cyclical_period": "cyclical_period",
        "schedule_settings": "schedule_settings",
        "installment_plan": "installment_plan",
        "subscription_plan": "subscription_plan",
        "first_charge_authorization_only": "first_charge_authorization_only",
        "first_charge_capture_after": "first_charge_capture_after",
        "metadata": "metadata",
        "three_ds": "three_ds",
    }

    _optionals = [
        "initial_amount",
        "period",
        "cyclical_period",
        "schedule_settings",
        "installment_plan",
        "subscription_plan",
        "first_charge_authorization_only",
        "first_charge_capture_after",
        "metadata",
        "three_ds",
    ]

    def __init__(
        self,
        transaction_token_id=None,
        amount=None,
        currency=None,
        initial_amount=APIHelper.SKIP,
        period=APIHelper.SKIP,
        cyclical_period=APIHelper.SKIP,
        schedule_settings=APIHelper.SKIP,
        installment_plan=APIHelper.SKIP,
        subscription_plan=APIHelper.SKIP,
        first_charge_authorization_only=False,
        first_charge_capture_after=APIHelper.SKIP,
        metadata=APIHelper.SKIP,
        three_ds=APIHelper.SKIP,
        additional_properties=None):
        """Initialize a SubscriptionCreateRequest instance."""
        # Initialize members of the class
        self.transaction_token_id = transaction_token_id
        self.amount = amount
        self.currency = currency
        if initial_amount is not APIHelper.SKIP:
            self.initial_amount = initial_amount
        if period is not APIHelper.SKIP:
            self.period = period
        if cyclical_period is not APIHelper.SKIP:
            self.cyclical_period = cyclical_period
        if schedule_settings is not APIHelper.SKIP:
            self.schedule_settings = schedule_settings
        if installment_plan is not APIHelper.SKIP:
            self.installment_plan = installment_plan
        if subscription_plan is not APIHelper.SKIP:
            self.subscription_plan = subscription_plan
        self.first_charge_authorization_only = first_charge_authorization_only
        if first_charge_capture_after is not APIHelper.SKIP:
            self.first_charge_capture_after = first_charge_capture_after
        if metadata is not APIHelper.SKIP:
            self.metadata = metadata
        if three_ds is not APIHelper.SKIP:
            self.three_ds = three_ds

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
        transaction_token_id =\
            dictionary.get("transaction_token_id")\
            if dictionary.get("transaction_token_id")\
                else None
        amount =\
            dictionary.get("amount")\
            if dictionary.get("amount")\
                else None
        currency =\
            dictionary.get("currency")\
            if dictionary.get("currency")\
                else None
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
        schedule_settings =\
            SubscriptionScheduleSettings.from_dictionary(
                dictionary.get("schedule_settings"))\
                if "schedule_settings" in dictionary.keys()\
                else APIHelper.SKIP
        installment_plan =\
            SubscriptionInstallmentPlan.from_dictionary(
                dictionary.get("installment_plan"))\
                if "installment_plan" in dictionary.keys()\
                else APIHelper.SKIP
        subscription_plan =\
            SubscriptionPlanSettings.from_dictionary(
                dictionary.get("subscription_plan"))\
                if "subscription_plan" in dictionary.keys()\
                else APIHelper.SKIP
        first_charge_authorization_only =\
            dictionary.get("first_charge_authorization_only")\
            if dictionary.get("first_charge_authorization_only")\
                else False
        first_charge_capture_after =\
            dictionary.get("first_charge_capture_after")\
            if dictionary.get("first_charge_capture_after")\
                else APIHelper.SKIP
        metadata =\
            GenericMetadata.from_dictionary(
                dictionary.get("metadata"))\
                if "metadata" in dictionary.keys()\
                else APIHelper.SKIP
        three_ds =\
            ChargeCreateRequestThreeDs.from_dictionary(
                dictionary.get("three_ds"))\
                if "three_ds" in dictionary.keys()\
                else APIHelper.SKIP

        additional_properties = APIHelper.get_additional_properties(
            dictionary={k: v for k, v in dictionary.items()
                        if k not in cls._names.values()},
            unboxing_function=lambda value: value)

        # Return an object of this model
        return cls(transaction_token_id,
                   amount,
                   currency,
                   initial_amount,
                   period,
                   cyclical_period,
                   schedule_settings,
                   installment_plan,
                   subscription_plan,
                   first_charge_authorization_only,
                   first_charge_capture_after,
                   metadata,
                   three_ds,
                   additional_properties)

    def __repr__(self):
        """Return a unambiguous string representation."""
        _transaction_token_id=self.transaction_token_id
        _amount=self.amount
        _currency=self.currency
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
        _schedule_settings=(
            self.schedule_settings
            if hasattr(self, "schedule_settings")
            else None
        )
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
        _first_charge_authorization_only=(
            self.first_charge_authorization_only
            if hasattr(self, "first_charge_authorization_only")
            else None
        )
        _first_charge_capture_after=(
            self.first_charge_capture_after
            if hasattr(self, "first_charge_capture_after")
            else None
        )
        _metadata=(
            self.metadata
            if hasattr(self, "metadata")
            else None
        )
        _three_ds=(
            self.three_ds
            if hasattr(self, "three_ds")
            else None
        )
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"transaction_token_id={_transaction_token_id!r}, "
            f"amount={_amount!r}, "
            f"currency={_currency!r}, "
            f"initial_amount={_initial_amount!r}, "
            f"period={_period!r}, "
            f"cyclical_period={_cyclical_period!r}, "
            f"schedule_settings={_schedule_settings!r}, "
            f"installment_plan={_installment_plan!r}, "
            f"subscription_plan={_subscription_plan!r}, "
            f"first_charge_authorization_only={_first_charge_authorization_only!r}, "
            f"first_charge_capture_after={_first_charge_capture_after!r}, "
            f"metadata={_metadata!r}, "
            f"three_ds={_three_ds!r}, "
            f"additional_properties={_additional_properties!r}, "
            f")"
        )

    def __str__(self):
        """Return a human-readable string representation."""
        _transaction_token_id=self.transaction_token_id
        _amount=self.amount
        _currency=self.currency
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
        _schedule_settings=(
            self.schedule_settings
            if hasattr(self, "schedule_settings")
            else None
        )
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
        _first_charge_authorization_only=(
            self.first_charge_authorization_only
            if hasattr(self, "first_charge_authorization_only")
            else None
        )
        _first_charge_capture_after=(
            self.first_charge_capture_after
            if hasattr(self, "first_charge_capture_after")
            else None
        )
        _metadata=(
            self.metadata
            if hasattr(self, "metadata")
            else None
        )
        _three_ds=(
            self.three_ds
            if hasattr(self, "three_ds")
            else None
        )
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"transaction_token_id={_transaction_token_id!s}, "
            f"amount={_amount!s}, "
            f"currency={_currency!s}, "
            f"initial_amount={_initial_amount!s}, "
            f"period={_period!s}, "
            f"cyclical_period={_cyclical_period!s}, "
            f"schedule_settings={_schedule_settings!s}, "
            f"installment_plan={_installment_plan!s}, "
            f"subscription_plan={_subscription_plan!s}, "
            f"first_charge_authorization_only={_first_charge_authorization_only!s}, "
            f"first_charge_capture_after={_first_charge_capture_after!s}, "
            f"metadata={_metadata!s}, "
            f"three_ds={_three_ds!s}, "
            f"additional_properties={_additional_properties!s}, "
            f")"
        )
