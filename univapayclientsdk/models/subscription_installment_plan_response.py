"""univapay_client_sdk.

This file was automatically generated for Univapay by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

# ruff: noqa: E501
from univapayclientsdk.api_helper import APIHelper


class SubscriptionInstallmentPlanResponse(object):
    """Implementation of the 'SubscriptionInstallmentPlanResponse' model.

    Installment plan applied to the subscription, as returned by the API. Covers both
    card-network installment plans (`revolving`, `fixed_cycles`) and legacy
    fixed-amount installment plans (`fixed_cycle_amount`).

    Attributes:
        plan_type (CombinedPlanType): Plan type selector.
        fixed_cycles (CombinedInstallmentFixedCycles): Number of installment cycles.
            Present when plan_type is fixed_cycles.
        fixed_cycles_amount (int): Total target amount for the fixed_cycle_amount
            plan type, in the smallest currency unit. Present when plan_type is
            fixed_cycle_amount. Note the plural `fixed_cycles_amount` key differs
            from `subscription_plan`'s singular `fixed_cycle_amount`.
        additional_properties (Dict[str, Any]): The additional properties for the
            model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "plan_type": "plan_type",
        "fixed_cycles": "fixed_cycles",
        "fixed_cycles_amount": "fixed_cycles_amount",
    }

    _optionals = [
        "plan_type",
        "fixed_cycles",
        "fixed_cycles_amount",
    ]

    _nullables = [
        "fixed_cycles",
        "fixed_cycles_amount",
    ]

    def __init__(
        self,
        plan_type=APIHelper.SKIP,
        fixed_cycles=APIHelper.SKIP,
        fixed_cycles_amount=APIHelper.SKIP,
        additional_properties=None):
        """Initialize a SubscriptionInstallmentPlanResponse instance."""
        # Initialize members of the class
        if plan_type is not APIHelper.SKIP:
            self.plan_type = plan_type
        if fixed_cycles is not APIHelper.SKIP:
            self.fixed_cycles = fixed_cycles
        if fixed_cycles_amount is not APIHelper.SKIP:
            self.fixed_cycles_amount = fixed_cycles_amount

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
        plan_type =\
            dictionary.get("plan_type")\
            if dictionary.get("plan_type")\
                else APIHelper.SKIP
        fixed_cycles =\
            dictionary.get("fixed_cycles")\
            if "fixed_cycles" in dictionary.keys()\
                else APIHelper.SKIP
        fixed_cycles_amount =\
            dictionary.get("fixed_cycles_amount")\
            if "fixed_cycles_amount" in dictionary.keys()\
                else APIHelper.SKIP

        additional_properties = APIHelper.get_additional_properties(
            dictionary={k: v for k, v in dictionary.items()
                        if k not in cls._names.values()},
            unboxing_function=lambda value: value)

        # Return an object of this model
        return cls(plan_type,
                   fixed_cycles,
                   fixed_cycles_amount,
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
        _plan_type=(
            self.plan_type
            if hasattr(self, "plan_type")
            else None
        )
        _fixed_cycles=(
            self.fixed_cycles
            if hasattr(self, "fixed_cycles")
            else None
        )
        _fixed_cycles_amount=(
            self.fixed_cycles_amount
            if hasattr(self, "fixed_cycles_amount")
            else None
        )
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"plan_type={_plan_type!r}, "
            f"fixed_cycles={_fixed_cycles!r}, "
            f"fixed_cycles_amount={_fixed_cycles_amount!r}, "
            f"additional_properties={_additional_properties!r}, "
            f")"
        )

    def __str__(self):
        """Return a human-readable string representation."""
        _plan_type=(
            self.plan_type
            if hasattr(self, "plan_type")
            else None
        )
        _fixed_cycles=(
            self.fixed_cycles
            if hasattr(self, "fixed_cycles")
            else None
        )
        _fixed_cycles_amount=(
            self.fixed_cycles_amount
            if hasattr(self, "fixed_cycles_amount")
            else None
        )
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"plan_type={_plan_type!s}, "
            f"fixed_cycles={_fixed_cycles!s}, "
            f"fixed_cycles_amount={_fixed_cycles_amount!s}, "
            f"additional_properties={_additional_properties!s}, "
            f")"
        )
