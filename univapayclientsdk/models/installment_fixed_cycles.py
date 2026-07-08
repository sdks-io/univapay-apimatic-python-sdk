"""univapay_client_sdk.

This file was automatically generated for Univapay by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

# ruff: noqa: E501

class InstallmentFixedCycles(object):
    """Implementation of the 'InstallmentFixedCycles' enum.

    Required if plan_type is fixed_cycles.

    Attributes:
        CYCLES_3: 3 cycles
        CYCLES_5: 5 cycles
        CYCLES_6: 6 cycles
        CYCLES_10: 10 cycles
        CYCLES_12: 12 cycles
        CYCLES_15: 15 cycles
        CYCLES_18: 18 cycles
        CYCLES_20: 20 cycles
        CYCLES_24: 24 cycles

    """

    CYCLES_3 = 3

    CYCLES_5 = 5

    CYCLES_6 = 6

    CYCLES_10 = 10

    CYCLES_12 = 12

    CYCLES_15 = 15

    CYCLES_18 = 18

    CYCLES_20 = 20

    CYCLES_24 = 24

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
