"""univapay_client_sdk.

This file was automatically generated for Univapay by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

# ruff: noqa: E501

class SimulationPlanSettingsType(object):
    """Implementation of the 'SimulationPlanSettingsType' enum.

    Plan type selector.

    Attributes:
        REVOLVING: The enum member of type str.
        FIXED_CYCLES: The enum member of type str.
        FIXED_CYCLE_AMOUNT: The enum member of type str.

    """

    REVOLVING = "revolving"

    FIXED_CYCLES = "fixed_cycles"

    FIXED_CYCLE_AMOUNT = "fixed_cycle_amount"

    @classmethod
    def from_value(cls, value, default=None):
        """Return the matching enum value for the given input."""
        if value is None:
            return default

        # If numeric and matches directly
        if isinstance(value, int):
            for name, val in cls.__dict__.items():
                if not name.startswith("_") and val == value:
                    return val

        # If string, perform case-insensitive match
        if isinstance(value, str):
            value_lower = value.lower()
            for name, val in cls.__dict__.items():
                if not name.startswith("_") and (
                    name.lower() == value_lower or str(val).lower() == value_lower
                ):
                    return val

        # Fallback to default
        return default
