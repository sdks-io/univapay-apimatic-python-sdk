"""univapay_client_sdk.

This file was automatically generated for Univapay by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

# ruff: noqa: E501
from univapayclientsdk.api_helper import APIHelper


class SubscriptionSimulationPlanSettings(object):
    """Implementation of the 'SubscriptionSimulationPlanSettings' model.

    Cycle-limiting plan configuration used to simulate an installment plan or a
    Univapay-side subscription plan.

    Attributes:
        plan_type (SimulationPlanSettingsType): Plan type selector.
        fixed_cycles (int): Number of cycles for the fixed_cycles plan. Must be
            greater than 1.
        fixed_cycle_amount (int): Total target amount for the fixed_cycle_amount
            plan. Must not exceed the requested amount.
        additional_properties (Dict[str, Any]): The additional properties for the
            model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "plan_type": "plan_type",
        "fixed_cycles": "fixed_cycles",
        "fixed_cycle_amount": "fixed_cycle_amount",
    }

    _optionals = [
        "plan_type",
        "fixed_cycles",
        "fixed_cycle_amount",
    ]

    def __init__(
        self,
        plan_type=APIHelper.SKIP,
        fixed_cycles=APIHelper.SKIP,
        fixed_cycle_amount=APIHelper.SKIP,
        additional_properties=None):
        """Initialize a SubscriptionSimulationPlanSettings instance."""
        # Initialize members of the class
        if plan_type is not APIHelper.SKIP:
            self.plan_type = plan_type
        if fixed_cycles is not APIHelper.SKIP:
            self.fixed_cycles = fixed_cycles
        if fixed_cycle_amount is not APIHelper.SKIP:
            self.fixed_cycle_amount = fixed_cycle_amount

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
            if dictionary.get("fixed_cycles")\
                else APIHelper.SKIP
        fixed_cycle_amount =\
            dictionary.get("fixed_cycle_amount")\
            if dictionary.get("fixed_cycle_amount")\
                else APIHelper.SKIP

        additional_properties = APIHelper.get_additional_properties(
            dictionary={k: v for k, v in dictionary.items()
                        if k not in cls._names.values()},
            unboxing_function=lambda value: value)

        # Return an object of this model
        return cls(plan_type,
                   fixed_cycles,
                   fixed_cycle_amount,
                   additional_properties)

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
        _fixed_cycle_amount=(
            self.fixed_cycle_amount
            if hasattr(self, "fixed_cycle_amount")
            else None
        )
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"plan_type={_plan_type!r}, "
            f"fixed_cycles={_fixed_cycles!r}, "
            f"fixed_cycle_amount={_fixed_cycle_amount!r}, "
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
        _fixed_cycle_amount=(
            self.fixed_cycle_amount
            if hasattr(self, "fixed_cycle_amount")
            else None
        )
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"plan_type={_plan_type!s}, "
            f"fixed_cycles={_fixed_cycles!s}, "
            f"fixed_cycle_amount={_fixed_cycle_amount!s}, "
            f"additional_properties={_additional_properties!s}, "
            f")"
        )
